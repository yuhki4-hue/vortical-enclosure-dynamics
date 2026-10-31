# 6. Development and Morphogenesis

> **作業版scope:** \(I\) とmorphogen、threshold labelとcell fate、model configurationとobserved morphologyの関係は定性的な提案対応である。finite constructionはmodel-local spatial organizationを支えるが、operational measurement mapまたはdemonstrated biological mechanismを与えない。

本節では、前節で導入した枠組みを用いて、
発生および形態形成を具体的に記述する。

目的は、発生を「設計の実行」としてではなく、

> 状態変化が持続配置へ近づきうる過程という提案的解釈

として理解することである。一般式だけで生物学的収束を確立するものではない。

---

## 6.1 初期状態と非対称性

受精卵は、状態空間の中で広い可能性を持つ初期状態にある。

この段階では、

- 情報密度 \(I\) はほぼ均一
- 明確な構造は存在しない

しかし、わずかな非対称性（初期条件や環境ゆらぎ）が存在する。

この非対称性が、後の構造形成の種となる。

---

## 6.2 情報密度としてのモルフォゲン

発生過程では、モルフォゲンと呼ばれる分子が
空間的な濃度分布を形成する。

ここではこれを、

> 情報密度 \(I(r, t)\)

として扱う。

初期の局所的な生成により、\(I\) の勾配が生まれ、
拡散と分解を含むダイナミクスのもとで分布が形成される。

---

## 6.3 ダイナミクス

情報密度は、以下の形で時間発展する：

\[
\frac{\partial I}{\partial t} = D\nabla^2 I - \lambda I + \sigma(r, t)
\]

> **版差注記:** このworking Markdownはsource signatureから \(\theta\) を省略している。canonical EN / JA manuscriptは \(\sigma(\mathbf r,t;\theta)\) を用いる。暗黙依存、別function、単なる省略のいずれかはここでは確定せず、両表記をversioned variantとして区別する。

ここで、

- \(D\)：拡散係数
- \(\lambda\)：減衰率
- \(\sigma\)：局所生成（DNAにより制約される）

である。

この方程式は特別なものではなく、
拡散系として標準的な形式である。

これはcontinuous coarse-grained evolution relationであり、finite toy codeをexact PDE solverまたは同一のdynamical objectとして指定するものではない。

---

## 6.4 誘導ポテンシャルと勾配

\(I\) の分布によりポテンシャル \(\Phi\) が誘導される。

\[
\Phi = \Phi[I]
\]

このとき、状態変化は

\[
F = -\nabla \Phi
\]

に従ってバイアスされる。

結果として、

> 状態は高い \(I\) を持つ領域、あるいはその勾配に沿って偏る

この偏りが、構造形成の方向性を与える。

---

## 6.5 閾値による分化

細胞の運命は、\(I\) の値に対する閾値によって分岐する。

例えば：

\[
I(r) < \theta_1 \rightarrow \text{状態 A}
\]

\[
\theta_1 \le I(r) < \theta_2 \rightarrow \text{状態 B}
\]

\[
I(r) \ge \theta_2 \rightarrow \text{状態 C}
\]

ここで重要なのは、

- \(I\) は連続量である
- 結果は離散的に現れる

という点である。

分化とは、

> 連続的な状態変化に対する閾値応答

として理解される。

数学的には上の含意はthreshold classification ruleであり、state labelとbiological interpretationは別roleである。

---

## 6.6 アトラクタとしての形態

上記のダイナミクスと閾値構造の組み合わせにより、

- 指定条件のもとでmodel distributionが持続し
- 分化labelが形成されうる

この配置を発生における形態と読むことは、別の生物学的解釈である。

したがって形態とは、

> あらかじめ指定された構造ではなく、  
> 持続配置へ近づくという候補解釈

である。

---

## 6.7 頑健性の理解

発生はしばしば高い再現性と頑健性を持つと記述される。

この性質は、設計の正確さではなく、

> 複数の近傍初期状態が同じ領域へ戻るなら、その挙動が頑健性の候補説明となる

というアトラクタ解釈として表現できる。

現在の形式関係と有限toy modelは、生物学的頑健性や任意摂動returnを確立せず、試験範囲内のmodel-localな持続、緩和、recommitmentのみを示す。

---

## 6.8 要約

発生および形態形成は、

- 初期のわずかな非対称性
- 情報密度の分布
- 勾配によるバイアス
- 閾値による分岐
- 提案的なアトラクタ解釈

によって記述される。

ここには設計図も目的も必要ない。

必要なのは、

> 状態が変化し、偏りが生まれ、候補となる持続配置が記述される

という最小限の構造だけである。
