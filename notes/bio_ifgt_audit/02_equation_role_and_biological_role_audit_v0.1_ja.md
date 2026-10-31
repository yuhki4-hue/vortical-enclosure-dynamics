# Bio-IFGT equation role / biological-role audit v0.1

## 0. Status

- Bio-IFGT audit: **IN PROGRESS**
- Phase 00 dependency / inheritance: **COMPLETE**
- Phase 01 equation / symbol inventory: **COMPLETE**
- Phase 02 equation role / biological-role audit: **COMPLETE**
- Phase 03 preload / boundary / circularity audit: **NOT STARTED**
- Upstream VED equation audit / core revision: **CLOSED / CLOSED**

最初のauthorityは[監査README](README_ja.md)、[Phase 00](00_dependency_and_inheritance_record_v0.1_ja.md)、
[Phase 01](01_equation_and_symbol_inventory_v0.1_ja.md)。
48 BIO-EQ IDs、S-source IDs、source hierarchy、working variants、上流OPENを引き継ぐ。
本稿の役割はclassificationであり、validity / circularity / empirical adequacy / evidence gradeではない。
sourceの主張を引用・分類することと、その主張を承認することを分ける。

EN TeX + self-contained JA TeX、JA working Markdown、code/READMEを別sourceとして読む。
PDF spot-checkはPhase 01 §11の結果を参照するのみで、今回PDF再検査・再生成は行わない。
source / equation / simulation / upstream recordsは無変更。新notation / theory / bridgeなし。

## 1. Role vocabulary and guards

\[
\text{mathematical role}\neq\text{biological interpretation}
\]
\[
\text{model variable}\neq\text{biological observable}
\]
\[
\text{formal attractor / region}\neq\text{life}
\]
\[
\text{finite update rule}\neq\text{biological developmental mechanism}
\]
\[
\text{simulation dependency}\neq\text{causal generation chain}
\]
\[
\text{boundary / initial condition}\neq\text{biological mechanism}
\]
\[
\text{simulation convenience}\neq\text{biological structure}
\]

READMEの6 inheritance gatesも維持する。これらはidentity/roleを混ぜないためのguardで、否定的な研究結論ではない。

Mathematical roles: DEFINITION; STATE / DOMAIN DECLARATION; ALGEBRAIC CONSTRUCTION; CONSTITUTIVE RELATION; BALANCE / CONTINUITY RELATION; UPDATE / EVOLUTION RULE; THRESHOLD / SWITCHING RULE; CONSTRAINT; BOUNDARY / INITIAL CONDITION; PHENOMENOLOGICAL / EFFECTIVE RELATION; OBSERVABLE / DIAGNOSTIC; VISUALIZATION TRANSFORM; SCHEMATIC FACTORIZATION; ROLE UNRESOLVED.

Biological roles: BIOLOGICAL STATE DESCRIPTION; BIOLOGICAL PROCESS DESCRIPTION; BIOLOGICAL MECHANISM CLAIM; BIOLOGICAL IDENTIFICATION; DEVELOPMENTAL INTERPRETATION; LIFE / VIABILITY INTERPRETATION; MORPHOLOGY / CELL-FATE INTERPRETATION; GENETIC / DNA INTERPRETATION; COGNITIVE / INTELLIGENCE FORWARD INTERPRETATION; MODEL-ONLY / TOY INTERPRETATION; SIMULATION DIAGNOSTIC; NO BIOLOGICAL ROLE CLAIMED; BIOLOGICAL ROLE UNRESOLVED.

primary roleは主表1行に1つ。secondaryは補助roleを最大1つ記録し、—は追加なし。
biological列も集計用の代表roleを1つ選び、併存する解釈は§3–14で分離する。
BIOLOGICAL MECHANISM CLAIMという分類はsourceのmechanism文法を表すだけで、成立判定ではない。
OBSERVABLE / DIAGNOSTICのobservableは数学的出力量を含み、生物学的測定を保証しない。

riskはrole間の読解上の移行を示す。
LOW = local operationが明示され解釈と区別しやすい。
MEDIUM = formal/model操作にbiological label・解釈が併記される。
HIGH = 同じ説明がmodel操作からlife/observed morphology等へ移る、または複数edgeを一体化する。
UNRESOLVED = 版差の意図が未固定で移行の読みを一意に決めない。
riskは誤りの確率、evidence level、claim downgradeの候補ではない。

### Source locators

| ID | Current source |
|---|---|
| S02 | [JA manuscript](../../bio-ifgt/main_ja.tex) |
| S03–05 | [abstract](../../bio-ifgt/sections/abstract.tex)、[introduction](../../bio-ifgt/sections/introduction.tex)、[intuitive picture](../../bio-ifgt/sections/intuitive_picture.tex) |
| S06–07 | [formal mapping](../../bio-ifgt/sections/formal_mapping.tex)、[core equations](../../bio-ifgt/sections/core_equations.tex) |
| S08–09 | [gene information flow](../../bio-ifgt/sections/gene_information_flow.tex)、[development](../../bio-ifgt/sections/development_morphogenesis.tex) |
| S10–12 | [life attractor](../../bio-ifgt/sections/life_attractor.tex)、[probability](../../bio-ifgt/sections/probability_revision.tex)、[second attractor](../../bio-ifgt/sections/intelligence_second_attractor.tex) |
| S13–15 | [note relation](../../bio-ifgt/sections/relation_to_note.tex)、[toy model](../../bio-ifgt/sections/minimal_developmental_simulation.tex)、[results/captions](../../bio-ifgt/sections/simulation_results_visualization.tex) |
| S16–18 | [discussion](../../bio-ifgt/sections/discussion.tex)、[conclusion](../../bio-ifgt/sections/conclusion.tex)、[Bio README](../../bio-ifgt/README.md) |
| S19–20 | [JA working](../../bio-ifgt/sections_ja/)、[handoff](../../bio-ifgt/notes/handoff.md) |
| S21–22 | [code](../../bio-ifgt/simulations/minimal_neural_field/simulate.py)、[simulation README](../../bio-ifgt/simulations/minimal_neural_field/README.md) |

## 2. BIO-EQ-01–48 role table

ExpressionはPhase 01から保持した転記/同じcode要約であり、新しい式ではない。
Source wording欄は出典と自己記述の要約。完全なsignature/版差はPhase 01 §2/7/13に従う。
31のROLE UNRESOLVEDは「単一数学roleなし」、23は「descriptive analogyに固有の数学roleを固定しない」の意味。

| BIO-EQ ID | Expression | Mathematical primary role | Secondary role | Domain | Biological role | Source wording | Role conflation risk |
|---|---|---|---|---|---|---|---|
| BIO-EQ-01 | \(\mathbf r\in\mathbb R^3,\ t\in\mathbb R\) | STATE / DOMAIN DECLARATION | — | r∈R3、t∈R; biological continuum | BIOLOGICAL STATE DESCRIPTION | S06:7; S02 Formal Mapping: State Description | LOW |
| BIO-EQ-02 | \(I(\mathbf r,t)\) | STATE / DOMAIN DECLARATION | DEFINITION | 空間・外部t→local scalar density; function space未指定 | BIOLOGICAL STATE DESCRIPTION | S06:12–14; S07:8–10; S09; S19: Information Density | HIGH |
| BIO-EQ-03 | \(\mathbf J(\mathbf r,t)\) | STATE / DOMAIN DECLARATION | DEFINITION | 空間・t→direction/rate vector; workingはplain J | BIOLOGICAL PROCESS DESCRIPTION | S06:20–22; S07:12–14; S19 plain J: Information Flow | HIGH |
| BIO-EQ-04 | \(\Phi=\Phi[I]\) | CONSTITUTIVE RELATION | PHENOMENOLOGICAL / EFFECTIVE RELATION | I field→potential functional; kernel/codomain未指定 | BIOLOGICAL PROCESS DESCRIPTION | S06:28–30; S07:43–46; S08/09; S19: induced effective potential、具体形未指定 | MEDIUM |
| BIO-EQ-05 | \(\mathbf F=-\nabla\Phi\) | DEFINITION | ALGEBRAIC CONSTRUCTION | continuum scalar potential→direction field | BIOLOGICAL PROCESS DESCRIPTION | S06:33–35; S07:38–41; S08/09; S19 plain F: gradient-driven bias | MEDIUM |
| BIO-EQ-06 | \(\mathbf J=-D\nabla I+\mu\mathbf F\) | CONSTITUTIVE RELATION | PHENOMENOLOGICAL / EFFECTIVE RELATION | continuum fields; D/mu coefficients | BIOLOGICAL PROCESS DESCRIPTION | S06:40–43; S07:29–33; S19: diffusive + induced components | MEDIUM |
| BIO-EQ-07 | \(d\tau/dt=\rho(I,\mathbf J)\) | DEFINITION | — | fields→progression scalar; internal tauをtに対して記述 | BIOLOGICAL PROCESS DESCRIPTION | S06:48–51; S07:62–65; S19: interpretive internal time | MEDIUM |
| BIO-EQ-08 | \(\partial_t I+\nabla\cdot\mathbf J=\sigma\) | BALANCE / CONTINUITY RELATION | — | continuum balanceのsource-local quantities | BIOLOGICAL PROCESS DESCRIPTION | S07:20–24,74–79; S08:30–33; S19: continuity equation | HIGH |
| BIO-EQ-09 | \(\Phi\sim-I\) | PHENOMENOLOGICAL / EFFECTIVE RELATION | CONSTITUTIVE RELATION | potentialのsign conventionの一例 | MODEL-ONLY / TOY INTERPRETATION | S07:50–51; S14:110; S19 core:95: example sign convention | LOW |
| BIO-EQ-10 | \(s\in\{A,T,G,C\}^{N}\) | STATE / DOMAIN DECLARATION | — | 有限nucleotide alphabetの長さN sequence | GENETIC / DNA INTERPRETATION | S08:8–10; S02/S19: sequence representation | LOW |
| BIO-EQ-11 | \(\theta=\theta(s)\) | CONSTITUTIVE RELATION | — | sequence→parameter set; concrete map未表示 | GENETIC / DNA INTERPRETATION | S08:14–17; S02:238: parameter set | HIGH |
| BIO-EQ-12 | \(I(\mathbf r,t)\mapsto I(\mathbf r,t)+\Delta I\) | UPDATE / EVOLUTION RULE | — | fieldのlocal event operation; Delta I具体形未指定 | GENETIC / DNA INTERPRETATION | S08:22–25; S02:246: local state change | HIGH |
| BIO-EQ-13 | \(F_k(I,\mathbf J,\mathbf r,t;\theta)>\theta_k\) | THRESHOLD / SWITCHING RULE | CONSTRAINT | response function→threshold comparison; total type未指定 | GENETIC / DNA INTERPRETATION | S08:50–53; S02:273: threshold condition | MEDIUM |
| BIO-EQ-14 | \(\partial_t I=D\nabla^2I-\lambda I+\sigma(\mathbf r,t;\theta)\) | UPDATE / EVOLUTION RULE | PHENOMENOLOGICAL / EFFECTIVE RELATION | continuum field; parameter-dependent source | DEVELOPMENTAL INTERPRETATION | S09:22–28; S02:313: standard reaction–diffusion form | HIGH |
| BIO-EQ-15 | \(I(\mathbf r)<\theta_1\Rightarrow A;\ \theta_1\le I(\mathbf r)<\theta_2\Rightarrow B;\ I(\mathbf r)\ge\theta_2\Rightarrow C\) | THRESHOLD / SWITCHING RULE | — | scalar threshold regions→state labels | BIOLOGICAL IDENTIFICATION | S09:45–53; S02:334; S19矢印はright-arrow: threshold response | HIGH |
| BIO-EQ-16 | \(x(t)=(x_1(t),\ldots,x_n(t))\) | STATE / DOMAIN DECLARATION | — | n-component biological/environmental state; state space | BIOLOGICAL STATE DESCRIPTION | S10:8–11; S02/S19: state vector | LOW |
| BIO-EQ-17 | \(dx/dt=F(x;\theta)\) | UPDATE / EVOLUTION RULE | — | state→state velocity; vector dimensionはxによる | BIOLOGICAL PROCESS DESCRIPTION | S10:14–17; S02/S19: system evolution | MEDIUM |
| BIO-EQ-18 | \(d\tau/dt=\rho(x)\) | DEFINITION | — | state x→progression scalar; rho具体形なし | LIFE / VIABILITY INTERPRETATION | S10:22–25; S02/S19: internal time | MEDIUM |
| BIO-EQ-19 | \(\Omega_{\mathrm{life}}\subset\Omega\) | STATE / DOMAIN DECLARATION | CONSTRAINT | state space内region; membership条件数式未指定 | LIFE / VIABILITY INTERPRETATION | S10:34–39; S11:20–23; S02/S19: life attractor / region-entry target | HIGH |
| BIO-EQ-20 | \(\Omega_{\mathrm{intel}}\subset\Omega_{\mathrm{life}}\) | CONSTRAINT | STATE / DOMAIN DECLARATION | state-region inclusion; additional constraints | COGNITIVE / INTELLIGENCE FORWARD INTERPRETATION | S12:18–21; S02/S19: additional-constraint subset | HIGH |
| BIO-EQ-21 | \(P_{\mathrm{intel}}\approx P_{\mathrm{life}}P_{\mathrm{second}\mid\mathrm{life}}\) | SCHEMATIC FACTORIZATION | — | schematic conditional probability; event measure未指定 | COGNITIVE / INTELLIGENCE FORWARD INTERPRETATION | S12:26–29; S02:450: schematic factorization、not numerical estimate | MEDIUM |
| BIO-EQ-22 | bias/constraint \(\mapsto I\); state update \(\mapsto\mathbf J\); asymmetry in update \(\mapsto\Phi\) | DEFINITION | — | description→formal labels; typed map未表示 | BIOLOGICAL STATE DESCRIPTION | S06:56–60; S19 summary prose: correspondence to formal quantities | MEDIUM |
| BIO-EQ-23 | \(I\leftrightarrow\) local bias; \(\mathbf J\leftrightarrow\) flow; \(\Phi\leftrightarrow\) return tendency; attractor \(\leftrightarrow\) preserving form | ROLE UNRESOLVED | — | L3/L1 descriptions; direct translationでないと記載 | DEVELOPMENTAL INTERPRETATION | S13:14–20; S19 relation note: not direct translations | MEDIUM |
| BIO-EQ-24 | \(\partial_t M=D_M\nabla^2M-\lambda_M M+\sigma_M(x,y)\) | UPDATE / EVOLUTION RULE | — | 2D toy scalar fields; PDE form | MODEL-ONLY / TOY INTERPRETATION | S14:26–30; S02:482: diffusion/decay/local production | MEDIUM |
| BIO-EQ-25 | \(\partial_t I=D_I\nabla^2I-\lambda_I I+\alpha M\) | UPDATE / EVOLUTION RULE | — | 2D toy scalar fields; PDE form | MODEL-ONLY / TOY INTERPRETATION | S14:34–38; S02:486: diffusion/decay/accumulation | MEDIUM |
| BIO-EQ-26 | \(N_{t+1}=N_t+\eta_N S(I-\theta_N)(1-N_t)\) | UPDATE / EVOLUTION RULE | THRESHOLD / SWITCHING RULE | 2D field discrete step; threshold function S | MODEL-ONLY / TOY INTERPRETATION | S14:42–46; S02:490: threshold update | MEDIUM |
| BIO-EQ-27 | \(G=\lvert\nabla I\rvert\) | DEFINITION | OBSERVABLE / DIAGNOSTIC | 2D represented field gradient magnitude | MODEL-ONLY / TOY INTERPRETATION | S14:50–53; S02:496: gradient structure | LOW |
| BIO-EQ-28 | \(B_{t+1}=B_t+\eta_B S(G-\theta_B)(1-B_t)\) | UPDATE / EVOLUTION RULE | THRESHOLD / SWITCHING RULE | 2D field discrete step | MODEL-ONLY / TOY INTERPRETATION | S14:55–59; S02:500: thresholded update | MEDIUM |
| BIO-EQ-29 | \(E_{t+1}=E_t+\eta_E S(N-\theta_{EN})S(B-\theta_{EB})A(x,y)(1-E_t)\) | UPDATE / EVOLUTION RULE | THRESHOLD / SWITCHING RULE | 2D field discrete step+positional gate | MODEL-ONLY / TOY INTERPRETATION | S14:63–68; S02:506: combined threshold/window | MEDIUM |
| BIO-EQ-30 | \(S(z)=1/(1+e^{-kz})\) | DEFINITION | THRESHOLD / SWITCHING RULE | scalar logistic function; k parameter | MODEL-ONLY / TOY INTERPRETATION | S14:70–72; S02:510: thresholding function | LOW |
| BIO-EQ-31 | \(M\to I\to N\to B\to E\) | ROLE UNRESOLVED | — | source summary sequence; not typed signature | DEVELOPMENTAL INTERPRETATION | S14:88–96; S15:93–95; S02:522,613: generation path / successive constraints（source wording） | HIGH |
| BIO-EQ-32 | \(\mathbf J\sim-\nabla\Phi\) | PHENOMENOLOGICAL / EFFECTIVE RELATION | — | toy explanatory flow relation; continuum notation | DEVELOPMENTAL INTERPRETATION | S14:111; S02:533: induces flows toward stable regions（source wording） | HIGH |
| BIO-EQ-33 | \(P_{\mathrm{intel}}\approx P_{\mathrm{life}}\times P_{\mathrm{life}}\) | SCHEMATIC FACTORIZATION | — | working probability expression; numerical measure未指定 | COGNITIVE / INTELLIGENCE FORWARD INTERPRETATION | S19 intelligence:105–112: 数値評価ではないとの説明; BIO-EQ-21と別版のまま記録 | UNRESOLVED |
| BIO-EQ-34 | \(\partial_t I=D\nabla^2 I-\lambda I+\sigma(r,t)\) | UPDATE / EVOLUTION RULE | PHENOMENOLOGICAL / EFFECTIVE RELATION | working continuum source signature thetaなし | DEVELOPMENTAL INTERPRETATION | S19 development:49–50: ダイナミクス | HIGH |
| BIO-EQ-35 | \(F_k(I,J,r,t)>\theta_k\) | THRESHOLD / SWITCHING RULE | CONSTRAINT | working response signature thetaなし | GENETIC / DNA INTERPRETATION | S19 gene:112–118: 閾値としてのif/then | MEDIUM |
| BIO-EQ-36 | `padded[2:,1:-1]+padded[:-2,1:-1]+padded[1:-1,2:]+padded[1:-1,:-2]-4.0*field` | ALGEBRAIC CONSTRUCTION | BOUNDARY / INITIAL CONDITION | finite 2D array→same-shape stencil; edge padding | MODEL-ONLY / TOY INTERPRETATION | S21 laplacian: edge-copy zero-flux Laplacian | LOW |
| BIO-EQ-37 | `1.0/(1.0+np.exp(clipped))`; `clipped=np.clip(-SIGMOID_K*z,-60.0,60.0)` / `-K_EYE*z` | DEFINITION | THRESHOLD / SWITCHING RULE | scalar/NumPy array elementwise; clipped exponent | MODEL-ONLY / TOY INTERPRETATION | S21 sigmoid / eye_sigmoid: stable logistic threshold | LOW |
| BIO-EQ-38 | `SOURCE_STRENGTH*np.exp(-((X-0.5)**2)/(2.0*SOURCE_WIDTH**2))` times `np.exp(-((Y-0.5)**2)/(2.0*Y_WIDTH**2))` | DEFINITION | — | finite grid coordinate arrays0..1→source array | MODEL-ONLY / TOY INTERPRETATION | S21 make_sigma_m central_band: morphogen source | MEDIUM |
| BIO-EQ-39 | `sigma[:,:SIGMA_M_BAND_WIDTH]=SIGMA_M_STRENGTH*vertical_profile[:,None]`; `vertical_profile=np.exp(-(y/0.65)**2)` | DEFINITION | — | left edge array; y=-1..1, band8columns | MODEL-ONLY / TOY INTERPRETATION | S21 make_sigma_m left_edge: source mode | MEDIUM |
| BIO-EQ-40 | `exp(-((Y-.5)**2)/(2*EYE_Y_WIDTH**2))`; edge_pairはcenters .35/.65の和; single_pairは追加 `exp(-((X-.35)**2)/(2*.18**2))` | CONSTRAINT | DEFINITION | finite array positional gates; modes4名/実質3形 | MODEL-ONLY / TOY INTERPRETATION | S21 make_eye_window（np.expの要約転記）: positional window; central_pairはalias | MEDIUM |
| BIO-EQ-41 | `G=np.sqrt(grad_x**2+grad_y**2)`; `G/(float(np.max(G))+1.0e-8)` | ALGEBRAIC CONSTRUCTION | OBSERVABLE / DIAGNOSTIC | np.gradient→magnitude→global-max normalization | MODEL-ONLY / TOY INTERPRETATION | S21 gradient_magnitude: normalized gradient magnitude | MEDIUM |
| BIO-EQ-42 | `M,N,B,E=np.zeros(...)`（各field個別初期化）; `I=PERTURBATION_SCALE*rng.standard_normal((size,size))` | BOUNDARY / INITIAL CONDITION | — | 2D floating arrays; separate initialization | MODEL-ONLY / TOY INTERPRETATION | S21 run_simulation: initialization（code位置; ROLE NOT YET AUDITED） | LOW |
| BIO-EQ-43 | `M += DT*(D_M*laplacian(M)-LAMBDA_M*M+sigma_M)`; `I += DT*(D_I*laplacian(I)-LAMBDA_I*I+ALPHA*M)` | UPDATE / EVOLUTION RULE | — | ordered in-place array update | MODEL-ONLY / TOY INTERPRETATION | S21 run_simulation: explicit finite-difference simulation | LOW |
| BIO-EQ-44 | `N += ETA_N*sigmoid(I-THETA_N)*(1.0-N)`; `B += ETA_B*sigmoid(G_norm-THETA_B)*(1.0-B)`（signal変数展開） | UPDATE / EVOLUTION RULE | THRESHOLD / SWITCHING RULE | ordered elementwise updates+clips | MODEL-ONLY / TOY INTERPRETATION | S21 run_simulation: threshold updates | LOW |
| BIO-EQ-45 | `E += ETA_E*eye_signal*(1.0-E)`; `eye_signal=eye_sigmoid(N-THETA_EN)*eye_sigmoid(B-THETA_EB)*eye_window` | UPDATE / EVOLUTION RULE | THRESHOLD / SWITCHING RULE | newN/newBを使うconditional update | MODEL-ONLY / TOY INTERPRETATION | S21 run_simulation: conditional eye update | LOW |
| BIO-EQ-46 | `np.clip(N,0.0,1.0)`, B/E同様; `range(steps+1)`, last stepではbreak | CONSTRAINT | UPDATE / EVOLUTION RULE | bounds0..1; step=0..steps; record-before-update | MODEL-ONLY / TOY INTERPRETATION | S21 run_simulation: executable constraints（ROLE NOT YET AUDITED） | LOW |
| BIO-EQ-47 | `np.mean(N>0.5)`, B/E同様; means/maxima、E>.5 contour/overlay | OBSERVABLE / DIAGNOSTIC | VISUALIZATION TRANSFORM | arrays→means,maxima,threshold fractions/overlay | SIMULATION DIAGNOSTIC | S21 print_summary / plotting: numerical summary / visualization | LOW |
| BIO-EQ-48 | `(field-minimum)/(maximum-minimum)`; maximum<=minimumならzeros | VISUALIZATION TRANSFORM | — | array→RGB用minmax normalization | SIMULATION DIAGNOSTIC | S21 normalize_for_plot: plot normalization、biological observableではない | LOW |

## 3. Core field roles

| Object / equations | Mathematical role | Biological roles kept separate | Source-local reading |
|---|---|---|---|
| I(r,t), 02 | STATE / DOMAIN DECLARATION + DEFINITION | state description / biological identification | S06「semantic contentではない」local structure/constraint/differentiation/interdependence。S04はobservational window内proxy、S09はmorphogen profilesをIとして表す |
| J(r,t), 03 | STATE / DOMAIN DECLARATION + DEFINITION | process description / gene-event aggregation | S05はseparate substanceでなくnet state-update direction/rate。S06はreaction/diffusion/transport/interactionsの寄与をまとめる |
| J=-D grad I+mu F, 06 | CONSTITUTIVE RELATION + PHENOMENOLOGICAL / EFFECTIVE RELATION | response/transportの記述、モデル内flow構成 | transported substanceの特定ではなくcoarse currentの関係。codeのdirect J integrationはない |
| Phi=Phi[I], 04 | CONSTITUTIVE RELATION + PHENOMENOLOGICAL / EFFECTIVE RELATION | induced bias / restoring tendency | system-dependent functionalを置く。具体kernelを補わず、restoring interpretationと同一視しない |
| F=-grad Phi, 05 | DEFINITION + ALGEBRAIC CONSTRUCTION | direction/response field / differentiation bias | 与えたPhiからdirection fieldを構成。S08はnew fundamental forceでないと明記 |
| Phi~ -I, 09 | PHENOMENOLOGICAL / EFFECTIVE RELATION | example potential / toy interpretation | sign choiceのexampleであり、all observablesのidentityとして読まない |
| balance, 08 | BALANCE / CONTINUITY RELATION | local production/outflow description / gene-event identification | S07 conservation-like transport、S08 gene-event source。sigmaがあるbalanceをunconditional conservationと同一視しない |
| dtau/dt, 07/18 | DEFINITION（accumulation relation） | internal progression / life-process interpretation | S06/S07/S10はinterpretive、S16 operational definitionはscope外。tで運動を記述しtauはその解釈に用いる |

Iの数学的carrierはcoarse scalar field、informationはそのdescription labelとして定義される。
morphogen concentration、gene activity/constraints、retained biasは適用先の説明であり、一つの
測定量としてglobalに統合しない。S16は具体的I/J/Phiの同定をfuture workとする。この所在を記録するだけで、
「observable未指定だからinvalid」とは判定しない。

sigmaのsource roleはbalanceの残差/局所sourceとしての位置と、gene-related eventsという
biological identificationの二層にある。source/sinkのbalance形は個々の反応機構を自動的に与えない。
Jにも実物の輸送への参照があるが、それだけで特定物質の測定fluxと定義されたとはしない。
tauはdefinition relative to tであり、biological clockを生成するupdate lawへ昇格させない。
rho(I,J)とrho(x)のidentityはPhase 01のまま未固定である。

## 4. DNA / threshold roles

| Equations | Mathematical role | Biological role / attached wording | Separation |
|---|---|---|---|
| 10 s in alphabet^N | STATE / DOMAIN DECLARATION | GENETIC / DNA INTERPRETATION | sequence表現であってcompleted morphologyのprogramという意味ではない |
| 11 theta(s) | CONSTITUTIVE RELATION | DNA constrains propensities/thresholds | parameter mapの記述と具体genotype→phenotype mechanismは別。S08/S16はorganism-specific thetaの導出を扱わないと記載 |
| 12 Delta I event | UPDATE / EVOLUTION RULE | transcription/translation/binding/modification | local changeの形式とevent-to-field aggregationを分離 |
| 13/35 Fk threshold | THRESHOLD / SWITCHING RULE + CONSTRAINT | DNA-conditioned reaction switching | switching criterionと実反応のimplementationを分離。workingのtheta省略を直さない |
| 14/34 RD | UPDATE / EVOLUTION RULE + PHENOMENOLOGICAL / EFFECTIVE RELATION | DEVELOPMENTAL INTERPRETATION | source自身がstandard coarse-grained reaction–diffusion componentと記載。morphogenのempirical identityは別 |
| 15 three intervals | THRESHOLD / SWITCHING RULE | MORPHOLOGY / CELL-FATE INTERPRETATION + BIOLOGICAL IDENTIFICATION | interval分類→state labels→observed morphologyを別段とする |

S09:53–61はcontinuous I / discrete observed outcome、stable state as morphology、
robustness from attractorを連続した文章で述べる。このため15はHIGH riskとした。
これはrole移行の所在分類であり、morphogenesisやrobustnessの成立/不成立、claim strengthは判定しない。
S08:69のtheta as historically stabilized quasi-closureもoriginのinterpretationであって、11の
具体写像そのものとは分ける。上流bridgeを補わない。

## 5. Life / attractor roles

| Target | Formal object / mathematical role | Property wording | Biological / forward role |
|---|---|---|---|
| x(t),16 | state-vector declaration | concentration/expression/reaction/environmentの例 | BIOLOGICAL STATE DESCRIPTION |
| dx/dt=F(x;theta),17 | UPDATE / EVOLUTION RULE | DNA-dependent constraintsの下のstate evolution | BIOLOGICAL PROCESS DESCRIPTION、具体maintenance機構と別 |
| rho(x),18 | internal accumulation definition | life regimeでtauが進むという別文章 | LIFE / VIABILITY INTERPRETATION |
| Omega_life subset,19 | STATE / DOMAIN DECLARATION + CONSTRAINT | bounded viable range、moderate perturbation後にreturnする傾向、S10で命名 | model regionの指定 + life identity / viability interpretation |
| sub-attractors | region内のmore specific stable regions、専用equationなし | cell differentiation as transition、plasticity/partial reversibility | MORPHOLOGY / CELL-FATE INTERPRETATION |
| regeneration | return / reconstructionというdynamical property記述 | larger disturbance後のattractor reconstruction | biological phenomenonのinterpretation |
| Omega_intel subset,20 | CONSTRAINT + STATE / DOMAIN DECLARATION | additional constraints/history retention/reference/sharing | COGNITIVE / INTELLIGENCE FORWARD INTERPRETATION |
| probability,21/33 | SCHEMATIC FACTORIZATION | conditional two-stage problem、not numerical estimate | cognitive emergenceの対象設定。working product意図は未固定 |

19は数学記号によるsubset表示に、return-region条件の文章と「life attractor」という命名が付く。
attractor propertyは文章として記述される。具体region membershipやflowの選び方まで表示された、
という意味ではない。ここでは定義・条件・物理生物学的同定のroleを分けるだけで、
existence/stabilityの証明有無や十分性を採点しない。

20のset inclusionと「lifeに支えられるが同一でないsecond attractor」は異なるrole。
working JA §9.2の「内部ではなく、その上」と§9.3のsubsetをどの比喩/数学scopeで読むかは
§13のUNRESOLVEDとして残す。知性理論自体は監査しない。

## 6. Toy-model / simulation roles

31全体に共通の生成roleを与えない。表は既存式・code依存の説明であり、新しいarrow calculusではない。

| Edge | Mathematical relation | Simulation relation | Biological interpretation | Same role? |
|---|---|---|---|---|
| source / diffusion / decay→M | 24 PDE evolution | 38/39 prescribed source + 43 finite update | morphogen fieldのtoy description | PDE / forcing / biological labelは別 |
| M→I | 25 source coupling alpha M + PDE | 43 uses newly updated M | constraint-density accumulation | model couplingとinformation生成解釈は別 |
| I→N | 26 soft thresholded update | 44 sigmoid, no DT, clip | neural-plate-like commitment | threshold update / developmental namingを分離 |
| I→G | 27 gradient magnitude definition / diagnostic | np.gradient then magnitude | spatial variation / boundary candidate | derived quantityとboundary interpretationを分離 |
| G→G_norm | 41 algebraic normalization | max+epsilon normalization, feeds B | normalized model intermediate | raw gradientとnormalized update inputは別 |
| G / G_norm→B | 28 thresholded evolution | 44 updated Iからnormalized input、B clip | boundary stabilization | diagnostic/input/updateのroleが異なる |
| N→B（compact chain上） | 31にはarrow、28はGを入力とする | direct N→B inputなし。executionはN後B | staged hierarchyのreading | single causal edgeとは同一でない。ROLE CONFLICTを§13へ |
| N+B+window→E | 29 combined threshold + positional constraint | 45 new N/B、eye_sigmoid、eye_window | eye-like commitment | model gateと眼の発生機構を分離 |
| A(x,y) / modes→gate | positional constraint | 40 imposed window arrays | coarse developmental positionのinterpretation | imposed condition≠emergent biological boundary |
| M/I/N/B/E→hierarchy | 31 descriptive sequence、単一数学roleなし | finite dependency graph / loop order | developmental stages | simulation dependency≠causal generation chain |
| hierarchy→quasi-closure / sub-attractor | S14:115 analogy / interpretation | quasi-closure scalarを別途計算していない | successive localization / secondary quasi-closure | correspondence≠model update |

S14/S15はtoy / biological-like / not specific processというscopeと、emergence / stable structuresという
語彙を併用する。両方を保存する。S15の「does not demonstrate biological mechanism」はsourceの限定文であり、
今回のevidence verdictではない。

## 7. Boundary / initialization / diagnostic roles

| Construct | Mathematical role | Model use | Biological separation |
|---|---|---|---|
| zero M/N/B/E | BOUNDARY / INITIAL CONDITION | separately initialized arrays | differentiation前のtoy stateという説明と別 |
| small random I | BOUNDARY / INITIAL CONDITION | seed7, perturbation1e-4 | biological/environmental fluctuationとの対応は解釈 |
| square grid | STATE / DOMAIN DECLARATION | default128² | organism boundaryそのものではない |
| edge-copy padding | BOUNDARY / INITIAL CONDITION | outer stencil boundary treatment | membrane mechanismと同一視しない |
| 5-point Laplacian | ALGEBRAIC CONSTRUCTION | diffusion updateのnumerical operator | underlying transportの同定と分離 |
| central/left source | DEFINITION of prescribed forcing profile | M equationの継続source、初期値でもboundary flux条件でもない | local productionのtoy interpretation |
| eye positional windows | CONSTRAINT / DEFINITION | multiplicative gate、several source-local modes | eye formationの実機構と分離 |
| N/B/E clipping | CONSTRAINT | finite array bounds0..1 | stability / viability propertyとは別 |
| exponent clipping | CONSTRAINT | logistic evaluationの数値範囲 | biological response saturationと同じ処理だと断定しない |
| ordered loop / DT | UPDATE / EVOLUTION RULE | M/IにDT、N/B/Eに別rate | biological timeや同時反応と同一視しない |

| Diagnostic / display | Mathematical role | Where / operation | Role boundary |
|---|---|---|---|
| mean | OBSERVABLE / DIAGNOSTIC | S21 print_summary, array reduction | internal model summary |
| max | OBSERVABLE / DIAGNOSTIC | print_summary | model extremum、measurementではない |
| fraction>.5 | OBSERVABLE / DIAGNOSTIC | thresholded count / total pixels | empirical cell/tissue fractionと別 |
| contour | VISUALIZATION TRANSFORM | save_neural_eye_overlay, E=.5 | displayed model threshold |
| white overlay | VISUALIZATION TRANSFORM | save_combined_with_eye, E>.5 mask | image marking、biological observationではない |
| RGB minmax | VISUALIZATION TRANSFORM | normalize_for_plot | per-field display scale、evolutionへ戻さない |
| G_norm | ALGEBRAIC CONSTRUCTION + OBSERVABLE / DIAGNOSTIC | gradient_magnitude→B input | display-only diagnosticではない |
| GIF step label | VISUALIZATION TRANSFORM | render_frame | model stepのt表示、clock/calibrationと別 |

「simulation convenience」はcode用途の分類であり、biological contentが不可能という意味ではない。
imposed grid/windowとS10の「region not externally imposed」は対象が異なる。境界のcircularityはPhase 03まで判定しない。

## 8. Paper/code role comparison

BIO-EQ-24–48を25行として全件照合する。source identity variantsはPhase 01のまま残す。

| BIO-EQ | Paper / working role | Code role | Role distinction |
|---|---|---|---|
| 24 | M PDE evolution | finite update43 | continuous evolution / executable update |
| 25 | I PDE/source coupling | new Mを使う43 | simultaneous signatureを補わない |
| 26 | thresholded N evolution | gate+update+clip44 | smooth gate / state update |
| 27 | raw magnitude definition | normalized intermediate41 | raw diagnostic / normalized input |
| 28 | B evolution using G | G_norm gate44 | parameter inputのcarrier差 |
| 29 | E gated update | two eye_sigmoid + window45 | biological-like label / model gating |
| 30 | one-k logistic definition | two definitions37 | gate roleは共通、slope/clipping別 |
| 31 | developmental sequence / hierarchy | branch dependencies | N→Bとexecution orderを区別 |
| 32 | interpretive J/Phi flow relation | direct implementationなし | code動作の同一式としない |
| 33 | working schematic probability | corresponding computationなし | simulation-derived probabilityでない |
| 34 | working RD evolution | toy M/I系は別instance | same generic form≠same biological model |
| 35 | working threshold criterion | toy sigmoid familyのみ | Fkのconcrete implementationとは未同定 |
| 36 | paper Laplacian symbol | stencil construction + boundary | operator / boundary implementation |
| 37 | S definition | sigmoid/eye_sigmoid definition + gate | scalar formula / numerical gate |
| 38 | paper sigma_M source | central-band forcing definition | input profile、initial conditionとは別 |
| 39 | paper sigma_M source | left-edge forcing definition | source support≠outer-boundary flux |
| 40 | paper A(x,y) | positional constraint | gate≠observed morphology |
| 41 | paper G | normalized gradient construction/input | diagnostic≠display-only |
| 42 | paper initial-state prose | zeros/noise initialization | BOUNDARY / INITIAL CONDITION |
| 43 | 24/25 evolution | ordered explicit finite update | DT / old/new valuesはcode role |
| 44 | 26/28 evolution | N then G_norm/B, clip | UPDATE + THRESHOLD |
| 45 | 29 evolution | enabled E update, new N/B | UPDATE + THRESHOLD / window |
| 46 | paper bounds/schedule未明示 | clipping / loop / frame schedule | CONSTRAINT + UPDATE |
| 47 | S15 observations of numerical run | mean/max/fraction/overlay | SIMULATION DIAGNOSTIC、empirical observationと分離 |
| 48 | combined visualization | minmax RGB transform | VISUALIZATION TRANSFORM |

## 9. Biological-identification role inventory

| Identification ID | Responsible expression | Formal/model side | Biological side stated by source | Role transition |
|---|---|---|---|---|
| BI-01 | 02 | coarse scalar density | morphogen profiles, retained constraint/bias | description→biological quantity naming |
| BI-02 | 03/08/12 | current/source/increment | gene events and aggregate reactions | model operation→process interpretation |
| BI-03 | 04–06 | potential/direction/current | differentiation bias / stable-state attraction | relation→developmental response |
| BI-04 | 11/13/15 | parameters / thresholds / labels | DNA conditions / cell fate | parameterization→genetic/morphology role |
| BI-05 | 15/17 | thresholds + state dynamics | morphology observed in development | mathematical state→observational identification |
| BI-06 | 19 | bounded returning region | life, viable range, maintenance | region naming→life identity |
| BI-07 | 19 and S10 sub-attractor prose | return / reconstruction | differentiation / regeneration | dynamical-property description→biological interpretation |
| BI-08 | 20/21 | subset + factorization | intelligence with retained/reused history | biological→cognitive forward interpretation |
| BI-09 | 24–31 | toy field patterns | neural-plate-like / eye-like | MODEL-ONLY / TOY INTERPRETATION + developmental reading |
| BI-10 | 47/48 | diagnostics / images | S15 calls output “observations” | numerical observationの語。直接biological measurementとは記載しない |

BIはclaim/evidence ledgerではない。同定の妥当性、operational mapの必要十分性、empirical adequacyは未評価。

## 10. Mechanism-language inventory

generates / produces / causes / drives / induces / stabilizes / determines / gives rise /
emerges / converges / returns / regenerates / maintains、および語形変化・日本語対応を検索し、文脈を確認した。
表はsemantic statement family単位で、EN/JA repriseをまとめる。単語のhit数ではない。
「source treats as」はsourceの文法的立場であり、監査者がmechanism成立を認定する分類ではない。

| Mechanism ID | Source / wording (short quote or paraphrase) | Equation / model | Source treats as | Role reading |
|---|---|---|---|---|
| ML-01 | S05:13–15 asymmetries give direction; flow arises from production等 | 02/03 | analogy / interpretation | intuitive state-update picture |
| ML-02 | S05:19–27 returns / preserves form | 17/19 concept | analogy / interpretation | stable-region pictureとorgan patternの接続 |
| ML-03 | S07:48 induce gradient-driven bias | 04/05 | model mechanism | constitutive/definitionからbias descriptionへ |
| ML-04 | S07:50 sign example points toward increasing density | 09/05 | mathematical consequence | 指定したsign example内のdirection説明 |
| ML-05 | S07:57 loop can produce sustained structures | 04–08 | model mechanism | feedback description / stable-structure language |
| ML-06 | S07:69 remain / return; interpreted as attractor | 19 concept | analogy / interpretation | stable-region naming criterion |
| ML-07 | S08:25 gene network generates information flow | 03/12 | biological mechanism | aggregate event processというsource文法 |
| ML-08 | S08:33 source represents gene-related generation | 08 | analogy / interpretation | balance source→biological production |
| ML-09 | S08:45 stable states draw nearby states; not fundamental force | 04/05 | analogy / interpretation | basin/return tendencyの説明 |
| ML-10 | S08:53 threshold induced by DNA parameters | 11/13 | model mechanism | response switching条件のparameterization |
| ML-11 | S08:57 thresholds branch / stable configurations appear / morphology observed | 11–15 | biological mechanism | model sequenceとbiological identificationが接続 |
| ML-12 | S08:69 historically stabilized constraints | 11 | analogy / interpretation | origin reading; concrete origin deriveしないと併記 |
| ML-13 | S09:7–17 asymmetries seed / production creates gradients | 02/14 | biological mechanism | developmental process description |
| ML-14 | S09:41 bias gives directionality | 04/05/14 | model mechanism | response→structure formationの説明 |
| ML-15 | S09:57 dynamics/thresholds stabilize; morphology is convergence result | 14/15 | biological mechanism | state/observed morphologyのrole移行 |
| ML-16 | S09:61 robustness follows / fluctuations absorbed | 17/19 concept | biological mechanism | attractor propertyからrobustnessを説明する文法 |
| ML-17 | S10:37–43 returns / region formed through interactions / organization persists | 17/19 | analogy / interpretation | naming条件とlife-maintenance description |
| ML-18 | S10:47 convergence to life region | 17/19 | analogy / interpretation | developmental interpretation |
| ML-19 | S10:51 transition into sub-attractors | 19 | analogy / interpretation | cell differentiation interpretation |
| ML-20 | S10:55 robustness follows / regeneration as reconstruction | 17/19 | biological mechanism | return性とregeneration interpretationを併記 |
| ML-21 | S11:25–37 states persist / life appears / region entry | 19 | analogy / interpretation | probability targetの再記述、数値でない |
| ML-22 | S12:11–21 history loops stabilize / intelligence appears | 20/21 | analogy / interpretation | second attractorのforward interpretation |
| ML-23 | S14:25–66 diffusion / accumulation / threshold stabilizes | 24–29 | model mechanism | toy ruleに付くdynamical explanation |
| ML-24 | S14:76–103 hierarchical structures emerge | 24–31 | model mechanism | toy emergence / developmental-like labels |
| ML-25 | S14:111 flows toward stable regions | 32 | analogy / interpretation | codeにJ/Phi integrationはない |
| ML-26 | S14:115 drives accumulation / secondary quasi-closure | 31 | analogy / interpretation | update依存→quasi-closure reading |
| ML-27 | S15:15–29 thresholding produces / dynamics determine where | 24–31 | model mechanism | reported numerical run内の形成説明 |
| ML-28 | S15:99–113 structures arise; not biological mechanism | 24–48 | model mechanism | source自身のtoy scopeを保持 |
| ML-29 | S16:19–37 updated / maintained / future identification | 02–20 | analogy / interpretation | scope/limits/future-work文脈 |
| ML-30 | S03/S17 abstract/conclusion、S18/S20 overview/design | 02–31 | analogy / interpretation | development/life/intelligenceのsummary、個別機構の新式なし |
| ML-31 | S13:24 repeated changes form flows / stabilize into form | 22/23 | analogy / interpretation | L1/L3のdescriptive correspondence |
| ML-32 | S22 source modes / v2 hierarchy / eye-like commitment | 24–45 | model mechanism | “not realistic embryogenesis”というlocal scope |

source wordsのcauses等に独立したrelevant instanceがない場合、そのverbのためだけにclaimを作らない。
codeのreturn statement、plot output生成、file namesやsection inputのkeywordはalgorithm/navigationであり
biological mechanismとして数えない。JAの省略・強調差は§13に別記する。
新たなempirical/physical evidenceを探索・追加していない。

## 11. Attractor terminology audit

同じ語のrepriseを下記15 usage familiesにまとめ、続くlocator manifestで検索hit行を全件保持する。
termの意味を一つに統合せず、dynamical propertyの「記述」と証明の評価を分ける。

| Term / entry | Formal object supplied? | Dynamical property stated? | Biological interpretation | Role status |
|---|---|---|---|---|
| AT-01 intuitive stable regions | S05 state-region prose、独立式なし | repeatedly returns / absorbs deviations | recognizable form | intuitive description |
| AT-02 core attractor | S07 region prose | remain / return after perturbation | stable structure | property criterion + naming |
| AT-03 gene stable configurations | 11–15と周辺prose | appear as attractors | cell fate / morphology | model sequence + identification |
| AT-04 morphology as attractor | 14/15 + S09 prose | convergence / robustness | observed morphology | process explanation + biological identity |
| AT-05 life attractor | 19 subset symbol + S10 | bounded viable motion / return after moderate perturbation | life maintenance | declaration + constraint + naming/interpretation |
| AT-06 viable range | S10 §Definition of Life、独立viability formulaなし | nonstatic / no arbitrary divergence / tau progresses | life regime | condition + LIFE / VIABILITY INTERPRETATION |
| AT-07 non-equilibrium life attractor | same19 | continued exchange/update, not equilibrium state | sustained organization | life-process interpretation |
| AT-08 developmental convergence | 17/19 | multiple initial conditions converge | reproducibility / robustness | developmental interpretation |
| AT-09 sub-attractors | nested regionsのprose、独立subset式なし | stable sub-regions / transitions | differentiation/plasticity | condition + morphology interpretation |
| AT-10 regeneration | same-region reconstruction prose | return after displacement/larger disturbance | regeneration | biological process interpretation |
| AT-11 probability target region | 19 reprise in S11 | entering / remaining | life-emergence probability target | domain/event identification |
| AT-12 second attractor | 20/21 | history retention/reuse、additional constraints | intelligence | set relation + cognitive forward interpretation |
| AT-13 note correspondence | 23 | “returning ... preserving form” | intuitive life/form/thinking flow | analogy、direct translationではない |
| AT-14 toy attractor-like configuration | 24–32/arrays + S14/S22 prose | stable configurations / secondary quasi-closure | neural/eye-like toy patterns | model interpretation、life regionと自動同一視しない |
| AT-15 future attractor regions | S16:37 / S19 discussion、future-work対象 | quantify attractor regionsを今後の作業として記載 | concrete biological systemsへのspecialization | research-target mention、現在のregion構成とは別 |

### Locator manifest

対象はBio current manuscript/working/design/model docs/code。PDF/画像の同語はPhase 01のsource対応を参照し、
今回新しい全文distribution auditはしていない。各行はkeywordに一致する行番号の全リストであり、
一行内の複数出現やEN/JA重複を独立conceptとして数えない。main.texのinput filenameはbuild参照である。

| Source | Matching lines | Classification context |
|---|---|---|
| [main.tex](../../bio-ifgt/main.tex) | 21, 46, 48 | build input名（term semanticsなし） |
| [main_ja.tex](../../bio-ifgt/main_ja.tex) | 21, 35, 37, 76, 212, 280, 341, 347, 349, 377, 383, 387, 389, 391, 407, 419, 427, 429, 433, 435, 465, 533, 535, 644 | JA manuscript counterpart; AT families |
| [README.md](../../bio-ifgt/README.md) | 3, 5, 7 | guide/model interpretation |
| [notes/handoff.md](../../bio-ifgt/notes/handoff.md) | 5, 15, 22, 24 | design terminology / summary |
| [simulations/minimal_neural_field/README.md](../../bio-ifgt/simulations/minimal_neural_field/README.md) | 5, 97 | guide/model interpretation |
| [sections/abstract.tex](../../bio-ifgt/sections/abstract.tex) | 3, 5 | EN source; AT families |
| [sections/conclusion.tex](../../bio-ifgt/sections/conclusion.tex) | 3 | EN source; AT families |
| [sections/core_equations.tex](../../bio-ifgt/sections/core_equations.tex) | 69 | EN source; AT families |
| [sections/development_morphogenesis.tex](../../bio-ifgt/sections/development_morphogenesis.tex) | 55, 61, 65 | EN source; AT families |
| [sections/discussion.tex](../../bio-ifgt/sections/discussion.tex) | 37 | EN source; AT families |
| [sections/gene_information_flow.tex](../../bio-ifgt/sections/gene_information_flow.tex) | 57 | EN source; AT families |
| [sections/intelligence_second_attractor.tex](../../bio-ifgt/sections/intelligence_second_attractor.tex) | 1, 3, 7, 9, 13, 29, 33, 41, 45 | EN source; AT families |
| [sections/introduction.tex](../../bio-ifgt/sections/introduction.tex) | 11 | EN source; AT families |
| [sections/intuitive_picture.tex](../../bio-ifgt/sections/intuitive_picture.tex) | 17 | EN source; AT families |
| [sections/life_attractor.tex](../../bio-ifgt/sections/life_attractor.tex) | 1, 29, 31, 37, 43, 47, 49, 51, 55 | EN source; AT families |
| [sections/minimal_developmental_simulation.tex](../../bio-ifgt/sections/minimal_developmental_simulation.tex) | 111, 113, 115 | EN source; AT families |
| [sections/probability_revision.tex](../../bio-ifgt/sections/probability_revision.tex) | 19, 31, 41 | EN source; AT families |
| [sections/relation_to_note.tex](../../bio-ifgt/sections/relation_to_note.tex) | 18, 36 | EN source; AT families |
| [sections_ja/abstract_ja.md](../../bio-ifgt/sections_ja/abstract_ja.md) | 20, 28, 34 | working variant; AT families / §13 |
| [sections_ja/conclusion_ja.md](../../bio-ifgt/sections_ja/conclusion_ja.md) | 15 | working variant; AT families / §13 |
| [sections_ja/core_equations_ja.md](../../bio-ifgt/sections_ja/core_equations_ja.md) | 157 | working variant; AT families / §13 |
| [sections_ja/development_morphogenesis_ja.md](../../bio-ifgt/sections_ja/development_morphogenesis_ja.md) | 123, 149, 163 | working variant; AT families / §13 |
| [sections_ja/discussion_ja.md](../../bio-ifgt/sections_ja/discussion_ja.md) | 136 | working variant; AT families / §13 |
| [sections_ja/gene_information_flow_ja.md](../../bio-ifgt/sections_ja/gene_information_flow_ja.md) | 134 | working variant; AT families / §13 |
| [sections_ja/intelligence_second_attractor_ja.md](../../bio-ifgt/sections_ja/intelligence_second_attractor_ja.md) | 1, 5, 19, 27, 31, 49, 53, 121, 125, 175, 190 | working variant; AT families / §13 |
| [sections_ja/life_attractor_ja.md](../../bio-ifgt/sections_ja/life_attractor_ja.md) | 1, 5, 91, 103, 116, 139, 144, 150, 152, 154, 156, 160, 176, 180, 184 | working variant; AT families / §13 |
| [sections_ja/probability_revision_ja.md](../../bio-ifgt/sections_ja/probability_revision_ja.md) | 67, 170 | working variant; AT families / §13 |
| [sections_ja/relation_to_note_ja.md](../../bio-ifgt/sections_ja/relation_to_note_ja.md) | 43, 115 | working variant; AT families / §13 |

## 12. Information terminology audit

| Information family | Source / expression | Mathematical carrier / role | Descriptive / biological meaning | Separation |
|---|---|---|---|---|
| INF-01 IFGT information | S04 quotation I=f(1-C) | upstream field quantity | IFGT closure-related description | Bio Iとのdirect identityをsourceが否定 |
| INF-02 Bio information density | S06/S07,02 | coarse scalar state variable | local structure/constraint/differentiation/interdependence | semantic message内容ではないと明記 |
| INF-03 retained bias | S04 / S21 docstring | observation-window proxy | retained structural bias | universal IFGT fieldと同一視しない |
| INF-04 morphogen information | S09,02/14 | scalar field / RD description | concentration profileをIで表す | generic constraint / measured concentrationのrolesを分離 |
| INF-05 gene information | S08,10–13 | sequence/parameter/event representation | reaction propensities, transcription等 | semantic instructionsとparameter constraintsを分離 |
| INF-06 information flow | S05–08,03/06/08 | vector current / balance constituent | net state update, reaction/transport aggregate | separate substanceでもcode独立fieldでもない |
| INF-07 simulation I | S14/S21/S22,25/43 | finite array update | biological constraint proxyのtoy label | observed biological datum / plot normalizationとは別 |
| INF-08 cognitive information | S12,20/21; Phase 00 downstream references | history/reference/reuseの記述 | second-attractor intelligence interpretation | Bio内部forwardrefに限定。consciousness/CT/inference theoryは監査しない |

information全体に単一semantic definitionを新設しない。I、J、Phiの役割を安定化することと、
gene/cognitive informationのglobal semanticsを解くことは別である。

## 13. Source-version role differences

formula同形でも周辺proseが別roleを与える場合を記録する。ROLE CONFLICTは対応付けるroleが
局所的に競合するという記録で、equation invalid / biological claim falseを意味しない。

| Version ID | Compared sources | Same expression / object? | Role difference | Status |
|---|---|---|---|---|
| VR-01 | S06/S07 / S02 / S19 core | I/J field definitions | description label共通、typography別 | SAME ROLE |
| VR-02 | S06/S08 / S02 / S19 potential | Phi[I], F=-grad Phi | effective/direction/restoringの強調差、fundamental forceとはしない | ROLE WORDING VARIANT |
| VR-03 | S06/S10/S16 / S02 / S19 | dtau/dt | interpretive scopeの説明量が版で異なる | ROLE WORDING VARIANT |
| VR-04 | S08 / S02 / S19 gene | s,theta(s),Delta I | sequence/parameter/local operationのrole共通 | SAME ROLE |
| VR-05 | S08/S09 / S19 gene/development | signature variants13/14 vs35/34 | omitted thetaでもswitch/evolution roleは維持、function identityは未固定 | ROLE WORDING VARIANT |
| VR-06 | S09 / S02 / S19 development | interval labels | cell-fate/morphology interpretation共通 | SAME ROLE |
| VR-07 | S10:51 / S02:391 / S19 life:152–168 | sub-region prose | EN/JA TeXはmay/存在しうる、workingは存在/説明を直述 | BIOLOGICAL INTERPRETATION VARIANT |
| VR-08 | S10:55 / S02 §7 / S19 life §7.8 | life region同式、周辺prose別 | EN/workingにregeneration/robustness説明、JA TeXは独立section省略 | BIOLOGICAL INTERPRETATION VARIANT |
| VR-09 | S12/S02 / S19 intelligence | 21 vs33 | factor intent未固定。schematicという自己記述は共通 | UNRESOLVED |
| VR-10 | S12/S02 / S19 intelligence §9.2–9.3 | same subset20 | working「内部ではなく、その上」とsubsetのdescriptive/mathematical scope未固定 | UNRESOLVED |
| VR-11 | S15:18 / S14:50–59 / S21 | gradient/B | results proseはgradient magnitude “defines a boundary field B”; model/codeはGを入力にBを更新 | ROLE CONFLICT |
| VR-12 | S14/S15 compact31 / S21/S22 | N→B appearance / actual dependency | sequence edgeとI-gradient→B updateのroleを混同すると競合 | ROLE CONFLICT |
| VR-13 | S14 / S21 two sigmoids | one family、parameters別 | threshold-function roleは共通、actual functionは版差 | SAME ROLE |
| VR-14 | S15 / S02 / S21 plotting | numerical observations | diagnostics / visualizationのlocal scope | SAME ROLE |
| VR-15 | S14:111/S02:533 / S21 | interpretive J/Phiとtoy arrays | paperはfield interpretation、codeはdirect J/Phi integrationなし | BIOLOGICAL INTERPRETATION VARIANT |

§13ではsourceを統合しない。VR-11/12は「どの関係を指すか」を後続監査へ渡すrole差であり、
このphaseでsource修正、claim downgrade、bridge constructionを指示していない。

## 14. Role-conflation ledger

| Conflation ID | Expression / claim | Mathematical role | Biological role | Why potentially conflated | Later phase |
|---|---|---|---|---|---|
| CON-01 | I / morphogen / constraint,02 | state / definition | state description + identification | generic Iとconcentration interpretationの移行 | 03 domain / 04 claim / 05 mapping |
| CON-02 | J / gene aggregation,03/08/12 | current / balance / update | process description | transported substance、generic current、gene effectsの兼用 | 03/04/05 |
| CON-03 | Phi/F,04–06 | constitutive / definition | bias / return interpretation | gradient directionとbasin/restoring tendencyの移行 | 03/04 |
| CON-04 | sigma,08/14 | source in balance/evolution | gene-event generation | source位置の指定を反応機構と読む余地 | 04/05 |
| CON-05 | tau,07/18 | accumulation definition | internal/viability interpretation | recorded t、internal progression、biological clockの区別 | 03/04/05 |
| CON-06 | theta(s),11/13 | parameter / threshold relation | DNA interpretation | formal mapの記述とconcrete genetic mechanism | 03/04/05 |
| CON-07 | fate thresholds,15 | switching/classification | morphology / biological identification | model labelsからobserved morphologyへ接続 | 04/05 |
| CON-08 | Omega_life,19 | region declaration / constraint | life / viability identification | bounded return regionとlifeを同段で命名 | 03/04/05 |
| CON-09 | attractor / regeneration | return-property prose | regeneration / robustness | definition条件とbiological explanationの移行 | 04/05 |
| CON-10 | Omega_intel / probability,20/21/33 | set constraint / factorization | cognitive forward interpretation | subset、history conditions、emergence targetの兼用 | 04; downstream監査は別 |
| CON-11 | toy hierarchy,31 | single role unresolved / edge-specific roles | developmental interpretation | PDE、threshold、diagnostic、gate、quasi-closureを単一arrowで表示 | 04/05 |
| CON-12 | G / G_norm / B,27/28/41 | derived quantity / normalized input / evolution | boundary stabilization | magnitudeそのものとBというdynamic stateを混同しうる | 03/05 |
| CON-13 | model output / “observation”,47/48 | diagnostic / visualization | SIMULATION DIAGNOSTIC | word observationの広義化。ただしS15はtoy scopeを明記し直接empirical claimをlocateせず | 05（guard確認、error認定でない） |
| CON-14 | imposed windows / initial state,38–42 | forcing / constraint / initial condition | developmental-like conditions | numerical conditionsとbiological boundary/structureの違い | 03/05 |
| CON-15 | J/Phi toy correspondence,32 | effective relation | developmental / quasi-closure interpretation | direct code flow integrationとinterpretive field relationの取り違え | 03/04/05 |

これらは後続問いの索引であり、revision candidateやevidence-gap verdictではない。
boundary circular、life attractor unjustified、simulation validates biology、emergence overclaimed等の判定は行っていない。

## 15. Phase-02 outcome

集計母集団は主表48行。数学primaryは各1、secondaryは非空欄だけを数える。
biologicalは主表の代表roleで数え、§3–14の複数解釈を再加算しない。
zero countのvocabularyも残し、「見つからないrole」から研究上の結論を導かない。

### Mathematical role counts

| Mathematical role | Primary count | Secondary count |
|---|---|---|
| DEFINITION | 9 | 3 |
| STATE / DOMAIN DECLARATION | 6 | 1 |
| ALGEBRAIC CONSTRUCTION | 2 | 1 |
| CONSTITUTIVE RELATION | 3 | 1 |
| BALANCE / CONTINUITY RELATION | 1 | 0 |
| UPDATE / EVOLUTION RULE | 12 | 1 |
| THRESHOLD / SWITCHING RULE | 3 | 7 |
| CONSTRAINT | 3 | 3 |
| BOUNDARY / INITIAL CONDITION | 1 | 1 |
| PHENOMENOLOGICAL / EFFECTIVE RELATION | 2 | 4 |
| OBSERVABLE / DIAGNOSTIC | 1 | 2 |
| VISUALIZATION TRANSFORM | 1 | 1 |
| SCHEMATIC FACTORIZATION | 2 | 0 |
| ROLE UNRESOLVED | 2 | 0 |

### Biological representative-role counts

| Biological role | Count |
|---|---|
| BIOLOGICAL STATE DESCRIPTION | 4 |
| BIOLOGICAL PROCESS DESCRIPTION | 7 |
| BIOLOGICAL MECHANISM CLAIM | 0 |
| BIOLOGICAL IDENTIFICATION | 1 |
| DEVELOPMENTAL INTERPRETATION | 5 |
| LIFE / VIABILITY INTERPRETATION | 2 |
| MORPHOLOGY / CELL-FATE INTERPRETATION | 0 |
| GENETIC / DNA INTERPRETATION | 5 |
| COGNITIVE / INTELLIGENCE FORWARD INTERPRETATION | 3 |
| MODEL-ONLY / TOY INTERPRETATION | 19 |
| SIMULATION DIAGNOSTIC | 2 |
| NO BIOLOGICAL ROLE CLAIMED | 0 |
| BIOLOGICAL ROLE UNRESOLVED | 0 |

### Role-conflation risk counts

| Risk | Count |
|---|---|
| HIGH | 12 |
| MEDIUM | 20 |
| LOW | 15 |
| UNRESOLVED | 1 |

| Summary unit | Count / result |
|---|---|
| BIO-EQ classified | 48 / 48; 元ID・Expression維持 |
| Mathematical primary / secondary | 48 primary; 25 secondary assignments |
| Biological representative families used | 9 / 13 vocabulary families |
| Mathematical ROLE UNRESOLVED | 2（23 descriptive correspondence / 31 multi-role chain） |
| Risk UNRESOLVED | 1（33 working probability）。上の2件とは別母集団 |
| Mechanism-language entries | 32 statement families; source-role classification only |
| Attractor entries | 15 usage families; locator28files / 113 matching lines（build入力3行を含む） |
| Information-role families | 8 |
| Paper/code role comparisons | 25 / 25（BIO-EQ-24–48） |
| Toy relation / edge entries | 11 |
| Biological-identification entries | 10 |
| Source-version comparisons | 15: SAME ROLE 5; ROLE WORDING VARIANT 3; BIOLOGICAL INTERPRETATION VARIANT 3; ROLE CONFLICT 2; UNRESOLVED 2 |
| Role-conflation ledger | 15 unique IDs |
| Validity / circularity / empirical adequacy / evidence grading | NOT PERFORMED |
| Claim downgrade / source integration / equation rewrite | NOT PERFORMED |
| New equation / notation / theory / bridge | NO |
| Upstream audit reopened | NO |

上流RC-005–010、RC-040、RC-041はOPENのまま。source-local role分類によって上流bridgeやBio biological
mappingが成立したとはしない。Phase 01のprobability/signature/function/carrierの未解決事項も保存する。

Validation: new record / READMEのlocal links 52 / 6件とsource paths、fences、display math、
table columns、48 ID coverageとPhase 01からのExpression一致、primary/secondary/biological/risk counts、
conflation ID uniqueness、git diff --checkはPASS。
作業前1429 filesのSHA-256比較では既存変更は本枝READMEだけ、新規は本recordだけ、削除0。
既存tracked変更96件とuntracked研究枝3件を保持し、source/PDF/code/figures、00/01、上流資料の変更なし。
simulation / compile / web research / commit / pushなし。Phase 03へ進まず停止する。
