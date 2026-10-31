# Bio-IFGT residual repair after final FAIL v0.1

## 0. Status

- Residual repair BFC-01 / BFC-02: **COMPLETE**
- Bio-IFGT audit: **CLOSED** / Final dispositions: **FROZEN**
- Bio-IFGT core revision: **READY FOR FINAL CONSISTENCY RECHECK**
- Final consistency check v1.0: historical **FAIL — CORE REVISION REMAINS OPEN**
- Independent final consistency recheck: **NOT STARTED**

本記録は2026-09-09の限定修復記録であり、80 dispositionsの再監査・再判定でもcore closure判定でもない。

## 1. Authority

- [Phase 07 frozen final dispositions](07_final_audit_record_v1.0_ja.md)
- [independent final consistency check v1.0](implementation_final_consistency_check_v1.0_ja.md): BFC-01 / BFC-02のexact authority。77 PASS / 3 FAILという修復前の結果を変更しない。
- [implementation 01](implementation_phase_01_source_identity_v0.1_ja.md)
- [implementation 02](implementation_phase_02_equation_role_and_paper_code_v0.1_ja.md)
- [implementation 03](implementation_phase_03_stability_attractor_life_v0.1_ja.md)
- [implementation 04](implementation_phase_04_biological_empirical_cross_scale_v0.1_ja.md)
- [implementation 05](implementation_phase_05_repository_sync_distribution_handoff_v0.1_ja.md)

比較baselineは本task開始時のdirty working tree。HEADへの巻戻し、既存変更の整理、historical auditの書換えは行わない。

## 2. Scope

| Blocker | Frozen authority | 修復範囲 | 数式変更 | OPEN保存 |
|---|---|---|---|---|
| BFC-01 | BIO-FD-064 / BIO-FD-065 | Bio EN/JA §12.5のGIF配布事実と対応PDF | NO | YES: historical lineage |
| BFC-02 | BIO-FD-080 | Intelligence I Section 9の四層比較本文・同節再言及と対応PDF | NO | YES: common carrier / mechanism / typed translation |

新semantic phase、Intelligence I独自理論の改訂、他downstream修復、simulation、GIF生成を行わない。

## 3. BFC-01 repair

[EN simulation results](../../bio-ifgt/sections/simulation_results_visualization.tex)と[self-contained JA](../../bio-ifgt/main_ja.tex)の時間発展可視化節を修復した。

- 旧unprefixed `development_v2_hierarchical.gif` pathは、現行配布に存在しない旧参照として保存。
- 実在する別名 `fig8_development_v2_hierarchical.gif` はhistorical local artifactと明示。
- 現audited run / tracked PNGとのlineageは未解決。検証済みcurrent supplementary outputではなく、current-run GIFを提供していないことをEN/JA双方で明示。
- 旧animationの内容を現runの証拠として記述せず、直後の既存sequenceは前節のstaged model descriptionとして保存。式には触れない。

[Bio README](../../bio-ifgt/README.md)はhistorical GIFをcurrent evidenceに使わないと既に明示。[simulation README](../../bio-ifgt/simulations/minimal_neural_field/README.md)のoutput一覧はscriptの生成能力の記述であり、配布済み一覧とは区別され、lineage OPEN注記もある。両者は無変更。working JA / handoffも確認し、現行配布を約束する当該文の追加修復は不要だった。

## 4. BFC-02 repair

[EN Section 9](../../intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex)と[JA Section 9](../../intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex)を限定修復した。

ENは四層tableの導入と直後の本文をproposed structural comparisonへ統一。Bio項目は提案的語彙の比較であり、common carrier、shared mechanism、common generative cause、typed cross-domain translationを確立しない。

JAは四層導入・共通特徴の導入・「偶然の類似ではなく／同一の構造的緊張から発生」の因果読みに関する文・含意quote・同節のシリーズ接続再言及・末尾summaryを同じceilingへ揃えた。tableと四層比較自体は保存。「閉じようとして閉じきれない」は比較を動機づける語彙として残す。

Figure 5 EN/JAとcaptionは既にproposed comparisonであり、編集・再生成しない。理論の独立評価や新しい翻訳mapは行わない。

## 5. Files changed

| 区分 | File | 今回の変更 |
|---|---|---|
| Source | [Bio EN results](../../bio-ifgt/sections/simulation_results_visualization.tex) | BFC-01本文のみ |
| Source | [Bio JA](../../bio-ifgt/main_ja.tex) | BFC-01本文のみ |
| Source | [Intelligence I EN §9](../../intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex) | BFC-02帰属scopeのみ |
| Source | [Intelligence I JA §9](../../intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex) | BFC-02帰属scopeのみ |
| Distribution | [Bio EN PDF](../../bio-ifgt/main.pdf) / [Bio JA PDF](../../bio-ifgt/main_ja.pdf) | 成功buildを同期 |
| Distribution | [Intelligence I EN PDF](../../intelligence-part1/main.pdf) / [Intelligence I JA PDF](../../intelligence-part1/main_ja.pdf) | 成功buildを同期 |
| Audit navigation | [README](README_ja.md) | 修復完了・recheck未開始・FAIL履歴link |
| New record | 本記録 | 限定修復trace |

合計: 新規1、既存変更9（本文4、PDF4、audit README1）。その他の既存tracked / notes filesは開始時hashのまま。

## 6. PDF rebuild

既存latexmk workflowを使用。Bio ENはpdfLaTeX、Bio JA / Intelligence I EN/JAはLuaLaTeX。すべて一時outdirで成功を確認した後、指定4 PDFのみcopyした。simulationは実行しない。

共通一時root: `${TEMP_EVIDENCE_ROOT}/bio_bfc_repair.BIBm1V`。各projectをcwdに、EN Bioは `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=.../bio-en main.tex`、他3件は `latexmk -lualatex -interaction=nonstopmode -halt-on-error -g -outdir=... main[_ja].tex` を使用した。

LuaLaTeXの初回試行はfont-cache write制限で失敗。承認された再試行でtask-local環境 `TEXMFVAR=${TEMP_EVIDENCE_ROOT}/bio_ifgt_impl05_texmfvar`、`TEXMFCACHE=${TEMP_EVIDENCE_ROOT}/bio_ifgt_impl05_texmfcache`、`XDG_CACHE_HOME=${TEMP_EVIDENCE_ROOT}/bio_ifgt_impl05_xdg`、`openout_any=a` を使用し成功した。repositoryの設定・sourceによる回避変更はない。

| PDF | Pages before / after | SHA-256 before | SHA-256 after |
|---|---|---|---|
| Bio EN | 31 / 31 | `5d9684dadeb58783410898a2918bbbf82a6d82e628fc1ebec6be15f7f794f330` | `1c087a772806b2e3acaafd02a3b81d238c3872af548601017060a2c06f8a3a54` |
| Bio JA | 25 / 25 | `40e7f19a7f3a307419367ecdf2ca85caa94232f7b45b6606c30997706246c1b2` | `dd67f26ca5d57576f940d9b71b7fde83d81db5725b7a00b2fcadb3d5ce3b4136` |
| Intelligence I EN | 26 / 26 | `44b36d14d8bb3f25d286018c9cee9331e99b9b3d3f983d9a79ed771e20af229c` | `0f5c86a8615537fd09536249ae223f33c4903249df710aee1dd0937d263802be` |
| Intelligence I JA | 73 / 73 | `6e924ad3e66cf2fdf798da8c479d1943ae67ad22633777a0aa937f5c120baa86` | `0b9344a0dd096f068ab245db0c555f31ec222ac83b4fb89f9271af4b46d8dfcb` |

最終buildは4/4成功。Bio ENの今回追加filenameによるoverfullは短い同義文に整えて解消。JA font-size substitution / caption-class warning、Intelligence I EN既存箇所のoverfullは非関連typesetting advisoryとして記録し、警告除去のためのsource改稿はしない。

## 7. EN/JA parity

| 対象 | EN | JA | 判定 |
|---|---|---|---|
| GIF | 旧path不在、historical alternate、lineage unresolved、current output非提供 | 同じ4条件 | PASS |
| 四層本文 | proposed roles comparison、共通carrier / cause / mechanism / translationを確立しない | 同じceiling、共通原因断定を除去 | PASS |
| Figure / caption / body | 提案的comparison | 提案的comparison | PASS |

PDF skillに従って抽出textだけでなくrasterを目視。Popplerが利用できないため既存Ghostscriptでrenderし、追加dependencyは導入しなかった。Bio EN p.22 / JA p.23、Intelligence I EN pp.22–23、JA pp.60–63 / 65–66の該当本文・Figure 5・summaryについて文字の欠落・重なりがないことを確認した（ページ番号は印刷表示）。

## 8. Equation immutability

開始前snapshotに対し、tracked Bio / Intelligence IのTeX・Markdown内のdisplay delimitersとequation / align / gather / multline / displaymath / eqnarray環境（star付き含む）を順序付きでSHA-256比較。

| 対象 | Source files | Displayed blocks | Added | Removed | Changed |
|---|---|---|---|---|---|
| Bio | 33 / 33 | 119 / 119 | 0 | 0 | 0 |
| Intelligence I | 26 / 26 | 49 / 49 | 0 | 0 | 0 |

file→block hash listのsorted JSON aggregateも前後一致: Bio `d88da4a7fd8b69fb0c9d1957731adc17507d1ac6e938d1a72c0749ac9f69d4fa`、Intelligence I `fd3ad16d0f5ccd42584bce5aedba3738fbfd3af83ed511929d9838369e27ffa3`。
差分を目視し、係数・符号・演算子・index・functional formの変更なし。新equation / notationなし。

## 9. Artifact immutability

| 対象 | 結果 |
|---|---|
| simulate.py | byte不変: `f98e10a807a53b1448fdb9e994864c7448f5b07e61e89bf73abfce0401ee8d8e` |
| requirements.txt | byte不変: `97bc1172e4176b7035e5aa74355d79f1ca8cd75605eb208a678fcd3b3cae49a3` |
| parameters / simulation | 変更・実行なし |
| Bio tracked PNG | 7/7 byte hash不変。新EN/JA PDFとも7/7 decoded RGB一致 |
| historical ignored GIF | byte不変: `590fcd1000e299d7e98d5512562e20b886fc1d358a4649fbae39f3689af150ee` |
| Intelligence I Figure 5 | EN/JA SVG・PNG計4ファイルbyte不変、新PDF embedded RGBもEN/JA一致 |
| GIF distribution | expected unprefixed pathは引続き不在。tracked GIF追加0。4 PDF attachmentsは0 |

Bio PNGとPDFの一致は今回の埋込確認であり、fresh simulation provenanceの追加推定ではない。historical GIFのrename・copy・delete・昇格はしない。

## 10. Strong-language rescan

GIFの `provided as supplementary material` / `supplementary animation provided` / `補足資料として提供` / `animation is available`、四層の `each layer exhibits` / `same structure` / `same structural tension` / `not accidental` / `arises from the same` / `同一の差分発展構造` / `同一の構造的緊張` / `偶然の類似ではなく` をsourceとPDFでcontext確認した。

BFC-01対象の提供断定は0。BFC-02対象のSection 9四層比較・同節summaryの未限定な共通原因断定は0。replacement wordingは4 PDFに収録されている。

Intelligence I JAの全文PDF検索には「同一の差分発展構造」が2件残る。これはSection 1 / 10の知性と意識の二者関係についての独自記述であり、今回のBio四層帰属の修復対象とは区別した。他sectionの理論改稿を行わず、全文でkeywordが0とは報告しない。working `draft_ja.md` の旧四層記述は冒頭source-status注記で非canonical / 非identityと明示済みのため保存。この限定scanは独立final consistency recheckを代替しない。

## 11. OPEN preservation

historical GIF lineage、Bio biological observable / empirical correspondence、IFGT/Bio typed translation、共通carrier / mechanism / generative causeの対応は解決していない。新証拠・新bridge・新理論はない。
Bio frozen dispositionsおよび上流VED/IFGT auditのfile hashは開始時と不変。8 upstream bridges、genotype→theta、life criterion、stability / basin、regeneration等のOPENを成立済みにする変更はない。

## 12. Validation

- source paths / relative links / Markdown fences / display delimiters / tables / TeX environment balanceを対象変更filesと関連READMEで検査。
- Bio33 source119 blocks、Intelligence I26 source49 blocksを開始時snapshotと比較。
- 指定4 PDF build成功・新source文言のtext抽出・該当page目視・Bio7 PNG / Figure 5 embedded pixel照合。
- GIF未配布の現物確認、historical GIFとsimulation一式・Figure 5 hash不変確認。
- `git diff --check`: PASS。
- 変更集合は§5の9既存files＋新recordだけ。既存173 tracked modificationsと3 untracked directory entriesを保存。build junkをrepositoryへ追加していない。
- 一時snapshot / hash manifest / text extraction / raster / build logsは `${TEMP_EVIDENCE_ROOT}/bio_bfc_repair.BIBm1V`。`before.json` / `verification.json` / `validation.json`でtask-local比較を再現できる。

## 13. Recheck readiness

**Residual repair: COMPLETE. Ready for independent final consistency recheck: YES.**

BFC-01 → BIO-FD-064 / 065、BFC-02 → BIO-FD-080の限定修復と配布同期を完了。v1.0 FAIL recordは保存し、[README](README_ja.md)をrecheck待ちへ更新した。
core revisionをCLOSEDとはしない。独立final consistency recheckは実施していない。commit / push / tagなし。本taskはここで停止する。
