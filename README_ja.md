# Vortical Enclosure Dynamics (VED)

Vortical Enclosure Dynamics（VED）は、因果ログ動力学と非閉包的な閉包過程から、時間・空間・物質・重力・宇宙論的構造がどのように立ち上がりうるかを探る理論的枠組みです。

![Differential Horizon Map](figures/differential_horizon_map.svg)

## 論文

- VED Vol.1 — Foundations: Minimal Axiom, Causal Logs, Time and Space  
  arXiv ID は未確定
- VED Vol.2 — Closure Geometry and the Standard Model  
  arXiv ID は未確定
- VED Vol.3 — Gravity, Black Holes, and Cosmology  
  arXiv ID は未確定
- VED Vol.4 — Differential Horizon, Observation, and Limits  
  arXiv ID は未確定
- IFGT — Information Field Geometry Theory  
  arXiv ID は未確定

## 現在の位置づけ

このリポジトリは、初回 arXiv 投稿のためのソース公開・研究背景提示を目的として、arXiv ID の確定前に先行公開しています。arXiv ID は投稿承認後に追記します。Vol.1 は現在の投稿対象、Vol.2-Vol.4 は連動する補助巻であり、定量的な導出にはなお未解決部分があります。

## 概念的な概要

VED は、差異から勾配、流れ、渦、閉包が生まれ、そこから有効な物理構造が立ち上がるという生成順序を提案します。この見方では、時間は因果ログの蓄積、空間は因果関係の構造、物質や幾何は安定した閉包現象として扱われ、初めから与えられた前提とは見なされません。

この枠組みは、完成済みの物理理論というより、構造的な研究プログラムとして読むことを意図しています。詳細な方程式、強い主張、方法論的立場、未解決問題は `docs/` に分け、ここでは入口ページとして必要な情報に絞っています。

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
paper/                             Vol.1-Vol.4 の LaTeX ソースと論文用図版
Information-Field-Geometry-Theory/ IFGT のソース、図版、PDF
arXiv_pdf/                         投稿用 PDF コピー
```

## 推奨読書順

1. VED Vol.1 — Foundations
2. VED Vol.3 — Gravity and Cosmology
3. IFGT — Information and Observation
4. VED Vol.4 — Differential Horizon
5. VED Vol.2 — Closure Geometry and the Standard Model

Vol.2 は、基礎概念への依存が最も強いため、あえて後ろに置いています。

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
