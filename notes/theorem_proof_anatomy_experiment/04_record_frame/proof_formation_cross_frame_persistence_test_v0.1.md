# Proof-Formation Cross-Frame Persistence Test v0.1

- **Status:** exploratory persistence test
- **Environment:** finite propositional prototype and frozen record-frame histories only
- **Date:** 2026-09-06
- **Companion:** [`proof_formation_cross_frame_persistence_checker_v0.1.py`](./proof_formation_cross_frame_persistence_checker_v0.1.py)

## 0. Status / posture

- **exploratory persistence test**
- **not a theorem**
- **not an invariant theorem**
- **not a new framework**
- **not a v0.2 proposal**
- **not a validation report**
- **not a canonical record architecture**
- **not a claim that any feature is universally frame-independent**
- **no new move codes**
- **no score**
- **no optimization**
- **no metric / geometry / topology / lattice**
- **no generalization beyond the finite prototype and frozen histories**

中心問いは次である。

> Across the same frozen histories projected through different record frames,  
> what, if anything, persists without depending on the specific frame vocabulary?

この問いに対し、最初から invariant を置かない。まず H1–H10、C-F、C-D の R0–R4 projections に persistence / non-persistence が実際にあるかを観察し、その後で共通 projection が何を捨てるかを監査する。blind-reader records は動機の範囲を越えて再解釈しない。

## 1. Existing frozen histories

record-frame sensitivity test の meanings を変更せず、次を再利用する。補助 history は追加しない。

| History | Frozen content |
|---|---|
| H1 | \(H_0=\{p\lor q\},C=p\) に \(\neg q\) を追加；same-id；established；provenance `INDEPENDENT` |
| H2 | \(S\) を \(\Omega\setminus\{\omega_{01}\}\) へ制限；same-id；established；provenance `UNKNOWN` |
| H3 | target を \(p\lor q\) へ弱化；same-id；established；provenance `UNKNOWN` |
| H4 | semantic repair なし；original \(x_0\) withdrawn；successor なし |
| H5 | \(x_0\) withdrawn；\(\{p\lor q,\neg q\}\models p\) を満たす successor \(x_1\) established |
| H6 | H5 と同じ mathematical after-material；\(x_0\) が strengthening を通じて継続し established |
| H7 | \(p\) と semantically equivalent な \(\neg\neg p\) を追加；provenance `UNKNOWN` |
| H8 | \(\top\) を追加；semantic state は不変；failed；provenance `UNKNOWN` |
| H9 | exact filter \(p\lor\neg q\) を post-hoc に追加；established |
| H10 | H9 と同じ formula / after-state；selection は `INDEPENDENT` と stipulate；established |
| C-F | intervention なし；failed, not withdrawn；provenance `INAPPLICABLE` |
| C-D | target \(p\) を verbatim に追加；established；provenance `UNKNOWN` |

共通 base は

\[
V=\{p,q\},\quad
\Omega=\{\omega_{00},\omega_{01},\omega_{10},\omega_{11}\},
\]

\[
H_0=\{p\lor q\},\quad C_0=p,\quad
E(H_0,C_0)=\{\omega_{01}\}
\]

である。R0 の designated endpoint choice、R1 の extensional carrier、R2 の raw typed slots、R3 の identity/status/successor、R4 の provenance も既存 test の定義をそのまま使う。

## 2. Reused frames without privilege

- **R0 — outcome-only:** designated endpoint の semantic success/failure と counterexample remains のみ。
- **R1 — semantic:** before/after の \(M(H),M(C),S,M(H)\cap S,E_S,\models_S\)。formula syntax は extensionally normalize される。
- **R2 — typed-transition:** R1 plus raw \(H,C,S\) slots と changed-slot record。
- **R3 — history/status:** R2 plus id、same/different identity assertion、withdrawn、endpoint status、successor relation、segmentation。
- **R4 — provenance-complete:** R3 plus `POST_HOC / INDEPENDENT / UNKNOWN / INAPPLICABLE`。

この列挙順は correctness、quality、または preference の順ではない。各 Rj は異なる observation scheme である。R4 が多くの fields を保持することは、その assertions の正当性や relevance を保証しない。

## 3. Candidate persistent features

以下は test candidates であり、invariants ではない。

### PERSIST-A — before/after relation exists

history に before と designated endpoint の relation があるか。C-F のように両 state が同一でも relation record は存在する。R0 が endpoint だけを残す場合、この relation は projection から読めない。

### PERSIST-B — semantic failure state

before または endpoint に \(E\ne\varnothing\)、すなわち non-entailment があるか。成功 histories も共通 before では失敗しているため、endpoint しか持たない R0 では一部が見えない。

### PERSIST-C — semantic effect changed

before と endpoint の evaluated semantic content

\[
\big(M(H)\cap S,M(C),E_S,H\models_S C\big)
\]

のいずれかが変化したか。

### PERSIST-D — some recorded state component changed

各 frame が保持する state components のうち、before/after で少なくとも一つが変化したか。この predicate は frame-relative である。H8 は R1 では unchanged、R2 では raw \(H\) changed となる。

### PERSIST-E — terminal disposition differs

original / endpoint が failed、established、withdrawn 等の異なる disposition を持つか。semantic failure と withdrawal を同一視しない。

### PERSIST-F — branch or successor structure exists

split history または successor relation が明記されているか。

### PERSIST-G — selection provenance distinction exists

`POST_HOC / INDEPENDENT / UNKNOWN / INAPPLICABLE` のいずれが source history に明記されているか、または pair 間にその差があるか。

### PERSIST-H — intervention occurred

underlying frozen history 上で何らかの intervention が明記されているか。これは source-history fact であり、semantic change と同値ではない。H8 は intervention を持つが semantic state は変わらない。

## 4. Three senses of persistence

### Type 1 — semantic persistence

truth table / evaluated semantics だけで回収できるもの。例は endpoint entailment と endpoint counterexample の有無である。R1 以上では before/after semantic change も回収できる。

### Type 2 — representational persistence

複数 frame が同じ field を保持するため繰り返し見えるもの。R1–R4 の before/after pair、R2–R4 の raw changed slots、R3–R4 の identity/status/successor が該当する。underlying semantics に同じ distinction があることを意味しない。

### Type 3 — source-history persistence

frozen history には明記されているが、一部 projections で不可視になるもの。H8 の \(+\top\)、H4 の withdrawal、H5 の successor、H9/H10 の provenance が該当する。

同じ feature が二つの意味を持つ場合も分ける。endpoint success の値は Type 1 として truth-table auditable だが、その値を R0–R4 がすべて表示する persistence は shared projector design による Type 2 の側面を持つ。

## 5. Feature-by-frame audit

`PRESERVED` は frame から feature を確実に読める場合だけに使う。PERSIST-D は predicate 自体が frame-relative なので、星印は「その frame 内の components については読めるが、他 frame と同じ predicate value を保証しない」を意味する。PERSIST-H の R3/R4 も frozen histories に限る。

| Feature | R0 | R1 | R2 | R3 | R4 |
|---|---|---|---|---|---|
| PERSIST-A before/after relation | LOST | PRESERVED | PRESERVED | PRESERVED | PRESERVED |
| PERSIST-B a semantic failure state exists before or after | PARTIALLY PRESERVED — endpoint only | PRESERVED | PRESERVED | PRESERVED | PRESERVED |
| PERSIST-C evaluated semantic effect changed | LOST | PRESERVED | PRESERVED | PRESERVED | PRESERVED |
| PERSIST-D some retained component changed | LOST | PRESERVED* | PRESERVED* | PRESERVED* | PRESERVED* |
| PERSIST-E terminal disposition differs | PARTIALLY PRESERVED — semantic endpoint only | PARTIALLY PRESERVED | PARTIALLY PRESERVED | PRESERVED | PRESERVED |
| PERSIST-F branch/successor exists | LOST | LOST | LOST | PRESERVED | PRESERVED |
| PERSIST-G selection provenance | LOST | LOST | LOST | LOST | PRESERVED |
| PERSIST-H intervention occurred | LOST | PARTIALLY PRESERVED | PARTIALLY PRESERVED | PRESERVED on frozen set | PRESERVED on frozen set |

`NOT APPLICABLE` は feature capability table 全体には使わない。history level では C-F と H4 の restriction-selection provenance が `INAPPLICABLE` である。R4 はその明記を保持する。

この表から、PERSIST-A–H のうち全 R0–R4 で完全に `PRESERVED` となる candidate はない。後述する endpoint semantic pair は PERSIST-B/E の限定された endpoint-only component であり、candidate feature 全体ではない。

## 6. History-by-history persistence audit

全 history について Q1–Q4 を次のように読む。

- **Q1:** 全 R0–R4 に共通するのは designated endpoint の semantic success/failure と counterexample remains の値。
- **Q2:** R1 以上では before/after model sets、entailment、\(E\)、semantic equality/change が残る。
- **Q3:** raw slot/syntax は R2、identity/status/successor は R3、provenance は R4 まで見えない。
- **Q4:** underlying intervention/history facts の多くは全 frames で同じようには見えない。

### 6.1 History table

| History | Common across R0–R4 | Semantic information in R1+ | Extra information requiring later frame | Source-history fact not uniform across frames |
|---|---|---|---|---|
| H1 | endpoint EST; \(E=\varnothing\) | false→true entailment；surviving \(\{10\}\) | raw `H:+¬q` at R2；`INDEPENDENT` at R4 | the intervention and motivation |
| H2 | endpoint EST; \(E=\varnothing\) | false→true；surviving \(\{10,11\}\)；explicit \(S'\) | raw `S changed` at R2；`UNKNOWN` at R4 | scope-selection event |
| H3 | endpoint EST; \(E=\varnothing\) | false→true；target model set expands | raw `C changed` at R2 | target-replacement event and its unknown motivation |
| H4 | endpoint semantic FAIL; \(E\ne\varnothing\) | semantic state unchanged | `withdrawn`, no successor at R3 | withdrawal is invisible in R0–R2 |
| H5 | designated endpoint EST; \(E=\varnothing\) | false→true；after semantics equal H6 | raw `H changed` at R2；withdrawal+successor at R3 | original \(x_0\) disposition disappears in R0–R2 |
| H6 | endpoint EST; \(E=\varnothing\) | false→true；after semantics equal H5 | raw `H changed` at R2；same-id continuation at R3 | continuation assertion disappears before R3 |
| H7 | endpoint EST; \(E=\varnothing\) | false→true；same extensional after-state as C-D | raw `+¬¬p` at R2 | formula form disappears in R0/R1 |
| H8 | endpoint FAIL; \(E\ne\varnothing\) | \(\sigma_0→\sigma_0\), no semantic change | raw `H:+⊤` at R2 | an intervention occurred, invisible in R0/R1 |
| H9 | endpoint EST; \(E=\varnothing\) | exact-filter after-state；same evaluated effect as H2 | raw `H` slot at R2；`POST_HOC` at R4 | selection timing/motivation |
| H10 | endpoint EST; \(E=\varnothing\) | same semantic record as H9 | same typed/history record as H9；`INDEPENDENT` at R4 | independent motivation assertion |
| C-F | endpoint FAIL; \(E\ne\varnothing\) | \(\sigma_0→\sigma_0\) | no-transition/failed record at R3 | absence of intervention is not recoverable in R0/R1 |
| C-D | endpoint EST; \(E=\varnothing\) | same extensional after-state as H7/H9/H10 | raw `H:+p` at R2 | verbatim insertion form disappears in R0/R1 |

### 6.2 Focus cases

- **H8 +⊤:** common endpoint failure survives、but the actual intervention does not survive R0/R1。
- **H5 withdrawal + successor:** endpoint success survives、but original withdrawal、identity break、successor relationはR3まで消える。
- **H9/H10:** endpoint、semantics、typed slots、identity/history が同じで、provenance distinction は R4 だけに残る。
- **H9/H2:** evaluated effect は同じだが full R1 は \(M(H)\) と \(S\) を別 carriers として保持するため distinct。共通 semantic effect と carrier distinction を混同しない。
- **H7/C-D:** extensional semantics は同じで、raw syntactic distinction は R2 からだけ見える。

## 7. Search for genuinely cross-frame common content

R0 が保持するのは designated endpoint の semantic pair だけであり、R1–R4 からも同じ pair を抽出できる。

\[
K_{\mathrm{end}}(h)
=
\big(
\text{endpoint semantic success/failure},
\text{counterexample remains?}
\big).
\]

Frozen histories では次の二値 group になる。

- \((\text{success},\text{no counterexample})\): H1, H2, H3, H5, H6, H7, H9, H10, C-D。
- \((\text{failure},\text{counterexample remains})\): H4, H8, C-F。

この pair の二成分は有限 semantic consequence では相互に対応し、一方が他方に独立情報を追加するわけではない。それでも R0 の literal output に合わせて両方を残す。

### What all frames share

- a designated endpoint exists in every projected record;
- that endpoint's semantic consequence value;
- whether its counterexample set is empty。

### What all frames do not share

- the before state itself — R0 lacks it;
- a before→after semantic relation — R0 cannot compare states;
- original identity or the claim that endpoint is the “same object” — absent before R3;
- withdrawal, successor, segmentation — absent before R3;
- provenance — absent before R4;
- intervention occurrence — H8/C-F collapse in R0/R1。

したがって all frames share at least endpoint semantic outcome, but not a formation history. また “before→endpoint exists” は R1–R4 の shared construction にはあるが R0 output にはなく、全 frame 共通ではない。

## 8. Strong candidate: “something happened”

H8 と C-F を比較する。

| Frame | H8 +⊤ versus C-F no intervention |
|---|---|
| R0 | COLLAPSED — both endpoint failure with counterexample |
| R1 | COLLAPSED — both \(\sigma_0→\sigma_0\) extensionally |
| R2 | DISTINCT — `H:+⊤` versus no changed slot |
| R3 | DISTINCT — typed difference plus event/status record |
| R4 | DISTINCT — R3 plus `UNKNOWN` versus `INAPPLICABLE` |

“something happened” は全 frames に残る observational fact ではない。H8 の intervention occurred は **Type 3 source-history persistence** であり、R0/R1 projection からは回収できない。R2 で見えるのは raw \(H\) slot を保持するという frame choice のためである。

## 9. Strong candidate: semantic outcome

endpoint semantic outcome と counterexample remains は R0 にあり、R1–R4 からも回収できる。この selected frame set 内では strongest cross-frame persistence である。

ただし H4/C-F は次を示す。

- H4: semantically failed and withdrawn。
- C-F: semantically failed but not withdrawn。
- R0/R1/R2: identical endpoint semantic outcome。

したがって semantic terminal outcome は research-history disposition ではない。さらに全 frame に残る理由の一部は、R1–R4 が R0 相当の endpoint semantics を共通に保持するよう設計されたことにある。よってこれは **lowest common denominator of the selected projectors** でもあり、未知の record frame に依存しないことを発見したとは言えない。

## 10. Strong candidate: relation rather than action

action label ではなく relation が残る可能性を、relation ごとに監査する。

| Candidate relation | First frame that can read it | Persistence finding |
|---|---|---|
| endpoint entails / does not entail | R0 | R0–R4 に残るが shared projector design の control が必要 |
| counterexample remains / none at endpoint | R0 | R0–R4 に残る；endpoint entailment と同じ semantic split |
| entailment changed false→true | R1 | R0 は before を持たないため全 frame 共通でない |
| counterexample set shrank / stayed | R1 | R0 は endpoint-only のため direction を失う |
| evaluated semantic content changed / unchanged | R1 | R0 では lost；H8 は unchanged |
| raw H/C/S slot changed | R2 | typed framesだけ；matched H9/H2 の semantic effect は同じ |
| identity continued / broke | R3 | history assertion；semanticsからは回収不能 |
| status changed / withdrawal occurred | R3 | failed と withdrawn を分けるが R0–R2 では lost |
| successor relation appeared | R3 | H5だけの split structure；R0–R2 では lost |
| selection provenance differs | R4 | H9/H10 を初めて分ける；semantic shapeからは infer しない |

endpoint relation 以外は特定 fields を共有する複数 frames にだけ残る。ここから relation を新しい基本実体として採用しない。

## 11. Cross-frame erasure test

既存 Erasure Test の姿勢だけを使い、各 field を消したときの distinction loss を観察する。

| Erased field | What distinction disappears? | What still survives? | More primitive remainder? |
|---|---|---|---|
| raw syntax | H7 \(+\neg\neg p\) versus C-D \(+p\)；H8 の syntactic \(+\top\) trace | extensional model sets、endpoint outcome | extensionally evaluated semantic state |
| H/S slot distinction | matched H9/H2 の assumption-change versus scope-change | identical surviving set、\(M(C)\)、\(E=\varnothing\)、success | evaluated effect only |
| id | identity continuity/break assertion itself | H5/H6 は status、successor、segmentation が残ればなお区別可能 | endpoint semantics plus non-identity history fields |
| status | H4 withdrawn versus C-F failed；original disposition | H5/H6 は id/successor/segmentation が残れば区別可能 | semantic failure/success |
| successor | predecessor→successor link | H5/H6 は different id、withdrawn、segmentation が残れば区別可能 | unlinked endpoint/history facts |
| provenance | H9 POST_HOC versus H10 INDEPENDENT | formula、semantic state、typed slots、identity/status | common transition record without selection history |
| semantic model sets | exact surviving-set and semantic-change distinctions；outcomeの再計算根拠 | raw formulas/slots or asserted endpoint boolean, if separately retained | asserted outcome only; no semantic audit if its basis is also erased |
| counterexample region | explicit failure locations and witness check | \(M(H),M(C),S\) から再計算可能；endpoint entailment remains | model-set inclusion；R0では success boolean |

重要な非対称性がある。id/status/successor は相互に重なるため、一 field だけ消しても H5/H6 distinction が必ず collapse するわけではない。R0–R2 のように history bundle 全体を消したとき初めて完全に collapse する。対して provenance は H9/H10 の唯一の差なので、それだけを消すと直ちに collapse する。

## 12. Common projection candidates

“minimal”、“canonical”、“sufficient”、“invariant” とは呼ばず、次を **common projection candidates** として残す。

### Candidate K1

\[
K_1(h)=\text{endpoint semantically entails?}
\]

### Candidate K2

\[
K_2(h)=
\big(
\text{endpoint semantically entails?},
E_{\mathrm{endpoint}}\ne\varnothing?
\big).
\]

K2 は existing R0 record をそのまま反映するが、この有限設定では二成分が同じ split を反復する。

### Candidate K3

`a designated endpoint record exists`。

K3 は semantic content よりも projector construction の事実である。R0–R4 がすべて endpoint を出力するよう設計されているため真になる。

K1/K2 は全 R0–R4 projections から読める。K3 も出力構造上は共通する。しかしいずれも action、before/after direction、identity、withdrawal、successor、provenance を保持しない。

## 13. Failure modes of common projections

K1/K2 に落とすと次が collapse する。

- **H4 / C-F:** withdrawn versus merely failed。
- **H5 / H6:** successor versus same-id continuation。
- **H9 / H10:** post-hoc versus independently motivated selection。
- **H8 / C-F:** intervention versus no intervention。
- **H1 / H2 / H3:** assumption、scope、target の異なる successful routes。
- **H7 / C-D:** semantically equivalent versus verbatim target insertion。
- **H9 / H2:** matched evaluated effect に至る異なる typed carrier histories。

したがって

> common across frames  
> does not mean  
> sufficient for formation history.

K1/K2 は terminal semantic bin を保存するが、failure をどう扱ったか、同じ claim が続いたか、別 successor か、selection が post-hoc かを保存しない。

## 14. Persistence matrices

### Table A — feature persistence

| Feature | R0 | R1 | R2 | R3 | R4 |
|---|---|---|---|---|---|
| A before/after relation | LOST | PRESERVED | PRESERVED | PRESERVED | PRESERVED |
| B failure before or after | PARTIALLY PRESERVED | PRESERVED | PRESERVED | PRESERVED | PRESERVED |
| C semantic effect changed | LOST | PRESERVED | PRESERVED | PRESERVED | PRESERVED |
| D retained component changed | LOST | PRESERVED, frame-relative | PRESERVED, frame-relative | PRESERVED, frame-relative | PRESERVED, frame-relative |
| E terminal disposition | PARTIALLY PRESERVED | PARTIALLY PRESERVED | PARTIALLY PRESERVED | PRESERVED | PRESERVED |
| F branch/successor | LOST | LOST | LOST | PRESERVED | PRESERVED |
| G provenance | LOST | LOST | LOST | LOST | PRESERVED |
| H intervention occurred | LOST | PARTIALLY PRESERVED | PARTIALLY PRESERVED | PRESERVED on frozen set | PRESERVED on frozen set |

### Table B — history common content

| History | Common semantic content | Lost at coarse frames | First frame where extra distinction appears |
|---|---|---|---|
| H1 | endpoint success; no counterexample | before failure and route | R1 semantic transition; R2 H-slot; R4 provenance |
| H2 | endpoint success; no counterexample | before failure and scope event | R1 explicit \(S\); R2 S-slot |
| H3 | endpoint success; no counterexample | before failure and target change | R1 target-model change; R2 raw C-slot |
| H4 | endpoint failure; counterexample remains | withdrawal | R3 status |
| H5 | endpoint success; no counterexample | withdrawn original and successor | R3 history/identity |
| H6 | endpoint success; no counterexample | same-id continuation | R3 identity assertion |
| H7 | endpoint success; no counterexample | \(\neg\neg p\) syntax | R2 raw syntax |
| H8 | endpoint failure; counterexample remains | \(+\top\) event | R2 raw H-slot |
| H9 | endpoint success; no counterexample | post-hoc selection | R2 typed H-slot; R4 provenance |
| H10 | endpoint success; no counterexample | independent motivation | R2 typed H-slot; R4 provenance |
| C-F | endpoint failure; counterexample remains | no-intervention history | R3 no-transition/status record |
| C-D | endpoint success; no counterexample | verbatim insertion | R2 raw syntax |

## 15. Mechanically checkable part

Companion checker は既存 sensitivity checker を変更せず import し、以下だけを検査する。

- R0–R4 projection equality / inequality;
- endpoint semantic status;
- counterexample remaining;
- before/after semantic equality;
- changed-slot field presence;
- id/status/successor/provenance field presence;
- selected fields の deletion effects;
- K2 equality;
- H7/C-D、H9/H2、H5/H6、H9/H10、H8/C-F の expected collapse/distinction。

checker は判断しない。

- what is truly fundamental;
- what is ontologically primitive;
- which frame is correct;
- whether an event “really” happened beyond frozen source history;
- whether identity is legitimate;
- whether provenance is trustworthy;
- whether a common projection is canonical;
- whether persistence implies importance。

全 histories について同じ K2 を各 R0–R4 projection から抽出でき、selected erasure checks も通過した。これは implementation consistency の確認であり、persistence の意義の adjudication ではない。

## 16. Answers to key questions

1. **Is any feature preserved across all R0–R4?** 限定的に yes。designated endpoint semantic success/failure と counterexample remains は全 projections から読める。
2. **What kind of persistence is it?** 値は Type 1 semantic。全 frame に出ることは shared endpoint fields に依存する Type 2 representational persistence でもある。source-history persistence とは別。
3. **Is “event occurred” preserved across all frames?** No。H8/C-F が R0/R1 で collapse する。
4. **Is endpoint semantic outcome preserved across all frames?** Yes, for these selected projectors and frozen histories。
5. **Is before/after relation preserved across all frames?** No。R0 は before を保持しない。
6. **Which features disappear first under coarse projection?** provenance、successor、withdrawal/identity、raw slots/syntax、before/after direction の順序づけではなく、R0 でそれらが一括して失われる。
7. **Which features require typed slots?** raw H/C/S change、\(+\top\)、\(\neg\neg p\) versus \(p\)、matched M1/scope carrier difference。R2 から。
8. **Which require history/status?** withdrawn versus failed、same-id versus new successor、split relation。R3 から。
9. **Which require provenance?** H9 POST_HOC versus H10 INDEPENDENT、UNKNOWN versus INAPPLICABLE。R4 から。
10. **Does any candidate deserve “invariant”?** No。K1/K2 は selected projectors に共通するが、その共通性は projector design に依存し、finite frozen range 外も未検査である。

## 17. Retain / revise / downgrade / kill

対象命題は “there exists a frame-independent minimal core of proof-formation records” である。

- **RETAIN — limited:** selected R0–R4 の全てから endpoint semantic outcome / counterexample-remains pair を回収できる。何も共通しないわけではない。
- **REVISE — triggered:** surviving content は endpoint semantics と shared projector construction に限定される。“frame-independent” を強く読めない。
- **DOWNGRADE — triggered:** common projection は formation history を区別するには粗すぎる。required collapse cases の全てを失う。
- **KILL — not triggered for the selected projections:** K1/K2 という非空の common content がある。ただし arbitrary frames を越える fundamental core claim は support されず、invariant reading は採用しない。

この disposition は、common endpoint projection を保存しつつ、それを formation record の十分条件や v0.2 foundation に昇格させないという意味である。

## 18. Important caution: projection-induced persistence

今回の最重要 control は、feature の由来を次の二つに分けることである。

1. underlying history / semantics にその値があること;
2. all projectors がその値を残すよう設計されていること。

K1/K2 の endpoint consequence value は truth table から監査できる。その意味では semantic fact である。しかし R0 が endpoint outcome を定義上保持し、R1 が endpoint semantic state を保持し、R2–R4 が R1 を継承するため、R0–R4 の全てから K1/K2 が読めること自体は design consequence である。

同様に、designated endpoint の存在も全 projector が endpoint を出力するという shared convention から来る。別の observation scheme が endpoint semantics を捨てる可能性はこの test で排除されていない。

したがって本テストが観測したのは

> persistence across these selected projectors

であって、

> frame-independent discovery

ではない。before/after を R1–R4 が保持する persistence も shared projector design であり、しかも R0 では消える。この control のため、K1/K2 を invariant、canonical core、または sufficient representation と呼ばない。

## 19. Final report

1. **Strongest cross-frame persistence:** designated endpoint の semantic success/failure と counterexample remains。
2. **Strongest non-persistence:** “an intervention occurred”。H8 \(+\top\) と C-F no intervention は R0/R1 で collapse する。
3. **Source-history fact invisible in coarse frames:** H5 の original withdrawal + successor、または H8 の \(+\top\)。
4. **Semantic fact preserved everywhere:** designated endpoint が entails するか、および endpoint \(E\) が空か。
5. **Typed fact lost without R2:** raw H/C/S changed slot。例は H9/H2 の H-versus-S carrier difference。
6. **History fact lost without R3:** H5 withdrawal+successor versus H6 same-id continuation。
7. **Provenance fact lost without R4:** H9 `POST_HOC` versus H10 `INDEPENDENT`。
8. **Does a common projection exist?** Yes。K1/K2 は selected R0–R4 から抽出できる。
9. **Is it sufficient for formation history?** No。withdrawal、successor、event、route、syntax、provenance を collapse する。
10. **Is “invariant” justified?** No。persistence は selected frame family と shared projector design に依存する。
11. **Disposition:** **RETAIN (limited) + REVISE + DOWNGRADE; KILL not triggered for the selected projections.**
12. **v0.2:** remain postponed。common endpoint projection を successor architecture の foundation にする根拠は得られていない。

---

**End of cross-frame persistence test.** Existing files were not modified. No new move code、canonical schema、fundamental invariant、frame ranking、score、or generalization was introduced.
