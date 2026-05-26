# Vortical Enclosure Dynamics (VED)

Vortical Enclosure Dynamics（VED）は、因果ログ動力学と非閉包的な閉包過程から、時間・空間・物質・重力・宇宙論的構造がどのように立ち上がりうるかを探る理論的枠組みです。

このリポジトリは、初回 arXiv 投稿のためのソース公開・研究背景提示を目的として、arXiv ID の確定前に先行公開しています。arXiv ID は投稿承認後に追記します。

![Differential Horizon Map](figures/differential_horizon_map.svg)

## 論文

- [VED Vol.1 — Foundations: Minimal Axiom, Causal Logs, Time and Space](paper/vol1/main.pdf)  
  arXiv ID は未確定
- [VED Vol.2 — Closure Geometry and the Standard Model](paper/vol2/main.pdf)  
  arXiv ID は未確定
- [VED Vol.3 — Gravity, Black Holes, and Cosmology](paper/vol3/main.pdf)  
  arXiv ID は未確定
- [VED Vol.4 — The Differential Horizon: Divergence, Renormalization, and the Boundary of Generation](paper/vol4/main.pdf)  
  arXiv ID は未確定  
  2026年5月に大幅改訂。registered difference、trace formation、local Differential Horizons を中核的な記述枠組みとして導入しました。Divergence は boundary signal として、renormalization は boundary contact の finite re-expression として読み替えられます。動的バリア（§13）は Differential Horizon Principle の最小形として再解釈されています。
- [IFGT — Information Field Geometry Theory](Information-Field-Geometry-Theory/main.pdf)  
  arXiv ID は未確定
- [Bio-IFGT — Biological Morphogenesis as Information-Flow Attractor Dynamics](bio-ifgt/main.pdf)  
  arXiv ID は未確定
- [Conceptual Topography — A Field-Theoretic Account of Conceptual Landscapes](./conceptual-topography/main.pdf)  
  arXiv ID は未確定
- [A Non-Generative Account of Consciousness — Temporal Non-Closure and Cross-Scale Log Referencing](./consciousness/main.pdf)  
  arXiv ID は未確定
- [Intelligence Part I — Structural Constraints on Intelligence as a Dynamical Phenomenon](./intelligence-part1/main.pdf)  
  arXiv ID は未確定

投稿用 PDF コピーは [`arXiv_pdf/`](arXiv_pdf/) にまとめています。

## 現在の位置づけ

すべての巻は、このリポジトリ内でプレプリントとして公開されています。arXiv 投稿は `gr-qc` および `physics.gen-ph` の endorsement 待ちです。その間、GitHub を暫定的な主要引用元として扱います。

Vol.4 は 2026年5月に構造的な大改訂を行い、観測と記述の枠組みを全章にわたって深めました。この改訂では、registered difference、descriptive window、pastified texture、boundary signal、local horizon-form、open generative framework という統一語彙が 14 セクション全体を貫く形で導入されています。

Vol.1–Vol.3 には、定量的導出に関してなお未解決の部分があります。

## 概念的な概要

VED は、差異から勾配、流れ、渦、閉包が生まれ、そこから有効な物理構造が立ち上がるという生成順序を提案します。この見方では、時間は因果ログの蓄積の効果、空間は因果関係によって誘導される構造、物質や幾何は安定化した閉包現象として扱われ、初めから与えられた前提とは見なされません。

この枠組みは、完成済みの物理理論というより、構造的な研究プログラムとして読むことを意図しています。詳細な方程式、強い主張、方法論的立場、未解決問題は [`docs/`](docs/) に分け、ここでは入口ページとして必要な情報に絞っています。

関連ドキュメント:

- [Overview](docs/00_overview.md)
- [Core Equations](docs/core_equations.md)
- [Key Correspondences](docs/correspondences.md)
- [Claims](docs/claims.md)
- [Methodology](docs/methodology.md)

## リポジトリ構成

```txt
docs/                              解説文書、方法論、主張整理、未解決問題
figures/                           図表・概念図
paper/                             Vol.1–Vol.4 の LaTeX ソースと論文用図版
Information-Field-Geometry-Theory/ IFGT のソース、図版、PDF
bio-ifgt/                          IFGT/VED の生物学的 coarse-graining
conceptual-topography/             IFGT/VED の認知・社会的応用層
consciousness/                     時間的非閉包とログ参照としての意識論
intelligence-part1/                非閉包的な力学的現象としての知性論 Part I
arXiv_pdf/                         投稿用 PDF コピー
notes/                             作業ノートと補足資料
```

- `bio-ifgt/`: IFGT/VED の生物学的 coarse-graining。生命、発生、
  遺伝子媒介的制約、知性を、完成形ではなく準閉包レジームとして記述します。
- `conceptual-topography/`: IFGT/VED の認知・社会的応用層。概念、理解、
  言語トークン、共有された概念地形を、投影された準閉包レジームとして記述します。
- `consciousness/`: 意識を、生成された対象ではなく、時間的非閉包、
  speed-scale orchestration、ログ参照として開かれるレジームとして記述する
  応用層です。IFGT 変数は、生物的・認知的観測窓に射影された有効変数として扱います。
- `intelligence-part1/`: VED/IFGT 応用系列における知性層の第一論文です。
  知性を、連結状態空間、時間順序、グローバル制約、外化された停止構造を要請する
  local horizon-form によって制約される力学的現象として扱います。

## 推奨読書順

一般読者向け:

1. VED Vol.1 — Foundations
2. VED Vol.3 — Gravity and Cosmology
3. IFGT — Information and Observation
4. VED Vol.4 — The Differential Horizon
5. VED Vol.2 — Closure Geometry and the Standard Model

物理背景のある読者向け:

1. VED Vol.1 — Foundations
2. VED Vol.3 — Gravity and Cosmology
3. VED Vol.4 — The Differential Horizon
4. IFGT — Information and Observation
5. VED Vol.2 — Closure Geometry and the Standard Model

Vol.2 は、基礎概念と初期巻で導入される構造的前提への依存が最も強いため、あえて後ろに置いています。一般読者には、情報流・勾配・準閉包を比較的具体的に導入する IFGT を Vol.4 の前に読む順序が向いています。一方、物理背景のある読者には、Differential Horizon の枠組みを先に読むことで、IFGT が観測境界の手前側の運動を記述していることが見えやすくなります。

## 公開モデル

- arXiv には固定された引用可能版を置きます。
- GitHub には更新中のソース、図、修正、補足ノートを置きます。
- note や一般向け記事には解釈的で導入的な説明を置きます。

## 未解決問題

この枠組みには、微視的形式化、定量的予測、重力の基準解、量子的振る舞いの扱いなど、引き続き検討すべき点があります。詳細は [Open Problems](docs/open_problems.md) を参照してください。

## 引用

arXiv ID が確定する前に本枠組みを参照または議論する場合は、このリポジトリを引用してください。arXiv 参照は投稿承認後に追記します。リポジトリの基本メタデータは [CITATION.cff](CITATION.cff) にあります。

## ライセンス

特記のない限り、理論文書と図版は CC BY 4.0 で公開します。詳細は [LICENSE](LICENSE) を参照してください。

## 著者の立場

このリポジトリは、完成宣言ではなく、更新され続ける研究枠組みとして提示されています。短い注記はここに残し、より詳しい立場説明は [Author Position](docs/author_position.md) に分けています。
