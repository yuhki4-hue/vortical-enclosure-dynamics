#!/usr/bin/env python3
"""Build Four-Bridge Publication RC1 from the v0.14 lineage, the v0.7 package and the repository BR3-012 data.
All inputs are read only. Output: /mnt/user-data/outputs/four-bridge-publication-rc1/"""
import csv, hashlib, io, json, os, re, shutil
OUT = '/mnt/user-data/outputs/four-bridge-publication-rc1'
B = '/mnt/user-data/outputs'
V7 = '/tmp/claude-0/-home-claude/80178cff-6b68-5cbc-bfd3-a8b935af46fb/scratchpad/v07'
REPO = '/mnt/user-data/uploads/isolated-repo'   # staged copies of Mac repository files (verified by SHA-256 against the Mac)
for d in ('publication', 'research-audit', 'frozen-inputs', 'spec', 'renderer', 'validation'):
    os.makedirs(f'{OUT}/{d}', exist_ok=True)

def rd(p): return list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))
def fmt(fields):
    s = io.StringIO(); csv.writer(s, delimiter='\t', lineterminator='\n').writerow(fields); return s.getvalue()[:-1]
def chk(v): assert '\t' not in v and '\n' not in v, v; return v
def write_tsv(p, header, rows):
    with open(p, 'w', encoding='utf-8') as f:
        f.write(fmt(header) + '\n')
        for r in rows: f.write(fmt([chk(str(r[h])) for h in header]) + '\n')
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()

INPUTS = {  # key: (path, origin, version)
 'overlay': (f'{B}/four_bridge_hr_impl_v0.14/english_publication_overlay_v0.7.tsv', 'package four_bridge_hr_impl_v0.14 (container outputs)', 'overlay v0.7'),
 'provenance': (f'{B}/four_bridge_hr_impl_v0.14/four_bridge_condition_provenance_v0.5.tsv', 'package four_bridge_hr_impl_v0.14', 'provenance v0.5'),
 'decisions': (f'{B}/four_bridge_hr_impl_v0.14/four_bridge_hr_impl_v0.14_decisions.tsv', 'package four_bridge_hr_impl_v0.14', 'decision log v0.14'),
 'draft': (f'{V7}/english_data_draft_v0.7.tsv', 'ZIP four_bridge_hr_impl_v0.7.zip (user-supplied)', 'draft v0.7'),
 'edges': (f'{V7}/english_data_edges_v0.5.tsv', 'ZIP four_bridge_hr_impl_v0.7.zip (user-supplied)', 'edges v0.5'),
 'scope_labels': (f'{B}/four_bridge_hr_impl_v0.8/four_bridge_scope_labels_v0.3.tsv', 'package four_bridge_hr_impl_v0.8', 'scope labels v0.3'),
 'label_schema_note': (f'{B}/four_bridge_hr_impl_v0.8/four_bridge_label_schema_note_v0.1.md', 'package four_bridge_hr_impl_v0.8', 'label schema note v0.1'),
 'figure2b': (f'{REPO}/figure2b/data.js', 'Mac repository figure2b/data.js (staged copy)', 'data.js 4.2-patchy-boundaries'),
 'br3_012_overlay_repo': (f'{REPO}/research/information-concept-map/english-reconstruction/english_publication_overlay_v0.1.tsv', 'Mac repository (staged copy)', 'overlay v0.1 (BR3-012 publication rows)'),
 'edges_v04_repo': (f'{REPO}/research/information-concept-map/english-reconstruction/english_data_edges_v0.4.tsv', 'Mac repository (staged copy)', 'edges v0.4'),
 'registry_repo': (f'{REPO}/research/information-concept-map/english-reconstruction/edge_type_registry_v0.2.tsv', 'Mac repository (staged copy)', 'edge type registry v0.2'),
 'pub_decision_log_repo': (f'{REPO}/research/information-concept-map/cross-linguistic-audit/publication_decision_log_v0.1.tsv', 'Mac repository (staged copy)', 'publication decision log v0.1 (BR3-012 decisions)'),
}

# ---------------------------------------------------------------- RC1-01 edges v0.6 (research audit)
SL = rd(INPUTS['scope_labels'][0])
RECON = {s['target_id']: (s['stable_id'], s['display_label']) for s in SL if s['scope'] == 'reconstruction'}
lines = open(INPUTS['edges'][0], encoding='utf-8').read().split('\n')[:-1]
H = next(csv.reader([lines[0]], delimiter='\t'))
NEWC = ['source_stable_label_id', 'target_stable_label_id', 'display_name_resolution', 'history_display_names']
out = [fmt(H + NEWC)]
changed = []
for l in lines[1:]:
    f = dict(zip(H, next(csv.reader([l], delimiter='\t'))))
    extra = {'source_stable_label_id': 'NONE', 'target_stable_label_id': 'NONE', 'display_name_resolution': 'UNCHANGED (no scope-label entry for either endpoint)', 'history_display_names': 'NONE'}
    hist = []
    for side in ('source', 'target'):
        tid = f[f'{side}_target_id' if side == 'source' else 'target_target_id_or_field']
        if tid in RECON:
            sid, lab = RECON[tid]
            extra[f'{side}_stable_label_id'] = sid
            resolved = f'{sid} — {lab}'
            if f[f'{side}_short_name'] != resolved:
                hist.append(f"{side}: v0.5 “{f[f'{side}_short_name']}” (from {f['display_name_source']})")
                f[f'{side}_short_name'] = resolved
                changed.append((f['edge_id'], side))
            extra['display_name_resolution'] = 'stable_label_id → scope_labels_rc1.tsv (reconstruction scope); display only, not a logical change'
    if hist:
        extra['history_display_names'] = '; '.join(hist)
        f['display_name_source'] = 'scope_labels_rc1.tsv:reconstruction (via stable_label_id)'
    out.append(fmt([chk(f[h]) for h in H] + [chk(extra[c]) for c in NEWC]))
open(f'{OUT}/research-audit/english_data_edges_v0.6.tsv', 'w', encoding='utf-8').write('\n'.join(out) + '\n')

# ---------------------------------------------------------------- RC1-02 draft v0.8 (research audit)
P = {r['item_id']: r for r in rd(INPUTS['provenance'][0])}
lines = open(INPUTS['draft'][0], encoding='utf-8').read().split('\n')[:-1]
H = next(csv.reader([lines[0]], delimiter='\t'))
out = [fmt(H + ['history_audit_conditions_v07', 'audit_conditions_source'])]
draft_changes = []
for l in lines[1:]:
    f = dict(zip(H, next(csv.reader([l], delimiter='\t'))))
    old = f['audit_conditions']; new = old
    for iid in ('AC-R0-06', 'AC-FC-06'):
        m = re.search(r'\[' + iid + r'\] ([^\[]*?)(?=; \[|$)', new)
        if m and m.group(1) != P[iid]['item_text']:
            new = new[:m.start(1)] + P[iid]['item_text'] + new[m.end(1):]
            draft_changes.append((f['target_id'], iid))
    if new != old:
        f['audit_conditions'] = new
        hist, src = old, 'item texts refreshed from four_bridge_condition_provenance_v0.5.tsv (current-state reference); v0.7 cell kept in history_audit_conditions_v07'
    else:
        hist, src = 'NOT-CHANGED-IN-v0.8', 'unchanged from draft v0.7'
    out.append(fmt([chk(f[h]) for h in H] + [chk(hist), chk(src)]))
open(f'{OUT}/research-audit/english_data_draft_v0.8.tsv', 'w', encoding='utf-8').write('\n'.join(out) + '\n')

# ---------------------------------------------------------------- frozen inputs (byte copies)
for k in ('overlay', 'provenance', 'decisions', 'scope_labels', 'label_schema_note'):
    shutil.copyfile(INPUTS[k][0], f'{OUT}/frozen-inputs/' + os.path.basename(INPUTS[k][0]))

# ---------------------------------------------------------------- publication data
OV = {r['overlay_id']: r for r in rd(INPUTS['overlay'][0])}
s = open(INPUTS['figure2b'][0], encoding='utf-8').read(); s = s[s.index('{'):s.rstrip().rstrip(';').rindex('}') + 1]
SRC = {e['id']: e for e in json.loads(s)['elements']}
D8 = {r['target_id']: r for r in rd(f'{OUT}/research-audit/english_data_draft_v0.8.tsv')}
DEC = {r['decision_id']: r for r in rd(INPUTS['decisions'][0])}
APPROVAL = {'R0': 'H-V4B-12-R0-B;H-V4B-12-R0-FINAL-A', 'Fc': 'H-V4B-12-FC-B', 'M1': 'H-V4B-12-M1-B', 'C0': 'H-V4B-12-C0-A'}
units = {}
for k in ('R0', 'Fc', 'M1', 'C0'):
    o = OV['OV-N-' + k]; tid = o['object_id'].split('(')[1].rstrip(')')
    units[k] = dict(id=k, group='four-bridge', bridge={'R0': 'BR3-008', 'Fc': 'BR3-023', 'M1': 'BR3-044', 'C0': 'BR3-027'}[k], target=tid,
                    stable_label_id=o['stable_label_id'], ja_label=o['original_japanese_label'], ja=o['original_japanese_text'], label=o['approved_english_label'],
                    gloss=o['selected_english_gloss_candidate'], formula=None if o['same_unit_formula'] == 'NONE' else o['same_unit_formula'],
                    note_full=o['mandatory_ambiguity_note_full'], note_short=o['mandatory_ambiguity_note_short'], shared=o['shared_note_refs'] != 'NONE',
                    cc=D8[tid]['constitutive_conditions'], evidence_class=o['evidence_class'], overlay_id='OV-N-' + k,
                    note_approval=APPROVAL[k], label_gloss_approval=o['publication_state'],
                    items=[{x: p[x] for x in ('item_id', 'item_kind', 'item_text', 'origin', 'role', 'scope', 'status')} for p in P.values() if p['source_id'] == k])
br = {}
for oid in ('OV-N-R4', 'OV-N-R4-SYS', 'OV-N-R4-COMB'):
    o = OV[oid]
    br[oid] = dict(id=o['object_id'], group='br3-012', overlay_id=oid, ja_label=SRC['R4']['label'].split('｜')[1] if oid == 'OV-N-R4' else '', ja=o['original_japanese_text'],
                   label='', gloss=o['selected_english_gloss_candidate'], formula=None, note_full=o['mandatory_ambiguity_note_full'], note_short=o['mandatory_ambiguity_note_short'],
                   shared=False, cc='', items=[], evidence_class=o['evidence_class'], note_approval=o['human_decision_id'], label_gloss_approval=o['publication_state'])
links = {k: {f: OV[k][f] for f in ('overlay_id', 'object_type', 'object_id', 'selected_english_gloss_candidate', 'mandatory_ambiguity_note_short', 'mandatory_ambiguity_note_full',
                                     'evidence_class', 'publication_state', 'publication_assertion', 'publication_display', 'management_scope')}
         for k in OV if not k.startswith('OV-N-') and k != 'OV-NOTE-INTERVENTION'}
data = dict(release='Four-Bridge Publication RC1', units=units, br3_012_units=br,
            shared_note=dict(full=OV['OV-NOTE-INTERVENTION']['mandatory_ambiguity_note_full'], short=OV['OV-NOTE-INTERVENTION']['mandatory_ambiguity_note_short'], approval='H-V4B-12-INTERVENTION-A'),
            links=links, scope_labels=[{k: s[k] for k in ('stable_id', 'target_id', 'source_id', 'scope', 'display_label', 'canonical_display_field')} for s in SL],
            sources={k: dict(path=os.path.relpath(v[0], '/'), origin=v[1], version=v[2]) for k, v in INPUTS.items()})
json.dump(data, open(f'{OUT}/publication/publication_data_rc1.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# flat tables
UH = ['unit_id', 'group', 'overlay_id', 'original_japanese_label', 'original_japanese_text', 'approved_english_label', 'approved_gloss', 'same_unit_formula', 'shared_note_ref', 'note_approval_decisions', 'label_gloss_publication_state']
rows = []
for u in list(units.values()) + list(br.values()):
    rows.append(dict(unit_id=u['id'], group=u['group'], overlay_id=u['overlay_id'], original_japanese_label=u['ja_label'] or 'NOT-RECORDED (BR3-012 overlay v0.1 has no label field)',
                     original_japanese_text=u['ja'], approved_english_label=u['label'] or 'NONE (BR3-012: no separate English label decision)', approved_gloss=u['gloss'],
                     same_unit_formula=u['formula'] or 'NONE', shared_note_ref='OV-NOTE-INTERVENTION' if u['shared'] else 'NONE', note_approval_decisions=u['note_approval'], label_gloss_publication_state=u['label_gloss_approval']))
write_tsv(f'{OUT}/publication/publication_units_rc1.tsv', UH, rows)
NH = ['note_id', 'unit_id', 'note_full', 'note_short', 'approval_decisions', 'approved_text_source', 'source_reference_basis']
nrows = []
NSRC = {'R0': 'overlay v0.4 OV-N-R0', 'Fc': 'overlay v0.5 OV-N-Fc', 'M1': 'full: overlay v0.4+; short: literal text in H-V4B-12-M1-B', 'C0': 'OV-N-C0 current at decision time (overlay v0.6)'}
for k, u in units.items():
    nrows.append(dict(note_id='OV-N-' + k, unit_id=k, note_full=u['note_full'], note_short=u['note_short'], approval_decisions=u['note_approval'], approved_text_source=NSRC[k], source_reference_basis=OV['OV-N-' + k]['source_reference_basis']))
nrows.append(dict(note_id='OV-NOTE-INTERVENTION', unit_id='R0;Fc;M1 (appended to full note)', note_full=data['shared_note']['full'], note_short=data['shared_note']['short'], approval_decisions='H-V4B-12-INTERVENTION-A',
                  approved_text_source='OV-NOTE-INTERVENTION current at decision time (overlay v0.6)', source_reference_basis=OV['OV-NOTE-INTERVENTION']['source_reference_basis']))
for oid, u in br.items():
    nrows.append(dict(note_id=oid, unit_id=u['id'], note_full=u['note_full'], note_short=u['note_short'], approval_decisions=u['note_approval'], approved_text_source='repository overlay v0.1 (BR3-012), unchanged', source_reference_basis=OV[oid]['source_reference_basis']))
write_tsv(f'{OUT}/publication/mandatory_notes_rc1.tsv', NH, nrows)
SH = ['stable_id', 'target_id', 'source_id', 'scope', 'display_label', 'canonical_display_field', 'resolution_rule']
write_tsv(f'{OUT}/publication/scope_labels_rc1.tsv', SH, [dict(s, resolution_rule='display name = display_label of (stable_id, scope); working_label never used for display') for s in SL])
DH = ['decision_id', 'role_in_rc1', 'log_file', 'log_row', 'status', 'finality']
order = list(DEC)
RL = {'H-V4B-12-CONDITIONAL': 'history: conditional approval (corrections ①②③)', 'H-V4B-12-M1-B-REVISED': 'R0 note M-1 correction; AC-R0-05/06', 'H-V4B-12-R0-B': 'history: partial R0 approval',
      'H-V4B-12-R0-FINAL-A': 'R0 notes final approval', 'H-V4B-12-FC-B': 'Fc notes approval', 'H-V4B-12-M1-B': 'M1 notes approval', 'H-V4B-12-C0-A': 'C0 notes approval',
      'H-V4B-12-INTERVENTION-A': 'shared intervention note approval', 'H-BR3-008-PUB-LABEL-GLOSS-A': 'R0 label + gloss', 'H-BR3-023-PUB-LABEL-GLOSS-A': 'Fc label + gloss',
      'H-BR3-044-PUB-LABEL-GLOSS-B': 'M1 label + gloss', 'H-BR3-027-PUB-LABEL-GLOSS-B': 'C0 label + gloss', 'H-BR3-023-D-H4-LIMIT': 'D-H4 scope limit', 'H-O-008-2-B': 'E2-001 / R0↔R1 publication scope',
      'H-BR3-012-HR-PUBLICATION': 'BR3-012 wording A (unchanged)', 'H-BR3-012-O3-CONDITIONAL': 'BR3-012 E2-004/E2-060 (unchanged)', 'HR-IMPL-5-B': 'scope-specific labels', 'HR-IMPL-6-B': 'edge display names (RC1-01)'}
write_tsv(f'{OUT}/publication/decision_refs_rc1.tsv', DH, [dict(decision_id=d, role_in_rc1=RL.get(d, 'kept (governing or historical)'), log_file='frozen-inputs/four_bridge_hr_impl_v0.14_decisions.tsv',
          log_row=str(order.index(d) + 2), status=DEC[d]['status'], finality=DEC[d]['finality']) for d in order])

# renderer data
render = dict(units=units, br3_012_units=br, shared_note=data['shared_note'], links=links, scope_labels=data['scope_labels'],
              sources=dict(overlay='frozen-inputs/english_publication_overlay_v0.7.tsv (CSV reader)', provenance='frozen-inputs/four_bridge_condition_provenance_v0.5.tsv', draft='research-audit/english_data_draft_v0.8.tsv'))
open(f'{OUT}/renderer/data.js', 'w', encoding='utf-8').write('window.FB_DATA = ' + json.dumps(render, ensure_ascii=False) + ';\n')
json.dump(dict(edges_display_changes=changed, draft_audit_snapshot_changes=draft_changes, inputs={k: dict(path=v[0], origin=v[1], version=v[2], sha256=sha(v[0])) for k, v in INPUTS.items()}),
          open(f'{OUT}/validation/build_log_rc1.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('edges changed', changed, '| draft changed', draft_changes)
