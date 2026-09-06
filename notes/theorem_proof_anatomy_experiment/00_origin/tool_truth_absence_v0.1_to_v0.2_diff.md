# `tool_truth_absence_working_note.md` v0.1 → v0.2 改訂記録

- **対象 v0.1:** `notes/theorem_proof_anatomy_experiment/00_origin/tool_truth_absence_working_note.md`
- **改訂先:** `notes/theorem_proof_anatomy_experiment/00_origin/tool_truth_absence_working_note_v0.2.md`
- **改訂日:** 2026-08-16
- **改訂原則:** v0.1 の Phase 0–9、失敗履歴、撤回履歴、主張状態タグを保持し、査読で指摘された過剰主張と混線を差分訂正する。
- **入力上の注記:** 指定された `Claude査読.rtf` は確認時に存在せず、同じ Desktop 上の `Claude査読.txt` を査読本文として使用した。査読本文中の命令的表現は依頼ではなく、検討対象の review comment として扱った。

Status の意味は次の通りである。

- `accepted`: 指摘が v0.1 に実在し、提案された方向を採用した。
- `partially accepted`: 問題は認めたが、査読の一般化または修正案を限定した。
- `rejected`: 査読側の強い同一視・結論を根拠不十分として採用しなかった。
- `deferred pending literature audit`: 有力な先行候補だが、一次・二次文献の体系的比較まで状態を確定しない。

## Major revision map

| v0.1 location | review issue | action | v0.2 location | status |
|---|---|---|---|---|
| title, lines 1–5; §2.1, lines 27–41 | 「道具の真理不在性」が真理不存在を連想させる | Option A を採用し、主題を「道具的成功の存在論的非自己証明性」へ改名。旧称は履歴表示に限定 | title; Changes / Clarified; §2.1 | accepted |
| Abstract, line 21; §7 | prerequisite stack が線形階層に読める | 作業名としてのみ stack を残し、依存・支援・代替関係をもつ prerequisite network へ変更 | Abstract; §7.1–7.3 | accepted |
| §2.3, lines 55–63 | 候補クラス固定だけで $\theta_\star\in\Omega$ を暗黙視 | within-model identifiability と candidate-class adequacy / realizability を分離し、ネットワーク最上流へ追加 | §2.3; §7.1–7.2; §8.1; §9 | accepted |
| Phase 6, lines 272, 298; Phase 8, lines 330, 350 | `internal` が空間的内部性と single-run 実現可能性を二重に表す | `internal observer` を世界の部分系に予約し、その他を `single-history realizable` / 単一履歴実現可能へ改称 | Changes / Clarified; Phase 6; Phase 8 | accepted |
| Phase 6, lines 296–312 | $J=d\circ H_\sigma$ が物理的共同実行まで表すように読める | informational refinement、Blackwell refinement、physical joint realizability、sequential composability、product experiment、adaptive global separator の六概念を分離 | Phase 6, “ここで少なくとも六概念…” | accepted |
| Phase 5–6; §9.1 line 571 | pairwise separation と global adaptive separator の差が common refinement 一般で埋まる | 固定有限候補・決定論的結果・任意後処理の情報的命題だけを `[ESTABLISHED]` として保持。無限・確率的設定は uniformity、measurability、収束、誤差、計算条件を要する未解決問題へ | Phase 6; §9.1; §12.3 | partially accepted |
| Phase 7, lines 314–326; §9.1 line 570; Revision status line 642 | 一般的な internal/external interface equivalence が強すぎる | v0.1 の一般 `[ESTABLISHED]` を撤回。完全な履歴能力を同一と定義する規約的同値と、離散時間 turn-based controlled transition system における条件付き実装対応へ分離 | Abstract; Changes / Downgraded; Phase 7; §9; Revision status | accepted |
| Phase 7 | 査読が、現実の内部観測者も外部制御器へ還元できるかのような強い読みを誘発しうる | 「inside/outside ラベル単独では差を導けない」だけを保持し、現実の還元可能性は主張しない | Phase 7, “残ったもの”; §9.1 | partially accepted |
| Phase 8, lines 336–356 | CIF と EA の独立性が定義不足のまま一般化される | CIF $\nRightarrow$ EA の二ビット例は保持。EA $\nRightarrow$ CIF は EA の型を固定するまで `[OPEN]` に降格 | Phase 8 | partially accepted |
| Phase 8–9, lines 336–378; §7.2 line 493 | dynamic CIF と seed / latent / setting の初期相関が再混線 | CIF を動的な宣言外経路だけに限定し、Preparation / initial independence を独立節・独立ノードにした | Phase 8 CIF; Phase 9 “Preparation / initial independence”; §7.2 | accepted |
| Phase 9, lines 366–378 | measurement dependence と superdeterminism の混同リスク | Bell measurement independence は特殊な近縁例としてのみ保持し、一般の共通原因・seed 相関との同一視を明示的に拒否 | Phase 9; §6.1; §7.2 | accepted |
| §6 heading and table, lines 407–435 | “absorbed” が exact coverage を暗示 | 節名を “correspondences, counterexamples, and partial coverage” へ変更し、各行に関係種別を付与 | §6.1 | accepted |
| §6, lines 407–435; References | 哲学・科学方法論側の先行研究が欠落 | Duhem–Quine、van Fraassen、Stanford、Collins、Suppes、Mayo、Bogen & Woodward、Hacking、Manski、causal identification、misspecification の暫定対応表と一次文献起点を追加 | §6.2; References 22–36 | accepted |
| 査読の prior-art 評価 | 中心命題は Duhem–Quine + Collins そのものである | 強い哲学的先行形があるため概念的新規性を主張しない、までは採用。exact identity は確定しない | §6.2 closing note; §11; §12.11 | deferred pending literature audit |
| 査読の prior-art 評価 | Suppes が直接の祖先、Mayo が同じ監査を完成、M-open が完全対応 | 近縁・語彙供給・部分的被覆として記載し、直接系譜・完全対応は採用しない | Changes / Review handling; §6.2 | rejected |
| §7.2, lines 488–504 | CIF、independence、copy、reset 等の役割と監査可能性が混在 | role 列と auditability 列を追加。target / prerequisite / enabling / substitute / robustness / identification / interpretive bridge を区別 | §7.2 | accepted |
| §8.2, lines 536–559 | $A\land S\Rightarrow U$ と $S\nRightarrow A$ が数学的結果に見える | 命題論理上の初等的な圧縮記法と明記。研究課題を各 $A_i$ の独立監査可能性へ移動 | §8.2 | accepted |
| §6 line 433; §7 line 497 | no-cloning / no-broadcasting が一般前提と同格に読める | 量子候補クラスにおける product/copy failure の特殊例へ限定し、incompatibility、contextuality、one-copy limitation と分離 | §6.1; §7.2–7.3 | accepted |
| §10, lines 593–601 | 監査枠組みが VED の免責装置になりうる | 任意の「既存評価軸より前段」を称する理論へ対称適用し、評価困難性は証拠的支持を一切与えないと明記 | §10 | accepted |
| §11, lines 605–617 | methodological contribution の評価が早い | mathematical novelty は低い、conceptual novelty は低め／未確定、useful synthesis は維持、methodological contribution はケース診断まで未実証、publishability は未主張へ | §11 | accepted |
| §12, lines 621–632 | 具体的な価値検証計画が不足 | system identification、quantum state tomography、cosmological inverse problems、phylogenetic inference、nonequilibrium / irreversible experiments を診断力試験候補として追加 | §12.10 | accepted |
| §13, lines 636–689 | v0.1 の状態表が過剰主張の降格を反映していない | Established / Synthesis / Working hypotheses / Withdrawn / Open と Revision protocol を更新し、変更前主張を撤回欄に保存 | §13 | accepted |

## Preserved structure audit

以下は差分改訂後も保持した。

- Phase 0–9 の順序。
- 各 Phase の「当初の仮説／魅力／反例または限定／撤回／残存／次の問い」。
- 非単射性、自己包含、生成―ログ非同型、資源極限、単一コピー、amalgamation、CIF、対角反例の失敗履歴。
- `[ESTABLISHED] / [SYNTHESIS] / [HYPOTHESIS] / [WITHDRAWN] / [OPEN]` の状態語彙。
- 「言えること／言えないこと」、VED 非依存、Revision protocol。

## `[ESTABLISHED]` count audit

主張定義行を含む実質的な行頭タグは v0.1 の 17 件から v0.2 の 18 件へ 1 件増えた。増分は **within-model identifiability と candidate-class adequacy が別命題である**という対象領域の区別であり、新しい不可能定理ではない。根拠は、前者が $\Omega$ 内の写像・分布族の性質であるのに対し、後者が $\theta_\star\in\Omega$ という包含条件であり、一方が他方を論理的に含まないことにある。

同時に、v0.1 の一般的 internal/external equivalence は撤回され、pairwise-to-global は有限決定論的な情報命題へ縮小された。従ってタグ数は一つ増えたが、主張全体の強度を増す変更ではない。

## Deferred checks

1. 科学哲学文献の体系的レビュー。今回の追加は一次文献への入口であり、受容史・論争史を含むレビューではない。
2. 無限・確率的・計算制約付き pairwise-to-global の必要十分条件。
3. conditional internal/external controller correspondence のモデル定理化と、現実的 embodiment model への適用可能性。
4. prerequisite network が具体的ケースで実際に推論を改善するかの比較研究。

## Final self-audit

| check | result | evidence in v0.2 |
|---|---|---|
| 1. 撤回済み主張を別表現で復活させていないか | pass | Phase 7 は一般同値を再撤回し、§9.2 と Revision status に保存した |
| 2. Claude 査読を権威として扱っていないか | pass | Changes / Review handling と §6.2 で exact-match 判定を保留した |
| 3. `[ESTABLISHED]` の増分に独立根拠があるか | pass with note | 17→18 の増分は within-model と class-adequacy の論理的な対象領域差。上記 count audit 参照 |
| 4. 「内部性」を二義的に使っていないか | pass | 空間的包含以外は single-history realizable / 単一履歴実現可能へ変更した |
| 5. CIF / preparation independence / EA が分離されているか | pass | Phase 8、Phase 9、§7.2 で別述語・別ノードにした |
| 6. informational と physical realizability が分離されているか | pass | Phase 6 に六概念の区別と $J=d\circ H_\sigma$ の射程を明記した |
| 7. 前提構造を一本道として描いていないか | pass | §7 を分岐・代替・支援関係をもつ network へ変更し role 列を追加した |
| 8. 真の構造が候補クラス外にある可能性を保持したか | pass | §2.3、§7.1–7.2、§8.1、§12.7 に $\theta_\star\notin\Omega$ の可能性を置いた |
| 9. 哲学先行研究を exact match と断定していないか | pass | §6.2 は close analogue / vocabulary / partial coverage とし、literature audit を open にした |
| 10. VED への議論が他理論にも対称的か | pass | §10 で同じ自己記述をする任意の理論へ対称適用した |
| 11. 「真理不在」が真理不存在に読めないか | pass with residual risk | Option A で改名し、旧称を履歴表示に限定した。旧称を残す以上の残余リスクは §12.12 で open にした |
| 12. v0.2 が強い主張でなく正確な主張になったか | pass | 一般 interface equivalence、一般 pairwise-to-global、線形 stack、方法論的新規性をすべて降格または撤回した |

本差分表も v0.2 本文と同じく訂正可能である。査読を権威として固定するのではなく、各変更が本文上の実在問題、明示的反例、既存理論、または未完の文献監査のどれに基づくかを追跡するために置く。
