# Reachability-oriented theorem/proof anatomy — synthesis / closure note v0.1

## 0. Status / posture

本稿は、以下の reachability-oriented stress test 系列を閉じるための **synthesis / closure record** である。

- `theorem_proof_anatomy_reachability_test_1_plus_1_eq_2_v0.1_ja.md`
- `theorem_proof_anatomy_reachability_test_addition_commutativity_v0.1_ja.md`
- `theorem_proof_anatomy_reachability_test_ivt_v0.1_ja.md`
- `theorem_proof_anatomy_reachability_test_fta_v0.1_ja.md`
- `theorem_proof_anatomy_reachability_cross_test_audit_v0.1.md`

本稿は：

- not a theorem
- not a new proof theory
- not a new semantics
- not a new framework proposal
- not `theorem_proof_anatomy_v2`
- no score
- no metric
- no proof geometry
- no metaphysical conclusion
- no VED claim

である。

本系列の目的は、新しい用語を維持することではなく、stress test を通して何が残り、何が不要になったかを記録することにある。

---

## 1. Final disposition

### 1.1 Reachability-oriented rewrite is retired

`reachability-oriented theorem/proof anatomy` を独立した rewrite / v2 系列として継続しない。

4本の stress test を通じて、中心語彙はすべて標準語へ無損失で戻った。

- `reachability` → derivability / \(\Gamma\vdash\varphi\)
- `route` → proof / derivation organization
- `constraint propagation` → ordinary proof bookkeeping
- `imported theorem expansion` → citation expansion / dependency tracing
- `setting migration` → change of theory / structure / interpretation

したがって、これらを新しい analytical primitive として維持する根拠はない。

### 1.2 v2 is not postponed; it is retired

`theorem_proof_anatomy_v2` を「後で書く可能性を残して延期する」とはしない。

reachability-oriented rewrite に関しては **retired** とする。

残った成果は、新 anatomy ではなく、既存 `theorem_proof_anatomy_v1.1` の Erasure Test と dependency audit を運用するための監査規律として回収する。

---

## 2. What survived

### 2.1 Different claims require different evidence

本系列で最も強く残ったのは、proof / theorem に関する異なる主張が、異なる証拠責任を持つという区別である。

| claim | sufficient evidence | not sufficient |
|---|---|---|
| この specific proof が壊れた | warrant を失った step を示す | theorem failure の証拠にはならない |
| theoremhood が残る | 同じ theory / target で alternative derivation を1本示す | 全 proof space の調査は不要 |
| non-derivable である | reduced theory の countermodel + soundness、または independence argument | failed proof attempts、citation tracing |
| hypothesis がこの formulation で必要 | hypothesis を落とした / 弱めた statement への counterexample | minimality や唯一の必要条件までは示さない |
| setting / interpretation が変わった | domain、symbol interpretation、object class、theory の変更点を明示 | truth value の比較だけでは元 theorem の反証にならない |
| proof resource が theorem-level に必要 | fixed base theory のもとで、その resource を欠くと non-derivable と示す | 複数 proof の resource intersection |

要約すれば：

\[
\text{proof failure}
\neq
\text{non-derivability}
\neq
\text{setting / claim change}.
\]

これは新しい数学的結果ではない。  
しかし、単一の「壊れた」という記述で異なる counterfactual を処理しないための監査規律として残す。

---

## 3. Dependency trace is not necessity

IVT / FTA stress test から、次の区別を残す。

\[
\text{displayed dependency}
\neq
\text{dependency found by citation expansion}
\neq
\text{theorem-level necessity evidence}.
\]

ある resource が

- proof 本文に現れる
- imported theorem の chosen proof を展開すると現れる
- 複数 proof に共通して現れる

ことは、その resource が theorem に logically necessary であることを示さない。

### 3.1 IVT control

supremum proof では completeness が直接現れた。

connectedness proof では displayed level では現れなかったが、選んだ standard proof of interval connectedness を展開すると least-upper-bound completeness が再登場した。

しかし、

\[
\text{reappears in one expansion}
\not\Rightarrow
\text{theorem-level necessity}.
\]

ordered-field axioms alone が IVT を保証しないことを示す独立 control は、\(\mathbb Q\) 上の \(q^2-2\) であった。

### 3.2 FTA control

Liouville / Cauchy route と winding / covering route は Level 2 まで largely heterogeneous のまま残った。

compactness、continuity、field/norm algebra は両 route に現れたが、そこから theorem-level necessity は得られなかった。

したがって dependency trace と necessity claim は別の証拠型として扱う。

---

## 4. Named theorem resource is not theorem assumption

本系列では繰り返し、次の境界が確認された。

\[
\text{named lemma / imported theorem}
\neq
\text{theorem assumption}.
\]

例：

- addition commutativity の \(L_1,L_2\)
- IVT の connectedness theorem / continuous-image theorem
- FTA の Liouville theorem / winding homotopy invariance

これらは proof organization 上の derived resources であり、名前を消して inline できる場合がある。

したがって今後の anatomy では最低限、

- theorem hypotheses / assumptions
- proof resources / derived theorems
- inference rules
- definitions
- ambient / background assumptions

を分離して記録する。

この区別は `theorem_proof_anatomy_v1.1` にすでに存在しており、本系列はそれを新設したのではなく、stress test で運用上の重要性を確認した。

---

## 5. Structure change is not refutation

4本を通じて、structure / interpretation change を元 theorem の falsification と読み違えないことが繰り返し確認された。

例：

- \(1+1=0\) in \(\mathbb Z/2\mathbb Z\)
- `+` を \(\max\) と解釈する
- IVT-like statement over \(\mathbb Q\)
- FTA-like root claim over \(\mathbb R\)

これらは、元の theorem と同じ statement を同じ structure で falsify したものではない。

したがって、comparison では必ず

- what was preserved
- what was changed
- which corresponding statement is now being tested

を明示する。

---

## 6. Preregistered citation-expansion depth

FTA stress test で導入した Level 0 / Level 1 / Level 2 / STOP は、mathematical invariant ではない。

その価値は **reproducibility** に限定して保持する。

### 6.1 What it improved

- one proof だけを post hoc に深く展開する asymmetry を抑える
- “reappeared” がどの expansion level の claim かを固定する
- comparison boundary 以下を OPEN として止める
- citation boundary だけで heterogeneity を演出する route を比較前に除外できる

### 6.2 What it did not improve

- theorem-invariant な proof depth は得られない
- foundation dependence は消えない
- which imported theorem proof to expand remains a choice
- expansion boundary itself is not mathematically canonical

したがって、この protocol は comparative audit の再現性を高める補助手順としてのみ残す。

---

## 7. What was killed

### 7.1 Reachability as a new primitive — KILL

\[
\text{reachability} = \text{ordinary derivability paraphrase}
\]

以上の analytical content は得られなかった。

### 7.2 Proof as route beyond derivation — KILL

proof route は ordinary derivation / proof organization で尽くされる。

### 7.3 Proof as constraint propagation — KILL as technical concept

説明的 gloss としては読めるが、ordinary proof bookkeeping 以上の内容を与えなかった。

causal / physical / truth-producing reading は採用しない。

### 7.4 Theorem as compressed reachability — KILL

bare theorem formula については不適切であり、\(\Gamma\vdash\varphi\) に直すと standard derivability assertion の言い換えになる。

### 7.5 Dependency relocation as new method — KILL as novelty claim

imported theorem 内で hidden dependency を見つける操作は ordinary citation / dependency tracing である。

### 7.6 Proof heterogeneity as theorem property — KILL / DOWNGRADE

heterogeneity は、

- which proofs are selected
- which imported theorem proofs are expanded
- where expansion stops

に依存する。

したがって theorem 自体の stable property として扱わない。

---

## 8. What changed relative to theorem_proof_anatomy_v1.1

本系列は v1.1 を置換しない。

むしろ、v1.1 の既存 anatomy のうち何を狭めるべきかを示した。

### 8.1 Retain

- object / ambient / background / definitional distinction
- theorem assumptions
- proof resources
- representative proof
- condition-removal stress
- explicit counterexamples / countermodels

### 8.2 Revise the Erasure Test operationally

単一の

> 「この条件・資源を消すと何が壊れるか」

だけではなく、少なくとも次を分ける。

#### E-A — proof-resource deletion
specific lemma / theorem / proof step / proof organization を消す。

問う：

> this proof fails?

theoremhood survival を示すには alternate derivation があればよい。

#### E-B — theory / hypothesis weakening
axiom、theorem hypothesis、object restriction などを弱める。

問う：

> weakened theory / statement still proves the target?

non-derivability / necessity claim には countermodel、counterexample、independence 等が必要。

#### E-C — setting / interpretation change
domain、structure、symbol interpretation、object class を変更する。

問う：

> still the same theorem?

truth value を比較する前に claim identity / preservation を監査する。

これは新しい formal taxonomy ではなく、Erasure Test の evidence burden を混同しないための operational split である。

### 8.3 Narrow R0 / R1 / R2

R0 / R1 / R2 は 21 theorem の condition-removal residue survey では比較語として残してよい。

しかし今回の single-theorem reachability stress tests では主診断としてほぼ機能せず、R2 は一度も中心的役割を持たなかった。

したがって R0/R1/R2 を single-theorem proof dependency audit の一般分類へ拡張しない。

---

## 9. Strongest negative result

4本の reachability stress test は、新しい theorem/proof anatomy を生成しなかった。

さらに、IVT / FTA で theorem-level necessity として独立に確認できたものは主に statement-side conditions であり、v1.1 がすでに assumptions として記録していたものを越えなかった。

したがって、この系列が増やしたのは

> what is necessary

についての新しい結果ではなく、

> what evidence is required before saying “necessary”

についての監査規律である。

これは本系列の最も重要な negative result とする。

---

## 10. Two remaining gaps

### 10.1 Fixed-base-theory necessity framework

本系列が繰り返し到達した問いは：

> is this resource actually necessary for the theorem?

であった。

しかし、informal proof comparison、citation expansion、route intersection だけではこの問いを一般に解けない。

この問いには fixed base theory を用いる既存の標準的方法がある。  
今後この方向へ進む場合は、reverse mathematics / proof-theoretic strength comparison 等の既存 apparatus と接続し、informal Erasure Test の判定と外部既知結果を比較する。

この接続は本稿では未実施とする。

### 10.2 Independent-reader reproduction

reachability 系列の4 test は single-author analysis である。

一方、proof-formation strand ではすでに、

- segmentation
- claim identity
- role assignment
- assumption vs proof-resource boundary

が reader によって揺れることが確認されている。

今回の

- what counts as a route
- what counts as a major imported theorem
- which standard proof is expanded
- where Level 2 stops

も reader-sensitive な judgment を含む。

したがって、将来 comparative audit を一般化する場合には independent reader reproduction が必要になる。

---

## 11. No automatic fifth theorem

FTA までで、

- route / theorem / setting separation
- heterogeneous proof comparison
- imported dependency expansion
- preregistered expansion boundary

は一通り stress された。

したがって variety を増やすだけの fifth theorem は追加しない。

追加するとすれば、先に新しい falsification question を固定する。

候補となる問いは：

> Does the informal necessity audit agree with a theorem whose proof-theoretic / reverse-mathematical strength is already externally settled?

この問いを採用する場合のみ、Bolzano–Weierstrass など既知の strength classification を持つ theorem を calibration target として使う価値がある。

これは reachability-oriented anatomy の continuation ではなく、v1.1 Erasure Test の external calibration である。

---

## 12. Final retained protocol

今後 theorem/proof anatomy で condition/resource removal を監査する場合、最低限次を確認する。

1. **What exactly was changed?**
   - proof resource
   - theorem hypothesis / theory
   - structure / interpretation

2. **What claim is being made?**
   - this proof fails
   - theoremhood survives
   - theorem is non-derivable
   - a hypothesis is necessary
   - setting changed

3. **What evidence matches that claim?**
   - broken step
   - alternative derivation
   - counterexample
   - countermodel + soundness
   - independence result
   - preservation / interpretation audit

4. **If imported theorems are compared, where does expansion stop?**
   - preregister the comparison depth when reproducibility matters

5. **Do not infer necessity from occurrence.**
   - visible use is not necessity
   - expanded use is not necessity
   - common use across several proofs is not necessity

6. **Keep assumptions and proof resources separate.**

7. **Treat structure migration as a different statement unless preservation is explicitly established.**

---

## 13. Closure statement

The reachability-oriented rewrite is closed.

Its bespoke vocabulary did not survive stress testing as new mathematical structure.

What survived is narrower and more useful:

> **Do not ask only “what broke?”  
> Ask what claim about the break is being made, and require evidence of the appropriate logical form.**

This result is methodological, not mathematical.

It should be folded back into `theorem_proof_anatomy_v1.1` as an audit discipline for Erasure Tests, while the reachability-oriented v2 line is retired.

No `theorem_proof_anatomy_v2` is created by this record.
