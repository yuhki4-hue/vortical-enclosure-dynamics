# 5. Gene × Information Flow

> **作業版scope:** DNA--\(\theta\)、gene event--\(J\)、gene source--\(\sigma\)、\(\Phi\)--restoring tendencyは抽象model representationまたは提案的biological interpretationである。具体的genotype-to-parameter map、event-to-current aggregation、measured source map、生化学mechanismは与えない。

本節では、DNAと生物学的過程を、情報密度とその流れによって記述する枠組みを与える。

ここでの目的は、DNAから発生・形態・細胞運命が立ち上がる過程を、
「意味」や「設計」ではなく、状態変化の連なりとして記述することである。

---

## 5.1 DNAの位置づけ

DNA配列 \(s\) は、

\[
s \in \{A, T, G, C\}^N
\]

で表される。

> **作業版注記:** ここで \(N\) はsequence lengthであり、toy modelのneural field \(N\) とは別である。

ここで重要なのは、DNAが意味や目的を持たない点である。

DNAが与えるのは、

- 分子生成の可能性
- 反応の起こりやすさ
- 閾値的な切り替え条件

といった、物理的・化学的な制約のみである。

したがって、DNAは「状態」ではなく、

> 系のダイナミクスを制約するパラメータ集合

として扱われる。

---

## 5.2 状態変化としての遺伝子イベント

転写、翻訳、結合、修飾といった遺伝子関連イベントは、

> 情報密度 \(I(r, t)\) を変化させる局所的な操作

として表現される。

これらのイベントは離散的であるが、
その総和は連続的な情報流 \(J(r, t)\) を用いてmodel化しうる。explicit event-to-current mapは与えない。

したがって、遺伝子ネットワークは、

> 情報流のcandidate sourceとして解釈される関係構造

として提案的に理解される。gene networkと \(J\) のoperational identityは主張しない。

---

## 5.3 連続方程式との接続

Section 4で導入した連続方程式

\[
\frac{\partial I}{\partial t} + \nabla \cdot J = \sigma
\]

において、

- \(\sigma\) は遺伝子イベントに起因する情報生成率
- \(J\) はそれらの積み重ねによって形成される流れ

として解釈される。

---

## 5.4 偏りと誘導ポテンシャル

情報密度 \(I\) に偏りが生じると、

\[
\Phi = \Phi[I]
\]

によって定まるポテンシャルが形成される。

このとき、状態変化は

\[
F = -\nabla \Phi
\]

に従ってバイアスを受ける。

重要なのは、ここで導入されているのが特別な力ではなく、

> 指定されたアトラクタ型モデルでは、選ばれた領域へ向かう復元バイアスとして表現しうる

という条件付き記述である点である。安定basinの存在や一般的returnは、この形式関係だけからは得られない。

---

## 5.5 閾値としての if/then

DNAが与える if/then は、

記号的なルールではなく、

> 連続場における閾値条件

として実装される。

すなわち、ある関数 \(F_k\) に対して

\[
F_k(I, J, r, t) > \theta_k
\]

のような条件で反応が切り替わる。

> **版差注記:** このworking Markdownは \(F_k\) の引数から \(\theta\) を省略している。canonical EN / JA manuscriptは \(F_k(I,J,\mathbf r,t;\theta)\) を用いる。省略をsilent identityや修正済みsignatureとは扱わず、versioned variantとして保存する。また \(F_k\) はvector bias \(\mathbf F\) およびstate-space field \(F(x;\theta)\) とは別objectである。

ここで \(\theta_k\) は抽象model layerでDNA-conditioned parameter setと関連づけられるが、具体的なsequence-to-threshold mapは実装されない。

---

## 5.6 形態の解釈

以上をまとめると、

- DNAは条件を与える
- 情報密度と流れが形成される
- 偏りがポテンシャルを生む
- 流れがバイアスされる
- 閾値によって状態が分岐する

その結果として、

> 結果の配置には、アトラクタに基づく解釈を与えうる

細胞運命や観測形態との同定は、この系列だけから導かれる結果ではなく、別の生物学的対応である。

---

## 5.7 提案的なスケール間再利用

この記述は、

- 分子スケール
- 細胞スケール
- 組織スケール

に対して同じ記述語彙を再利用することが提案される。

ただし違いは粗視化levelだけとは限らず、source-local objectも変わる。

\[
I, J, \Phi, \text{閾値}, \text{安定解}
\]

という表示はrole analogyの候補であって、typed scale map、coarse-graining operator、保存invariant、universalityを確立しない。

ここで表示中の「安定解」はworking sourceの圧縮された解釈ラベルであり、具体系の定常解、安定basin、またはscaleをまたぐ同一解を確立したという意味ではない。

---

## 5.8 要約

本節の内容は次のようにまとめられる。

> DNAは意味を持たない条件集合であり、  
> 情報密度とその流れは候補となる持続配置を記述し、生物学的構造という読みは解釈として区別される。

この枠組みは、次節以降で扱う発生および形態形成の具体例の基盤となる。
