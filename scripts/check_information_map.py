#!/usr/bin/env python3
"""Offline checks for the imported series. No browser, network or dependencies."""
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
def check(condition, message):
    if not condition:
        errors.append(message)

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids = [], set()
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs: self.links.append(attrs[key])

provenance = json.loads((ROOT / 'sources/information-map/imports.json').read_text())
for item in provenance['imports']:
    if item.get('policy') == 'byte-exact':
        path = ROOT / item['destination']
        check(hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256'], 'Import drift: ' + str(path))
    for member, expected in item.get('members', {}).items():
        if member in ('figure1/index.html', 'figure2b/index.html', 'figure3/index.html', 'figure2b/data.js', 'figure2b/README.md', 'figure2b/AUDIT.md'):
            continue
        check(hashlib.sha256((ROOT / member).read_bytes()).hexdigest() == expected, 'Explorer source drift: ' + member)

historic_header_separator = '\n---\n\n'
for member in ('figure2b/README.md', 'figure2b/AUDIT.md'):
    expected = next(item['members'][member] for item in provenance['imports'] if member in item.get('members', {}))
    current = (ROOT / member).read_text()
    check(historic_header_separator in current, 'Missing current-integration header: ' + member)
    historic_body = current.split(historic_header_separator, 1)[1] if historic_header_separator in current else ''
    check(hashlib.sha256(historic_body.encode()).hexdigest() == expected, 'Historic body drift: ' + member)
    check('../docs/information-map.md' in current.split(historic_header_separator, 1)[0], 'Missing current integration link: ' + member)

audit = (ROOT / 'audits/information-map/figure-2-v4-audit.html').read_text()
embedded = re.findall(r'<svg\b[\s\S]*?</svg>', audit)
check(len(embedded) == 2, 'Expected two SVGs in combined audit')
for name, source in zip(('A', 'B'), embedded):
    standalone = ET.fromstring((ROOT / f'assets/information-map/figure-2{name}-v4.svg').read_bytes())
    embedded_svg = ET.fromstring(source.replace('chem' + name + '-', ''))
    check(ET.tostring(standalone) == ET.tostring(embedded_svg), 'Embedded SVG differs: ' + name)

raw_data = (ROOT / 'figure2b/data.js').read_text()
data = json.loads(raw_data.removeprefix('window.FIGURE_DATA = ').strip().removesuffix(';'))
chem = json.loads((ROOT / 'audits/information-map/chemotaxis-case-audit.json').read_text())
check(data['auditSources']['chemotaxis'] == chem, '3D chemotaxis audit differs from source')
integration_text = (ROOT / 'figure2b/integration-metadata.js').read_text()
integration_match = re.search(r'window\.FIGURE2B_INTEGRATION_METADATA = (\{[\s\S]*?\});', integration_text)
integration = json.loads(integration_match.group(1)) if integration_match else {}
chem_integration = integration.get('chemotaxis', {})
provenance_scope = chem_integration.get('provenance', {}).get('scope')
current_integration = chem_integration.get('currentIntegration', {})
check(provenance_scope == chem['scope'], 'Historical chemotaxis scope not preserved under provenance')
check(current_integration.get('status') == 'embedded', 'Current chemotaxis integration status')
check(current_integration.get('embeddedClaimCount') == len(chem['claims']) == 41, 'Current embedded chemotaxis claim count')
check(current_integration.get('sourceClaimCount') == len(chem['claims']), 'Current source chemotaxis claim count')
check(current_integration.get('checker') == 'scripts/check_information_map.py', 'Current integration checker locator')
check(current_integration.get('theoryValidation') is False, 'Current integration must not claim theory validation')
check(current_integration.get('browserValidation') is False, 'Current integration must not claim browser validation')
check('delete chemotaxis.scope;' in integration_text, 'Historical scope must not remain a current runtime integration field')
dna = json.loads((ROOT / 'audits/information-map/dna-case-audit.json').read_text())
check(data['auditSources']['dna'] == dna, 'Derived DNA audit differs from embedded source')
claims = next(x for x in data['elements'] if x['id'] == 'ex-bacteria')['auditClaims']
check(len(claims) == len(chem['claims']) == 41, 'Chemotaxis claim count')
for claim in chem['claims']:
    match = next((x for x in claims if x['id'] == claim['id']), {})
    check(all(match.get(k) == claim[k] for k in ('relation', 'status', 'evidenceKind')), 'Claim mismatch: ' + claim['id'])
    check(match.get('scope') == claim['sigmaId'] and match.get('caveat') == claim['caveats'], 'Scope/caveat mismatch: ' + claim['id'])
check(data['twoDConditionsUrl'] == '../figure2a/', '3D condition link not wired')

directories = ('figure1', 'figure2a', 'figure2b', 'figure3', 'information-map', 'audits/information-map')
pages = {p: Page(p.read_text()) for directory in directories for p in (ROOT / directory).rglob('*.html')}
local_count = 0
for path, page in pages.items():
    for link in page.links:
        u = urlsplit(link)
        if u.scheme or u.netloc: continue
        check(not u.path.startswith('/'), f'Base-path unsafe link: {path.relative_to(ROOT)} -> {link}')
        target = (path.parent / unquote(u.path)).resolve() if u.path else path
        if target.is_dir(): target = target / 'index.html'
        check(target.is_file(), f'Missing link: {path.relative_to(ROOT)} -> {link}')
        local_count += 1
        if u.fragment and '=' not in u.fragment and target.suffix == '.html' and target.is_file():
            target_page = pages.get(target) or Page(target.read_text())
            check(unquote(u.fragment) in target_page.ids, f'Missing anchor: {path.relative_to(ROOT)} -> {link}')
for directory in ('figure1', 'figure2a', 'figure2b', 'figure3', 'figure2b/audit'):
    text = (ROOT / directory / 'index.html').read_text()
    check('series.css' in text and 'series-nav' in text and 'series-pager' in text, 'Missing series navigation: ' + directory)
for css in [ROOT / 'assets/information-map/series.css', ROOT / 'figure2b/style.css', ROOT / 'figure2b/mobile.css']:
    for ref in re.findall(r'url\(["\']?([^\)"\']+)', css.read_text()):
        if not urlsplit(ref).scheme:
            check((css.parent / ref).is_file(), 'Missing CSS resource: ' + ref)
print(f'Checked {len(pages)} HTML pages, {local_count} local references, source hashes, embedded SVGs, integration metadata and 41 chemotaxis claims.')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('PASS')
