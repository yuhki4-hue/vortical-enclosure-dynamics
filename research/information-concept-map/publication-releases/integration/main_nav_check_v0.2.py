#!/usr/bin/env python3
"""Static checks for navigation v0.2 on the main branch (read-only; Python 3 standard library only).
Usage: python3 main_nav_check_v0.2.py [edge_type_registry.tsv]
The registry lives only in the local research tree; without it, M-4 checks the built-in term list below
(copied from edge_type_registry_v0.2.tsv, column edge_type)."""
import csv, hashlib, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); PR = os.path.dirname(HERE); RC = os.path.join(PR, 'four-bridge-rc1')
TERMS = ['requires-condition', 'requires-field', 'may-satisfy', 'may-fill', 'references', 'parallel-axis-to', 'contrasts-with', 'member-of',
         'overlaps-with', 'strengthens', 'foregrounds', 'operationalizes', 'presupposes', 'redescribes', 'denies', 'defines', 'constitutes', 'silent',
         'unaudited', 'function-embedded-under', 'link-out-to', 'cross-linguistic-bridge-ref', 'alternative-of']
if len(sys.argv) > 1: TERMS = [r['edge_type'] for r in csv.DictReader(open(sys.argv[1], encoding='utf-8'), delimiter='\t')]
R = []
def rec(i, res, ev): R.append(dict(check=i, result=res, evidence=ev)); print(f'{i} | {res} | {ev}')
NAV = ('README_main_v0.2.md', 'index_main_v0.2.html')
txt = {f: open(os.path.join(PR, f), encoding='utf-8').read() for f in NAV}
links = []
for f, t in txt.items():
    for h in re.findall(r'\]\(([^)#]+)\)', t) + re.findall(r'href="([^"#]+)"', t):
        if not re.match(r'^[a-z]+:', h): links.append((f, h, os.path.exists(os.path.normpath(os.path.join(PR, h)))))
miss = [(f, h) for f, h, ok in links if not ok]
rec('M-1 all relative links in navigation v0.2 resolve on main', 'PASS' if links and not miss else 'FAIL', f'{len(links)} links; missing={miss}')
rec('M-2 RC1 entry link', 'PASS' if any(h == 'four-bridge-rc1/renderer/index.html' and ok for f, h, ok in links) else 'FAIL', 'four-bridge-rc1/renderer/index.html')
loc = 'cross-linguistic-audit/br3-012-publication-prototype/' in txt['index_main_v0.2.html'] and 'data-local-only="br3-012"' in txt['index_main_v0.2.html']
nolink = not any('cross-linguistic-audit' in h for f, h, ok in links)
rec('M-3 BR3-012 named as local-only, not linked', 'PASS' if loc and nolink else 'FAIL', f'local path stated={loc}; no link into cross-linguistic-audit={nolink}')
nav = ''.join(txt.values()); hits = [t for t in TERMS if re.search(r'\b' + re.escape(t) + r'\b', nav)]
dis = all('do not add, change or imply any' in t for t in txt.values())
rec('M-4 navigation is not an edge', 'PASS' if not hits and dis else 'FAIL', f'edge-type terms found={hits}; disclaimer in both files={dis}')
pos = [x for x in re.findall(r'[^.\n]*\b(?:deployed|published)\b[^.\n]*', nav, re.I) if not re.search(r'NOT-DEPLOYED|not (?:be )?(?:deployed|published)|no(?:thing)?[^.]*(?:deployed|published)|has not|not a publication|never', x, re.I)]
rec('M-5 NOT-DEPLOYED, not reported as published', 'PASS' if all('NOT-DEPLOYED' in t for t in txt.values()) and not pos else 'FAIL', f'un-negated statements={pos}')
m = list(csv.DictReader(open(os.path.join(RC, 'RELEASE_MANIFEST.tsv'), encoding='utf-8'), delimiter='\t'))
bad = [r['path'] for r in m if hashlib.sha256(open(os.path.join(RC, r['path']), 'rb').read()).hexdigest() != r['sha256']]
rec('M-6 RC1 = frozen manifest', 'PASS' if len(m) == 36 and not bad else 'FAIL', f'{len(m)} entries; mismatched={bad}')
src = os.path.join(PR, '..', '..', '..', 'figure2b', 'data.js'); h = hashlib.sha256(open(src, 'rb').read()).hexdigest() if os.path.exists(src) else None
rec('M-7 source authority figure2b/data.js present and as recorded', 'PASS' if h and h.startswith('734d15119fa1c7f4') else 'FAIL', f'sha256={h}')
v01 = [h for f, h, ok in links if h in ('index.html', 'README.md')]
rec('M-8 navigation v0.1 kept and pointed to, not altered', 'PASS' if v01 else 'FAIL', f'v0.2 links to v0.1: {sorted(set(v01))} (v0.1 file content is checked by git diff: no M lines)')
json.dump(R, open(os.path.join(HERE, 'main_nav_check_v0.2_results.json'), 'w'), ensure_ascii=False, indent=1)
