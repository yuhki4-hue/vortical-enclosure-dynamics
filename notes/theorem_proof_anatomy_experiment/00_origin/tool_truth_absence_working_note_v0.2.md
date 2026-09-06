# 道具的成功の存在論的非自己証明性

## 旧作業名「道具の真理不在性」— 観測・予測成功と存在論的一意性のあいだにある条件群

- **副題:** 観測写像の非一意性仮説から、科学的識別可能性の前提ネットワークへ
- **English title:** *Instrumental Success and Ontological Non-Self-Certification: A Working Note on the Prerequisite Network of Scientific Identifiability*
- **Alternative English title:** *From Non-Injective Observation Maps to the Prerequisite Network of Scientific Identifiability*
- **Status:** working note / corrigible synthesis / not a theorem announcement
- **Version:** 0.2
- **Date:** 2026-08-16
- **Relation to VED:** independent methodological note; not evidence for VED
- **Structural caution:** 「前提スタック」は v0.1 以来の作業名であり、固定された線形階層を意味しない。v0.2 では原則として「前提ネットワーク」または「監査ネットワーク」と呼ぶ。

---

## 1. Abstract

本ノートは、観測・予測の成功と生成構造の一意的同定との関係をめぐって行われた一連の検討を、成功した結論ではなく、失敗・撤回・問題分解の履歴として再構成する。当初は、観測写像の非単射性、観測者の内部性、生成から安定ログへの変換などから、存在論的一意性に関する一般的不可能定理を得られるのではないかと考えた。しかし、非単射性は逆問題と識別可能性の初等的事実に対応し、自己包含性だけから非識別可能性は導けず、生成―ログ非同型性も情報損失を定義へ埋め込めば循環することが判明した。さらに、決定的有限オートマトンや線形系の極小実現では、完全な振る舞いから同型を除く一意性が回復するクラスが存在するため、クラス非依存の一般命題は維持できなかった。

その後、問題は、各候補対を分離する反実験族と、一つの物理的に実現可能な適応履歴との違いへ移った。ここでも、単一コピー上の破壊的測定がもたらす障害は内部観測者に固有ではなく、同じ単一コピー制約を外部観測者に課せば再現する。v0.1 はここから一般的な内部／外部インターフェース同値を `[ESTABLISHED]` としたが、v0.2 はこれを撤回する。完全に同一の実現可能インターフェースを定義すれば履歴集合が一致するという規約的事実と、特定の制御系モデルで内部・外部制御器を対応づける条件付き結果を分離する。残る弱い教訓は、`inside/outside` というラベル単独から識別能力差を導けない、ということに限られる。

本ノートは、これらを「科学的識別可能性の前提ネットワーク」として並べ直す。ただし、これは新しい普遍定理でも、固定された前提階層でもない。個々の条件は inverse problems、statistical identifiability、system identification、automata testing、Blackwell comparison、bisimulation、active diagnosis、safe exploration、causal inference、self-measurement、inference-device theory、量子情報などで研究されている。Duhem–Quine、constructive empiricism、unconceived alternatives、experimenter's regress、models of data、severe testing などにも強い哲学的近縁がある。正確な系譜や同値性は未監査であり、概念的新規性は主張しない。本ノートの暫定的価値は、各条件の役割・代替関係・独立監査可能性と、それを見落とした失敗履歴を同じ文書で追跡することにある。

---

## Changes from v0.1

### Downgraded

- **内部／外部インターフェース同値:** 一般的な `[ESTABLISHED]` を撤回した。完全なインターフェース同一化による規約的同値と、明示的な離散時間・ターン制制御モデルでのみ検討できる条件付き対応へ分解した。
- **Pairwise-to-global:** 一般形を撤回し、固定有限候補・決定論的実験・任意後処理では成立する情報的因子化と、無限・確率的・計算制約付きの場合の未解決問題を分けた。
- **方法論的新規性:** 「methodological contribution の可能性あり」から、ケーススタディで診断力が示されるまで未実証、へ降格した。

### Clarified

- **Title choice (Option A):** 主題を「道具的成功の存在論的非自己証明性」へ改名し、「道具の真理不在性」を旧作業名として括弧的位置に残した。
- **CIF と preparation/initial independence:** 動的な因果遮蔽と、seed・setting・preparation・潜在変数の初期相関を別項目にした。
- **内部観測者と単一履歴実現可能性:** `internal observer` は世界の部分系としての観測者だけに予約し、`internally realizable` は `single-history realizable` または「単一履歴実現可能」へ改称した。
- **実験精密化:** informational refinement、Blackwell refinement、physical joint realizability、sequential composability、product experiment、adaptive global separator を別概念として明記した。
- **哲学的先行研究:** exact match を主張せず、近縁、反例、語彙供給、部分的被覆の別を導入した。

### Added

- **候補クラス充足性:** within-model identifiability と、真の生成構造が候補クラスに含まれるかという model-class adequacy / realizability を分離した。
- **哲学・科学方法論の先行層:** Duhem–Quine、van Fraassen、Stanford、Collins、Suppes、Mayo、Bogen–Woodward、Hacking、Manski、causal identification、model misspecification を追加した。
- **前提ネットワークの役割:** target specification、prerequisite、enabling condition、substitute condition、robustness condition、identification condition、interpretive bridge を付した。
- **補助条件の独立監査可能性:** independently testable、design-certified、model-relative、only indirectly constrained、circularly entangled with success criterion の区別を追加した。

### Preserved

- Phase 0–9 の失敗履歴と撤回理由。
- 主張状態タグと「言えること／言えないこと」の分離。
- 訂正を先に置き、失敗した主張を削除しない方法。
- VED からの独立性。
- 自己包含だけから普遍的な内部観測不可能性は導けない、という結論。

### Review handling note

この改訂は Claude Code 査読を revision input として用いたが、その系譜判断を権威として採用していない。「中心命題は Duhem–Quine と Collins そのものである」「Suppes が直接の祖先である」「Mayo が同じ監査プログラムを完成済みである」「M-closed/M-open が完全に対応する」といった強い読みは採用せず、`[OPEN: literature audit]` とした。主要コメントごとの処理は別紙 `tool_truth_absence_v0.1_to_v0.2_diff.md` に記録する。

---

## 2. Scope and terminology

### 2.1 旧作業名「真理不在性」の限定

本ノートにおける「真理不在性」は、**真理そのものが存在しない**という主張ではない。また、**観測や予測から生成構造へ原理的に到達できない**という普遍的不可能性でもない。

暫定的には、次の監査上の主張を指す。

> 観測・予測・計算の成功それ自体には、その成功を唯一の存在論的世界像へ接続するために用いられた補助条件の正当性までは含まれていない。

短く言えば、

> 「当たる」という事実だけの中に、「世界は唯一このようである」を保証する条件すべてが含まれているわけではない。

したがって旧称の「不在」とは、対象世界からの真理の欠落ではなく、**道具的成功の自己証明能力の不在**を指す。v0.2 は主題を「道具的成功の存在論的非自己証明性」へ改名し、「道具の真理不在性」は失敗履歴を保存する旧作業名としてのみ残す。

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

Bayesian model comparison の M-closed/M-open や model misspecification はこの区別に近い語彙を供給するが、生成構造の存在論的包含と完全に同じ概念であるとはまだ確認していない。Stanford の unconceived alternatives も候補外の可能性を考える強い近縁だが、本ノートとの正確な対応は `[OPEN: literature audit]` とする。

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

## 5. What each failure taught us

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

## 6. Existing theories: correspondences, counterexamples, and partial coverage

### 6.1 数学・統計・計算・物理における対応

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
| **Breuer self-measurement** | partially constrains / supplies counterexample under assumptions | Phase 2 の自己測定直観 | 部分系状態への制限など追加条件がある。自己包含だけの一般定理へ拡張しない |
| **Wolpert inference devices** | provides close analogue / conditional impossibility | Phase 2・9 の対角的自己推論 | probe family と出力意味論を固定した不可能性であり、任意の有限候補識別とは同一でない |
| **Causal graphs / d-separation / Markov blanket** | supplies formal vocabulary | Phase 8 の動的 CIF と Phase 9 の共通原因 | 変数分解と因果仮定に相対的であり、グラフがデータだけから一意に得られるとは限らない |
| **Measurement independence** | special-case correspondence | Phase 9 の setting と潜在状態の初期相関 | Bell 型推論における特定の独立仮定。一般の seed 漏洩・交絡と同一視せず、superdeterminism の同義語にしない |
| **No-cloning / no-broadcasting** | quantum special-case counterexample | Phase 5–6 の product/copy failure | 量子候補クラスに固有の制約である。incompatibility、contextuality、one-copy limitation と混同せず、普遍的前提にしない |

二つの反対方向を同時に保持する必要がある。Myhill–Nerode や線形極小実現は、適切なクラスと極小性の下で生成子の一意性を回復する。他方、latent model の非識別、有限資源、自己測定、対角 query、safe exploration、量子クラスにおける copy 制約は、それぞれ限定された限界を示す。したがって「観測から生成構造は一意にならない」も「十分な観測なら必ず一意になる」も、クラス指定なしには成立しない。

### 6.2 科学哲学・科学方法論における先行形

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

---

## 7. Scientific Identifiability Prerequisite Network

### 7.1 「スタック」は固定階層ではない

「前提スタック」は検討履歴を保存する作業名として残すが、v0.2 では **科学的識別可能性の前提ネットワーク**と呼ぶ。availability、safety、reset、fresh preparation、copy、persistent excitation、separation は常に直列に並ぶ必要条件ではない。一部は目的、一部は実現機構、一部は互いの代替、一部は robustness 条件である。

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

### 7.2 前提ネットワーク監査表

`auditability` は、`independently testable`、`design-certified`、`model-relative`、`only indirectly constrained`、`circularly entangled with success criterion` の五分類を基本語彙とする。一つの項目に複数の性格がありうる。

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

### 7.3 代替・支援・特殊条件を区別する

この表の全項目が全科学分野で常に必要という意味ではない。対象の reset が不可能でも、自然に生じる複数事例や長い時間発展が、適切な同質性・定常性仮定の下で代替する場合がある。ただし、それらが同じ $\theta$ または同じ population law に従うことは追加条件である。量子状態 tomography では fresh preparation の意味が重要になりうる一方、no-cloning、測定 incompatibility、contextuality、単一コピー制約は別々の論点である。歴史的一回事象の因果推論では、再準備の代わりに比較対象、自然実験、構造仮定を用いることがある。

従ってこのネットワークは普遍的公理列ではなく、**何が目的で、何が前提で、何が実現機構・代替・robustness 条件であり、それぞれを成功基準から独立にどこまで監査したかを記録するテンプレート**である。

---

## 8. From predictive success to ontological interpretation

### 8.1 予測成功と識別可能性は別である

予測成功は、候補クラスの完全識別を必要としない。異なる生成構造が同じ予測分布を与える場合、予測に必要なのは観測同値類または predictive quotient だけである。逆に、モデルパラメータが理論上識別可能でも、データ不足、ノイズ、分布移動、逆問題の不安定性により予測が失敗しうる。さらに within-model で一意でも $\theta_\star\notin\Omega$ なら、その一意性は候補クラスの adequacy を保証しない。

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

### 8.2 「存在論的非自己証明性」の暫定定義

以上を踏まえ、本ノートでは作業概念を次のように精密化する。

> 観測・予測・計算の成功は、世界の何らかの構造を捉えている強い証拠になりうる。しかし、その成功だけから、使用した候補記述、実験可能性、再準備、独立性、共同実現可能性、記録十分性、因果的遮蔽、極小性規準などが、世界の存在構造を一意に定めるための正しい条件であることまでは導かれない。

従って、

> 真理が観測成功の中に「存在しない」のではない。観測成功だけでは、観測成功を生成構造へ接続する補助条件まで同時に自己証明されない。

これは数学的定理ではなく [SYNTHESIS] としての監査原理である。「道具の真理不在性」は、この ontological non-self-certification を指した旧作業名としてだけ残す。名称自体が真理不存在を連想させる過剰なものだったため、v0.2 の主題名には採用しない。

論理式で圧縮するなら、補助条件群を $A$、成功事実を $S$、一意的生成解釈を $U$ として、個別クラスで

$$
A\land S\Rightarrow U
$$

を示せても、

$$
S\Rightarrow A
$$

は成功の定義だけからは出ない、という記法になる。しかし、形式化された限りでこれは命題論理上の初等的な指摘にすぎず、数学的結果として数えない。$A$ を都合よく成功から独立と定義すれば、結論を定義へ埋め込むだけにもなる。

非自明な研究課題は $A=\bigwedge_i A_i$ の各成分について、次を個別に問うことである。

1. $A_i$ は成功判定 $S$ から独立した試験で検証できるか。
2. 装置構成・乱数化・隔離によって design-certified と言えるか。
3. $A_i$ は候補クラスまたは因果変数分解にのみ相対的か。
4. 反例探索や外部妥当性から only indirectly constrained されるだけか。
5. $A_i$ の採否と成功基準が circularly entangled していないか。

この**補助条件の独立監査可能性**が v0.2 の主問題である。$A_i$ の一部が別の観測や工学的検証によって強く支持されることは否定しないし、その成功を軽視する理由にもならない。

---

## 9. What can currently be claimed

### 9.1 現時点で言えること

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
- **[SYNTHESIS]** 科学実験は再準備、反復、隔離、校正、安定記録、比較、励起、誤差制御によって識別条件を工学的に成立させていると整理できる。
- **[SYNTHESIS]** これらの条件を、固定階層ではない前提ネットワークとして監査することには説明上の価値がありうる。方法論的な診断力はケーススタディ前には未実証である。

### 9.2 現時点では言えないこと

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
- **[WITHDRAWN]** 既存科学の存在論的推論が一般に誤っている。
- **[WITHDRAWN]** VED がこの議論によって正しいと証明される。
- **[WITHDRAWN]** VED が標準科学で評価しづらいことだけで、その内容が正当化される。

---

## 10. Relation to VED

**この研究ノートは VED を証明しない。** また、VED を通常の識別・予測・検証要件から免除しない。本ノートの各主張は VED の公理や生成図式とは独立に成立または失敗する。この監査ネットワークは VED に限らず、「既存の評価軸より前段の生成条件を扱う」と自己記述する任意の理論へ対称的に適用される。

限定的に言えるのは次だけである。

> 通常の科学的評価が、既に実験可能性、記録、再準備、識別可能性、因果的遮蔽などが成立した層を前提としているなら、それ以前の生成条件を対象とする理論が既存の評価軸に乗りにくい可能性を考えるための地図にはなる。

しかし、標準評価軸に乗りにくいことそれ自体は、その理論への証拠的支持を**一切与えない**。むしろ、その理論が前提ネットワークのどのノードを再構成し、どの代替的検証可能性を提供するかを明示する追加責任を生む。この基準は VED に有利にも不利にも特別扱いされない。

---

## 11. Value of rearrangement rather than novelty

個々の部品が既知であっても、それらを「観測成功から存在論的解釈へ進むための前提ネットワーク」として並べ直すことに独立した価値があるか。現時点の評価は次の通りである。

| 評価区分 | 現時点の判定 | 理由 |
|---|---|---|
| **trivial repackaging** | 個別の非単射命題・有限共通精密化命題には該当 | 写像の非単射、有限分離族の積、容量の鳩ノ巣原理は新規内容ではない |
| **mathematical novelty** | **低い** | 中心論理、非単射性、有限決定論的な結合署名は初等的で、各条件問題にも既存理論がある |
| **conceptual novelty** | **低め／未確定** | underdetermination、constructive empiricism、experimenter's regress、models of data、severe testing 等との体系的比較が未了である |
| **useful synthesis** | **維持可能** | inverse problems、automata testing、causal shielding、safe exploration、self-measurement と哲学的先行形を一つの失敗履歴へ対応づけると、混同箇所が見えやすい |
| **methodological contribution** | **未実証** | CIF/EA、初期独立性、候補クラス adequacy、informational/physical refinement の分離が、具体的事例で診断を変えるかまだ示していない |
| **potentially publishable synthesis** | **現状では主張しない** | 系統的文献レビュー、複数ケースの比較、用語史、再現可能な監査手順が必要 |
| **unsupported overreach** | 「真理不在の定理」「内部観測の普遍的不可能性」として発表する場合に該当 | 既知結果を超える一般定理がなく、反例クラスも明確である |

したがって、現時点で守れる価値は「新しい定理」ではなく、**異なる分野に分散した前提候補を、存在論的推論の監査ネットワークへ再配置する useful synthesis** である。これが trivial repackaging を超えるかは未決着である。次の価値検証は、ネットワークを具体的科学事例へ適用し、どの条件が独立試験、設計保証、モデル相対的解析、間接制約、成功基準との循環のどれに当たるかを比較することである。

---

## 12. Open questions

1. **[OPEN] 確率過程における EA の正確な定義。** Blackwell refinement、support separation、相互特異性、漸近識別を、物理的履歴合成とどう接続するか。
2. **[OPEN] 内生的実験集合の数学的構造。** partial category、effectus、game semantics、controlled transition system のどれが domain obstruction と interference obstruction を最も自然に表すか。
3. **[OPEN] Pairwise-to-global の境界。** 無限候補、無限履歴、位相的コンパクト性、計算可能方策、有限記憶制約の下で、どの amalgamation/compactness 条件が十分または必要か。
4. **[OPEN] CIF の経験的監査可能性。** 動的なコード漏洩と隠れ feedback を、装置設計・因果介入・security verification の組合せでどこまで排除できるか。因果変数分解の選択自体をどう監査するか。
5. **[OPEN] Preparation / initial independence の監査。** seed・setting・潜在状態の初期相関と共通原因を、randomization、negative control、設計履歴によってどこまで CIF とは独立に制約できるか。
6. **[OPEN] 再準備の同一性。** 「同じ生成構造 $\theta$ の fresh sample」という仮定を、どのレベルで操作的に保証し、どのレベルでモデル仮定として受け入れているか。
7. **[OPEN] Candidate-class adequacy。** $\theta_\star\in\Omega$ を仮定せず、近似識別、partial identification、misspecification diagnostics、候補クラス拡張をどう組み合わせるか。
8. **[OPEN] 予測的同値と存在論的同値。** minimal realization、causal abstraction、gauge quotient、latent-variable equivalence の間に共通の比較枠組みを作れるか。
9. **[OPEN] 逆安定性の位置。** 一意性があるが極端に不安定な逆問題を、存在論的一意性の成功例と数えるべきか、実践的非識別として別分類すべきか。
10. **[OPEN] 科学事例による診断力の試験。** system identification、quantum state tomography、cosmological inverse problems、phylogenetic inference、nonequilibrium / irreversible experiments に同じ監査ネットワークを適用する。これらを問題分野と先に断定するのではなく、異分野で同じ分類が実際に見落としを発見し、推論を変更するかを試す。
11. **[OPEN: literature audit] 哲学・方法論上の新規性監査。** Duhem–Quine、van Fraassen、Stanford、Collins、Suppes、Mayo、Bogen & Woodward、Hacking、Manski および model misspecification 文献との exact / partial / merely analogous の境界を一次文献と専門的二次文献で系統監査する。
12. **[OPEN] 用語の継続監査。** v0.2 は「道具的成功の存在論的非自己証明性」へ改名した。旧称を履歴表示として残す利益が、なお真理不存在という誤読リスクを上回るかを今後も見直す。

---

## 13. Revision status

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

### Interpretive synthesis

- 実験可能性、再準備、reset、記憶、独立性、EA、識別可能性、逆安定性を、役割と代替関係をもつ「科学的識別可能性の前提ネットワーク」として読むこと。
- 「道具の真理不在性」を、真理の不存在ではなく、道具的成功の存在論的非自己証明性として読むこと。
- 科学実験を、ネットワーク中の条件を工学的に構成・維持する実践として捉えること。
- 異分野の既存理論を、観測成功から存在論へ進む異なる矢印の監査理論として対応づけること。

### Working hypotheses

- CIF、initial independence、EA、recording、identifiability、candidate-class adequacy を分離した監査表が、具体的な理論比較で実用的な診断力を持つ。
- 内生的な実験の部分合成構造を形式化することで、既存の active diagnosis と causal-interface analysis の間に有用な橋を作れる。
- 補助条件を auditability 別に分類することが、既存の underdetermination・severe testing・models of data 等の議論に対して追加の操作的診断を与える。[OPEN: literature audit and case studies]

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
- 乱数化だけで方策依存 adversary を排除できる。
- 観測成功は存在論的一意性を常に排除する。
- 中心命題の命題論理的略記が新しい数学的結果である。
- 哲学側の系統監査なしに概念的新規性または方法論的貢献を主張できる。
- 本検討が VED の正しさを支持または証明する。

### Open questions

上記 §12 を現行の課題表とする。新しい反例または先行研究が見つかった場合、まず該当する Phase、前提ネットワークのノード・役割・依存、主張状態タグを更新し、結論だけを上書きしない。

### Revision protocol

今後の改訂では、各変更に次を記録する。

1. 変更前の主張。
2. 反例、証明、または先行研究。
3. 影響を受ける Phase と前提ネットワークのノード・依存関係。
4. `ESTABLISHED / SYNTHESIS / HYPOTHESIS / WITHDRAWN / OPEN` の状態変更。
5. VED との関係に変更がないか。

本ノートの目標は最終結論の保存ではなく、**訂正可能な依存関係と撤回理由の保存**である。

---

## 14. References

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

---

## Closing note

本ノートが保存しようとするのは、整った最終理論ではない。観測写像の非単射性から始まった一般定理への期待が、完全観測、自己記述可能系、極小実現の一意性、外部にも成立する破壊的反例、そして非形式的な「同一インターフェース」議論への再批判によって順番に崩れ、そのたびに問いがより限定された条件問題へ移った過程である。

現時点での最小限の結論は次である。

> 観測・予測成功は生成構造を強く支持しうるが、その成功だけでは、候補クラスの adequacy、実験可能性、再準備、動的遮蔽、初期独立性、共同実現可能性、記録、識別可能性、逆安定性、存在論的橋渡しのすべてが同時には自己証明されない。この指摘は普遍的不可能定理ではなく、各補助条件をどこまで独立に監査できるかを問う訂正可能な前提ネットワークである。
