# Bio-IFGT Phase 05 — simulation / empirical correspondence audit

## 0. Status

- Bio-IFGT audit: **IN PROGRESS**
- Phase 00–04: **COMPLETE**（既存classification・burdenを変更しない）
- Phase 05 simulation / empirical correspondence audit: **COMPLETE**
- Phase 06 revision candidates: **NOT STARTED**
- Upstream VED equation audit / core revision: **CLOSED / CLOSED**
- 対象は既存modelの有限再実行、artifact provenance、model-local dependenceとbiological correspondenceの分離。
- source / equation / claim / tracked output / PDFの編集なし。parameter探索・最適化・retuningなし。
- 新model family・dataset・bridge・notation・theory・revision dispositionなし。外部web researchなし。

Authorityは[README](README_ja.md)、[Phase 00](00_dependency_and_inheritance_record_v0.1_ja.md)、
[Phase 01](01_equation_and_symbol_inventory_v0.1_ja.md)、
[Phase 02](02_equation_role_and_biological_role_audit_v0.1_ja.md)、
[Phase 03](03_preload_boundary_and_circularity_audit_v0.1_ja.md)、
[Phase 04](04_claim_and_evidence_burden_audit_v0.1_ja.md)。
上流[frozen dispositions](../ved_equation_audit/06_final_audit_record_v1.0_ja.md)を変更しない。
S/BIO-EQ/CLM/GAP/U/EM/DOWNの既存IDを継承する。
今回のRUN/ART/DSは監査記録用IDであり理論notationではない。

## 1. Audit guards

以下は比較のguardsであって、妥当性・不可能性のverdictではない。

- reproduced simulation ≠ empirical validation
- tracked figure ≠ run provenance
- parameter robustness ≠ biological robustness
- ablation sensitivity ≠ causal biological mechanism
- model observable ≠ biological observable
- visual resemblance ≠ measurement correspondence
- mode dependence ≠ falsification
- finite reproducibility ≠ cross-model universality
- same output pattern ≠ same biological process

既存の weaker formal / finite supportを、stronger biological burdenが残ることによって消さない。
本稿のrunは新たな**model-local audit observations**を加えるが、新biological evidenceは加えない。
Phase 04のburdenを上書きせず、後続phaseへscope付きで引き渡す。

## 2. Simulation source / artifact authority

| Artifact ID | Source | Role | Current? | Executable? | Generated from what? | Provenance status |
|---|---|---|---|---|---|---|
| ART-01 | S21 [simulate.py](../../bio-ifgt/simulations/minimal_neural_field/simulate.py) | finite model / plotting authority | YES | YES | authored code | SHA-256を§23固定、無改変import / CLI実行 |
| ART-02 | S22 [simulation README](../../bio-ifgt/simulations/minimal_neural_field/README.md)、[requirements](../../bio-ifgt/simulations/minimal_neural_field/requirements.txt) | documented command / toy limits | YES | command / dependencies | authored docs | default commandとruntimeを照合 |
| ART-03 | S14 [toy manuscript](../../bio-ifgt/sections/minimal_developmental_simulation.tex) | paper equations / interpretation | YES | NO | EN entryからinput | continuous expressionsをcodeと自動同一視しない |
| ART-04 | S15 [results manuscript](../../bio-ifgt/sections/simulation_results_visualization.tex) | numerical observations / captions | YES | NO | EN entryからinput | 7 tracked PNGを参照、原run manifestは付属しない |
| ART-05 | S24 [outputs](../../bio-ifgt/simulations/minimal_neural_field/outputs/)のtracked 7 PNG | paper-distributed finite figures | YES | NO | generator pathあり | §6でcurrent defaultとの全画素一致を確認 |
| ART-06 | S24 local ignored fig1–7 PNG / fig8 GIF | local alternate artifacts | current authorityとは区別 | NO | historical local lineage未固定 | fig8 GIFはfreshとframe pixels不一致、原config不明 |
| ART-07 | [EN main.pdf](../../bio-ifgt/main.pdf)、[JA main.pdf](../../bio-ifgt/main_ja.pdf) | current distribution | YES | NO | [EN TeX](../../bio-ifgt/main.tex)、[JA TeX](../../bio-ifgt/main_ja.tex) | 図の埋込RGBとtracked PNG照合、全文再build監査ではない |
| ART-08 | [JA working Markdown](../../bio-ifgt/sections_ja/)、[handoff](../../bio-ifgt/notes/handoff.md) | working version / design | source hierarchyに従う | NO | authored variants | probability/signatureの差を修復しない |
| ART-09 | 今回temp RUN-01–24 | audit-generated witness / manifest | 今回の有限実験 | YES | ART-01 unchanged + temporary instrumentation | §23のcommand / parameter / hashesで識別 |

PNG名だけから過去のseed・環境・全parameterを確定しない。pixel reproductionはcurrent generatorとの対応であり、historical run identityの逆算ではない。
PDF skillに従い、既存pypdfで抽出し、Poppler不在のため既存CoreGraphics rendererを代替使用した。PDF再生成・配布物の置換なし。

## 3. Environment and reproducibility

| Item | Observed |
|---|---|
| Runtime | /opt/miniconda3/bin/python, Python 3.13.5 (Anaconda, Clang 14.0.6), macOS-26.6.2-arm64 |
| Packages | numpy 2.3.3; matplotlib 3.10.7; imageio 2.37.3; Pillow 12.0.0 |
| Requirements | declared packagesを既存環境でimport成功。install・requirements変更なし |
| Alternative interpreter | /usr/bin/python3 3.9.6ではimageio未導入。simulationは上記既存環境で成功し、制約を回避するsource修正はしていない |
| PDF extraction | 既存pypdf 6.16.1、EN28 / JA21 pages |
| PDF rendering | 既存Swift / CoreGraphics renderer、module cacheとPNGはtempのみ |
| Seed | np.random.default_rng(SEED), default 7 |
| Cache / bytecode | MPLCONFIGDIR / XDG_CACHE_HOMEはtemp; import wrapperはsys.dont_write_bytecode=True |
| Default execution | RUN-01/02 exit 0、GIF込み。初回font cache準備以外に実行を妨げるdependencyなし |

temporary rootは ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn 。
`audit_runner.py`は元moduleのrun_simulationをそのまま呼び、sys.settraceでstep checkpointを採取する。
摂動runだけstep 800の配列を指定量変更し、以後同じupdateを続ける。
function bodyの代替実装、parameter最適化、equation修正は行っていない。

## 4. Default rerun

documented defaultのmodel parameterを一切変えず、保存先だけtempへ変更した。
RUN-01/02の実commandは§23に全記載。GIFはdefault通り有効、800更新、128×128、DT=0.08、
central_band / central_band_window / enable_eye=True、seed=7。
RUN-03/04はraw arraysの照合用に同じdefaultをAPIで再実行し、GIF保存のみ無効化した。
CLIで未保存のarraysを取得するinstrumentation controlであって別modelではない。

全定数は§23。M/N/B/Eはzero、Iはscale=0.0001のseeded perturbation。
各CLI runは14 PNG + 1 GIF（81 frames）を生成。stdoutにmodel/geometry/options、mean/max/fractionが出る。
出力先行を除くstdoutは一致する。S15自体には以下のmean/maxの数値表はないため、
「paper掲載数値を再現した」とは記さず、**current S21 stdout / raw arraysの再現**とする。

| Field | Mean | Max | Fraction > 0.5 |
| --- | --- | --- | --- |
| M | 1.833025 | 20.974771 | 0.260498 |
| I | 4.443594 | 48.765219 | 0.299805 |
| N | 0.268697 | 1.000000 | 0.266602 |
| B | 0.338513 | 1.000000 | 0.196228 |
| E | 0.080327 | 0.999999 | 0.079102 |

## 5. Determinism

| Comparison | Test | Result |
|---|---|---|
| RUN-01 / RUN-02 | 14 PNG + GIFのSHA-256 | 15/15 byte一致 |
| 同上 | decoded PNG pixels / GIF全81frame RGB | 全一致 |
| 同上 | stdout | output path 2行を除き一致、診断数値一致 |
| RUN-03 / RUN-04 | M/I/N/B/E ndarray raw bytes | 5/5一致 |
| API / CLI | defaultの同title/cmap 5 v2 field PNG | 5/5 byte一致 |
| Overall | same source / config / environment | **BYTE / NUMERICAL DETERMINISTIC** |

別OS・別BLAS・別package環境の独立再現を実施したとはしない。
tracked PNGとのmetadata/圧縮差は、上記同環境rerun間の非決定性ではない。

## 6. Tracked-output correspondence

全7 PNGは900×810 RGBA、decoded全画素差0（MAE=0）。
file hashは0/7一致。Software tEXtはtracked Matplotlib 3.9.4 / fresh 3.10.7で異なり、
IDAT compressed payloadも異なる。従って「差はmetadataだけ」とは断定しない。
status名は **PIXEL MATCH / METADATA DIFFERENCE**、圧縮byte差も併記する。

| Output | Fresh counterpart | Pixel/array match? | Hash match? | Current provenance status |
| --- | --- | --- | --- | --- |
| `boundary_field_final_v2.png` | RUN-01/boundary_field_final_v2.png | 全画素YES / 原raw arrayなし | NO | PIXEL MATCH / METADATA DIFFERENCE（IDAT差あり） |
| `combined_fields_with_eye_v2.png` | RUN-01/combined_fields_with_eye_v2.png | 全画素YES / 原raw arrayなし | NO | PIXEL MATCH / METADATA DIFFERENCE（IDAT差あり） |
| `eye_commitment_final_v2.png` | RUN-01/eye_commitment_final_v2.png | 全画素YES / 原raw arrayなし | NO | PIXEL MATCH / METADATA DIFFERENCE（IDAT差あり） |
| `information_density_final_v2.png` | RUN-01/information_density_final_v2.png | 全画素YES / 原raw arrayなし | NO | PIXEL MATCH / METADATA DIFFERENCE（IDAT差あり） |
| `morphogen_final_v2.png` | RUN-01/morphogen_final_v2.png | 全画素YES / 原raw arrayなし | NO | PIXEL MATCH / METADATA DIFFERENCE（IDAT差あり） |
| `neural_commitment_final_v2.png` | RUN-01/neural_commitment_final_v2.png | 全画素YES / 原raw arrayなし | NO | PIXEL MATCH / METADATA DIFFERENCE（IDAT差あり） |
| `neural_eye_overlay_v2.png` | RUN-01/neural_eye_overlay_v2.png | 全画素YES / 原raw arrayなし | NO | PIXEL MATCH / METADATA DIFFERENCE（IDAT差あり） |

current EN PDF pp.19–25の7 embedded RGB images、JA pp.17–20の同7 imagesはtrackedのdecoded RGBと全一致。
各pageをrenderしてtitle / caption / contour / relative lobe配置も視認した。
これはdistributionの**図version**の対応であり、PDF全数式や全claimのclosure監査ではない。

S15が示すunprefixed development_v2_hierarchical.gifは作業開始時repository内に存在せず、今回tempに生成できた。
既存ignored fig8_development_v2_hierarchical.gifは81framesだが、fresh GIFとbyte / decoded RGBの両方で不一致。
その差から原因parameterや旧modelを推測しない。U16のhistorical lineageは未解決のまま。
tracked画像は一切上書きしていない。

## 7. Reported-result reproduction

| Reported result | Fresh run result | Match status | Claim scope |
|---|---|---|---|
| S15 central M/I profiles | 両者中央peak、§4数値 / PDF figs1–2の画素一致 | reproduced | finite prescribed-source response |
| S15 central neural-plate-like N | N >0.5: 4368 cells、x46–81、y0–127 | reproduced | neuralはmodel label |
| S15 boundary-like B bands | relative high bands、B/G_norm spatial correlation 0.949549 | qualitative reproduced | accumulated Bとinstant gradientは別物 |
| S15 / S22 paired eye-like lobes | 明るい左右lobe、中央は相対的に低い | visually reproduced | 二つの独立した器官・connected componentsとはしない |
| S15 central region does not produce E | E[63,63]=0.689486、E[64,64]=0.704404; >0.5 maskは全体1 component | literal zero/exclusionとは一致しない | central contrast低下とEの不存在を分離 |
| S21 mean/max/fraction | RUN-01/02 stdout同値、RUN-03/04 raw同値 | reproduced | numerical observationのみ |
| S15 stages / GIF | 0/200/400/800の発達を視認、81 frames生成 | finite temporal sequence reproduced | N→Bの直接因果入力は示さない |
| S15 stable solutions | 800の図は一致するが§13で1600/3200まで変化 | finite final imageのみ一致 | long-time stationarityと同一でない |
| S15 structural possibility / not biological mechanism | 既存toyとして再現できる | sourceの限定を維持 | empirical observationに変換しない |

connected componentは監査用に4-neighbor・threshold >0.5で数えた。
defaultのN/B/Eはいずれも1 component。これは図中の二つのbright lobesを否定するものではなく、離散topologyの読みを限定する。
GIFはM/I/N/E-over-N表示で、Bの専用panelもfast/slow測定panelもない。

## 8. Paper/code execution correspondence

「Affects reported pattern?」の未実施counterfactualを、実測したeffectと混同しない。
今回はsource variantを直すためのraw-G置換やDT統一などのmodel redesignをしていない。

| Difference | Affects execution? | Affects reported pattern? | Source currently describes accurately? | Status |
|---|---|---|---|---|
| BIO-EQ-27 raw G vs code G_norm | YES、globalmax+1e-8でnormalizeしてB入力 | current normalized ruleでtracked再現。raw置換差は未測定 | paper raw / code normalizedは既存variant | execution identityを区別 |
| paper S vs sigmoid k8 / eye_sigmoid k20 | YES | current二種類で再現。k統一試験なし | one Sで全codeを同一視できない | version distinction維持 |
| DT on M/I, not N/B/E | YES | current per-step commitmentで再現。DT統一差未測定 | paper continuousとcode step-rate差 | biological time calibrationなし |
| new M→I, new N/B→E | YES sequential | current順序で再現。simultaneous update対照なし | continuous expressionsだけから順序は読めない | explicit implementation dependency |
| clipping / exponential clipping | codeに実在 | current有限runで使用、除去影響未測定 | codeが実行authority | constraint / numerical operation |
| source modes | YES | RUN-15でN/B/Eが左へ変化 | docsに既存modeあり | positionとamplitude/profileの複合変更 |
| eye modes / disabled | YES | RUN-16–19でalias一致 / E変形 / zero | docsに既存modeあり | window dependence実測 |
| compact N→B | NO direct code input | theta_N±10%でもB配列はdefaultと同一 | actual I→G_norm→B、paper sequenceとの差 | VR-11/12 / GAP-15維持 |
| B equals gradientという短縮 | Bはthresholded accumulating state | default B_min=0.176440、長runでは全grid >0.5 | instantaneous extractionとの同一視は不可 | formal role / executionを分離 |

## 9. Parameter sensitivity

RUN-05–19は全て800steps。globalを各run後defaultへ戻し、一因子ずつ変更した。
scalarは事前に選んだ±10%のみ。複数parameter探索や結果に合わせた選び直しをしていない。
fractionは監査用model maskでありbiological area fractionではない。

| Test ID | Changed parameter | Default → test | N >0.5 | B >0.5 | E >0.5 | Components N/B/E |
| --- | --- | --- | --- | --- | --- | --- |
| RUN-05 | SEED | 7 → 3 | 0.266602 | 0.195984 | 0.079224 | 1/1/1 |
| RUN-06 | SEED | 7 → 11 | 0.266602 | 0.196106 | 0.079163 | 1/1/1 |
| RUN-07 | SOURCE_STRENGTH | 1 → 0.9 | 0.261475 | 0.196228 | 0.078857 | 1/1/1 |
| RUN-08 | SOURCE_STRENGTH | 1 → 1.1 | 0.270020 | 0.196228 | 0.079102 | 1/1/1 |
| RUN-09 | D_M | 0.45 → 0.405 | 0.261230 | 0.194580 | 0.077393 | 1/1/1 |
| RUN-10 | D_M | 0.45 → 0.495 | 0.270020 | 0.200989 | 0.080322 | 1/1/1 |
| RUN-11 | THETA_N | 1.15 → 1.035 | 0.270752 | 0.196228 | 0.079102 | 1/1/1 |
| RUN-12 | THETA_N | 1.15 → 1.265 | 0.261230 | 0.196228 | 0.078857 | 1/1/1 |
| RUN-13 | THETA_B | 0.55 → 0.495 | 0.266602 | 0.227661 | 0.087341 | 1/1/1 |
| RUN-14 | THETA_B | 0.55 → 0.605 | 0.266602 | 0.177856 | 0.071533 | 1/2/2 |
| RUN-15 | source_mode | central_band → left_edge | 0.092896 | 0.067749 | 0.030640 | 1/1/1 |
| RUN-16 | eye_mode | central_band_window → central_pair | 0.266602 | 0.196228 | 0.079102 | 1/1/1 |
| RUN-17 | eye_mode | central_band_window → edge_pair | 0.266602 | 0.196228 | 0.138306 | 1/1/1 |
| RUN-18 | eye_mode | central_band_window → single_pair | 0.266602 | 0.196228 | 0.070984 | 1/1/1 |
| RUN-19 | enable_eye | true → false | 0.266602 | 0.196228 | 0.000000 | 1/1/0 |

seed3/7/11はcentral coarse patternを保持。source/D_M/theta_N±10%でもcoarse locationとN→Eのconditional patternは残る。
theta_B+10%ではB/Eの>0.5 component数が1から2へ変わる。従って**coarse patternの限定的な局所頑健性**と**mask topologyの感度**は併記する。
この小近傍を超えるparameter robustness・organism robustness・universalityを推定しない。

## 10. Eye-window dependence

**STRONGLY WINDOW-DEPENDENT（model-local）**。
N/Bが同じでもwindow変更でEの広がり・重心・threshold areaが変化する。
central_pairはcentral_band_windowの同じGaussianのaliasなので、RUN-16は独立な異なる構成の再現ではない。
edge_pairはy=0.35/0.65の重ね合わせで縦方向に広がり、single_pairは追加x gateで非対称になる。
no-eyeではEが全zero、M/I/N/Bはdefaultと同一。

defaultの2 bright lobesと、>0.5の1 connected regionを区別する。
source mode変更ではN/Bとのoverlapも変わるため、Eの差をwindow単独効果とはしない。
EM-04 OUTPUT-LOCATION PRELOADEDは、完成画像が入力されるという意味ではない。
sourceはsmooth positional preferenceを与え、patternはその条件下で生じる。
位置free spontaneous organizationやeye biological mechanismをこの試験から追加主張しない。

## 11. Boundary-field dependence

BはIのnormalized gradientを入力とするthresholded accumulating state。
seed差は小さいmask差、theta_N変更ではB raw array不変、theta_B±10%ではareaとconnectednessが変わる。
D_M±10%でもband width/areaが変化し、source modeではbandが左へ移る。
default correlation 0.949549は瞬間の空間関係であり、B=G_normのidentityや機構的同定ではない。
3200stepsではB_min=0.539937、全gridが>0.5となるので、同じmaskを長時間「境界だけ」と読むことはできない。
gradient-sensitive constructionとの整合的な有限応答を観察したが、生物膜/organism boundary形成とはしない。

## 12. Neural-pattern dependence

Nのcentralityはcentral source/Iに依存する。
seed3/11ではほぼ同じ中央band。theta_N±10%でfractionは0.270752 / 0.261230へ変化し、default0.266602を挟む。
left_edgeではfraction0.092896の左側patternとなる。神経組織の位置予測ではなく、source/threshold下のmodel maskである。
Nは800以後も増加・拡幅する（§13）。finite final-step persistenceを神経発達の安定性としない。

## 13. Long-time behavior

| Run / steps | M mean | I mean | N mean | B mean | E mean | N/B/E fraction >0.5 |
|---|---|---|---|---|---|---|
| RUN-03 / 800 | 1.833025 | 4.443594 | 0.268697 | 0.338513 | 0.080327 | 0.266602 / 0.196228 / 0.079102 |
| RUN-20 / 1600 | 2.101139 | 7.841718 | 0.344616 | 0.491505 | 0.124964 | 0.339355 / 0.275696 / 0.121643 |
| RUN-21 / 3200 | 2.146092 | 9.498429 | 0.405387 | 0.682022 | 0.185459 | 0.393799 / 1.000000 / 0.181152 |

| Step | M last-step max change | I | N | B | E |
|---|---|---|---|---|---|
| 800 | 0.00583647 | 0.0559715 | 0.00656625 | 0.000978588 | 0.00453783 |
| 1600 | 0.000637372 | 0.0188170 | 0.00287741 | 0.000421735 | 0.00203463 |
| 3200 | 0.00000975003 | 0.00143515 | 0.000609528 | 0.000145585 | 0.00324152 |

分類は **CONTINUES EVOLVING**、一部高値pixelの**NUMERICAL SATURATION**を伴う。
M/Iの変化は小さくなるが3200でゼロではない。N/B/Eの最大値がほぼ1でも場全体のstationarityを意味しない。
Bのmask拡大、N/Eの拡幅、Eのlast-step最大変化が3200でも約0.00324であることを確認した。
長runのrenderは相対色だけでなくcolorbar最小値とraw arrayを併読した。
CLM-45へは「800のfinite shapeが再現」「3200までは変化継続」の両方を引き渡し、stability proofを作らない。

## 14. Post-formation perturbation

step800、元loopの次update前に1回だけ介入し、3200まで同一式を継続。
controlはRUN-21の**同時刻**array。成長しているunperturbed trajectoryと比べ、800の静止画像への復帰とはしない。
診断上のrecoveryは「対象fieldの全grid RMS差が、介入直後に対して90%以上減少」と定義した監査上の有限閾値であり、
biological criterionでもsourceの既存定義でもない。whole-state recoveryとは別に集計する。

| Run | Intervention at step800 | RMS immediately after | RMS at3200 | Ratio | Finite result |
|---|---|---|---|---|---|
| RUN-22 | I×1.05, rows48:80 / cols48:80 | 0.3492313963 | 0.0050208851 | 0.014377 | 98.56%減少、I relaxation |
| RUN-23 | N−0.05 clipped, rows48:80 / cols48:80 | 0.0125000000 | 0 (numerical) | 0 | high-N領域のrecommitment |
| RUN-24 | N+0.05 clipped, rows48:80 / cols16:32 | 0.0088388348 | 0.0087636574 | 0.991495 | 試験時間内の90% recoveryなし |

sliceはPython half-open、image上の物理長単位ではない。
RUN-22の3200でN/B/E RMS差は0.000193205 / 0.000424139 / 0.000672361と残る。
RUN-23はNが2400までにcontrolと数値一致、E差は3200で約5.95e-14。
RUN-24はN正のoffsetがほぼ残り、Eにも約0.000115265の差が残る。
未試験の逆向き同位置pair、B/E直接破壊、大擾乱、無限時間復帰については結論しない。

## 15. Regeneration / return check

N/B/E updateはbounded stateに非負incrementを足す形で、現行sourceにはそれらを内生的に減らす項がない。
clipはboundedness操作であってdecommitment / repair ruleではない。
RUN-23の減少後の回復は、sourceの正方向accumulationが高値へ再度進む例。
RUN-24では低値領域への増加を取り去るrecoveryを3200まで観察しなかった。
Iのdiffusion/decayによるrelaxationとこのcommitment挙動を混同しない。

target-field finite recovery 2件 / no-recovery 1件。
内訳はI relaxation 1、N monotonic recommitment 1であり、一般的なbidirectional returnや生物再生の2事例とはしない。
Bio-localに既存regeneration-specific protocol/resultはlocateせず、今回もsmall state interventionのみ。
CLM-21のlarger disturbance後のlife-attractor reconstructionをtoyへの新しい同定mapで補わない。

## 16. Attractor terminology vs executable evidence

| Term | Executable evidence located | Strongest model-local reading | Stronger reading not established |
|---|---|---|---|
| stable final pattern | default画像を再現、long-run変化も観察 | 指定finite horizonの再現可能なpattern | exact stationary solution / asymptotic stability |
| attractor-like | constrained organization、partial saturation、I relaxation | 限定されたmodel descriptionとしての類比 | basin / invariant region / existence / uniqueness theorem |
| attractor / life attractor | toy内にOmega_life membership実装なし | manuscriptのregion interpretationと区別 | toyがlife attractorを実装・証明 |
| return | I perturbation decay、N recommitment | specified field / intervention / timeでの有限応答 | arbitrary-direction return |
| robustness | seedsと±10%のcoarse pattern維持、topology変化あり | tested neighborhood限定 | biological / universal robustness |
| regeneration | small interventionsのみ、large reconstruction testなし | relaxation / recommitmentを分離した有限観察 | biological regeneration mechanism |

## 17. Biological observable correspondence

| Model variable | Biological label | Explicit measurement map? | Units/calibration? | External data counterpart? | Current correspondence status |
|---|---|---|---|---|---|
| M | morphogen | 実際の物質名・濃度measurementへのmapなし | physical calibration未表示 | modelに使用なし | QUALITATIVE BIOLOGICAL ANALOGY |
| I | biological constraint density / retained bias | operational proxy選択mapなし | toy array、physical units未表示 | 使用なし | PROPOSED CORRESPONDENCE |
| N | neural commitment | cell-fate assayへのmapなし | clipped0–1 state、確率校正ではない | 使用なし | QUALITATIVE BIOLOGICAL ANALOGY |
| B | boundary stabilization | membrane/boundary測定mapなし | clipped0–1 accumulated state | 使用なし | QUALITATIVE BIOLOGICAL ANALOGY |
| E | eye-like commitment | eye tissue/organ測定mapなし | clipped0–1 state | 使用なし | QUALITATIVE BIOLOGICAL ANALOGY |
| G / G_norm | spatial gradient / normalized update input | biologyへの独立mapなし | grid差分・global normalization | 使用なし | MODEL-ONLY |

0–1、fraction >0.5、contour、RGB normalizationはmodel診断・表示であってbiological calibrationではない。
J/Phi/tau/DNA/theta(s)/Omega_life/Omega_intelの独立fieldや測定protocolはこの実行modelに実装されていない。
これをsource-local定義の否定とはせず、toyからそれらへの橋を追加しない。

## 18. Empirical-data inventory

| Data ID | Artifact / search scope | Source/provenance | Used by model? | Biological? | Current role |
|---|---|---|---|---|---|
| DATA-01 | Bio tracked 7 PNG + local alternate PNG/GIF | code-generated pattern | outputであってinput dataではない | biological labels付きmodel | VISUAL / DIAGNOSTIC OUTPUT |
| DATA-02 | Bio PDF / TeX / READMEのgeneric observation言及 | authored descriptions | loaderなし | biologyへの言及あり | paired measurement tableではない |
| DATA-03 | repository CSV/TSV/JSON search | 主にVol.4 / dimensionality simulation、AI Spine metadata | Bio modelは使用しない | Bio measurementではない | 他枝dataをBio証拠に転用しない |
| DATA-04 | Bio microscopy / accession / dataset URL / experiment protocol / calibration search | 対応する実測artifactをlocateせず | NO | 該当なし | EVIDENCE NOT LOCATED（探索範囲付き） |

Bio current tracked source、working JA、simulation docs/code、PDF text、output filenamesを確認。
repositoryのCSV/TSV/JSON候補とmicroscopy/experiment/data/accession語を探索したが、
Bioで使用される外部生物dataset、直接measurement、model-data paired tableは0件。
「存在し得ない」「生物学的にfalse」ではない。今回外部dataを導入せず、外部webも開かない。
current Bioに「validated / confirmed experimentally / quantitative fit / prediction confirmed」を達成済みmodel-data比較として述べる箇所はlocateしない。
generic biological observations / empirical future-work languageを実験成功の報告と数えない。

## 19. Literature / citation usage

[refs.bib](../../bio-ifgt/refs.bib)には8entries：
Wolpert2015 / Turing1952 / Kauffman1993 / Prigogine1984 / Hopfield1982 / Friston2010 / Waddington1957 / Murray2002。
current EN/JA TeXでcite / nocite / bibliography / printbibliography / addbibresourceによる参照・組込みをlocateしない。
よって「refs.bibがある」ことをmodelと実験のcitation-linked comparisonとしない。
S14等のreaction–diffusion背景説明は残すが、特定reference内の結果・dataを本監査が読んだことにはしない。
外部文献本文は閲覧していない。現在の実績はbibliographic background候補の所在であり、paired empirical evidenceではない。

## 20. Downstream fast/slow attribution

CLM-50 / DOWN-01：
[consciousness SSO](../../consciousness/sections/sso.tex):9–23、
[JA SSO](../../consciousness/sections_ja/sso_ja.tex)のBio simulation “confirmed” attributionを照合した。

**NO BIO-LOCAL FAST/SLOW CONFIRMATION RESULT LOCATED**。

codeにはfixed ratesと時系列はあるが、fast/slow layerの操作的criterion、rate-ratio analysis、
relaxation-time fit、dedicated diagnostic、比較tableはない。
GIFのstage表示や異なる変数の立上がり順序はその専用確認と同一ではない。
今回のsnapshot/perturbationも新たなtimescale-separation testを設計したものではなく、このattributionを遡及的に満たさない。
Bio source / stdout / tracked figures / GIF / EN PDFに専用結果なし。CLI helpの“faster checks”は実行時間の語。
DOWN-05/06のtheta/Fやsecond-attractorの“same role/structure”も、今回translationの測定はない。
下流sourceは編集せず、Phase 06以降のattribution判断へ引き渡す。

## 21. Inter-individual attribution

CLM-53 / DOWN-07の[II social](../../intelligence-part2/sections/09_social_blockchain_ja.tex)にある
「Bioが個体間相互拘束による準閉包維持を示した」という元成果を探索した。
Bioの[second attractor](../../bio-ifgt/sections/intelligence_second_attractor.tex)末尾はinter-individual sharingをfuture extension / beyond minimal frameworkとする。
[discussion](../../bio-ifgt/sections/discussion.tex)もfuture interactionを述べる。
current toyには個体index、複数organism、相互coupling、social/shared-field実験はない。
**NO BIO-LOCAL INTER-INDIVIDUAL CONSTRUCTION / RESULT LOCATED**。
system/environment exchangeや将来sharingへの言及は、個体間maintenanceの実証・構成と同一ではない。

DOWN-01/07を重点照合し、DOWN-02/03のwindow comparison、DOWN-04のlife substrate、
DOWN-05/06のidentity pressure、DOWN-08のsummary repriseはPhase 04のscopeを保持する。
下流理論そのものの監査やhomology判定には進まない。

## 22. Cross-scale correspondence

CLM-43/46/47のmolecular / cell / tissue / whole-organism / IFGT / toy / cognitive layer間で、
typed carrier map、spatial/temporal calibration、scale-dependent parameter translation、
coarse-graining operator、preserved biological invariantをこのrepositoryのBio-local構成としてlocateしない。
G_normのnormalizationは同じfinite grid内の数値operationであって、それ自体scale bridgeではない。
Bio-local field再定義とsource-local対応languageは残し、same glyph / repeated analogyをidentityとしない。

上流RC-005/006/007/008/009/010/040/041は全てOPENのまま。
今回のarray再現やparameter dependenceによってC_ij→C、J_ij→vector、rho→continuum、
distance→metric、micro source→sigma、L carrier→tensor、time translation、VED/IFGT sigmaのいずれも閉じない。
[relation to note](../../bio-ifgt/sections/relation_to_note.tex)はL3/L1の説明を持つが、特定L1 noteのpath/versionが同sourceで指定されず、GAP-20のpaired locatorは未固定。

## 23. Run provenance manifest

各RUNの実行先は共通temp root / RUN-ID。
manifest.jsonにcommand、全module定数、実際のkwargs、seed、environment、code/wrapper hash、
runtime、各field mean/max/min/fraction、component、snapshot履歴、raw array hashes、generated artifact hashesを保存した。
moduleのSTEPS/ENABLE_GIF等とruntime overrideが異なる場合は**kwargsが実際の実行条件**である。
seed/source strength等はmanifest config.globals、steps/modesはconfig.kwargs、介入はconfig.perturbに明示する。

共通code SHA-256:
`f98e10a807a53b1448fdb9e994864c7448f5b07e61e89bf73abfce0401ee8d8e`

共通temporary runner SHA-256:
`51fd83a65672ee35ce8053cd739abbb0f866d085e39c815948c63776b35adcdf`

共通定数（モデルを改訂したparameterではなく実行baselineの転記）：

```json
{
  "GRID_SIZE": 128,
  "STEPS": 800,
  "DT": 0.08,
  "SEED": 7,
  "MODEL_VERSION": "v2_hierarchical",
  "SOURCE_MODE": "central_band",
  "ENABLE_GIF": true,
  "GIF_EVERY": 10,
  "GIF_FPS": 12,
  "D_M": 0.45,
  "LAMBDA_M": 0.03,
  "SIGMA_M_STRENGTH": 0.2,
  "SIGMA_M_BAND_WIDTH": 8,
  "SOURCE_STRENGTH": 1,
  "SOURCE_WIDTH": 0.035,
  "Y_WIDTH": 0.35,
  "D_I": 0.16,
  "LAMBDA_I": 0.02,
  "ALPHA": 0.09,
  "THETA_N": 1.15,
  "ETA_N": 0.03,
  "SIGMOID_K": 8,
  "ENABLE_EYE": true,
  "EYE_MODE": "central_band_window",
  "ETA_B": 0.02,
  "THETA_B": 0.55,
  "ETA_E": 0.02,
  "THETA_EN": 0.5,
  "THETA_EB": 0.5,
  "EYE_Y_WIDTH": 0.08,
  "K_EYE": 20,
  "PERTURBATION_SCALE": 0.0001
}
```

環境は§3共通。以下のcommandは実際の保存先を含む。
RUN-03–24のwrapperは元moduleをimportしてBASE globalsをresetし、下記configのみoverride。
GIFを無効にしたAPI runでもupdate数・式は変わらない。
snapshotsはstep0/100/200/400/600/800/801/900/1000/1200/1600/2400/3199/3200とlast step/直前のうちrun内のもの。
介入はstep800のcheckpoint保存前。full sourceを置換せず元function line eventで配列を参照した。

| RUN ID | Command | Config delta (baselineから) | Seed | Runtime seconds |
| --- | --- | --- | --- | --- |
| RUN-01 | `/opt/miniconda3/bin/python ${LOCAL_REPO}/bio-ifgt/simulations/minimal_neural_field/simulate.py --output-dir ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/RUN-01` | `{"kind":"cli"}` | 7 | 7.852 |
| RUN-02 | `/opt/miniconda3/bin/python ${LOCAL_REPO}/bio-ifgt/simulations/minimal_neural_field/simulate.py --output-dir ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/RUN-02` | `{"kind":"cli"}` | 7 | 5.286 |
| RUN-03 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-03` | `{}` | 7 | 2.239 |
| RUN-04 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-04` | `{}` | 7 | 0.727 |
| RUN-05 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-05` | `{"globals":{"SEED":3}}` | 3 | 0.557 |
| RUN-06 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-06` | `{"globals":{"SEED":11}}` | 11 | 0.533 |
| RUN-07 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-07` | `{"globals":{"SOURCE_STRENGTH":0.9}}` | 7 | 0.556 |
| RUN-08 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-08` | `{"globals":{"SOURCE_STRENGTH":1.1}}` | 7 | 0.502 |
| RUN-09 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-09` | `{"globals":{"D_M":0.405}}` | 7 | 0.513 |
| RUN-10 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-10` | `{"globals":{"D_M":0.495}}` | 7 | 0.482 |
| RUN-11 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-11` | `{"globals":{"THETA_N":1.035}}` | 7 | 0.492 |
| RUN-12 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-12` | `{"globals":{"THETA_N":1.265}}` | 7 | 0.484 |
| RUN-13 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-13` | `{"globals":{"THETA_B":0.495}}` | 7 | 0.486 |
| RUN-14 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-14` | `{"globals":{"THETA_B":0.605}}` | 7 | 0.501 |
| RUN-15 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-15` | `{"kwargs":{"source_mode":"left_edge"}}` | 7 | 0.482 |
| RUN-16 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-16` | `{"kwargs":{"eye_mode":"central_pair"}}` | 7 | 0.508 |
| RUN-17 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-17` | `{"kwargs":{"eye_mode":"edge_pair"}}` | 7 | 0.500 |
| RUN-18 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-18` | `{"kwargs":{"eye_mode":"single_pair"}}` | 7 | 0.512 |
| RUN-19 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-19` | `{"kwargs":{"enable_eye":false}}` | 7 | 0.392 |
| RUN-20 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-20` | `{"kwargs":{"steps":1600}}` | 7 | 0.852 |
| RUN-21 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-21` | `{"kwargs":{"steps":3200}}` | 7 | 1.721 |
| RUN-22 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-22` | `{"kwargs":{"steps":3200},"perturb":{"field":"I","step":800,"slice":[48,80,48,80],"kind":"multiply","amount":1.05}}` | 7 | 1.680 |
| RUN-23 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-23` | `{"kwargs":{"steps":3200},"perturb":{"field":"N","step":800,"slice":[48,80,48,80],"kind":"add","amount":-0.05}}` | 7 | 1.639 |
| RUN-24 | `/opt/miniconda3/bin/python ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn/audit_runner.py RUN-24` | `{"kwargs":{"steps":3200},"perturb":{"field":"N","step":800,"slice":[48,80,16,32],"kind":"add","amount":0.05}}` | 7 | 1.690 |

以下は各runのraw metric要約。M/Iはmean/max、N/B/Eはmean/max/fraction >0.5。
CLIはstdoutに同じ値があり、raw array保存はAPI defaultで補う。

| RUN ID | M mean/max | I mean/max | N mean/max/fraction | B mean/max/fraction | E mean/max/fraction |
| --- | --- | --- | --- | --- | --- |
| RUN-01 | 1.833025/20.974771 | 4.443594/48.765219 | 0.268697/1.000000/0.266602 | 0.338513/1.000000/0.196228 | 0.080327/0.999999/0.079102 |
| RUN-02 | 1.833025/20.974771 | 4.443594/48.765219 | 0.268697/1.000000/0.266602 | 0.338513/1.000000/0.196228 | 0.080327/0.999999/0.079102 |
| RUN-03 | 1.833025/20.974771 | 4.443594/48.765219 | 0.268697/1.000000/0.266602 | 0.338513/1.000000/0.196228 | 0.080327/0.999999/0.079102 |
| RUN-04 | 1.833025/20.974771 | 4.443594/48.765219 | 0.268697/1.000000/0.266602 | 0.338513/1.000000/0.196228 | 0.080327/0.999999/0.079102 |
| RUN-05 | 1.833025/20.974771 | 4.443594/48.765221 | 0.268697/1.000000/0.266602 | 0.338518/1.000000/0.195984 | 0.080354/0.999999/0.079224 |
| RUN-06 | 1.833025/20.974771 | 4.443594/48.765222 | 0.268697/1.000000/0.266602 | 0.338372/1.000000/0.196106 | 0.080355/0.999999/0.079163 |
| RUN-07 | 1.649722/18.877294 | 3.999235/43.888697 | 0.264218/1.000000/0.261475 | 0.338635/1.000000/0.196228 | 0.080192/0.999999/0.078857 |
| RUN-08 | 2.016327/23.072248 | 4.887953/53.641741 | 0.272656/1.000000/0.270020 | 0.338418/1.000000/0.196228 | 0.080434/0.999999/0.079102 |
| RUN-09 | 1.833025/21.408043 | 4.443594/49.542638 | 0.264168/1.000000/0.261230 | 0.336419/1.000000/0.194580 | 0.079414/0.999999/0.077393 |
| RUN-10 | 1.833025/20.572595 | 4.443594/48.034608 | 0.273055/1.000000/0.270020 | 0.340556/1.000000/0.200989 | 0.081233/0.999999/0.080322 |
| RUN-11 | 1.833025/20.974771 | 4.443594/48.765219 | 0.277323/1.000000/0.270752 | 0.338513/1.000000/0.196228 | 0.080455/0.999999/0.079102 |
| RUN-12 | 1.833025/20.974771 | 4.443594/48.765219 | 0.262338/1.000000/0.261230 | 0.338513/1.000000/0.196228 | 0.080194/0.999999/0.078857 |
| RUN-13 | 1.833025/20.974771 | 4.443594/48.765219 | 0.268697/1.000000/0.266602 | 0.416644/1.000000/0.227661 | 0.088899/0.999999/0.087341 |
| RUN-14 | 1.833025/20.974771 | 4.443594/48.765219 | 0.268697/1.000000/0.266602 | 0.277398/1.000000/0.177856 | 0.073082/0.999999/0.071533 |
| RUN-15 | 0.197556/5.156624 | 0.478911/12.424748 | 0.096097/1.000000/0.092896 | 0.235875/1.000000/0.067749 | 0.031169/0.999994/0.030640 |
| RUN-16 | 1.833025/20.974771 | 4.443594/48.765219 | 0.268697/1.000000/0.266602 | 0.338513/1.000000/0.196228 | 0.080327/0.999999/0.079102 |
| RUN-17 | 1.833025/20.974771 | 4.443594/48.765219 | 0.268697/1.000000/0.266602 | 0.338513/1.000000/0.196228 | 0.140231/0.999999/0.138306 |
| RUN-18 | 1.833025/20.974771 | 4.443594/48.765219 | 0.268697/1.000000/0.266602 | 0.338513/1.000000/0.196228 | 0.072561/0.999990/0.070984 |
| RUN-19 | 1.833025/20.974771 | 4.443594/48.765219 | 0.268697/1.000000/0.266602 | 0.338513/1.000000/0.196228 | 0.000000/0.000000/0.000000 |
| RUN-20 | 2.101139/22.827242 | 7.841718/76.756364 | 0.344616/1.000000/0.339355 | 0.491505/1.000000/0.275696 | 0.124964/1.000000/0.121643 |
| RUN-21 | 2.146092/23.063921 | 9.498429/87.734206 | 0.405387/1.000000/0.393799 | 0.682022/1.000000/1.000000 | 0.185459/1.000000/0.181152 |
| RUN-22 | 2.146092/23.063921 | 9.499971/87.764802 | 0.405412/1.000000/0.393799 | 0.681931/1.000000/1.000000 | 0.185457/1.000000/0.181396 |
| RUN-23 | 2.146092/23.063921 | 9.498429/87.734206 | 0.405387/1.000000/0.393799 | 0.682022/1.000000/1.000000 | 0.185459/1.000000/0.181152 |
| RUN-24 | 2.146092/23.063921 | 9.498429/87.734206 | 0.406937/1.000000/0.393799 | 0.682022/1.000000/1.000000 | 0.185478/1.000000/0.181152 |

以下にgenerated artifact hashesを全run分保存する。metadataを含むfile bytesのSHA-256であり、
npz hashとndarray raw-byte hashは別物。RUN-01/02のGIFframe数は81。
tempは将来削除され得るため、このrecord内のcommand/config/数値/hashを恒久的な監査traceとする。
raw arrays / images / wrapper自体はrepositoryへ追加していない。manifest全詳細の保管場所は上記temp。

```json
{
  "RUN-01": {
    "artifacts": {
      "boundary_field_final_v2.png": "9807ad24575bfd3fec586dab50f76a5cc361bc9ba8785dc63231614a4302181c",
      "combined_fields_central_band.png": "eff15b055d46e8aa7e46b8c3cb567a5427d0aeb83e442f926b320a0a3c730a2f",
      "combined_fields_with_eye_central_band.png": "34cfbafb7508f5ccb47d829bc3649822256f4a43ad4708b37792c47fa6af4065",
      "combined_fields_with_eye_v2.png": "34cfbafb7508f5ccb47d829bc3649822256f4a43ad4708b37792c47fa6af4065",
      "development_v2_hierarchical.gif": "d088682257e8b3f02efc533b4181e07d0ff9b105bd7985867639e8bc103cf8d8",
      "eye_commitment_final_central_band.png": "af766efa6851c1d420615d79519c7de88e23f69346d38f2941c0c487aebed913",
      "eye_commitment_final_v2.png": "06ef0070f033097d39fb3a035729537e1d362082dc7027f75e556fa0dae05569",
      "information_density_final_central_band.png": "c4c1efbfa502c6862212cf8e6debaf9d401dadc39f4ce9f8f1dc40dde9dcbcee",
      "information_density_final_v2.png": "d1b05599f9687987814e3120ee69895fbd1eb4f4595b6b47d2c7f6a68a94a270",
      "morphogen_final_central_band.png": "135783f0defb1dadfa189f617684f273fb8255e8b6b185f48de388ee7d822034",
      "morphogen_final_v2.png": "61ea95f85f12e631c86a2f0b716f89ead672d91d112ad011e620f0facffae330",
      "neural_commitment_final_central_band.png": "ae62010fedf624594ec682da654245ca845a80f9f23314e9e2c1635f243d80d6",
      "neural_commitment_final_v2.png": "0eb9e570e1486de00ab66c727a776c660c35a01687cb08c37867a88973467aaa",
      "neural_eye_overlay_central_band.png": "5b5132d1960e2bc9768817c4181399e78bdfd36c13a11a336aad498623ad92d6",
      "neural_eye_overlay_v2.png": "5b5132d1960e2bc9768817c4181399e78bdfd36c13a11a336aad498623ad92d6",
      "stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout.txt": "c7b71af2828dafc121745d2d4b5357f68b9ad22828e06bc7242124da5e092834"
    },
    "raw_array_sha256": "not saved by original CLI"
  },
  "RUN-02": {
    "artifacts": {
      "boundary_field_final_v2.png": "9807ad24575bfd3fec586dab50f76a5cc361bc9ba8785dc63231614a4302181c",
      "combined_fields_central_band.png": "eff15b055d46e8aa7e46b8c3cb567a5427d0aeb83e442f926b320a0a3c730a2f",
      "combined_fields_with_eye_central_band.png": "34cfbafb7508f5ccb47d829bc3649822256f4a43ad4708b37792c47fa6af4065",
      "combined_fields_with_eye_v2.png": "34cfbafb7508f5ccb47d829bc3649822256f4a43ad4708b37792c47fa6af4065",
      "development_v2_hierarchical.gif": "d088682257e8b3f02efc533b4181e07d0ff9b105bd7985867639e8bc103cf8d8",
      "eye_commitment_final_central_band.png": "af766efa6851c1d420615d79519c7de88e23f69346d38f2941c0c487aebed913",
      "eye_commitment_final_v2.png": "06ef0070f033097d39fb3a035729537e1d362082dc7027f75e556fa0dae05569",
      "information_density_final_central_band.png": "c4c1efbfa502c6862212cf8e6debaf9d401dadc39f4ce9f8f1dc40dde9dcbcee",
      "information_density_final_v2.png": "d1b05599f9687987814e3120ee69895fbd1eb4f4595b6b47d2c7f6a68a94a270",
      "morphogen_final_central_band.png": "135783f0defb1dadfa189f617684f273fb8255e8b6b185f48de388ee7d822034",
      "morphogen_final_v2.png": "61ea95f85f12e631c86a2f0b716f89ead672d91d112ad011e620f0facffae330",
      "neural_commitment_final_central_band.png": "ae62010fedf624594ec682da654245ca845a80f9f23314e9e2c1635f243d80d6",
      "neural_commitment_final_v2.png": "0eb9e570e1486de00ab66c727a776c660c35a01687cb08c37867a88973467aaa",
      "neural_eye_overlay_central_band.png": "5b5132d1960e2bc9768817c4181399e78bdfd36c13a11a336aad498623ad92d6",
      "neural_eye_overlay_v2.png": "5b5132d1960e2bc9768817c4181399e78bdfd36c13a11a336aad498623ad92d6",
      "stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout.txt": "9f35f8995a2c8b6b75f65c020f20172f5dafac16736e20d777d371c51ea5fa88"
    },
    "raw_array_sha256": "not saved by original CLI"
  },
  "RUN-03": {
    "artifacts": {
      "B.png": "02cc251e7a92c24b6f5d096b13603ca0ecc47b3e941555f49abd2bf09de39330",
      "E.png": "01450ef4eabb79203b8bf011bc39f7ed5094495087a916bb032d7479702f877c",
      "N.png": "d45d7935e24b561d216178b8f7623c7e01d63a8f619ce83bfa00ce727257b00a",
      "arrays.npz": "c261226452269589b522d9d77b1e63b7b86c659c096ac957131c835e42db4c70",
      "boundary_field_final_v2.png": "9807ad24575bfd3fec586dab50f76a5cc361bc9ba8785dc63231614a4302181c",
      "eye_commitment_final_v2.png": "06ef0070f033097d39fb3a035729537e1d362082dc7027f75e556fa0dae05569",
      "information_density_final_v2.png": "d1b05599f9687987814e3120ee69895fbd1eb4f4595b6b47d2c7f6a68a94a270",
      "morphogen_final_v2.png": "61ea95f85f12e631c86a2f0b716f89ead672d91d112ad011e620f0facffae330",
      "neural_commitment_final_v2.png": "0eb9e570e1486de00ab66c727a776c660c35a01687cb08c37867a88973467aaa",
      "snapshots.npz": "862a07f6b1ab6acc10d8e951f37a86bbad82efe4e276db020e15ba4cef1283b4",
      "stdout.txt": "966a0dff9d9b4d8ce8524c17af1b193bced64b95b09a3f2641032bf68a2c8c60"
    },
    "raw_array_sha256": {
      "M": "605d79608f5079f4b1167c373b918116eb152c46894b0f51f544ef982652578f",
      "I": "0a11da77d397d57d4c187a1a8d38ee0c58da71c024ccbfd9691ac7a08bf7912a",
      "N": "60030ec9aa21379b70c37ae3097551d26924659e96dbe86dcc734992aa6cbfaf",
      "B": "2a250e943c0e80afcd78b6ef917ec3c639eda4ce6aed1c7069489ac2b2190c12",
      "E": "ac4dbd867e23576e46fccbd27fff7de44abcc735907abb2651b2610db3ed23fd"
    }
  },
  "RUN-04": {
    "artifacts": {
      "B.png": "ee1c67002e9a18900e33df2a7e0fbec00b836de07d23d6f04aea83f075ded5b8",
      "E.png": "962d3cc37b8d7dec344a515cd58a80aef67a2b15f2366c0aeb926df6ff97011a",
      "N.png": "aa61b2e4c21f2134d75363a450beac96b9ffd6816ce089adc42d7d9e398071b5",
      "arrays.npz": "c261226452269589b522d9d77b1e63b7b86c659c096ac957131c835e42db4c70",
      "boundary_field_final_v2.png": "9807ad24575bfd3fec586dab50f76a5cc361bc9ba8785dc63231614a4302181c",
      "eye_commitment_final_v2.png": "06ef0070f033097d39fb3a035729537e1d362082dc7027f75e556fa0dae05569",
      "information_density_final_v2.png": "d1b05599f9687987814e3120ee69895fbd1eb4f4595b6b47d2c7f6a68a94a270",
      "morphogen_final_v2.png": "61ea95f85f12e631c86a2f0b716f89ead672d91d112ad011e620f0facffae330",
      "neural_commitment_final_v2.png": "0eb9e570e1486de00ab66c727a776c660c35a01687cb08c37867a88973467aaa",
      "snapshots.npz": "862a07f6b1ab6acc10d8e951f37a86bbad82efe4e276db020e15ba4cef1283b4",
      "stdout.txt": "966a0dff9d9b4d8ce8524c17af1b193bced64b95b09a3f2641032bf68a2c8c60"
    },
    "raw_array_sha256": {
      "M": "605d79608f5079f4b1167c373b918116eb152c46894b0f51f544ef982652578f",
      "I": "0a11da77d397d57d4c187a1a8d38ee0c58da71c024ccbfd9691ac7a08bf7912a",
      "N": "60030ec9aa21379b70c37ae3097551d26924659e96dbe86dcc734992aa6cbfaf",
      "B": "2a250e943c0e80afcd78b6ef917ec3c639eda4ce6aed1c7069489ac2b2190c12",
      "E": "ac4dbd867e23576e46fccbd27fff7de44abcc735907abb2651b2610db3ed23fd"
    }
  },
  "RUN-05": {
    "artifacts": {
      "B.png": "00a9450243c8afba942b50362fb06145d1bd4aed72f5083a8668547eee06a6bd",
      "E.png": "0fc5cae95975f75553fc5bf0a410a392ccb75bef1016db66a4b77dc48480ca02",
      "N.png": "e5803186fdef7be23f743915daff3544cb99b355bf5f3a95c393b1b8e7963552",
      "arrays.npz": "f2d0442840e674eb57b50309cf0e204b9d2c231157af4ab7db02a7ae02bceef4",
      "snapshots.npz": "687b773a72ad3b702ee317e799f474e5c5a2fa67998b6743444c44b92448a39c",
      "stdout.txt": "5ffd7470af35a78909df28557f2ff56b6316ba9b0385991b2ef9f652acaf5dfe"
    },
    "raw_array_sha256": {
      "M": "605d79608f5079f4b1167c373b918116eb152c46894b0f51f544ef982652578f",
      "I": "d05fcdafbc2159d79582b096c7d8f98eea3a1b4c78c82d2de9cb920cf53bc73e",
      "N": "a263d180f3f6314788ba491783b05b93a0db82a854202c194fd259647da61274",
      "B": "55bae74a22a9b4779920c8a0ff130d27dc396f3c9ee77b9addc16a3e7d914504",
      "E": "41624bac6ae2dbf407f8a97f8193a4c306caac8dc1fee0ea2d050641da5f2cc5"
    }
  },
  "RUN-06": {
    "artifacts": {
      "B.png": "157cb968c2cce433d86fa01d17d8e8a5604d0961db01c70985f980f27d41b49b",
      "E.png": "2722226fc4ee4e8aed160f88075e558a40e09de72b29db032496ff9eb99d4b3c",
      "N.png": "cd82bd22f91a7818bce7c4fb7918487d2c60690cd2e5bd2ec786f0ddbc9a9d6d",
      "arrays.npz": "88bbb31f7e555ba4848a3a3a28a30f0cfb5eb70cb5eacc2630fd2e76fe23bd87",
      "snapshots.npz": "1fc851707641bc3fb092ebacafaf2940196b1a9378afa36ef8e3d9fdce91d1d1",
      "stdout.txt": "ff8accfb0457dbc454f6b049b884590ec0ad3147ea17da76a4d075935d43ef6f"
    },
    "raw_array_sha256": {
      "M": "605d79608f5079f4b1167c373b918116eb152c46894b0f51f544ef982652578f",
      "I": "ac094fd69dbe9a69808a154c16aadd65a1fac34df955a662ea0a584a3d0578da",
      "N": "d4ab2cadb898ea595db8c9f7c721c5db42db6efc483060350aafaada90462ddc",
      "B": "0bf6a957f9b626b5d7518568c02abb3843613f4caea7ebec8ba3ca22c1d05597",
      "E": "34519ebbeb9ae648bcc4d290b6c0ef48487c91b8be2115a9753e000a0279075c"
    }
  },
  "RUN-07": {
    "artifacts": {
      "B.png": "20818563284e93fabd1db85d24e35003276b42bb01bbdbce2f5f9d05fba42c74",
      "E.png": "62ece3de13ef2475d8183a02167723e48f00dfac581c537e968e62a32e02f228",
      "N.png": "5516c6a112e0766e338c24cc82b36bfcf018056142f0a67ba148aa0a45316851",
      "arrays.npz": "54d4e7e432fd78ecf8a08411ae547ea2ad94abacb16711355b39c3c0bbebed97",
      "snapshots.npz": "27b3eaf6f12b5232d7928743c02b664a56af9beb98fd9e1f89422638903d705f",
      "stdout.txt": "718e10f54d3e1c2469584681ed6b4bc55aa48805fe583914738b210007778e5d"
    },
    "raw_array_sha256": {
      "M": "bd0e5e299d1611d98d822d27c5d6cf8e5f7da690cd92792b65be380e09d96009",
      "I": "bdb51b594ce3e77cdac37363096ebd40b71340225cf503d2923b7f4e7cb9d6ea",
      "N": "9eedf9cd7c6f7ecaed05e66e1c431304969054645b5ed2492d587995b62144bb",
      "B": "37e109f12e33ecade853b191bfb57741a7ecee0f2fd06c5452efe90e95f38faf",
      "E": "4cee3988ded56945dc1a1a5a01096756e5841626114ffbf99b5a6537e88e5a78"
    }
  },
  "RUN-08": {
    "artifacts": {
      "B.png": "34103b0ee3ae0d7e58d06af9b17de97b0cff217bdf5ac8b7e972d429ca01a8ac",
      "E.png": "84edf0670cdad4cf1a722ec87a9987879fba4130c91572364064544bc129b33c",
      "N.png": "f6f423b7cae1ab6983055036ba34355ee2e2b81e1abcdadc5997839d00eab3b6",
      "arrays.npz": "bcb453670420cfe3f5847d1c47b15c2bf1f9e762801d0eba35b6bfafbe20e9ee",
      "snapshots.npz": "62ce0fc91e77ad8ceec337d11891cd0e70d79a4b7e516437ea2c3081d02d5c03",
      "stdout.txt": "d3566b8508661a2a47c25f910d82a8d02b012697c053c0cb1889e19e1c4434e4"
    },
    "raw_array_sha256": {
      "M": "e4f0c1ba7b6ac697a12dd3b4fd41fb416afe820602d18b3bbeae98ca09d6ce3b",
      "I": "d2246fbec3dbfd297360c18242bc0d736ac7f5afafa95a50c6d77c8ee772c153",
      "N": "1b8abd995e100ab736ea7286c2cc5a3e38127a2bd554805760e70d27fa97ea25",
      "B": "dddcb3b327887af344ecde424d22f501e2b81312509bfb1d220cd52898401a8a",
      "E": "331fcde3f86bc5a8be7972646ca278787c809233f1edb8ed2c2b3e9dcb04c2c6"
    }
  },
  "RUN-09": {
    "artifacts": {
      "B.png": "a94108b66ccf0ef0aede0d2c538db7ef7620dd07340e9fe5863f7304e73fc6ad",
      "E.png": "a503a0577ba4760cc8214046e6b8a547f59b093ac07ff673102ba60396748442",
      "N.png": "cb662876bc8749f708ded783ad79db055969428d93078a2e7f9d97b6e32917fc",
      "arrays.npz": "dea10b5d143cc777213aaeef9450283e56c3d479bf6a569e3d85ba005e3a246e",
      "snapshots.npz": "059ea6ca022f4ea5046bb361c1fb2b12b9affd544d0686d1a5e9ce8370738666",
      "stdout.txt": "ae2e9d907ee55cd415efeffa2b0217f54138191ebfc146a6fdbc68dfed431906"
    },
    "raw_array_sha256": {
      "M": "5c4a979d43298f5f30f8346865505d2b4ec2375d41c818cb589e5afb9487a833",
      "I": "1b14b79a0c5ab847bd70861701d2ad47b100260efe67e2e7fc16ebf848739626",
      "N": "0072f8e27fa48756a67f632249feaa36923b13bb4bcaf2758f804bb9edd22ce2",
      "B": "6ead4f3ff50ac90bb7727b312b68ca7262fd8eaf3a35a50d18c0f8c67fd9afd0",
      "E": "732a63ee928f340aaf8d1890a0abf827bce416a837c57f82f7b690a1f25618b9"
    }
  },
  "RUN-10": {
    "artifacts": {
      "B.png": "ea72a14345310bf9067ea2798fc086c8b9aed0f129dddb7c0ef2a07c1461f06e",
      "E.png": "207acea473b98e9704fe2a07ff7c1806491dd8e6cf4545b0690e6cf1bcc52abb",
      "N.png": "25650f77e45856fd13fc774ca353abeda29e37f40b1ea6a9ebff8b521b08d828",
      "arrays.npz": "f759ffd8f21cd5dbb40219e9dff6c888779d65c094f7d60d4438056d4f54851d",
      "snapshots.npz": "2e1aabc9272e47f122af08a8922ee0fc2b6b470e152705473016654a0ea0a698",
      "stdout.txt": "f420302b479809edce9df71646d729f52309fc6f39a1fe6ececba9a23f4b641a"
    },
    "raw_array_sha256": {
      "M": "ab5f6f80df9f801e66b20625242e70cf4f742129b6149dfadf652c50fe5205a6",
      "I": "fc9f32ddde617e71ee447420e72186170ba21c93d3a4269a3f03a610bb51eb3f",
      "N": "d2c2864338e1eadc696b94a1d4a129e6a36bd02db64ad500de1f47c87094c05a",
      "B": "aaa07a4a13d8fb30a16c3edd37edbeb3d2b27b3f4ee8b3ff229cea66018a2e46",
      "E": "cac997186ca35540d7cb5b4c130d0fe4b8cb28f25ce288c5094e7ce4e71673f5"
    }
  },
  "RUN-11": {
    "artifacts": {
      "B.png": "c74721eb5cd3f2004219488538509d4b528dd71d8a362c3806e53a37eef23c15",
      "E.png": "dd75da564cc73e1908237d3a8c5f21a0d87dab6ff4473e3699624f29753960d3",
      "N.png": "a592fe491df818c81be9aa00fa8e4e1cab79672b3d9accda8c58111195c0223c",
      "arrays.npz": "57b2cf1f4e52f80dab17584204b8deef73fa857ebe93cdbc49df4bad75e07898",
      "snapshots.npz": "407c34f9f48542c9af642d51241003f72cd087eb9aeea9196bc914ad2cba110b",
      "stdout.txt": "4322ebf174975b3758739159fc4e288e2ad3a463e4fa007fa4c3847abe6072a8"
    },
    "raw_array_sha256": {
      "M": "605d79608f5079f4b1167c373b918116eb152c46894b0f51f544ef982652578f",
      "I": "0a11da77d397d57d4c187a1a8d38ee0c58da71c024ccbfd9691ac7a08bf7912a",
      "N": "e2bc00015acb4a93dad0d39c87d8ca8a2aa1fbe3ea20c43331f6d9b5acf66144",
      "B": "2a250e943c0e80afcd78b6ef917ec3c639eda4ce6aed1c7069489ac2b2190c12",
      "E": "9863e64f78df0958c24378d2e5b7612be6dd6883eb33cd08733584c4fe0897d6"
    }
  },
  "RUN-12": {
    "artifacts": {
      "B.png": "c150477596f2862f05a054f031c17e15dde3ecee28f8deaabc175d540a08ea7f",
      "E.png": "dbd82382b2b29707bc90c39c44404c134bd90d00545f7092ffcf2087ae14e46b",
      "N.png": "4f261c3a8e24dd08ad873a675196a007daf0253be39e6a59759bb0c2f2255363",
      "arrays.npz": "36df29786807f29000ee6c183c227d78ea817b37d15e0f28d48d7909f1db9127",
      "snapshots.npz": "c15a902a64ea327a1d54b8f315442ea6b4ea50476eedf09ad693795d72c1be09",
      "stdout.txt": "001aaeccc1bf2169a8c2c6db69f0b502723df6db77d43646d9bec47896ea67e1"
    },
    "raw_array_sha256": {
      "M": "605d79608f5079f4b1167c373b918116eb152c46894b0f51f544ef982652578f",
      "I": "0a11da77d397d57d4c187a1a8d38ee0c58da71c024ccbfd9691ac7a08bf7912a",
      "N": "31954b1acf18e7e55b677e42a790fb50eb753d37d361af762a7bad4a21f799a3",
      "B": "2a250e943c0e80afcd78b6ef917ec3c639eda4ce6aed1c7069489ac2b2190c12",
      "E": "53374a191f17527962604b2fcc97e4801adf9d8962ff3d6b27cc7d36efa1acbb"
    }
  },
  "RUN-13": {
    "artifacts": {
      "B.png": "31975fc69603db97af59ea853cb076f8ee8cfd5401bcbc5befc0ae6c10a044d6",
      "E.png": "47913877271f5f2156601d330522d563b9ff871862b75e243182178d4e25ed19",
      "N.png": "71784a07f163605627af1900802db020cc6addec50d1e3f76d94e7f093093731",
      "arrays.npz": "a215cd943f612544ee58e7b9fde2d292c924ecba39b9076667a9ae9536e6596c",
      "snapshots.npz": "119ef7529d9c3836fb3b31698c2d2e5f5de91f86dffcdf830dcbc8469034b819",
      "stdout.txt": "df90c80965a7f88954adc2f10b22d3723ff87a82f0ad83df1296c5aa8a8b0977"
    },
    "raw_array_sha256": {
      "M": "605d79608f5079f4b1167c373b918116eb152c46894b0f51f544ef982652578f",
      "I": "0a11da77d397d57d4c187a1a8d38ee0c58da71c024ccbfd9691ac7a08bf7912a",
      "N": "60030ec9aa21379b70c37ae3097551d26924659e96dbe86dcc734992aa6cbfaf",
      "B": "72339472960b70c10f8bd2602dbc3843aa33e527c2c91318e2ce3d2772d27616",
      "E": "87117c8de9d478f5e2b4a1edd1ebd25804aca6163e3f450b0b597071d098ef23"
    }
  },
  "RUN-14": {
    "artifacts": {
      "B.png": "dd917248be58bde9a87c2c5a0e71c000749c8644377d20afa66cd1fd4e5e3423",
      "E.png": "45639fd9b4705434f70da1667416cc1c280c38c3d2ca0db85119fc5f1bded80f",
      "N.png": "1a645c082c76ad6eee3e4b079e70480353031bc54e1af7aac281b0da20a1a790",
      "arrays.npz": "f7f824f482a85a6bfd6408e533d6bb73f32bc52c4ffdc830d18f3bfcf94d2d43",
      "snapshots.npz": "23d37de1c645553a582a3c979284235d3581c3a752a20980bf925e3b4bfbe56d",
      "stdout.txt": "2133fc74c7eb777be70f23967678c2f21312b5da80cb13034cde9eae729f6b56"
    },
    "raw_array_sha256": {
      "M": "605d79608f5079f4b1167c373b918116eb152c46894b0f51f544ef982652578f",
      "I": "0a11da77d397d57d4c187a1a8d38ee0c58da71c024ccbfd9691ac7a08bf7912a",
      "N": "60030ec9aa21379b70c37ae3097551d26924659e96dbe86dcc734992aa6cbfaf",
      "B": "c4564361e5e5a36602fdcb9ff3e9031c699ec0f3ecb4b22c3a7be247cd879642",
      "E": "a069539d05deae7607d73d5da846d4306041ec822194e6d76e0aa3d6e6e70d89"
    }
  },
  "RUN-15": {
    "artifacts": {
      "B.png": "d9ab8fb019f83c389c503bdfee2f9a7dd83747984af10d5bb44f42b8e9bb877b",
      "E.png": "9c84f162a4da5ce7b7c467822c0938a27966487a81e4cb1c943ce8b38c9816a0",
      "N.png": "e4948e6551720b04b40fc0f473829697cce43602fc2e5cfe2a75672d2071397f",
      "arrays.npz": "245245bdd73e980520a89f95566ed8211415a5a39706f30d49bfa40d9e482f88",
      "snapshots.npz": "3b10ce6949581bb353830d99bc739fc339155d277c81ae75374e4dac57f90626",
      "stdout.txt": "0e0f93379e85a7abc8bdd5fc10201c1e521323b00096f2ec8680d916937d4af3"
    },
    "raw_array_sha256": {
      "M": "992e0d55e7995250b0f5420f3e5ec4a68623cb0a228feee0ff5fb467a4978691",
      "I": "70b564032717355b7b5b7ec39c51d3fa43cd20e9a8438d3f1e1e8294315da2ea",
      "N": "957cf289df5950c27e062d48ad0779fa271bfe5f2a5477b3ee7b5d19c1957633",
      "B": "f789d946f76e45200dd9e56e6c726afe33837d150f8c5a05388ef91e225c9ef6",
      "E": "ee213c6de7d2fa182b772c9ec9fdde97b913635f4b63824e5fd226e7fb14a8f8"
    }
  },
  "RUN-16": {
    "artifacts": {
      "B.png": "5f6e8c30a332263548a2fb86ec747934597a9bf16656dd3fc89aeb6a6e4b9e21",
      "E.png": "e031f234b5a545118097626316ac327de65b0da9f0e2bfa151a50fa6a58faf7a",
      "N.png": "206bff5bf3c15727ba58a0217e6fc3a1554f85c0263430b38bf828203df95fab",
      "arrays.npz": "c261226452269589b522d9d77b1e63b7b86c659c096ac957131c835e42db4c70",
      "snapshots.npz": "862a07f6b1ab6acc10d8e951f37a86bbad82efe4e276db020e15ba4cef1283b4",
      "stdout.txt": "bc5111ceea6616452840628d149653184227438ecab21dfbeea499e404332337"
    },
    "raw_array_sha256": {
      "M": "605d79608f5079f4b1167c373b918116eb152c46894b0f51f544ef982652578f",
      "I": "0a11da77d397d57d4c187a1a8d38ee0c58da71c024ccbfd9691ac7a08bf7912a",
      "N": "60030ec9aa21379b70c37ae3097551d26924659e96dbe86dcc734992aa6cbfaf",
      "B": "2a250e943c0e80afcd78b6ef917ec3c639eda4ce6aed1c7069489ac2b2190c12",
      "E": "ac4dbd867e23576e46fccbd27fff7de44abcc735907abb2651b2610db3ed23fd"
    }
  },
  "RUN-17": {
    "artifacts": {
      "B.png": "daaa997c77658243feda4e5904d74a0577dd28e5fa224731cf839dd31d6fb267",
      "E.png": "2cbb9a51f6cdbc1c705fe3b85d3b664d1623fee29a40a2ad5e8de92578dadf1f",
      "N.png": "04edd68c97c45e8a9dda37d3cd40176f3ab89dab0a8c4d9195604d383eebf8ea",
      "arrays.npz": "d3ad8e2e7a3a80d906136a80a18c09421d13ecfeddc4315aa0eebcdd9889276a",
      "snapshots.npz": "cf1c55972b7372fe5acce9c3537468e71083696320e4c14cfb40b26e1fa2bc19",
      "stdout.txt": "3ed8a39349057c55303ddaaa12774ec12a48612b82d2a3b6675d67c664e18cc2"
    },
    "raw_array_sha256": {
      "M": "605d79608f5079f4b1167c373b918116eb152c46894b0f51f544ef982652578f",
      "I": "0a11da77d397d57d4c187a1a8d38ee0c58da71c024ccbfd9691ac7a08bf7912a",
      "N": "60030ec9aa21379b70c37ae3097551d26924659e96dbe86dcc734992aa6cbfaf",
      "B": "2a250e943c0e80afcd78b6ef917ec3c639eda4ce6aed1c7069489ac2b2190c12",
      "E": "c6adf9a6e89c46d6eeb79de433a16b8a4cb78ebc5ea6f3abd1d5e50ebad547ba"
    }
  },
  "RUN-18": {
    "artifacts": {
      "B.png": "cb168f8dad48e26d127d85f5877770aa777d6bc0d45c7d5c6e73dcb6b93470b6",
      "E.png": "9ba8ac4cd070509353a52498ccd512c7c121990bf213120f7ad3801e1717e85b",
      "N.png": "beb330c78eb931c4a613a8f10a99a7d51c9accaa60233fd38f3ed9ba755f343f",
      "arrays.npz": "e0aa5de4976c45ae0b6dec4e5d5f75457a4cc659dd907e38e81950a32b306baa",
      "snapshots.npz": "d4af815c957ec769ec598a4496497a6101be5309e05725668553de1360865b48",
      "stdout.txt": "2de620130d97253cb817adf33e47d5eef937d87c06952749ebe101536d87d782"
    },
    "raw_array_sha256": {
      "M": "605d79608f5079f4b1167c373b918116eb152c46894b0f51f544ef982652578f",
      "I": "0a11da77d397d57d4c187a1a8d38ee0c58da71c024ccbfd9691ac7a08bf7912a",
      "N": "60030ec9aa21379b70c37ae3097551d26924659e96dbe86dcc734992aa6cbfaf",
      "B": "2a250e943c0e80afcd78b6ef917ec3c639eda4ce6aed1c7069489ac2b2190c12",
      "E": "6cfbb6dfd493615a34f1b514ddf4a9678cd1e3b20db1efe199dae6483ffdeae8"
    }
  },
  "RUN-19": {
    "artifacts": {
      "B.png": "9d365acbe144dff8491ffef89e3fdfa131417ec64b5560cacb3d749569d105d6",
      "E.png": "816c8ff6b9ba4064487c1141a9ef2cf0faebddbc7867662a071e4d6dbbec1f60",
      "N.png": "ef8965d180396a6cfd8497e605ca7a0310fcc978efc0a958883a925aa26e26a7",
      "arrays.npz": "4c50962828b29bafaefefedd4dbd4448b7da01820f7f0f109f4f574f3a4e85ad",
      "snapshots.npz": "8338a15afe97c2dcf70e38e3b7b6c0d04bde86990ef5784b1b38977992a9747c",
      "stdout.txt": "2e8dea79afec2ef8eadbbc6448efe931e5b6e4f259195e77c4cbfcd56833f163"
    },
    "raw_array_sha256": {
      "M": "605d79608f5079f4b1167c373b918116eb152c46894b0f51f544ef982652578f",
      "I": "0a11da77d397d57d4c187a1a8d38ee0c58da71c024ccbfd9691ac7a08bf7912a",
      "N": "60030ec9aa21379b70c37ae3097551d26924659e96dbe86dcc734992aa6cbfaf",
      "B": "2a250e943c0e80afcd78b6ef917ec3c639eda4ce6aed1c7069489ac2b2190c12",
      "E": "fa43239bcee7b97ca62f007cc68487560a39e19f74f3dde7486db3f98df8e471"
    }
  },
  "RUN-20": {
    "artifacts": {
      "B.png": "680008b6012a1a465e03c0884af5da43458a485604f3bb9b3520a3f07a643e7f",
      "E.png": "e00f9431a1eeef1758521460fd34e9e071dff33e5896bf69a3dd80d289bf0625",
      "N.png": "5e0813a59542f5c128cf9cdd94aa57612e44a5cb9047719d5b92a747e4cc8523",
      "arrays.npz": "d83ba272d1b9e0c08a81625a28ef555375acbf1980eac635427234aab3eb0abe",
      "snapshots.npz": "d1f5d53f3952d7061556bdc6668465468e9cc8c0923794d1bc75ca92646749a9",
      "stdout.txt": "77b7d5d5d140caa352c1597e25d91814fa2df083d138728f92d525f52d738b63"
    },
    "raw_array_sha256": {
      "M": "637f80fc1a00b72f6e99cfbc67b455c98028dc11243457c91318ba0edef8dfa0",
      "I": "867f553f36e29c7c4b0a8e0b69d541302944a2c7483c6b659d830c023ef081a4",
      "N": "e06637ce0280c18f9f4c4e4f74f50df5b692508859dbc307cb921225f6a77414",
      "B": "83a71fbcd9271d684ffefe943ce363daf39019ecc0ce6e217e72b467c0e3477f",
      "E": "df8f1fecd38427ec8afd579ab83bc9f1696b515e7e8b3068465669dd621095a8"
    }
  },
  "RUN-21": {
    "artifacts": {
      "B.png": "cad21aa3df8dc41f6da57f57b96eefdaa25e662c7be0a8e4f759e91a252a24f5",
      "E.png": "0a9417f03601e12a4959a09d431d10f4113f0d82248774a4e1a723cf2ba822b2",
      "N.png": "bce4bb72d812fc6c6e92eb2cb9aa1f4a40788577a94353cc35babbe8abd27a8d",
      "arrays.npz": "d13efe18c30fc047905c44e95b78f6fc251889b277fc554eb38dbbb2879344ca",
      "snapshots.npz": "3c030d71be349e405acd9a2603aab1772838465906b2d5c797b90e8baf94483e",
      "stdout.txt": "888bef7b05c9920e675beefb13a194c4b4357606c997654c070740baa35de76d"
    },
    "raw_array_sha256": {
      "M": "bda34cbd0bf3b126814d9bf92bef7aff4c0ba9508e076bb62d1aaa35a40eba9d",
      "I": "6809a852b727266751dd39f33792316d07861da41390d403ebec0b4262b54b0c",
      "N": "7d9c342e6a6d230c7b0f9230d899ab0ab6db1f09e6bc0623ef77dabf01c58cb1",
      "B": "6a44926ac1223ea878bfd5ff5db7326b8c2ecaf7b59366aa3fb21b2d19216d96",
      "E": "db0bfd7041a317524a67b43ed8a4d00a257757cc30d99c771e4dad7a038763e9"
    }
  },
  "RUN-22": {
    "artifacts": {
      "B.png": "0a05d4002ff925fa95f3cf03223e842bde4f3effd0a7ab74a9e34da2879b7fae",
      "E.png": "abb86000806c423587548b7bd38f7291a2db6634755f7b1c0c18855cda2e602d",
      "N.png": "bc71501d100a06e7cdb44b439ed8b4d5f219b28ec922be043aa47a24ba9e0104",
      "arrays.npz": "e95a074a120172db2f7ab775122e8b47918fea620edd563f4848df5018ca7a09",
      "intervention.npz": "0db7947bf29755af65090b7c8b040095921a41d19775004c412991453257348c",
      "snapshots.npz": "2cd4b89bd8a689709007072cdb5ec771429a0823ecd9e4ec97f9a18c389c50cc",
      "stdout.txt": "290865666d6150761c0dc6c41048d2d5a76e52b3525a707e40282f198111abfe"
    },
    "raw_array_sha256": {
      "M": "bda34cbd0bf3b126814d9bf92bef7aff4c0ba9508e076bb62d1aaa35a40eba9d",
      "I": "bb332812d49238dd73a2b8f3570487d5ddb4a133147812f1c2937dcd81a7a349",
      "N": "84aecfd3c46bf62f6fecea39bafa05bd28580884127d65ad1ab8a53fabdfb1a9",
      "B": "f5fc92a0b08d76bb6cc0af93ab8d64c7952d685a0ec40f56633810304281ce44",
      "E": "ab149b045b53bf6522443fd9c7ec5f1f97f5657f697f64a6f2bd5c0929047e32"
    }
  },
  "RUN-23": {
    "artifacts": {
      "B.png": "e1701f52818add58fd2b831050517f597096d36bebcda806787a970fd417cd4d",
      "E.png": "e2f8cf820e6e3f740716697415d1e546f73ce5d659658d65170f61810c61cdc2",
      "N.png": "b1e33add4f5c96f2b764e8631fc956c271940ea43cfbfe2fe45ef8965be4fee5",
      "arrays.npz": "609663aef546e62d589345f1e61655b7a2ac4c91f77807b4c9e95133368e7421",
      "intervention.npz": "c272b22770d6b66cbf0b72b28e873387a693ae7600bda8aa75a94729374bb69d",
      "snapshots.npz": "9773dbe13f757aac9c2dc1123719652a720ede621012aee0c223cae339655e67",
      "stdout.txt": "888bef7b05c9920e675beefb13a194c4b4357606c997654c070740baa35de76d"
    },
    "raw_array_sha256": {
      "M": "bda34cbd0bf3b126814d9bf92bef7aff4c0ba9508e076bb62d1aaa35a40eba9d",
      "I": "6809a852b727266751dd39f33792316d07861da41390d403ebec0b4262b54b0c",
      "N": "7d9c342e6a6d230c7b0f9230d899ab0ab6db1f09e6bc0623ef77dabf01c58cb1",
      "B": "6a44926ac1223ea878bfd5ff5db7326b8c2ecaf7b59366aa3fb21b2d19216d96",
      "E": "49b04bbb697cb02ee28620ffae1272f2d52debfbc8946d31836ff309c9a1c325"
    }
  },
  "RUN-24": {
    "artifacts": {
      "B.png": "6e68cf8e9fbe871a208bec2528ae55fa90b274fe950635ece7b9fad4a3928ec0",
      "E.png": "f5b9340c6a97943c96d51b1825f6caac7ddc34332ee00d61b4d5d2da75da1e1c",
      "N.png": "6d515c72f901b30063f43115f3bd0ef70c20855e3fe4342fe1005ea46a45fc72",
      "arrays.npz": "2497f5842f4d89649f1681c4f11fd6a86e438724730a329710743ae415858b16",
      "intervention.npz": "d52fd67e0c2a4acd54724f45c46cdbe7e01a6e35824b59de4d3b9f561bb16be6",
      "snapshots.npz": "9d08f78d4ea8fefbc81308f2a1186230c051961f59bf125fc9b7046cb13ec94e",
      "stdout.txt": "898692ee87f26871514e21a2949be0d4af14a25be8d9248a53f7992ff8613dc5"
    },
    "raw_array_sha256": {
      "M": "bda34cbd0bf3b126814d9bf92bef7aff4c0ba9508e076bb62d1aaa35a40eba9d",
      "I": "6809a852b727266751dd39f33792316d07861da41390d403ebec0b4262b54b0c",
      "N": "b683dd6072fa6b9c6cbf4e3dab957ae22fc0d472c7dfc1961d4b3dad583cc456",
      "B": "6a44926ac1223ea878bfd5ff5db7326b8c2ecaf7b59366aa3fb21b2d19216d96",
      "E": "e1c41f165989a7e0c6525c78d2f29d1b059998fbe388d1785cb9e3814b5a24f0"
    }
  }
}
```

Tracked/fresh PNG hash対（全画素一致とfile bytes不一致を独立に検査）：

| Output | Tracked SHA-256 | RUN-01 SHA-256 |
| --- | --- | --- |
| boundary_field_final_v2.png | `d02e01162eb107b90532f7308c5d009dc7834595bfa12c03864279d9f9e43838` | `9807ad24575bfd3fec586dab50f76a5cc361bc9ba8785dc63231614a4302181c` |
| combined_fields_with_eye_v2.png | `8b88544ad86c33aa0104e6a1a6752408f73452a01b196e9c9fb8aba6b1b16ef9` | `34cfbafb7508f5ccb47d829bc3649822256f4a43ad4708b37792c47fa6af4065` |
| eye_commitment_final_v2.png | `1d999077a1b8af76d2e1a269d58c8404934e10a5bfbfb2450030be02e59a4053` | `06ef0070f033097d39fb3a035729537e1d362082dc7027f75e556fa0dae05569` |
| information_density_final_v2.png | `b142a9144ad5d749282338016fb929ddc96df7bf4ef09dea61546a807d7abe08` | `d1b05599f9687987814e3120ee69895fbd1eb4f4595b6b47d2c7f6a68a94a270` |
| morphogen_final_v2.png | `fdd22963306db0195f05d499a6f7e0ff782edd1d6d5534660d9ae8e54386f26a` | `61ea95f85f12e631c86a2f0b716f89ead672d91d112ad011e620f0facffae330` |
| neural_commitment_final_v2.png | `692174849934cd7703164dcafa403d986b7651261d8bcfca8b0f0ff46b3b9480` | `0eb9e570e1486de00ab66c727a776c660c35a01687cb08c37867a88973467aaa` |
| neural_eye_overlay_v2.png | `41299f413758f5189a0677d5839ee2d8491929d54f1ce614116b7548474a6a5b` | `5b5132d1960e2bc9768817c4181399e78bdfd36c13a11a336aad498623ad92d6` |

## 24. Reproducibility classification

**R4 LOCAL PARAMETER ROBUSTNESS DEMONSTRATED — 限定されたcoarse pattern / tested neighborhoodのみ**。

| Level | Directly supported? | Scope |
|---|---|---|
| R0 NOT EXECUTABLE | 非該当 | 既存環境で実行成功 |
| R1 EXECUTABLE | YES | unchanged source |
| R2 DETERMINISTIC DEFAULT REPRODUCTION | YES | same environment / seed / parameters |
| R3 TRACKED OUTPUT REPRODUCED | YES, pixel-level | 7/7 pixels、file hashesは圧縮/metadata差 |
| R4 LOCAL PARAMETER ROBUSTNESS DEMONSTRATED | 限定YES | seeds3/7/11、selected ±10%でcentral N/boundary-sensitive B/local Eというcoarse patternを保持 |
| R5 INDEPENDENT MODEL / DATA REPLICATION | locateせず | 同じsourceのrerunは独立modelではない |
| R6 EMPIRICAL BIOLOGICAL VALIDATION | locateせず | biological measurement comparisonなし、総合validation verdictを行わない |

R4のqualifierを外して引用しない。厳密なconnectednessの保存、source/eye modeに対する不変性、
long-time stationary pattern、任意方向perturbation returnはこのR4に含まれない。
これらを含む強いrobustness基準については**R4達成とはしない**。数値結果とfailure/sensitivityを同時に読む。

## 25. Empirical correspondence classification

ここでのE0–E5はcurrent artifactの対応層の所在であり、Bio全体のvalidated/unvalidated verdictではない。
E2にはmodel labelの定義だけでなく生物側とのoperational relationを要する。

| Reading | Level located | Evidence / limit |
|---|---|---|
| morphogen | E1 QUALITATIVE ANALOGY | MのRD-like field、特定物質へのmeasurement mapなし |
| cell fate | E1 QUALITATIVE ANALOGY | threshold categoriesとcommitment名、assay mappingなし |
| morphology | E1 QUALITATIVE ANALOGY | structured model pattern、paired specimenなし |
| neural-like pattern | E1 QUALITATIVE ANALOGY | central band resemblance / sourceのtoy label |
| boundary-like B | E1 QUALITATIVE ANALOGY | gradient-sensitive accumulated pattern、膜measurementなし |
| eye-like E | E1 QUALITATIVE ANALOGY | gated lobes / window dependence、eye development dataなし |
| life attractor | E0 TERMINOLOGICAL ONLY | toyでOmega_life operational membershipは実装されない。manuscriptのconceptual interpretationは保持 |
| robustness | E1 QUALITATIVE ANALOGY | model-local dependence/relaxationと生物robustnessの対応は類比まで |
| regeneration | E1 QUALITATIVE ANALOGY | attractor reconstructionというsource解釈、今回のsmall interventionは独立biological対応でない |
| fast/slow differentiation | E0 TERMINOLOGICAL ONLY (attribution) | Bio-local dedicated diagnosticなし |

10対象：E0=2、E1=8、E2/E3/E4/E5=0。
empirical falsity、mechanism impossibleという判定はしない。

## 26. Discrepancy ledger

| Discrepancy ID | Source A | Source B | Difference | Semantic importance | Later action needed? |
|---|---|---|---|---|---|
| DS-01 | tracked PNG | RUN-01 | all pixels match / metadata+IDAT byte difference、原manifestなし | run lineageとvisual再現の区別 | provenance記録を引渡し、上書きしない |
| DS-02 | S15 unprefixed GIF path | repo ignored fig8 / fresh GIF | 指定artifact欠在、local別名GIFはframe pixel不一致 | 配布animationのversion未固定 | artifact correspondence handoff |
| DS-03 | S14 raw G | S21 normalized gradient | raw vs global normalization | B入力identity | Phase 06で対象固定 |
| DS-04 | S14 one S | S21 k8 / k20 | switching steepness variant | threshold execution | source/code role handoff |
| DS-05 | continuous paper rates | S21 update | DT適用範囲・sequential order・clip | time/update signature | mathematical修正は本phaseなし |
| DS-06 | S15 N→B path | code / theta_N tests | B direct inputはI→G_norm、N変更でB不変 | dependency arrow | Phase 06 handoff |
| DS-07 | gradient defines B wording | accumulated B | instantaneous derivativeとstateの差 | boundary interpretation | GAP-16へ |
| DS-08 | stable solutions / final state | RUN-20/21 | 3200まで変化、B mask全域化 | finite horizon vs stationarity | CLM-45 scope handoff |
| DS-09 | center does not produce E / paired | RUN-03 / PDF contour | center E>0.5、1 component、bright lobesはある | absence / topology / visual wording分離 | CLM-40 local reading |
| DS-10 | geometry not encoded reading | source/window / RUN-15–19 | location preferenceが入力されEに影響 | completed drawing不使用とlocation-freeの差 | CLM-41 handoff |
| DS-11 | DOWN-01 confirmed fast/slow | Bio code / stdout / GIF / PDF | dedicated diagnostic/resultなし | attribution source locator | CLM-50 / GAP-21 |
| DS-12 | DOWN-07 Bio showed inter-individual | Bio current construction | future referenceのみ、個体間modelなし | attribution source locator | CLM-53 / GAP-22 |

12件はrevision dispositionsではない。DS-01は数値pattern不一致ではなくbyte/provenance差である。
既存probability / threshold / sigma signature / JA working variantsはPhase 01のまま残し、今回source統合を行わない。

## 27. Evidence-update matrix

「Would this alter later disposition?」はここでは決定しない。結果を後続phaseへ渡すだけである。
Phase 04のburden列はそのまま転記し、YES/PARTIAL/NOを書き換えない。

| Claim | Phase-04 burden | New Phase-05 support located? | Would this alter later disposition? | Phase-06 handoff |
|---|---|---|---|---|
| CLM-01 | YES | source-local定義 / formal / conceptual scopeを維持、対応data追加なし | NO CHANGE | dispositionは未決定、scope付きでPhase 06へ |
| CLM-02 | YES | source-local定義 / formal / conceptual scopeを維持、対応data追加なし | NO CHANGE | dispositionは未決定、scope付きでPhase 06へ |
| CLM-03 | PARTIAL | Iのobservable mapなし、array再現と分離 | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-04 | YES | source-local定義 / formal / conceptual scopeを維持、対応data追加なし | NO CHANGE | dispositionは未決定、scope付きでPhase 06へ |
| CLM-05 | NO | Jのevent aggregation / flux calibrationなし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-06 | YES | source-local定義 / formal / conceptual scopeを維持、対応data追加なし | NO CHANGE | dispositionは未決定、scope付きでPhase 06へ |
| CLM-07 | PARTIAL | toyはPhi/Jを直接積分しない | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-08 | YES | source-local定義 / formal / conceptual scopeを維持、対応data追加なし | NO CHANGE | dispositionは未決定、scope付きでPhase 06へ |
| CLM-09 | NO | sigma_Mはprescribed、gene measurementなし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-10 | YES | source-local定義 / formal / conceptual scopeを維持、対応data追加なし | NO CHANGE | dispositionは未決定、scope付きでPhase 06へ |
| CLM-11 | NOT APPLICABLE | biological duration calibrationなし、future target維持 | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-12 | YES | source-local定義 / formal / conceptual scopeを維持、対応data追加なし | NO CHANGE | dispositionは未決定、scope付きでPhase 06へ |
| CLM-13 | NO | DNA sequence→parameter実装なし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-14 | PARTIAL | parameter provenance / historical stabilization mapなし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-15 | YES | source-local定義 / formal / conceptual scopeを維持、対応data追加なし | NO CHANGE | dispositionは未決定、scope付きでPhase 06へ |
| CLM-16 | YES | source-local定義 / formal / conceptual scopeを維持、対応data追加なし | NO CHANGE | dispositionは未決定、scope付きでPhase 06へ |
| CLM-17 | NO | paired morphology observationなし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-18 | PARTIAL | toy spatial witnessはあるがbiological convergence/mechanism mapなし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-19 | YES | source-local定義 / formal / conceptual scopeを維持、対応data追加なし | NO CHANGE | dispositionは未決定、scope付きでPhase 06へ |
| CLM-20 | NO | small perturbation試験を追加、生物returnへは未対応 | MODEL-LOCAL SUPPORT ADDED | dispositionは未決定、scope付きでPhase 06へ |
| CLM-21 | PARTIAL | I relaxation / N recommitment / N増加残存を分離。large regeneration未試験 | MODEL-LOCAL SUPPORT ADDED | dispositionは未決定、scope付きでPhase 06へ |
| CLM-22 | YES | source-local定義 / formal / conceptual scopeを維持、対応data追加なし | NO CHANGE | dispositionは未決定、scope付きでPhase 06へ |
| CLM-23 | NO | life independent operational criterionなし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-24 | PARTIAL | Omega_life領域constructionをtoyに追加しない | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-25 | PARTIAL | matter/energy exchangeの生物maintenance mapなし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-26 | YES | source-local定義 / formal / conceptual scopeを維持、対応data追加なし | NO CHANGE | dispositionは未決定、scope付きでPhase 06へ |
| CLM-27 | PARTIAL | probability measure / sampling modelなし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-28 | YES | source-local定義 / formal / conceptual scopeを維持、対応data追加なし | NO CHANGE | dispositionは未決定、scope付きでPhase 06へ |
| CLM-29 | PARTIAL | history/reference/sharingのtoy実装なし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-30 | YES | source-local定義 / formal / conceptual scopeを維持、対応data追加なし | NO CHANGE | dispositionは未決定、scope付きでPhase 06へ |
| CLM-31 | UNRESOLVED | JA working probability variantは無修正 | SOURCE/ARTIFACT CONFLICT FOUND | dispositionは未決定、scope付きでPhase 06へ |
| CLM-32 | YES | default+7pixel再現、限定parameter pattern保持 | SUPPORT STRENGTHENED WITHIN SAME CLAIM LEVEL | dispositionは未決定、scope付きでPhase 06へ |
| CLM-33 | YES | M finite execution / profile再現 | SUPPORT STRENGTHENED WITHIN SAME CLAIM LEVEL | dispositionは未決定、scope付きでPhase 06へ |
| CLM-34 | YES | new Mを使うI response再現 | SUPPORT STRENGTHENED WITHIN SAME CLAIM LEVEL | dispositionは未決定、scope付きでPhase 06へ |
| CLM-35 | YES | N finite pattern再現、source/threshold dependence確認 | SUPPORT STRENGTHENED WITHIN SAME CLAIM LEVEL | dispositionは未決定、scope付きでPhase 06へ |
| CLM-36 | YES | normalized gradient現物確認、raw式と分離 | SUPPORT STRENGTHENED WITHIN SAME CLAIM LEVEL | dispositionは未決定、scope付きでPhase 06へ |
| CLM-37 | YES | B update実行、gradient/threshold dependence確認 | SUPPORT STRENGTHENED WITHIN SAME CLAIM LEVEL | dispositionは未決定、scope付きでPhase 06へ |
| CLM-38 | PARTIAL | gradient-sensitive Bと膜/biological boundary mapを分離 | MODEL-LOCAL SUPPORT ADDED | dispositionは未決定、scope付きでPhase 06へ |
| CLM-39 | YES | existing window/mode/no-eyeのE応答確認 | SUPPORT STRENGTHENED WITHIN SAME CLAIM LEVEL | dispositionは未決定、scope付きでPhase 06へ |
| CLM-40 | YES | 左右bright lobesを再現、独立2components / zero中心とは区別 | SUPPORT STRENGTHENED WITHIN SAME CLAIM LEVEL | dispositionは未決定、scope付きでPhase 06へ |
| CLM-41 | PARTIAL | window/location入力の依存を実測、drawing非入力と分離 | MODEL-LOCAL SUPPORT ADDED | dispositionは未決定、scope付きでPhase 06へ |
| CLM-42 | UNRESOLVED | actual I→G_norm→B、compact N→Bと分離 | SOURCE/ARTIFACT CONFLICT FOUND | dispositionは未決定、scope付きでPhase 06へ |
| CLM-43 | PARTIAL | toyとPhi/J/quasi-closureのtyped mapなし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-44 | YES | stdout/pixel/raw determinismとdiagnostics再現 | SUPPORT STRENGTHENED WITHIN SAME CLAIM LEVEL | dispositionは未決定、scope付きでPhase 06へ |
| CLM-45 | PARTIAL | long-run変化・saturation・限定returnデータ追加、stationary readingは未成立 | MODEL-LOCAL SUPPORT ADDED | dispositionは未決定、scope付きでPhase 06へ |
| CLM-46 | PARTIAL | molecular/cell/tissue typed scale mapなし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-47 | PARTIAL | cross-layer mapなし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-48 | UNRESOLVED | L1 counterpartのexact locator未固定 | SOURCE/ARTIFACT CONFLICT FOUND | dispositionは未決定、scope付きでPhase 06へ |
| CLM-49 | NOT APPLICABLE | empirical future-work scope維持、model-data comparisonなし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-50 | NO | NO BIO-LOCAL FAST/SLOW CONFIRMATION RESULT LOCATED | SOURCE/ARTIFACT CONFLICT FOUND | dispositionは未決定、scope付きでPhase 06へ |
| CLM-51 | NO | downstream necessity / same-role translationの追加supportなし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-52 | PARTIAL | second-attractor内部translationの追加supportなし | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-53 | NO | NO BIO-LOCAL INTER-INDIVIDUAL RESULT LOCATED | SOURCE/ARTIFACT CONFLICT FOUND | dispositionは未決定、scope付きでPhase 06へ |
| CLM-54 | YES | source-local定義 / formal / conceptual scopeを維持、対応data追加なし | NO CHANGE | dispositionは未決定、scope付きでPhase 06へ |
| CLM-55 | PARTIAL | 背景記述をpaired datasetに変換しない | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |
| CLM-56 | PARTIAL | generic biological observationをmodel-data比較としない | NO CHANGE — stronger burden remains | dispositionは未決定、scope付きでPhase 06へ |

「SUPPORT STRENGTHENED」は9families（CLM-32/33/34/35/36/37/39/40/44）。
同じfinite/formal claim level内の実物照合であって、source claimの強度変更ではない。
CLM-20/21/38/41/45にはmodel-local dataを追加したが、各stronger biological / stability readingのburden充足へ自動計上しない。
phase04のfinite実績5families（CLM-32/35/40/44/45）は全て今回traceし、45には支持だけでなく変化継続の結果も残す。

### GAP coverage

| Gap ID | Claim references | Phase-05 finding / location | Remaining handoff |
|---|---|---|---|
| GAP-01 | CLM-03 | §17 I mapなし | biological observable criterion |
| GAP-02 | CLM-05 | §17 J direct integration / event mapなし | flux aggregation |
| GAP-03 | CLM-07 | §17 Phi functional / restoring biology未実装 | response map |
| GAP-04 | CLM-13/14 | §17 theta(s)未実装、default定数は§23 | genotype/parameter provenance |
| GAP-05 | CLM-09 | §4/8 prescribed sigma_M | biological production map |
| GAP-06 | CLM-11/49 | §17/18 external time calibrationなし | future targetのまま |
| GAP-07 | CLM-17/18/55/56 | §17–19 paired morphology measurementなし | weaker model construction維持 |
| GAP-08 | CLM-20/45 | §9/13/14 longer / parameter / perturbation結果 | finite responseとbiological stabilityを分離 |
| GAP-09 | CLM-21 | §14/15 small interventionのみ | large regenerationとは別 |
| GAP-10 | CLM-23 | §17/25 life criterionなし | region definition≠life measurement |
| GAP-11 | CLM-24/25 | §17 toyにlife region/exchange maintenance実装なし | biological system-specific relation |
| GAP-12 | CLM-27 | §22 probability model追加なし | measure / sampling |
| GAP-13 | CLM-29 | §20–22 downstream referenceのみ | history/sharingの実装とtranslation |
| GAP-14 | CLM-31 | Phase 01 variant維持、source hash不変 | working square / conditional probability form |
| GAP-15 | CLM-42 | §8 B dependencyとtheta_N対照 | compact sequenceの意味 |
| GAP-16 | CLM-38 | §11/17 B sensitivity / long mask変化 | biological boundary map |
| GAP-17 | CLM-41 | §10 existing window / source依存実測 | location-free読みと区別 |
| GAP-18 | CLM-32/35/40/44/45 | §4–7/23 default・pixel・manifest | historical run特定とは別 |
| GAP-19 | CLM-43/46/47 | §22 cross-scale typed mapなし | analogyをidentityとしない |
| GAP-20 | CLM-48 | §22 L1 exact locator未固定 | paired source/version |
| GAP-21 | CLM-50/51/52 | §20専用fast/slow結果なし | downstream attribution |
| GAP-22 | CLM-53 | §21 Bio-local inter-individual結果なし | downstream attribution |

### Prior preload / uncertainty coverage

| Prior ID | Current trace | Scope |
|---|---|---|
| U10 | §17/18/25 | model output≠biological observable |
| U11 | §5–8/23/26 | paper/code/version、pixel再現と原manifest |
| U13 | §20 | dedicated fast/slow未locate |
| U16 | §6 | current GIF生成可、ignored fig8は不一致 / lineage未固定 |
| EM-01 | §7/9, CLM-32/18 | constrained spatial witnessとbiological morphogenesis分離 |
| EM-02 | §11, CLM-37/38 | gradient-sensitive Bの実行、膜同定なし |
| EM-03 | §12, CLM-35 | source/threshold dependence |
| EM-04 | §10, CLM-39/41 | location preloadを実測 |
| EM-05 | §7/10, CLM-40/41 | bright lobes / connected mask分離 |
| EM-06 | §17/25, CLM-23/24 | toyにlife-region membershipなし |
| EM-07 | §14/15, CLM-21 | relaxation / recommitment、large regenerationではない |
| EM-08 | §20–22, CLM-29 | second-attractor実装なし、forward reference保持 |
| EM-09 | §17/25, CLM-17 | model labelsとempirical fate map分離 |

### Decomposed chain coverage

| Prior edge | Execution / evidence checked | Inference limit |
|---|---|---|
| EDGE-01 | source/diffusion/decay→M, RUN-03/07–10/15 | prescribed-source finite response |
| EDGE-02 | new M→I, default raw arrays | biological information identityでない |
| EDGE-03 | I→N, RUN-11/12 | thresholded commitment |
| EDGE-04 | I→G, source function | raw derivative構成 |
| EDGE-05 | G→G_norm, current normalized output | global numerical operation |
| EDGE-06 | G_norm→B, RUN-13/14 | boundary-sensitive accumulation |
| EDGE-07 | compact N→B, theta_N変更でB不変 | direct inputなし |
| EDGE-08 | N/B/window→E, RUN-16–19 | imposed cue下のresponse |
| EDGE-09 | mode/coordinates→window | location preference |
| EDGE-10 | fields→hierarchy, GIF/snapshots | stage order≠one causal chain |
| EDGE-11 | hierarchy→quasi-closure/sub-attractor | typed map / attractor criterionを補わない |

## 28. Phase-05 outcome

| Required count / classification | Result / counting rule |
|---|---|
| Simulation runs | 24: RUN-01–24 |
| Default runs | 4: original CLI2 + API raw control2 |
| Deterministic comparisons | 2 pairs: CLI pair / raw pair、さらにAPI/CLI5PNG一致 |
| Tracked outputs exact bytes | 0/7 |
| Tracked outputs pixel-equivalent | 7/7、うちbyte同一を除いても7 |
| Tracked output pattern mismatches | 0/7。file-hash differencesは7/7 |
| Parameter perturbation runs | 8: selected scalar ±10%, RUN-07–14 |
| Seed variation runs | 2追加: RUN-05/06、defaultを含むunique seeds3 |
| Mode / no-eye runs | 5: RUN-15–19（source1、alternative eye3、disabled1） |
| Long-time controls | 2: RUN-20/21、1600 / 3200 steps |
| Post-formation perturbation runs | 3: RUN-22–24、各3200まで |
| Recovery cases | 2: I relaxation1、N recommitment1、target-field90% criterionのみ |
| No-recovery cases | 1: N positive offset、3200まで |
| General / biological regeneration established | 0：その同定・総合verdictを行っていない |
| Eye-window dependence | STRONGLY WINDOW-DEPENDENT (model-local) |
| Boundary sensitivity | gradient/threshold/source依存、theta_B+10%でmask topology変化、long mask全域化 |
| Neural sensitivity | seeds/小thresholdでcoarse中央pattern保持、source modeで左へ、long widening |
| Empirical biological datasets located / used | 0 / 0 |
| Operational biological maps located | 0 |
| Dedicated Bio fast/slow confirmation diagnostics | 0 |
| Bio-local inter-individual results | 0 |
| Cross-scale typed maps located | 0 |
| Discrepancies | 12: DS-01–12 |
| Phase-04 support strengthened within same level | 9: CLM-32/33/34/35/36/37/39/40/44 |
| Additional model-local characterization, not stronger-claim fulfillment | 5: CLM-20/21/38/41/45 |
| Reproducibility classification | R4限定coarse-pattern neighborhood、topology/long-time/biologyの保証なし |
| Empirical correspondence classification | 10 readings: E0=2、E1=8、E2–E5=0 |
| Mandatory handoff coverage | GAP22/22、U4/4、EM9/9、EDGE11/11、Phase-04 CLM56/56 |

default再現、pixel一致、parameter sensitivity、long-time変化、摂動応答は全て有限model-local観察である。
生物学的false/invalid verdict、Bio全体のempirical validation verdict、claim変更、equation変更、
revision disposition、new model / bridge / notation / theory、upstream reopeningを行っていない。
Phase 04のburden table・Phase 03のpreload/circularity classificationも変更していない。

### Validation / write boundary

検証結果を以下に記録する。全simulation output / snapshots / images / GIF / PDF renders / caches / temporary scriptsはtemp root内。
tracked figure / main PDF / source / requirements / codeは無変更。
このtaskでrepositoryへ作るのは本recordだけ、既存編集は本枝READMEのstatus/linkだけ。
開始時1432filesのhash baselineと最終照合し、既存user working-tree changesを維持する。

- Local links / source paths: PASS。新record26 + README9 = 35 relative targetsが存在する。
- Markdown fences / display math / tables: PASS。未閉鎖fence・不均衡display delimiterなし、新record25表 / README1表のcolumn数が一致する。埋込JSON 2 blocksもparse成功。
- ID / coverage: PASS。RUN manifest24/24、run metric table24/24、DS12/12、CLM56/56、GAP22/22、EM9/9、EDGE11/11。U10/U11/U13/U16を別表でtrace。各ledgerのID一意、参照範囲内。
- Phase-04 burden preservation: PASS。56/56を元claim tableと再照合し一致。support-strengthened9、model-local-characterization5の件数も表から再集計。
- Output provenance: PASS。24 manifestsのsource hashがcurrent sourceと一致、179 generated-artifact file hashesを再計算してmanifest / 本recordと一致。raw default5 arrays / CLI15 image artifacts / tracked7 pixel comparisonsは§5–6。
- PDF visual / image correspondence: PASS（図のspot-check範囲）。EN7 / JA7 embedded imagesのRGB一致、EN pp.19–25 / JA pp.17–20のrendersを視認。Poppler不在は既存CoreGraphicsで代替、PDF再buildなし。
- Simulation validation: PASS。24 runs完走。初回analysisのtracked-file列挙がignored alternate PNGを含んだため、git ls-filesの7画像へ限定してanalysisを再実行した。これはrunの追加・parameter変更ではない。biological validation verdictではない。
- Write scope: PASS。開始時1432既存filesのSHA-256比較で変更は本枝READMEのみ、削除0、新規は本recordのみ。source / equations / tracked images / PDFs / prior audit recordsはbyte不変。既存user変更は保持。
- git diff --check: PASS。新recordはuntrackedなので上記Markdown / whitespace検証も別途実施した。
- Temporary outputs: ${TEMP_EVIDENCE_ROOT}/bio_ifgt_phase05.Oq64Sn に限定。repository内に新しいsimulation出力・build/cache junkなし。tempは今回削除していない。
- No simulation redesign / source repair / web research / commit / push。Phase 06は未着手。

Phase 05はここで完了。Phase 06 revision candidatesへ着手せず停止する。
