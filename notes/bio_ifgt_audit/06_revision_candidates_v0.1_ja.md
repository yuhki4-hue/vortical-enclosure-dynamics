# Bio-IFGT Phase 06 — revision candidates

## 0. Status

- Bio-IFGT audit: **IN PROGRESS**
- Phase 00–05: **COMPLETE**（既存classification / burden / findingsを変更しない）
- Phase 06 revision candidates: **COMPLETE**
- Phase 07 final audit record: **NOT STARTED**
- Upstream VED equation audit / core revision: **CLOSED / CLOSED**
- 本稿の78件はすべて**candidate action**。final disposition、実装承認、closure verdictではない。
- source / equation / simulation / downstream / tracked figure / PDFの変更なし。新run・data・bridge・notation・theoryなし。

Authorityは[README](README_ja.md)、
[Phase 00 dependency](00_dependency_and_inheritance_record_v0.1_ja.md)、
[Phase 01 identity](01_equation_and_symbol_inventory_v0.1_ja.md)、
[Phase 02 role](02_equation_role_and_biological_role_audit_v0.1_ja.md)、
[Phase 03 preload](03_preload_boundary_and_circularity_audit_v0.1_ja.md)、
[Phase 04 claim/evidence](04_claim_and_evidence_burden_audit_v0.1_ja.md)、
[Phase 05 execution](05_simulation_and_empirical_correspondence_audit_v0.1_ja.md)。
上流[frozen VED dispositions](../ved_equation_audit/06_final_audit_record_v1.0_ja.md)は変更対象でない。

## 1. Candidate vocabulary / guards

| Candidate action | 本phaseでの意味 |
|---|---|
| KEEP | formal / model-local contentを明記したscope内で保持する候補 |
| REVISE | 数学を変えずrole / domain / wording / source・artifact関係を明示する候補 |
| DOWNGRADE | current evidence ceilingを越える強い読みを限定する候補 |
| SPLIT | 同字・同文・同arrowの複数object / role / claimを分離する候補 |
| RETIRE | defensibleな弱いscopeも見つからないformulationを退役させる候補 |
| OPEN | 特定の未解決identity / map / mechanism / stability / provenanceを研究課題として残す候補 |

Guardsは以下。未確立をFALSEへ反転させない。

- stronger claim unsupported ≠ weaker formal result should be removed
- source conflict ≠ equation is wrong
- simulation sensitivity ≠ model invalid
- no empirical map ≠ formal construction false
- preload ≠ cheating / circularity
- model-local reproduction ≠ biological validation

R4をR6、E1をE2以上に変えない。Phase 05の監査runを主理論の新proof・生物学的証拠として採用する候補ではない。
Phase 03でsource-level vicious circularityは確立されていない。この結果を「すべて非循環」の証明にも変えない。

## 2. Candidate construction rules

一つのBIO-RCに一つのcandidate actionを付ける。同一対象のformal retention、claim ceiling、missing mapは別aspectとして別行にする。
したがって同じCLMにKEEPとDOWNGRADEが付いても、同一claim aspectへ矛盾した二判定を付けるわけではない。
§17のCurrent issueがWhy、Preserveが保全対象、Proposed change scopeが将来の限定変更範囲である。

P1はsemantic / factual mismatch、P2はclaim-strength / identity alignment、P3はdocumentary / provenance cleanup。
priorityは実装順の目安でありvalidity gradeでない。source locationはPhase 04のCLM locatorを継承し、§17に逆引きを置く。
S番号はPhase 00、BIO-EQ/CF/COLはPhase 01、CON/VRはPhase 02、CIR/BND/EMはPhase 03、CLM/GAPはPhase 04、DS/RUNはPhase 05のID。
BIO-RCだけが今回の新しい**監査管理ID**であり、理論notationではない。

### Current-facing source locator

| Scope / S ID | Source |
|---|---|
| EN / JA build, S01/S02 | [main.tex](../../bio-ifgt/main.tex)、[self-contained main_ja.tex](../../bio-ifgt/main_ja.tex) |
| Fields, S04/S06/S07 | [introduction](../../bio-ifgt/sections/introduction.tex)、[formal mapping](../../bio-ifgt/sections/formal_mapping.tex)、[core equations](../../bio-ifgt/sections/core_equations.tex) |
| Intuitive description, S05 | [intuitive picture](../../bio-ifgt/sections/intuitive_picture.tex) |
| DNA / morphology, S08/S09 | [gene information flow](../../bio-ifgt/sections/gene_information_flow.tex)、[development](../../bio-ifgt/sections/development_morphogenesis.tex) |
| Life / probability / second attractor, S10–12 | [life attractor](../../bio-ifgt/sections/life_attractor.tex)、[probability](../../bio-ifgt/sections/probability_revision.tex)、[intelligence forward](../../bio-ifgt/sections/intelligence_second_attractor.tex) |
| L3/L1, S13 | [relation to note](../../bio-ifgt/sections/relation_to_note.tex) |
| Toy / results, S14/S15 | [toy manuscript](../../bio-ifgt/sections/minimal_developmental_simulation.tex)、[results and captions](../../bio-ifgt/sections/simulation_results_visualization.tex) |
| Scope / future, S03/S16/S17 | [abstract](../../bio-ifgt/sections/abstract.tex)、[discussion](../../bio-ifgt/sections/discussion.tex)、[conclusion](../../bio-ifgt/sections/conclusion.tex) |
| Source versions, S18–20 | [Bio README](../../bio-ifgt/README.md)、[working JA](../../bio-ifgt/sections_ja/)、[handoff](../../bio-ifgt/notes/handoff.md) |
| Execution / provenance, S21–24 | [simulate.py](../../bio-ifgt/simulations/minimal_neural_field/simulate.py)、[simulation README](../../bio-ifgt/simulations/minimal_neural_field/README.md)、[requirements](../../bio-ifgt/simulations/minimal_neural_field/requirements.txt)、[outputs](../../bio-ifgt/simulations/minimal_neural_field/outputs/) |
| Distribution / background, S25/S26 | [EN PDF](../../bio-ifgt/main.pdf)、[JA PDF](../../bio-ifgt/main_ja.pdf)、[refs.bib](../../bio-ifgt/refs.bib) |
| DOWN-01, S31 | [SSO EN](../../consciousness/sections/sso.tex)、[SSO JA](../../consciousness/sections_ja/sso_ja.tex) |
| DOWN-04, S34 | [Intelligence I introduction](../../intelligence-part1/sections/01_introduction.tex) |
| DOWN-05/06/07, S35 | [II inference](../../intelligence-part2/sections/02_inference_operator_ja.tex)、[II stopping](../../intelligence-part2/sections/05_emergent_stopping_layer_ja.tex)、[II social](../../intelligence-part2/sections/09_social_blockchain_ja.tex) |

EN/JA manuscript、working MD、codeは自動統合しない。build authorityは掲載版の識別を解くが、working variantの作者意図まで解かない。
S25はPhase 01 spot-check / Phase 05 embedded figure照合の範囲を継承し、今回PDFの新closure監査をしたとはしない。

## 3. Source / notation candidates

Group A: BIO-RC-001–012。I/J/rho/sigma/t/tau/Phi/Fはsource-local identitiesを分離する。
GとG_normとBは別object、paper Sとcode二sigmoidsはsource variantsとして扱う。
plain Jがcodeで積分されない事実は、paper equationの否定ではない。

theta/sigmaのsignature省略はREVISE候補であり、式の引数を今補完する提案ではない。
conditional probabilityとworking square formはCF-01の意図をOPEN候補へ残す。
JA workingのsecond-attractor「上位」説明とsubset、regenerationの強さ等のVR-07–10も、
source-version索引とforward/return scopeの候補へ分配する。working sourceを黙ってcanonical化しない。

## 4. Core equation candidates

Group B: BIO-RC-013–017。I/J state、Phi[I]、negative gradient、J constitutive relation、
balance、optional tau accumulation、reaction–diffusion、state-space evolutionのformal contentは保持候補。
必要なのはR3/local fields、operator、chosen functional、external t、observation windowのscopeであり数式改変ではない。

Phiの符号例からbiological restoring mechanismを導出しない。rhoやPhiの具体functional・独立calibrationは未指定部分を残す。
clock mapはBIO-RC-016、biological responseへの独立対応はBIO-RC-023/064/069と連携させ、
新functional、new clock mechanism、fundamental physical forceを導入しない。

## 5. Biological identification candidates

Group C: BIO-RC-018–023。definitionを保持したまま、Iのproxy/observable、Jのgene aggregation、
sigmaのgene production、Phiのbiological responseを分ける。
OPEN候補はmeasurement mapや独立source functionという具体的burdenを指し、漠然とした不確実性ではない。

Iがlocal constraint/morphogen proxyとして記述可能なことと、その測定同定が達成済みであることは別。
biological identificationを限定する候補は、sourceが既にinterpretiveと明示する箇所まで機械的に弱めることを求めない。

## 6. DNA / theta candidates

Group D: BIO-RC-024–026。sequence alphabet、抽象theta(s)、Delta I、threshold ruleは保持候補。
具体genotype→parameter map、organism-specific threshold prediction、historical stabilizationは別のclaim/mapとして扱う。
code定数の存在からDNA写像を補わず、parameter tuning履歴が記録されていないことから結果合わせを推定しない。
CF-02/03/11、CON-06、CIR-09とtraceする。

## 7. Morphogenesis candidates

Group E: BIO-RC-027–029。四つのaspectを混ぜない。

| Aspect | Candidate handoff |
|---|---|
| threshold rule / finite structured spatial pattern | BIO-RC-027 KEEP |
| observed morphology = stable configuration | BIO-RC-028 DOWNGRADE、019/064 OPEN map |
| proposed field dynamicsがmorphogenesisを説明 | BIO-RC-028 DOWNGRADEのbiological mechanism aspect |
| intuitive sequence / generic same-DNA biological background | BIO-RC-029 REVISE、066背景の所在 |

finite witnessを消さず、empirical morphologyやdevelopmental convergenceへ無媒介に継承しない。

## 8. Life-attractor candidates

Group F: BIO-RC-030–042。life attractor全体に一つのactionを付けない。

| Aspect | Candidate |
|---|---|
| Omega_life subset / bounded viable returning regionという定義 | BIO-RC-030 KEEP |
| model region / biological lifeのrole分離 | BIO-RC-031 SPLIT |
| life identification | BIO-RC-032 DOWNGRADE、033 OPEN criterion |
| not externally imposed / region形成 | BIO-RC-034 DOWNGRADE、036 OPEN construction |
| continued exchange/updateによるmaintenance | BIO-RC-035 DOWNGRADE、036 OPEN map |
| return / robustness / regeneration | BIO-RC-044/045/046へ別handoff |
| life probability target reformulation | BIO-RC-037 KEEP |
| dimensional reductionの説明 / quantitative probability | BIO-RC-038 REVISE、039 OPEN measure |
| second-attractor subset / conditional factorization | BIO-RC-040 KEEP |
| history/reuse/sharing / cognitive identification | BIO-RC-041 REVISE、042 OPEN translation |

boundedness、viable range、return、exchange、progressionをmodel conditionとして列記することは、
independent biological life criterionを供給したことではない。
not externally imposedをtoy computational boundaryまで内生化した意味にしない。
probabilityのevent再記述は数値推定ではなく、conditional factorizationをworking squareへ同一化しない。

## 9. Attractor / stability candidates

Group G: BIO-RC-043–046。Phase 05 §13–16の有限結果をそのまま保持する。

- 800-step defaultは再現するが1600/3200でも変化。3200でB >0.5 maskは全grid、B_min=0.539937。
- RUN-22のI差は同時刻controlに対し98.56%減少。whole-state完全returnではない。
- RUN-23はN減少後のmonotonic recommitment。RUN-24のN正offsetは3200までほぼ残る。
- N/B/Eには内生的decrease項がなく、saturation、persistence、bidirectional repairを分離する。

「stable solutions」のstationary readingはP1 DOWNGRADE候補。
「attractor-like」は限定された類比としてREVISE候補であり、attractorという語を一律RETIREしない。
generic life-regionの定義をtoyが実装しているとはしない。未試験の時間・介入・biologyについて不可能性を主張しない。
監査用90% target-field RMS基準を新しい生命・再生基準として採用しない。

## 10. Toy-chain candidates

Group H: BIO-RC-047–051。以下はPhase 02/05の既存EDGE inventoryを参照したdependency tableであり、
新chainやarrow calculusの提案ではない。compact display自体も今回は変更しない。

| Existing edge | Execution / role fact | Candidate |
|---|---|---|
| EDGE-01 source / diffusion / decay to M | prescribed-source PDE / finite update | BIO-RC-047/048 |
| EDGE-02 M to I | new Mを使うI step | BIO-RC-047/048 |
| EDGE-03 I to N | threshold accumulation | BIO-RC-047/059 |
| EDGE-04 I to G | raw gradient construction | BIO-RC-007/047 |
| EDGE-05 G to G_norm | global normalization | BIO-RC-007/047 |
| EDGE-06 G_norm to B | accumulating state update | BIO-RC-047/052 |
| EDGE-07 compact N to B | actual direct inputなし | BIO-RC-049 |
| EDGE-08 N/B/window to E | new N/Bとpositional gate | BIO-RC-047/048/056 |
| EDGE-09 mode / coordinates to window | imposed location preference | BIO-RC-056/057 |
| EDGE-10 fields to developmental hierarchy | navigation / interpretation | BIO-RC-049/050 |
| EDGE-11 hierarchy to quasi-closure / sub-attractor | proposed analogy、typed mapなし | BIO-RC-051 |

paper raw G/code G_norm、one/two sigmoids、DT適用範囲、sequential order、clip、modeを記述上分ける。
raw Gへの置換、DT統一、simultaneous update、gate除去等のmodel redesignは候補に含めない。

## 11. Boundary candidates

Group I: BIO-RC-052/053、identityは007。Bはgradient-sensitive inputから蓄積するstateでありinstantaneous gradientでない。
threshold_B/sourceに依存し、長時間では>0.5 maskが全域化する。
「boundary stabilization」はfinite-horizonのmodel labelへscopeを明示する候補。

biological membrane / organism boundaryの同定はsourceに具体claimとしてlocateされていない。
存在しない膜生成claimを新設してDOWNGRADEするのではなく、mapをOPEN候補に残す。
observation boundary、state-space region、computational edge、source support、display thresholdも同じboundaryへ統合しない。

## 12. Eye / neural candidates

Group J: BIO-RC-054–058、Group K: BIO-RC-059。
default Eには二つのbright lobesがある一方、E[63,63]=0.689486、E[64,64]=0.704404、
4-neighbor / >0.5 maskは一つのconnected componentである。
central exclusionのliteral readingはREVISE候補であり、visual lobesの保持と両立する。
二器官が形成されたとも、eye-like contrastが存在しないとも結論しない。

window変更はEを変え、no-eyeではE=0。完成final arrayはpreloadされないが、coarse位置情報はpreloadされる。
geometry-not-encodedの強い読みを限定する候補は、この二つの区別に限る。
Nはseed3/7/11、小threshold変化でcoarse patternを保つが、source変更で移動し長時間で広がる。
neural-like / eye-like labelsは測定済み組織identityにしない。

## 13. Simulation / provenance candidates

Group L: BIO-RC-060–063。24 runsはPhase 05の既存実績であり、今回新runは0。

| Established audit fact | Candidate limit |
|---|---|
| default CLI / raw control deterministic | same environment/configのscopeを保持 |
| tracked PNG 7/7 pixel-equivalent、0/7 byte-exact | metadata + IDAT差、original run manifestとの区別 |
| selected small parameter neighborhoodでcoarse pattern保持 | R4限定、topology・mode・long-time invarianceは含めない |
| current generatorがGIFを生成できる | historical ignored GIFとのlineage同定とは別 |
| EN/JA embedded imagesはtracked RGBと一致 | 図version照合であり全文closureでない |

RUN-14ではB/E mask component数も変わる。R4を強いrobustnessへ単純転記しない。
tracked PNGの削除・上書きは提案しない。GIFの元configを未解決として残し、caption/PDF同期は将来の承認済みsource変更後だけ。

## 14. Empirical-correspondence candidates

Group M: BIO-RC-064–066。Phase 05の10対象はE0=2、E1=8、E2–E5=0。
dataset、operational map、paired measurementが所在しないことを、生物学的falseへ変換しない。
N/B/Eの0–1、fraction >0.5、RGB normalizationはcalibrationではない。
S15のnot biological mechanism / structural possibility、S16/17のempirical future workは保持候補。
refs.bibの8entryはcurrent build未引用であり、背景文献の所在をmodel-data evidenceへ変換しない。

## 15. IFGT / cross-scale candidates

Group O: BIO-RC-067–071。明示的なnonidentity correspondenceはKEEP候補、
scale-universalな強い読みはDOWNGRADE候補、typed mapsとL1 source locatorはOPEN候補。
L3/L1のsame phenomenonという文は比喩的比較とexact translationを分けるREVISE候補。

| Upstream OPEN | Bio inheritance guard / candidate trace |
|---|---|
| RC-005 C_ij to C(x,tau) | Bio-local I再定義から閉じない。BIO-RC-001/067/069 |
| RC-006 J_ij to continuum J | Bio vector定義は上流coarse bridgeでない。BIO-RC-002/021/069 |
| RC-007 rho_i to continuum rho | Bio progressionとの同字から閉じない。BIO-RC-003/016/069 |
| RC-008 network distance to metric | BioのR3/gridは上流metric constructionの証明でない。BIO-RC-014/069 |
| RC-009 dot rho_i to sigma | prescribed sigma_M / gene sourceから閉じない。BIO-RC-004/021/069 |
| RC-010 L / L_ab to L_mu_nu | Bio closure語はtensor mapを供給しない。BIO-RC-051/069 |
| RC-040 IFGT tau / VED tau | Bio internal timeの定義はtranslationでない。BIO-RC-005/016/069 |
| RC-041 VED sigma / IFGT sigma | same processの継承をしない。BIO-RC-004/021/069 |

8件とも上流OPENのまま。Bio-local redefinitionは許容される別source記述として扱い、
それ自体をbridge bypassの不正・不可能性としない。上流disposition countsに影響しない。

## 16. Downstream attribution candidates

Group N: BIO-RC-072–078。現在のdownstream sourceを修復するのではなく、将来監査へのhandoffである。

| Downstream target | Bio-local record | Candidate handoff |
|---|---|---|
| DOWN-01 / CLM-50 fast/slow confirmed necessarily | NO BIO-LOCAL FAST/SLOW CONFIRMATION RESULT LOCATED | BIO-RC-072 DOWNGRADE、076 OPEN |
| DOWN-05 / CLM-51 same F / same dynamics | different signatures、typed translationなし | BIO-RC-073 SPLIT、076 OPEN |
| DOWN-06 / CLM-52 same second-attractor / internal description | Bioのsubset proposalまで | BIO-RC-074 SPLIT、076 OPEN |
| DOWN-07 / CLM-53 inter-individual maintenance showed | Bioはfuture extension、local resultなし | BIO-RC-075 DOWNGRADE、076 OPEN |
| DOWN-02/03/04 / CLM-54 | nonidentity window / citation不在 / vocabulary reuseを区別 | BIO-RC-077 KEEP |
| DOWN-08 reprises / cross-language figures | duplicateは独立Bio evidenceでない | BIO-RC-078 REVISE handoff |

same glyphはsame dynamicsの証明でない。downstream独自理論の真偽・social homology判定には進まない。
Phase 03ではBio→downstream→Bioという逆向きのexplanatory proof loopはlocateされていない。
今回のattribution修正候補をvicious circularity verdictへ拡張しない。

## 17. Candidate master table

全行のactionは候補。W=source wording/context対象、S=simulation description/provenance対象、
D=downstream handoff対象。これらは重複可の集計用ラベルであり新theory categoriesではない。
数式内容を変える候補は0件。Wには保持・研究課題の記載候補も含み、sourceを今変更する件数ではない。

| BIO-RC | Target | Candidate action | Priority | Current issue / Why | Preserve | Proposed change scope | Evidence / audit trace | Scope tags |
|---|---|---|---|---|---|---|---|---|
| BIO-RC-001 | Iのsource-local identities | SPLIT | P2 | IFGT/Bio/toy/codeの同字は同一carrierを与えない | 各sourceのI定義と観測window | 同字の対応と生物同定を別記、改名なし | CLM-02 CLM-03 CON-01 CF-09 COL-01 BIO-EQ-02 | W |
| BIO-RC-002 | Jの離散・連続・Bio・code関係 | SPLIT | P2 | gene aggregationとvector定義、code不在が混同され得る | Bio currentの定義 | VED J_ij、IFGT vector、Bio J、toy直接積分なしを分離 | CLM-04 CLM-05 CON-02 CF-09 BIO-EQ-03 | W |
| BIO-RC-003 | rhoのdensity / progression | SPLIT | P2 | rho_i、continuum density、rho(I,J)、rho(x)のmap未固定 | 各signatureのlocal意味 | densityとprogressionの別source意味を明示 | CLM-10 CF-12 CON-05 BIO-EQ-07 BIO-EQ-18 | W |
| BIO-RC-004 | sigmaのsource identity | SPLIT | P2 | VED/IFGT/Bio/gene-event/sigma_Mは同processでない | balanceのsource slotとprescribed sigma_M | source-specific roleとgene解釈を分離 | CLM-08 CLM-09 CON-04 BIO-EQ-08 BIO-EQ-34 | W |
| BIO-RC-005 | t / tau / simulation step | SPLIT | P2 | external recording、internal accumulation、stepを同clockにしない | t相対のtau定義 | IFGT tau、VED tau_i、Bio tau、DT/orderの区別 | CLM-10 CLM-11 CON-05 GAP-06 | W |
| BIO-RC-006 | Phi / F / F_k / F(x;theta) | SPLIT | P2 | bias vector、threshold response、state velocityの同字再使用 | source-local signatures | different domainsとcode Phi/F未実装を記載 | CLM-06 CLM-07 CLM-51 CON-03 CON-15 CF-10 COL-03 | W |
| BIO-RC-007 | raw G / G_norm / accumulated B | SPLIT | P1 | raw gradientとglobal normalizationとstateは別object | 各式・code operation | paper raw GとB入力G_norm、Bの蓄積を別記 | CLM-36 CLM-37 CLM-38 CON-12 CF-04 DS-03 DS-07 VR-11 BIO-EQ-27 BIO-EQ-41 | W, S |
| BIO-RC-008 | paper S / code sigmoids | REVISE | P2 | paper one Sにcode k8/k20・exp clipの差 | 各既存functional form | 異なるsteepnessと用途をexecution説明で明示、統一しない | CF-05 DS-04 BIO-EQ-30 BIO-EQ-37 CLM-39 | W, S |
| BIO-RC-009 | theta / sigma signature versions | REVISE | P2 | EN/JA TeXとworking MDでparameter argument省略 | 全既存signature | build版とworking variantを対照、黙って補完しない | CLM-12 CF-02 CF-03 BIO-EQ-13 BIO-EQ-34 BIO-EQ-35 | W |
| BIO-RC-010 | EN/JA build / working / PDF authority | REVISE | P3 | working MDはJA mainのinputでない | 各versionと歴史 | source-of-truth、role wording差、PDF spot-check範囲を明示 | CF-07 CF-08 VR-07 VR-08 VR-09 VR-10 CLM-31 | W |
| BIO-RC-011 | working probability squareの意図 | OPEN | P2 | canonical conditional formとの関係未決 | 両versionを所在付き保存 | typo/shorthand/alternativeの作者意図を未解決として記録 | CLM-31 GAP-14 CF-01 BIO-EQ-21 BIO-EQ-33 | W |
| BIO-RC-012 | その他local glyph衝突 | REVISE | P3 | N長さ/array、B fate/boundary、E energy/commitment等 | 原notation | Phase01 COL-01–16のsource-local索引、同一視のみ予防 | CLM-12 CLM-16 CLM-39 CF-13 COL-04 COL-05 COL-06 COL-07 COL-08 COL-09 COL-10 COL-11 COL-12 COL-13 COL-14 COL-15 COL-16 | W |
| BIO-RC-013 | core state / potential / constitutive / balance content | KEEP | P2 | stronger biology burdenはformal contentの削除理由でない | BIO-EQ-01–09の定義・条件付き構成・balance | formal scopeを保持、physical flux/force証明を付加しない | CLM-01 CLM-02 CLM-04 CLM-06 CLM-08 CON-01 CON-02 CON-03 CON-04 | W |
| BIO-RC-014 | core equation role / domain context | REVISE | P2 | R3、微分可能性、chosen Phi、windowが必要 | 式の符号・係数・operators全て | representation-dependent/effective/conditionalという既存roleを局所明示 | CLM-06 CLM-07 CLM-55 CON-03 CIR-01 CIR-07 GAP-03 | W |
| BIO-RC-015 | internal time accumulation | KEEP | P2 | optional interpretive definition相対tを保持可能 | BIO-EQ-07/18とsource解釈 | physical/biological clock生成証明へ読ませないscope保持 | CLM-10 CON-05 CIR-02 | W |
| BIO-RC-016 | clock / rho functional calibration | OPEN | P2 | progression functionalと実測duration map未固定 | interpretive accumulation | rho specification・duration criterion・upstream time mapを研究課題として記す | CLM-11 CLM-49 GAP-06 CF-12 CON-05 | W |
| BIO-RC-017 | reaction–diffusion / state-space equations | KEEP | P2 | formal PDEとstate dynamicsは独立に保持できる | BIO-EQ-14/16/17の内容 | 生物機構・life basin存在を自動帰結にしない | CLM-15 CLM-19 CON-08 | W |
| BIO-RC-018 | Iのproxy definition / biological identification | SPLIT | P2 | window選択後のquantityとobserved morphogen同定は別 | local structure/constraintの記述 | 定義、対応提案、operational identityを分ける | CLM-02 CLM-03 CON-01 GAP-01 CIR-04 | W |
| BIO-RC-019 | I / morphology observable map | OPEN | P2 | measurement、units、複数proxyの対応が未所在 | source-local proxyとfinite state | 観測window・calibration・independent identificationを未解決として残す | CLM-03 CLM-17 GAP-01 GAP-07 CON-07 | W |
| BIO-RC-020 | gene event→Jという機構的連続化 | DOWNGRADE | P2 | event-to-current map未所在 | gene-event operationsとcurrent slot | established aggregation readingをcandidate process descriptionへ限定する候補 | CLM-05 GAP-02 CON-02 | W |
| BIO-RC-021 | event→J / biological sigma mechanism | OPEN | P2 | source slotだけではmeasured flux/productionでない | balance equation、Delta I表現 | aggregation map、独立source function、measurement対応を未解決化 | CLM-05 CLM-09 GAP-02 GAP-05 CON-02 CON-04 CIR-05 CIR-08 | W |
| BIO-RC-022 | sigma=gene productionの達成済み機構読み | DOWNGRADE | P2 | prescribed forcingは生物生産同定でない | local source/sink description | biological productionはproposed interpretationに限る候補 | CLM-09 GAP-05 CON-04 | W |
| BIO-RC-023 | Phiが生物return / differentiationを説明する読み | DOWNGRADE | P2 | chosen potentialの数学と生物原因mapは別 | gradient-dependent biasとconditional consequence | 生物因果はcandidate response interpretationとして区別 | CLM-07 GAP-03 CON-03 CIR-07 | W |
| BIO-RC-024 | DNA alphabet / theta(s) / event / threshold formal layer | KEEP | P2 | 抽象map表現は具体実装と別に保持可能 | BIO-EQ-10–13、既存threshold labels | genotype→phenotypeを導出したと付加しない | CLM-12 CON-06 CF-11 | W |
| BIO-RC-025 | DNA parametersがdevelopmentを決定する強い読み | DOWNGRADE | P2 | sequence→parameter実装・予測mapなし | DNA-conditioned parameter proposal | 実装済みgenetic mechanismと抽象parameterizationを区別する文言候補 | CLM-13 GAP-04 CON-06 | W |
| BIO-RC-026 | theta(s) / historical quasi-closure provenance | OPEN | P2 | 定数の選定履歴・遺伝子写像・歴史安定化map未固定 | historical interpretationの可能性 | mapとparameter provenanceを未解決、結果に合わせたtuningを推定しない | CLM-13 CLM-14 GAP-04 CF-11 CON-06 CIR-09 | W |
| BIO-RC-027 | threshold classification / finite spatial witness | KEEP | P2 | formal labelsと再現patternのweaker supportあり | BIO-EQ-15、800-step structured pattern、toy limits | observed tissue identityを保持対象へ混入しない | CLM-16 CLM-32 CON-07 RUN-01 RUN-02 EM-01 EM-09 | W, S |
| BIO-RC-028 | stable configurations=observed morphology / morphogenesis説明 | DOWNGRADE | P2 | paired biological mapとdevelopmental mechanism未所在 | RD・threshold・finite structural possibility | 観測同定と機構説明はcandidate interpretationにする候補 | CLM-17 CLM-18 GAP-07 CON-07 CIR-10 | W |
| BIO-RC-029 | intuitive asymmetry→flow→form / generic biology背景 | REVISE | P2 | conceptual sequence、background、model証拠のrole差 | intuitive proposal、same-DNA differentiation背景 | conditional representation・literature背景・toy witnessを区別、普遍必然性を足さない | CLM-55 CLM-56 GAP-07 CON-11 | W |
| BIO-RC-030 | Omega_life subset / conditional return definition | KEEP | P2 | named regionと条件付きattractor用語は保持可能 | BIO-EQ-19、bounded/viable/return/exchange/progression条件 | 定義として保持、region存在・生物life同定の証明を付けない | CLM-19 CLM-22 CON-08 CIR-11 CIR-12 EM-06 | W |
| BIO-RC-031 | model viable region / life identity | SPLIT | P2 | model criterionと生命のoperational criterionが混在 | region definitionとlife perspective | membership定義、dynamical property、生物同定を別claimにする候補 | CLM-22 CLM-23 CON-08 GAP-10 | W |
| BIO-RC-032 | region membershipによるbiological life identification | DOWNGRADE | P2 | 定義のみでは独立life identificationを満たさない | life-as-sustained-motion proposal | 達成済みlife identification読みをproposed interpretationへ限定 | CLM-23 GAP-10 CON-08 | W |
| BIO-RC-033 | life operational criterion / boundary | OPEN | P2 | independent viability・system boundaryのmap未固定 | state-spaceと明示条件 | 観測基準、領域選択、boundary identificationを未解決とする | CLM-23 GAP-10 CON-08 BND-03 BND-04 | W |
| BIO-RC-034 | life region formed endogenously | DOWNGRADE | P2 | generic dynamicsとnot externally imposedのscope不明瞭 | endogenous organizationの研究提案 | preselected state spaceと領域構成の達成を区別する候補 | CLM-24 GAP-11 CON-08 EM-06 | W |
| BIO-RC-035 | exchange/updateがlife maintenanceを説明する読み | DOWNGRADE | P2 | toyにresource/exchange-maintenance機構実装なし | non-equilibrium description | maintenanceをcandidate interpretationとしてsource-localに限定 | CLM-25 GAP-11 CON-08 | W |
| BIO-RC-036 | endogenous region / exchange-maintenance construction | OPEN | P2 | existence・invariant region・resource mapping未固定 | state dynamicsのformal target | 研究課題を明示、toy gridをlife regionへ同定しない | CLM-24 CLM-25 GAP-11 CON-08 | W |
| BIO-RC-037 | life probabilityのpoint→region target reformulation | KEEP | P2 | 数値推定でない概念的eventの再記述 | entry/persistenceの問題設定 | 計算済み確率としないscope保持 | CLM-26 CIR-15 | W |
| BIO-RC-038 | fewer variables / probability reduction wording | REVISE | P2 | measure・projectionなしに定量結論へ飛べない | reformulationのmotivation | dimensional reductionをproposed descriptionに限定、VED dimensionality結果は対象外 | CLM-27 GAP-12 | W |
| BIO-RC-039 | life probability measure / projection | OPEN | P2 | sample space・measure・sampling/calibration未指定 | qualitative probability question | 定量確率と減次mapを研究課題に残す | CLM-27 GAP-12 | W |
| BIO-RC-040 | second-attractor subset / conditional factorization | KEEP | P2 | 概念的set relationとschematic expressionを保持 | BIO-EQ-20/21のcanonical forms | intelligenceの必然的生成・数値確率に変えない | CLM-28 CLM-30 CON-10 | W |
| BIO-RC-041 | history/reuse/sharing条件のforward role | REVISE | P2 | Bioとworkingの強さ・subset説明差 | cognitive forward proposal | additional conditionsとsufficiencyを分離、working role variantを記載 | CLM-29 CON-10 GAP-13 VR-07 VR-10 CIR-14 EM-08 | W |
| BIO-RC-042 | second-attractor biological/cognitive translation | OPEN | P2 | toyにhistory/reference/sharing実装なし | Bio-local forward perspective | 独立criterionとtranslationを下流研究へ引渡す | CLM-29 GAP-13 CON-10 | W |
| BIO-RC-043 | 800-step outputをstable solutionsと呼ぶ読み | DOWNGRADE | P1 | 1600/3200も変化、B mask全域化 | 800-step再現可能pattern | stationary/asymptotic読みをfinite-horizon descriptionへ限定する候補 | CLM-45 GAP-08 DS-08 RUN-20 RUN-21 CON-09 | W, S |
| BIO-RC-044 | attractor-like / robustness / returnの多義 | REVISE | P2 | 有限relaxation、recommitment、saturationは異なる | 限定された類比と条件付きreturn定義 | termごとに時間・field・摂動範囲を付す、全attractor語を撤去しない | CLM-19 CLM-20 CLM-21 CLM-45 CON-09 CIR-12 CIR-13 RUN-22 RUN-23 RUN-24 | W, S |
| BIO-RC-045 | biological robustness / regenerationの説明読み | DOWNGRADE | P2 | 小摂動応答は大擾乱再構成・biological returnでない | robustness/regenerationのconceptual interpretation | 達成済み説明の読みをcandidateへ限定、既にinterpretiveな箇所は保持 | CLM-20 CLM-21 GAP-08 GAP-09 CON-09 EM-07 | W |
| BIO-RC-046 | basin / stability / general regeneration | OPEN | P2 | bidirectional return・existence・invariance・large repair未確立 | finite relaxationとmonotonic recommitment | 定理・protocol・生物mapを研究課題に残し、無限時間不可能性を言わない | CLM-20 CLM-21 CLM-45 GAP-08 GAP-09 CON-09 RUN-24 | W |
| BIO-RC-047 | individual toy evolution / updates / diagnostics | KEEP | P2 | current codeでfinite witnessを再現 | BIO-EQ-24–30、36–48のsource-specific content | paper/code variantsを統一せず、model-local contentを保持 | CLM-33 CLM-34 CLM-35 CLM-36 CLM-37 CLM-39 CLM-44 RUN-03 RUN-04 CON-13 | W, S |
| BIO-RC-048 | paper/code execution correspondence | REVISE | P1 | DT、new M、新N/B、clips等が一つの式から読めない | 元PDE・step rule・code全て | source side-by-side説明とactual順序を明示、数式変更しない | CF-06 DS-05 CLM-33 CLM-34 CLM-39 BIO-EQ-43 BIO-EQ-44 BIO-EQ-45 | W, S |
| BIO-RC-049 | compact M/I/N/B/E navigation vs dependencies | SPLIT | P1 | NはBへ直接入力されない | compact summaryのreading-order用途と各式 | 11edgesをrole別参照に分け、navigationとexecutionを別表示する候補 | CLM-42 GAP-15 DS-06 VR-12 CON-11 RUN-11 RUN-12 | W, S |
| BIO-RC-050 | one hierarchical generation path | DOWNGRADE | P2 | PDE/diagnostic/gating/physical interpretationは同関係でない | staged finite model perspective | 一様なcausal/biological generationとしての読みに限定を置く候補 | CLM-42 CLM-43 GAP-15 CON-11 CON-15 | W, S |
| BIO-RC-051 | toy hierarchy→Phi/J/quasi-closure/sub-attractor | OPEN | P2 | direct Phi/J integrationやtyped mapなし | sourceのstructural analogy | mapping/attractor criterionを未解決として残す | CLM-43 GAP-19 CF-09 CON-15 BIO-EQ-32 | W, S |
| BIO-RC-052 | B definition / boundary stabilization description | REVISE | P1 | Bは瞬間gradient extractionでなくaccumulated state | gradient-sensitive finite bands | B roleと800-step horizonを記載、3200の全grid maskを踏まえ常時boundaryだけとはしない | CLM-37 CLM-38 DS-07 DS-08 VR-11 CON-12 RUN-13 RUN-14 RUN-21 EM-02 | W, S |
| BIO-RC-053 | B→membrane / organism boundary map | OPEN | P2 | sourceはboundary-like、具体膜identityはlocateしない | boundary-like model label | operational biological boundaryを将来課題とし、存在しない膜claimを新設/撤回しない | CLM-38 GAP-16 CON-12 BND-08 | W |
| BIO-RC-054 | finite eye-like bright-lobe pattern | KEEP | P2 | default tracked pixels再現 | 二つの相対的bright lobesとtoy limitation | 器官同定や二独立componentを保持対象にしない | CLM-40 RUN-01 RUN-02 EM-05 | W, S |
| BIO-RC-055 | central no-E / paired topology wording | REVISE | P1 | 中心E約0.69/0.70、>0.5 maskは1component | 相対的中央contrast低下とbright lobes | zero/exclusionや独立二componentでなく観測された有限形状を記述する候補 | CLM-40 DS-09 RUN-03 CON-14 | W, S |
| BIO-RC-056 | final drawing非入力 / positional geometry preload | SPLIT | P1 | 完成配列は非入力だがcoarse locationはwindow入力 | no completed final-shape encoding | output shape、output location、window conditional responseを別記 | CLM-41 GAP-17 DS-10 CON-14 EM-04 EM-05 | W, S |
| BIO-RC-057 | geometry-free / spontaneous eye emergence reading | DOWNGRADE | P2 | Eはstrongly window-dependent、no-eyeで0 | 制約下のstructural possibility | unqualified geometry非入力の強い読みだけ限定、眼機構主張を新設しない | CLM-41 GAP-17 DS-10 RUN-16 RUN-17 RUN-18 RUN-19 | W, S |
| BIO-RC-058 | E→biological eye correspondence | OPEN | P2 | measurement map・organism calibration未所在 | eye-like label | 眼のoperational correspondenceを未解決、toy削除にしない | CLM-40 CLM-41 GAP-17 | W |
| BIO-RC-059 | central/stable/neural-like N wording | REVISE | P2 | 小seed/thresholdで保持するがsourceで移動、長時間拡幅 | 800-step neural-like central band | source・threshold・horizon条件を明記、neural tissue同定を避ける候補 | CLM-35 CLM-45 GAP-18 RUN-05 RUN-06 RUN-11 RUN-12 RUN-15 RUN-21 EM-03 | W, S |
| BIO-RC-060 | limited reproducibility / numerical observation | KEEP | P3 | default deterministic、7pixels再現、限定R4 | 既存toy limitsとPhase05 audit witness | audit記録scopeで保持、主理論へ新proofとして転用しない | CLM-32 CLM-35 CLM-40 CLM-44 GAP-18 CON-13 RUN-01 RUN-02 RUN-03 RUN-04 | S |
| BIO-RC-061 | PNG provenance / exact再現の表記 | REVISE | P3 | pixel7/7、byte0/7、metadataとIDAT差 | tracked7PNGとcurrent reproduction | pixel/byte/historical manifestを区別してfuture provenanceに記載 | DS-01 GAP-18 CLM-44 CF-13 U11 | W, S |
| BIO-RC-062 | historical GIF / original-run lineage | OPEN | P3 | unprefixed path不在、ignored alternateはpixels不同 | historical artifactとfresh generator capability | 元config・environmentを未解決、同名からrun identityを逆算しない | DS-02 GAP-18 CLM-44 U16 | W, S |
| BIO-RC-063 | future distribution / caption synchronization | REVISE | P3 | source候補採用後に重複caption/PDFがずれるrisk | 現tracked画像・歴史・currentPDF | 承認後だけEN/JA/caption/README/PDFを同期、今は再生成しない | DS-01 DS-02 DS-08 DS-09 DS-10 CLM-40 CLM-45 CF-08 | W, S |
| BIO-RC-064 | model state→biological observables / calibration | OPEN | P2 | E0=2/E1=8、E2–5=0、data/map未所在 | model fields・diagnostics・qualitative analogies | M/I/N/B/E/G units、measurement、paired datasetを研究課題として明示 | CLM-03 CLM-17 CLM-35 CLM-38 CLM-40 CLM-49 GAP-01 GAP-07 GAP-16 CON-13 U10 | W |
| BIO-RC-065 | toy limitations / empirical future work | KEEP | P2 | specific biological mechanismを示さないとsource明示 | S15 structural possibility、future empirical tasks | 現状scope保持、absence of dataをfalsificationにしない | CLM-01 CLM-32 CLM-49 CON-13 | W |
| BIO-RC-066 | bibliography / biological background as evidence | REVISE | P3 | refs8はcurrent build未引用、paired comparisonなし | 背景文脈・refs.bib・generic observations | background、citation usage、actual dataの所在を分ける、文献/証拠を追加しない | CLM-56 CLM-49 GAP-07 | W |
| BIO-RC-067 | explicit IFGT/Bio nonidentity correspondence | KEEP | P2 | sourceにnot identityを明記 | proposed correspondenceとBio-local redefinition | 上流OPENを閉じず現scope保持 | CLM-01 CLM-47 GAP-19 | W |
| BIO-RC-068 | same formal structure / role across scales | DOWNGRADE | P2 | typed scale map・invariant・cross-model test未所在 | molecule/cell/tissueへのcommon description proposal | 達成済みuniversalityの読みに限りproposed analogyへ限定 | CLM-46 GAP-19 | W |
| BIO-RC-069 | IFGT/Bio / biological scale translation | OPEN | P2 | carrier、coarse-graining、parameter/time map未固定 | source-local definitions | 8upstream OPENを継承成立済みにせずBio translationも研究課題に残す | CLM-43 CLM-46 CLM-47 GAP-19 CON-15 | W |
| BIO-RC-070 | L1 note counterpart locator / exact correspondence | OPEN | P3 | S13は特定path/versionを指定しない | L3/L1 structural comparison | paired source/versionとexact translationを未解決、任意noteを選ばない | CLM-48 GAP-20 U15 | W |
| BIO-RC-071 | L3/L1 same phenomenon / same structure wording | REVISE | P2 | not direct translationとexact同一の読みを分ける必要 | metaphorとformal layerの比較 | proposed correspondenceのscopeを局所明示する候補 | CLM-48 GAP-20 | W |
| BIO-RC-072 | Bio confirmed fast/slow necessarily attribution | DOWNGRADE | P1 | dedicated Bio-local diagnostic/result未所在 | 下流fast/slow proposalの研究対象 | Bio確認済み・必然的根拠という帰属を外す候補、下流独自論証は別監査 | CLM-50 GAP-21 DS-11 DOWN-01 U13 | W, D |
| BIO-RC-073 | same F glyph→same dynamics attribution | SPLIT | P1 | different signatures/domainでidentity mapなし | 下流local Fとformal analogy | 同字、analogy、dynamical identityの別claim化をhandoff | CLM-51 GAP-21 DOWN-05 CF-10 CF-11 CIR-21 | W, D |
| BIO-RC-074 | L_R/L_E same second-attractor / internal description | SPLIT | P2 | Bio set relationから下流operator identityは出ない | related conceptual comparison | analogyとestablished same structureを分離する候補 | CLM-52 GAP-21 DOWN-06 CON-10 | W, D |
| BIO-RC-075 | Bio showed inter-individual maintenance attribution | DOWNGRADE | P1 | Bio-local construction/resultなし、future extensionのみ | inter-individual future perspective | 既成果帰属をfuture relation/下流提案として扱う候補 | CLM-53 GAP-22 DS-12 DOWN-07 | W, D |
| BIO-RC-076 | downstream identity / mechanism translations | OPEN | P2 | F、second attractor、sharingのtyped map未所在 | downstream local theoriesを否定しない | translation・independent evidenceを下流監査へ残す | CLM-50 CLM-51 CLM-52 CLM-53 GAP-21 GAP-22 DOWN-01 DOWN-05 DOWN-06 DOWN-07 | W, D |
| BIO-RC-077 | vocabulary reuse / scoped nonidentity references | KEEP | P3 | Bioのlife vocabulary継承は強い帰属と別 | Intelligence I descriptive substrate、window comparison | DOWN-02/03/04を過剰修正せず、Bio未引用の枝へ依存を発明しない | CLM-54 DOWN-02 DOWN-03 DOWN-04 | W, D |
| BIO-RC-078 | downstream reprises / figures handoff | REVISE | P3 | duplicate同文を独立証拠にしない | historical titles・recordsとlocal concepts | 採用後のEN/JA/summary/figure同期を下流ownerへ引渡す候補のみ | CLM-50 CLM-51 CLM-52 CLM-53 DOWN-08 | W, D |

### CLM reverse trace — 56/56

同じCLMの異なるaspectへ複数候補が対応する。下表のsource locatorはPhase 04 §3を継承し、候補から一次sourceへ戻れるようにする。
| Claim | Current source locator | BIO-RC candidates |
|---|---|---|
| CLM-01 | S03/S16:7–15,41; S17 | BIO-RC-013, BIO-RC-065, BIO-RC-067 |
| CLM-02 | S04:15; S06:11–15 | BIO-RC-001, BIO-RC-013, BIO-RC-018 |
| CLM-03 | S09:13–17; S06; BI-01 | BIO-RC-001, BIO-RC-018, BIO-RC-019, BIO-RC-064 |
| CLM-04 | S06:19–43; S07:28–33 | BIO-RC-002, BIO-RC-013 |
| CLM-05 | S08:21–33; ML-07 | BIO-RC-002, BIO-RC-020, BIO-RC-021 |
| CLM-06 | S07:37–53 | BIO-RC-006, BIO-RC-013, BIO-RC-014 |
| CLM-07 | S08:45; S09:40; S14:110–113 | BIO-RC-006, BIO-RC-014, BIO-RC-023 |
| CLM-08 | S07:19–24; BIO-EQ-08 | BIO-RC-004, BIO-RC-013 |
| CLM-09 | S08:33; S09:26 | BIO-RC-004, BIO-RC-021, BIO-RC-022 |
| CLM-10 | S06:47–51; S10:21–25 | BIO-RC-003, BIO-RC-005, BIO-RC-015 |
| CLM-11 | S16:27 | BIO-RC-005, BIO-RC-016 |
| CLM-12 | S08:7–23,49–53 | BIO-RC-009, BIO-RC-012, BIO-RC-024 |
| CLM-13 | S08:53,57; S16:31 | BIO-RC-025, BIO-RC-026 |
| CLM-14 | S08:69 | BIO-RC-026 |
| CLM-15 | S09:21–28 | BIO-RC-017 |
| CLM-16 | S09:44–53 | BIO-RC-012, BIO-RC-027 |
| CLM-17 | S08:57; S09:53–57 | BIO-RC-019, BIO-RC-028, BIO-RC-064 |
| CLM-18 | S09:57,65; S04:9 | BIO-RC-028 |
| CLM-19 | S07:69; S10:37 | BIO-RC-017, BIO-RC-030, BIO-RC-044 |
| CLM-20 | S09:61; S10:47,55; S19 life §7.8 | BIO-RC-044, BIO-RC-045, BIO-RC-046 |
| CLM-21 | S10:55; S19 life §7.8 | BIO-RC-044, BIO-RC-045, BIO-RC-046 |
| CLM-22 | S10:27–37 | BIO-RC-030, BIO-RC-031 |
| CLM-23 | S10:29,43,59 | BIO-RC-031, BIO-RC-032, BIO-RC-033 |
| CLM-24 | S07:57,80; S10:39 | BIO-RC-034, BIO-RC-036 |
| CLM-25 | S10:43; S16:19–23 | BIO-RC-035, BIO-RC-036 |
| CLM-26 | S11:19–37 | BIO-RC-037 |
| CLM-27 | S11:29–31 | BIO-RC-038, BIO-RC-039 |
| CLM-28 | S12:17–21 | BIO-RC-040 |
| CLM-29 | S12:11–13,21,33–45; S19 intelligence §9.3 | BIO-RC-041, BIO-RC-042 |
| CLM-30 | S12:25–29; S02 probability | BIO-RC-040 |
| CLM-31 | S19 intelligence §9.4; Phase 01 CF-01 | BIO-RC-010, BIO-RC-011 |
| CLM-32 | S14:101,119; S15:99–113; S24 | BIO-RC-027, BIO-RC-060, BIO-RC-065 |
| CLM-33 | S14:25–30; S21 run_simulation | BIO-RC-047, BIO-RC-048 |
| CLM-34 | S14:33–38; S21 run_simulation | BIO-RC-047, BIO-RC-048 |
| CLM-35 | S14:41–46; S22; S24 N | BIO-RC-047, BIO-RC-059, BIO-RC-060, BIO-RC-064 |
| CLM-36 | S14:49–53; S21 gradient_magnitude | BIO-RC-007, BIO-RC-047 |
| CLM-37 | S14:54–59; S21 run_simulation | BIO-RC-007, BIO-RC-047, BIO-RC-052 |
| CLM-38 | S14:53; S15:18,57 | BIO-RC-007, BIO-RC-052, BIO-RC-053, BIO-RC-064 |
| CLM-39 | S14:62–68; S21 make_eye_window/run_simulation | BIO-RC-008, BIO-RC-012, BIO-RC-047, BIO-RC-048 |
| CLM-40 | S22 Toy Eye; S15:25,64; S24 E | BIO-RC-054, BIO-RC-055, BIO-RC-058, BIO-RC-060, BIO-RC-063, BIO-RC-064 |
| CLM-41 | S14:5,76,101; S15:9,21,104; S02:473 | BIO-RC-056, BIO-RC-057, BIO-RC-058 |
| CLM-42 | S14:87–96; S15:92–95 | BIO-RC-049, BIO-RC-050 |
| CLM-43 | S14:107–115 | BIO-RC-050, BIO-RC-051, BIO-RC-069 |
| CLM-44 | S15 Observations; S21 print_summary/plotting | BIO-RC-047, BIO-RC-060, BIO-RC-061, BIO-RC-062 |
| CLM-45 | S14:101,113; S15:25,107 | BIO-RC-043, BIO-RC-044, BIO-RC-046, BIO-RC-059, BIO-RC-063 |
| CLM-46 | S08:59–61; S17:5 | BIO-RC-068, BIO-RC-069 |
| CLM-47 | S04:15; S11:37; S16:23 | BIO-RC-067, BIO-RC-069 |
| CLM-48 | S13:14–20,44; U15 | BIO-RC-070, BIO-RC-071 |
| CLM-49 | S16:31–37; S17:9; AT-15 | BIO-RC-016, BIO-RC-064, BIO-RC-065, BIO-RC-066 |
| CLM-50 | DOWN-01 / S31 SSO:9–23 | BIO-RC-072, BIO-RC-076, BIO-RC-078 |
| CLM-51 | DOWN-05 / II inference:21–29 | BIO-RC-006, BIO-RC-073, BIO-RC-076, BIO-RC-078 |
| CLM-52 | DOWN-06 / II stopping:67,106 | BIO-RC-074, BIO-RC-076, BIO-RC-078 |
| CLM-53 | DOWN-07 / II social:134,165 | BIO-RC-075, BIO-RC-076, BIO-RC-078 |
| CLM-54 | DOWN-04 / Intelligence I Introduction:15 | BIO-RC-077 |
| CLM-55 | S05:13–27; S04:9 | BIO-RC-014, BIO-RC-029 |
| CLM-56 | S04:5; Phase 00 EMP-01 | BIO-RC-029, BIO-RC-066 |

### Phase 05 discrepancy reverse trace — 12/12

| DS ID | BIO-RC candidates |
|---|---|
| DS-01 | BIO-RC-061, BIO-RC-063 |
| DS-02 | BIO-RC-062, BIO-RC-063 |
| DS-03 | BIO-RC-007 |
| DS-04 | BIO-RC-008 |
| DS-05 | BIO-RC-048 |
| DS-06 | BIO-RC-049 |
| DS-07 | BIO-RC-007, BIO-RC-052 |
| DS-08 | BIO-RC-043, BIO-RC-052, BIO-RC-063 |
| DS-09 | BIO-RC-055, BIO-RC-063 |
| DS-10 | BIO-RC-056, BIO-RC-057, BIO-RC-063 |
| DS-11 | BIO-RC-072 |
| DS-12 | BIO-RC-075 |

### Phase 04 evidence burden reverse trace — 22/22

| GAP ID | BIO-RC candidates |
|---|---|
| GAP-01 | BIO-RC-018, BIO-RC-019, BIO-RC-064 |
| GAP-02 | BIO-RC-020, BIO-RC-021 |
| GAP-03 | BIO-RC-014, BIO-RC-023 |
| GAP-04 | BIO-RC-025, BIO-RC-026 |
| GAP-05 | BIO-RC-021, BIO-RC-022 |
| GAP-06 | BIO-RC-005, BIO-RC-016 |
| GAP-07 | BIO-RC-019, BIO-RC-028, BIO-RC-029, BIO-RC-064, BIO-RC-066 |
| GAP-08 | BIO-RC-043, BIO-RC-045, BIO-RC-046 |
| GAP-09 | BIO-RC-045, BIO-RC-046 |
| GAP-10 | BIO-RC-031, BIO-RC-032, BIO-RC-033 |
| GAP-11 | BIO-RC-034, BIO-RC-035, BIO-RC-036 |
| GAP-12 | BIO-RC-038, BIO-RC-039 |
| GAP-13 | BIO-RC-041, BIO-RC-042 |
| GAP-14 | BIO-RC-011 |
| GAP-15 | BIO-RC-049, BIO-RC-050 |
| GAP-16 | BIO-RC-053, BIO-RC-064 |
| GAP-17 | BIO-RC-056, BIO-RC-057, BIO-RC-058 |
| GAP-18 | BIO-RC-059, BIO-RC-060, BIO-RC-061, BIO-RC-062 |
| GAP-19 | BIO-RC-051, BIO-RC-067, BIO-RC-068, BIO-RC-069 |
| GAP-20 | BIO-RC-070, BIO-RC-071 |
| GAP-21 | BIO-RC-072, BIO-RC-073, BIO-RC-074, BIO-RC-076 |
| GAP-22 | BIO-RC-075, BIO-RC-076 |

### Phase 02 role conflation reverse trace — 15/15

| CON ID | BIO-RC candidates |
|---|---|
| CON-01 | BIO-RC-001, BIO-RC-013, BIO-RC-018 |
| CON-02 | BIO-RC-002, BIO-RC-013, BIO-RC-020, BIO-RC-021 |
| CON-03 | BIO-RC-006, BIO-RC-013, BIO-RC-014, BIO-RC-023 |
| CON-04 | BIO-RC-004, BIO-RC-013, BIO-RC-021, BIO-RC-022 |
| CON-05 | BIO-RC-003, BIO-RC-005, BIO-RC-015, BIO-RC-016 |
| CON-06 | BIO-RC-024, BIO-RC-025, BIO-RC-026 |
| CON-07 | BIO-RC-019, BIO-RC-027, BIO-RC-028 |
| CON-08 | BIO-RC-017, BIO-RC-030, BIO-RC-031, BIO-RC-032, BIO-RC-033, BIO-RC-034, BIO-RC-035, BIO-RC-036 |
| CON-09 | BIO-RC-043, BIO-RC-044, BIO-RC-045, BIO-RC-046 |
| CON-10 | BIO-RC-040, BIO-RC-041, BIO-RC-042, BIO-RC-074 |
| CON-11 | BIO-RC-029, BIO-RC-049, BIO-RC-050 |
| CON-12 | BIO-RC-007, BIO-RC-052, BIO-RC-053 |
| CON-13 | BIO-RC-047, BIO-RC-060, BIO-RC-064, BIO-RC-065 |
| CON-14 | BIO-RC-055, BIO-RC-056 |
| CON-15 | BIO-RC-006, BIO-RC-050, BIO-RC-051, BIO-RC-069 |

### Phase 01 source conflict reverse trace — 13/13

| CF ID | BIO-RC candidates |
|---|---|
| CF-01 | BIO-RC-011 |
| CF-02 | BIO-RC-009 |
| CF-03 | BIO-RC-009 |
| CF-04 | BIO-RC-007 |
| CF-05 | BIO-RC-008 |
| CF-06 | BIO-RC-048 |
| CF-07 | BIO-RC-010 |
| CF-08 | BIO-RC-010, BIO-RC-063 |
| CF-09 | BIO-RC-001, BIO-RC-002, BIO-RC-051 |
| CF-10 | BIO-RC-006, BIO-RC-073 |
| CF-11 | BIO-RC-024, BIO-RC-026, BIO-RC-073 |
| CF-12 | BIO-RC-003, BIO-RC-016 |
| CF-13 | BIO-RC-012, BIO-RC-061 |

### Execution / source-role trace

| Prior trace | Candidate / what remains distinct |
|---|---|
| VR-11 | BIO-RC-007/052: gradient-derived quantity と accumulating B |
| VR-12 | BIO-RC-049: compact reading order と actual dependency |
| RUN-01/02/03/04 | BIO-RC-027/047/054/060/061: default / raw / pixel reproduction |
| RUN-05/06 | BIO-RC-059/060: seed-local finite pattern |
| RUN-07/08/09/10 | BIO-RC-060/052: source strength / diffusion局所感度、R4限定 |
| RUN-11/12 | BIO-RC-049/059: N閾値でB不変、direct N inputなし |
| RUN-13/14 | BIO-RC-052/060: B threshold / topology感度 |
| RUN-15 | BIO-RC-056/059: sourceによる位置変化 |
| RUN-16/17/18/19 | BIO-RC-056/057: eye mode / disabled、aliasを別modelに数えない |
| RUN-20/21 | BIO-RC-043/052/059: long-time evolution / mask全域化 |
| RUN-22/23/24 | BIO-RC-044/045/046: relaxation / recommitment / finite no-returnを分離 |
| CIR / EM handoffs | BIO-RC-018/026/028/030/041/044/049/052/056/076: definition・preload・interpretationを分離。serious vicious circularityの新判定なし |

## 18. Preserve / change / OPEN matrix

| Domain | Preserve | Change candidate | Must remain OPEN |
|---|---|---|---|
| core field equations | local definitions、balance、conditional potential/current | BIO-RC-001–018: identityとrole/domainの記述 | clock、rho/Phi specification、biological response map |
| DNA / thresholds | sequence、abstract theta(s)、threshold/event | BIO-RC-009/024–026: version・mechanism scope | genotype→parameter、history provenance、event aggregation |
| morphogenesis | RD、model classification、finite spatial witness | BIO-RC-027–029: biological identificationとbackgroundを区別 | observable / convergence / organism map |
| life attractor | region definition、conditional return、life perspective | BIO-RC-030–042: definition/identity/endogenous/probabilityのaspect分離 | life criterion、region existence、measure、second-attractor map |
| toy simulation | existing model、individual update、24run audit findings | BIO-RC-047–051: executionとnavigation記述 | Phi/J/quasi-closure translation |
| boundary | gradient-sensitive accumulated B、finite bands | BIO-RC-007/052: extraction/state/時間scope | membrane / organism boundary map |
| eye | finite bright lobes、imposed-cue response | BIO-RC-054–058: topology / center / location scope | eye biological measurement / mechanism mapping |
| neural pattern | finite neural-like band | BIO-RC-059: source/threshold/horizon限定 | neural tissue observable map |
| attractor / stability | conditional concept、limited analogy、finite response | BIO-RC-043–046: stationary / robustness / regeneration強度 | basin、stability、general return、biological regeneration |
| empirical correspondence | model variables、E1 analogies、future work | BIO-RC-064–066: diagnosis / background / empiricalの区別 | units、dataset pairing、calibration、independent replication |
| IFGT relation | explicit nonidentity / proposed correspondence | BIO-RC-067–071: universal/exact reading限定 | 8upstream bridges、Bio scale maps、L1 locator |
| downstream reuse | local concepts、vocabulary / analogies | BIO-RC-072–078: unsupported achievement attributionのhandoff | identity translation、fast/slow / social dedicated result |
| artifacts | tracked7PNG、currentPDF、historical artifacts | BIO-RC-060–063: provenanceと将来同期 | historical GIF/original run configuration |

## 19. Dependency order

以下は候補を将来検討する順序であって実装開始ではない。研究OPENの解決をscope修正の前提にしない。

| Order | Candidate class | Dependency / gate |
|---|---|---|
| 1 | source identity / artifact truth: 001–012, 061/062/070 | build版とworking版、pixelsとbytes、exact source locatorを先に分離 |
| 2 | notation / role split: 018/031/049/056/073/074 | 同字・definition/identity・navigation/executionを分ける |
| 3 | formal equation scope: 013–017/024/027/030/037/040/047 | 保持すべきformal contentを固定。式修正には進まない |
| 4 | simulation execution correspondence: 007/008/048/049/052/055/056 | codeをpaperへ黙って置換せず両versionのscopeを記す |
| 5 | stability / attractor wording: 043–046/059 | finite horizon、long-time変化、returnの方向を区別 |
| 6 | biological identification: 019–029/032–042/053/057/058/064–066 | weaker constructionを保持、measurementやmechanismはOPENのまま |
| 7 | IFGT / cross-scale: 067–071 | upstream dispositionsを越えず、same roleをtyped mapにしない |
| 8 | downstream attribution: 072–078 | Bio-local supportに対して帰属を整合。下流理論全体の改訂は別scope |
| 9 | distribution / figures / PDFs: 063/078 | Phase 07で選択された候補の別途実装承認後、sourceから同期 |

BIO-RCの番号を省略した数字は同じBIO-RC namespaceを指す。
候補一覧は作業指示の承認ではない。最終選択、具体実装、配布同期は今回行わない。

## 20. What not to change

候補は以下を要求しない。

- equation deletion、係数・sign・operator・index・functional formの改変。
- toy model removal、parameter retuning、source modes/gates/DTのredesign。
- tracked image deletion、PDFの無断置換、historical recordの消去。
- upstream VED/IFGT audit reopening、上流OPEN bridgeの解決・FALSE化。
- empirical falsification、Bio-IFGT invalidという総合判定。
- lifeをattractorとしてmodel化できない、制約下でeye-like structureが生じ得ないという主張。
- Phase 05の監査runを主理論の追加生物学的証拠・定理へ移すこと。
- working/canonical sourceの無trace統合、Bio-localにない膜機構や個体間modelの新設。

### RETIRE検討の結果

RETIRE候補は0件。absence of validationを理由にした退役は提案しない。

| Examined wording | Selected candidate alternative | RETIREしない理由 |
|---|---|---|
| central region does not produce E | BIO-RC-055 REVISE | literal exclusionは合わないが中央contrast低下という正確な記述が残る |
| direct N to Bとして読むcompact chain | BIO-RC-049 SPLIT / 050 DOWNGRADE | navigation順としての用途とindividual equationsを保持できる |
| Bio confirmed fast/slow necessarily | BIO-RC-072 DOWNGRADE | confirmation帰属は保持できないが下流proposalとの区別に弱い読みが残る |
| Bio showed inter-individual maintenance | BIO-RC-075 DOWNGRADE | Bioのfuture extensionとの関連は保持できる |
| working probability square | BIO-RC-011 OPEN | obsolete/typoと断定するauthorityがなく、履歴を消す理由にしない |

最終Phase 07で別候補が選ばれる可能性を閉じない。

## 21. Phase-06 outcome

| Count / scope | Candidate result |
|---|---|
| Total BIO-RC | 78 (BIO-RC-001–078) |
| KEEP | 14 |
| REVISE | 18 |
| DOWNGRADE | 15 |
| SPLIT | 13 |
| RETIRE | 0 |
| OPEN | 18 |
| P1 | 10 |
| P2 | 58 |
| P3 | 10 |
| Equation-affecting candidates | 0（数学的内容の変更・削除を要求する候補） |
| Source-wording candidates | 77（W、KEEP/OPENを含むcontext対象。実編集件数でない） |
| Simulation-description candidates | 20（S、Wと重複可） |
| Downstream-handoff candidates | 7（D、Wと重複可） |
| New simulation runs / evidence | 0 / 0（Phase 05の既存findingsのみ継承） |
| Trace coverage | CLM56/56、DS12/12、GAP22/22、CON15/15、CF13/13、VR-11/12、EDGE11/11、RUN24/24 |
| Upstream bridge disposition changes | 0、8 OPENはOPENのまま |
| Final dispositions / final closure | 未決定 / 未実施 |

上記の候補件数はfinal disposition countsではない。Phase 04のburden表・Phase 05のR4/E分類は書換えない。
P1は数式修復の承認でも、Bio全体のinvalidity判定でもない。

### Validation / write scope

検証対象は本recordとREADMEのみ。以下は実施結果である。
Phase 07は作成せず、source / simulation / tracked outputs / PDF / downstream / 上流監査は変更しない。

- Local links / source paths: PASS。本record41 + README10 = 51 relative targetsが存在する。
- Markdown fences / display math / tables: PASS。fence/display delimiterの不均衡なし。本record19表 + README1表のcolumn数一致、trailing whitespaceなし。
- Candidate IDs: PASS。master tableのBIO-RC-001–078は重複・欠番なし。本文の全BIO-RC参照も範囲内。
- Counts: PASS。KEEP14 / REVISE18 / DOWNGRADE15 / SPLIT13 / RETIRE0 / OPEN18 = 78。P1=10 / P2=58 / P3=10 = 78。scope tagsはW77 / S20 / D7で再集計一致。
- Trace coverage: PASS。master tableからCLM56/56、DS12/12、GAP22/22、CON15/15、CF13/13へ対応。VR-11/12、EDGE11、RUN24を別表で追跡。BIO-EQ / COL / CIR / BND / EM / DOWNの参照IDは先行記録に存在する。
- Preservation review: PASS。formal contentのKEEPとbiological identificationのDOWNGRADE/OPENをaspect別に保持。R4の限定、E0/E1、pixel/byte差、long-time変化、location preload、下流の帰属限定を維持。最終dispositionは未固定。
- Write scope: PASS。開始時1433既存filesのSHA-256比較で変更は本枝READMEのみ、削除0、新規は本recordのみ。source / equations / code / tracked images / PDFs / downstream / Phase 00–05 / upstream recordsはbyte不変。
- git diff --check: PASS。untracked新recordは上記Markdown/whitespace検査も別途実施。既存96 tracked modificationsと3 untracked research directoriesを保持、今回のtemp/build artifact追加なし。
- Simulation / web: 新run・再build・外部researchなし。Phase 05の既存記録のみ参照。
- Commit / push: 実施しない。

Phase 06候補作成で停止し、Phase 07 final audit recordへ進まない。
