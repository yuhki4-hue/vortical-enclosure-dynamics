# Proof-Formation Record-Frame Sensitivity Test v0.1

- **Status:** exploratory sensitivity test
- **Environment:** finite propositional prototype only
- **Input posture:** prototype、stress test、post-mortem、および既存の inter-reader records を変更せずに使用
- **Date:** 2026-09-06
- **Companion:** [`proof_formation_record_frame_sensitivity_checker_v0.1.py`](./proof_formation_record_frame_sensitivity_checker_v0.1.py)

## 0. Status / posture

- **exploratory sensitivity test**
- **not a theorem**
- **not a new framework**
- **not a v0.2 proposal**
- **not a validation report**
- **not a claim that any record frame is objectively correct**
- **not a claim that richer frames are better**
- **not a claim that action types are pre-given**
- **no new move codes**
- **no score**
- **no optimization**
- **no geometry / metric / lattice / topology**
- **no generalization beyond this finite prototype**

中心問いは次だけである。

> Given the same underlying history,  
> which distinctions are preserved, collapsed, or introduced  
> by different record frames?

R0–R4 はこの問いのための一時的な observation schemes である。canonical な layer 数、正式 record schema、または successor architecture の候補ではない。blind-reader experiment は遡及的に書き換えず、本テストとの関係は toy analogue に限定する。

## 1. Core distinction

### 1.1 Underlying history

本テストの **underlying history** は、各例について事前に固定した次の有限 source record である。

- before claim / state;
- observed failure or trigger;
- an actual intervention or handling event;
- after state(s);
- status / identity / provenance facts when explicitly stipulated.

この history を「真の行動実体」とはみなさない。ここで truth table から回収できるのは semantic facts だけであり、intervention、identity、segmentation、provenance はテスト入力として明示された事実である。history は action taxonomy の代替となる基礎実体ではなく、異なる projection に同じ入力を渡すために凍結した記録にすぎない。

### 1.2 Record frame

**Record frame** は、underlying history のどの情報を保持し、どの情報を捨てるかを決める projection / observation scheme である。本テストでは R0–R4 を使う。

record frame は action taxonomy と同一ではない。action label を保持しなくても、`H`、`C`、`S` のどの slot が変化したかを事前に分ければ、その typing 自体が action distinction を可視化しうる。逆に slot、identity、status、provenance を捨てる frame では、実際に異なると stipulate された histories が collapse しうる。

## 2. Frozen underlying histories

全 frame に同じ histories を通す。共通の finite base は

\[
V=\{p,q\},\qquad
\Omega=\{\omega_{00},\omega_{01},\omega_{10},\omega_{11}\},
\]

\[
H_0=\{p\lor q\},\qquad C_0=p,
\]

\[
M(H_0)=\{\omega_{01},\omega_{10},\omega_{11}\},
\quad M(C_0)=\{\omega_{10},\omega_{11}\},
\quad E(H_0,C_0)=\{\omega_{01}\}
\]

である。全 H1–H10 の failure witness は \(\omega_{01}\)。指定がない限り original identity は \(x_0\) である。

### H1 — ordinary assumption strengthening

- Intervention: \(B=\{\neg q\}\) を追加。
- After: \(H_1'=\{p\lor q,\neg q\}\), \(C'=p\), \(S'=\Omega\)。
- \(M(H_1')=\{\omega_{10}\}\), \(E(H_1',p)=\varnothing\)。
- Status: `established`; \(x_0\) continues。
- Provenance: `INDEPENDENT` と明示的に stipulate する。これは真理値表からの inference ではない。

### H2 — scope-restriction analogue

- Intervention: \(S\) を
  \[
  S_2'=\Omega\setminus\{\omega_{01}\}
  =\{\omega_{00},\omega_{10},\omega_{11}\}
  \]
  へ制限。
- After: \(H'=H_0\), \(C'=p\)。
- \(M(H_0)\cap S_2'=\{\omega_{10},\omega_{11}\}\), \(E_{S_2'}(H_0,p)=\varnothing\)。
- Status: `established` relative to \(S_2'\); \(x_0\) continues。
- Provenance: `UNKNOWN`。

### H3 — conclusion weakening

- Intervention: \(C_0=p\) を \(C_3'=p\lor q\) へ変更。
- After: \(H'=H_0\), \(S'=\Omega\)。
- \(M(C_3')=\{\omega_{01},\omega_{10},\omega_{11}\}\), \(E(H_0,C_3')=\varnothing\)。
- Status: `established`; \(x_0\) continues。
- Provenance: selection reason は `UNKNOWN`。

### H4 — withdrawal only

- Intervention: semantic repair なし。\(H,C,S\) は不変。
- Original status: \(x_0\) is `withdrawn`。
- \(E(H_0,C_0)=\{\omega_{01}\}\) は残る。
- Successor: none。
- Restriction-selection provenance: `INAPPLICABLE`。\(H,C,S\) を変える selection がないことが history に明記されているためである。

### H5 — withdrawal plus successor

- Original: \(x_0=(H_0,p)\) is `withdrawn`。
- Successor:
  \[
  x_1=(\{p\lor q,\neg q\},p),\qquad x_1\ne x_0.
  \]
- Successor status: `established`。
- Segmentation: withdrawn original と successor introduction の split record。
- Successor restriction provenance: `UNKNOWN`。

### H6 — same-id continuation

- Mathematical after-material は H5 と同一：\(H'=\{p\lor q,\neg q\}\), \(C'=p\)。
- Intervention: \(x_0\) を継続し、\(\neg q\) を追加。
- Status: \(x_0\) is `established` under strengthened assumptions。
- Segmentation: single continuation。
- Provenance: `UNKNOWN`。

### H7 — semantically equivalent target insertion

- Intervention: target \(p\) そのものではなく \(\neg\neg p\) を追加。
- After: \(H'=\{p\lor q,\neg\neg p\}\), \(C'=p\)。
- \(M(\neg\neg p)=M(p)\) なので \(M(H')=\{\omega_{10},\omega_{11}\}\) and \(E(H',p)=\varnothing\)。
- Status: `established`; \(x_0\) continues。
- Provenance: `UNKNOWN`。verbatim comparator と provenance を同じにして、syntax と semantics の差だけを試す。

### H8 — no-op strengthening

- Intervention: \(\top\) を追加。
- After: \(H'=\{p\lor q,\top\}\), \(C'=p\)。
- \(M(H')=M(H_0)\), \(E(H',p)=\{\omega_{01}\}\)。
- Status: `failed`; \(x_0\) continues。
- Provenance: `UNKNOWN`。実際の syntactic intervention はあるが、semantic state は変わらない。

### H9 — post-hoc exact-filter repair

Let

\[
\varphi_F=p\lor\neg q,
\qquad M(\varphi_F)=\{\omega_{00},\omega_{10},\omega_{11}\}.
\]

- Intervention: failure 観測後に \(B=\{\varphi_F\}\) を選び追加。
- After:
  \[
  M(H_0\cup\{\varphi_F\})
  =\{\omega_{10},\omega_{11}\}
  =M(H_0)\cap M(C_0).
  \]
- Status: `established`; \(x_0\) continues。
- Provenance: explicitly `POST_HOC`。

### H10 — independently motivated repair with the same semantic result

- Formula、before、after、identity、segmentation、status は H9 と同一。
- Intervention: 同じ \(\varphi_F=p\lor\neg q\) を追加。
- Provenance: failure 観測とは独立に選ばれていたと `INDEPENDENT` を stipulate する。

H10 の independent motivation は test input であり、checker が信用性を検証したものではない。H9/H10 は exact same after-state を作れるため、近似 pair を使う必要はなかった。

### Two comparison controls

H1–H10 を変えず、要求された P3/P6 と frame invisibility を比較するため、次の二 record だけを追加する。

- **C-F — failed, not withdrawn:** \(H,C,S\) は base のまま、intervention なし、status `failed`, provenance `INAPPLICABLE`。
- **C-D — verbatim target insertion:** \(B=\{p\}\) を追加、\(x_0\) continues、status `established`, provenance `UNKNOWN`。H7 と同じ semantic after-state を持つ。

## 3. Candidate record frames

以下は test-local projections であり、formal record schema ではない。R0–R4 の個数や順序も canonical ではない。

### R0 — outcome-only frame

保持するもの：

- designated endpoint の terminal semantic success/failure;
- designated endpoint に counterexample が残るか。

H5 のように original と successor が併存する場合、R0 は designated endpoint である successor だけを出力し、withdrawn original を捨てる。この endpoint selection 自体が R0 の事前選択である。

### R1 — semantic frame

before と designated after について、次を保持する。

\[
\big(M(H),M(C),S,M(H)\cap S,E_S(H,C),H\models_S C\big).
\]

このテストでは \(H\) と \(C\) を raw formula syntax ではなく model sets として extensionally 保持し、\(S\) は独立 field として保持する。したがって R1 は evaluated effect \((M(H)\cap S,M(C))\) より豊かであり、すでに `M(H)` と `S` の carrier roles を事前に分けている。

保持しないもの：move label、raw formula syntax、id、semantic `established/failed` を超える status、provenance、successor relation、episode segmentation。

### R2 — typed-transition frame

R1 に加えて次を保持する。

- raw \(H,C,S\) の before / after slots;
- `H`、`C`、`S` のどの slot が syntactically changed したか。

このテストでは action label を入力から転記しない。slot pattern が一意な場合に M1/M2/scope-compatible な形を読めるが、checker は「実際にその move だった」と判定しない。特に H5 の predecessor/successor 関係を捨てた R2 は、H6 と同じ `H changed` record になる。

保持しないもの：id、withdrawn、successor、provenance、episode segmentation。

### R3 — history/status frame

R2 に加えて次を保持する。

- original id と endpoint id;
- same/different identity assertion;
- `withdrawn` と endpoint status;
- successor relation;
- recorded episode segmentation。

provenance / motivation は保持しない。identity の正当性を semantics から推論もしない。

### R4 — provenance-complete frame

R3 に加えて次を保持する。

- restriction / replacement がいつ、なぜ選ばれたと record されているか;
- `POST_HOC` versus `INDEPENDENT`;
- information がないときの `UNKNOWN`;
- underlying history が selection 自体の不存在を明記するときだけ `INAPPLICABLE`。

R4 は本テストで最も多くの stipulated fields を保持するだけであり、“best” または complete ではない。provenance statement の信用性も判定しない。

## 4. Projection discipline

1. 全 Rj に同じ H1–H10、C-F、C-D を入力する。
2. R0/R1 は formula から id を再構成しない。
3. R1 は raw syntax を model-set equality より復元しない。
4. R2 は post-hocness、independent motivation、withdrawal、successor relationを推論しない。
5. R3 は provenance を推論しない。同じ after-formula から identity continuity も推論しない。
6. R4 は underlying history に明記された provenance だけを転記する。semantic shape が exact filter でも、明示がなければ `UNKNOWN` のままとする。
7. `INAPPLICABLE` は transition/provenance target が存在しないと明記された C-F と、\(H,C,S\) selection のない H4 にだけ使う。
8. H5 の R0–R2 projection が withdrawn original を失っても、そこから「withdrawal がなかった」とは推論しない。これは omission の結果である。

## 5. Pairwise distinguishability

判定語は次に限定する。

- **DISTINCT:** 二つの projected records が異なる。
- **COLLAPSED:** underlying histories は異なるが、frame 内の projected records が同一。
- **NOT REPRESENTABLE:** frame に投影可能な record 自体が作れない。
- **AMBIGUOUS:** frozen history または projection rule が一意の record を定めない。

本テストでは histories と projection rules を明示的に freeze したため、P1–P9 の各投影は作成でき、`NOT REPRESENTABLE` と `AMBIGUOUS` は生じない。たとえば R2 は withdrawal action 自体を表現できないが、その残余 semantic/typed state は投影できるので、H4/C-F は `NOT REPRESENTABLE` ではなく `COLLAPSED` とする。

要求された minimum pairs は次である。

- P1: H1 / H2 — ordinary strengthening versus specified scope restriction。
- P2: H1 / H3 — assumption strengthening versus conclusion weakening。
- P3: H4 / C-F — withdrawn versus merely failed。
- P4: H5 / H6 — withdrawal+successor versus same-id continuation。
- P5: H9 / H10 — post-hoc versus independently motivated exact same transition。
- P6: H7 / C-D — semantically equivalent insertion versus verbatim target insertion。
- P7: H1 / H8 — successful strengthening versus no-op strengthening。

二つの controlled checks も追加する。

- P8: H9 / H2 — identical evaluated after-effect を持つ matched M1/scope pair。
- P9: H8 / C-F — real syntactic intervention versus no intervention。

## 6. Preservation / collapse / induced distinction

- **Preserved distinction:** underlying histories に明記された差を frame が対応 field として保持する。例：R4 が H9/H10 の stipulated provenance を保持する。
- **Collapsed distinction:** histories に差があるが、projection が同一になる。例：R0–R2 で H5/H6 が同一になる。
- **Induced distinction:** lower evaluated semantics では同一な二 history が、frame が事前に分けた slot/type/syntax field により異なる record になる。

`induced` は false や useless を意味しない。semantic effect から生じた差か、record carrier が別 fields を事前登録したことで生じた差かを区別する語としてだけ使う。

## 7. Central test: M1 versus scope

### 7.1 Required P1 is not an exact semantic match

指定された H1 と H2 は terminal success と empty \(E\) を共有するが、surviving valuations は異なる。

\[
\operatorname{survive}(H1)=\{\omega_{10}\},
\qquad
\operatorname{survive}(H2)=\{\omega_{10},\omega_{11}\}.
\]

したがって P1 は R0 では collapse するが、surviving set を保持する chosen R1 では DISTINCT である。ここを stress-test の exact M1/scope collapse として扱うことはできない。

### 7.2 Matched P8

H9 と H2 は次の evaluated after-effect を共有する。

\[
M(H)\cap S=\{\omega_{10},\omega_{11}\},
\quad M(C)=\{\omega_{10},\omega_{11}\},
\quad E_S=\varnothing,
\quad H\models_S C.
\]

しかし histories は異なる。

- H9: \(H\) slot に \(p\lor\neg q\) を追加し、\(S=\Omega\) のまま。
- H2: \(H=H_0\) のまま、\(S\) slot を \(\Omega\setminus\{\omega_{01}\}\) に変更。

Frame ごとの結果：

- **R0:** COLLAPSED。success / empty \(E\) だけでは差がない。
- **R1:** chosen full carrier では DISTINCT。H9 は \(M(H')=\{\omega_{10},\omega_{11}\},S=\Omega\)、H2 は \(M(H')=\{\omega_{01},\omega_{10},\omega_{11}\},S=S_2'\) を保持する。ただし evaluated subprojection \((M(H)\cap S,M(C),E_S,\models_S)\) へ落とすと COLLAPSED。したがって R1 の差は already chosen carrier roles に依存する。
- **R2:** DISTINCT。`H changed` と `S changed` を別 slot として保持する。
- **R3:** DISTINCT。R2 の差を継承する。両方とも same-id continuation なので identity が新しい差を作るわけではない。
- **R4:** DISTINCT。さらに H9=`POST_HOC`、H2=`UNKNOWN` という provenance 差も保持する。

中心問いへの答え：

> R2 は evaluated semantics にすでにあった差を回収したのではない。  
> `H` と `S` を別 slot として事前登録したことにより、semantic effect にない typed distinction を保持した。

chosen R1 full carrier も同じ差をすでに含むが、それは R1 が \(M(H)\) と \(S\) を別々に保持すると決めたからである。この結論は finite scope surrogate にだけ当てはまり、M3/M4 や他の restriction へ一般化しない。

## 8. Central test: provenance

H9 と H10 は formula、raw slots、semantic before/after、identity、status、segmentation が同一で、stipulated provenance だけが異なる。

| Frame | H9 versus H10 |
|---|---|
| R0 | COLLAPSED |
| R1 | COLLAPSED |
| R2 | COLLAPSED |
| R3 | COLLAPSED |
| R4 | DISTINCT — `POST_HOC` versus `INDEPENDENT` |

これは、provenance が record されるまで一部の distinction が不可視であることを示す。semantic shape から provenance を infer してはいない。H10 の independence は入力として stipulate され、R4 はそれを転記するだけである。したがって provenance があらゆる formation question に常に必要だとは結論しない。

## 9. Central test: identity / episode boundary

H5 と H6 は同じ before と mathematical after-material を持つ。

- **R0:** designated endpoint はどちらも semantically established、\(E=\varnothing\)。COLLAPSED。
- **R1:** before / after semantic states が同じ。COLLAPSED。
- **R2:** raw before/after slots も同じで、どちらも `H changed`。id、withdrawal、successor link を保持しないので COLLAPSED。
- **R3:** 初めて DISTINCT。H5 は `x0 withdrawn → successor x1 established` の split、H6 は `x0 continues → established` の single continuation。
- **R4:** DISTINCT のまま。両者の provenance は `UNKNOWN` なので、追加の provenance distinction はない。

したがって、“same claim repaired” と “original withdrawn + successor introduced” が初めて区別可能になるのは **R3** である。これは prior episode-boundary issue の toy analogue にすぎず、H5 と H6 のどちらが客観的に正しい segmentation かを決めない。

## 10. Central test: frame invisibility

### 10.1 H8 versus C-F

H8 では \(\top\) を実際に追加する。C-F では何もしない。それでも

\[
M(H_0\cup\{\top\})=M(H_0),
\qquad E(H_0\cup\{\top\},p)=E(H_0,p).
\]

- R0: both failed with a counterexample — COLLAPSED。
- R1: raw syntax を捨てるので同じ \(\sigma_0\to\sigma_0\) — COLLAPSED。
- R2: `H:+\top` versus `no slot change` — DISTINCT。
- R3/R4: R2 の差を継承して DISTINCT。

実在すると stipulate された intervention が R1 では不可視で、R2 では可視になる。

### 10.2 H7 versus C-D

\(\neg\neg p\) と \(p\) は同じ model set を持つため R0/R1 は collapse する。R2 は raw formula syntax を保持するので `H:+¬¬p` と `H:+p` を区別する。これは semantic target insertion と verbatim insertion の差を truth table が作ったのではなく、syntax-bearing record が作った distinction である。両者の provenance は `UNKNOWN` のままであり、R4 もそこから motivation を推論しない。

## 11. Central test: frame-induced distinction

主要例は matched H9/H2 である。evaluated after-effect は同一だが、full R1 と R2 は `M(H)`/`S`、さらに raw `H`/`S` を separate carriers として保持するため DISTINCT になる。

第二例は H7/C-D である。R1 は formula を model sets として保持するため collapse し、R2 は raw syntax を保持するため distinct になる。

ここから言えるのは次だけである。

- semantic indistinguishability does not imply historical identity;
- typed distinguishability does not imply semantic distinction;
- record design determines which distinctions are observable in that record.

typed distinction が有用か、どの carrier が正しいかはこの test の外にある。frame-induced distinction を artificial または false とは呼ばない。

## 12. Minimal projection tables

### 12.1 Compact semantic-state notation

以下で \(A=M(H)\), \(T=M(C)\), \(Q=A\cap S\) とする。

- \(\sigma_0\): \(A=\{01,10,11\},T=\{10,11\},S=\Omega,Q=\{01,10,11\},E=\{01\},\text{FAIL}\)。
- \(\sigma_1\): \(A=\{10\},T=\{10,11\},S=\Omega,Q=\{10\},E=\varnothing,\text{EST}\)。
- \(\sigma_2\): \(A=\{01,10,11\},T=\{10,11\},S=\{00,10,11\},Q=\{10,11\},E=\varnothing,\text{EST}\)。
- \(\sigma_3\): \(A=T=Q=\{01,10,11\},S=\Omega,E=\varnothing,\text{EST}\)。
- \(\sigma_4\): \(A=T=Q=\{10,11\},S=\Omega,E=\varnothing,\text{EST}\)。

### 12.2 History projections

`EST/FAIL` in R0 は semantic endpoint だけを表す。R2 の `Δ=∅` は \(H,C,S\) slot に変化がないという意味で、history event がなかったという推論ではない。表を短くするため、R3 cell は「R2 に加えて保持する history/status」、R4 cell は「R3 に加えて保持する provenance」を表示する。

| History | R0 | R1 | R2 | R3 | R4 |
|---|---|---|---|---|---|
| H1 | EST; \(E=∅\) | \(\sigma_0→\sigma_1\) | `H:+¬q` | `x0→x0; EST; single` | R3 + `INDEPENDENT` |
| H2 | EST; \(E=∅\) | \(\sigma_0→\sigma_2\) | `S:Ω→Ω\{01}` | `x0→x0; EST; single` | R3 + `UNKNOWN` |
| H3 | EST; \(E=∅\) | \(\sigma_0→\sigma_3\) | `C:p→p∨q` | `x0→x0; EST; single` | R3 + `UNKNOWN` |
| H4 | FAIL; \(E=\{01\}\) | \(\sigma_0→\sigma_0\) | `Δ(H,C,S)=∅` | `x0 withdrawn; no successor` | R3 + `INAPPLICABLE` |
| H5 | EST; \(E=∅\) | \(\sigma_0→\sigma_1\) | `H:+¬q` | `x0 withdrawn; x1 successor EST; split` | R3 + `UNKNOWN` |
| H6 | EST; \(E=∅\) | \(\sigma_0→\sigma_1\) | `H:+¬q` | `x0→x0; EST; single` | R3 + `UNKNOWN` |
| H7 | EST; \(E=∅\) | \(\sigma_0→\sigma_4\) | `H:+¬¬p` | `x0→x0; EST; single` | R3 + `UNKNOWN` |
| H8 | FAIL; \(E=\{01\}\) | \(\sigma_0→\sigma_0\) | `H:+⊤` | `x0→x0; FAIL; single` | R3 + `UNKNOWN` |
| H9 | EST; \(E=∅\) | \(\sigma_0→\sigma_4\) | `H:+(p∨¬q)` | `x0→x0; EST; single` | R3 + `POST_HOC` |
| H10 | EST; \(E=∅\) | \(\sigma_0→\sigma_4\) | `H:+(p∨¬q)` | `x0→x0; EST; single` | R3 + `INDEPENDENT` |
| C-F | FAIL; \(E=\{01\}\) | \(\sigma_0→\sigma_0\) | `Δ(H,C,S)=∅` | `x0 failed; no transition` | R3 + `INAPPLICABLE` |
| C-D | EST; \(E=∅\) | \(\sigma_0→\sigma_4\) | `H:+p` | `x0→x0; EST; single` | R3 + `UNKNOWN` |

### 12.3 Pairwise distinguishability

| Pair | R0 | R1 | R2 | R3 | R4 |
|---|---|---|---|---|---|
| P1 H1/H2 | COLLAPSED | DISTINCT | DISTINCT | DISTINCT | DISTINCT |
| P2 H1/H3 | COLLAPSED | DISTINCT | DISTINCT | DISTINCT | DISTINCT |
| P3 H4/C-F | COLLAPSED | COLLAPSED | COLLAPSED | DISTINCT | DISTINCT |
| P4 H5/H6 | COLLAPSED | COLLAPSED | COLLAPSED | DISTINCT | DISTINCT |
| P5 H9/H10 | COLLAPSED | COLLAPSED | COLLAPSED | COLLAPSED | DISTINCT |
| P6 H7/C-D | COLLAPSED | COLLAPSED | DISTINCT | DISTINCT | DISTINCT |
| P7 H1/H8 | DISTINCT | DISTINCT | DISTINCT | DISTINCT | DISTINCT |
| P8 H9/H2 | COLLAPSED | DISTINCT | DISTINCT | DISTINCT | DISTINCT |
| P9 H8/C-F | COLLAPSED | COLLAPSED | DISTINCT | DISTINCT | DISTINCT |

P8 の R1 `DISTINCT` は evaluated-effect distinction ではない。full R1 が \(M(H)\) と \(S\) を別 carriers として保持するという choice による。checker は full R1 equality と、より低い evaluated subprojection の equality を別々に確認する。

## 13. Mechanically checkable part

Companion checker は既存 v0.1 checker を変更せず import し、次だけを検算する。

- truth-table equivalence;
- projected semantic states の same/different;
- surviving sets と \(E\) の same/different;
- raw \(H,C,S\) slots の same/different;
- supplied id/status/provenance fields の same/different;
- R0–R4 projected records の equality;
- §12.3 の P1–P9 matrix。

checker は次を判定しない。

- which frame is correct;
- whether an identity assertion is legitimate;
- whether a provenance statement is trustworthy;
- whether a distinction is important;
- whether a frame-induced distinction is desirable;
- whether an action really belongs to a move class。

`intervention` field は frozen input の説明用であり、projection equality を action label で決めるためには使わない。checker 内の dictionaries は実装 scaffolding にすぎず、新しい formal record schema ではない。

実行結果は全 truth-table checks、matched-effect checks、P1–P9 projection comparisons を通過した。

## 14. Sensitivity findings

### F1 — coarse-frame collapse

**Holds.** R0 は H1/H2/H3 の異なる成功 route、H5/H6 の identity history、H9/H10 の provenance を collapse する。

### F2 — typed-slot recovery

**Holds.** R2 は H/C/S のどの slot が変わったかを保持することで H1/H2/H3 を区別し、raw syntax によって H8/C-F と H7/C-D も区別する。

### F3 — frame-induced distinctions

**Holds.** matched H9/H2 の evaluated effect は同一だが、separate `H`/`S` carriers が差を作る。H7/C-D も extensionally同一だが raw syntax field で差が現れる。

### F4 — identity/history threshold

**Holds.** H4/C-F と H5/H6 は R0–R2 で collapse し、id/status/successor/segmentation を保持する R3 で初めて distinct になる。

### F5 — provenance threshold

**Holds.** H9/H10 は R0–R3 で collapse し、R4 で初めて distinct になる。

### F6 — semantic invisibility of no-op/equivalent actions

**Holds.** H8 の \(+\top\) は R1 で no intervention と同一になる。H7/C-D の syntax difference も extensional R1 では消え、R2 で現れる。

### F7 — richer is not automatically more correct

**Holds.** R3/R4 はより多くの stipulated distinctions を保持するので、この有限表ではより informative である。しかし追加情報は identity/provenance assertions を真にせず、どの distinction が task-relevant かも決めない。情報量の増加を correctness や superiority に変換できない。

## 15. Record-frame bias

“Bias” はここで statistical bias や正式 taxonomy を意味せず、projection choice が observed distinction を方向づけるという記述に限定する。

- **Omission bias（descriptive）:** field を捨てるため、本来 stipulated された差が collapse する。H5/H6 は R3 より前、H9/H10 は R4 より前で collapse する。
- **Typing bias（descriptive）:** semantically同じ effect が、separate slots の事前登録によって distinct になる。matched H9/H2 の `H` versus `S` と、H7/C-D の raw syntax が該当する。
- **Identity bias（descriptive）:** R3 は continuity/discontinuity assertion を保持するため H5/H6 を区別するが、その assertion の正当性は確認しない。
- **Provenance bias（descriptive）:** R4 は post-hoc/independent field を許すため H9/H10 を区別するが、semantic shape からその差を発見したのではない。

したがって action を先に taxonomy へ割り当てず self-state change を記録しても、どの state components を別 carriers として事前登録するかによって observed action distinctions は変わった。この意味で **record-frame bias は観測された**。ただし bias は error と同義ではなく、projection に不可避な選択があるという test-local finding である。

## 16. What this test does not show

本テストは次を確立しない。

- the correct carrier;
- the correct number of record layers;
- the correct action taxonomy;
- the correct claim identity criterion;
- the correct episode boundary;
- that richer frames are better;
- that semantic frames are insufficient for every purpose;
- that typed distinctions are artificial;
- that provenance should always dominate;
- that realistic mathematics behaves like this finite prototype。

さらに、R0–R4 が exhaustive/canonical であること、H1–H10 が realistic formation histories を代表すること、または blind-reader differences が本テストで説明されたことも示さない。

## 17. Kill / revise / retain

対象命題は “recording self-state change avoids the bias of pre-registering action types” だけである。

- **RETAIN — limited:** action label を事前入力しなくても、before/after self-state の差から semantic outcome、changed slot、no-op を可視化できた。全 action types を先に列挙する必要はなかった。
- **REVISE — triggered:** self-state registration は carrier、raw syntax、identity、status、successor、provenance のどれを保持するかという prior choices を含む。したがって bias を “avoid” するという強い表現は維持できない。
- **DOWNGRADE — triggered:** record-frame choice が observed action distinctions を大きく左右した。H5/H6、H9/H10、H8/C-F は保持 fields の threshold まで collapse し、H9/H2 と H7/C-D は frame typing によって初めて distinct になった。
- **KILL — not triggered:** semantic、typed-slot、identity/status、provenance の各差は少なくとも一つの frame で有用に区別できた。全 projection を通じて何も残らないわけではない。

結論は、self-state registration を捨てることではない。**一部の action distinction を action label なしで露出できる点を RETAIN し、bias-free という含意を REVISE/DOWNGRADE する。** v0.2 design は依然 postponed とする。

## 18. Final report

1. **Strongest preserved distinction:** R4 が H9/H10 の明示的 `POST_HOC` / `INDEPENDENT` 差を、semantic・typed・identity fields が完全に同じまま保持したこと。
2. **Strongest collapse:** H9/H10 は R0–R3 で完全に collapse する。別軸では H5/H6 が R0–R2 で collapse する。
3. **Strongest frame-induced distinction:** H9/H2 の identical evaluated effect が、`H` と `S` を別 carrier とする frame で distinct になったこと。
4. **First identity-visible frame:** R3。
5. **First provenance-visible frame:** R4。
6. **Action invisible in a coarse frame:** H8 の \(+\top\) は R0/R1 で C-F の no intervention と区別できない。
7. **Were richer frames more informative?** この frozen finite test では yes。より多くの stipulated fields を保持したためである。
8. **Were they shown more correct?** No。identity/provenance の正当性も frame relevance も検証していない。
9. **Did self-change registration remove bias?** No。action-label preclassification を減らせても、carrier/typing/identity/provenance choices による record-frame sensitivity が残った。
10. **Disposition:** **RETAIN (limited) + REVISE + DOWNGRADE; KILL not triggered.** v0.2 は postponed のままとする。

---

**End of sensitivity test.** Existing files were not modified. No action taxonomy、formal record schema、canonical frame set、score、optimization、or generalization was introduced.
