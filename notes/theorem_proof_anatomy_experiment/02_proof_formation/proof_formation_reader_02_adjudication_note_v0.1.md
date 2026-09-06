# Reader 02 Adjudication Note v0.1

- **Status:** qualitative adjudication and diagnosis of one blind reader submission. Not a framework revision, not a score, not an agreement measure.
- **Target of audit:** [`proof_formation_reader_02_claudecode_v0.1.1.md`](./proof_formation_reader_02_claudecode_v0.1.1.md)
- **Rules applied:** [`proof_formation_adjudication_rules_v0.1.md`](./proof_formation_adjudication_rules_v0.1.md) §§1–3
- **Frozen inputs:** [`proof_formation_frozen_toy_corpus_v0.1.md`](./proof_formation_frozen_toy_corpus_v0.1.md), [`proof_formation_coder_instructions_v0.1.1.md`](./proof_formation_coder_instructions_v0.1.1.md)
- **Date:** 2026-09-05
- **Files modified by this note:** none. This file is additive.

Constraints observed: no new move code, no new taxonomy, no score, no geometry, no agreement rate, no framework generalization, no revised field schema, no v0.1.2 design. The answer key in adjudication rules §5 is treated as one source-anchored reference, explicitly **not** as the sole correct column (§5 says so itself).

---

## 0. Classification scheme used

Every audited item receives a primary class, and a secondary class where more than one applies.

| Class | Meaning |
|---|---|
| **A** | SOURCE-RESOLVED — source wording / exact before-after / explicit verdict fixes it uniquely |
| **B** | GENUINE SOURCE AMBIGUITY — source itself admits multiple readings or segmentations |
| **C** | PACKET DEFECT — the frozen packet or the instructions lack information the reader needed |
| **D** | FRAMEWORK BOUNDARY — source is readable, but current fields / M1–M17 / role distinctions cannot express it naturally |
| **E** | CODER OVERREACH — Reader 02 inferred more than the source supports |
| **F** | ADJUDICABLE CODING ERROR — move / provenance / status / role assignment is wrong given source + instructions |
| **G** | NOT ENOUGH EVIDENCE — neither packet nor original source settles it, or it lies outside this source boundary |

Field-level verdicts use `KEEP` / `CORRECT` / `UNRESOLVED` / `SOURCE GAP` / `FRAMEWORK GAP`, per the brief. Adjudication rules §1 priority is applied: source wording > exact before/after > explicit status > explicit dependency change > inference. Rules §2.5 is applied strictly: **only SOURCE-RESOLVED items are corrected**; everything else stays UNRESOLVED with both readings preserved.

---

## 1. Reader 02 isolation audit

### 1.1 What was read, and when

| Item | Finding | Evidence |
|---|---|---|
| Files read during the reader phase | `proof_formation_coder_instructions_v0.1.1.md`, `proof_formation_frozen_toy_corpus_v0.1.md` — these two only | tool-call sequence of the reader run; both read in full before Step 0 |
| Original sources | **None consulted.** Reader 02 declined return-to-source and recorded the declension and its reason in §0 of its own output | reader output §0; no source file was opened in the reader phase |
| Adjudication rules / answer key | **Not read during the reader phase.** Opened for the first time in the present adjudication phase, after the reader file was written and closed | file write completed before the adjudication rules were first opened; the reader output contains no reference to any key content, example-bank ID, or difficulty flag |
| Meta-experiment document | Not read. Its filename was visible in the IDE-open notice and in the corpus header link | reader output cites no §12.2 content beyond what the corpus header states |
| Reader 01 output / calibration note | **Not read.** See 1.2 for a metadata-level exposure | — |
| Trajectory summaries, node ledger, other readers | Not read | — |

### 1.2 Disclosable metadata exposures (content-free)

Three contacts with forbidden-file *names* occurred. None transmitted any coding, verdict, or excerpt.

1. During file-existence verification the reader phase ran `ls -lt`, whose output listed `proof_formation_reader_01_calibration_note.md` with its size and timestamp. Filename, size, mtime only; no content was opened or quoted.
2. The IDE reported that the user had `proof_formation_meta_experiment_v0.1.md` open. Filename only.
3. The frozen corpus header itself names the adjudication-rules path and the meta-experiment path. This is inherent to the packet, not a reader action.

**Assessment:** these do not compromise blindness. Nothing in the reader output can be traced to them. Classification: not a defect.

### 1.3 Outside-knowledge audit

The instructions forbid filling gaps with outside knowledge or general expectations about how proofs normally work. Three candidate insertions were checked.

| Location | Insertion | Verdict |
|---|---|---|
| E02-b `proof_or_evidence_resources` | `|X| = |A||E| > |A|` counting argument, supplied where the source states only that `r` cannot be injective | **Permitted, borderline.** Labelled INFERENCE, used only to fill the resource field, and did not alter any claim, move, or status. Directly entailed by the source's own `|E|>1` and `r: X→A`. Class **A** primary, **E** secondary (minor). KEEP. |
| Named results in E02/E03/E04/E11 (quine, Kleene recursion, Blackwell, Löb, adaptive distinguishing sequence) | All names appear verbatim in the excerpts; Reader 02 added no content about what they say beyond the excerpt's own gloss | KEEP. No overreach. |
| `degenerate_or_target_leakage` operationalization | Reader 02 invented a two-sense reading for an undefined field | Treated separately in §4.4. Not outside *subject-matter* knowledge; it is an instruction gap. |

### 1.4 Blindness verdict

**The Reader 02 submission qualifies as a formal blind reader result.** It was produced with access to exactly the two permitted files, without source return, and without any contact with the key, the adjudication rules, Reader 01, or the meta-experiment.

**One limitation must be recorded, and it concerns this note rather than the submission.** The reader and this adjudicator are the same model instance in the same session. The reader phase was blind in the required sense — the ordering is verifiable and the key was genuinely unavailable when the codings were made — but **this adjudication is a self-audit, not an independent adjudication.** Adjudication rules §1 forbids using authority or convenience as grounds, which limits the damage; nonetheless, for the inter-reader test proper, this note should be treated as:

> *blind reader submission + self-adjudication*, not *blind reader submission + independent adjudication*.

Gate item §7.1 of the adjudication rules ("all readers submitted independently without seeing the answer key") is satisfied by the submission. Independence of the *adjudicator* is a separate requirement that §7 does not state and that this note does not meet. If the protocol requires an independent adjudicator, §§2–7 below should be re-derived by a different party; the classifications here are offered as a first pass, and every correction issued is argued from source + instructions so that it can be checked without trusting the adjudicator.

---

## 2. Segmentation adjudication

Reader 02 split 12 corpus items into 18 subepisodes. Adjudication rules §3 bullet 2 makes non-resolution **mandatory** when the boundary is multiply possible and the choice changes move or status. That rule governs everything in this section.

### 2.1 E02 — self-containment / conditional capacity

1. **R02 segmentation:** E02-a (universal implication withdrawn, side claim retained) / E02-b (conditional capacity proposition).
2. **Alternative retained by R02:** single episode with the conditional proposition as A3.
3. **Explicit in source:** the `[WITHDRAWN]` implication and the `[ESTABLISHED]` qualitative claim are one recorded pair (Excerpt 3). Excerpt 4 carries its own assumption set, its own defeater list, and its own explicit non-identity verdict ("これは「自己包含定理」ではなく…命題である").
4. **Not fixed by source:** whether 「条件付きの容量命題は残る」 continues the 「残ったもの」 block or opens a new one.
5. **Classification:** **B** primary. The key's AB-P2 uncertainty note independently permits both ("二episode化も許す"), and its E02 row requires only that the two not be merged silently — which R02 did not do.
6. **Change coding?** No.
7. **Unresolved?** Yes. Retain R02's AMBIGUOUS flag as written.

### 2.2 E04 — pairwise vs global separator

1. **R02 segmentation:** single episode, three after-claims (A1 withdrawn / A2 quantifier gap / A3 synthesis).
2. **Alternative retained:** E04-a (two-bit construction establishes the quantifier gap) / E04-b (internality reading withdrawn).
3. **Explicit in source:** one `[WITHDRAWN]`, one `[ESTABLISHED]`, one `[SYNTHESIS]`, all in one block (Excerpt 4). The external-observer control and the prior art are one witness block (Excerpt 3).
4. **Not fixed by source:** whether Excerpt 2's construction is a result in its own right or only material for the withdrawn interpretation.
5. **Classification:** **B** primary. Status labels differ across the three after-claims, which R02 honoured with three separate `terminal_status` entries — this satisfies the key's "`withdrawn` と狭い remnant を一つの terminal status へ潰さない" concern (rules §6.2).
6. **Change coding?** No.
7. **Unresolved?** Yes, as recorded.

### 2.3 E05 — internal/external interface correction

1. **R02 segmentation:** E05-a (general equivalence withdrawn → stipulative equivalence + conditional lemma) / E05-b (`inside vs outside` withdrawn).
2. **Alternative retained:** E05-a split further into a1 (convention) / a2 (conditional lemma).
3. **Explicit in source:** the diff row fixes one accepted revision with a two-way split; Excerpt 4 records **two** distinct `[WITHDRAWN]` items with different objects.
4. **Not fixed by source:** whether the two withdrawals are one decision or two; whether the two replacements are two branches of one episode or two episodes.
5. **Classification:** **B** primary, **D** secondary. The key's CI-P1 uncertainty note allows exactly this ("一episodeの二branchとするか、二episodeとするかは`AMBIGUOUS`を許す"). R02's extraction of E05-b as a separate subepisode is *finer* than the key's row but is anchored in a distinct source `[WITHDRAWN]` with a distinct object, so it is source-compatible.
6. **Change coding?** No.
7. **Unresolved?** Yes on both boundaries. Note that E05-b carries `failure_witness: INFERENCE / AMBIGUOUS` — an honest consequence of splitting it out, and the price of the finer segmentation. Retain both.

### 2.4 E06 — GST

1. **R02 segmentation:** E06-a (case verdict) / E06-b (mechanism name) / E06-c (taxonomy deletion).
2. **Alternative retained:** single revision episode, A1–A4.
3. **Explicit in source:** the diff row fixes `working positive case → frozen negative baseline` (the key's EB-P1 treats exactly this as one explicit revision episode). The three bullets of Excerpt 4 have distinct objects.
4. **Not fixed by source:** whether the bullets are three transitions or one change list. Excerpt 4 gives no reason for the taxonomy deletion, so that bullet has no witness of its own.
5. **Classification:** **B** primary, **C** secondary. The key's EB-P1 uncertainty note explicitly allows sub-episode separation ("個別のquotient、model extension、bibliographic correctionはsub-episodeとして分離可能"), so R02's three-way split is a permitted refinement. The C component: the key's E06 row names an **Erasure Test** as the witness. Confirmed present in the original at `deferred_resolution_case_01_gst_v0.2.md` §16 ("固有語彙を消しても情報は失われず…Deferred Resolution は、このケースでは methodological construct として独立しない") and **absent from every E06 excerpt in the frozen packet**. Reader 02 could not have reached that witness.
6. **Change coding?** No.
7. **Unresolved?** Yes. E06-c additionally stays UNRESOLVED on witness and decision rule (**C**).

### 2.5 E08 — hydrology

1. **R02 segmentation:** single episode, A1 (documentary continuity) / A2 (effectiveness untested).
2. **Alternative retained:** E08-a (deletion of the effectiveness sentence, C-3) / E08-b (verdict relabel).
3. **Explicit in source:** the v0.1→v0.2 verdict-label row and the C-3 change row are both explicit; both name N-04 as the operative finding.
4. **Not fixed by source:** whether relabel and sentence-deletion are one change or two.
5. **Classification:** **B** primary, **C** secondary. The key's EB-B2 splits E08 differently again — C-1, C-2, C-3 as three sub-episodes with different failure types (two factual corrections, one internal contradiction). **C-1 and C-2 do not appear anywhere in the frozen packet**; only C-3 does. R02's alternative split is therefore a different partition of a *smaller* visible object, and is source-compatible on what it could see. The key's partition is unreachable from the packet.
6. **Change coding?** No.
7. **Unresolved?** Yes, and the unreachability of C-1/C-2 should be recorded as a packet-level fact, not as a reader shortfall.

### 2.6 E09 — P0 to P1-reduced

1. **R02 segmentation:** E09-a (P0 decision) / E09-b (P1-reduced termination).
2. **Alternative retained:** none.
3. **Explicit in source:** 「P0 と本検査により、その計画の前提は二段階にわたって否定された」 fixes two stages. The key's AB-P1 uncertainty note independently requires the split ("(iv) terminationはP1-reduced後にactualとなるので、P0時点と後続episodeを分ける").
4. **Not fixed by source:** nothing at the boundary level.
5. **Classification:** **A**. This is the one segmentation in the submission that the source resolves uniquely, and R02 resolved it correctly and declined to mark it ambiguous.
6. **Change coding?** No.
7. **Unresolved?** No — correctly not left open.

### 2.7 E12 — ordinal

1. **R02 segmentation:** E12-a (S-axis) / E12-b (A-axis).
2. **Alternative retained:** none.
3. **Explicit in source:** two separate 判定 blocks with different objects and different verdict letters (`S2*`, `A2`).
4. **Not fixed by source:** whether the A-axis block is a transition at all or a standing classification record (R02 raised this itself).
5. **Classification:** **A** for the split; **G** for the A-axis transition question (the A-ladder is not in the packet, and the original would have to be read to settle whether A2 is a downgrade or an initial classification).
6. **Change coding?** No.
7. **Unresolved?** Yes on the "is E12-b a transition" question only.

### 2.8 Two boundaries R02 closed that the source leaves open

These are the section's substantive findings, and they run against Reader 02.

**E10 — CORRECT the boundary flag.** R02 wrote `alternative_segmentations: 考慮したが採用せず` and did **not** mark the boundary AMBIGUOUS, on the ground that Excerpt 3 (Gödel II as a metatheorem from external consistency to internal unprovability) has no before/after of its own. But in the same block R02 declined **M12** *because of* that boundary choice. Adjudication rules §3 bullet 2 makes non-resolution mandatory precisely when "episode boundary が複数可能で、どれを選ぶかにより move/status が変わる" — and R02's own reasoning demonstrates that the M12 code varies with the boundary. Recording the boundary as settled while recording the move as boundary-dependent is internally inconsistent.
Classification: **F** primary (procedural, adjudicable from the rules R02 was operating under — the instructions' Step 0 states the same requirement), **B** secondary. Correction: E10 `episode_boundary` → **AMBIGUOUS**, with the Gödel-I / Gödel-II / C1-verdict composite reading retained as an alternative. The M12 question itself is **not** corrected; it becomes UNRESOLVED (see §4.1).

**E11 — CORRECT the location of the boundary record.** R02 recorded `alternative_segmentations: 考慮したが採用せず` for the §2 and §11 sub-readings, but the boundary that actually matters — whether the mathematical transition `T → T + Rfn_Γ(T)` is its own sub-episode — appears only inside a `considered and NOT coded: M6` note. The key's AB-B1 calls this "E11で最も重要な adjudication point" and requires deciding the boundary first. R02 reached the same substantive position as AB-B1 (T⁺ is the analysis object under a meta-label episode) but filed the boundary question in the move field instead of the segmentation field.
Classification: **F** minor (record location), **B** primary on the substance. Correction: add the mathematical-extension sub-episode to E11 `alternative_segmentations` as a retained alternative; leave the M6/M12 declines standing as boundary-dependent.

---

## 3. Episode-by-episode field audit

### 3.0 One systematic finding, stated once

**Provenance of `move_taken`.** In 17 of 18 blocks Reader 02 labels M-codes `SOURCE-DERIVED` (e.g. E01 "M15 SOURCE-DERIVED; M17 SOURCE-DERIVED"), reserving INFERENCE for cases where it felt the mapping was strained (E01's M14, E05-b's M14, E02-a's M14). The adjudication rules' provenance anchor §5.2 states the opposite as a blanket rule: "M-code、difficulty、episode grouping、primary/secondary は INFERENCE".

Adjudicating this from the instructions alone rather than from the key: coder instructions Step 4 define `SOURCE-DERIVED` as "stated or directly entailed by the cited excerpt" and `INFERENCE` as "reconstruction needed to connect source statements", and they never say whether the provenance label attaches to *the operation* (which is often quoted verbatim — 「撤回した」「削除した」「降格した」) or to *the code assignment* (which is always a mapping into a taxonomy the source does not use). Reader 02 consistently chose the first reading and applied it consistently.

Classification: **D** primary (the instructions do not fix the referent of the provenance label on this field), **F** secondary (under the key's §5.2 anchor these are mislabels). Verdict: **UNRESOLVED / FRAMEWORK GAP**, not corrected. Recorded once here; not repeated in the per-episode tables below, where `provenance` verdicts refer to the other fields.

Related but distinct: Reader 02's own defect #5 (the `dependencies` provenance slot covers three fields at once) is a different problem and is adjudicated in §5.

### 3.1 E01

| Field | Verdict | Note |
|---|---|---|
| claim_before | KEEP | Quoted; the novelty clause 「新しい一般定理として主張すること」 is taken from the `[WITHDRAWN]` line, which is priority-1 wording. **A** |
| claim_identity | KEEP | Single ID, matches the single withdrawal record. **A** |
| obligation_type | KEEP | Dual (theorem + novelty) rather than forced to one. Instructions Step 1 permit this by not requiring exclusivity; refusing to pick is the conservative reading. **B** |
| assumptions | KEEP | **A** |
| proof_or_evidence_resources | KEEP | "no left inverse" correctly placed as resource, not assumption. **A** |
| evaluation_or_decision_rules | KEEP | The content criterion 「非単射でなければならない条件を別途示さない限り」 is correctly a decision rule and not an assumption. **A** |
| failure_witness | KEEP | Both witnesses (prior art, `O=id`) recorded; neither promoted to a move. Matches instructions' "counterexample is normally a trigger or witness". **A** |
| available_branches | KEEP | "show separately the conditions under which O must be non-injective" is source-explicit and untaken. **A** |
| adopted_side_claims | KEEP | Own ID, own status. **A** |
| move_taken (M15, M17, M14) | KEEP | Key core is M15+M17 with M2/M4/M14 allowed; R02 took the core and one permitted extra, and declined M4 with a stated reason. **A/B** |
| claim_after | KEEP | **A** |
| terminal_status | KEEP | Two statuses for two after-claims; no blending. **A** |
| provenance (non-move fields) | KEEP | **A** |
| degenerate_or_target_leakage | KEEP | Sense-1 degeneracy (conclusion contained in premise) is directly supported by Excerpt 2. See §4.4. **A** |
| uncertainties | KEEP | The M14/M5 boundary and the "side claim vs pre-existing background fact" question are both real. **B** |

### 3.2 E02-a / E02-b

| Field | E02-a | E02-b |
|---|---|---|
| claim_before | KEEP — withdrawal formula quoted verbatim. **A** | KEEP — correctly points back at B02 rather than inventing a new before. **A** |
| claim_identity | KEEP. **A** | KEEP — `B02'` marked as successor, not as B02 rescued. This is the exact trap AB-P2 names ("元claimの看板を救済しない") and R02 avoids it. **A** |
| obligation_type | KEEP. **A** | KEEP. **A** |
| assumptions | KEEP — the two hypothesis-level assumptions only. **A** | UNRESOLVED — the four defeater conditions are placed here; see §4.3. **B** |
| proof_or_evidence_resources | KEEP — UNKNOWN is correct; the source gives the original claim no resource. **A** | KEEP with note — counting argument is INFERENCE-labelled. **A/E** |
| evaluation_or_decision_rules | KEEP — INFERENCE label is honest; the "だけでは/単独では" rule is real but never stated as a rule. **B** | KEEP — the naming rule 「自己包含定理ではなく…」 is priority-1 wording used as a decision rule. **A** |
| failure_witness | KEEP — four witnesses, none promoted to a move. Key §5.1 anchors exactly these as failure witnesses. **A** | KEEP — NOT APPLICABLE is correct. **A** |
| available_branches | KEEP — Breuer/Wolpert's extra conditions are source-explicit and untaken here. **A** | KEEP — UNKNOWN. **A** |
| adopted_side_claims | KEEP. **A** | KEEP — NOT APPLICABLE correct: the after is the claim itself, not a side claim. **A** |
| move_taken | KEEP — M17 + M14. Matches key core (M17/M14). The M15 decline is audited in §4.1 and upheld. **A** | KEEP — M1 + M4. Matches key core (M1/M4 for the side claim). M2 decline audited in §4.2. **A/B** |
| claim_after | KEEP. **A** | KEEP. **A** |
| terminal_status | KEEP. **A** | KEEP — "retained as conditional" plus the explicit non-theorem demotion. **A** |
| provenance | KEEP. | KEEP. |
| degenerate_or_target_leakage | KEEP — "no degeneracy here" is the right call; the failure is under-derivation, not circularity. **A** | KEEP — leakage-block reading is well anchored in 「自己包含定理ではなく」. **A** |
| uncertainties | KEEP — the cross-item E01→E02 M7 question is real and is adjudicated in §5 item 9. **C/D** | KEEP. **B** |

### 3.3 E03

| Field | Verdict | Note |
|---|---|---|
| claim_before | KEEP | Withdrawal wording quoted. **A** |
| claim_identity | KEEP | **A** |
| obligation_type | KEEP | **A** |
| assumptions | KEEP | **A** |
| proof_or_evidence_resources | KEEP | UNKNOWN correct; the definitional move is placed as cause-of-degeneracy, not as resource. **A** |
| evaluation_or_decision_rules | UNRESOLVED | Role overlap with S03 recorded rather than duplicated, per instructions Step 2's no-duplication rule. See §4.3. **B/D** |
| failure_witness | KEEP | Three witnesses including the definitional circularity. **A** |
| available_branches | UNRESOLVED | Near-identical in content to S03; R02 flagged this itself. **D** |
| adopted_side_claims | KEEP | Two side claims, separately identified. **A** |
| move_taken (M17, M15, M14) | KEEP | Exactly the key core (M14, M15, M17). M4 (allowed) not taken — permitted. **A** |
| claim_after | KEEP | Three after-claims. **A** |
| terminal_status | KEEP | **A** |
| provenance | KEEP | |
| degenerate_or_target_leakage | KEEP | The strongest instance in the submission: 「非同型性を定義へ埋め込んでいるだけである」 is quoted, and the key's AA-P1 independently treats this exact sentence as the canonical target-leakage flag. **A** |
| uncertainties | KEEP | **B** |

### 3.4 E04

| Field | Verdict | Note |
|---|---|---|
| claim_before | KEEP | Taken from the `[WITHDRAWN]` line ("二ビット破壊例を…内部性そのものが生む不可能性の例として使うこと") rather than from the opening hypothesis. This is the correct priority-1/priority-3 reading: what was withdrawn is the *use*, not the construction. **A** |
| claim_identity | KEEP | **A** |
| obligation_type | KEEP | "interpretation / reduction (attribution of cause)" is a defensible fit; the instructions' list has no better slot. **B/D** |
| assumptions | KEEP | **A** |
| proof_or_evidence_resources | KEEP | Two-bit construction as resource/witness, not move. **A** |
| evaluation_or_decision_rules | KEEP | Matched-resource control, INFERENCE-labelled — correct, since the source applies it without stating it as a rule. **A/B** |
| failure_witness | KEEP | External replication + prior art. **A** |
| available_branches | UNRESOLVED | Fresh preparation: branch or scope condition. Key E04 row says only "Fresh preparation is not main move", which R02 honoured. The branch/scope question is left open by the key too. **B** |
| adopted_side_claims | KEEP | S04 and S04b separated, with `[SYNTHESIS]` given `open` rather than `established`. **A** |
| move_taken (M17, M15, M14) | KEEP | Exactly the key core. The key adds "retained comparison may take M13" — *may*; not taken, permitted. **A/B** |
| claim_after | KEEP | **A** |
| terminal_status | KEEP | Three distinct statuses; the `open` for A3 is the correct refusal to bank a research direction as a result. **A** |
| provenance | KEEP | |
| degenerate_or_target_leakage | KEEP | Sense-2 leakage ("internality label absorbing what the resource conditions produce"). Supported by the source's own control argument, though the vocabulary is R02's. See §4.4. **A/D** |
| uncertainties | KEEP | **B** |

### 3.5 E05-a / E05-b

| Field | E05-a | E05-b |
|---|---|---|
| claim_before | KEEP — the v0.1 general `[ESTABLISHED]` quoted in full. **A** | KEEP — quoted from the second `[WITHDRAWN]`. **A** |
| claim_identity | KEEP — identity explicitly **not** preserved across the revision. This is the CI-P1 trap ("claim identity は完全に保存され M1 のみ") and R02 avoids it. **A** | UNRESOLVED — whether this is a separate identity or a facet of E05-a. **B** |
| obligation_type | KEEP for the before; FRAMEWORK GAP for A2 — R02 correctly reports that no listed type covers a definitional convention. **D** | UNRESOLVED — AMBIGUOUS recorded. **B** |
| assumptions | KEEP — the informal v0.1 interface list. **A** | KEEP. **A** |
| proof_or_evidence_resources | KEEP — induction on history length placed as proof route, matching key §5.1 ("履歴長帰納法はproof route"). **A** | SOURCE GAP — UNKNOWN. **C** |
| evaluation_or_decision_rules | KEEP — the "what counts as the same interface" insufficiency is priority-1 wording. **A** | SOURCE GAP — UNKNOWN. **C** |
| failure_witness | KEEP — the existence-claim/convention conflation, quoted. **A** | UNRESOLVED — no witness of its own in the excerpts; R02 marked it INFERENCE/AMBIGUOUS rather than importing E04's control argument. Correct restraint. **C/G** |
| available_branches | KEEP — UNKNOWN. **A** | KEEP — UNKNOWN. **A** |
| adopted_side_claims | KEEP — NOT APPLICABLE; A2/A3 are successors, not side claims. **A** | KEEP — UNKNOWN, with the interface-property reading noted but not asserted. **A** |
| move_taken | KEEP core (M17, M14 = key core exactly); UNRESOLVED on **M1 attached to A2** — see §4.2; KEEP M1/M4/M8 on A3 (key permits M1/M4 as a separate branch, and anchors induction as route). **A + D** | KEEP M17; M14 INFERENCE-labelled and defensible. **A/B** |
| claim_after | KEEP — two successors, each with the source's own limiting sentence attached. **A** | KEEP. **A** |
| terminal_status | KEEP — three distinct statuses; "retained as convention" is not reported as a proved equivalence. Gate item §7.5 satisfied. **A** | KEEP. **A** |
| provenance | KEEP | KEEP |
| degenerate_or_target_leakage | KEEP — quoted degeneracy for A2 ("定義したかの帰結"). One of the two cases the key's gate item 5 specifically tests. **A** | UNRESOLVED — leakage asserted by analogy with E04 while admitting the source does not connect them. Mild **E**; INFERENCE-labelled, so retained rather than corrected. |
| uncertainties | KEEP — including the diff-document isolation problem, adjudicated in §5 item 12. **C** | KEEP. **B/C** |

### 3.6 E06-a / E06-b / E06-c

| Field | E06-a | E06-b | E06-c |
|---|---|---|---|
| claim_before | UNRESOLVED — depends on whether Source A is pre-revision. R02 marked the dependence. **C/G** | UNRESOLVED — reconstructed by inversion from "降格した", INFERENCE-labelled. Rules §3 bullet 1 (claim_before not fixed) applies. **B/C** | UNRESOLVED — same, weaker. **C** |
| claim_identity | KEEP. **A** | KEEP. **A** | KEEP. **A** |
| obligation_type | KEEP. **A** | KEEP. **A** | FRAMEWORK GAP — no type covers a taxonomy claim; AMBIGUOUS recorded. **D** |
| assumptions | KEEP. **A** | KEEP (INFERENCE). **B** | SOURCE GAP. **C** |
| proof_or_evidence_resources | SOURCE GAP — UNKNOWN. **C** | SOURCE GAP. **C** | SOURCE GAP. **C** |
| evaluation_or_decision_rules | KEEP with gap — rule *existence* source-derived, rule *content* (Null C, Null D/E) unavailable. **C** | KEEP — the v0.2 epistemic posture is quoted and correctly used as a decision rule. **A** | SOURCE GAP — UNKNOWN. **C** |
| failure_witness | KEEP with gap — 「支持しなかった」 quoted; the underlying observation is not in the packet. The key's Erasure Test witness is unreachable from the packet (verified in §2.4). **C** | KEEP — Excerpt 5's existing-vocabulary reconstruction. **A** | SOURCE GAP — no witness at all; R02 correctly refused to supply one. **C** |
| available_branches | SOURCE GAP — UNKNOWN, including whether DR-1 survived. **C/G** | SOURCE GAP. **C** | SOURCE GAP. **C** |
| adopted_side_claims | KEEP — none claimed. **A** | UNRESOLVED — whether "retained as a rejected working hypothesis" is retention or abandonment. **B** |  KEEP — NOT APPLICABLE. **A** |
| move_taken | KEEP M17 (key core). **A** | KEEP M15 + M17 (key core M15/M17). Key also allows M5/M7/M14 for the field-native rewrite of Excerpt 5; R02 used M15 alone — permitted alternative, not an error. **A/B** | KEEP M17; the M14 decline is correct restraint (no reason given in source, and instructions forbid inferring researcher intent). **A** |
| claim_after | KEEP. **A** | KEEP. **A** | KEEP. **A** |
| terminal_status | KEEP — "withdrawn + negative result fixed" double label is the source's own double wording, and R02 said so. Matches key's "frozen negative result". **A/D** | KEEP. **A** | KEEP. **A** |
| provenance | KEEP | KEEP | KEEP |
| degenerate_or_target_leakage | KEEP — no claim made; the Null D/E reading is flagged INFERENCE and not asserted. **A** | UNRESOLVED — leakage asserted as INFERENCE. Defensible from Excerpt 5. **B** | KEEP — UNKNOWN. **A** |
| uncertainties | KEEP — the Source A version question is the single most consequential packet gap in the submission. **C** | KEEP. **C** | KEEP. **C** |

### 3.7 E07

| Field | Verdict | Note |
|---|---|---|
| claim_before | KEEP | H1 quoted in full, including the comparative clause about the field-native control. **A** |
| claim_identity | KEEP | **A** |
| obligation_type | KEEP | empirical + comparative, both supported. **A** |
| assumptions | KEEP | **A** |
| proof_or_evidence_resources | KEEP | Audit, control corpus, cross-chain display. Matches key AR-B1 ("frozen controlとreview procedureはevidence resources"). **A** |
| evaluation_or_decision_rules | KEEP | The preregistered §5/§6 condition and the ladder rejection rule are placed here, not in assumptions. AR-B1 says this placement is right and that the "assumption" reading is also permitted; R02 chose the primary one and did not duplicate. **A** |
| failure_witness | KEEP | Seven-item null list + Q5. **A** |
| available_branches | KEEP | M0 open / M2–M3 rejected, both source-explicit. R02 also noted that the field cannot express the difference between "left open" and "closed by rule" — a real framework observation. **A + D** |
| adopted_side_claims | KEEP | **A** |
| move_taken | **CORRECT — add M2 as a co-code** | See §4.1. M17 KEEP. M16 not codable from the packet (see below). |
| claim_after | KEEP | **A** |
| terminal_status | KEEP | "not supported / negative result fixed" + "retained as M1 (source-local)". Matches the key's terminal column exactly, including the label-collision discipline. **A** |
| provenance | KEEP | |
| degenerate_or_target_leakage | KEEP | "explicitly blocked" reading, anchored in Q5. **A** |
| uncertainties | KEEP | §5/§6 contents and the M0–M3 definitions are genuinely absent. **C** |

**M16 for E07.** The key's E07 row expects "M16 for next real-record question". The proposal that would license it is in the original at `scientific_assurance_case_02_metrology_comparison.md` §13.2 ("A real-protocol audit should sample, with permission and predetermined criteria: …"), and it is **not in any E07 excerpt in the frozen packet** (the packet draws on §4, §3, and §14). Reader 02 could not reach it. Furthermore the key's own provenance anchor §5.2 states "sourceが将来のreal-record auditや未証明bridgeを提案する場合のみ OPEN HYPOTHESIS。提案を completed move としない" — and §13.2 is a proposal in the subjunctive. The key's E07 row and the key's §5.2 anchor therefore pull in opposite directions on this item. Classification: **C** primary (packet), with a noted internal tension in the key itself. Not a reader error; not corrected.

### 3.8 E08

| Field | Verdict | Note |
|---|---|---|
| claim_before | KEEP | Both the verdict label and the effectiveness sentence quoted. **A** |
| claim_identity | KEEP | Single identity, but see §2.5: the key partitions this object differently using material outside the packet. **B/C** |
| obligation_type | KEEP | **A** |
| assumptions | KEEP | INFERENCE-labelled; thin but honest. **B** |
| proof_or_evidence_resources | KEEP | N-04 / L-01–L-03 recorded as evidence with an explicit "these are source-local labels, not move codes" warning. **A** |
| evaluation_or_decision_rules | KEEP | Internal-consistency rule + measurement requirement. **A** |
| failure_witness | KEEP | Internal contradiction with N-04. Matches key CI-P2 / EB-B2 ("evidential overclaim / internal contradiction"). **A** |
| available_branches | SOURCE GAP | Verdict A's content is absent from the packet; R02 recorded the branch's existence without inventing its content. Correct restraint. **C** |
| adopted_side_claims | KEEP | **A** |
| move_taken (M2, M14, M17) | KEEP | Key core is M2 + M14, with M15/M17 permitted where P0 is included. R02's M17 is anchored on 「当該表現を削除」 — a real withdrawal of a sentence-level claim. **A** |
| claim_after | KEEP | **A** |
| terminal_status | KEEP | **Notable:** A2 is `untested / open (not refuted)`, and R02 justified it by citing M17's own exclusion ("do not use for calling an untested claim refuted"). This matches the source's 「確認できていないこと」 exactly and matches the key's terminal column. **A** |
| provenance | KEEP | |
| degenerate_or_target_leakage | KEEP | Sense-2 leakage, but here anchored in the source's own internal-contradiction finding rather than in analogy. **A** |
| uncertainties | KEEP | The "who/what is Codex" question is a real determinant of whether the witness is internal or external. **C/G** |

### 3.9 E09-a / E09-b

| Field | E09-a | E09-b |
|---|---|---|
| claim_before | KEEP — the design plan with its stated premise. **A** | KEEP (INFERENCE) — continuation state of E09-a's A2. The key's CI-B2 says dependency alone does not fix identity and permits AMBIGUOUS here; R02 asserted continuity. Mild **E**, but the source's 「二段階にわたって」 supports it. UNRESOLVED. |
| claim_identity | KEEP. **A** | UNRESOLVED per CI-B2. **B** |
| obligation_type | KEEP — `design decision`, the one place the instruction list fits cleanly. **A** | KEEP. **A** |
| assumptions | KEEP. **A** | KEEP (INFERENCE). **B** |
| proof_or_evidence_resources | KEEP. **A** | SOURCE GAP — the check's content is not in the packet. **C** |
| evaluation_or_decision_rules | KEEP — premise test, the meta-rule 「設計どおりに進めることが、設計の目的に反する場合がある」, and the source-local priority labels, all separated from assumptions. **A** | KEEP with gap — Part IX is cited as a preregistered stopping rule but its content is unavailable. **C** |
| failure_witness | KEEP — the 14→1 count. **A** | SOURCE GAP — witness named, content absent. **C** |
| available_branches | KEEP — (ii) and (iv) as available-untaken, (iii) as explicitly rejected. Matches key AB-P1 exactly, including not listing (ii)–(iv) as moves. **A** | KEEP — UNKNOWN. **A** |
| adopted_side_claims | KEEP — NOT APPLICABLE. **A** | KEEP — S09 = comparative review. **A** |
| move_taken | KEEP M17 + M4 (key core includes M4, M17). M16 not codable from packet — see below. **A/C** | KEEP M17; M15 left AMBIGUOUS. Key lists M15 in E09's expected set; the specific sentence that would anchor it for the *downgrade* is not in the packet, so AMBIGUOUS is the correct disposition. **B/C** |
| claim_after | KEEP. **A** | KEEP — three after-claims. **A** |
| terminal_status | KEEP. **A** | KEEP — matches key's "comparative methodology terminated; review remains". **A** |
| provenance | KEEP | KEEP |
| degenerate_or_target_leakage | KEEP — "explicitly blocked" reading anchored in the meta-rule. **A** | KEEP — UNKNOWN. **A** |
| uncertainties | KEEP. **C** | KEEP — including the cross-subepisode branch-tracking problem. **D** |

**M16 for E09.** The key's WS-P2 anchors M16 on 「これは「比較研究プログラム」ではなく「一つの記述形式についての限定的な問い」である」. Verified: that sentence exists in the original at `p0_generic_standards_baseline_v0.1.md` line 202 and is **not in any E09 excerpt in the frozen packet**. Unlike the E07 case, this sentence records a completed reframing rather than a proposal, so M16 would be well-founded with full source access. Reader 02's decline is correct *relative to the packet* and would be wrong relative to the original. Classification: **C** primary. Not corrected — correcting it would require importing text the blind reader was not given.

### 3.10 E10

| Field | Verdict | Note |
|---|---|---|
| claim_before | UNRESOLVED | Reconstructed by inversion from the C1 verdict, INFERENCE-labelled, and flagged in uncertainties. Rules §3 bullet 1 applies. **B/C** |
| claim_identity | KEEP | **A** |
| obligation_type | KEEP | novelty + comparative. **A** |
| assumptions | KEEP | The §0 self-limitation ("比較のためのメタ記述であって標準用語ではない") is placed as an assumption/scope statement rather than as a witness — correct, and it matters for the leakage reading. **A** |
| proof_or_evidence_resources | KEEP | G1 statement, G2's metatheorem type, the 21-theorem comparison. Matches key §5.1's anchoring of Q/c.e./consistency as adopted-theorem assumptions and diagonal lemma as resource — R02 did not promote any of them to assumptions or to moves. Gate item §7 "Do not treat diagonal proof as move" satisfied. **A** |
| evaluation_or_decision_rules | KEEP with gap | Ladder criteria quoted from the verdict reasoning; ladder definitions absent. **A/C** |
| failure_witness | KEEP | "no proof-theoretically independent classification; lower diagnostic resolution". **A** |
| available_branches | KEEP | C2/C3 as explicitly rejected. **A** |
| adopted_side_claims | KEEP | C1 as retained metaphor, with residual value preserved — matching M15's own note that absorption does not erase residual value. **A** |
| move_taken (M15, M17, M14) | KEEP as coded; **M12 → UNRESOLVED** | See §4.1. The three coded moves are all in the key's expected set. |
| episode_boundary | **CORRECT → AMBIGUOUS** | See §2.8. |
| claim_after | KEEP | **A** |
| terminal_status | KEEP | "demoted / not raised" + "retained as metaphor" + "negative result fixed" — three distinct statuses, matching the key's terminal column. **A** |
| provenance | KEEP | |
| degenerate_or_target_leakage | KEEP | "explicitly blocked" reading anchored in 「Gödel が『閉包反転』の実例だと証明されたのではなく」. **A** |
| uncertainties | KEEP | **C** |

### 3.11 E11

| Field | Verdict | Note |
|---|---|---|
| claim_before | KEEP | The §0 central hypothesis quoted, including the kill-test declaration. **A** |
| claim_identity | KEEP | The meta-label S2 is kept distinct from the mathematical reflection principles — exactly what key CI-B1 requires ("その対象である reflection principles を一命題にしない"). **A** |
| obligation_type | KEEP | comparative claim. **A** |
| assumptions | KEEP | Γ recorded as scope definition, not as a property of T — matching AR-P2's positive anchor. **A** |
| proof_or_evidence_resources | KEEP | T⁺ construction, scope-dependence observation, and the Löb clarification are all resources, and diagonal-lemma-type items are not promoted to assumptions (AR-P2). **A** |
| evaluation_or_decision_rules | KEEP | Kill test recorded as an evaluation stance, explicitly **not** as a move. **A** |
| failure_witness | KEEP | **A** |
| available_branches | KEEP | UNKNOWN — the source declares it will not maintain S2, and offers no rescue. **A** |
| adopted_side_claims | KEEP | **A** |
| move_taken (M14, M2) | KEEP; M3 UNRESOLVED; M17 UNRESOLVED; M6/M12 UNRESOLVED | Key meta-episode set is M2/M3/M14/M17. R02 took M2+M14, left M3 as an explicit AMBIGUOUS, and did not consider M17. See §4.1–4.2. |
| alternative_segmentations | **CORRECT — add the T→T⁺ sub-episode** | See §2.8. |
| claim_after | KEEP | **A** |
| terminal_status | KEEP | "demoted to limited form" with the explicit note that the kill test did not kill S2 outright. Matches key's "S2* local only". **A** |
| provenance | KEEP | |
| degenerate_or_target_leakage | UNRESOLVED | Marked SOURCE-DERIVED, but "target leakage" is R02's vocabulary; the source says the label 「型とレベルの差を隠す」. The phenomenon is source-derived, the classification is not. Mild **E** on the provenance label; see §4.4. |
| uncertainties | KEEP | Including the correct refusal to assume E11's S2* and E12's S2* are the same ladder. **A/G** |

### 3.12 E12-a / E12-b

| Field | E12-a | E12-b |
|---|---|---|
| claim_before | UNRESOLVED — reconstructed by inversion from 「万能スカラーではない」; INFERENCE-labelled and flagged. Rules §3 bullet 1. **B/C** | KEEP — UNKNOWN/AMBIGUOUS recorded *in the field itself*, which is the most conservative disposition in the submission. **A/C** |
| claim_identity | KEEP. **A** | UNRESOLVED. **C** |
| obligation_type | KEEP. **A** | KEEP — AMBIGUOUS. **B** |
| assumptions | KEEP — the suppressed-parameter list placed as assumptions of the corrected claim. Key §5.1 calls the same list a "calibration package"; see §4.2. **A/D** | KEEP. **A** |
| proof_or_evidence_resources | KEEP — bridge-theorem convergence for the standard package. **A** | KEEP. **A** |
| evaluation_or_decision_rules | KEEP with gap. **A/C** | KEEP with gap — the A-ladder is absent. **C** |
| failure_witness | KEEP — the six-item non-entailment list, quoted. **A** | UNRESOLVED — R02 itself notes this is a coverage confirmation rather than a failure. Honest. **B/D** |
| available_branches | KEEP — bridge theorems placed here and explicitly **not** in `move_taken`, which is exactly what key AB-B2 requires ("M8/M9/M10を`move_taken`にしない"). AB-B2 also says the assumptions-vs-branch placement may stay unresolved; R02 chose branch and said so. **A/B** | KEEP — A3 upgrade and the Turing–Feferman identification, both explicitly rejected in source. **A** |
| adopted_side_claims | KEEP. **A** | KEEP. **A** |
| move_taken | KEEP M14, M2, M3, M4 (all in key's expected set); **M1 UNRESOLVED** (§4.2); M13 decline permitted (key says 併記できる). **A + D** | KEEP M14; M15 beyond the key but source-compatible; **M12 UNRESOLVED** (§4.1). **A/B** |
| claim_after | KEEP. **A** | KEEP. **A** |
| terminal_status | KEEP — "withdrawn" for the universal reading and "retained in restricted form" for S2*, held apart. This is the exact double-fixation the key's WS-B2 describes. **A** | KEEP. **A** |
| provenance | KEEP | KEEP |
| degenerate_or_target_leakage | KEEP — the 「|T|=α」 shorthand leakage is source-anchored in the opening. **A** | KEEP. **A** |
| uncertainties | KEEP — including R02's own flag on the M1/M3/M4 decomposition granularity. **D** | KEEP — including "is this a transition at all". **B/G** |

---

## 4. Focused audits

### 4.1 The "considered and NOT coded" decisions

Reader 02 declined six codes on one stated principle: *a passage that describes object-level structure is not thereby a formation move of the research episode.* The principle itself is sound and is anchored in three places the reader could see or could not see:

- coder instructions, "Items that are not automatically moves": "A completed proof type is not automatically the operation that made the obligation closable."
- adjudication rules §3, final bullet: "mathematical operation が source 内で説明されているだけか、当該 episode で実際に採用された move かが境界依存" — i.e. **boundary-dependent, not universally false**.
- key AB-B1: under a meta-vocabulary episode "M6 は説明対象であって `move_taken` とは限らない".

So the principle is valid but it is *conditional on the episode boundary*. That is the axis on which each decline must be judged.

| Decline | Verdict | Class |
|---|---|---|
| **E02-a — M15** | **UPHELD.** quine / Kleene / Breuer / Wolpert are used to *refute* the claim and to show that existing impossibilities carry extra conditions; nothing is returned to them as an equivalent. The key's E02 row asks for M17/M14 and does not expect M15. Contrast E01 and E03, where the source says the claim *is* the existing setting — R02 coded M15 there. The discrimination is correct. | **A** |
| **E07 — M15** | **UPHELD.** The seven-item null list is the empirical result of the preregistered comparison, i.e. a witness. Coding it as absorption would convert an outcome into an operation. R02 recorded the alternative reading as AMBIGUOUS rather than suppressing it. | **A/B** |
| **E07 — M2** | **NOT UPHELD — see correction below.** | **F/D** |
| **E10 — M12** | **UNRESOLVED, not corrected.** Under R02's single meta-episode boundary the decline follows; under the Gödel-II sub-episode boundary (which key EB-B1 explicitly permits, calling E10 "意図的に composite") M12 applies, and the key's §5.1 anchor ties the external-consistency-to-internal-unprovability passage to M12. Since the code varies with the boundary, rules §3 forbids resolution. What *is* correctable is the boundary flag (§2.8). | **B** primary, **F** on the flag |
| **E11 — M6** | **UPHELD.** R02's reasoning coincides with key AB-B1 almost verbatim, including the requirement to fix the boundary first. Note that AB-B1 calls this "E11 で最も重要な adjudication point"; the reader reached the intended distinction blind. | **A/B** |
| **E12-a — M13** | **UPHELD as permitted.** Key WS-B2 says M13 "併記できる" (may be co-recorded), which is permission, not requirement — even though the E12 row lists M13 first. R02 additionally kept bridge theorems out of `move_taken`, which key AB-B2 requires explicitly. | **B** |
| **E12-b — M12** | **UNRESOLVED.** Same structure as E10. R02 applied one principle consistently across E10 / E11 / E12-b; these are one decision instantiated three times, not three independent misses, and should not be counted as three. | **B** |

**Correction (E07, `move_taken`): add M2 as a co-code alongside M17.**
Grounds, argued from source and instructions rather than from the key: adjudication priority 2 fixes the exact before/after conclusion. The before-conclusion asserts a diagnostic finding that the field-native control does not reach as clearly or as early; the after-conclusion asserts organizational value with "no demonstrated diagnostic or methodological added value", about the same object (the generic audit). That is a weakening of what is concluded, not a change of object class, so M2's exclusion clause does not bite. R02 declined on the ground that value-kind change is not obviously value-strength change; that is a real hesitation, but the source's own ladder places the after-claim below the before-claim on one axis, and the source states the reduction in its own words ("It changed presentation and cross-chain visibility only").
**Caveat preserved:** under a strict reading of rules §1, M-code assignment sits at priority 5 (inference), and one may hold that no M-code is ever "SOURCE-RESOLVED" and therefore correctable under §2.5. On that reading this item is UNRESOLVED rather than corrected. Both dispositions are recorded; the reader's own AMBIGUOUS note stands either way.

### 4.2 M1 / M2 / M3 / M4 decomposition

No primary code is forced anywhere in this section, per the brief and per key WS-B1 ("primary を強制しない").

**E02-b (M1 + M4, M2 declined).** Matches the key's side-claim expectation (M1/M4) exactly. The M2 question — whether "generally impossible" → "r cannot be injective" is a conclusion weakening in its own right or merely the shadow of the added conditions — is the same question key WS-B1 leaves open for the finite-refinement case. **B. KEEP both the codes and the decline.**

**E05-a (M1 on A2, and M1 + M4 + M8 on A3).** The A3 bundle is well founded: M4 for the turn-based system restriction, M1 for the commutation and declared-update conditions, M8 for the history-length induction, each with its own citation, and key §5.1 anchors the same three items in the same three roles. The A2 attachment is the problem: the full interface `I` is a *stipulation* that makes the equivalence analytic, and calling a stipulation an "assumption strengthening of the claim" is the closest available fit rather than a correct description. R02 saw this and reported it as defect #5/#10 in its own list. **UNRESOLVED / FRAMEWORK GAP (D).** Not corrected: no M-code covers "the claim became definitional", and inventing one is forbidden.

**E11 (M14 + M2, M3 left AMBIGUOUS, M17 not considered).** The M3/M14 overlap is genuine: Γ is a formula-class scope selector (M3 territory) and local-vs-uniform is named inside M14's own definition. Key WS-B2's note says the S2→S2* relabel may be M2 or M14 and lists M3 in the meta set, so all three dispositions are permitted. **B. KEEP.** Separately, R02 never considered **M17** for E11 even though its own terminal status reads "demoted", and M17 explicitly covers demotion; the key lists M17 in the meta-episode set. This is not corrected, because instructions state that status labels are not automatically M-codes, and M2 already carries the operation. Recorded as an **UNRESOLVED co-code candidate (B)**.

**E12-a (M14 + M2 + M4 + M3 + M1).** The M2/M3/M4/M14 quartet matches the key. The fifth code, M1 for "notation, base/metatheory, reduction notion", is the one place where R02 codes more than the source clearly licenses: the source says these were **suppressed by a shorthand** and must be disclosed, and disclosure of a parameter that was always operative is not obviously the addition or strengthening of a condition. Key §5.1 calls the same list a "calibration package", i.e. definitional scope. **D primary (no code expresses "make suppressed parameters explicit"), E secondary (mild over-assignment). UNRESOLVED.** R02 flagged the decomposition granularity itself as uncertain, which is the correct level of self-report.

**Positive finding.** The instructions' M3-versus-M4 test ("ask what the restriction ranges over") was applied explicitly and correctly in E02-b, E05-a and E12-a, with separate before/after citations for each code as the instructions require. Where the source did not fix the range, R02 used AMBIGUOUS rather than guessing. This part of the codebook did its job.

### 4.3 Role ambiguity

| Boundary | Instance | Reader 02's handling | Class |
|---|---|---|---|
| assumption vs proof/evidence resource | E12-a suppressed parameters (notation, base/metatheory, formula class, reduction notion) placed in `assumptions` | Chosen without a role-ambiguity flag. Key AR-B2 mandates AMBIGUOUS for exactly this family of items when the theorem version is not fixed. | **B**; UNRESOLVED. Not corrected — the source does present them as parts of the claim's statement. |
| assumption vs proof/evidence resource | E10 Gödel conditions (Q, c.e. axiomatization, consistency) vs diagonal lemma | Correctly separated; nothing promoted. Matches AR-P1. | **A**; KEEP |
| assumption vs evaluation rule | E07 preregistered §5/§6 conditions | Placed in `evaluation_or_decision_rules`. AR-B1 names this the primary reading and permits the "assumption" reading; R02 chose one and did not duplicate. | **A**; KEEP |
| assumption vs evaluation rule | E05-a interface specification `I` | Recorded in both senses in R02's own §3.5, but entered once in the block. | **D**; UNRESOLVED |
| available branch vs scope condition | E04 fresh preparation | Entered as branch with an explicit role note. Key requires only that it not be the main move — satisfied. | **B**; UNRESOLVED |
| available branch vs scope condition | E02-b four defeater conditions | Entered as assumptions with an explicit role note; not duplicated. Rules §3 bullet 4 makes this non-resolvable. | **B**; UNRESOLVED |
| available branch vs adopted side claim | E03 "prove loss for a concrete channel" (branch) vs S03 "loss must be proved" (side claim) | Written apart; R02 states the separation is its own reconstruction. | **D**; UNRESOLVED |
| available branch vs adopted side claim | E02 Breuer/Wolpert extra conditions — available in E02-a, partly adopted in E02-b | Recorded in both blocks with no link, because no link field exists. | **D**; UNRESOLVED |
| available branch vs adopted side claim | E09 option (iv) available at P0, effectively taken at P1-reduced | Same; R02 reported the missing linkage. Key AB-P1 anticipates the transition and the form cannot express it. | **D** primary, **C** secondary |
| retained claim vs evaluation rule | E03 S03 (「証明しなければならない」) | Entered once as a side claim, with the dual role noted in the evaluation field. This is the only handling that satisfies the no-duplication rule without losing information. | **D**; UNRESOLVED |
| retained claim vs evaluation rule | E12-a bridge-theorem requirement | Entered as available branch, per AB-B2's explicit instruction not to make it a move; AB-B2 leaves assumption-vs-branch open. | **A/B**; KEEP |

Summary: of eleven role boundaries, one is source-resolved and correctly resolved (E07/AR-B1), one is source-resolved and correctly separated (E10/AR-P1), four are genuine source ambiguities correctly left open, and five are framework boundaries where the form's no-duplication rule forces information loss. **No role assignment in the submission is adjudicably wrong.**

### 4.4 `degenerate_or_target_leakage`

Reader 02 operationalized an undefined field in two senses. Auditing each against the three documents:

**Sense 1 — the conclusion is embedded in the definition or the premise.**
Fully supported, though not by anything the reader was allowed to read. Adjudication rules AA-P1 quotes the *identical* E03 sentence and names it "conclusion-as-definition による target leakage / degenerate rescue"; AA-P2 adds quotient laundering; gate item §7.5 makes E03 and E05 the designated test cases. Reader 02 flagged E01, E03 and E05-a under this sense — E03 and E05-a being exactly the two the gate names. **Convergence with the withheld definition, reached blind. Class A on the instances; the definition's absence from the reader-facing file is a protocol defect (§5 item 1).**

**Sense 2 — the nominal target absorbs a result actually produced by other factors.**
Partially supported. It is adjacent to AA-P2 (what you quotient by decides the conclusion) and to the substance of the key's E04 core (the obstruction is not internality-specific), but the rules file the neighbouring phenomena under a *different* flag, "added arbitrariness" (§4.6, A = typed UNKNOWN / mixed), and never define sense 2 under this name. Reader 02 used it in E02-b, E04, E05-b, E06-b, E08, E11, E12-a.

**Disposition.** This is an **instruction gap / framework boundary (D)**, not coder error (**not F, not E**), for three reasons: (i) the field appears in the required submission block with no definition anywhere in the two files the reader was permitted to read; (ii) the reader disclosed the improvisation explicitly and named it as defect #1 of its own list; (iii) the improvisation never propagated — no move, status, claim or role in the submission depends on it.

**One narrow exception.** E11 marks the leakage `SOURCE-DERIVED`. The phenomenon is source-derived (「型とレベルの差を隠す」), but the classification into a category the source does not use cannot be. Mild **E** on that one provenance label. E05-b's analogy-based leakage is correctly marked INFERENCE and needs no change.

**Additional provenance finding (independent of the field above).** Reader 02 used `SOURCE-DERIVED`, `UNKNOWN`, `AMBIGUOUS`, `INFERENCE` and `NOT APPLICABLE`, but used **`OPEN HYPOTHESIS` zero times** in 18 blocks, although the instructions define it and at least two sites invite it: E04's `[SYNTHESIS]` research direction (recorded as status `open` but provenance SOURCE-DERIVED/INFERENCE) and E12-a's unproved bridge theorems (recorded as an available branch). Key §5.2 reserves OPEN HYPOTHESIS for precisely these. Classification: **F minor** (an available label went unused where it fits), **D** secondary (the instructions define OPEN HYPOTHESIS as a provenance label while the natural home for these items is the status or branch field, so the label has no clear attachment point). Recorded, not corrected.

---

## 5. Audit of the 13 defects reported in Reader 02 §3.7

Categories: **real protocol defect** / **real framework boundary** / **source-corpus design issue** / **reader misunderstanding** / **not enough evidence**.

| # | Reported defect | Verdict | Grounds |
|---|---|---|---|
| 1 | `degenerate_or_target_leakage` undefined | **real protocol defect** | Confirmed. The field is required by the submission block; its definition exists only in adjudication rules §4.6 (AA-P1/AA-P2), which readers are forbidden to open. The concept is load-bearing — gate item §7.5 tests it — so a reader-facing field carries reader-inaccessible semantics. |
| 2 | `move_taken` not indexed per after-claim | **real protocol defect** | Confirmed and anticipated by the key itself: CI-P1 says "必要なら二つの after-branch を別行にする", i.e. the intended answer needs a per-branch row the form does not have. Bites in E05-a and E09-a. |
| 3 | `A1/A2` collides with source-local `A2`, `M0–M3`, `S2*`, `C1`, `D`, `N-04` | **real protocol defect**, low severity | Instructions warn only about source-local "M1". Key §6.2 lists this exact misreading as an expected inter-reader failure and flags E07 as "label collision". R02 self-mitigated with per-block warnings; another reader might not. |
| 4 | `claim_identity` vs `claim_before` never distinguished | **real protocol defect**, minor | Confirmed: Step 1 is titled "Fix claim identity and obligation" but describes only how to write the claim. The field pair is undefined. R02's ID reading is reasonable and harmless. |
| 5 | provenance granularity: `dependencies` covers three fields | **real protocol defect** | Confirmed, and self-contradictory: the same section directs "apply provenance at the smallest practical unit". Bites wherever the three dependency roles have different provenance (E06-a is the clearest). |
| 6 | Step 3 side-claim IDs vs Step 4 `A1/A2` labels | **real protocol defect**, minor | Confirmed: Step 3 says use the side claim's own ID under `claim_after` and `terminal_status`; Step 4 says label after-claims A1, A2. R02's `A2 [S01]` compromise loses nothing. |
| 7 | no rule for what to do after recording an alternative segmentation | **real protocol defect** at the reader-facing layer | The instructions say to record both and mark AMBIGUOUS but not whether to code both, nor where to state which was adopted. The rule exists — adjudication rules §2.5, "両案を残す" — in the withheld file. R02's choice (code one, record the other with adoption grounds) matches §2.5's intent. |
| 8 | no cross-subepisode link field | **real protocol defect** primary, **real framework boundary** secondary | Confirmed by a case the key itself constructs: AB-P1 requires splitting P0 from P1-reduced *because* option (iv) changes status across the split, and the form then provides nowhere to record that the same branch changed status. Same in E02-a→E02-b. |
| 9 | may a `claim_before` be taken from another corpus item (E01→E02)? | **source-corpus design issue** primary, **not enough evidence** secondary | The corpus slices one working note into items by Phase, cutting a running claim; Step 0 says an item is a container but not whether containers may be crossed. Whether M7 applies to the static→dynamic rewrite cannot be settled from the packet. |
| 10 | `obligation_type` has no slot for a definitional convention or a taxonomy claim | **real framework boundary** | Confirmed for both. The key treats 規約的同値 as a first-class outcome (CI-P1) while the type list has no such entry; E06-c's deleted taxonomy has no type at all. |
| 11 | no rule for reconciling source status words with the suggested vocabulary | **real framework boundary**, minor | The instructions' "may follow the source" is permissive by design; the gap appears only when both vocabularies are in play (E06-a carries "withdrawn" and "frozen negative" together). Key §6.2 lists status-collapse as an expected disagreement, which implies the reconciliation is meant to stay open. |
| 12 | isolation rule vs `*_v0.1_to_v0.2_diff.md` source paths | **source-corpus design issue** primary, **real protocol defect** secondary | A genuine contradiction: the corpus lists diff documents as returnable original sources while the same instructions ban trajectory summaries. Sharpened by the fact that the key's own CI-P1 and EB-P1 anchor on those very diff files — the evidence base for the expected coding sits in the zone the reader could not safely enter. |
| 13 | no procedure when an excerpt is structurally insufficient | **source-corpus design issue** | Confirmed empirically, and it is the most consequential of the thirteen. See §6.1: three key-expected codings rest on text absent from the packet. Combined with #12, the reader has no admissible route to that text. |

None of the thirteen is a reader misunderstanding. Two (#1, #7) are cases where the missing rule exists but only in the withheld file.

---

## 6. Relation to the withheld answer key

The key states it is "唯一の正解列ではない". It is used here as one source-anchored reference. No counts, no rates.

### 6.1 Three key-expected codings are unreachable from the frozen packet

Verified against the originals during this adjudication:

| Item | Key expects | Anchor text | In packet? |
|---|---|---|---|
| E06 | Erasure/prior-art reconstruction as the witness | `deferred_resolution_case_01_gst_v0.2.md` §16 — "固有語彙を消しても情報は失われず…methodological construct として独立しない" | **No.** No E06 excerpt mentions the Erasure Test. |
| E07 | M16 for the "next real-record question" | `scientific_assurance_case_02_metrology_comparison.md` §13.2 — "A real-protocol audit should sample…" | **No.** Packet draws on §4, §3, §14 only. |
| E09 | M16 for the reframing to a limited question | `p0_generic_standards_baseline_v0.1.md` line 202 — "これは「比較研究プログラム」ではなく「一つの記述形式についての限定的な問い」である" | **No.** Packet draws on §§5–6 tables and the (iii) note. |

These are **corpus-design facts, not reader shortfalls**, and they interact with defects #12 and #13: the reader is told it may return to source when an excerpt is insufficient, but cannot know which absent sentence to look for, and for E06 the route runs through a diff document of contested admissibility.

A further tension inside the key itself: the E07 row expects M16, while the key's own provenance anchor §5.2 says a proposed future audit is OPEN HYPOTHESIS and "提案を completed move としない" — and §13.2 is written in the subjunctive. On the key's own rule, M16 for E07 is questionable even with full source access.

### 6.2 Qualitative relation, episode by episode

| Item | Relation |
|---|---|
| E01 | **Expected core matched** (M15, M17) **+ permitted alternative taken** (M14). Terminal statuses match the key's column. |
| E02 | **Expected core matched** on both sides (main M17/M14; side M1/M4). **Finer than the key row but explicitly permitted** — AB-P2 allows two-episode treatment. The key's central requirement ("Do not merge silently") is met. |
| E03 | **Expected core matched exactly** (M14, M15, M17). Permitted M4 not taken. The target-leakage flag coincides with AA-P1. |
| E04 | **Expected core matched** (M14, M15, M17). **Permitted alternative not taken** (M13 on the retained comparison). Fresh preparation correctly kept out of `move_taken`. |
| E05 | **Expected core matched** (M14, M17; M1/M4 as a separate branch; induction as route). **Finer than the key** (E05-b extracted). **Key itself leaves the one-vs-two episode question ambiguous** (CI-P1 note), so the refinement is inside the permitted zone. |
| E06 | **Expected core matched** (M15, M17). **Finer than the key** (three subepisodes; EB-P1's note permits sub-episodes). **Permitted alternatives not taken** (M5/M7/M14 on the field-native rewrite). **Key's witness unreachable from packet.** |
| E07 | **Partly matched:** M17 and the label-collision discipline match; **weaker than the key on M2** (adjudicated in §4.1 — correction issued with a caveat); **M16 unreachable from packet, and questionable on the key's own §5.2 rule.** |
| E08 | **Expected core matched** (M2, M14; plus M17 anchored on the sentence deletion). **Different partition than the key's** (C-1/C-2 are outside the packet), source-compatible on what was visible. |
| E09 | **Expected core partly matched** (M4, M17). **M15 left AMBIGUOUS** where the key expects it; **M16 unreachable from packet.** Segmentation matches the key's requirement to split P0 from P1-reduced. |
| E10 | **Expected core partly matched** (M14, M15/M17). **M12 not taken — boundary-dependent, and the key itself flags E10 as "ambiguous composite".** The adjudicable point is the missing boundary flag, not the missing code. Diagonal proof correctly not treated as a move. |
| E11 | **Expected core partly matched** (M2, M14; M3 left open, which the key permits; M17 not considered). **The M6 decline coincides with the key's own AB-B1 reasoning.** Gate item §7.6 (same-T reflection vs external extension vs metalevel) satisfied. |
| E12 | **Expected core matched** (M14, M2, M3, M4). **M13 declined — permitted** ("併記できる"). **M12 not taken — boundary-dependent.** **Stronger than the key on M1** (§4.2) and on M15 in E12-b (source-compatible, key silent). |

No episode is stronger than the key in a way that overclaims a result: the two "stronger" entries are extra codes on retained claims, not upgrades of any status. No episode collapses a `withdrawn` and a narrow remnant into one status — the failure mode key §6.2 predicts most often.

---

## 7. Final classification

### A. Clear coding errors (correctable from source + instructions)

1. **E10 `episode_boundary` recorded as settled** while the same block makes a move code depend on that boundary. Correction: mark AMBIGUOUS and retain the Gödel-I / Gödel-II / C1-verdict composite reading. (§2.8)
2. **E07 `move_taken` missing M2.** Correction: add M2 alongside M17 — with the recorded caveat that under a strict priority-5 reading of the adjudication rules, M-code assignments may be held non-correctable, making this UNRESOLVED instead. (§4.1)
3. **E11 `alternative_segmentations` omits the `T → T⁺` sub-episode**, which is filed only inside a move-field note. Correction: record it as a retained alternative. (§2.8)
4. **`OPEN HYPOTHESIS` never used** where at least two sites invite it (E04 A3, E12-a bridge theorems). Minor. (§4.4)

That is the complete list. Everything else that differs from the key is classified below rather than corrected.

### B. Genuine ambiguity (readers may legitimately diverge)

- Segmentation of E02, E04, E05, E06, E08 — all five with alternatives already recorded by the reader.
- E10 and E11 boundary choices, and the M12 / M6 codes that follow from them.
- E12-b: whether the A2 verdict is a transition at all.
- M2 co-coding in E02-b; M3 in E11; M17 in E11; M13 in E12-a; M15 in E09-b.
- Role boundaries: E02-b defeaters (assumption vs branch), E04 fresh preparation (branch vs scope), E12-a suppressed parameters (assumption vs resource).
- E06-b: whether "retained as a rejected working hypothesis" is retention or abandonment.
- E09-b claim identity relative to E09-a (key CI-B2 permits AMBIGUOUS here).

### C. Packet defects (information the reader was not given)

- **Source-local ladders undefined:** Null C / Null D/E (E06), M0–M3 (E07), D 相当 / Part IX / NONEVAL / RET-DOWN / L2-L3 (E09), C1–C3 (E10), S1/S2/S2* (E11), A0–A3 (E12).
- **Preregistration internals absent:** metrology §5 falsification and §6 success conditions (E07).
- **Verdict alternatives absent:** hydrology verdict A's content (E08); C-1 and C-2 changes (E08).
- **Version identity unresolved:** whether `deferred_resolution_case_01_gst.md` is the pre-revision text (E06) — the single most consequential gap, since `claim_before` depends on it.
- **Witness content absent:** what the P1-reduced check observed (E09); what "Codex" is (E08); what the GST series failure consisted of (E06).
- **Three key-expected codings rest on text outside the packet** (§6.1).
- **Structurally insufficient excerpts:** E08 Excerpt 1 (a heading), E06 Excerpt 2 (a table row).

### D. Framework boundaries (expressible only unnaturally in the current form)

- No code or type for **a claim becoming definitional** (E05-a A2).
- No code for **disclosing suppressed parameters** as distinct from adding conditions (E12-a).
- No code for **deleting a classification scheme** (E06-c) or **renaming a verdict** (E08).
- No type for **definitional convention** or **taxonomy claim** (`obligation_type`).
- No slot binding **a move to a specific after-claim** (E05-a, E09-a).
- No slot **linking subepisodes**, so a branch that changes status across a split is unrecordable (E09, E02).
- No way to distinguish a branch **left open** from one **closed by rule** (E07 M0 vs M2/M3).
- The **no-duplication rule forces information loss** where one sentence genuinely carries two roles (E03 S03; E05-a interface `I`).
- `degenerate_or_target_leakage` **undefined at the reader-facing layer**, with sense 2 not defined anywhere.
- **Provenance referent unfixed** for `move_taken` — operation or code label (§3.0).

### E. Useful negative results (preserve as-is; do not engineer away)

1. **The object-level / formation-move boundary is real and boundary-dependent, and a careful reader will refuse the same codes three times over.** R02 declined M6, M12, M12 on one consistent principle that coincides with the key's own AB-B1. The lesson is not that the reader missed M12 twice; it is that under a meta-label episode boundary these codes are genuinely not available, and the form has no way to say "this code exists at another boundary".
2. **An undefined field was independently reconstructed in the sense the withheld rules define** (sense 1 = conclusion-as-definition), and improvised in a second sense the rules file elsewhere. This is evidence about how much of the framework is carried by the withheld document rather than by the reader-facing one.
3. **Three expected codings are unreachable from the frozen excerpts.** That is a measurement about the packet, and it would silently reappear as "inter-reader disagreement" if the packet were used unchanged and the gap were not recorded.
4. **The M3-versus-M4 rule works**; the M1/M2 boundary against M3/M4 does not resolve on its own and required AMBIGUOUS in three separate places.
5. **Role separation survived only by leaving one role unrecorded.** The instruction "record AMBIGUOUS; do not duplicate" is followable, but its cost is a systematically under-populated `evaluation_or_decision_rules` field wherever a retained claim doubles as a rule.
6. **Every terminal status in 18 blocks was kept separate per after-claim** — the failure mode the key predicts most often did not occur, on any episode, including the three-status cases (E04, E10) .

---

## 8. Gate decision

### Verdict: **G1 — running a blind Reader 03 on v0.1.1 is worthwhile, with the defects recorded rather than repaired.**

Judged against the three criteria in the brief, and not against agreement:

**(i) Can a reader reconstruct the transition core from the source?** Yes, in all twelve items. Every block carries a source-derived before, witness, after, and explicit status, or an `UNKNOWN` tied to a named missing item. The four items with the thinnest excerpts (E06, E08, E09, E12-b) still yielded the correct terminal statuses. Adjudication-rules gate item §7.2 is met.

**(ii) Can disagreement causes be described in the existing categories?** Yes. Every divergence in this note landed in `claim identity`, `episode boundary`, `assumption-resource`, `M2-M3-M4`, `actual-available`, `provenance`, or `status`. No new category was needed, and no new move code was tempting enough to invent. Gate items §7.3, §7.4, §7.8, §7.9, §7.10 are met.

**(iii) Do instruction defects dominate the coding results?** No — and this is the decisive point. The thirteen confirmed defects changed **where** things were recorded (which field, which block, which note), not **what** was reconstructed. Not one of them altered a claim, a witness, a status, or a withdrawal. The two designated leakage traps (E03, E05) were both caught, satisfying §7.5; the E11 reflection distinction was preserved, satisfying §7.6.

**Conditions attached to G1** (records, not repairs, and not proposed schema changes):

1. Reader 03 must receive the **same** v0.1.1 files unchanged. The freeze rule forbids amending the packet mid-test, and the packet defects in §7C are themselves part of what this test measures.
2. This note must travel with the submission as **self-adjudication**, not independent adjudication (§1.4). If the protocol requires an independent adjudicator, §§2–7 should be re-derived by another party before any cross-reader comparison is attempted.
3. The three unreachable key codings (§6.1) should be recorded as packet facts **before** Reader 03 submits, so that a second reader's identical absence is not later read as inter-reader disagreement.
4. Adjudication-rules gate item §7.1 refers to *all readers*; it remains open until at least one further independent submission exists. G1 authorizes running Reader 03, not passing the Phase-0 gate.

**Why not G2.** G2 would be justified if the packet gaps prevented reconstruction of the transitions themselves, or if the coding output were being driven by form defects rather than by the sources. Neither holds: the gaps are concentrated in *ladder definitions and witness details* while the *transitions* remained recoverable, and the form defects displaced information without corrupting it. Raising agreement is explicitly not a permitted reason to revise, and no argument for G2 survives once that motive is excluded.

---

**End of adjudication note.** No existing file was modified. No move code, taxonomy, score, geometry, agreement rate, field schema, or v0.1.2 design was introduced.
