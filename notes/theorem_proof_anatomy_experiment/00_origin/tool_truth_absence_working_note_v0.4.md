# 道具的成功の存在論的非自己証明性

## 科学的成功を支える保証の分散構造と、その背景化・受け渡し

- **旧作業名:** 「道具の真理不在性」
- **English title:** *Ontological Non-Self-Certification of Instrumental Success: Distributed Assurance, Backgrounding, and Cross-Domain Handoffs in Scientific Inference*
- **Status:** working note / conservative and corrigible synthesis / not a theorem announcement
- **Version:** 0.4
- **Date:** 2026-08-16
- **Relation to VED:** independent methodological note; not evidence for VED
- **Structural caution:** 「前提スタック」「前提ネットワーク」は v0.1–v0.2 の歴史的語彙である。v0.4 は、v0.3 の中心像である、異種の保証経路、その出所、背景化、分野間 handoff を追う **assurance network / guarantee-provenance map** を変更しない。

---

## 1. Abstract

本ノートは、観測・予測の成功と生成構造の一意的同定との関係をめぐる検討を、成功した理論ではなく、失敗・撤回・問題分解の履歴として保存する。当初探した普遍的不可能定理は得られなかった。非単射性は inverse problems と identifiability の初等的核であり、自己包含だけから非識別可能性は導けず、生成―ログ非同型も情報損失を定義へ埋め込めば循環する。極小実現や有限オートマトンには振る舞いから同型を除く一意性が回復するクラスもある。

v0.2 は失敗後に現れた条件群を Scientific Identifiability Prerequisite Network として整理した。量子論へのケース適用と、量子情報・測定・Bell 基礎論・統計・科学哲学の prior-art reconstruction は、この整理をさらに限定した。tomography–calibration–estimation、Bell experiment–finite statistics–causal assumptions、contextuality–operational equivalence–model exclusion などの局所構造は、既存研究の語彙と定理の方が一般監査語彙より精密である。量子ケースは既存科学の missing structure を示さず、**Type B — existing nodes, weak cross-domain edges, with a strong Type A component** と評価された。

そこで v0.3 は、中心像を「必要条件のノード列」から、科学的結論を支える異種の保証経路へ移した。v0.4 はこの中心像を維持する。定理、モデル仮定、装置設計、校正、統計的制約、独立な経験的 cross-check、因果仮定、model-class restriction、解釈上の追加推論は、同じ種類の保証ではない。本ノートでは、それらがどこから来て、どの結論へ渡され、どの分野で合理的に背景化されるかを追う作業を **assurance provenance（保証の出所／保証来歴）** と呼ぶ。ただし、これは新しい形式理論ではなく、assurance case、metrological traceability、evidence graph 等との体系的比較も未完である。

残る最小限の立場は保守的である。道具的・予測的成功それ自体は、その成功を支える全ての保証経路と、それらを唯一の存在論へ接続する追加原理を同時には自己証明しない。しかし多くの保証経路は、target success とは別の校正、設計、統計、再現、介入、理論によって非常に強く支持されうる。v0.4 の候補価値は indexing、cross-domain visualization、provenance・cross-impact・backgrounding・handoff の追跡にあり、方法論的診断力は real handoff audit で field-native control と異なる判断を示すまで未実証である。GST Case 01 の negative result は、新しい機構ではなく、一般語彙を残すための棄却基準を厳しくした。

---

## Changes from v0.3

### Added

- **GST Case 01 as a frozen negative calibration result:** 反復的な Deferred Resolution / boundary-relocation 仮説が field-native reconstruction に対して独立の診断効果を示さなかった事例を、自己反証履歴として追加した。
- **Explicit Erasure Test failure:** 固有語彙を消しても technical distinction、scope judgment、diagnostic decision が保存され、部分的には記述精度が上がった実例を記録した。
- **Control-reconstruction requirement:** generic audit vocabulary に方法論的価値を認める前に、field-native terminology だけによる control と比較し、diagnosis、decision、scope judgment、または retrieval result の具体的差を要求する。

### Preserved

- assurance provenance、backgrounding、handoff、cross-impact を追う v0.3 の中心像。
- field-native terminology first。
- organizational usefulness は plausible、methodological usefulness は unproven という評価。
- 真理の存在についての中立性、Phase 0–9 の撤回履歴、VED からの独立性。

### Not adopted

- Deferred Resolution を独立した方法論概念とすること。
- boundary relocation を assurance network の新しい中心 edge とすること。
- frequency、recurrence、formal invariance、diagnostic effect、modal impossibility を混在させた DR taxonomy。

本改訂は新しい理論内容を追加するものではない。一般語彙候補が Erasure Test に失敗した一件を correction trail に固定する minor correction revision である。

---

## Historical changes from v0.2

### Downgraded

- **Prerequisite network の独自性:** 既存の局所理論を置換する中心構造から、既存の保証関係を横断表示する歴史的・比較的な図へ降格した。
- **CIF / EA の一般性:** CIF は Bell 外の制御系を比較する generic audit label、EA は複数の既存合成概念を比較する umbrella に限定した。いずれも field-native theorem object より上位に置かない。
- **Candidate-class adequacy:** misspecification、dimension/leakage、M-open、unconceived alternatives、causal-model adequacy を横断参照する索引語へ降格した。
- **Methodological usefulness:** 「ケースで弱い usefulness を示した」から、**organizational usefulness is plausible; methodological usefulness remains unproven** へさらに限定した。
- **Missing-edge interpretation:** 量子 prior-art reconstruction では genuine missing edge を確認していない。弱い接続と literature-audit 不足を分ける。

### Reframed

- **Prerequisite → assurance provenance:** 条件を事前に積む図から、結論を支える保証の種類・出所・受け渡しを追う図へ中心像を移した。
- **Node → edge / support relation:** 何が存在するかだけでなく、theorem、設計、校正、統計、因果、解釈のどの関係が結論を支えるかを優先する。
- **Hidden assumption → backgrounded / stabilized interface:** 分野内で所与とされる条件を直ちに隠蔽や欠陥と呼ばず、別分野・装置・標準手続への合理的委譲として扱う。
- **One-node failure → cross-cutting failure:** drift、SPAM、selection 等が複数の保証 edge を同時に壊す作用を保存する。gauge はノイズと同一視しない。

### Added

- **Assurance provenance:** theorem-relative、design-supported、calibration-supported、statistically constrained、empirically cross-checked、model-relative、interpretive/theory-choice dependent という非排他的な出所分類。
- **Backgrounding and stabilized interfaces:** ある分野が、他の実践で安定化された条件を所与とする構造。
- **Cross-domain handoff:** upstream の条件付き結論が downstream で何を背景化したまま入力になるかを追う表示。
- **Cross-impact tracking:** 一つの failure mode が複数 edge に与える影響。
- **Erasure Test:** 固有語彙を消して既存文献だけで内容と判断が再現できるなら、追加価値を presentation / indexing に限定する反証基準。
- **Type A–D case classification:** 量子ケースを Type B、ただし強い Type A 成分を持つ事例として記録した。

### Preserved

- Phase 0–9 の失敗・撤回・次の問いの chronology。
- 「道具的成功の存在論的非自己証明性」という限定的な監査上の立場。
- 真理の存在・不存在について中立であること。
- `ESTABLISHED / SYNTHESIS / HYPOTHESIS / WITHDRAWN / OPEN` の状態管理。
- VED からの独立性と、任意理論への対称適用。
- きれいな最終理論より correction trail を優先する方針。

### Evidence and review handling

改訂根拠は、量子ケース、量子 prior-art reconstruction、Case Study 01 に対する Claude Code 敵対的査読、v0.1→v0.2 差分記録である。査読は権威ではなく検索・反証入力として用いた。

- **Accepted:** Bell の PI/OI 分解不足、memory / coincidence-time loophole 不足、指定有限次元状態モデルでの informational completeness が ideal state identifiability の必要十分条件になること、i.i.d. が全 tomography 手法に必須ではないこと、usefulness 判定に既存研究との head-to-head comparison が不足していたこと。
- **Partially accepted:** Bell 文脈での CIF redundancy。Bell では field-native vocabulary の方が精密だが、Bell 外の generic label まで同一とは確定しない。
- **Rejected:** failure mode の排他的 one-primary-node 配属、GPT での broadcastability / incompatibility の無条件な単純同値、Bell の “La nouvelle cuisine” を1976年とする書誌情報。主要処理は `tool_truth_absence_v0.2_to_v0.3_diff.md` に記録する。

---

## 2. Scope and terminology

### 2.1 旧作業名「真理不在性」の限定

本ノートにおける「真理不在性」は、**真理そのものが存在しない**という主張ではない。また、**観測や予測から生成構造へ原理的に到達できない**という普遍的不可能性でもない。

暫定的には、次の監査上の主張だけを指す。

> 道具的・予測的成功それ自体は、その成功を支えているすべての保証経路の正当性と、それらを唯一の存在論へ接続する追加原理を、同時には自己証明しない。

この限定には、必ず次を対にする。

> 多くの保証経路は、target success とは独立の校正、設計、統計、再現、介入、理論によって非常に強く支持されうる。「成功だけから自己証明されない」ことは、「根拠がない」ことを意味しない。

したがって旧称の「不在」とは、対象世界からの真理の欠落でも、世界像の必然的非一意性でも、観測の本質的不完全性でもない。**道具的成功に、全ての保証と解釈原理を一括して自己証明する能力がない**という限定的な意味である。v0.4 でも「道具の真理不在性」は失敗履歴を保存する旧作業名としてのみ残す。

この定義自体も [SYNTHESIS] であり、以後の反例や先行研究によって修正されうる。

### 2.2 「道具」の範囲

ここでいう道具は、物理的測定装置だけを意味しない。少なくとも次を含む。

- 実験装置と操作プロトコル
- 統計モデル、シミュレータ、予測器
- 記録媒体とデータ処理系
- モデル選択基準、極小性規準、正則化
- 計算資源、乱数源、再準備・リセット手順

したがって問題は「装置が世界を正しく写すか」だけではなく、どの実験・記録・推論インターフェースを通して候補構造を比較しているかである。

### 2.3 候補クラスと存在論的差異

候補集合を方策選択前に固定し、再ラベル付け、ゲージ変換、または採用する構造同型をあらかじめ商で除く。

$$
\Omega=\Theta/{\cong}.
$$

以下で「異なる生成構造」と呼ぶのは、固定された $\cong$ に関して異なる元である。$\cong$ を指定しなければ、同型な再記述を別存在論として数える自明化と、観測同値で全てを商にして一意性を定義的に得る自明化の両方が起こる。

ただし、候補クラスを固定することと、真の生成構造がその中に含まれることは別である。仮に真の生成構造を $\theta_\star$ と書けるとしても、

$$
\theta_\star\in\Omega
$$

は識別アルゴリズムから従う結論ではなく、model-class adequacy または realizability の仮定である。$\Omega$ 内で一意に識別できることを **within-model identifiability**、$\Omega$ が対象生成過程を適切に表現しているかを **model-class adequacy** と呼んで区別する。後者が失敗すれば、$\Omega$ 内の一意解は「候補中の最良または一意な近似」であって、存在論的一意性ではない。

Bayesian model comparison の M-closed/M-open、statistical misspecification、dimension/leakage diagnosis、causal-model adequacy、Stanford の unconceived alternatives には、それぞれこの問題の一部を扱う field-native vocabulary がある。v0.4 の **candidate-class adequacy** は、それらを置換する新概念ではなく、異なる adequacy problems を横断参照するための索引語に限る。完全対応は `[OPEN: literature audit]` とする。

### 2.4 主張状態タグ

- **[ESTABLISHED]** 既存数学または明示的反例によって比較的強く支持される。
- **[SYNTHESIS]** 既存結果を本ノートの問いの下で並べ直した解釈。
- **[HYPOTHESIS]** 追加検討を要する作業仮説。
- **[WITHDRAWN]** 本検討で撤回した主張。
- **[OPEN]** 現時点で未解決または文献監査が不十分な問い。

### 2.5 Field-native terminology first

個別分野を記述するときは、その分野で定義・検証されている語彙を先に使う。例えば Bell 実験では parameter independence、outcome independence、measurement independence、detection loophole、memory loophole、coincidence-time loophole を用い、これらを CIF や generic independence の一語で置換しない。量子測定では joint measurability、nondisturbance、instrument、supplied copies、collective access を優先し、EA は比較用 umbrella としてのみ後から使う。

一般監査語彙の役割は、異分野間の類似、差異、handoff を索引化することである。field-native theorem の仮定・形式対象・射程を粗くする場合は、一般語彙を使わない。

---

## 3. Initial question

### Phase 0：出発点

**当初の仮説。** 観測・予測が継続的に成功するとき、その成功から世界の生成構造または存在論的一意性まで進めるのか、それとも両者の間には一般的な断絶があるのか。

**なぜ魅力的に見えたか。** 量子論における複数解釈、観測者問題、経験的に同等な理論記述、科学的道具の高い予測性能が、同じ問いの異なる表現に見えたためである。

**何によって限定されたか。** 「予測が当たる」「パラメータが識別できる」「振る舞い同値類が一意である」「生成子が同型を除き一意である」「一つの存在論的解釈が支持される」は別々の命題である。これらを一つの矢印にまとめると、統計・制御・計算・哲学の異なる問題を混同する。

**撤回したもの。** [WITHDRAWN] 量子解釈や観測者問題の存在だけを、一般的不可能定理の根拠にすること。

**残ったもの。** [OPEN] 予測成功から生成構造の同定へ進む各段階で、どの補助仮定が使われるかを分解する問い。

**次の問い。** まず観測を写像として最小化したとき、何が数学的に言えるか。

本ノートは特定の量子解釈の正否を論じない。また VED の正否をこの問題から導かない。

---

## 4. Sequence of failed conjectures

### Phase 1：観測写像の非単射性

**当初の仮説。** 候補世界集合 $W$、ログ空間 $L$、観測写像

$$
O:W\to L
$$

について、

$$
O(w_1)=O(w_2),\qquad w_1\neq w_2
$$

ならば、ログから世界を一意に復元できない。この構造を「観測写像の存在論的非一意性定理」として一般化できるのではないか。

**なぜ魅力的に見えたか。** 観測ログと生成世界の区別を、哲学的修辞を使わず最小の数式で表現できたためである。またファイバー

$$
O^{-1}(l)
$$

が複数候補を含むことは、観測成功と構造的一意性の差を可視化した。

**何によって壊れたか。** これは inverse problems、identifiability、observational equivalence、quotient/fiber の基本設定そのものである。非単射写像に左逆がないこと以上の内容は、$O$ が非単射でなければならない条件を別途示さない限り得られない。また $O=\mathrm{id}_W$ は即座の反例である。

**撤回したもの。** [WITHDRAWN] 「観測写像の存在論的非一意性」を新しい一般定理として主張すること。

**残ったもの。** [ESTABLISHED] 観測同値類と採用した構造同型類は区別しなければならない。識別可能性はモデルクラスと実験族に相対的である。

**次の問い。** 観測者が世界の内部にあることは、$O$ の非単射性を強制する追加条件になるか。

### Phase 2：内部観測の非包括性

**当初の仮説。** 観測者が世界内部の物理過程なら、観測は静的写像ではなく

$$
W_t\xrightarrow{\mathcal O_A}(W_{t+1},l)
$$

と書くべきであり、自己を含む世界の完全記述は一般に不可能ではないか。

**なぜ魅力的に見えたか。** 観測反作用、有限記憶、自己言及、記述生成過程自身の内部化を同時に扱えるように見えた。また外部の無限能力観測者を暗黙に置く通常の逆問題より強い制約が期待された。

**何によって壊れたか。** 自己包含だけでは非単射性は導けない。有限候補 $\Omega$ と十分大きな内部記憶 $M$ に対し、閉じた系

$$
X=\Omega\times M,
\qquad
(\theta,m_0)\mapsto(\theta,\operatorname{enc}(\theta))
$$

を作れば、内部観測者は候補を一意に記録できる。無限集合では真部分集合と全体が同じ濃度を持ちうる。さらに自己出力プログラム（quine）や Kleene の再帰定理は、適切な計算モデルでは自己記述が可能であることを示す。Breuer の自己測定制約や Wolpert の inference-device 不可能性には、真部分系への制限、全状態の識別要求、固定された出力意味論、自己問合せ閉包など追加条件がある。ここでの quine はプログラムを指し、Duhem–Quine の Quine とは区別する。

**撤回したもの。** [WITHDRAWN]

$$
\text{self-containment}
\Rightarrow
\text{universal non-identifiability}.
$$

**残ったもの。** [ESTABLISHED] 自己包含は、識別対象に観測者自身の状態や出力を含めるため、容量制約や対角化の前提を成立させることがある。しかし、それ単独では不可能性を生まない。

条件付きの容量命題は残る。例えば有限世界 $X=A\times E$ で、識別候補を全初期状態 $\Omega=X$ とし、全ての利用可能な最終記録が真部分系 $A$ に収まらなければならず、$|E|>1$ なら、任意の最終回答 $r:X\to A$ は単射になれない。ただし、候補を小さな部分集合へ制限する、環境自由度を記憶として利用する、外部ログを認める、または無限集合で濃度差が消える場合、この単純な議論は使えない。これは「自己包含定理」ではなく、自己包含に記録場所・候補範囲・有限容量を加えた命題である。

**次の問い。** 観測者の位置ではなく、生成過程からログへの変換そのものが情報を失うのではないか。

### Phase 3：生成―ログ非同型

**当初の仮説。** 観測ログは生成ダイナミクスのコピーではなく、

$$
\text{generation}
\to
\text{constraint formation}
\to
\text{stabilization}
\to
\text{log}
$$

を経るため、生成構造と安定ログ空間の同型は一般に失われるのではないか。

**なぜ魅力的に見えたか。** 実際の測定には緩和、閾値化、粗視化、記録媒体への転写があり、生の微視的過程と安定記録は異なる。生成とログの区別は経験的にも自然に見えた。

**何によって壊れたか。** 「安定化」を多対一写像、「記録」を粗視化として定義すれば、非同型性を定義へ埋め込んでいるだけである。逆に、過程全体が可逆で全情報を保持する場合や、ログが生成状態を完全符号化する場合には同型または単射が可能である。coarse graining、Blackwell comparison、sufficient statistics、bisimulation、minimal realization は、どの情報が保存されるかを既に精密化している。

**撤回したもの。** [WITHDRAWN] 生成からログへの段階が存在するだけで、生成構造の非一意性が従うという主張。

**残ったもの。** [ESTABLISHED] 情報損失は仮定ではなく、具体的なチャネル、統計量、力学、同値関係について証明しなければならない。Blackwell 的な「後処理で得られる情報」と物理的に同時実行可能な測定は同じではない。

**次の問い。** 観測資源を増加させたとき、非識別ファイバーが縮小・消滅する境界を記述できるか。

### Phase 4：資源階層と極限ファイバー

**当初の仮説。** 内部観測資源を

$$
r=(T,M,B,\varepsilon^{-1},\Omega_{\mathrm{obs}},\mathcal I)
$$

のように置き、資源 $r$ で得られる実験署名を

$$
E_r:\Theta\to Z_r
$$

とする。ファイバー

$$
F_r(\theta)=\{\theta':E_r(\theta')=E_r(\theta)\},
\qquad
F_\infty(\theta)=\bigcap_rF_r(\theta)
$$

を用いれば、資源を増やしても残る「存在論的ファイバー」の一般理論が得られるのではないか。

**なぜ魅力的に見えたか。** 有限観測と理想的完全観測を区別でき、時間、記憶、精度、帯域、介入能力を一つの順序にまとめられる。また「有限には不明だが極限では識別可能」と「極限でも非識別」を分離できる。

**何によって壊れたか。** 有限候補では、全実験族が候補を分離し各ペアに有限実験があれば、有限個の実験選択で分離できることがある。無限候補では、各有限段階のファイバーが非自明でも、その下降列が一点へ収束しうる。逆に極限でも残るファイバーは、モデルクラス、位相、許容実験、ノイズ、計算可能性に依存する。finite model theory、automata theory、realization theory、algebraic statistics、HMM identifiability、bisimulation、learning in the limit、resource-bounded indistinguishability が既に多様な境界を扱っている。

**撤回したもの。** [WITHDRAWN] 資源増大に対して残るファイバーについて、生成クラス非依存の一般定理があるという期待。

**残ったもの。** [ESTABLISHED] 資源順序に沿うファイバーの変化は有用な記法であるが、それ自体は定理ではない。有限／無限、exact／generic／asymptotic、one-shot／limit identification を区別する必要がある。

**次の問い。** 全ての反実験を別々に考えれば分離できることと、一つの実際の履歴で分離できることは同じか。

### Phase 5：全反実験族と単一履歴の差

**当初の仮説。** 固定候補クラス $\Omega$ について、

$$
\forall\theta\neq\theta'\;\exists e
$$

と

$$
\exists\sigma\;\forall\theta\neq\theta'
$$

は異なる。各候補対を区別する実験が存在しても、それらを一つの適応的観測履歴へ統合できない系があるのではないか。

**なぜ魅力的に見えたか。** これは単なる静的非単射性を超え、実験が対象を更新・破壊すること、行動可能性が履歴に依存すること、方策が一つの現実履歴しか通れないことを表せる。

**具体例。** 候補を二ビット $(a,b)$ とする。操作 $A$ は $a$ を読むが $b$ を破壊し、操作 $B$ は $b$ を読むが $a$ を破壊する。別々の新規コピーなら $(a,b)$ を得られるが、単一コピー上では順序にかかわらず片方を失う。

**何によって壊れたか。** この障害は内部観測者に固有ではない。同じ単一コピー、同じ破壊的操作、同じ記憶、同じリセット不能を外部観測者へ課せば、外部でも同じ反例が成立する。また有限状態機械の adaptive distinguishing sequence、active diagnosis、sequential experiment design は、適応的な識別方策の存在を既に扱っている。

逆に、外部インターフェースが同じ固定 $\theta$ に従う fresh preparation を有限回許すなら、この反例は消える。より一般に、各ペア $\theta\neq\theta'$ に対する実験 $e_{\theta,\theta'}$ の可能結果集合が

$$
R_e(\theta)\cap R_e(\theta')=\varnothing
$$

を満たし、外部インターフェースがそれらの積実験を実行できるなら、敵対的環境が各座標の許容結果を相関させても大域分離できる。任意の候補対に対応する一座標で結果集合が非交差だからである。ただし adversary が試行間で実際の $\theta$ を変更できるなら、それは同一生成構造の識別問題ではない。この外部側の成功は外部性ではなく、fresh preparation と product closure による。

ここで $R_e(\theta)\cap R_e(\theta')=\varnothing$ は zero-error separation の強い条件である。確率分布の support が重なる場合は、この有限積の議論をそのまま使えず、誤り確率、反復スケジュール、漸近分離、相互特異性などを §6.1 の Hellinger/absolute-continuity の行および §7.2 の statistical separation で別に扱う。

**撤回したもの。** [WITHDRAWN] 二ビット破壊例を、内部性そのものが生む不可能性の例として使うこと。

**残ったもの。** [ESTABLISHED] ペアごとの実験可能性と単一方策による大域分離の間には量化順序の差がある。[SYNTHESIS] その差を接続するには、「内部性」というラベルではなく、対象モデルに適した逐次合成、記録保存、共通精密化、uniformity、誤差制御などを調べる必要がある。どれが必要十分かは設定ごとに異なる。

**次の問い。** 個別実験を一つの実現可能実験へまとめるための部分合成・共通精密化条件は何か。

### Phase 6：experimental amalgamation / common refinement

**当初の仮説。** 実験を集合ではなく、履歴依存で部分的にしか合成できない構造として扱い、pairwise separation から global adaptive separator が存在する境界を、amalgamation 条件として特徴づけられるのではないか。

**なぜ魅力的に見えたか。** 候補依存で実行可能操作が異なる場合、実験は全域的関数ではない。また操作後の状態変化により、$e_1$ と $e_2$ が個別に可能でも $e_2\circ e_1$ が未定義になりうる。これは静的な観測写像では見えない。

**得られた区別。** [SYNTHESIS]

- **Domain obstruction:** 局所候補集合では実行可能な分離実験が、固定した全候補集合では安全に実行できない。
- **Interference obstruction:** $A$ と $B$ は個別に可能だが、一方の実行が他方の実行可能性または情報を破壊する。
- **Globalization:** 局所的に定義された実験を全候補に共通の実験へ延長できるか。
- **Amalgamation:** 複数実験の識別情報を保存する、単一履歴実現可能な共通精密化が存在するか。

内生的な操作可能性を候補選択へ密輸入しないため、方策集合も固定候補クラスに対して定義する。履歴 $h$ と両立する候補 $\theta$ の可能状態集合を $C_\theta(h)$、状態 $x$ で許容される操作を $U_\theta(x)$ とすれば、方策 $\sigma$ は各到達可能履歴で

$$
\sigma(h)\in
\bigcap_{\substack{\theta\in\Omega\\x\in C_\theta(h)}}
U_\theta(x)
$$

を満たすものに限る。操作不能自体が観測情報なら、候補ごとに操作を方策集合から消すのではなく、失敗結果 $\bot$ を返す全域操作としてモデル化する。これにより、pairwise separator も global separator も、方策選択前に固定された同じ方策空間の元になる。

決定論的実験 $e:\Omega\to Z_e$ に対し、

$$
e\preceq f
\quad\Longleftrightarrow\quad
\exists d\; e=d\circ f
$$

と置く。有限候補で選んだペア分離実験族 $\{e_i\}$ の結合署名

$$
J(\theta)=(e_i(\theta))_i
$$

は単射である。単一履歴実験 $H_\sigma$ と後処理 $d$ が

$$
J=d\circ H_\sigma
$$

を満たすことは、$H_\sigma$ が大域分離器であることと同値になる。この意味では、共通精密化の存在が正確な必要十分条件である。これは Blackwell refinement の決定論的退化に近い **informational refinement** の主張である。

ここで少なくとも六概念を区別する。

1. **Informational refinement:** $f$ の結果から後処理で $e$ の結果を復元できる。
2. **Blackwell refinement:** 確率実験間で、一方が他方の Markov kernel による garbling として得られる。
3. **Physical joint realizability:** 複数操作を同じ物理試料または同じ run で共同実行できる。
4. **Sequential composability:** 前の操作後にも、次の操作が宣言された状態更新の下で実行できる。
5. **Product experiment:** fresh preparation や複数コピー上の結果を結合できる。
6. **Adaptive global separator:** 観測履歴に応じて操作を選び、全候補を一方策で分離できる。

$J=d\circ H_\sigma$ が直接述べるのは第一項だけである。$H_\sigma$ が候補を同定した後、各 pairwise 実験の結果を計算上再構成できることは、pairwise 実験が同一試料で物理的に共同実行されたことを意味しない。第三項から第六項には、状態更新、利用可能操作、コピー、reset、誤差、計算可能性を含む追加モデルが必要である。

**何によって限定されたか。** この同値は、固定有限候補、決定論的結果、任意の後処理を許すという条件では初等的であり、新定理ではない。確率実験では Blackwell kernel、敵対的非決定性では結果集合またはゲーム意味論、物理的共同実行では状態更新を含む別の精密化概念が必要である。無限候補または確率的履歴で pairwise separation から global/asymptotic separation へ進むには、uniformity、measurability、convergence schedule、summable error、almost-sure と zero-error の区別、計算資源などが追加で必要になりうる。

**撤回したもの。** [WITHDRAWN] informational refinement と physical joint realizability を同一視すること。候補を一意に同定した後で各実験結果を計算上再構成できても、同じ試料上で複数実験を物理的に共同実行できたことにはならない。

**残ったもの。** [SYNTHESIS] 内生的実験集合を部分圏、partial algebra、game arena などとして記述し、reset、fresh preparation、nondemolition、記録追記、安全継続が有限共通精密化または単一履歴実現可能性を保証する条件を比較する問題。

**次の問い。** この合成障害は内部／外部という位置関係から出るのか、それとも両者のインターフェース差から出るのか。

### Phase 7：内部／外部インターフェース同値仮説の再訂正

**当初の仮説。** 内部観測者には、外部観測者にはない固有の識別限界があるのではないか。

**なぜ魅力的に見えたか。** 内部観測者は対象と同じ状態空間に含まれ、測定反作用、有限記憶、自己言及、初期相関に曝されるためである。

**最初の訂正と、その再訂正。** v0.1 は、内部と外部の制御器に同じ入力、出力、記憶容量、コピー数、reset、敵対性、因果インターフェースを与えれば、生成可能な履歴集合は同じになる、と一般的な [ESTABLISHED] 命題として記した。しかし「同じインターフェース」の中に何を含めるかが不十分であり、実際の内部観測者をそのような外部制御器へ還元できるという存在命題と、同じ履歴能力を**定義上**与える規約とが混線していた。この一般形は v0.2 で撤回する。

ここでは二段階に分ける。

1. **規約的同値。** timing、concurrency、memory accessibility、memory vulnerability、computational cost、embodiment cost、self-readout、stochasticity、causal channels、reset/copy/fresh preparation、adversarial access を含む完全な実現可能インターフェース $\mathcal I$ を指定し、二つの制御器に許される protocol と transcript の関係を同一と定義すれば、両者の履歴集合は一致する。これは物理的に重要な同値定理というより、行動的インターフェースの同一性をどう定義したかの帰結である。
2. **条件付きモデル対応。** 離散時間・turn-based の controlled transition system で、制御器状態が宣言された遷移だけにより更新され、宣言された記憶へのアクセスが保証され、計算遅延と embodiment cost が状態遷移へ明示されているとする。さらに内部実装と外部実装の状態写像が、許容 action、transition、observation を可換に保つなら、履歴長についての帰納法により、一方の方策を他方へ移して同じ transcript 分布を得られる。この主張は指定モデル内の条件付き補題であり、そのような状態写像が現実の観測者について存在することを保証しない。

**撤回したもの。** [WITHDRAWN] 一般の内部観測者と外部観測者について、「同一の因果・資源インターフェース」を非形式的に仮定するだけで識別能力同値が証明される、という v0.1 の主張。[WITHDRAWN] `inside vs outside` という空間的位置だけを第一義的数学条件とすること。

**残ったもの。** [ESTABLISHED] `inside/outside` というラベル**だけ**から識別能力差は導けない。差を主張するには、timing、記憶の脆弱性、自己読出し、計算・身体化コスト、fresh preparation、遮蔽された乱数、reset、操作可能範囲など、追加のモデル差を特定しなければならない。同じ単一コピー・破壊的操作という制約を外部制御器にも課せば二ビット反例が再現する一方、これだけで現実の内部観測者が外部制御器へ完全還元できるとは言えない。

**次の問い。** 「インターフェース因子化」という語の下で、因果的遮蔽と実験合成を混同していないか。

### Phase 8：interface factorization の分解

**当初の仮説。** 外部の分離実験族が一つの単一履歴実現可能な適応実験を通じて因子化できないことが、内部観測限界の本体ではないか。

**なぜ魅力的に見えたか。** 因子化という語は、入力・出力チャネル、実験精密化、情報復号、制御器状態の遮蔽を一つにまとめられるように見えた。

**何によって分解されたか。** 少なくとも次の二概念は別である。

#### Causal Interface Factorization (CIF)

制御器の現在状態 $C_t$ が、宣言された action channel $U_t$ を迂回して対象状態 $X_t$ に動的に読まれず、対象から制御器への影響も宣言された observation channel $Y_t$ を通るという条件である。確率的な略記では、例えば

$$
P(X_{t+1},Y_t\mid X_t,U_t,C_t)
=
P(X_{t+1},Y_t\mid X_t,U_t)
$$

のような因子化を要求する。これは**動的な因果遮蔽**の条件であり、時刻 0 の seed、setting、潜在状態の独立性を含めない。正確な条件は、何を $X_t,U_t,C_t,Y_t$ と数えるかという採用済みの因果変数分解、因果グラフ、構造方程式に相対的である。

#### Experimental Amalgamation (EA)

複数の実験的識別情報を、一つの**単一履歴実現可能**な実験または適応履歴へ共通精密化できることである。これは CIF ではなく、物理的共同実現可能性または逐次合成可能性を含む実験構造の条件である。

CIF は EA を含意しない。二ビット破壊例では、コード漏洩がなく CIF が成立しても EA は失敗する。逆方向については、対象が方策コードを読めるモデルでも、限定された実験族に共通精密化が存在する例を作れると思われるが、EA の確率的・物理的定義を固定する前に一般的な非含意命題とはしない。[OPEN] どの EA 概念について逆方向の独立性が成立するかをモデル別に確認する必要がある。

**撤回したもの。** [WITHDRAWN] CIF と EA をともに `interface factorization` と呼び、一つの条件として扱うこと。

**残ったもの。** [ESTABLISHED] CIF と EA は異なる述語である。前者は宣言外の動的因果経路、後者は実験情報の単一履歴での合成可能性を問うため、片方を検証して他方を済ませることはできない。

**次の問い。** 自己包含は CIF の失敗を強制するか。また乱数を導入すれば、方策依存の対角的環境を避けられるか。

### Phase 9：対角線、乱数、初期相関

**当初の仮説。** 世界が内部観測者の方策コードを含むなら、選ばれた方策を読んで必ず失敗させる対角的生成系を作れるため、内部方策には固有の限界があるのではないか。

**なぜ魅力的に見えたか。** 自己包含性を、単なる容量制約ではなく方策依存の不可能性へ接続できるように見えた。Wolpert 型推論装置との類似もあった。

**何によって限定されたか。** 外部環境に方策コードが動的に漏れていれば、同じ対角的応答を構成できる。逆に世界の部分系としての内部観測者でも、方策コードが因果的に遮蔽されていれば、その種のコード読出し反例は成立しない。したがってこの反例の本体は内部性ではなく CIF の成否である。

候補クラス固定の規律にも注意が必要である。方策を見た後で adversary が新しい候補を追加する反例は許されない。対角例を使うなら、「方策コードを入力として読み、その値に応答する」という遷移規則を持つ候補生成系を、方策選択前に候補クラスへ含めなければならない。

#### Preparation / initial independence

乱数についても、単に「ランダム化したから adversary は読めない」とは言えない。動的 CIF が成立しても、時刻 0 で乱数 $R$ と環境側潜在変数 $\Lambda$ が相関していれば、環境は後の選択について情報を持ちうる。ここで必要になりうる条件は、seed independence、setting independence、preparation independence、initial latent correlation の制御、共通原因の排除またはモデル化である。これらは CIF とは別の**準備・初期独立性**条件であり、どの条件付き独立性を採るべきかは実験プロトコルに相対的である。seed の秘匿や生成器品質も、独立性そのものとはさらに別の設計条件である。

Bell 文脈の measurement independence

$$
P(\lambda\mid x,y)=P(\lambda)
$$

とは構造的類似があるが、一般の実験設計における初期相関の存在を直ちに superdeterminism と同一視してはならない。measurement dependence は、通常の共通原因、装置記憶、選択バイアス、seed 漏洩などでも起こりうる。Bell の局所隠れ変数モデルに固有の前提配置と、一般的な実験インターフェース監査は区別する。

**撤回したもの。** [WITHDRAWN] 自己包含だけから CIF の失敗または乱数独立性の失敗が従うという主張。

**残ったもの。** [SYNTHESIS] 自己包含が非自明になるのは、自己出力を含む query closure、真部分系記録容量、コード可視性、初期相関など、対象と観測者の結合条件を追加したときである。

**次の問い。** 単一の不可能定理ではなく、科学的識別が成立するための異なる前提を、固定した直列階層ではなく依存・代替関係をもつネットワークとして監査できるか。

---

## 5. What the failed theorem search actually uncovered

最初に探したのは、「観測には普遍的な存在論的非一意性がある」という一般定理だった。Phase 1–9 は、その探索が順に失敗した記録である。同時に、失敗するたびに、それまで一つに見えていた問題が別の条件へ分かれた。

- observation-map identifiability
- resource and query access
- single-history composition
- preparation、reset、copy、collective access
- causal shielding and declared interaction paths
- setting / preparation / sampling independence
- calibration、reference frame、SPAM、gauge
- model-class specification and misspecification
- finite-sample error、inverse stability、predictive validation
- model-class exclusion から interpretation への追加推論

量子 prior-art reconstruction が示したのは、これらの多くが未発見だったことではない。tomography、GST、state discrimination、Bell methodology、contextuality、ontological models、統計学、科学哲学が、それぞれの formal object と語彙で既に高度に研究している。Bell の PI/OI、memory loophole、coincidence-time loophole、量子測定の joint measurability / nondisturbance、GST の gauge などでは、field-native terminology の方が本ノートの一般語彙より精密である。

従って失敗探索の成果を、新しい不可能定理や新しい条件群の発見として評価しない。より限定的には、**既知の保証構造が別分野へ分散しているとき、その保証の出所、cross-impact、backgrounding、handoff をどう追うかという問いが形成された**と評価する。この問いの形成自体が新しい方法論的貢献かどうかも未実証である。

---

## 6. What each failure taught us

各失敗は、元の問いを否定しただけでなく、混同していた論理層を分離した。

| 失敗した期待 | 修正後の教訓 | 現在の扱い |
|---|---|---|
| 非単射性から新しい存在論定理が得られる | 非単射性は識別不能の定義的核にすぎない | model class と experiment family を指定する |
| 内部性が非識別性を強制する | `inside/outside` のラベル単独では差を導けない。完全な履歴能力の同一化は規約的で、実装対応はモデル条件付きである | timing・容量・自己問合せ・記憶脆弱性・遮蔽条件を個別化する |
| 生成からログへの移行は必ず情報を失う | 情報損失は具体的チャネルについて証明が必要 | sufficiency、Blackwell order、coarse graining へ接続する |
| 資源極限でも一般にファイバーが残る | 極限挙動は候補クラスと収束概念に依存する | finite、generic、asymptotic、limit learning を分ける |
| ペア分離があれば単一履歴でも分離できる | 固定有限・決定論的設定の informational refinement と、物理的共同実現・無限確率設定を分ける | domain/interference obstruction と収束・誤差条件を追跡する |
| 破壊的測定は内部性の徴候である | 同じ単一コピー制約なら外部でも失敗する | copy/reset/fresh preparation を明記する |
| interface factorization は一概念である | CIF と EA は別の述語であり、少なくとも CIF は EA を含意しない | 因果グラフと実験精密化を別々に監査する |
| 乱数で対角 adversary を避けられる | 動的 CIF と準備・初期独立性は別条件であり、seed の秘匿も追加条件である | private randomness、initial correlation、common cause を明示する |

この経緯から、現時点での焦点は「観測成功に存在論が含まれないことの証明」ではなく、**観測成功を生成構造の同定へ接続する前提を、どこまで個別に検査できるか**へ移った。

---

## 7. Existing theories: correspondences, counterexamples, and partial coverage

### 7.1 数学・統計・計算・物理における対応

この問題の各部分には、複数分野で既に形式化された問題が対応する。ただし「吸収」という v0.1 の表現は、同じ問題が完全に解かれているかのように強すぎた。v0.2 では関係を `covers`、`supplies counterexample`、`provides close analogue`、`supplies formal vocabulary`、`partially constrains`、`special-case correspondence` に分ける。

| 既存理論 | 関係の種類 | 対応する段階・失敗 | 本ノートへの限定・教訓 |
|---|---|---|---|
| **Inverse problems** | covers | Phase 1 の $O^{-1}(l)$ の存在・一意性・安定性 | 単射でも逆が不安定なら実用的復元は壊れる。存在論的含意は理論の射程外 |
| **Statistical identifiability** | covers | 観測 law が異なるパラメータを区別するか | global/local/generic を分ける。指定モデル族の内部命題であり、$\theta_\star\in\Omega$ を保証しない |
| **System identification** | covers / partially constrains | Phase 4–6 の入出力履歴からの動的モデル推定 | persistent excitation、次数、ノイズ、閉ループ性、可観測性を条件化する |
| **Minimal realization** | supplies counterexample | 「完全な振る舞いでも生成子は一意でない」という一般化 | 可制御・可観測な線形極小実現は相似を除き一意になる。普遍的非一意性を反証する |
| **Myhill–Nerode / automata minimization** | supplies counterexample / formal vocabulary | Phase 1・4 の振る舞い同値類 | 正則言語の最小 DFA は同型を除き一意であり、canonical generator があるクラスを示す |
| **Adaptive distinguishing sequences** | covers a finite deterministic special case | Phase 5 の $\forall\exists$ と $\exists\forall$ | ペア識別可能性と preset/adaptive separator の存在を分ける。無限・確率設定を自動的には扱わない |
| **Blackwell comparison** | supplies formal vocabulary | Phase 3・6 の informational refinement | garbling による比較を与えるが、同一試料での物理的共同実行を含意しない |
| **Sufficient statistics** | partially constrains | Phase 3 のログ圧縮と情報保存 | 十分性は指定されたモデル族・推論対象に相対的であり、「全生成存在論に十分」ではない |
| **Bisimulation / process testing** | supplies formal vocabulary | 観測同値と実装差 | 相互作用可能な過程の外的同値と商を定義するが、どの実装差を ontology と数えるかは別途決める |
| **Active diagnosis** | provides close analogue / partial coverage | Phase 5–6 の介入による候補縮約 | 許容制御と診断を結びつける。ここでいう EA 全般との exact match は主張しない |
| **Sequential/adaptive experiment design** | covers / partially constrains | 単一適応履歴での実験選択 | 情報獲得、停止、誤りを扱うが、安全性・再準備・実験可用性はモデルごとに別条件になりうる |
| **Hellinger process / absolute continuity / singularity** | supplies formal vocabulary / partial coverage | 分布差と単一履歴分離の混同 | 有限観測、漸近分離、相互特異性、contiguity を区別させる |
| **Safe exploration** | provides close analogue | Phase 6 の domain obstruction | 情報的な行動が安全制約下では実行不能という構造を与える |
| **Learning in the limit / Gold** | covers a limiting notion | Phase 4 の有限段階非識別と極限識別 | 有限時点の一意性と、推測が極限で安定することを分ける |
| **Query learning / Angluin** | supplies formal vocabulary / special-case characterization | 問合せ形式が学習能力を変えること | 利用可能な query の種類を前提化する。正例データからの学習可能性に関する Angluin の特徴づけは限定クラスの結果である |
| **Latent model / HMM identifiability** | covers special model classes | Phase 3–4 の隠れ生成子と出力過程 | 非識別例と、rank 等の条件下の generic identifiability の双方がある |
| **Quantum tomography / estimation** | covers a mature model-relative problem | 有限次元状態・過程の ideal identifiability、finite-sample estimation、confidence、stability | informational completeness は指定状態空間での injectivity を特徴づける。準備の exchangeability、drift、misspecification、ontology は別問題 |
| **Detector/process tomography and GST** | covers calibration, SPAM, and gauge structure | 装置を既知とする校正依存と self-consistent characterization | GST は SPAM を前景化するが、operationally identifiable target は gauge を除く。同定が absolute ontology を与えるとはしない |
| **Breuer self-measurement** | partially constrains / supplies counterexample under assumptions | Phase 2 の自己測定直観 | 部分系状態への制限など追加条件がある。自己包含だけの一般定理へ拡張しない |
| **Wolpert inference devices** | provides close analogue / conditional impossibility | Phase 2・9 の対角的自己推論 | probe family と出力意味論を固定した不可能性であり、任意の有限候補識別とは同一でない |
| **Causal graphs / d-separation / Markov blanket** | supplies formal vocabulary | Phase 8 の動的 CIF と Phase 9 の共通原因 | 変数分解と因果仮定に相対的であり、グラフがデータだけから一意に得られるとは限らない |
| **Measurement independence** | special-case correspondence | Phase 9 の setting と潜在状態の初期相関 | Bell 型推論における特定の独立仮定。一般の seed 漏洩・交絡と同一視せず、superdeterminism の同義語にしない |
| **Bell methodology and causal formulations** | covers a specialized inference network | Bell-local factorization、parameter/outcome independence、measurement independence、loophole、finite-sample inference | memory、coincidence-time、detection、setting choice 等は field-native に分解する。CIF 一語へ畳み込まない |
| **Contextuality and ontological-model no-go results** | covers model-class exclusion under explicit assumptions | operational equivalence、noncontextuality、$\psi$-ontic/$\psi$-epistemic distinctions、preparation independence | Bell、KS、generalized contextuality、PBR は異なる定理であり、単独で unique ontology を選ばない |
| **No-cloning / no-broadcasting** | quantum special-case counterexample | Phase 5–6 の product/copy failure | 量子候補クラスに固有の制約である。incompatibility、contextuality、one-copy limitation と混同せず、普遍的前提にしない |

二つの反対方向を同時に保持する必要がある。Myhill–Nerode や線形極小実現は、適切なクラスと極小性の下で生成子の一意性を回復する。他方、latent model の非識別、有限資源、自己測定、対角 query、safe exploration、量子クラスにおける copy 制約は、それぞれ限定された限界を示す。したがって「観測から生成構造は一意にならない」も「十分な観測なら必ず一意になる」も、クラス指定なしには成立しない。

### 7.2 科学哲学・科学方法論における先行形

v0.1 はこの層をほぼ欠いていた。以下は exact match や直接の系譜を確定する表ではなく、中心命題に強い先行形があることを示す暫定対応である。

| 先行研究・概念 | 関係の種類 | 本ノートのどの論点に対応するか | 留保 |
|---|---|---|---|
| **Duhem–Quine / underdetermination** | provides close philosophical analogue | 観測的成功の評価が単独仮説ではなく補助仮定・背景理論に依存すること | Duhem と Quine の射程は同一でなく、「本ノートそのもの」とは断定しない |
| **van Fraassen / constructive empiricism** | provides close philosophical analogue | empirical adequacy と、理論の非観察的構造を文字通り真と受け入れることの区別 | 本ノートは constructive empiricism を採用せず、存在論的一意性の可能性も排除しない |
| **Stanford / unconceived alternatives** | supplies a challenge to class adequacy | 現在の候補集合に未着想の競合が含まれない可能性、すなわち $\theta_\star\in\Omega$ と候補網羅性 | model misspecification と完全に同じ概念ではない |
| **Collins / experimenter's regress** | provides close sociological and epistemic analogue | 装置の正しさと結果の正しさが相互依存し、成功基準が循環的に絡みうること | すべての補助条件が regress に陥るとは主張しない |
| **Suppes / models of data** | supplies formal and methodological vocabulary | 原データ、データモデル、理論モデルの媒介を区別し、ログを生成過程の単純コピーとしないこと | 「直接の祖先」かどうかは文献史的監査を要する |
| **Mayo / severe testing and error statistics** | supplies a positive audit programme / partial coverage | 成功がどの誤りを高確率で発見できた試験によるかを問うこと | 本ノートの全前提ネットワークを既に尽くすとは言わない |
| **Bogen & Woodward / data and phenomena** | supplies a conceptual distinction | 記録されたデータと、理論が説明する比較的安定した現象との間の推論段階 | 本ノートの log/generation 区別との一対一対応ではない |
| **Hacking / representing and intervening** | provides close methodological analogue | 表象の成功だけでなく、介入可能性・実験実践を識別の条件として重視すること | 介入成功から単一 ontology が直ちに出るとは読まない |
| **Manski / partial identification** | covers an alternative inferential target | 点識別が失敗するとき、仮定を明示して identified set を報告すること | ontology 全般の理論ではなく、指定統計モデル内の推論戦略である |
| **Causal identifiability / do-calculus / identification theory** | covers special causal queries | 観測・介入分布と因果仮定から、特定の因果量が一意に導出できるか | causal query の識別と生成構造全体の同定を混同しない |
| **M-closed / M-open vocabulary; model misspecification** | supplies close vocabulary / covers statistical consequences | 真の分布・生成機構が候補クラス内にあるか、外にあるかを区別すること | M-open 等の用法は文献間で揺れ、本ノートの $\theta_\star\in\Omega$ と完全同値とはしない |

[OPEN: systematic philosophy-of-science literature audit] 強い哲学的先行形が存在するため、中心命題の概念的新規性は現時点では主張しない。ただし「Duhem–Quine と Collins の単なる再記述」「Suppes が直接の祖先」「Mayo が同じ監査プログラムを完成済み」「M-open が完全に対応する」という査読上の候補評価も、一次・二次文献の体系的比較なしには確定しない。

### 7.3 既存研究に対する本ノートの位置

既存研究は、識別、校正、誤差、因果仮定、model-class exclusion、解釈問題をそれぞれ高度に扱っている。v0.4 はそれらを置換せず、一般監査語彙を field-native theory より上位に置かない。候補となる役割は、**indexing、visualization、assurance-provenance tracking、cross-impact tracking、backgrounding map、handoff map、scope-preservation warning** に限られる。これらが単なる提示形式を超えるかは §12 の Erasure Test と methodological-value test に委ねる。

---

## 8. Distributed assurance and assurance provenance

### 8.1 中心像と、歴史的な prerequisite network

「前提スタック」「科学的識別可能性の前提ネットワーク」は検討履歴を保存する名称として残すが、v0.4 の中心概念ではない。availability、safety、reset、fresh preparation、copy、persistent excitation、separation は、目的、前提、実現機構、代替、robustness condition として異なる役割を持つ。さらに量子ケースでは、self-testing のように downstream behavior が device characterization へ戻る経路と、一つの failure が複数 edge を壊す経路が確認された。

中心像は、科学的 claim を支える異種の support relation と、その出所である。

~~~text
claim
 ├─ theorem-relative
 ├─ design-supported
 ├─ calibration-supported
 ├─ statistically constrained
 ├─ empirically cross-checked
 ├─ model-relative
 └─ interpretive / theory-choice dependent
~~~

これらは排他的でも網羅的でもない。同じ claim が複数の経路に支えられ、各経路が別の仮定と uncertainty を持ちうる。以下の v0.2 図は、保証の全理論ではなく、どの support relation を追加調査すべきかを示す歴史的 inventory として読む。

当初想定した直線

```text
world → experiments → records → identifiability
      → prediction success → ontological interpretation
```

は、そのままでは正しくない。予測成功は生成構造の完全識別なしにも成立し、識別可能性があっても有限標本で予測が成功するとは限らない。より安全な依存図は次である。

```text
[target Ω, equivalence ≅] ─────── [candidate-class adequacy: θ★ ∈ Ω ?]
          │                                      │
          ├──────────────┬───────────────────────┤
          ▼              ▼                       ▼
 [experiment       [dynamic CIF]       [preparation / initial
  availability]                         independence]
          │              │                       │
     ┌────┴─────┐        └──────────┬────────────┘
     ▼          ▼                   ▼
 [safe       [reset / fresh   [declared interaction
 exploration] preparation /    and transcript laws]
     │         repeat / copy]          ▲
     └────┬─────┘                       │
          ├── [persistent excitation] ──┤
          ├── [sequential composition / product experiment / EA]
          └── [stable recording and sufficient reduction]
                                          │
                               ┌──────────┴──────────┐
                               ▼                     ▼
                    [identifiability and      [predictive adequacy
                     inverse stability]        on a target domain]
                               └──────────┬──────────┘
                                          ▼
                         [causal / minimality / symmetry /
                          model-adequacy bridge principles]
                                          ▼
                         [ontological interpretation —
                          defeasible, not automatic]
```

矢印は論理含意ではなく、典型的な依存または支援関係を表す。とりわけ $\theta_\star\in\Omega$ は downstream の識別成功から一般には出ない。最下流の解釈も、上流成功に機械的に含まれる出力ではない。一方、候補クラスの適切性、分離、安定性、橋渡し原理が独立に強く支持される個別クラスで、一意的解釈が合理的に支持される可能性を本ノートは否定しない。

### 8.2 Assurance provenance（保証の出所／保証来歴）

本ノートでいう **assurance provenance** は、ある科学的結論が、どの種類の保証経路、仮定、装置設計、校正、データ、理論に支えられているかを追跡するための作業語である。これは新しい形式理論ではなく、カテゴリーも完全ではない。assurance case、metrological traceability、evidence graph、argumentation framework などとの先行研究比較は未完である。

v0.4 では v0.3 の support-provenance 七分類を増やさず、そのまま暫定使用する。

| provenance label | 意味 | 注意 |
|---|---|---|
| **theorem-relative** | 明示された公理・モデル・正則性条件の下で、定理または解析により支えられる | 前提の経験的妥当性まで定理が保証するわけではない |
| **design-supported** | 空間配置、遮蔽、乱数化、制御、プロトコル構成により支えられる | 実装逸脱と未モデル経路を別に監査する |
| **calibration-supported** | 校正、参照標準、traceability、装置同定により支えられる | 校正の transfer、drift、gauge を追跡する |
| **statistically constrained** | 有限標本推論、誤差率、信頼領域、検定、感度分析により制約される | sampling model と stopping rule に相対的でありうる |
| **empirically cross-checked** | 独立測定、control、replication、別方式との整合で支持される | 「独立」の範囲と共有誤差を明示する |
| **model-relative** | 指定された state space、causal model、noise model、同値関係の内部で成立する | model-class adequacy は別の評価である |
| **interpretive / theory-choice dependent** | 説明、統合、単純性、因果像、存在論などの追加基準に依存する | operational result から自動的には出ない |

これらは相互排他的ではない。一つの support edge が theorem-relative かつ model-relative であり、別の校正と実験的 cross-check も受けることがある。`only indirectly constrained` と `circularly entangled with success criterion` は provenance の種類ではなく、監査上の scope/risk flag として残す。

### 8.3 v0.2 auditability taxonomy との対応

| v0.2 の表現 | v0.4 で維持する扱い |
|---|---|
| independently/directly testable | empirically cross-checked または statistically constrained。独立性の範囲を別記する |
| independently supported | design-supported、calibration-supported、empirically cross-checked のいずれか、または複数 |
| design-certified | design-supported。「certified」は保証範囲を明示できる場合に限定 |
| analytically guaranteed | theorem-relative。モデル前提を併記 |
| statistically constrained | 同名を維持 |
| model-relative | 同名を維持 |
| only indirectly constrained | provenance ではなく scope flag |
| circularly entangled | provenance ではなく依存関係上の risk flag |
| not self-certified by target success | 根拠欠如ではなく、target success 単独の論理的射程を示す注記 |

### 8.4 歴史的 condition inventory

以下は v0.2 の前提ネットワーク表を保存したものである。各行は普遍的な必須ノードではなく、field-native analysis へ進むための索引である。旧 `auditability` 欄は v0.2 の語彙を保持するために残し、実際の監査では上の provenance taxonomy へ写して用いる。

| ノード | role | 必要になるもの | 主な既存理論 | 外すと何が壊れるか | auditability |
|---|---|---|---|---|---|
| **Target specification** | target specification | 候補クラス $\Omega$、同型・ゲージ同値 $\cong$、識別対象 | model theory、realization theory、statistical modeling | ラベル差を構造差と誤認、または観測同値で結論を定義的に消去 | **model-relative**。比較言語と候補境界は成功スコアから出ない |
| **Candidate-class adequacy** | prerequisite / interpretive bridge | 真の生成構造を表す候補が $\Omega$ 内にあること、または近似誤差の明示 | misspecification、M-open vocabulary、unconceived alternatives、robust statistics | within-model で一点識別しても、対象外の生成構造を排除できない | **only indirectly constrained**。外部予測・残差・拡張比較で圧力を掛けられるが、網羅性の自己証明は困難 |
| **Dynamic CIF / shielding** | prerequisite | 現在の制御器状態が宣言 action channel を迂回して動的に読まれない | causal graphs、d-separation、security/noninterference | code-reading adversary、宣言外 feedback | **design-certified + model-relative**。隔離・介入試験は可能だが、変数分解と未測定経路に依存 |
| **Preparation / initial independence** | prerequisite / robustness condition | seed、setting、preparation と潜在状態の必要な初期独立性 | causal inference、randomization、measurement independence | 初期共通原因や seed 相関を動的漏洩と誤認し、擬似反復を独立証拠と数える | **design-certified + only indirectly constrained**。ランダム化設計や negative control で支えるが有限ログだけの完全証明ではない |
| **Experiment availability** | prerequisite | 候補集合上で意味をもつ共通操作、校正済み介入 | active design、control、diagnosis | 分離に必要な操作が存在しない、候補ごとに実行可能 domain が異なる | **independently testable + model-relative**。装置範囲は試験できるが未着想候補までの全域性は保証しない |
| **Safe explorability** | enabling / robustness condition | 壊滅状態を避けて情報的領域へ到達する方策 | safe exploration、viability、robust control | informative action が危険・不可逆で選べない | **design-certified + model-relative**。未知遷移への保証は採用した不確実性集合に依存 |
| **Re-preparation / reset / repetition** | enabling or substitute condition | 同じ $\theta$ に従う fresh preparation、reset、反復、またはそれらに代わる自然反復 | experimental design、ergodic/control assumptions | 破壊的実験を比較できず、順序依存を解消できない | **independently testable + circular-entanglement risk**。「同じ $\theta$」の判定が同定目標を先取りしうる |
| **Copy / product access** | enabling or substitute condition; theory-specific | 複数試料を同じ候補の実現として扱い、結果を積にできること | probability、experimental design、quantum information | pairwise 実験を別試料上でも統合できない | **design-certified + model-relative**。no-cloning/no-broadcasting は量子候補クラスでの特殊な failure で、一般条件ではない |
| **Persistent excitation** | enabling condition | 候補差が transcript に現れる入力系列 | system identification、adaptive control | 未励起方向にモデル差が隠れる | **model-relative + independently testable within model**。rank 条件は確認できるがモデル外の差を保証しない |
| **Sequential composition / product / EA** | enabling and identification condition | 操作後の継続可能性、情報保存、必要なら共通精密化 | automata testing、active diagnosis、Blackwell comparison | pairwise separation から一つの adaptive global separator が出ない | **model-relative**。有限決定論モデルでは探索可能な場合があるが、物理的共同実現は設計監査を要する |
| **Stable recording / sufficient reduction** | enabling / robustness condition | 記憶、時刻、参照系、識別対象に十分な圧縮 | metrology、information theory、sufficient statistics | 後続操作が過去ログを消し、圧縮が識別情報を落とす | **independently testable + model-relative**。媒体は検査できるが十分性は $\Omega$ と目的に相対的 |
| **Statistical or process separation** | identification condition | 異候補が異なる law、support、または process behaviour を与える | identifiability、bisimulation、testing、Hellinger theory | law 一致なら非識別、support 重複なら一回の zero-error 分離不能 | **model-relative**。解析可能だが、有限データから law の同一性を一般に確定できない |
| **Inverse stability** | robustness condition | 小さなログ誤差が巨大な構造差へ増幅されない | inverse problems、regularization | 数学的一意性があっても実用復元不能 | **model-relative + independently testable locally**。条件数等を調べられるが misspecification は別問題 |
| **Predictive validation** | validation outcome | 対象領域・損失・distribution shift を明示した成功 | statistics、learning theory、forecast evaluation、severe testing | interpolation を全構造の支持と誤認し、分布外で破綻 | 指定領域では **independently testable**。領域選択や成功基準と **circularly entangled** になりうる |
| **Ontological bridge** | interpretive bridge | class adequacy、因果意味論、極小性、対称性商、競合理論比較 | philosophy of science、causal inference、realization theory | predictive quotient を唯一の生成構造と誤認 | **only indirectly constrained + model-relative**。独立介入・統合・競合排除で支持を増せるが成功だけでは自己証明されない |

### 8.5 代替・支援・特殊条件を区別する

この表の全項目が全科学分野で常に必要という意味ではない。対象の reset が不可能でも、自然に生じる複数事例や長い時間発展が、適切な同質性・定常性仮定の下で代替する場合がある。ただし、それらが同じ $\theta$ または同じ population law に従うことは追加条件である。量子状態 tomography では fresh preparation の意味が重要になりうる一方、no-cloning、測定 incompatibility、contextuality、単一コピー制約は別々の論点である。歴史的一回事象の因果推論では、再準備の代わりに比較対象、自然実験、構造仮定を用いることがある。

従ってこの inventory は普遍的公理列ではなく、**何が目的で、何が前提で、何が実現機構・代替・robustness 条件であり、それぞれがどの保証経路に支えられるかを記録するための索引**である。

### 8.6 Backgrounded assumptions / stabilized interfaces

**Backgrounding** とは、ある研究領域の主要問題ではない条件が、別の理論、装置設計、校正、標準手続によって安定化され、その領域では通常所与として扱われることである。これは neglect、hidden assumption、methodological failure の同義語ではない。成熟した科学に必要な分業でありうる。

例えば tomography は校正済み POVM と準備手順を入力にすることがあり、interpretation literature は実験室での SPAM 同定や finite-sample protocol を背景化しうる。監査上問うのは、(i) どこで支えられたか、(ii) どの範囲まで transfer できるか、(iii) 下流で必要な uncertainty と scope が保存されているか、である。背景化の存在だけから欠陥を推論しない。

### 8.7 Cross-domain handoff

**Handoff** は、上流分野で条件付きに得られた output が、下流分野の input として渡される関係である。量子ケースでは、例えば次の流れがある。

~~~text
calibration / device characterization
              ↓
tomographic state or process estimate
              ↓
Bell / contextuality operational statistics
              ↓
model-class exclusion
              ↓
interpretation / theory comparison
~~~

この図は一方向の必然的パイプラインではない。device-independent/self-testing のような逆向きの情報経路や、別経路からの cross-check もある。handoff の存在は欠陥でも情報損失でもない。中心的な監査問いは、**上流の条件、uncertainty、適用範囲が下流でどこまで保持され、どこから合理的に背景化されるか**である。

この問いを暫定的な ledger として書くなら、上流 output を

$$
O_{\mathrm{up}}=(\hat{\theta},U,A,S)
$$

と置ける。ここで $\hat{\theta}$ は estimate / claim、$U$ は uncertainty、$A$ は assumptions / calibration conditions、$S$ は validated scope である。下流が $T(O_{\mathrm{up}})$ を利用するとき、$U,A,S$ の decision-relevant な部分が representation と判断過程に保持されているかを問う。ただし、情報量または loss の一般尺度は定義せず、何が decision-relevant かは case-specific とする。

この **handoff-loss question** は、transfer の途中で scope または uncertainty が実際に失われるかを問う。科学的問題が構造的に後続問題へ deferred されるとは仮定しない。

### 8.8 Cross-cutting failure modes

failure mode を一つのノードへ排他的に割り当てない。一つの failure が複数の support edge を横断して壊しうるからである。

~~~text
drift
 ├─ preparation stationarity
 ├─ fixed target identity
 ├─ calibration transfer
 ├─ GST model validity
 └─ finite-sample assumptions
~~~

同様に SPAM は preparation と measurement characterization の双方に作用し、trial selection は記録、sampling、Bell inference の複数 edge に作用しうる。gauge freedom は常に「故障」なのではなく、operationally identifiable target を gauge-equivalence class へ修正する必要を示す場合がある。primary source や first detection site を記録してもよいが、cross-impact を消してはならない。

### 8.9 一般監査ラベルの限界

- **CIF** は Bell の parameter independence、outcome independence、measurement independence、signaling、cross-talk、各 loophole を置換しない。Bell 外の controller/environment interface を比較する generic audit label 候補に限定する。
- **EA** は joint measurability、nondisturbance、sequential composability、supplied copies、fresh preparation、collective access、adaptive experiment を置換しない。「複数情報を同一 target についてどの物理資源で統合するか」を比較する umbrella に限定する。
- **candidate-class adequacy** は misspecification、dimension/leakage、M-open vocabulary、unconceived alternatives、causal-model adequacy を置換しない。field-specific adequacy problems の横断索引である。

これらの語は exact theorem object でも、field-native terminology より上位の方法論でもない。

---

## 9. From predictive success to ontological interpretation

### 9.1 予測成功と識別可能性は別である

予測成功は、候補クラスの完全識別を必要としない。異なる生成構造が同じ予測分布を与える場合、予測に必要なのは観測同値類または predictive quotient だけである。逆に、モデルパラメータが理論上識別可能でも、データ不足、ノイズ、分布移動、逆問題の不安定性により予測が失敗しうる。さらに within-model で一意でも $\theta_\star\notin\Omega$ なら、その一意性は候補クラスの adequacy を保証しない。

圧縮して「predictive success は generative identifiability を一般には含意せず、identifiability も finite-sample predictive success を含意しない」と書ける。ただし、これは新しい数学的結果ではなく、異なる評価対象を混同しないための記法である。

これは「予測成功は存在論と無関係」という意味ではない。複数の独立領域で、厳しい介入テストに耐え、競合モデルを排除する予測成功は、世界構造を捉えている強い証拠になりうる。ただし、どの候補を競合に含めたか、実験が候補差を励起したか、再準備や独立性が成立したか、観測同値を超える解釈原理を何に置いたかは、成功スコアそのものとは別に監査される。

### 9.2 「存在論的非自己証明性」の暫定定義

以上を踏まえ、本ノートでは作業概念を次のように精密化する。

> 道具的・予測的成功それ自体は、その成功を支えているすべての保証経路の正当性と、それらを唯一の存在論へ接続する追加原理を、同時には自己証明しない。

従って、

> しかし多くの保証経路は、target success とは別の校正、設計、統計、再現、介入、理論によって非常に強く支持されうる。

これは数学的定理ではなく [SYNTHESIS] としての scope-preservation principle である。「道具の真理不在性」は、この ontological non-self-certification を指した旧作業名としてだけ残す。名称自体が真理不存在を連想させる過剰なものだったため、v0.4 の主題名には採用しない。「自己証明されない」と「根拠がない」は同義ではない。

補助条件群を $A$、成功事実を $S$、一意的生成解釈を $U$ と置き、「個別モデルで $A$ と $S$ から $U$ を導けても、$S$ だけから $A$ が出るわけではない」と圧縮できる。しかし、形式化された限りでこれは命題論理上の初等的な注意であり、数学的結果として数えない。$A$ を都合よく成功から独立と定義すれば、結論を定義へ埋め込むだけにもなる。

非自明な研究課題は $A=\bigwedge_i A_i$ の各成分について、次を個別に問うことである。

1. $A_i$ は成功判定 $S$ から独立した試験で検証できるか。
2. 装置構成・乱数化・隔離によって design-certified と言えるか。
3. $A_i$ は候補クラスまたは因果変数分解にのみ相対的か。
4. 反例探索や外部妥当性から only indirectly constrained されるだけか。
5. $A_i$ の採否と成功基準が circularly entangled していないか。

この**保証来歴と独立監査可能性**が v0.4 でも主問題である。$A_i$ の一部が別の観測や工学的検証によって強く支持されることは否定しないし、その成功を軽視する理由にもならない。

---

## 10. What can currently be claimed

### 10.1 現時点で言えること

- **[ESTABLISHED]** 観測・予測成功と生成構造の一意的識別は、一般には異なる定義をもつ別の評価対象である。ただし、これを $S\nRightarrow A$ と書くこと自体は初等的で、新しい数学的結果ではない。
- **[ESTABLISHED]** 指定モデルで両者を接続する定理には、候補クラス、同値基準、実験族、識別可能性など、その定理が要求する補助条件がある。
- **[ESTABLISHED]** 非単射観測写像の非一意性は既知かつ初等的であり、それ自体は新定理ではない。
- **[ESTABLISHED]** 内部観測一般の普遍的不可能性は成立しない。自己包含的でありながら自己状態または候補を符号化できる系が構成できる。
- **[ESTABLISHED]** `inside/outside` というラベル単独から識別能力差は導けない。完全な履歴能力を同じと置く規約はほぼ定義的であり、内部実装と外部実装の対応は特定モデルの条件付き命題である。
- **[ESTABLISHED]** 固定有限候補・決定論的結果・任意後処理という設定では、pairwise 実験の結合署名と大域分離器の informational refinement の関係を初等的に特徴づけられる。
- **[SYNTHESIS]** 無限・確率的設定の pairwise-to-global には uniformity、measurability、収束、誤差、計算可能性を含む追加条件が必要になりうるが、単一の一般境界定理は本ノートでは示していない。
- **[ESTABLISHED]** informational refinement と physical joint realizability は異なる。
- **[ESTABLISHED]** 決定的有限オートマトンや線形極小実現のように、適切な条件下で振る舞いが生成子を同型を除き一意に定めるクラスがある。
- **[ESTABLISHED]** latent-variable model、自己測定、推論装置、safe exploration、量子コピー制約などには、それぞれ異なる条件付き限界がある。
- **[ESTABLISHED]** within-model identifiability は候補クラス内部の命題であり、$\theta_\star\in\Omega$ という model-class adequacy とは別である。
- **[SYNTHESIS]** 識別、校正、有限標本誤差、因果仮定、model-class exclusion、解釈問題は、既存の専門分野で高度に研究されている。今回監査した量子ケースの局所記述では、field-native literature の方が本ノートの一般語彙より精密だった。
- **[SYNTHESIS]** 科学的成功は、theorem implication、modeling assumption、experiment design、calibration、statistics、causal assumptions、model-class restriction、interpretive inference など、異種の support relation の束として記述できる。
- **[SYNTHESIS]** 各分野は、別の分野または実験実践で安定化された条件を合理的に背景化し、結果を cross-domain handoff により受け渡すことがある。そのため、局所的には明瞭な保証来歴が全体図では見えにくくなる場合がある。
- **[SYNTHESIS]** target success は、それを支える全条件を論理的に自己証明しない。しかし、それらの条件は校正、設計、統計、再現、介入、理論から強い独立支持を得うる。
- **[SYNTHESIS]** drift、SPAM、selection、model violation のような一つの failure mode は、複数の support edge に横断的に作用しうる。
- **[SYNTHESIS]** 共通の保証来歴図は indexing と可視化を改善しうる。ただし、量子ケース後も organizational usefulness は plausible に留まり、methodological usefulness は未実証である。
- **[ESTABLISHED FOR THE GST CASE]** 一般監査語彙は、直観的に一貫した cross-domain narrative を与えても独立の診断内容を加えない場合がある。GST Case 01 では field-native reconstruction が全ての技術的結論を保存し、nuisance/reference uncertainty、quotient-level identifiability、gauge-sensitive reporting、model-specific extension の区別を一部でより精密にした。

### 10.2 現時点では言えないこと

- **[WITHDRAWN]** 普遍的な「真理不在定理」が成立する。
- **[WITHDRAWN]** 真理そのものが存在しない。
- **[WITHDRAWN]** 科学は真理へ到達できない。
- **[WITHDRAWN]** 内部観測者は原理的に世界を識別できない。
- **[WITHDRAWN]** 観測・予測成功から存在論的一意性が常に排除される。
- **[WITHDRAWN]** 生成からログへの変換があるだけで、情報損失または非同型性が従う。
- **[WITHDRAWN]** 現実の内部観測者は一般に、同一インターフェースの外部制御器へ還元できる。
- **[WITHDRAWN]** pairwise separation と common refinement の語だけで、無限・確率的な global adaptive separator の存在が一般に特徴づけられる。
- **[WITHDRAWN]** 前提ネットワークが全分野に共通する一本道の必要条件列である。
- **[WITHDRAWN]** within-model で一意に識別できれば、真の生成構造が候補クラス内に含まれる。
- **[WITHDRAWN]** measurement independence の破れは常に superdeterminism である。
- **[WITHDRAWN]** 今回の統合が数学的に新規である。
- **[WITHDRAWN]** 哲学的先行研究の監査前に、今回の統合の概念的新規性を主張できる。
- **[WITHDRAWN]** 既存研究に重要な missing edge が既に確認された。
- **[WITHDRAWN]** 「存在論的非自己証明性」が underdetermination 文献に対して確立した概念的新規性を持つ。
- **[WITHDRAWN]** 科学は重要な仮定を一般に隠している。
- **[WITHDRAWN]** cross-domain backgrounding が存在すれば、推論誤りまたは情報損失が生じる。
- **[WITHDRAWN]** 本ノートの図が既存の専門的レビューより優れている。
- **[WITHDRAWN]** 保証来歴図が確立した方法論的貢献である。
- **[WITHDRAWN]** 動的な boundary-relocation mechanism が確立した。
- **[WITHDRAWN]** Deferred Resolution が独立した methodological construct である。
- **[WITHDRAWN]** visualization だけで方法論的新規性が成立する。
- **[WITHDRAWN]** assurance provenance が field-native review または protocol checklist より優れた診断を既に実証した。
- **[WITHDRAWN]** 既存科学の存在論的推論が一般に誤っている。
- **[WITHDRAWN]** VED がこの議論によって正しいと証明される。
- **[WITHDRAWN]** VED が標準科学で評価しづらいことだけで、その内容が正当化される。

---

## 11. Relation to VED

**この研究ノートは VED を証明しない。** また、VED を通常の識別・予測・検証要件から免除しない。本ノートの各主張は VED の公理や生成図式とは独立に成立または失敗する。本ノートが指摘する保証の分散構造は VED を含むあらゆる理論に同じように適用され、「既存の評価軸より前段の生成条件を扱う」と自己記述する任意の理論にも対称的に適用される。

限定的に言えるのは次だけである。

> 通常の科学的評価が、実験可能性、記録、再準備、識別可能性などの安定化された interface を利用しているなら、それより上流の生成条件を対象とする理論について、どの保証経路を別の方法で用意する必要があるかを問う索引にはなりうる。

しかし、標準評価軸に乗りにくいことそれ自体は、その理論への証拠的支持を**一切与えない**。VED が「より手前を扱う」と自己記述しても、この監査から証拠的優位性は一切得られない。むしろ、どの保証経路を再構成し、どの代替的検証可能性を提供するかを明示する追加責任を負う。この基準は VED に有利にも不利にも特別扱いされない。

GST Case 01 で一般監査語彙が field-native vocabulary に吸収されたことは、VED を含む他の理論候補にも同じ Erasure Test と自己批判基準を適用すべきことを示すだけであり、VED への証拠的支持は与えない。

---

## 12. Value of rearrangement rather than novelty

個々の部品が既知であっても、保証の出所、背景化、handoff、cross-impact を横断表示することに独立した価値があるか。量子 prior-art reconstruction は、既存研究を最大限強く読めば、局所ノードと主要 edge の大半を field-native literature だけから再構成できることを示した。

| 評価区分 | 現時点の判定 | 理由 |
|---|---|---|
| **trivial repackaging** | 個別の非単射命題・有限共通精密化命題には該当 | 写像の非単射、有限分離族の積、容量の鳩ノ巣原理は新規内容ではない |
| **mathematical novelty** | **低い** | 中心論理、非単射性、有限決定論的な結合署名は初等的で、各条件問題にも既存理論がある |
| **conceptual novelty** | **低め／未確定** | underdetermination、constructive empiricism、experimenter's regress、models of data、severe testing 等との体系的比較が未了である |
| **organizational usefulness** | **plausible** | 分散した保証来歴、背景化、handoff、cross-impact を一つの図で追える可能性がある |
| **useful synthesis** | **限定的に維持可能** | 異分野で同じ語を強制せず、field-native 結論の scope を受け渡す索引として使う場合に限る |
| **methodological contribution** | **未実証** | 量子ケースは主に再分類・可視化であり、missing check や実験設計変更をまだ示していない |
| **potentially publishable synthesis** | **現状では主張しない** | 系統的文献レビュー、複数ケースの比較、用語史、再現可能な監査手順が必要 |
| **unsupported overreach** | 「真理不在の定理」「内部観測の普遍的不可能性」として発表する場合に該当 | 既知結果を超える一般定理がなく、反例クラスも明確である |

### 12.1 Erasure Test

> 監査ネットワーク固有の語彙を消しても、科学的内容、区別、実験判断を既存文献だけで同じように再現できるなら、そのケースでの追加価値は presentation / indexing に留まる。

これは一般的な方法論定理ではなく、自己評価のための反証基準である。量子ケースでは、tomography、GST、Bell、contextuality の局所内容はほぼ erasure に耐え、本ノート固有の追加価値は主として cross-domain visualization に残った。

GST Case 01 は、このテストの明示的な negative calibration になった。固有語彙を除いても技術的内容と判断が残っただけでなく、field-native reconstruction の方が一部で精密だった。したがって revision rule を次のように強める。

> 固有語彙を消した結果、field-native reconstruction の方が精密になるなら、その一般語彙は「補助的」として温存せず、少なくとも当該ケースでは積極的に降格または撤回する。

### 12.2 Methodological-value test

「見やすくなった」だけでは方法論的価値を認めない。少なくとも、missing assumption または新しい failure path の発見、experiment design や preregistration の改善、evidence ranking の変更、scope overreach の防止、あるいは別分野での同一 audit procedure の再利用のいずれかを、比較可能な事例で示す必要がある。

さらに、同じケースを field-native terminology だけで解析した **control reconstruction** と比較し、generic audit vocabulary によって diagnosis、decision、scope judgment、または relevant literature / evidence の retrieval に具体的差が生じることを要求する。それまでは、**organizational usefulness plausible; methodological usefulness unproven** と判定する。

新しい可視性は、それ自体で新しい科学的内容または方法論を意味しない。ただし横断配置が見落とし、scope loss、handoff error を再現可能に発見し、control より判断を改善するなら、その時点で方法論的価値へ昇格しうる。

### 12.3 Negative calibration result: GST Case 01

GST lineage を用いて、局所的解決が反復的な “Deferred Resolution / boundary relocation” を生むかを検査した。しかし standard QPT、self-consistent estimation、GST gauge、operational quotient、model checking、model-specific extension は field-native vocabulary だけでより正確に再構成できた。固有語彙を消しても technical distinction、scope judgment、diagnostic decision は失われず、いくつかの点では記述精度が上がった。

このため Deferred Resolution は独立方法論として採用せず、Case 01 を **frozen negative result** とした（[case note](./deferred_resolution_case_01_gst_v0.2.md); [revision ledger](./deferred_resolution_case_01_gst_v0.1_to_v0.2_diff.md)）。

この negative result から残す教訓は限定する。(1) 複数の residual / remaining conditions を一つの共通 mechanism の証拠としない、(2) model assumption、nuisance/reference uncertainty、quotient / representational redundancy、reporting convention、model misspecification、model-specific extension を区別する、(3) field-native vocabulary より情報の少ない一般語彙を降格する、(4) chronological sequence と logical dependency sequence を分ける、の四点である。assurance provenance の方法論的価値はこの一件だけでは棄却しないが、依然として未実証である。

### 12.4 量子ケースの Type 判定

- **Type A — Existing network already sufficient:** 既存研究だけで局所構造をほぼ再構成でき、追加価値は主に再命名・再描画である。
- **Type B — Existing nodes, weak cross-domain edges:** ノードと主要な局所 edge は既知だが、分野間の handoff と全体可視性が弱い。
- **Type C — Added audit structure:** 共通監査構造が実際の診断、設計、評価を改善する。
- **Type D — Genuine missing structure:** 既存研究に重要な依存関係の欠落が確認され、統合によって新しい推論問題が現れる。

量子 prior-art reconstruction の暫定判定は **Type B with a strong Type A component** である。tomography–calibration–estimation、Bell experiment–finite statistics–causal assumptions、contextuality–operational equivalence–model exclusion は既存文献が精密に接続している。他方、異分野間で保証の scope がどう背景化・handoff されるかの共通表示は弱い。これは C または D の証拠ではない。

従って現時点で守れる価値は、強い順に、(1) cross-domain visualization、(2) indexing / terminology と research-question generation、(3) 未検証の audit-procedure candidate である。新定理、新概念、確立した methodological framework は主張しない。

---

## 13. Open questions and next empirical step

以下では、先行研究確認で解ける課題を **[OPEN: literature audit]**、比較可能な実証または新しい表現法を要する課題を **[OPEN: research]** と区別する。

1. **[OPEN: research] Real handoff audit.** 上流文書で明示された uncertainty、assumptions / calibration conditions、validated scope が、下流の data product、論文、review、decision rule にどこまで保持されるかを実資料で追跡する。
2. **[OPEN: literature audit] Assurance provenance formalization.** assurance case、metrology、traceability、evidence graph、argumentation framework が既に何を形式化しているか。本ノートのカテゴリーに残る差はあるか。
3. **[OPEN: research] Scope / uncertainty loss across transfer.** $O_{\mathrm{up}}=(\hat{\theta},U,A,S)$ から下流表現へ渡すとき、decision-relevant な $U,A,S$ が実際に脱落し、判断を変えた事例はあるか。handoff の存在だけを loss と呼ばず、科学的問題が構造的に deferred されるとも仮定しない。
4. **[OPEN: research] Erasure benchmark.** standard textbook、review、protocol checklist と、generic audit vocabulary を用いた記述を control comparison し、diagnosis、decision、scope judgment、retrieval の何が本当に変わるか。
5. **[OPEN: research] Cross-domain reuse.** metrology、cosmology、nonequilibrium / irreversible experiments、phylogenetic inference、system identification で同じ handoff / provenance 表現が再現し、実際の判断を改善するか。
6. **[OPEN: research] Cross-impact representation.** one failure → multiple support edges を、不確実性の二重計上や因果方向の誤認なしにどう表現するか。
7. **[OPEN: research] Backgrounding audit.** 合理的な分業としての backgrounding と、適用範囲を越えてしまう危険な backgrounding を、事後物語ではなく再現可能な基準で区別できるか。
8. **[OPEN: literature audit] Philosophy and methodology.** Duhem–Quine、van Fraassen、Stanford、Collins、Suppes、Mayo、Bogen & Woodward、Hacking、Manski、model misspecification と、assurance-case / evidence-network 文献との exact / partial / merely analogous の境界を系統監査する。
9. **[OPEN: research] Legacy mathematical questions.** 確率的 EA、内生的実験の部分合成、無限候補の pairwise-to-global、CIF の経験的監査、再準備の同一性、逆安定性の位置づけは未解決のままである。ただし、一般監査語彙を先に置かず、各 field-native problem から定式化を始める。
10. **[OPEN] 用語の継続監査。** 旧称「道具の真理不在性」を履歴表示として残す利益が、真理不存在という誤読リスクを上回るかを引き続き見直す。

### 13.1 次の実証ステップ

次に必要なのは新しい概念追加ではなく、**real handoff audit** である。次の比較ケースは **metrological traceability** を優先する。traceability と uncertainty propagation が field-native に明示され、参照連鎖と文書上の handoff を追え、比較的 closure に近い対照も構成しやすいからである。これは Case 02 の結論を先取りせず、監査語彙なしの control reconstruction と同じ資料を比較するための選定理由にすぎない。

具体的には、calibration certificate、uncertainty budget、traceability statement、下流の measurement result / decision rule を対象に、上流の $U,A,S$ が保持されるかを確認する。generic map が field-native metrology review または checklist にない missing check、scope error、decision difference を一つも生まなければ、そのケースでの価値も presentation / indexing に留まる。

---

## 14. Revision status

### Established / comparatively secure

- 非単射観測写像から一意復元できないことは初等的である。
- 候補クラスと構造同値関係は、方策選択前に固定しなければならない。
- within-model identifiability と、$\theta_\star\in\Omega$ という candidate-class adequacy は別の命題である。
- 自己包含だけから普遍的非識別可能性は導けない。
- `inside/outside` というラベルだけから識別能力差は導けず、具体的な差には追加のモデル条件が必要である。完全に同じ履歴能力を与える規約は定義的で、実装対応は条件付きである。
- 固定有限候補・決定論的結果・任意後処理の設定では、結合署名と大域分離器の informational refinement を初等的に対応づけられる。無限・確率的一般形は含まない。
- CIF と EA は異なる概念である。
- 動的 CIF と preparation / initial independence は異なる条件である。
- informational refinement と physical joint realizability は異なる。
- 予測成功、統計的識別可能性、生成子の一意性、存在論的解釈は異なる主張である。
- 一意な極小実現が存在するクラスと、非識別性が残るクラスの両方がある。
- GST Case 01 では、field-native reconstruction が technical conclusions と scope judgments を保存し、仮説した反復的な boundary-relocation mechanism に独立の診断効果がなかった。

### Interpretive synthesis

- 科学的 claim を theorem、設計、校正、統計、cross-check、モデル、解釈に由来する異種の support relation の束として読み、その provenance を追うこと。
- 実験可能性、再準備、reset、記憶、独立性、実験合成、識別可能性、逆安定性を、固定前提列ではなく代替・feedback・cross-impact を含む保証網として表示すること。
- 「道具の真理不在性」を、真理の不存在ではなく、道具的成功の存在論的非自己証明性として読むこと。
- backgrounded/stabilized interface と cross-domain handoff を、欠陥ではなく科学的分業として記述した上で、scope の保存を問うこと。
- cross-cutting failure mode を一つのノードへ排他的に所属させず、複数 support edge への作用として表示すること。

### Working hypotheses

- 保証来歴、backgrounding、handoff、cross-impact を併記する map が、real handoff audit で missing check、failure path、scope overreach の少なくとも一つを field-native control より多く発見できる。
- 同一の audit procedure が量子論以外でも再利用でき、標準レビューの単なる再配置を超える。
- provenance taxonomy が既存 assurance-case、metrology、traceability、evidence-graph 文献に対して何らかの追加的索引価値を持つ。[OPEN: literature audit]

### Withdrawn claims

- 「観測写像の存在論的非一意性定理」が新しい一般定理である。
- 生成からログへの段階が存在すれば、生成構造とログは必ず非同型になる。
- 自己包含する内部観測者は原理的に全世界を識別できない。
- 資源を無限に増やしても存在論的ファイバーが一般に残る。
- 二ビット破壊例が内部観測者に固有の不可能性を示す。
- 内部性そのものが interface factorization の失敗を生む。
- 非形式的に「同じインターフェース」と言えば、一般の内部／外部観測者の履歴能力同値が確立する。
- CIF と experimental amalgamation は同じ条件である。
- CIF が seed・setting・潜在状態の初期独立性まで含む。
- pairwise separation から global separator への接続を、無限・確率的設定でも common refinement の語だけで一般に特徴づけられる。
- 前提スタックが全分野に共通する固定線形階層である。
- prerequisite network が独自の一般理論または field-native framework より上位の方法論である。
- CIF、EA、candidate-class adequacy が新しい field-level concept または一般的 theorem object である。
- 一つの failure mode は一つの primary node へ排他的に所属すべきである。
- 乱数化だけで方策依存 adversary を排除できる。
- 観測成功は存在論的一意性を常に排除する。
- 中心命題の命題論理的略記が新しい数学的結果である。
- 哲学側の系統監査なしに概念的新規性または方法論的貢献を主張できる。
- 量子ケースが Type C/D、または重要な missing edge を実証した。
- Deferred Resolution が独立した methodological construct である。
- boundary relocation が保証網の一般的または中心的な動的 edge である。
- visualization だけで方法論的新規性が成立する。
- 本検討が VED の正しさを支持または証明する。

### Open questions

上記 §13 を現行の課題表とする。新しい反例または先行研究が見つかった場合、まず該当する Phase、support edge、provenance、handoff、cross-impact、主張状態タグを更新し、結論だけを上書きしない。

### Revision protocol

今後の改訂では、各変更に次を記録する。

1. 変更前の主張。
2. 反例、証明、または先行研究。
3. 影響を受ける Phase と、support edge、provenance、backgrounding、handoff、cross-impact。
4. `ESTABLISHED / SYNTHESIS / HYPOTHESIS / WITHDRAWN / OPEN` の状態変更。
5. VED との関係に変更がないか。

新しい generic term を残す前には、次の順序で比較する。

1. field-native baseline reconstruction。
2. generic-term reconstruction。
3. 固有語彙を除く Erasure control。
4. diagnosis、decision、scope judgment、retrieval の差を調べる diagnostic-difference test。
5. 既存の名称・概念との prior-art naming audit。
6. 上記を通過した場合にのみ generic term を保持する。

本ノートの目標は最終結論の保存ではなく、**訂正可能な依存関係と撤回理由の保存**である。

---

## 15. References

以下は完全な文献レビューではなく、各失敗に対応・反例・部分的被覆・近縁概念を与える理論への起点である。今後、分野別レビューと一次文献の追加監査が必要である。

1. Allman, E. S., Matias, C., & Rhodes, J. A. (2009). “Identifiability of Parameters in Latent Structure Models with Many Observed Variables.” *The Annals of Statistics*, 37(6A), 3099–3132. [doi:10.1214/09-AOS689](https://doi.org/10.1214/09-AOS689)
2. Angluin, D. (1987). “Learning Regular Sets from Queries and Counterexamples.” *Information and Computation*, 75(2), 87–106. [doi:10.1016/0890-5401(87)90052-6](https://doi.org/10.1016/0890-5401(87)90052-6)
3. Barnum, H., Caves, C. M., Fuchs, C. A., Jozsa, R., & Schumacher, B. (1996). “Noncommuting Mixed States Cannot Be Broadcast.” *Physical Review Letters*, 76, 2818–2821. [doi:10.1103/PhysRevLett.76.2818](https://doi.org/10.1103/PhysRevLett.76.2818)
4. Blackwell, D. (1953). “Equivalent Comparisons of Experiments.” *The Annals of Mathematical Statistics*, 24(2), 265–272. [doi:10.1214/aoms/1177729032](https://doi.org/10.1214/aoms/1177729032)
5. Breuer, T. (1995). “The Impossibility of Accurate State Self-Measurements.” *Philosophy of Science*, 62(2), 197–214. [doi:10.1086/289852](https://doi.org/10.1086/289852)
6. Chernoff, H. (1959). “Sequential Design of Experiments.” *The Annals of Mathematical Statistics*, 30(3), 755–770. [doi:10.1214/aoms/1177706205](https://doi.org/10.1214/aoms/1177706205)
7. Fisher, R. A. (1922). “On the Mathematical Foundations of Theoretical Statistics.” *Philosophical Transactions of the Royal Society A*, 222, 309–368. [doi:10.1098/rsta.1922.0009](https://doi.org/10.1098/rsta.1922.0009)
8. Gold, E. M. (1967). “Language Identification in the Limit.” *Information and Control*, 10(5), 447–474. [doi:10.1016/S0019-9958(67)91165-5](https://doi.org/10.1016/S0019-9958(67)91165-5)
9. Hall, M. J. W. (2010). “Local Deterministic Model of Singlet State Correlations Based on Relaxing Measurement Independence.” *Physical Review Letters*, 105, 250404. [doi:10.1103/PhysRevLett.105.250404](https://doi.org/10.1103/PhysRevLett.105.250404)
10. Jacod, J., & Shiryaev, A. N. (2003). *Limit Theorems for Stochastic Processes* (2nd ed.). Springer. Chapter IV treats Hellinger processes, absolute continuity, and singularity. [doi:10.1007/978-3-662-05265-5](https://doi.org/10.1007/978-3-662-05265-5)
11. Kalman, R. E. (1963). “Mathematical Description of Linear Dynamical Systems.” *Journal of the Society for Industrial and Applied Mathematics, Series A: Control*, 1(2), 152–192. [doi:10.1137/0301010](https://doi.org/10.1137/0301010)
12. Lee, D., & Yannakakis, M. (1994). “Testing Finite-State Machines: State Identification and Verification.” *IEEE Transactions on Computers*, 43(3), 306–320. [doi:10.1109/12.272431](https://doi.org/10.1109/12.272431)
13. Ljung, L. (1999). *System Identification: Theory for the User* (2nd ed.). Prentice Hall.
14. Moldovan, T. M., & Abbeel, P. (2012). “Safe Exploration in Markov Decision Processes.” *Proceedings of ICML 2012*. [arXiv:1205.4810](https://arxiv.org/abs/1205.4810)
15. Nerode, A. (1958). “Linear Automaton Transformations.” *Proceedings of the American Mathematical Society*, 9(4), 541–544. [doi:10.1090/S0002-9939-1958-0135681-9](https://doi.org/10.1090/S0002-9939-1958-0135681-9)
16. Park, D. (1981). “Concurrency and Automata on Infinite Sequences.” In *Theoretical Computer Science: 5th GI-Conference*, 167–183. [doi:10.1007/BFb0017309](https://doi.org/10.1007/BFb0017309)
17. Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference*. Morgan Kaufmann. ISBN 978-0-934613-73-6.
18. Rothenberg, T. J. (1971). “Identification in Parametric Models.” *Econometrica*, 39(3), 577–591. [doi:10.2307/1913267](https://doi.org/10.2307/1913267)
19. Sampath, M., Lafortune, S., & Teneketzis, D. (1998). “Active Diagnosis of Discrete-Event Systems.” *IEEE Transactions on Automatic Control*, 43(7), 908–929. [doi:10.1109/9.701089](https://doi.org/10.1109/9.701089)
20. Wolpert, D. H. (2008). “Physical Limits of Inference.” *Physica D*, 237(9), 1257–1281. [doi:10.1016/j.physd.2008.03.040](https://doi.org/10.1016/j.physd.2008.03.040)
21. Wootters, W. K., & Zurek, W. H. (1982). “A Single Quantum Cannot Be Cloned.” *Nature*, 299, 802–803. [doi:10.1038/299802a0](https://doi.org/10.1038/299802a0)
22. Angluin, D. (1980). “Inductive Inference of Formal Languages from Positive Data.” *Information and Control*, 45(2), 117–135. [doi:10.1016/S0019-9958(80)90285-5](https://doi.org/10.1016/S0019-9958(80)90285-5)
23. Bernardo, J. M., & Smith, A. F. M. (1994). *Bayesian Theory*. Wiley. Chapter 4 develops model comparison vocabulary later associated with M-closed/M-open discussions. [doi:10.1002/9780470316870.ch4](https://doi.org/10.1002/9780470316870.ch4)
24. Bogen, J., & Woodward, J. (1988). “Saving the Phenomena.” *The Philosophical Review*, 97(3), 303–352. [doi:10.2307/2185445](https://doi.org/10.2307/2185445)
25. Collins, H. M. (1992). *Changing Order: Replication and Induction in Scientific Practice*. University of Chicago Press. (Original edition 1985.)
26. Duhem, P. (1954). *The Aim and Structure of Physical Theory*, trans. P. P. Wiener. Princeton University Press. [digital edition doi:10.1515/9780691233857](https://doi.org/10.1515/9780691233857)
27. Hacking, I. (1983). *Representing and Intervening: Introductory Topics in the Philosophy of Natural Science*. Cambridge University Press. [doi:10.1017/CBO9780511814563](https://doi.org/10.1017/CBO9780511814563)
28. Manski, C. F. (2003). *Partial Identification of Probability Distributions*. Springer. [doi:10.1007/b97478](https://doi.org/10.1007/b97478)
29. Mayo, D. G. (2018). *Statistical Inference as Severe Testing: How to Get Beyond the Statistics Wars*. Cambridge University Press. [doi:10.1017/9781107286184](https://doi.org/10.1017/9781107286184)
30. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
31. Quine, W. V. O. (1951). “Two Dogmas of Empiricism.” *The Philosophical Review*, 60(1), 20–43. [doi:10.2307/2266637](https://doi.org/10.2307/2266637)
32. Shpitser, I., & Pearl, J. (2006). “Identification of Joint Interventional Distributions in Recursive Semi-Markovian Causal Models.” *Proceedings of AAAI 2006*, 1219–1226. [University of California eScholarship record](https://escholarship.org/uc/item/2hw2x8d2)
33. Stanford, P. K. (2006). *Exceeding Our Grasp: Science, History, and the Problem of Unconceived Alternatives*. Oxford University Press. [doi:10.1093/0195174089.001.0001](https://doi.org/10.1093/0195174089.001.0001)
34. Suppes, P. (1962). “Models of Data.” In E. Nagel, P. Suppes, & A. Tarski (eds.), *Logic, Methodology and Philosophy of Science: Proceedings of the 1960 International Congress*, 252–261. Stanford University Press. [doi:10.1016/S0049-237X(09)70592-0](https://doi.org/10.1016/S0049-237X(09)70592-0)
35. van Fraassen, B. C. (1980). *The Scientific Image*. Oxford University Press. [doi:10.1093/0198244274.001.0001](https://doi.org/10.1093/0198244274.001.0001)
36. White, H. (1982). “Maximum Likelihood Estimation of Misspecified Models.” *Econometrica*, 50(1), 1–25. [doi:10.2307/1912526](https://doi.org/10.2307/1912526)
37. Christandl, M., & Renner, R. (2012). “Reliable Quantum State Tomography.” *Physical Review Letters*, 109, 120403. [doi:10.1103/PhysRevLett.109.120403](https://doi.org/10.1103/PhysRevLett.109.120403)
38. van Enk, S. J., & Blume-Kohout, R. (2013). “When Quantum Tomography Goes Wrong: Drift of Quantum Sources and Other Errors.” *New Journal of Physics*, 15, 025024. [doi:10.1088/1367-2630/15/2/025024](https://doi.org/10.1088/1367-2630/15/2/025024)
39. Nielsen, E., Gamble, J. K., Rudinger, K., Scholten, T., Young, K., & Blume-Kohout, R. (2021). “Gate Set Tomography.” *Quantum*, 5, 557. [doi:10.22331/q-2021-10-05-557](https://doi.org/10.22331/q-2021-10-05-557)
40. Jarrett, J. P. (1984). “On the Physical Significance of the Locality Conditions in the Bell Arguments.” *Noûs*, 18, 569–589. [doi:10.2307/2214878](https://doi.org/10.2307/2214878)
41. Brunner, N., Cavalcanti, D., Pironio, S., Scarani, V., & Wehner, S. (2014). “Bell Nonlocality.” *Reviews of Modern Physics*, 86, 419–478. [doi:10.1103/RevModPhys.86.419](https://doi.org/10.1103/RevModPhys.86.419)
42. Larsson, J.-Å. (2014). “Loopholes in Bell Inequality Tests of Local Realism.” *Journal of Physics A*, 47, 424003. [doi:10.1088/1751-8113/47/42/424003](https://doi.org/10.1088/1751-8113/47/42/424003)
43. Barrett, J., Collins, D., Hardy, L., Kent, A., & Popescu, S. (2002). “Quantum Nonlocality, Bell Inequalities, and the Memory Loophole.” *Physical Review A*, 66, 042111. [doi:10.1103/PhysRevA.66.042111](https://doi.org/10.1103/PhysRevA.66.042111)
44. Larsson, J.-Å., & Gill, R. D. (2004). “Bell’s Inequality and the Coincidence-Time Loophole.” *Europhysics Letters*, 67, 707–713. [doi:10.1209/epl/i2004-10124-7](https://doi.org/10.1209/epl/i2004-10124-7)
45. Spekkens, R. W. (2005). “Contextuality for Preparations, Transformations, and Unsharp Measurements.” *Physical Review A*, 71, 052108. [doi:10.1103/PhysRevA.71.052108](https://doi.org/10.1103/PhysRevA.71.052108)
46. Harrigan, N., & Spekkens, R. W. (2010). “Einstein, Incompleteness, and the Epistemic View of Quantum States.” *Foundations of Physics*, 40, 125–157. [doi:10.1007/s10701-009-9347-0](https://doi.org/10.1007/s10701-009-9347-0)
47. Budroni, C., Cabello, A., Gühne, O., Kleinmann, M., & Larsson, J.-Å. (2022). “Kochen–Specker Contextuality.” *Reviews of Modern Physics*, 94, 045007. [doi:10.1103/RevModPhys.94.045007](https://doi.org/10.1103/RevModPhys.94.045007)
48. Bell, J. S. (1990). “La nouvelle cuisine.” In A. Sarlemijn & P. Kroes (eds.), *Between Science and Technology*. Elsevier; reprinted in *Speakable and Unspeakable in Quantum Mechanics*. [doi:10.1017/CBO9780511815676.026](https://doi.org/10.1017/CBO9780511815676.026)
49. Shimony, A. (1986). “Events and Processes in the Quantum World.” In R. Penrose & C. J. Isham (eds.), *Quantum Concepts in Space and Time*. Oxford University Press.

---

## 16. Self-audit and final verdict

### 16.1 Conservative-revision audit

- v0.4 は新しい定理または普遍的不可能性を追加していない。
- Phase 0–9 と撤回履歴を保存した。
- 量子 prior art を、本ノートの一般語彙より局所的に精密なものとして読んだ。
- missing edge の存在を実証済みとはしていない。
- backgrounding を neglect とせず、handoff を自動的な information loss としていない。
- assurance provenance を新理論または完全分類として扱っていない。
- Bell、GST、tomography、quantum measurement では field-native terminology を優先した。
- CIF と EA は比較用 umbrella/index へ降格した。
- failure mode の cross-impact を一つの所属へ還元していない。
- methodological usefulness は未実証とした。
- Erasure Test を反証基準として採用したが、方法論定理にはしていない。
- GST negative result を肯定的成果へ読み替えず、固有語彙の撤回事例として固定した。
- handoff loss と Deferred Resolution を分離した。
- visualization と methodology を同一視せず、field-native control との判断差を要求した。
- assurance provenance は一ケースから撤回せず、その方法論的価値を未実証のままにした。
- VED への証拠的接続を行っていない。
- literature-review task と real protocol / cross-domain research task を区別した。

### 16.2 What is the strongest defensible contribution after the quantum prior-art reconstruction?

| 候補 | 現時点の順位 | 判定 |
|---|---:|---|
| **cross-domain visualization** | 1 | 最も擁護しやすい。既知の保証の出所、背景化、handoff、cross-impact を同じ図面で追う |
| **terminology / indexing** | 2 | field-native terminology への索引として限定すれば有用性がありうる |
| **research question generator** | 2 | handoff loss、real handoff audit、erasure benchmark を明示した |
| **audit procedure** | 3 | 候補。real handoff audit で field-native control を超える診断をまだ示していない |
| **methodological framework** | — | 未確立 |
| **new concept** | — | 主張しない |
| **theorem** | — | ない |

本ノートが保存しようとするのは、整った最終理論ではない。観測写像の非単射性から始まった一般定理への期待が、完全観測、自己記述可能系、極小実現の一意性、外部にも成立する破壊的反例、そして非形式的な「同一インターフェース」議論への再批判によって順番に崩れ、そのたびに問いがより限定された条件問題へ移った過程である。

現時点での最小限の結論は次である。

> 観測・予測成功は生成構造を強く支持しうるが、その成功だけでは、それを支えるすべての保証経路と、唯一の存在論へ接続する追加原理を同時には自己証明しない。多くの保証は既存分野で独立に強く支えられており、v0.4 の役割候補は、それらを置換することではなく、保証の出所、scope、backgrounding、handoff、cross-impact を追跡可能にすることである。

**現時点の証拠では、v0.4 は既存科学が照らしていない場所を指すノートではなく、主として、既存の照明がどこから来て、どこへ渡され、どこで合理的に背景化されるかを見えるようにするノートである。** 未知の暗部がないとは言えないが、本調査はそれを確立していない。

### 16.3 What changed after GST Case 01?

GST Case 01 から得られたのは新しい科学的機構ではなく、一般監査語彙を残すための基準を厳しくする必要性だった。固有語彙が field-native control より diagnosis、decision、scope judgment、retrieval を改善しないなら presentation / indexing に限定し、消去によって精度が上がるなら当該ケースから撤回する。

現在の生きた実証問いは、**scope、uncertainty、assumption provenance が科学的 handoff を越えて実際に保持されるか**である。
