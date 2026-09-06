# Proof-Formation Inter-Reader Test — Coder Instructions v0.1

- **Status:** Phase 0前 qualitative reconstruction protocol
- **Basis:** [`proof_formation_meta_experiment_v0.1.md`](./proof_formation_meta_experiment_v0.1.md)
- **Task:** 与えられた一つのsource episodeを、source wordingの範囲内で再構成する
- **Do not:** 新しいmove、score、尺度、geometry、一般法則を追加しない

## 1. Coding unit

最小単位は、完成した証明の型ではなく、次のtransitionである。

```text
claim_before + obligation + failure_witness
    -> move_taken
    -> claim_after + terminal_status
```

episodeは、sourceが結びつける最小のbefore / witness / afterで切る。題名、同じ文書、単なる時系列だけで複数のclaimを一つにしない。逆に、明示的なparent、revision ledger、before/after、withdrawalがある場合はその関係を優先する。境界が複数成立するなら `AMBIGUOUS` とし、候補境界を併記する。

## 2. Required record

各episodeについて次を埋める。sourceにない内容を推測せず、空欄にせず `UNKNOWN` または `AMBIGUOUS: ...` と書く。

| Field | Record |
|---|---|
| `episode_id` | corpusのID |
| `claim_before` | 変更前のexact claim。量化、否定、statusを保持 |
| `target_and_scope` | object、domain/model class、formula class、theory/language、corpus、intended use |
| `obligation_type` | formal proof、counterexample exclusion、novelty、empirical discrimination、reproducibility、decision relevance等 |
| `assumptions` | theorem/claim成立に必要な条件。可能ならobject / ambient / background / definitional |
| `proof_or_evidence_resources` | 導出・検査に使うlemma、coding、reduction、data、literature、control、review procedure等 |
| `failure_witness` | counterexample、logical objection、prior art、failed control、Erasure、factual correction、missing evidence |
| `available_branches` | sourceが明示するが、main routeとして採用されたとは限らない救済・縮小・別問題・終了候補 |
| `move_taken` | 実際に採用されたM1–M17。複数可。primaryを無理に一つ選ばない |
| `claim_after` | 変更後のexact claim/questionとscope |
| `terminal_status` | proved / conditionally proved / comparison result / empirical protocol / synthesis / open / withdrawn / frozen negative |
| `provenance_label` | 各重要記述をSOURCE-DERIVED / INFERENCE / OPEN HYPOTHESISに分ける |

## 3. Six mandatory distinctions

1. **Claim identity:** quantifier、target、theory/language、対象class、結論型、statusを比較する。同じ題名や語彙だけでは同一claimとしない。identity自体がsourceで固定されなければ `AMBIGUOUS`。
2. **Episode boundary:** sourceが明示したdependencyだけを用いる。別のcounterexample、別のclaim、別のverdictを一つに束ねる必要があるなら、複数episode案を残す。
3. **Assumption vs proof resource:** statement/domainを成立させる条件はassumption、同じstatementを導出・検査するrouteはresource。formula class、provability predicate、candidate classは通常target/definitional側。diagonal lemma、cut elimination、文献corpus、control reviewは通常resource側。両方に読めるtheorem versionなら `AMBIGUOUS`。
4. **Conclusion weakening vs scope restriction:** 結論の量化・精度・一般性・必然性を弱めたならM2。対象、formula class、model/corpusを狭めたならM3/M4。両方変われば複数codeを付す。
5. **Actual move vs available rescue:** `withdrawn`、`adopted`、`retained`、`next work`、選択肢の採否を確認する。「条件を加えれば成立する」「可能である」という記述だけを`move_taken`にしない。
6. **Source-derived vs inference:** sourceのexact wording、明示status、明示dependencyだけがSOURCE-DERIVED。M-code割当、claim grouping、動機説明、反実仮想は通常INFERENCE。sourceが将来検査として置くものはOPEN HYPOTHESIS。

## 4. Coding constraints

- M1–M17は基準文書の意味のまま使う。該当なし、複数、`UNKNOWN`、`AMBIGUOUS`を許す。
- source固有の評価記号（例: Metrology Caseの`M1 — Organizational value`、stress testの`S2*`）はformation move codeではない。`source verdict: M1`のように明記し、`move_taken: M1`と混同しない。
- counterexample、prior art、R0/R1/R2、conservation、Erasure Test、kill criterionは、それ自体をmoveとしない。
- reflectionは一語でcode化せず、formula class、same theory / extension、internal / metalevelを記録する。
- `T+P \vdash P`、結論をassumptionへ入れる、成功objectだけをdomainとする、lossを定義へ埋める等は、解決とせず`degenerate / target-leakage candidate`と注記する。
- 不明点を埋めるためにsource外の意図、自然さ、歴史的因果を補わない。
- answer keyと他readerの記録は提出前に見ない。

## 5. Submission block

```text
episode_id:
episode_boundary:
claim_identity:
claim_before:
target_and_scope:
obligation_type:
assumptions:
proof_or_evidence_resources:
failure_witness:
available_branches:
move_taken:
claim_after:
terminal_status:
provenance_label:
degenerate_or_target_leakage:
uncertainties:
source_excerpts_used:
```

このtestでは一致率、kappa、precisionその他の数値を計算しない。不一致の型と、それがsource wordingだけで解消できるかを記録する。
