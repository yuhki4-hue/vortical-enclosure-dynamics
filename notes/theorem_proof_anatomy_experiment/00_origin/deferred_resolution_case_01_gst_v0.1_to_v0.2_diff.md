# GST Case 01 v0.1 → v0.2 Revision Ledger

**Source:** [deferred_resolution_case_01_gst.md](./deferred_resolution_case_01_gst.md)  
**Revised note:** [deferred_resolution_case_01_gst_v0.2.md](./deferred_resolution_case_01_gst_v0.2.md)  
**Review inputs:** [Claude Code review](./deferred_resolution_case_01_gst_adversarial_review_claudecode.md); [Codex review](./deferred_resolution_case_01_gst_adversarial_review_codex.md)  
**Revision type:** conservative negative-result freeze  
**Date:** 2026-08-16

## 1. Revision rule

v0.1 は変更・削除していない。v0.2 は、両敵対的査読を revision input としつつ、一次資料と field-native reconstruction を優先して新規作成した。

Disposition は次を意味する。

- **accepted:** 査読指摘を独立確認し、修正へ採用。
- **partially accepted:** 問題の方向は採用したが、範囲・用語・結論を限定。
- **rejected:** 一次資料またはより精密な区別と衝突したため不採用。
- **reframed:** 問題を認めつつ、査読の処方とは別の記述へ変更。

Claim-strength は v0.1 と比べた主張強度の変化であり、文章量の変化ではない。

---

## 2. Executive change summary

| Area | v0.1 | v0.2 | Net effect |
|---|---|---|---|
| Overall result | weak positive result | negative result | decreased |
| Deferred Resolution | provisional independent concept | rejected historical search label | decreased |
| Five-level taxonomy | case classification device | deleted | decreased |
| A→B/C | weak boundary relocation | reference / nuisance uncertainty moved into joint estimand | more precise, less general |
| Gauge | mixed equivalence vocabulary | quotient identifiability separated from reporting choices and misspecification | differentiated |
| Later extensions | linear Stage E | parallel model-specific branches | linear claim removed |
| Ontology | “ontological closure” weak claim | model adequacy / representational uniqueness only | decreased |
| Assurance provenance | full map | no independent diagnostic effect in this case | decreased |
| Final status | working positive case | frozen negative baseline | frozen |

---

## 3. Detailed diff ledger

| # | Previous statement / v0.1 location | Revised statement / v0.2 location | Claude review input | Codex review input | Primary-literature verification | Disposition | Claim strength |
|---:|---|---|---|---|---|---|---|
| 1 | §1.1, §19, §22: “DR-1 — Weak relocation” is the best case classification | Abstract, §§16–18, §22–23: hypothesized recurrent chain was not supported; case frozen as negative | Erasure leaves almost all technical content; presentation-level at best | Erasure leaves all scientific content; DR-1 does not survive as a distinct mechanism | Field-native GST/QPT/model-checking literature reconstructs all central results | **accepted** | decreased |
| 2 | §19: five-level ordinal taxonomy | Deleted; no ordinal classification retained | Taxonomy mixes recurrence, invariance, diagnostic value, and modal non-closure | Same objection; highest category is a different modal claim | No source establishes this as a field-native scale | **accepted** | decreased |
| 3 | §2: Deferred Resolution treated as a working concept to classify the lineage | §§2–3: only a historical, rejected search hypothesis | Definition is broad enough to capture ordinary progress | Concept fails falsifiability/erasure in this case | Box/Ljung/Gelman–Shalizi provide ordinary model-building accounts | **accepted** | decreased |
| 4 | Title presents “Deferred Resolution Case 01” as the primary object | Title centers conditional inference, quotient identifiability, and scope revision; DR appears only as a negative test | Recommended demotion if erasure succeeds | Recommended negative-case title | N/A; editorial consequence of the audit | **accepted** | decreased |
| 5 | §§16.1–16.2: standard tomography → self-consistent estimation described as boundary relocation | §7: “nuisance/reference parameter promotion” or joint estimation under weaker reference assumptions | Strongest local candidate still looks like ordinary refinement | More precise as nuisance/reference parameter promotion | Merkel 2013 explicitly changes from conditioned gate-generated SPAM to joint gate estimation while retaining base \(\rho_0,M_0\) | **reframed** | decreased and sharpened |
| 6 | General comparison lacked Box, nuisance-parameter theory, Ljung, and modern model-checking cycle | §4 and References add Box 1976, Cox–Reid 1987, Ljung 1999, Gelman–Shalizi 2013 | Requested prior-art correction | Agreed that ordinary inverse-problem maturation is stronger baseline | Bibliographic metadata checked against DOI/publisher or author pages | **accepted** | decreased novelty |
| 7 | §8: gauge classification included “physical equivalence” | §10: replaced by “operational indistinguishability under the declared experiment algebra” | “Physical equivalence” is too strong | Same; interface-relative equivalence is safer | GST likelihood is invariant under gauge transformation, but that does not establish unrestricted ontological identity | **accepted** | decreased |
| 8 | §§8–9: gauge optimization could read as reporting convention after quotient closure | §§9–10, §15: quotient-level identifiability closes redundancy; representative/metric choices remain decision-relevant | Generic gauge transforms need not preserve CP; practical metrics can be gauge-variant | Same; avoid treating optimization as cosmetic | Nielsen et al. 2021 explicitly discusses CP/gauge tension and gauge variation of fidelity, diamond distance, entropy | **accepted** | differentiated, not increased |
| 9 | §9 “Stage D” had one deferred-resolution status | §9 splits identifiability and reporting/decision layers | Required two-layer reading | Agreed quotient closes one question but not every reporting convention | Di Matteo et al. 2020 parameterizes operational observables; Nielsen et al. 2021 covers representative/gauge optimization practice | **accepted** | more precise |
| 10 | §10: non-Markovian and related work formed “Stage E” in a visual chain | §11: “Related model extensions…” with parallel branches | Linear staging is historically misleading | Process tensor predates gauge-free tomography; branches are target-specific | Pollock 2018 precedes Di Matteo 2020; Rudinger, White, Li address different scope failures | **accepted** | decreased |
| 11 | Li et al. reference metadata was defective | §11.4 and References: seven authors; *QST* 9, 035027 (2024), DOI ad3d80 | Corrected authors but one review passage proposed 025027 | Proposed 035027 and requested primary verification | arXiv 2307.14696 and DOI landing metadata confirm 035027 and full author list | Claude authors **accepted**; Claude page **rejected**; Codex **accepted** | unchanged scientific claim |
| 12 | §7 left ambiguity about Merkel 2013 base SPAM and mature gauge vocabulary | §7 records fixed \(\rho_0,M_0\), future extensions, and absence of explicit mature “gauge”/“similarity transform” terminology without inferring absence of mathematical invariance | Marked base-SPAM and historical gauge reading partly unverified | Requested primary-source separation | Full primary text confirms fixed \(\rho_0,M_0\); conclusion names their errors and slowly time-varying errors; full-text search found no explicit “gauge” or “similarity” terminology | **accepted after verification** | more precise |
| 13 | §18 Weak Claim C: operational success vs “ontological closure” | §15.4 and §18: model adequacy, representational uniqueness, interpretive uniqueness separated; last is not inferred | “Ontological closure” not defined by the technical literature | Recommended deletion or decomposition | GST literature directly treats model fit and gauge representation, not unique ontology | **accepted** | decreased |
| 14 | §18 retained four weak claims, including boundary-relocation language | §18 retains only standard supported claims and lists recurrent relocation/ontological claims as unsupported | Several claims trivial, broad, or unsupported | Same | Supported parts map directly to standard identifiability/model-checking literature | **accepted** | decreased |
| 15 | §17 Erasure Test was not the final result | §16: erasure is the formal negative result; field-native rewrite loses nothing and gains precision | YES, almost entirely | YES, entirely | Rewrite in §12 uses only established terms and reproduces the case | **accepted** | decreased |
| 16 | Null A/E constrained but did not overturn the weak positive result | §17 formally adopts ordinary refinement/model-building plus reviewer-generated narrative; quotient resolution supports the gauge subcase | Null A and E are strongest | Same; Null C also strong locally | Chronology and logical independence of extensions support Null E; prior art supports Null A | **accepted** | decreased |
| 17 | §14 full assurance-provenance map | §19 removes the full table and records no independent diagnostic effect | If labels erase, added value is presentation | Same | Target, experiment, and judgment are unchanged by the classification | **accepted** | decreased |
| 18 | §15.3 cross-impact example centered drift but did not assign first-line audit responsibility | §14 retains non-exclusive cross-impact and adds primary detection responsibility | Suggested one primary node; risked exclusive allocation | Recommended responsibility rather than ownership | Failure-specific diagnostics exist across GST/extensions; no single-node ontology is required | Claude exclusive placement **rejected**; detection-responsibility idea **reframed** | unchanged |
| 19 | §16.3 treated gauge-free work as a possible transition in the chain | §§9, 15: quotient resolution closes representation; reporting layer is separate and not a DR rescue | Quotient may solve the apparent residual | Same | Operational gauge-free tomography makes observables the parameters | **accepted** | decreased |
| 20 | §16.4 tied fixed Markovian GST to later extensions as relocation | §§11–13: goodness-of-fit may motivate branches but does not uniquely imply one | Scope extension is an independent problem | Same | Process-tensor, simultaneous-GST, leakage, and instrument-set work have different targets | **accepted** | decreased |
| 21 | §20 recommended Minor revision to v0.3 | §20 recommends no substantive revision; at most a one-paragraph negative report | Case does not justify a construct | Same | Negative erasure result supplies no positive structure for v0.3 | **reframed** | decreased |
| 22 | §22 conclusion supported weak relocation | §23 opens and closes with explicit negative result | Must answer strongest attack directly | Must state NO if no added diagnosis | Entire case rebuilt without DR terms | **accepted** | decreased |
| 23 | No freeze status | §22 “Frozen negative result” restricts future changes and revival | Negative baseline recommended implicitly | Explicit negative baseline useful for comparison | N/A; revision-governance decision | **accepted** | unchanged epistemic content |
| 24 | Bibliography carried forward without an explicit sanity audit | §24 supplies corrected references and direct DOI/primary links | Requested bibliographic correction | Requested primary checks | Minimum DOI/title/venue/year audit performed; Li and Merkel received full-text attention | **accepted** | unchanged |
| 25 | D’Ariano & Lo Presti (2001), PRL 86, 4195 was listed with the title “Imprinting complete information…” | Reference corrected to “Quantum tomography for measuring experimentally the matrix elements of an arbitrary quantum operation” | Claude review incorrectly said the old “Imprinting…” title was correct | Codex review did not resolve this title conflict | DOI 10.1103/PhysRevLett.86.4195 and arXiv quant-ph/0012071 identify the 2001 tomography paper; “Imprinting…” is a separate 2003 PRL 91, 047902 paper | Claude claim **rejected after primary verification** | unchanged scientific claim; increased bibliographic accuracy |

---

## 4. Reviewer agreement and disagreement

### 4.1 Agreement adopted

両査読は次で一致し、一次資料とも整合した。

- recurrent chain は支持されない。
- A→B/C は ordinary joint estimation / inverse-problem refinement と読める。
- gauge quotient と model adequacy は別問題である。
- later extensions を一つの Stage E に置くべきでない。
- “ontological closure” は GST 文献の直接的 outcome ではない。
- Erasure 後に技術内容が残るなら、独立概念としての価値はない。

### 4.2 “Entirely” vs “almost entirely”

Claude review は、固有語彙を消すと科学的内容は **almost entirely** 残るとした。Codex review は **entirely** 残るとした。v0.2 は後者を採る。

理由は、Claude review が残りうるとした時系列上の non-edge も、Deferred Resolution 語彙ではなく通常の bibliography / dependency audit から得られるからである。実際、process tensor の先行年代と gauge-free work との論理非依存は field-native reconstruction にそのまま残った。

### 4.3 Li et al. bibliographic conflict

Claude review の著者訂正は正しかったが、掲載番号を 025027 とした箇所は一次資料と衝突した。一次資料は *Quantum Science and Technology* 9, **035027** (2024), DOI 10.1088/2058-9565/ad3d80 を示す。したがって 035027 を採用した。

### 4.4 Merkel et al. verification

査読段階で留保されていた二点を分けた。

- fixed base \(\rho_0,M_0\): 一次本文で確認済み。
- 後の GST と同じ gauge / similarity-transform language: 明示語としては本文内に確認できない。

後者から「invariance がなかった」「後に gauge problem が発生した」とは推論しない。absence of terminology と absence of mathematical symmetry は同じではない。

### 4.5 Cross-cutting failures

Claude review の “one primary node” 処方は、drift や SPAM の cross-impact を失わせるため採用しなかった。代わりに、非排他的な **primary detection responsibility** を置いた。これは ownership classification ではなく protocol accountability の索引である。

### 4.6 D’Ariano–Lo Presti title conflict

Claude review は v0.1 の D’Ariano–Lo Presti (2001), PRL 86, 4195 の題名を “Imprinting complete information about a quantum channel on its output state” とする記載を正しいと評価したが、一次書誌と衝突した。DOI 10.1103/PhysRevLett.86.4195 は “Quantum tomography for measuring experimentally the matrix elements of an arbitrary quantum operation” である。“Imprinting…” は別論文、*Physical Review Letters* 91, 047902 (2003), DOI 10.1103/PhysRevLett.91.047902 である。v0.2 は前者へ訂正し、査読側の誤りを correction trail に残した。

---

## 5. Claim-strength audit

### Decreased

- ケース判定
- DR の概念的地位
- taxonomy
- A→B/C の一般化
- linear historical narrative
- ontological implication
- methodological usefulness
- v0.3 への改訂要求

### Unchanged but clarified

- standard QPT の calibration dependence
- self-consistent estimation の技術的役割
- GST の gauge orbit
- quotient-level identifiability
- model checking と model extension
- cross-cutting failure modes

### Increased

新しい一般主張の強度は増やしていない。一次資料により局所的な書誌・技術記述の確度だけを上げた。

---

## 6. Source verification ledger

| Claim | Source used | Verification result | Use in v0.2 |
|---|---|---|---|
| Standard QPT can misattribute gate-generated SPAM errors | Merkel et al. 2013 primary article | confirmed | §7 |
| D’Ariano & Lo Presti 2001 title/DOI | PRL 86, 4195; DOI 10.1103/PhysRevLett.86.4195; arXiv quant-ph/0012071 | “Quantum tomography for measuring experimentally…”; distinct from the 2003 “Imprinting…” paper | §24 |
| Merkel model fixes base \(\rho_0,M_0\) | Merkel et al. 2013 full text | confirmed | §7 |
| Merkel explicitly uses mature GST gauge terminology | Merkel et al. 2013 full-text search | not found | absence stated narrowly; not used as DR evidence |
| GST probabilities are invariant along gauge directions | Nielsen et al. 2021 review | confirmed | §§8–10 |
| General/non-unitary gauge transformations need not preserve CP | Nielsen et al. 2021 review | confirmed | §9.2 |
| Fidelity/diamond/entropy can be gauge-variant | Nielsen et al. 2021 review | confirmed | §9.2 |
| Operational tomography targets observable parameters | Di Matteo et al. 2020 primary article | confirmed | §9.1 |
| Process tensor predates operational gauge-free tomography | Pollock 2018 vs Di Matteo 2020 | confirmed | §§5, 11, 17 |
| Li et al. metadata | arXiv 2307.14696 and DOI ad3d80 | seven authors; QST 9, 035027 (2024) | §§11.4, 24 |
| Ordinary model-building cycle is established prior art | Box 1976; Gelman & Shalizi 2013 | confirmed at general level | §4 |
| Nuisance/reference uncertainty has established inference theory | Cox & Reid 1987 | confirmed; no exact GST identity claimed | §4 |
| System identification includes structure, estimation, validation, revision | Ljung 1999 | confirmed at workflow level | §4 |

---

## 7. Deleted structures

以下は v0.2 本文に移植していない。

- 旧五段階 DR taxonomy。
- recurrent chain を示す単線図。
- Stage E という呼称。
- “physical equivalence”。
- “ontological closure”。
- positive weak-relocation verdict。
- full assurance-provenance table。

削除理由は簡略化ではなく、それぞれが異種の問題を同一尺度または同一 chain に見せていたためである。

---

## 8. Preserved correction trail

v0.1 の失敗は削除せず、次の場所から追跡できる。

1. v0.1 本文はそのまま保存。
2. v0.2 §1 が withdraw / rewrite / preserve を要約。
3. 本台帳 §3 が各主張の移動を記録。
4. v0.2 §16 が Erasure Test の negative result を記録。
5. v0.2 §17 が Null A + Null E を正式採用。
6. v0.2 §22 が freeze rule を定める。

---

## 9. Final audit

| Check | Result |
|---|---|
| 旧 weak-positive判定を残していない | PASS |
| 旧五段階 taxonomy を削除した | PASS |
| Box / Ljung / nuisance prior art を追加した | PASS |
| “physical equivalence” を肯定語として削除した | PASS |
| gauge quotient と reporting choice を分離した | PASS |
| later extensions の直線性を除いた | PASS |
| “ontological closure” を outcome から削除した | PASS |
| Li et al. を一次資料で訂正した | PASS |
| Merkel 2013 の確認済み事項と用語不在を分けた | PASS |
| Erasure Test を negative result とした | PASS |
| Null A + Null E を採用した | PASS |
| assurance table の診断効果なしを明示した | PASS |
| cross-impact と detection responsibility を両立した | PASS |
| case を negative baseline として freeze した | PASS |
| v0.1 を変更・削除していない | PASS |

---

## 10. Ledger conclusion

v0.2 の変更はすべて、主張を強くするのではなく、異種の技術問題を field-native vocabulary へ戻す方向に働いた。新しく増えたのは一般理論ではなく、一次資料に基づく区別と correction trail である。

**GST Case 01はDeferred Resolutionを支持せず、既存のmodel-building / identifiability / quotient / validation語彙でより正確に記述できるnegative caseとして凍結された。**
