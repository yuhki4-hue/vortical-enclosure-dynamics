# 道具の真理不在性

## 観測・予測成功と存在論的一意性のあいだにある条件群

- **副題:** 観測写像の非一意性仮説から、科学的識別可能性の前提スタックへ
- **English title:** *Instrumental Success and Ontological Non-Self-Certification: A Working Note on the Preconditions of Scientific Identifiability*
- **Alternative English title:** *From Non-Injective Observation Maps to the Prerequisite Stack of Scientific Identifiability*
- **Status:** working note / corrigible synthesis / not a theorem announcement
- **Version:** 0.1
- **Date:** 2026-08-16
- **Relation to VED:** independent methodological note; not evidence for VED

---

## 1. Abstract

本ノートは、観測・予測の成功と生成構造の一意的同定との関係をめぐって行われた一連の検討を、成功した結論ではなく、失敗・撤回・問題分解の履歴として再構成する。当初は、観測写像の非単射性、観測者の内部性、生成から安定ログへの変換などから、存在論的一意性に関する一般的不可能定理を得られるのではないかと考えた。しかし、非単射性は逆問題と識別可能性の初等的事実に吸収され、自己包含性だけから非識別可能性は導けず、生成―ログ非同型性も情報損失を定義へ埋め込めば循環することが判明した。さらに、決定的有限オートマトンや線形系の極小実現では、完全な振る舞いから同型を除く一意性が回復するクラスが存在するため、クラス非依存の一般命題は維持できなかった。

その後、問題は、各候補対を分離する反実験族と、一つの物理的に実現可能な適応履歴との違いへ移った。ここでも、単一コピー上の破壊的測定がもたらす障害は内部観測者に固有ではなく、同じ因果インターフェースを外部観測者に課せば再現する。残った中心問題は、内部／外部という位置関係ではなく、実験可能性、再準備、リセット、記録保持、安全性、独立性、共通精密化、統計的分離、逆問題の安定性などが、どのように識別可能性を支えるかである。

本ノートは、これらを「科学的識別可能性の前提スタック」として並べ直す。ただし、これは新しい普遍定理ではない。個々の層は inverse problems、statistical identifiability、system identification、automata testing、Blackwell comparison、bisimulation、active diagnosis、safe exploration、causal inference、self-measurement、inference-device theory、量子情報などで既に研究されている。本ノートの暫定的価値は、それらが「観測成功から存在論的解釈へ進む際に、どこで使われているか」を監査可能な順序で示すことにある。

---

## 2. Scope and terminology

### 2.1 「真理不在性」の限定

本ノートにおける「真理不在性」は、**真理そのものが存在しない**という主張ではない。また、**観測や予測から生成構造へ原理的に到達できない**という普遍的不可能性でもない。

暫定的には、次の監査上の主張を指す。

> 観測・予測・計算の成功それ自体には、その成功を唯一の存在論的世界像へ接続するために用いられた補助条件の正当性までは含まれていない。

短く言えば、

> 「当たる」という事実だけの中に、「世界は唯一このようである」を保証する条件すべてが含まれているわけではない。

したがって「不在」とは、対象世界からの真理の欠落ではなく、**道具的成功の自己証明能力の不在**を指す。この意味をより直接に表す名称としては、「道具的成功の存在論的非自己証明性」または *ontological non-self-certification of instrumental success* の方が安全である。「道具の真理不在性」は誤解を招きやすい作業名であり、今後の改名対象である。

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

### 2.4 主張状態タグ

- **[ESTABLISHED]** 既存数学または明示的反例によって比較的強く支持される。
- **[SYNTHESIS]** 既存結果を本ノートの問いの下で並べ直した解釈。
- **[HYPOTHESIS]** 追加検討を要する作業仮説。
- **[WITHDRAWN]** 本検討で撤回した主張。
- **[OPEN]** 現時点で未解決または文献監査が不十分な問い。

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

を作れば、内部観測者は候補を一意に記録できる。無限集合では真部分集合と全体が同じ濃度を持ちうる。さらにクワインや Kleene の再帰定理は、適切な計算モデルでは自己記述が可能であることを示す。Breuer の自己測定制約や Wolpert の inference-device 不可能性には、真部分系への制限、全状態の識別要求、固定された出力意味論、自己問合せ閉包など追加条件がある。

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

**撤回したもの。** [WITHDRAWN] 二ビット破壊例を、内部性そのものが生む不可能性の例として使うこと。

**残ったもの。** [ESTABLISHED] ペアごとの実験可能性と単一方策による大域分離の間には量化順序の差がある。その差を埋めるのは「内部性」ではなく、実験の共同実現可能性である。

**次の問い。** 個別実験を一つの実現可能実験へまとめるための部分合成・共通精密化条件は何か。

### Phase 6：experimental amalgamation / common refinement

**当初の仮説。** 実験を集合ではなく、履歴依存で部分的にしか合成できない構造として扱い、pairwise separation から global adaptive separator が存在する境界を、amalgamation 条件として特徴づけられるのではないか。

**なぜ魅力的に見えたか。** 候補依存で実行可能操作が異なる場合、実験は全域的関数ではない。また操作後の状態変化により、$e_1$ と $e_2$ が個別に可能でも $e_2\circ e_1$ が未定義になりうる。これは静的な観測写像では見えない。

**得られた区別。** [SYNTHESIS]

- **Domain obstruction:** 局所候補集合では実行可能な分離実験が、固定した全候補集合では安全に実行できない。
- **Interference obstruction:** $A$ と $B$ は個別に可能だが、一方の実行が他方の実行可能性または情報を破壊する。
- **Globalization:** 局所的に定義された実験を全候補に共通の実験へ延長できるか。
- **Amalgamation:** 複数実験の識別情報を保存する、内部実現可能な共通精密化が存在するか。

内生的な操作可能性を候補選択へ密輸入しないため、方策集合も固定候補クラスに対して定義する。履歴 $h$ と両立する候補 $\theta$ の内部状態集合を $C_\theta(h)$、状態 $x$ で許容される操作を $U_\theta(x)$ とすれば、方策 $\sigma$ は各到達可能履歴で

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

は単射である。内部履歴 $H_\sigma$ と後処理 $d$ が

$$
J=d\circ H_\sigma
$$

を満たすことは、$H_\sigma$ が大域分離器であることと同値になる。この意味では、共通精密化の存在が正確な必要十分条件である。

**何によって限定されたか。** この同値は、固定有限候補、決定論的結果、任意の後処理を許すという条件では初等的であり、新定理ではない。確率実験では Blackwell kernel、敵対的非決定性では結果集合またはゲーム意味論、物理的共同実行では状態更新を含む別の精密化概念が必要である。

**撤回したもの。** [WITHDRAWN] informational refinement と physical joint realizability を同一視すること。候補を一意に同定した後で各実験結果を計算上再構成できても、同じ試料上で複数実験を物理的に共同実行できたことにはならない。

**残ったもの。** [SYNTHESIS] 内生的実験集合を部分圏、partial algebra、game arena などとして記述し、reset、fresh preparation、nondemolition、記録追記、安全継続が有限共通精密化を保証する条件を比較する問題。

**次の問い。** この合成障害は内部／外部という位置関係から出るのか、それとも両者のインターフェース差から出るのか。

### Phase 7：内部／外部インターフェース同値

**当初の仮説。** 内部観測者には、外部観測者にはない固有の識別限界があるのではないか。

**なぜ魅力的に見えたか。** 内部観測者は対象と同じ状態空間に含まれ、測定反作用、有限記憶、自己言及、初期相関に曝されるためである。

**何によって壊れたか。** 内部と外部の制御器に、同じ入力、出力、記憶容量、コピー数、リセット可能性、敵対性、因果インターフェースを与えれば、両者が生成できる履歴集合は同じになる。外部方策の制御状態を内部状態へ埋め込み、内部制御を履歴依存方策として外部へ射影できるからである。

**撤回したもの。** [WITHDRAWN] `inside vs outside` という空間的位置だけを第一義的数学条件とすること。

**残ったもの。** [ESTABLISHED] 差を生むのは、fresh preparation、外部記憶、遮蔽された乱数、対象から隔離された計算、reset、操作可能範囲などのインターフェース非対称性である。外部観測者にこれらを与えなければ、内部反例は外部でも成立する。

**次の問い。** 「インターフェース因子化」という語の下で、因果的遮蔽と実験合成を混同していないか。

### Phase 8：interface factorization の分解

**当初の仮説。** 外部の分離実験族が一つの内部履歴を通じて因子化できないことが、内部観測限界の本体ではないか。

**なぜ魅力的に見えたか。** 因子化という語は、入力・出力チャネル、実験精密化、情報復号、内部状態の遮蔽を一つにまとめられるように見えた。

**何によって分解されたか。** 少なくとも次の二概念は別である。

#### Causal Interface Factorization (CIF)

観測者の内部コード・記憶・乱数 $C_t$ が、宣言された action channel $U_t$ を迂回して対象状態 $X_t$ に直接読まれず、対象から観測者への影響も宣言された observation channel $Y_t$ を通るという条件である。確率的な略記では、例えば

$$
P(X_{t+1},Y_t\mid X_t,U_t,C_t)
=
P(X_{t+1},Y_t\mid X_t,U_t)
$$

のような因子化を要求する。正確な条件は採用する因果グラフまたは構造方程式に依存する。

#### Experimental Amalgamation (EA)

複数の実験的識別情報を、一つの内部実現可能実験または適応履歴へ共通精密化できることである。

CIF と EA は互いに含意しない。二ビット破壊例では、コード漏洩がなく CIF が成立しても EA は失敗する。逆に、対象が方策コードを読めて CIF が失敗していても、十分な fresh preparation と共同測定があれば特定の実験族について EA が成立する場合がある。

**撤回したもの。** [WITHDRAWN] CIF と EA をともに `interface factorization` と呼び、一つの条件として扱うこと。

**残ったもの。** [ESTABLISHED] 因果的遮蔽の問題と、実験族の共通精密化の問題は、別々に検証しなければならない。

**次の問い。** 自己包含は CIF の失敗を強制するか。また乱数を導入すれば、方策依存の対角的環境を避けられるか。

### Phase 9：対角線、乱数、初期相関

**当初の仮説。** 世界が内部観測者の方策コードを含むなら、選ばれた方策を読んで必ず失敗させる対角的生成系を作れるため、内部方策には固有の限界があるのではないか。

**なぜ魅力的に見えたか。** 自己包含性を、単なる容量制約ではなく方策依存の不可能性へ接続できるように見えた。Wolpert 型推論装置との類似もあった。

**何によって限定されたか。** 外部環境に方策コードや乱数 seed が漏れていれば、同じ対角的応答を構成できる。逆に内部観測者でも、コードと private randomness が因果的に遮蔽されていれば、その反例は成立しない。したがって本体は内部性ではなく CIF の成否である。

候補クラス固定の規律にも注意が必要である。方策を見た後で adversary が新しい候補を追加する反例は許されない。対角例を使うなら、「方策コードを入力として読み、その値に応答する」という遷移規則を持つ候補生成系を、方策選択前に候補クラスへ含めなければならない。

乱数についても、単に「ランダム化したから adversary は読めない」とは言えない。必要なのは、例えば乱数 $R$ と環境側潜在変数 $\Lambda$ の適切な条件付き独立性、seed の秘匿、生成器の品質、初期相関の制御である。これらは private randomness、adversarial environment、initial correlation、causal shielding の問題へ分解される。

Bell 文脈の measurement independence

$$
P(\lambda\mid x,y)=P(\lambda)
$$

とは構造的類似があるが、一般の実験設計における初期相関の存在を直ちに superdeterminism と同一視してはならない。measurement dependence は、通常の共通原因、装置記憶、選択バイアス、seed 漏洩などでも起こりうる。Bell の局所隠れ変数モデルに固有の前提配置と、一般的な実験インターフェース監査は区別する。

**撤回したもの。** [WITHDRAWN] 自己包含だけから CIF の失敗または乱数独立性の失敗が従うという主張。

**残ったもの。** [SYNTHESIS] 自己包含が非自明になるのは、自己出力を含む query closure、真部分系記録容量、コード可視性、初期相関など、対象と観測者の結合条件を追加したときである。

**次の問い。** 単一の不可能定理ではなく、科学的識別が成立するための異なる前提を層として監査できるか。

---

## 5. What each failure taught us

各失敗は、元の問いを否定しただけでなく、混同していた論理層を分離した。

| 失敗した期待 | 修正後の教訓 | 現在の扱い |
|---|---|---|
| 非単射性から新しい存在論定理が得られる | 非単射性は識別不能の定義的核にすぎない | model class と experiment family を指定する |
| 内部性が非識別性を強制する | 同一インターフェースなら内部／外部差はない | 容量・自己問合せ・遮蔽条件を個別化する |
| 生成からログへの移行は必ず情報を失う | 情報損失は具体的チャネルについて証明が必要 | sufficiency、Blackwell order、coarse graining へ接続する |
| 資源極限でも一般にファイバーが残る | 極限挙動は候補クラスと収束概念に依存する | finite、generic、asymptotic、limit learning を分ける |
| ペア分離があれば単一履歴でも分離できる | 物理的共同実現には amalgamation が必要 | domain/interference obstruction を追跡する |
| 破壊的測定は内部性の徴候である | 同じ単一コピー制約なら外部でも失敗する | copy/reset/fresh preparation を明記する |
| interface factorization は一概念である | CIF と EA は独立である | 因果グラフと実験精密化を別々に監査する |
| 乱数で対角 adversary を避けられる | seed の秘匿と独立性自体が追加仮定である | private randomness と initial correlation を明示する |

この経緯から、現時点での焦点は「観測成功に存在論が含まれないことの証明」ではなく、**観測成功を生成構造の同定へ接続する前提を、どこまで個別に検査できるか**へ移った。

---

## 6. Existing theories that absorbed each conjecture

この問題は一つの新しい数学問題だったのではなく、複数分野で別々の名前を与えられていた問題群だった。以下は類似語の列挙ではなく、どの失敗をどの理論が吸収したかの対応である。

| 既存理論 | 吸収した段階・失敗 | 本ノートへの限定・教訓 |
|---|---|---|
| **Inverse problems** | Phase 1 の $O^{-1}(l)$ の一意性 | 一意性だけでなく存在性・安定性・正則化を区別する。単射でも逆が不安定なら実用的復元は壊れる |
| **Statistical identifiability** | 観測分布が異なるパラメータを区別するか | global/local/generic identifiability を分ける。識別可能性は指定モデル族の内部命題で、モデル族自体の正しさを証明しない |
| **System identification** | 入出力履歴から動的モデルを推定する Phase 4–6 | 入力の励起性、モデル次数、ノイズ、閉ループ性、可観測性など、成功に必要な条件を明示する |
| **Minimal realization** | 「完全な振る舞いでも生成子は一意でない」という一般化への反例 | 線形系では可制御・可観測な極小実現が相似変換を除き一意になる条件がある。存在論的非一意性はクラス依存 |
| **Myhill–Nerode / automata minimization** | Phase 1・4 の振る舞い同値類 | 正則言語には同型を除き一意な最小 DFA がある。完全な外的振る舞いと極小性が canonical generator を与えるクラスの代表例 |
| **Adaptive distinguishing sequences** | Phase 5 の $\forall\exists$ と $\exists\forall$ の差 | ペア識別可能でも preset/adaptive distinguishing sequence の存在は別問題。適応性、長さ、存在判定が既に研究されている |
| **Blackwell comparison** | Phase 3・6 の informational refinement | 一つの実験が別の実験の garbling かを比較する。ただし物理的に同じ試料上で共同実行できることまでは含意しない |
| **Sufficient statistics** | 「安定ログが生成情報を失う」という Phase 3 | 統計量が指定モデル・目的に関して情報を保存する条件を与える。「全存在論に十分」という無条件概念ではない |
| **Bisimulation / process testing** | 観測同値と内部状態差の区別 | 相互作用可能な過程の外的同値を定義し、商を構成する。非同型な実装差を何として数えるかを明示させる |
| **Active diagnosis** | Phase 5–6 の介入による候補縮約 | 診断可能領域へ移る条件付き制御計画、許容操作、制御と診断の結合を扱う。EA の応用上の近縁 |
| **Sequential/adaptive experiment design** | 単一適応履歴でどの実験を次に選ぶか | 情報獲得率、停止規則、誤り率を扱う。実験が常に安全・実行可能・再準備可能とは限らない |
| **Hellinger process / absolute continuity / singularity** | 「分布が違う」と「一履歴で完全分離できる」の混同 | 異なるが同値な確率測度は有限観測で重なりうる。相互特異性、contiguity、漸近分離を区別する必要がある |
| **Safe exploration** | Phase 6 の domain obstruction | 情報価値の高い行動でも、安全制約下では実行不能になりうる。安全方策集合は候補不確実性とともに定義される |
| **Learning in the limit / Gold** | Phase 4 の有限段階非識別と極限識別 | 各有限データでは候補が残っても、推測が極限で安定することがある。有限時点の一意性とは別概念 |
| **Query learning / Angluin** | 実験・問合せインターフェースが学習能力を変えること | membership/equivalence query など、利用可能な問合せ形式自体が識別可能性の前提である |
| **Latent model / HMM identifiability** | Phase 3–4 の隠れ生成子と出力過程の関係 | 非識別例だけでなく、rank・系列長などの条件下で generic identifiability も成立する。HMM 一般を非一意と断定できない |
| **Breuer self-measurement** | Phase 2 の内部自己測定直観 | 含む系の全状態を内部装置が区別する制約を与えるが、対象クラスと部分系への制限が不可欠。自己包含だけの定理として拡張しない |
| **Wolpert inference devices** | Phase 2・9 の対角的自己推論 | 自己出力を含む probe family と固定出力意味論の下で不可能性を得る。任意の有限候補識別へ自動的に拡張しない |
| **Causal graphs / d-separation / Markov blanket** | Phase 8–9 の CIF | コード、seed、対象状態、設定、出力の遮蔽・共通原因を明示する。グラフは因果仮定を可視化するが、データだけで一意に決まるとは限らない |
| **Measurement independence** | Phase 9 の設定と潜在状態の初期相関 | Bell 型推論での特定の独立仮定。一般の seed 漏洩や交絡と構造的に似るが、全てを superdeterminism と呼ばない |
| **No-cloning / no-broadcasting** | Phase 5–6 の copy/product interface | 未知量子状態の一コピーから普遍的な実験積を作れない場合がある。ただし同じ一コピー条件なら外部観測者にも等しく作用する |

二つの反対方向の先行結果を同時に保持することが重要である。一方では Myhill–Nerode や線形極小実現が、適切なクラスと極小性の下で生成子の一意性を回復する。他方では latent model の非識別、有限資源、自己測定、対角 query、safe exploration、no-cloning などが特定条件下の限界を示す。したがって「観測から生成構造は一意にならない」も「十分な観測なら必ず一意になる」も、クラス指定なしには成立しない。

---

## 7. Scientific identifiability prerequisite stack

### 7.1 一本の鎖ではなく、分岐をもつ前提構造

当初想定した直線

```text
world → experiments → records → identifiability
      → prediction success → ontological interpretation
```

は、そのままでは正しくない。予測成功は生成構造の完全識別なしにも成立し、識別可能性があっても有限標本で予測が成功するとは限らない。より安全な構造は次である。

```text
[fixed target class Ω and equivalence ≅]
                    │
                    ▼
[causal interface / shielding assumptions]
                    │
                    ▼
[available and safely executable experiments]
                    │
                    ▼
[reset / fresh preparation / repetition / excitation]
                    │
                    ▼
[joint realizability / experimental amalgamation]
                    │
                    ▼
[stable recording / memory / sufficient reduction]
                    │
                    ▼
[induced observational laws or process behaviours]
              ┌─────┴──────────┐
              ▼                ▼
 [identifiability and       [predictive adequacy
  inverse stability]         on a target domain]
              │                │
              └─────┬──────────┘
                    ▼
[model-class adequacy, causal semantics, minimality,
 symmetry quotient, bridge principles]
                    │
                    ▼
[ontological interpretation — defeasible, not automatic]
```

最下流の解釈は、上流の成功に機械的に含まれる出力ではない。一方で、上流条件が十分に確立され、候補クラスが適切で、分離と安定性が証明されている場合には、一意的解釈が合理的に支持されることを本ノートは否定しない。

### 7.2 前提スタック監査表

| 層 | 必要になるもの | 主な既存理論 | 外すと何が壊れるか | 観測結果だけで検証できるか |
|---|---|---|---|---|
| **0. Target specification** | 候補クラス $\Omega$、同型・ゲージ同値 $\cong$、識別対象 | model theory、realization theory、statistical modeling | ラベル違いを存在論差と誤認、または観測同値で結論を定義的に消去 | できない。比較言語と候補境界は方法論的選択を含む |
| **1. CIF / shielding** | コード・記憶・seed が宣言チャネルを迂回しない | causal graphs、d-separation、security/noninterference | 方策を読んで応答する環境、隠れフィードバック、初期相関 | 一般にはデータだけで完全検証できない。設計監査・介入・物理隔離が必要 |
| **2. Experiment availability** | 候補と両立する共通操作、校正済み介入 | active design、control、diagnosis | 区別に必要な操作が存在しない、または候補ごとに操作可否が異なる | 操作範囲は試験できるが、未試験候補まで含む全域性には仮定が残る |
| **3. Safe explorability** | 壊滅状態を避けながら情報領域へ到達可能 | safe exploration、viability、robust control | informative action が危険・不可逆で実行不能 | 安全包絡は部分的に検証可能だが、未知遷移に対する保証はモデル依存 |
| **4. Re-preparability / resetability** | 同じ $\theta$ に従う fresh preparation、reset、反復 | experimental design、ergodic/control assumptions | 破壊的実験を比較できない、順序依存が残る | 工学的試験は可能。ただし「同じ $\theta$ が再現された」は同一性仮定を含む |
| **5. Copy and independence** | コピー間で候補が保存され、ノイズ・設定・seed の相関が管理される | probability、causal inference、quantum information | 擬似反復、adversarial correlation、no-cloning による product failure | 独立性は統計的に反証できる場合があるが、有限データから完全証明はできない |
| **6. Persistent excitation** | 候補差が出力へ現れる入力系列 | system identification、adaptive control | モデル差が未励起方向に隠れる | 採用モデル内では rank 等を確認可能。モデル外の全差異を保証しない |
| **7. Experimental amalgamation** | ペア実験の共通精密化、履歴間の記録保存 | automata testing、active diagnosis、Blackwell refinement | $\forall\theta\neq\theta'\exists e$ から $\exists\sigma\forall\theta\neq\theta'$ が出ない | 有限モデルでは合成探索可能な場合がある。物理的全実現性は別途検証が必要 |
| **8. Stable recording** | 結果が比較可能な形で保持される記憶、時刻、参照系 | metrology、information theory、sufficient statistics | 後続実験が過去ログを消す、圧縮が識別情報を落とす | 記録媒体は検査できるが、「十分性」は候補モデルと目的に相対的 |
| **9. Statistical separation** | 異なる候補が異なる law/support を与える | identifiability、testing、Hellinger/likelihood theory | 分布一致なら統計的非識別、support 重複なら一回の zero-error 分離不能 | 指定モデル内で解析可能。有限データだけでは分布同一性・相違を確定できない |
| **10. Inverse stability** | 小さなログ誤差が巨大な構造差へ増幅されない | inverse problems、regularization | 数学的一意性があっても実用復元不能 | 条件数・連続性はモデル内で解析可能。モデル誤指定には別監査が必要 |
| **11. Predictive validation** | 対象領域・損失・分布移動を明示した成功 | statistics、learning theory、forecast evaluation | interpolation を世界全体の支持と誤認、分布外で破綻 | 指定された評価領域では検証可能。領域選択自体は成功から出ない |
| **12. Ontological bridge** | model-class adequacy、因果意味論、極小性、対称性商、競合理論比較 | philosophy of science、causal inference、realization theory | 予測的商を唯一の生成構造と誤認 | 観測だけで自己証明されないが、独立実験・統合・説明力で支持を強められる |

### 7.3 スタックは必要条件の固定リストではない

この表の全項目が全科学分野で常に必要という意味ではない。例えば天文学では対象の reset が不可能でも、自然に生じる多数の事例や時間発展が代替する。量子状態 tomography では fresh preparation の意味が重要だが、単一の歴史的事象の因果推論では再準備を別の仮定で置き換える。したがって「前提スタック」は、普遍的公理列ではなく、**どの層を別の何で代替したかを記録する監査テンプレート**である。

---

## 8. From predictive success to ontological interpretation

### 8.1 予測成功と識別可能性は別である

予測成功は、候補クラスの完全識別を必要としない。異なる内部構造が同じ予測分布を与える場合、予測に必要なのは観測同値類または predictive quotient だけである。逆に、モデルパラメータが理論上識別可能でも、データ不足、ノイズ、分布移動、逆問題の不安定性により予測が失敗しうる。

したがって一般には、

$$
\text{predictive success}
\not\Rightarrow
\text{generative identifiability},
$$

かつ

$$
\text{identifiability}
\not\Rightarrow
\text{finite-sample predictive success}.
$$

これは「予測成功は存在論と無関係」という意味ではない。複数の独立領域で、厳しい介入テストに耐え、競合モデルを排除する予測成功は、世界構造を捉えている強い証拠になりうる。ただし、どの候補を競合に含めたか、実験が候補差を励起したか、再準備や独立性が成立したか、観測同値を超える解釈原理を何に置いたかは、成功スコアそのものとは別に監査される。

### 8.2 「道具の真理不在性」の暫定定義

以上を踏まえ、本ノートでは作業概念を次のように精密化する。

> 観測・予測・計算の成功は、世界の何らかの構造を捉えている強い証拠になりうる。しかし、その成功だけから、使用した候補記述、実験可能性、再準備、独立性、共同実現可能性、記録十分性、因果的遮蔽、極小性規準などが、世界の存在構造を一意に定めるための正しい条件であることまでは導かれない。

従って、

> 真理が観測成功の中に「存在しない」のではない。観測成功だけでは、観測成功を生成構造へ接続する補助条件まで同時に自己証明されない。

これは数学的定理ではなく [SYNTHESIS] としての監査原理である。論理式で略記するなら、補助条件群を $A$、成功事実を $S$、一意的生成解釈を $U$ として、一般に

$$
A\land S\Rightarrow U
$$

を示せる個別クラスがあっても、

$$
S\Rightarrow A
$$

は成功の定義だけからは出ない、という主張である。$A$ の一部が別の観測や工学的検証によって支持されることは否定しない。

---

## 9. What can currently be claimed

### 9.1 現時点で言えること

- **[ESTABLISHED]** 観測・予測成功と生成構造の一意的識別は、論理的に同じ命題ではない。
- **[ESTABLISHED]** 両者を接続するには、候補クラス、同値基準、実験族、識別可能性などの補助条件が必要である。
- **[ESTABLISHED]** 非単射観測写像の非一意性は既知かつ初等的であり、それ自体は新定理ではない。
- **[ESTABLISHED]** 内部観測一般の普遍的不可能性は成立しない。自己包含的でありながら自己状態または候補を符号化できる系が構成できる。
- **[ESTABLISHED]** 同一の因果・資源インターフェースを与えれば、内部／外部という位置関係だけでは識別能力差は生じない。
- **[ESTABLISHED]** ペア分離と一つの大域適応方策の存在は異なる。両者の差は実験の共通精密化、継続可能性、記録保存に依存する。
- **[ESTABLISHED]** informational refinement と physical joint realizability は異なる。
- **[ESTABLISHED]** 決定的有限オートマトンや線形極小実現のように、適切な条件下で振る舞いが生成子を同型を除き一意に定めるクラスがある。
- **[ESTABLISHED]** latent-variable model、自己測定、推論装置、safe exploration、量子コピー制約などには、それぞれ異なる条件付き限界がある。
- **[SYNTHESIS]** 科学実験は再準備、反復、隔離、校正、安定記録、比較、励起、誤差制御によって識別条件を工学的に成立させていると整理できる。
- **[SYNTHESIS]** これらの条件を一つの前提スタックとして監査することには、少なくとも説明上・方法論上の価値がある。

### 9.2 現時点では言えないこと

- **[WITHDRAWN]** 真理そのものが存在しない。
- **[WITHDRAWN]** 科学は真理へ到達できない。
- **[WITHDRAWN]** 内部観測者は原理的に世界を識別できない。
- **[WITHDRAWN]** 観測・予測成功から存在論的一意性が常に排除される。
- **[WITHDRAWN]** 生成からログへの変換があるだけで、情報損失または非同型性が従う。
- **[WITHDRAWN]** measurement independence の破れは常に superdeterminism である。
- **[WITHDRAWN]** 今回の統合が数学的に新規である。
- **[WITHDRAWN]** 既存科学の存在論的推論が一般に誤っている。
- **[WITHDRAWN]** VED がこの議論によって正しいと証明される。
- **[WITHDRAWN]** VED が標準科学で評価しづらいことだけで、その内容が正当化される。

---

## 10. Relation to VED

**この研究ノートは VED を証明しない。** また、VED を通常の識別・予測・検証要件から免除しない。本ノートの各主張は VED の公理や生成図式とは独立に成立または失敗する。

限定的に言えるのは次だけである。

> 通常の科学的評価が、既に実験可能性、記録、再準備、識別可能性、因果的遮蔽などが成立した層を前提としているなら、それ以前の生成条件を対象とする理論が既存の評価軸に乗りにくい可能性を考えるための地図にはなる。

しかし「評価軸に乗りにくい」ことは、理論が正しいことの証拠ではない。むしろ、その理論が前提スタックのどの層を再構成し、どの代替的検証可能性を提供するかを明示する追加責任を生む。

---

## 11. Value of rearrangement rather than novelty

個々の部品が既知であっても、それらを「観測成功から存在論的解釈へ進むための前提スタック」として並べ直すことに独立した価値があるか。現時点の評価は次の通りである。

| 評価区分 | 現時点の判定 | 理由 |
|---|---|---|
| **trivial repackaging** | 個別の非単射命題・有限共通精密化命題には該当 | 写像の非単射、有限分離族の積、容量の鳩ノ巣原理は新規内容ではない |
| **useful synthesis** | **該当する可能性が高い** | inverse problems、automata testing、causal shielding、safe exploration、self-measurement を一つの失敗履歴へ対応づけると、混同箇所が見えやすい |
| **methodological contribution** | **条件付きで該当** | CIF/EA の分離、候補クラス事前固定、informational/physical refinement の分離を、実際の理論監査手順にできるなら有用 |
| **potentially publishable synthesis** | **現状では未達、発展余地あり** | 系統的文献レビュー、複数の具体的ケーススタディ、用語の先行使用調査、反証可能な監査プロトコルが必要 |
| **unsupported overreach** | 「真理不在の定理」「内部観測の普遍的不可能性」として発表する場合に該当 | 既知結果を超える一般定理がなく、反例クラスも明確である |

したがって、現時点で守れる価値は「新しい定理」ではなく、**異なる分野に分散した前提を、存在論的推論の監査順序へ再配置する useful synthesis** である。これを研究上の貢献へ高めるには、単なるチェックリストではなく、具体的な科学事例に適用して、どの層が実際に独立検証され、どの層が慣行的仮定として残っているかを示す必要がある。

---

## 12. Open questions

1. **[OPEN] 確率過程における EA の正確な定義。** Blackwell refinement、support separation、相互特異性、漸近識別を、物理的履歴合成とどう接続するか。
2. **[OPEN] 内生的実験集合の数学的構造。** partial category、effectus、game semantics、controlled transition system のどれが domain obstruction と interference obstruction を最も自然に表すか。
3. **[OPEN] Pairwise-to-global の境界。** 無限候補、無限履歴、位相的コンパクト性、計算可能方策、有限記憶制約の下で、どの amalgamation/compactness 条件が十分または必要か。
4. **[OPEN] CIF の経験的監査可能性。** コード漏洩、seed 相関、隠れフィードバックを、装置設計・因果介入・セキュリティ検証の組合せでどこまで排除できるか。
5. **[OPEN] 再準備の同一性。** 「同じ生成構造 $\theta$ の fresh sample」という仮定を、どのレベルで操作的に保証し、どのレベルでモデル仮定として受け入れているか。
6. **[OPEN] 予測的同値と存在論的同値。** minimal realization、causal abstraction、gauge quotient、latent-variable equivalence の間に共通の比較枠組みを作れるか。
7. **[OPEN] 逆安定性の位置。** 一意性があるが極端に不安定な逆問題を、存在論的一意性の成功例と数えるべきか、実践的非識別として別分類すべきか。
8. **[OPEN] 科学事例への適用。** 系同定、量子 tomography、天文学的逆問題、分子系統推定などで前提スタックを実際に監査し、単なる一般論を超えられるか。
9. **[OPEN] 用語選択。** 「道具の真理不在性」を維持する利益が誤読リスクを上回るか。「道具的成功の非自己証明性」へ改名すべきか。
10. **[OPEN] 新規性監査。** science studies、robustness analysis、experimental epistemology、underdetermination 論に、同等の前提スタックが既に提示されていないか、系統的調査が必要である。

---

## 13. Revision status

### Established / comparatively secure

- 非単射観測写像から一意復元できないことは初等的である。
- 候補クラスと構造同値関係は、方策選択前に固定しなければならない。
- 自己包含だけから普遍的非識別可能性は導けない。
- 同じ因果・資源インターフェースなら、内部／外部という位置だけで識別能力差は生じない。
- ペア分離と大域適応分離は異なり、その接続には共通精密化または同等の合成条件が必要である。
- CIF と EA は異なる概念である。
- 予測成功、統計的識別可能性、生成子の一意性、存在論的解釈は異なる主張である。
- 一意な極小実現が存在するクラスと、非識別性が残るクラスの両方がある。

### Interpretive synthesis

- 実験可能性、再準備、リセット、記憶、独立性、EA、識別可能性、逆安定性を「科学的識別可能性の前提スタック」として読むこと。
- 「道具の真理不在性」を、真理の不存在ではなく、道具的成功の存在論的非自己証明性として読むこと。
- 科学実験を、スタックの条件を工学的に構成・維持する実践として捉えること。
- 異分野の既存理論を、観測成功から存在論へ進む異なる矢印の監査理論として対応づけること。

### Working hypotheses

- CIF/EA/recording/identifiability を分離した監査表が、具体的な理論比較で実用的な診断力を持つ。
- 内生的な実験の部分合成構造を形式化することで、既存の active diagnosis と causal-interface analysis の間に有用な橋を作れる。
- 「補助条件は成功によって自己証明されない」という定式化が、従来の underdetermination 論より操作的な議論を可能にする。

### Withdrawn claims

- 「観測写像の存在論的非一意性定理」が新しい一般定理である。
- 生成からログへの段階が存在すれば、生成構造とログは必ず非同型になる。
- 自己包含する内部観測者は原理的に全世界を識別できない。
- 資源を無限に増やしても存在論的ファイバーが一般に残る。
- 二ビット破壊例が内部観測者に固有の不可能性を示す。
- 内部性そのものが interface factorization の失敗を生む。
- CIF と experimental amalgamation は同じ条件である。
- 乱数化だけで方策依存 adversary を排除できる。
- 観測成功は存在論的一意性を常に排除する。
- 本検討が VED の正しさを支持または証明する。

### Open questions

上記 §12 を現行の課題表とする。新しい反例または先行研究が見つかった場合、まず該当する Phase、前提スタックの層、主張状態タグを更新し、結論だけを上書きしない。

### Revision protocol

今後の改訂では、各変更に次を記録する。

1. 変更前の主張。
2. 反例、証明、または先行研究。
3. 影響を受ける Phase とスタック層。
4. `ESTABLISHED / SYNTHESIS / HYPOTHESIS / WITHDRAWN / OPEN` の状態変更。
5. VED との関係に変更がないか。

本ノートの目標は最終結論の保存ではなく、**訂正可能な依存関係と撤回理由の保存**である。

---

## 14. References

以下は完全な文献レビューではなく、各失敗を吸収した理論への起点である。今後、分野別レビューと一次文献の追加監査が必要である。

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

---

## Closing note

本ノートが保存しようとするのは、整った最終理論ではない。観測写像の非単射性から始まった一般定理への期待が、完全観測、自己記述可能系、極小実現の一意性、外部にも成立する破壊的反例、因果インターフェースの同値性によって順番に崩れ、そのたびに問いがより限定された条件問題へ移った過程である。

現時点での最小限の結論は次である。

> 観測・予測成功は生成構造を強く支持しうるが、その成功は、候補クラス、実験可能性、再準備、独立性、共同実現可能性、記録、識別可能性、逆安定性、存在論的橋渡しを自動的には自己証明しない。この指摘は普遍的不可能定理ではなく、既存理論に分散した前提を明示するための訂正可能な監査枠組みである。
