#!/usr/bin/env python3
"""Four-Bridge Publication RC1 — data and source-faithful validation (read-only).
Usage: python3 -I validate_rc1.py <rc1 dir> <outputs dir (lineage packages)> <v0.7 package dir> <staged repo root>
String checks and semantic checks are reported in separate columns."""
import csv, hashlib, json, os, re, sys, zipfile
RC, B, V7, REPO = sys.argv[1:5]
R = []
def rec(i, string, semantic, basis):
    R.append(dict(check=i, string_check=string, semantic_check=semantic, basis=basis)); print(f'{i} | string={string} | semantic={semantic} | {basis[:300]}')
def rd(p): return list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))
def ov(p): return {r['overlay_id']: r for r in rd(p)}
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
P = lambda *a: os.path.join(*a)
F, S = 'mandatory_ambiguity_note_full', 'mandatory_ambiguity_note_short'
OV = ov(P(RC, 'frozen-inputs/english_publication_overlay_v0.7.tsv'))
PROV = {r['item_id']: r for r in rd(P(RC, 'frozen-inputs/four_bridge_condition_provenance_v0.5.tsv'))}
DEC = {r['decision_id']: r for r in rd(P(RC, 'frozen-inputs/four_bridge_hr_impl_v0.14_decisions.tsv'))}
D7 = {r['target_id']: r for r in rd(P(V7, 'english_data_draft_v0.7.tsv'))}; D8 = {r['target_id']: r for r in rd(P(RC, 'research-audit/english_data_draft_v0.8.tsv'))}
E5 = {r['edge_id']: r for r in rd(P(V7, 'english_data_edges_v0.5.tsv'))}; E6 = {r['edge_id']: r for r in rd(P(RC, 'research-audit/english_data_edges_v0.6.tsv'))}
E4 = {r['edge_id']: r for r in rd(P(REPO, 'research/information-concept-map/english-reconstruction/english_data_edges_v0.4.tsv'))}
PUB = json.load(open(P(RC, 'publication/publication_data_rc1.json'), encoding='utf-8'))
js = open(P(RC, 'renderer/data.js'), encoding='utf-8').read(); REN = json.loads(js[len('window.FB_DATA = '):-2])
s = open(P(REPO, 'figure2b/data.js'), encoding='utf-8').read(); s = s[s.index('{'):s.rstrip().rstrip(';').rindex('}') + 1]
SRC = {e['id']: e for e in json.loads(s)['elements']}
REND = json.load(open(P(RC, 'validation/render_results_rc1.json'))) if os.path.exists(P(RC, 'validation/render_results_rc1.json')) else []
K = ['R0', 'Fc', 'M1', 'C0']; TID = {'R0': 'EN-ICM-0054', 'Fc': 'EN-ICM-0019', 'M1': 'EN-ICM-0053', 'C0': 'EN-ICM-0007'}
rp = lambda prefix: all(r['result'] == 'PASS' for r in REND if r['id'].startswith(prefix)) and any(r['id'].startswith(prefix) for r in REND)

# SF-1 Japanese
bad = []
for k in K:
    u = OV['OV-N-' + k]
    if u['original_japanese_text'] != SRC[k]['description'] or u['original_japanese_label'] != SRC[k]['label'].split('｜')[1]: bad.append(k)
    if PUB['units'][k]['ja'] != SRC[k]['description'] or REN['units'][k]['ja'] != SRC[k]['description']: bad.append(k + ':pub/render')
r4 = SRC['R4']['description']
if OV['OV-N-R4']['original_japanese_text'] != r4: bad.append('R4')
for oid, suf in (('OV-N-R4-SYS', ' (source of BR3-012)'), ('OV-N-R4-COMB', ' (source of BR3-013)')):
    if OV[oid]['original_japanese_text'] != r4 + suf: bad.append(oid)
rec('SF-1 Japanese original', 'PASS' if not bad else 'FAIL', 'N/A (exact identity suffices)', f'4 units: description and label = figure2b/data.js in overlay v0.7, publication data and renderer data; BR3-012: R4 text = data.js R4; R4-SYS/R4-COMB = R4 text + the existing provenance suffix; mismatches={bad}')

# SF-2 labels and glosses
want = {}
for d in ('H-BR3-008-PUB-LABEL-GLOSS-A', 'H-BR3-023-PUB-LABEL-GLOSS-A', 'H-BR3-044-PUB-LABEL-GLOSS-B', 'H-BR3-027-PUB-LABEL-GLOSS-B'):
    m = re.match(r'Label: (.+?)\. Gloss: (.+?\.)', DEC[d]['decision']); want[d] = m.groups()
mp = {'R0': 'H-BR3-008-PUB-LABEL-GLOSS-A', 'Fc': 'H-BR3-023-PUB-LABEL-GLOSS-A', 'M1': 'H-BR3-044-PUB-LABEL-GLOSS-B', 'C0': 'H-BR3-027-PUB-LABEL-GLOSS-B'}
bad = [k for k in K if (OV['OV-N-' + k]['approved_english_label'], OV['OV-N-' + k]['selected_english_gloss_candidate']) != want[mp[k]] or (PUB['units'][k]['label'], PUB['units'][k]['gloss']) != want[mp[k]]]
a_wording = re.search(r'HR-2: wording A "(.+?)"', DEC['H-BR3-012-HR-PUBLICATION']['decision']).group(1)
if OV['OV-N-R4']['selected_english_gloss_candidate'] != a_wording: bad.append('R4 wording A')
rec('SF-2 approved labels and glosses', 'PASS' if not bad else 'FAIL', 'N/A', f'compared with the decision-log texts (label/gloss decisions; BR3-012 wording A); mismatches={bad}')

# SF-3 notes
O4 = ov(P(B, 'four_bridge_hr_impl_v0.8/english_publication_overlay_v0.4.tsv')); O5 = ov(P(B, 'four_bridge_hr_impl_v0.10/english_publication_overlay_v0.5.tsv')); O6 = ov(P(B, 'four_bridge_hr_impl_v0.11/english_publication_overlay_v0.6.tsv'))
m1s = re.search(r'Approved short note: “(.+?)”', DEC['H-V4B-12-M1-B']['decision']).group(1)
APP = {'OV-N-R0': (O4['OV-N-R0'][F], O4['OV-N-R0'][S]), 'OV-N-Fc': (O5['OV-N-Fc'][F], O5['OV-N-Fc'][S]), 'OV-N-M1': (O4['OV-N-M1'][F], m1s),
       'OV-N-C0': (O6['OV-N-C0'][F], O6['OV-N-C0'][S]), 'OV-NOTE-INTERVENTION': (O6['OV-NOTE-INTERVENTION'][F], O6['OV-NOTE-INTERVENTION'][S])}
c0d = re.search(r'Full note: “(.+?)” Short note: “(.+?)”', DEC['H-V4B-12-C0-A']['decision']).groups(); ind = re.search(r'Full note: “(.+?)” Short note: “(.+?)”', DEC['H-V4B-12-INTERVENTION-A']['decision']).groups()
bad = [k for k, (f, s_) in APP.items() if (OV[k][F], OV[k][S]) != (f, s_)]
bad += [] if c0d == APP['OV-N-C0'] else ['C0 vs log text']; bad += [] if ind == APP['OV-NOTE-INTERVENTION'] else ['shared vs log text']
notes = {r['note_id']: r for r in rd(P(RC, 'publication/mandatory_notes_rc1.tsv'))}
bad += [k for k in APP if (notes[k]['note_full'], notes[k]['note_short']) != APP[k]]
bad += [k for k in K if (REN['units'][k]['note_full'], REN['units'][k]['note_short']) != APP['OV-N-' + k]] + ([] if (REN['shared_note']['full'], REN['shared_note']['short']) == APP['OV-NOTE-INTERVENTION'] else ['render shared'])
rec('SF-3 V4B-12 approved notes', 'PASS' if not bad else 'FAIL', 'ANALYST-CONSISTENT (each note’s content checked against its approving decision in V4B-12 records v0.10–v0.14; no new reading)',
    f'5 units × (overlay v0.7, mandatory_notes_rc1.tsv, renderer data) = approved texts (R0: overlay v0.4; Fc: v0.5; M1: v0.4 full + log short; C0 and shared: v0.6 = text quoted in the log); mismatches={bad}')

# SF-4 M1 coordinates and formula
m = OV['OV-N-M1']
c = [m['same_unit_formula'] == 'Rel(d;Q|Σ,𝒟,M,τ)', 'Rel(d;Q|Σ,𝒟,M,τ)' in m['original_japanese_text'], all(x in m[F] for x in ('Σ', '𝒟', 'mechanism M', 'τ')),
     all(x in m[S] for x in ('Σ, 𝒟, M, τ', 'M = mechanism')), re.search(r'Σ.*𝒟.*M.*τ', D8['EN-ICM-0053']['constitutive_conditions']) is not None, REN['units']['M1']['formula'] == 'Rel(d;Q|Σ,𝒟,M,τ)']
rec('SF-4 M1 coordinates and formula', 'PASS' if all(c) else 'FAIL', 'ANALYST-CONSISTENT (coordinates remain constraints of the relation: “a change in any of these is a different claim”)', f'formula in overlay, Japanese text and renderer; coordinates in full/short notes and in publication constitutive conditions: {c}; same render unit verified by the render check: {rp("C-M1-FORMULA")}')

# SF-5 intervention not projected
cc = {k: D8[TID[k]]['constitutive_conditions'] for k in ('R0', 'Fc', 'M1')}
c = {'CC free of intervention': not any(re.search('interven', v, re.I) for v in cc.values()),
     'R0 note': 'not written into the definition' in OV['OV-N-R0'][F] and 'not part of the Japanese R0 definition' in OV['OV-N-R0'][F],
     'Fc note': 'it is not a condition of the Japanese Fc' in OV['OV-N-Fc'][F],
     'M1 short': 'not part of the Japanese definition' in OV['OV-N-M1'][S],
     'shared note scope': OV['OV-NOTE-INTERVENTION'][F].startswith('Intervention. In the source-faithful publication layer'),
     'reconstruction items scoped': all(PROV[i]['scope'] == 'RECONSTRUCTION-ONLY' for i in ('AC-R0-05', 'AC-M1-14', 'AC-FC-11'))}
rec('SF-5 no back-projection of intervention', 'PASS' if all(c.values()) else 'FAIL', 'ANALYST-CONSISTENT (intervention kept as source-map audit question / assessment route; D-H4 and conditional proposals reconstruction-only)', '; '.join(f'{k}={v}' for k, v in c.items()))

# SF-6 C0 pathways
c = {'CC': not re.search('pathway|identif|sensing', D8['EN-ICM-0007']['constitutive_conditions'], re.I),
     'note': all(x in OV['OV-N-C0'][F] for x in ("does not require that the system has no sensing or action pathways", 'cannot be told apart', 'have not been identified')),
     'AC-C0-11 not effective': (PROV['AC-C0-11']['scope'], PROV['AC-C0-11']['status']) == ('LEGACY-RECORD-ONLY', 'NOT-EFFECTIVE'),
     'AC-C0-02..04 audit questions': all(PROV[i]['role'] == 'AUDIT-QUESTION' for i in ('AC-C0-02', 'AC-C0-03', 'AC-C0-04'))}
rec('SF-6 C0 pathway conditions not required', 'PASS' if all(c.values()) else 'FAIL', 'ANALYST-CONSISTENT (absence, inseparability and non-identification are each excluded as requirements; O-027-3 open)', '; '.join(f'{k}={v}' for k, v in c.items()))

# SF-7 R0↔R1
c = {'E2-001/002 hidden + not asserted': all(OV[f'OV-E-{e}']['publication_display'] == 'HIDDEN-LISTED' and OV[f'OV-E-{e}']['publication_assertion'] == 'NOT-ASSERTED-IN-PUBLICATION' for e in ('E2-001', 'E2-002')),
     'R0↔R1 link not asserted': OV['OV-L-R0-R1']['publication_assertion'].startswith('NOT-ASSERTED'),
     'R0 note neither establishes nor denies': 'neither establishes nor denies that R1 requires R0' in OV['OV-N-R0'][F],
     'render: not drawn in publication layer': rp('C-LAYER')}
rec('SF-7 R0↔R1 not asserted in publication', 'PASS' if all(c.values()) else 'FAIL', 'ANALYST-CONSISTENT', '; '.join(f'{k}={v}' for k, v in c.items()))

# SF-8 separation
viol = [i for i, p in PROV.items() if p['origin'].startswith('TARGET') and p['scope'] == 'PUBLICATION-AND-RECONSTRUCTION']
viol += [i for i, p in PROV.items() if p['origin'] == 'SOURCE-AUDIT-QUESTION' and p['role'] == 'PUBLICATION-CONSTITUTIVE']
viol += [f'{t}:{i}' for t in TID.values() for i in (D8[t].get('reconstruction_condition_refs') or '').split(';') if i and PROV[i]['scope'] != 'RECONSTRUCTION-ONLY']
viol += [f'{t}:CC-changed' for t in TID.values() if D8[t]['constitutive_conditions'] != D7[t]['constitutive_conditions'] or D8[t]['reconstruction_conditions'] != D7[t]['reconstruction_conditions']]
rec('SF-8 separation of reconstruction / audit / publication conditions', 'PASS' if not viol else 'FAIL', 'ANALYST-CONSISTENT', f'no TARGET-origin item in publication scope; no audit question promoted; reconstruction_condition_refs all RECONSTRUCTION-ONLY; constitutive and reconstruction columns unchanged v0.7→v0.8; violations={viol}')

# SF-9 provenance = display
bad = []
for t in TID.values():
    for m_ in re.finditer(r'\[(AC-[A-Z0-9]+-\d\d)\] ([^\[]*?)(?=; \[|$)', D8[t]['audit_conditions']):
        if PROV[m_.group(1)]['item_text'] != m_.group(2): bad.append('draft:' + m_.group(1))
for k in K:
    for it in REN['units'][k]['items']:
        if {x: PROV[it['item_id']][x] for x in it} != it: bad.append('render:' + it['item_id'])
st = all('V4B-12-AUTHOR-APPROVED' in OV[k]['note_revision_status'] for k in APP)
rec('SF-9 provenance = display state', 'PASS' if not bad and st else 'FAIL', 'ANALYST-CONSISTENT (AC-R0-06 current reconstruction label; AC-FC-06 componenthood not required — both match the notes)', f'draft v0.8 audit_conditions item texts = provenance v0.5; renderer items = provenance v0.5; overlay approval statuses = V4B-12-AUTHOR-APPROVED for all 5 notes: {st}; mismatches={bad}')

# RC1-01
lg = ['source_target_id', 'target_target_id_or_field', 'edge_type', 'edge_sense', 'scope', 'condition', 'status', 'edge_assertion_status', 'evidence_status', 'tradition_id', 'slot', 'edge_type_v02', 'edge_sense_v02']
diffs = {e: [k for k in E5[e] if E5[e][k] != E6[e][k]] for e in E5}
diffs = {e: v for e, v in diffs.items() if v}
c = {'only E2-001 changed': list(diffs) == ['E2-001'] and set(diffs['E2-001']) == {'target_short_name', 'display_name_source'},
     'logic fields = v0.5 = v0.4': all(E6[e][k] == E5[e][k] == E4[e][k] for e in ('E2-001', 'E2-002') for k in lg if k in E4[e]),
     'display = reconstruction label': E6['E2-001']['target_short_name'] == 'R0-COUPLING — causal coupling',
     'resolved via stable ID': E6['E2-001']['target_stable_label_id'] == 'R0-COUPLING',
     'history kept': 'R0-COUPLING — interaction' in E6['E2-001']['history_display_names'] and E6['E2-001']['legacy_target_short_name'] == E5['E2-001']['legacy_target_short_name'],
     'all rows kept': len(E5) == len(E6)}
rec('RC1-01 E2-001 display name', 'PASS' if all(c.values()) else 'FAIL', 'ANALYST-CONSISTENT (display only; HR-IMPL-5-B/6-B)', '; '.join(f'{k}={v}' for k, v in c.items()))
# RC1-02
d = {t: [k for k in D7[t] if D7[t][k] != D8[t][k]] for t in D7}
d = {t: v for t, v in d.items() if v}
c = {'only audit_conditions of EN-ICM-0054/0019': d == {'EN-ICM-0019': ['audit_conditions'], 'EN-ICM-0054': ['audit_conditions']} or d == {'EN-ICM-0054': ['audit_conditions'], 'EN-ICM-0019': ['audit_conditions']},
     'old cells kept as history': all(D8[t]['history_audit_conditions_v07'] == D7[t]['audit_conditions'] for t in d),
     'no promotion (CC/reconstruction unchanged)': all(D8[t][k] == D7[t][k] for t in D7 for k in ('constitutive_conditions', 'reconstruction_conditions', 'reconstruction_condition_refs') if k in D7[t])}
rec('RC1-02 draft audit snapshot', 'PASS' if all(c.values()) else 'FAIL', 'ANALYST-CONSISTENT', '; '.join(f'{k}={v}' for k, v in c.items()))

# SF-10 non-change
res = {}
LIN = {'overlay v0.7': (P(B, 'four_bridge_hr_impl_v0.14/english_publication_overlay_v0.7.tsv'), 'frozen-inputs/english_publication_overlay_v0.7.tsv'),
       'provenance v0.5': (P(B, 'four_bridge_hr_impl_v0.14/four_bridge_condition_provenance_v0.5.tsv'), 'frozen-inputs/four_bridge_condition_provenance_v0.5.tsv'),
       'decisions v0.14': (P(B, 'four_bridge_hr_impl_v0.14/four_bridge_hr_impl_v0.14_decisions.tsv'), 'frozen-inputs/four_bridge_hr_impl_v0.14_decisions.tsv'),
       'scope labels v0.3': (P(B, 'four_bridge_hr_impl_v0.8/four_bridge_scope_labels_v0.3.tsv'), 'frozen-inputs/four_bridge_scope_labels_v0.3.tsv')}
res['frozen copies byte-identical'] = [k for k, (a, b) in LIN.items() if sha(a) != sha(P(RC, b))]
def man(d):
    bad = []
    for line in open(P(d, 'sha256_manifest.txt'), encoding='utf-8'):
        h, p = line.rstrip('\n').split('  ', 1)
        if sha(P(d, p)) != h and not p.endswith('.png'): bad.append(p)
    return bad
for dd in ('four_bridge_hr_impl_v0.8', 'four_bridge_hr_impl_v0.10', 'four_bridge_hr_impl_v0.11', 'four_bridge_hr_impl_v0.12', 'four_bridge_hr_impl_v0.13', 'four_bridge_hr_impl_v0.14'):
    res[dd] = man(P(B, dd))
res['v0.7 package'] = man(V7)
MAC = {'figure2b/data.js': '734d15119fa1c7f4f1e46d776d57e29f7fccfdd9a2b77a8ede2f1323d45d34a7',
       'research/information-concept-map/english-reconstruction/english_publication_overlay_v0.1.tsv': '97d751047fdf9f6498c6948e25fa99fdce1c33eae666169d0306f48d87b37f90',
       'research/information-concept-map/english-reconstruction/english_data_edges_v0.4.tsv': 'ae2f25eb568334da1c340c8eaee172e9bb8b31122fb030365b480749601503f6',
       'research/information-concept-map/english-reconstruction/edge_type_registry_v0.2.tsv': '883c5b60753cbc269ea7a4c965eb83d3aaa4a28099ef2a4c9cf791d0dfab2b50',
       'research/information-concept-map/cross-linguistic-audit/publication_decision_log_v0.1.tsv': 'b8a1fb428fc600a0682ddc065cbfc75b82634b279b1fa3228347c67d504149f1'}
res['staged repo copies = Mac SHA-256'] = [p for p, h in MAC.items() if sha(P(REPO, p)) != h]
O1 = ov(P(REPO, 'research/information-concept-map/english-reconstruction/english_publication_overlay_v0.1.tsv'))
res['BR3-012 overlay rows = repo overlay v0.1'] = [k for k in O1 if any(O1[k][c] != OV[k][c] for c in O1[k])]
PL1 = {r['decision_id']: r for r in rd(P(REPO, 'research/information-concept-map/cross-linguistic-audit/publication_decision_log_v0.1.tsv'))}
res['BR3-012 decisions = repo log v0.1'] = [k for k in PL1 if k not in DEC or any(PL1[k][c] != DEC[k][c] for c in PL1[k])]
rec('SF-10 existing decisions, canonical files and earlier versions unchanged', 'PASS' if not any(res.values()) else 'FAIL', 'N/A',
    f'{res}; v0.10 working-copy PNGs excluded (pixel-identical re-encoding, reported in v0.11 N-3); Mac repository was not written in RC1')
json.dump(R, open(P(RC, 'validation/data_validation_results_rc1.json'), 'w'), ensure_ascii=False, indent=1)
print('SUMMARY', {x: sum(r['string_check'] == x for r in R) for x in ('PASS', 'FAIL')})
