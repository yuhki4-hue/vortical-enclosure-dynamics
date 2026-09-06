# Proof-Formation Frozen Toy Corpus v0.1

- **Status:** frozen input packet for the pre-Phase-0 inter-reader reconstruction test
- **Basis:** [`proof_formation_meta_experiment_v0.1.md`](./proof_formation_meta_experiment_v0.1.md), §12.2
- **Corpus size:** 12 episodes
- **Use:** coderには本ファイルと[`coder instructions`](./proof_formation_coder_instructions_v0.1.md)だけを先に渡す
- **Answer key:** 本文から分離し、[`adjudication rules`](./proof_formation_adjudication_rules_v0.1.md)に置く

このcorpusは基準文書§12.2の12候補を、その順序のまま固定したconvenience sampleである。prevalence、universality、move taxonomyの完全性を推定しない。excerptは原文からそのまま抜き出した。見出し用の要約はsource excerptではない。coderは必要なら記載pathの原sourceへ戻ってよいが、trajectory summary、meta-experimentのnode ledger、answer key、他readerの記録は提出前に見ない。

---

## E01 — Observation-map noninjectivity

**Source path:** `notes/theorem_proof_anatomy_experiment/00_origin/tool_truth_absence_working_note_v0.2.md`, Phase 1

**Excerpt 1**

> **当初の仮説。** 候補世界集合 $W$、ログ空間 $L$、観測写像
>
> $$
> O:W\to L
> $$
>
> について、
>
> $$
> O(w_1)=O(w_2),\qquad w_1\neq w_2
> $$
>
> ならば、ログから世界を一意に復元できない。この構造を「観測写像の存在論的非一意性定理」として一般化できるのではないか。

**Excerpt 2**

> **何によって壊れたか。** これは inverse problems、identifiability、observational equivalence、quotient/fiber の基本設定そのものである。非単射写像に左逆がないこと以上の内容は、$O$ が非単射でなければならない条件を別途示さない限り得られない。また $O=\mathrm{id}_W$ は即座の反例である。

**Excerpt 3**

> **撤回したもの。** [WITHDRAWN] 「観測写像の存在論的非一意性」を新しい一般定理として主張すること。
>
> **残ったもの。** [ESTABLISHED] 観測同値類と採用した構造同型類は区別しなければならない。識別可能性はモデルクラスと実験族に相対的である。

---

## E02 — Self-containment impossibility and conditional capacity

**Source path:** `notes/theorem_proof_anatomy_experiment/00_origin/tool_truth_absence_working_note_v0.2.md`, Phase 2

**Excerpt 1**

> **当初の仮説。** 観測者が世界内部の物理過程なら、観測は静的写像ではなく
>
> $$
> W_t\xrightarrow{\mathcal O_A}(W_{t+1},l)
> $$
>
> と書くべきであり、自己を含む世界の完全記述は一般に不可能ではないか。

**Excerpt 2**

> **何によって壊れたか。** 自己包含だけでは非単射性は導けない。有限候補 $\Omega$ と十分大きな内部記憶 $M$ に対し、閉じた系
>
> $$
> X=\Omega\times M,
> \qquad
> (\theta,m_0)\mapsto(\theta,\operatorname{enc}(\theta))
> $$
>
> を作れば、内部観測者は候補を一意に記録できる。無限集合では真部分集合と全体が同じ濃度を持ちうる。さらに自己出力プログラム（quine）や Kleene の再帰定理は、適切な計算モデルでは自己記述が可能であることを示す。Breuer の自己測定制約や Wolpert の inference-device 不可能性には、真部分系への制限、全状態の識別要求、固定された出力意味論、自己問合せ閉包など追加条件がある。

**Excerpt 3**

> **撤回したもの。** [WITHDRAWN]
>
> $$
> \text{self-containment}
> \Rightarrow
> \text{universal non-identifiability}.
> $$
>
> **残ったもの。** [ESTABLISHED] 自己包含は、識別対象に観測者自身の状態や出力を含めるため、容量制約や対角化の前提を成立させることがある。しかし、それ単独では不可能性を生まない。

**Excerpt 4**

> 条件付きの容量命題は残る。例えば有限世界 $X=A\times E$ で、識別候補を全初期状態 $\Omega=X$ とし、全ての利用可能な最終記録が真部分系 $A$ に収まらなければならず、$|E|>1$ なら、任意の最終回答 $r:X\to A$ は単射になれない。ただし、候補を小さな部分集合へ制限する、環境自由度を記憶として利用する、外部ログを認める、または無限集合で濃度差が消える場合、この単純な議論は使えない。これは「自己包含定理」ではなく、自己包含に記録場所・候補範囲・有限容量を加えた命題である。

---

## E03 — Generation–log non-isomorphism

**Source path:** `notes/theorem_proof_anatomy_experiment/00_origin/tool_truth_absence_working_note_v0.2.md`, Phase 3

**Excerpt 1**

> **当初の仮説。** 観測ログは生成ダイナミクスのコピーではなく、
>
> $$
> \text{generation}
> \to
> \text{constraint formation}
> \to
> \text{stabilization}
> \to
> \text{log}
> $$
>
> を経るため、生成構造と安定ログ空間の同型は一般に失われるのではないか。

**Excerpt 2**

> **何によって壊れたか。** 「安定化」を多対一写像、「記録」を粗視化として定義すれば、非同型性を定義へ埋め込んでいるだけである。逆に、過程全体が可逆で全情報を保持する場合や、ログが生成状態を完全符号化する場合には同型または単射が可能である。coarse graining、Blackwell comparison、sufficient statistics、bisimulation、minimal realization は、どの情報が保存されるかを既に精密化している。

**Excerpt 3**

> **撤回したもの。** [WITHDRAWN] 生成からログへの段階が存在するだけで、生成構造の非一意性が従うという主張。
>
> **残ったもの。** [ESTABLISHED] 情報損失は仮定ではなく、具体的なチャネル、統計量、力学、同値関係について証明しなければならない。Blackwell 的な「後処理で得られる情報」と物理的に同時実行可能な測定は同じではない。

---

## E04 — Pairwise separation versus a global adaptive separator

**Source path:** `notes/theorem_proof_anatomy_experiment/00_origin/tool_truth_absence_working_note_v0.2.md`, Phase 5

**Excerpt 1**

> **当初の仮説。** 固定候補クラス $\Omega$ について、
>
> $$
> \forall\theta\neq\theta'\;\exists e
> $$
>
> と
>
> $$
> \exists\sigma\;\forall\theta\neq\theta'
> $$
>
> は異なる。各候補対を区別する実験が存在しても、それらを一つの適応的観測履歴へ統合できない系があるのではないか。

**Excerpt 2**

> **具体例。** 候補を二ビット $(a,b)$ とする。操作 $A$ は $a$ を読むが $b$ を破壊し、操作 $B$ は $b$ を読むが $a$ を破壊する。別々の新規コピーなら $(a,b)$ を得られるが、単一コピー上では順序にかかわらず片方を失う。

**Excerpt 3**

> **何によって壊れたか。** この障害は内部観測者に固有ではない。同じ単一コピー、同じ破壊的操作、同じ記憶、同じリセット不能を外部観測者へ課せば、外部でも同じ反例が成立する。また有限状態機械の adaptive distinguishing sequence、active diagnosis、sequential experiment design は、適応的な識別方策の存在を既に扱っている。
>
> 逆に、外部インターフェースが同じ固定 $\theta$ に従う fresh preparation を有限回許すなら、この反例は消える。

**Excerpt 4**

> **撤回したもの。** [WITHDRAWN] 二ビット破壊例を、内部性そのものが生む不可能性の例として使うこと。
>
> **残ったもの。** [ESTABLISHED] ペアごとの実験可能性と単一方策による大域分離の間には量化順序の差がある。[SYNTHESIS] その差を接続するには、「内部性」というラベルではなく、対象モデルに適した逐次合成、記録保存、共通精密化、uniformity、誤差制御などを調べる必要がある。どれが必要十分かは設定ごとに異なる。

---

## E05 — v0.1 to v0.2 internal/external interface correction

**Source path A:** `notes/theorem_proof_anatomy_experiment/00_origin/tool_truth_absence_v0.1_to_v0.2_diff.md`, Major revision map

**Excerpt 1**

> | Phase 7, lines 314–326; §9.1 line 570; Revision status line 642 | 一般的な internal/external interface equivalence が強すぎる | v0.1 の一般 `[ESTABLISHED]` を撤回。完全な履歴能力を同一と定義する規約的同値と、離散時間 turn-based controlled transition system における条件付き実装対応へ分離 | Abstract; Changes / Downgraded; Phase 7; §9; Revision status | accepted |

**Source path B:** `notes/theorem_proof_anatomy_experiment/00_origin/tool_truth_absence_working_note_v0.2.md`, Phase 7

**Excerpt 2**

> **最初の訂正と、その再訂正。** v0.1 は、内部と外部の制御器に同じ入力、出力、記憶容量、コピー数、reset、敵対性、因果インターフェースを与えれば、生成可能な履歴集合は同じになる、と一般的な [ESTABLISHED] 命題として記した。しかし「同じインターフェース」の中に何を含めるかが不十分であり、実際の内部観測者をそのような外部制御器へ還元できるという存在命題と、同じ履歴能力を**定義上**与える規約とが混線していた。この一般形は v0.2 で撤回する。

**Excerpt 3**

> 1. **規約的同値。** timing、concurrency、memory accessibility、memory vulnerability、computational cost、embodiment cost、self-readout、stochasticity、causal channels、reset/copy/fresh preparation、adversarial access を含む完全な実現可能インターフェース $\mathcal I$ を指定し、二つの制御器に許される protocol と transcript の関係を同一と定義すれば、両者の履歴集合は一致する。これは物理的に重要な同値定理というより、行動的インターフェースの同一性をどう定義したかの帰結である。
> 2. **条件付きモデル対応。** 離散時間・turn-based の controlled transition system で、制御器状態が宣言された遷移だけにより更新され、宣言された記憶へのアクセスが保証され、計算遅延と embodiment cost が状態遷移へ明示されているとする。さらに内部実装と外部実装の状態写像が、許容 action、transition、observation を可換に保つなら、履歴長についての帰納法により、一方の方策を他方へ移して同じ transcript 分布を得られる。この主張は指定モデル内の条件付き補題であり、そのような状態写像が現実の観測者について存在することを保証しない。

**Excerpt 4**

> **撤回したもの。** [WITHDRAWN] 一般の内部観測者と外部観測者について、「同一の因果・資源インターフェース」を非形式的に仮定するだけで識別能力同値が証明される、という v0.1 の主張。[WITHDRAWN] `inside vs outside` という空間的位置だけを第一義的数学条件とすること。

---

## E06 — GST Deferred Resolution v0.1 to v0.2

**Source path A:** `notes/theorem_proof_anatomy_experiment/00_origin/deferred_resolution_case_01_gst.md`, §1.1 and §22

**Excerpt 1**

> ケース全体の最適判定は **DR-1 — Weak relocation** である。ただし **Null C（Solved by quotient）** と **Null D/E（historical sequencing / reviewer-imposed narrative）** が全系列の強い読みを制限する。この判定は科学一般の法則を主張しない。

**Source path B:** `notes/theorem_proof_anatomy_experiment/00_origin/deferred_resolution_case_01_gst_v0.1_to_v0.2_diff.md`, §2

**Excerpt 2**

> | Final status | working positive case | frozen negative baseline | frozen |

**Source path C:** `notes/theorem_proof_anatomy_experiment/00_origin/deferred_resolution_case_01_gst_v0.2.md`, opening and §1.1

**Excerpt 3**

> **Status:** Frozen negative result
>
> **Epistemic posture:** field-native reconstruction first; no claim of a new mechanism
>
> **GST系列は、仮説した反復的なDeferred Resolution連鎖を支持しなかった。**

**Excerpt 4**

> - ケース全体を支持結果とした旧判定を撤回した。
> - Deferred Resolution を独立した機構名から、今回棄却された historical working hypothesis へ降格した。
> - frequency、recurrence、formal invariance、diagnostic effect、modal impossibility を一列に並べた旧五段階 taxonomy を削除した。

**Excerpt 5**

> 技術内容は、conditional inverse problem、reference / nuisance uncertainty、joint estimation、identifiability modulo gauge、quotient parameterization、model checking、model-specific extension という既存語彙で、より正確に再構成できる。

---

## E07 — Metrology H1 to M1

**Source path A:** `notes/theorem_proof_anatomy_experiment/00_origin/scientific_assurance_case_02_metrology_preregistration.md`, §4

**Excerpt 1**

> ### H1 — Transfer-loss diagnostic
>
> The relevant information exists in field-native documents, but a generic transfer audit finds at least one path in which upstream scope, uncertainty, assumptions, or reference information is lost or distorted in downstream use, and the field-native control does not find the same issue as clearly or as early.
>
> H1 is supported only if at least one preregistered success condition in §6 survives all applicable falsification conditions in §5.

**Source path B:** `notes/theorem_proof_anatomy_experiment/00_origin/scientific_assurance_case_02_metrology_comparison.md`, §§3 and 14

**Excerpt 2**

> This produced a compact cross-chain display. It did not produce:
>
> - a new missing assumption;
> - a new uncertainty component;
> - a different judgment about a calibration scope;
> - a different conformity decision;
> - a new traceability break;
> - a source absent from the frozen control corpus;
> - a remedy not already present in field-native practice.

**Excerpt 3**

> ### Q5. Did the generic audit change a judgment?
>
> No. It changed presentation and cross-chain visibility only.

**Excerpt 4**

> ### Q7. What is the final M0–M3 classification?
>
> **M1 — Organizational value**, with no demonstrated diagnostic or methodological added value. M0 remains a defensible stricter label; M2 and M3 are rejected by the preregistered criteria.

---

## E08 — Hydrology “preservation” to documentary continuity

**Source path A:** `notes/theorem_proof_anatomy_experiment/00_origin/hydrology_negative_knowledge_preservation_note_v0.1.md`, Current verdict

**Excerpt 1**

> ### **B. Partial preservation history identified**

**Excerpt 2**

> **A を選ばない理由。** (i) 保存機構の**有効性**を示す証拠が、17C→17B の一回の参照を除いてほとんどない（N-04）。(ii) 明示的退役と無言の消滅が同一文書内に併存する（L-01）。(iii) 下流ガイダンス一文書で不確かさ・非定常性の語が消える（L-02）。(iv) 未解決問題は 36 年間解決されないまま残った（L-03）。**保存機構は忘却を防いだが、解決も、下流への完全な伝達も保証していない。**

**Source path B:** `notes/theorem_proof_anatomy_experiment/00_origin/hydrology_negative_knowledge_preservation_note_v0.2.md`, Changes from v0.1 and Current verdict

**Excerpt 3**

> | **C-3** | Current verdict「保存機構は忘却を防いだ」 | **N-04（有効性は未確認）と内部矛盾。** Codex の指摘は正当 | 当該表現を削除（§Verdict） |

**Excerpt 4**

> | v0.1 | v0.2 |
> |---|---|
> | B. Partial preservation history identified | **Documentary continuity identified; preservation effectiveness untested** |

**Excerpt 5**

> **確認できていないこと。** 実際の参照・利用・下流伝達・忘却防止効果は、いずれも測定していない。**文書上の再発見可能性は残ったが、それ以上は言えない。**

---

## E09 — P0 to P1-reduced termination

**Source path A:** `notes/theorem_proof_anatomy_experiment/00_origin/p0_generic_standards_baseline_v0.1.md`, §§5–6

**Excerpt 1**

> **14 コード中、比較研究の対象として生き残るのは実質 1 コード（`NONEVAL`）、保留が 1 コード（`RET-DOWN`）である。**

**Excerpt 2**

> | **(i) 縮小継続** | `NONEVAL` のみを対象に、GUM/VIM と GRADE handbook を検索する。「評価していない」に相当する定型表現が存在するかを見る | 小（検索のみ） | **推奨** |
> | (ii) `RET-DOWN` の検査 | L2+L3 を持つ generic 系列（例：ISO 規格＋それを引用する national regulation）を 1 組取得 | 中 | 次点 |
> | (iii) 設計どおり P1–P5 | 三分野の完全な artifact chain 復元 | 大 | **非推奨。** 対象が 1 コードでは正当化できない |
> | (iv) 終了 | comparative review へ降格して終了 | ゼロ | 許容範囲 |

**Excerpt 3**

> **(iii) を採らないことを明記する。** 設計文書は三分野の完全比較を計画したが、P0 の結果はその計画の前提（比較すべきコードが十分にある）を否定した。**設計どおりに進めることが、設計の目的に反する場合がある。**

**Source path B:** `notes/theorem_proof_anatomy_experiment/00_origin/p1r_noneval_two_field_check_v0.1.md`, §§6 and 9

**Excerpt 4**

> | **P1-reduced 後** | **D 相当。terminate as comparative methodology; downgrade to comparative review** |

**Excerpt 5**

> **比較方法論としては終了する。** 設計文書 Part IX の規定に従う。

**Excerpt 6**

> **設計文書 Part VIII の P1–P5(三分野の完全な artifact chain 復元)には進まない。** P0 と本検査により、その計画の前提は二段階にわたって否定された。

---

## E10 — Gödel “closure reversal” to C1

**Source path:** `notes/theorem_proof_anatomy_experiment/01_theorem_anatomy/godel_incompleteness_closure_reversal_stress_test_ja.md`, §§0, 1, 7–8

**Excerpt 1**

> 本稿は theorem_proof_anatomy_v1.1_ja.md の分析枠を、Gödel の第1・第2不完全性定理へ試験適用する。ここでいう「逃走経路」「閉じ方」「封鎖」「残差」「閉包」「閉包反転」は比較のためのメタ記述であって、標準数理論理学・証明論の用語ではない。

**Excerpt 2**

> \(T\) を、Robinson arithmetic \(Q\) を含む、計算可能に公理化された古典一階理論とする。\(T\) が整合的なら、ある算術文 \(R_T\) が存在し、\(T\nvdash R_T\) かつ \(T\nvdash\neg R_T\) である。

**Excerpt 3**

> 第2定理の結論は、外部の整合性仮定から内部文の **非証明可能性** を導くメタ定理である。

**Excerpt 4**

> **C1 — 説明比喩としてのみ有効**
>
> 「閉包反転」は、既存21定理との比較において、条件が positive closure を作る場合と、条件が effective closure の限界を可視化する場合を対照させる短いラベルとしては働く。しかし、証明論的に独立した新分類を与えず、標準概念より診断解像度が低い。従って C2・C3 へは上げない。

**Excerpt 5**

> negative result として重要なのは、Gödel が「閉包反転」の実例だと証明されたのではなく、**閉包語彙は Gödel の機構を発見・区別する道具にはならず、標準的分析後の比較要約にのみ使える**と分かったことである。

---

## E11 — Reflection S2 to S2*

**Source path:** `notes/theorem_proof_anatomy_experiment/01_theorem_anatomy/reflection_principles_scope_stress_test_ja.md`, §§0, 2–3, 11, 21

**Excerpt 1**

> 今回の中心仮説は、「自己保証」が single local reflection では比較ラベルとして働いても、uniform / global reflection や semantic soundness まで含めると型とレベルの差を隠すのではないか、である。S2 を維持するのでなく、積極的に kill test する。

**Excerpt 2**

> formula class \(\Gamma\) は \(T\) の「性質」ではなく、どの reflection instances を追加するかという scope definition である。

**Excerpt 3**

> reflection principle を外部から \(T\) へ追加して
>
> \[
> T^+=T+\mathrm{Rfn}_\Gamma(T),
> \quad
> T^+=T+\mathrm{RFN}_\Gamma(T),
> \quad\text{or}\quad
> T^+=T+\mathrm{GRP}(T)
> \]
>
> のような stronger theory を構成し、\(T\)-provability から対象文・全数 instance・truth への橋を新しい axioms として与える。得られる strength、conservation、consistency strength は scope、\(\Gamma\)、base、truth axioms に依存し、単一の結論 \(P\) には還元できない。

**Excerpt 4**

> Löb は reflection principle の追加を禁止しない。「同じ \(T\) が自分に関する reflection を theorem にする」場合の collapse を述べる。reflection theory は、外部から旧理論 \(T\) を対象化して stronger theory を作る。この subject shift がなければ progression 全体を誤読する。

**Excerpt 5**

> **S2\* — 限定的S2。** local reflection では有効だが、uniform / global / soundness まで広げると型・言語・メタレベルの差を隠して破綻する。

---

## E12 — Proof-theoretic ordinal scalar to fixed-package calibration

**Source path:** `notes/theorem_proof_anatomy_experiment/01_theorem_anatomy/proof_theoretic_ordinal_stress_test_ja.md`, opening and §§16–18, 25

**Excerpt 1**

> 中心結論を先に述べる。**proof-theoretic ordinal は、比較方法を固定した自然な理論群に対しては強力でしばしば頑健な一次元 calibration だが、理論の全 strength を表す万能スカラーではない。** 「|T|=\alpha」は、少なくとも notation、base/metatheory、formula class、reduction notion を省略した略記である。

**Excerpt 2**

> \[
> |T|=|U|
> \]
>
> から、一般には次のいずれも自動ではない。
>
> - same theorem set
> - mutual interpretability
> - same consistency strength
> - same \(\Pi_1\)-consequences
> - same induction schemas
> - same reflection rank
>
> 従うのは、まず「採用した ordinal calibration が \(T,U\) を同じ座標へ写した」ことだけである。追加結論には、その calibration と theorem inclusion、conservation、interpretability 等を結ぶ定理が要る。

**Excerpt 3**

> **判定: S2\*.**
>
> 自然な理論群と標準 analysis package では、cut elimination、TI/WO、reflection、worm ordering が橋渡し定理により同じ ordinalへ収束し、ordinal は複数の標準 notions を統合する頑健な一次元 coordinate になる。だが任意の理論、任意の formula class、任意の interpretability/conservation notionを一つにする universal scalar ではない。単独の characterization 内だけなら S1、PA のような収束例まで含めて限定的 S2 と評価する。

**Excerpt 4**

> **判定: A2。**
>
> analyzed theory \(T\)、その proof を符号化する calculus、ordinal notation、reduction theorem、notation の well-foundedness を証明する metatheory は型が異なる。これは Turing–Feferman progression の subject/extension reindexing と同一ではないが、「評価される理論」と「評価を正当化する理論」の区別として ordinal-analysis 全般に安定する architecture feature である。標準 metamathematical level distinction で十分なので A3 ではない。

---

## Freeze rule

episodeの追加・削除、excerpt差替え、順序変更はinter-reader test開始後に行わない。誤引用またはpath errorが見つかった場合はtestを止め、訂正履歴を別途残して全readerへ同じ版を再配布する。難易度、ambiguity flag、期待code、answer keyは本ファイルへ追記しない。
