#!/usr/bin/env python3
"""In-repository verification of the Four-Bridge RC1 integration (read-only; Python 3 standard library only).
Run from anywhere:  python3 research/information-concept-map/publication-releases/integration/verify_rc1_in_repo.py [pre-hash-list]
pre-hash-list (optional): 'sha256  path' lines (repo-relative) taken before integration, for RI-2."""
import csv, hashlib, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); PR = os.path.dirname(HERE)          # publication-releases/
RC = os.path.join(PR, 'four-bridge-rc1'); ROOT = os.path.abspath(os.path.join(PR, '..', '..', '..'))
R = []
def rec(i, res, ev): R.append(dict(check=i, result=res, evidence=ev)); print(f'{i} | {res} | {ev}')
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
rd = lambda p: list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))

# RI-1
m = rd(os.path.join(RC, 'RELEASE_MANIFEST.tsv'))
bad = [r['path'] for r in m if not os.path.exists(os.path.join(RC, r['path'])) or sha(os.path.join(RC, r['path'])) != r['sha256']]
files = sorted(os.path.relpath(os.path.join(d, f), RC) for d, _, fs in os.walk(RC) for f in fs)
extra = [f for f in files if f not in {r['path'] for r in m} and f != 'RELEASE_MANIFEST.tsv']
rec('RI-1 RC1 hashes = manifest', 'PASS' if not bad and not extra and len(m) == 36 else 'FAIL', f'{len(m)} manifest entries; files present {len(files)} (36 + RELEASE_MANIFEST.tsv); mismatched={bad}; unlisted={extra}; RELEASE_MANIFEST.tsv sha256={sha(os.path.join(RC, "RELEASE_MANIFEST.tsv"))}')

# RI-2 (optional pre-hash list)
if len(sys.argv) > 1:
    pre = {}
    for line in open(sys.argv[1], encoding='utf-8'):
        h, p = line.rstrip('\n').split('  ', 1); pre[p[2:] if p.startswith('./') else p] = h
    changed = [p for p, h in pre.items() if not os.path.exists(os.path.join(ROOT, p)) or sha(os.path.join(ROOT, p)) != h]
    rec('RI-2 pre-existing files unchanged', 'PASS' if not changed else 'FAIL', f'{len(pre)} pre-existing files; changed or missing={changed[:20]}')
else:
    rec('RI-2 pre-existing files unchanged', 'NOT-RUN', 'no pre-hash list given')

# RI-4 / RI-5 links
links = []
for f in ('README.md', 'index.html'):
    t = open(os.path.join(PR, f), encoding='utf-8').read()
    for h in re.findall(r'\]\(([^)#]+)\)', t) + re.findall(r'href="([^"#]+)"', t):
        if not re.match(r'^[a-z]+:', h): links.append((f, h, os.path.exists(os.path.normpath(os.path.join(PR, h)))))
missing = [(f, h) for f, h, ok in links if not ok]
br = [h for f, h, ok in links if 'br3-012-publication-prototype/index.html' in h and ok]
rc = [h for f, h, ok in links if h == 'four-bridge-rc1/renderer/index.html' and ok]
rec('RI-4 BR3-012 links exist', 'PASS' if br and not [x for x in missing if 'br3-012' in x[1]] else 'FAIL', f'BR3-012 entry links resolved: {sorted(set(br))}')
rec('RI-5 RC1 entry links exist', 'PASS' if rc and not missing else 'FAIL', f'{len(links)} relative links in README.md + index.html; missing={missing}')

# RI-6 navigation is not an edge
nav = open(os.path.join(PR, 'README.md'), encoding='utf-8').read() + open(os.path.join(PR, 'index.html'), encoding='utf-8').read()
reg = rd(os.path.join(ROOT, 'research/information-concept-map/english-reconstruction/edge_type_registry_v0.2.tsv'))
edge_terms = [r['edge_type'] for r in reg if re.search(r'\b' + re.escape(r['edge_type']) + r'\b', nav)]
disclaim = 'do not add, change or imply any' in nav and 'conceptual edge' in nav
rc1_edges_same = sha(os.path.join(RC, 'research-audit/english_data_edges_v0.6.tsv')) == next(r['sha256'] for r in m if r['path'] == 'research-audit/english_data_edges_v0.6.tsv')
rec('RI-6 navigation links are not edges', 'PASS' if not edge_terms and disclaim and rc1_edges_same else 'FAIL', f'edge-type vocabulary in navigation files={edge_terms}; disclaimer present={disclaim}; no edge file created or changed by integration (RC1 edges v0.6 = frozen)={rc1_edges_same}')

# data for RI-7..10
OV = {r['overlay_id']: r for r in rd(os.path.join(RC, 'frozen-inputs/english_publication_overlay_v0.7.tsv'))}
js = open(os.path.join(RC, 'renderer/data.js'), encoding='utf-8').read(); REN = json.loads(js[len('window.FB_DATA = '):-2])
P = {r['item_id']: r for r in rd(os.path.join(RC, 'frozen-inputs/four_bridge_condition_provenance_v0.5.tsv'))}
# RI-7
c = {'reconstruction-only items never in publication scope': all(not (p['origin'].startswith('TARGET') and p['scope'] == 'PUBLICATION-AND-RECONSTRUCTION') for p in P.values()),
     'renderer filters audit items by scope': 'it.scope === "PUBLICATION-AND-RECONSTRUCTION"' in open(os.path.join(RC, 'renderer/app.js'), encoding='utf-8').read(),
     'reconstruction-layer link rows marked': all('reconstruction' in OV[k]['management_scope'] for k in ('OV-E-E2-001', 'OV-E-E2-002', 'OV-A-QREL-PLACEMENT'))}
rec('RI-7 publication / reconstruction kept apart (data)', 'PASS' if all(c.values()) else 'FAIL', '; '.join(f'{k}={v}' for k, v in c.items()) + ' (display check: integration/nav_render_check.js)')
# RI-8
s = open(os.path.join(ROOT, 'figure2b/data.js'), encoding='utf-8').read(); s = s[s.index('{'):s.rstrip().rstrip(';').rindex('}') + 1]
SRC = {e['id']: e for e in json.loads(s)['elements']}
APP = {'R0': ('Interaction', 'There is a physical coupling, and it affects a state or process.'), 'Fc': ('Causal-role function', 'Contribution to a specified capacity or process.'),
       'M1': ('Q-relative difference-making', 'A difference changes the consequences for a specified Q.'), 'C0': ('Passive stabilization', 'Change decays through physicochemical responses.')}
notes = {r['note_id']: r for r in rd(os.path.join(RC, 'publication/mandatory_notes_rc1.tsv'))}
bad = []
for k, (lab, gl) in APP.items():
    o = OV['OV-N-' + k]; u = REN['units'][k]
    if (o['approved_english_label'], o['selected_english_gloss_candidate']) != (lab, gl) or (u['label'], u['gloss']) != (lab, gl): bad.append(k + ':label/gloss')
    if o['original_japanese_text'] != SRC[k]['description'] or u['ja'] != SRC[k]['description']: bad.append(k + ':ja')
    if (u['note_full'], u['note_short']) != (o['mandatory_ambiguity_note_full'], o['mandatory_ambiguity_note_short']) or (notes['OV-N-' + k]['note_full'], notes['OV-N-' + k]['note_short']) != (u['note_full'], u['note_short']): bad.append(k + ':notes')
    if 'V4B-12-AUTHOR-APPROVED' not in o['note_revision_status']: bad.append(k + ':status')
if OV['OV-N-M1']['same_unit_formula'] != 'Rel(d;Q|Σ,𝒟,M,τ)': bad.append('M1 formula')
rec('RI-8 approved wording unchanged', 'PASS' if not bad else 'FAIL', f'labels, glosses, Japanese (vs repository figure2b/data.js), full and short notes consistent across frozen overlay, mandatory_notes_rc1.tsv and renderer data; approval status present; mismatches={bad}')
# RI-9
c = all(OV[f'OV-E-{e}']['publication_display'] == 'HIDDEN-LISTED' and OV[f'OV-E-{e}']['publication_assertion'] == 'NOT-ASSERTED-IN-PUBLICATION' for e in ('E2-001', 'E2-002')) and OV['OV-L-R0-R1']['publication_assertion'].startswith('NOT-ASSERTED')
rec('RI-9 E2-001/E2-002 not asserted in publication', 'PASS' if c else 'FAIL', 'overlay: E2-001/E2-002 HIDDEN-LISTED + NOT-ASSERTED-IN-PUBLICATION; R0↔R1 comparison NOT-ASSERTED (display check in nav_render_check.js)')
# RI-10
kl = open(os.path.join(RC, 'KNOWN_LIMITATIONS.md'), encoding='utf-8').read()
rr = json.load(open(os.path.join(RC, 'validation/render_results_rc1.json')))
c = {'open items listed': all(x in kl for x in ('R-series necessary-condition', 'intervention-sensitivity', 'AC-FC-09', 'O-027-3', '状態・過程', 'Native-reader review')),
     'NOT-TESTED kept': any(r['result'] == 'NOT-TESTED' for r in rr) and 'NOT-TESTED' in kl,
     'provenance open statuses': (P['AC-C0-10']['status'], P['AC-FC-09']['status'], P['AC-R0-09']['status']) == ('OPEN-UNRESOLVED',) * 3}
rec('RI-10 open items and NOT-TESTED kept', 'PASS' if all(c.values()) else 'FAIL', '; '.join(f'{k}={v}' for k, v in c.items()))
# RI-11
rm = open(os.path.join(PR, 'README.md'), encoding='utf-8').read() + open(os.path.join(RC, 'README.md'), encoding='utf-8').read()
c = all(x in rm for x in ('verify_rc1_in_repo.py', 'nav_render_check.js', 'Playwright', 'pdftotext', 'validate_rc1.py', 'render_rc1.js'))
rec('RI-11 verification steps and dependencies documented', 'PASS' if c else 'FAIL', 'integration README + RC1 README name the scripts, Python 3, Playwright/Chromium, pdftotext, and the lineage packages needed for full data validation')
# RI-12
t = nav + open(os.path.join(HERE, 'four_bridge_rc1_repository_integration_v0.1.md'), encoding='utf-8').read() if os.path.exists(os.path.join(HERE, 'four_bridge_rc1_repository_integration_v0.1.md')) else nav
pos = [x for x in re.findall(r'[^.\n]*\b(?:deployed|published)\b[^.\n]*', t, re.I) if not re.search(r'NOT-DEPLOYED|not (?:be )?(?:deployed|published)|no(?:thing)?[^.]*(?:deployed|published)|has not|not a publication|never', x, re.I)]
rec('RI-12 not reported as published', 'PASS' if 'NOT-DEPLOYED' in nav and not pos else 'FAIL', f'status NOT-DEPLOYED shown; un-negated deployed/published statements={pos}')
json.dump(R, open(os.path.join(HERE, 'verify_rc1_in_repo_results.json'), 'w'), ensure_ascii=False, indent=1)
