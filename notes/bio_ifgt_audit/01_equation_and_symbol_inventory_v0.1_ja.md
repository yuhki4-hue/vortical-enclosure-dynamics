# Bio-IFGT equation / symbol inventory v0.1

## 0. Status

- Bio-IFGT audit: **IN PROGRESS**
- Phase 00 dependency / inheritance: **COMPLETE**
- Phase 01 equation / symbol inventory: **COMPLETE**
- Phase 02 equation role / biological-role audit: **NOT STARTED**
- Upstream VED equation audit / core revision: **CLOSED**
- Inventory / source identity resolution only。式・source・PDF・code・notationは変更していない。

基準は[Phase 00](00_dependency_and_inheritance_record_v0.1_ja.md)と[監査README](README_ja.md)。
上流の[frozen 06](../ved_equation_audit/06_final_audit_record_v1.0_ja.md)と
[closure v1.1](../ved_equation_audit/implementation_final_closure_recheck_v1.1_ja.md)のdispositionsは変更しない。
以下はidentity guardであり、Bioへの評価結論ではない。

\[
\text{source-local definition}\neq\text{cross-layer identity}
\]
\[
\text{formal field dynamics}\neq\text{biological mechanism}
\]
\[
\text{cross-layer correspondence}\neq\text{mechanistic derivation}
\]
\[
\text{simulation witness}\neq\text{empirical validation}
\]
\[
\text{model state variable}\neq\text{biological observable}
\]
\[
\text{VED / IFGT OPEN bridge}\neq\text{Bio-IFGT inherited established result}
\]

source-declared meaningはsourceの自己記述の転記であり、equation roleの最終分類ではない。
wrong / invalid / circular、mechanism、evidence grade、empirical validation、
universality、life attractorの妥当性は判定しない。下流監査も開始しない。

## 1. Authority / source hierarchy

| Authority ID | Source class | Build/current status | Primary for what? | Secondary/working variant? |
|---|---|---|---|---|
| A01 | [EN main](../../bio-ifgt/main.tex) + sections | 15 sectionsをinputするmanuscript | EN本文・式・macro展開 | JAより常に優先するとは宣言しない |
| A02 | [JA main](../../bio-ifgt/main_ja.tex) | self-contained TeX、working MDをinputしない | JA配布原稿の式・本文 | ENとの差は別途記録 |
| A03 | [JA working Markdown](../../bio-ifgt/sections_ja/) | 13 files、A01/A02の直接build inputでない | working版の表現 | manuscriptに自動統合しない |
| A04 | [simulate.py](../../bio-ifgt/simulations/minimal_neural_field/simulate.py) | v2_hierarchical executable、今回は実行なし | 実際の配列・定数・更新順・plot処理 | paper式との対応は候補として比較 |
| A05 | [simulation README](../../bio-ifgt/simulations/minimal_neural_field/README.md) | current runtime説明 | 変数ラベル、mode、branch図 | 実行挙動はA04で確認 |
| A06 | [EN PDF](../../bio-ifgt/main.pdf) / [JA PDF](../../bio-ifgt/main_ja.pdf) | 28 / 21 pages、current distribution | 配布されたglyphの確認 | source authorityでなく派生物、§11はspot-checkのみ |
| A07 | [handoff](../../bio-ifgt/notes/handoff.md) | design / handoff memo、skeleton方針 | 設計時の目的・範囲 | 現行TeXを上書きするauthorityでない |
| A08 | [Bio README](../../bio-ifgt/README.md) | current入口 | source配置・参照先 | working版とTeXの差の意図までは決めない |
| A09 | [consciousness formal mapping](../../consciousness/sections/formal_mapping.tex)、[intelligence II preliminaries](../../intelligence-part2/sections/01_preliminaries_ja.tex)、[inference](../../intelligence-part2/sections/02_inference_operator_ja.tex)、[CT formal mapping](../../conceptual-topography/sections/formal_mapping.tex) | downstream current-facing citation / comparison | 下流が何を同じと呼ぶかの所在 | Bioの定義を逆方向に確定しない |
| A10 | [tracked simulation figures](../../bio-ifgt/simulations/minimal_neural_field/outputs/) | tracked PNG 7件、他のignored旧出力と区別 | 変数名・colorbar・overlay表示 | plot/codeからの派生、empirical measurementへ置換しない |

「配布原稿にどちらが載るか」はA01/A02で解決できるが、「working差がtypo / shorthand /
alternativeのどれか」はbuild関係だけでは解決できない。その範囲は **SOURCE AUTHORITY UNRESOLVED** とする。
A04は数値処理のauthorityであり、連続式との完全同一性のauthorityではない。

以下のS番号はPhase 00のsource IDを維持する。行位置のほかsection/function名をlocatorとする。

| Source ID | Direct source / locator |
|---|---|
| S02 | [JA self-contained manuscript](../../bio-ifgt/main_ja.tex) |
| S04 | [introduction](../../bio-ifgt/sections/introduction.tex) |
| S06 | [formal_mapping](../../bio-ifgt/sections/formal_mapping.tex) |
| S07 | [core_equations](../../bio-ifgt/sections/core_equations.tex) |
| S08 | [gene_information_flow](../../bio-ifgt/sections/gene_information_flow.tex) |
| S09 | [development_morphogenesis](../../bio-ifgt/sections/development_morphogenesis.tex) |
| S10 | [life_attractor](../../bio-ifgt/sections/life_attractor.tex) |
| S11 | [probability_revision](../../bio-ifgt/sections/probability_revision.tex) |
| S12 | [intelligence_second_attractor](../../bio-ifgt/sections/intelligence_second_attractor.tex) |
| S13 | [relation_to_note](../../bio-ifgt/sections/relation_to_note.tex) |
| S14 | [minimal_developmental_simulation](../../bio-ifgt/sections/minimal_developmental_simulation.tex) |
| S15 | [simulation_results_visualization](../../bio-ifgt/sections/simulation_results_visualization.tex) |
| S16 | [discussion](../../bio-ifgt/sections/discussion.tex) |
| S19 | [working core](../../bio-ifgt/sections_ja/core_equations_ja.md)、[gene](../../bio-ifgt/sections_ja/gene_information_flow_ja.md)、[development](../../bio-ifgt/sections_ja/development_morphogenesis_ja.md)、[intelligence](../../bio-ifgt/sections_ja/intelligence_second_attractor_ja.md)ほかA03 |
| S21 | A04、function名は§2/6/12 |
| S22 | A05 |

## 2. Equation inventory

Phase-00 BIO-EQ-01–48を全件sourceと照合した。重複repriseは同一行、working/codeの別項目は
元IDのまま維持する。新しい式の提案ではない。
EN/JA macro \I / \J / \PhiI / \dd はI / bold J / Phi / roman dへ展開して表示する。
exact symbol setは式中の変数・parameter・indexを対象とし、演算子はExpressionに保存する。
signatureの型はsourceの文脈までを記載し、未指定の関数空間/codomainを補わない。

identity statusは行ごとの主比較の状態であり、全source間の同一性を意味しない。
SAME EXPRESSION / SAME ROLE CLAIMEDもsource自身のmeaningの一致に限定する。
code要約行40/42/44はliteral source全体の代替でなく、展開した抜粋である。

| BIO-EQ ID | Expression | Source | Exact symbol set | Domain/signature | Source-declared meaning | Variant elsewhere? | Identity status |
|---|---|---|---|---|---|---|---|
| BIO-EQ-01 | \(\mathbf r\in\mathbb R^3,\ t\in\mathbb R\) | S06:7; S02 Formal Mapping | r,t | r∈R3、t∈R; biological continuum | State Description | EN/JA同domain | SAME EXPRESSION / SAME ROLE CLAIMED |
| BIO-EQ-02 | \(I(\mathbf r,t)\) | S06:12–14; S07:8–10; S09; S19 | I,r,t | 空間・外部t→local scalar density; function space未指定 | Information Density | toy 2D、code array、IFGT非同一 | SAME GLYPH / DIFFERENT SOURCE ROLE |
| BIO-EQ-03 | \(\mathbf J(\mathbf r,t)\) | S06:20–22; S07:12–14; S19 plain J | J,r,t | 空間・t→direction/rate vector; workingはplain J | Information Flow | Jijとは別carrier; code Jなし | SAME GLYPH / DIFFERENT SOURCE ROLE |
| BIO-EQ-04 | \(\Phi=\Phi[I]\) | S06:28–30; S07:43–46; S08/09; S19 | Phi,I | I field→potential functional; kernel/codomain未指定 | induced effective potential、具体形未指定 | EN/JA同形; CTは別具体形 | SAME EXPRESSION / SAME ROLE CLAIMED |
| BIO-EQ-05 | \(\mathbf F=-\nabla\Phi\) | S06:33–35; S07:38–41; S08/09; S19 plain F | F,Phi | continuum scalar potential→direction field | gradient-driven bias | plain F、Fk、F(x;theta)は分離 | SAME GLYPH / DIFFERENT SOURCE ROLE |
| BIO-EQ-06 | \(\mathbf J=-D\nabla I+\mu\mathbf F\) | S06:40–43; S07:29–33; S19 | J,D,I,mu,F | continuum fields; D/mu coefficients | diffusive + induced components | EN/JA同形; code直接J更新なし | SAME EXPRESSION / SAME ROLE CLAIMED |
| BIO-EQ-07 | \(d\tau/dt=\rho(I,\mathbf J)\) | S06:48–51; S07:62–65; S19 | tau,t,rho,I,J | fields→progression scalar; internal tauをtに対して記述 | interpretive internal time | 18はrho(x); field/state map未指定 | VARIANT FORM |
| BIO-EQ-08 | \(\partial_t I+\nabla\cdot\mathbf J=\sigma\) | S07:20–24,74–79; S08:30–33; S19 | I,J,t,sigma | continuum balanceのsource-local quantities | continuity equation | upstreamは別source;34/14は別表示 | SAME GLYPH / DIFFERENT SOURCE ROLE |
| BIO-EQ-09 | \(\Phi\sim-I\) | S07:50–51; S14:110; S19 core:95 | Phi,I | potentialのsign conventionの一例 | example sign convention | kernel固定ではない; toy prose reprise | SAME EXPRESSION / SAME ROLE CLAIMED |
| BIO-EQ-10 | \(s\in\{A,T,G,C\}^{N}\) | S08:8–10; S02/S19 | s,A,T,G,C,N | 有限nucleotide alphabetの長さN sequence | sequence representation | N/G/C/Aに別用途あり | SAME GLYPH / DIFFERENT SOURCE ROLE |
| BIO-EQ-11 | \(\theta=\theta(s)\) | S08:14–17; S02:238 | theta,s | sequence→parameter set; concrete map未表示 | parameter set | codeは手設定theta-like定数 | SAME EXPRESSION / SAME ROLE CLAIMED |
| BIO-EQ-12 | \(I(\mathbf r,t)\mapsto I(\mathbf r,t)+\Delta I\) | S08:22–25; S02:246 | I,r,t,Delta I | fieldのlocal event operation; Delta I具体形未指定 | local state change | EN/JA同形 | SAME EXPRESSION / SAME ROLE CLAIMED |
| BIO-EQ-13 | \(F_k(I,\mathbf J,\mathbf r,t;\theta)>\theta_k\) | S08:50–53; S02:273 | Fk,I,J,r,t,theta,thetak,k | response function→threshold comparison; total type未指定 | threshold condition | 35はtheta引数なし | VARIANT FORM |
| BIO-EQ-14 | \(\partial_t I=D\nabla^2I-\lambda I+\sigma(\mathbf r,t;\theta)\) | S09:22–28; S02:313 | I,t,D,lambda,sigma,r,theta | continuum field; parameter-dependent source | standard reaction–diffusion form | 34はsigma(r,t) | VARIANT FORM |
| BIO-EQ-15 | \(I(\mathbf r)<\theta_1\Rightarrow A;\ \theta_1\le I(\mathbf r)<\theta_2\Rightarrow B;\ I(\mathbf r)\ge\theta_2\Rightarrow C\) | S09:45–53; S02:334; S19矢印はright-arrow | I,r,theta1,theta2,A,B,C | scalar threshold regions→state labels | threshold response | working→とmanuscript⇒; B/Cは他用途あり | VARIANT FORM |
| BIO-EQ-16 | \(x(t)=(x_1(t),\ldots,x_n(t))\) | S10:8–11; S02/S19 | x,t,x1,...,xn,n | n-component biological/environmental state; state space | state vector | toy xは位置、下流xは推論状態 | SAME GLYPH / DIFFERENT SOURCE ROLE |
| BIO-EQ-17 | \(dx/dt=F(x;\theta)\) | S10:14–17; S02/S19 | x,t,F,theta | state→state velocity; vector dimensionはxによる | system evolution | F bias/Fk/下流推論演算子と別signature | SAME GLYPH / DIFFERENT SOURCE ROLE |
| BIO-EQ-18 | \(d\tau/dt=\rho(x)\) | S10:22–25; S02/S19 | tau,t,rho,x | state x→progression scalar; rho具体形なし | internal time | 07のfieldsとxの写像未指定 | VARIANT FORM |
| BIO-EQ-19 | \(\Omega_{\mathrm{life}}\subset\Omega\) | S10:34–39; S11:20–23; S02/S19 | Omega_life,Omega | state space内region; membership条件数式未指定 | life attractor / region-entry target | EN/JA同subset; grid domainとは別 | SAME EXPRESSION / SAME ROLE CLAIMED |
| BIO-EQ-20 | \(\Omega_{\mathrm{intel}}\subset\Omega_{\mathrm{life}}\) | S12:18–21; S02/S19 | Omega_intel,Omega_life | state-region inclusion; additional constraints | additional-constraint subset | EN/JA/working同subset | SAME EXPRESSION / SAME ROLE CLAIMED |
| BIO-EQ-21 | \(P_{\mathrm{intel}}\approx P_{\mathrm{life}}P_{\mathrm{second}\mid\mathrm{life}}\) | S12:26–29; S02:450 | \(P_{\mathrm{intel}},P_{\mathrm{life}},P_{\mathrm{second}\mid\mathrm{life}}\) | schematic conditional probability; event measure未指定 | schematic factorization、not numerical estimate | 33のPlife×Plifeと相違 | VARIANT FORM |
| BIO-EQ-22 | bias/constraint \(\mapsto I\); state update \(\mapsto\mathbf J\); asymmetry in update \(\mapsto\Phi\) | S06:56–60; S19 summary prose | I,J,Phi; bias,state update,asymmetry | description→formal labels; typed map未表示 | correspondence to formal quantities | working prose; source-local correspondence | SAME EXPRESSION / SAME ROLE CLAIMED |
| BIO-EQ-23 | \(I\leftrightarrow\) local bias; \(\mathbf J\leftrightarrow\) flow; \(\Phi\leftrightarrow\) return tendency; attractor \(\leftrightarrow\) preserving form | S13:14–20; S19 relation note | I,J,Phi,attractor; note labels | L3/L1 descriptions; direct translationでないと記載 | not direct translations | working prose; biological observable mapではない | SAME EXPRESSION / SAME ROLE CLAIMED |
| BIO-EQ-24 | \(\partial_t M=D_M\nabla^2M-\lambda_M M+\sigma_M(x,y)\) | S14:26–30; S02:482 | M,t,DM,lambdaM,sigmaM,x,y | 2D toy scalar fields; PDE form | diffusion/decay/local production | 43: finite M update | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-25 | \(\partial_t I=D_I\nabla^2I-\lambda_I I+\alpha M\) | S14:34–38; S02:486 | I,t,DI,lambdaI,alpha,M | 2D toy scalar fields; PDE form | diffusion/decay/accumulation | 43: new Mを使うfinite I update | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-26 | \(N_{t+1}=N_t+\eta_N S(I-\theta_N)(1-N_t)\) | S14:42–46; S02:490 | N,t,etaN,S,I,thetaN | 2D field discrete step; threshold function S | threshold update | 44: DTなし、clip追加 | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-27 | \(G=\lvert\nabla I\rvert\) | S14:50–53; S02:496 | G,I | 2D represented field gradient magnitude | gradient structure | 41: returned quantityはG_norm | VARIANT FORM |
| BIO-EQ-28 | \(B_{t+1}=B_t+\eta_B S(G-\theta_B)(1-B_t)\) | S14:55–59; S02:500 | B,t,etaB,S,G,thetaB | 2D field discrete step | thresholded update | 44: G_norm、DTなし、clip | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-29 | \(E_{t+1}=E_t+\eta_E S(N-\theta_{EN})S(B-\theta_{EB})A(x,y)(1-E_t)\) | S14:63–68; S02:506 | E,t,etaE,S,N,thetaEN,B,thetaEB,A,x,y | 2D field discrete step+positional gate | combined threshold/window | 45: eye_sigmoid/newN,newB/enable_eye | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-30 | \(S(z)=1/(1+e^{-kz})\) | S14:70–72; S02:510 | S,z,k | scalar logistic function; k parameter | thresholding function | 37: slopes8/20、exponent clip | VARIANT FORM |
| BIO-EQ-31 | \(M\to I\to N\to B\to E\) | S14:88–96; S15:93–95; S02:522,613 | M,I,N,B,E | source summary sequence; not typed signature | generation path / successive constraints（source wording） | code/READMEはI gradient→Bの分岐 | VARIANT FORM |
| BIO-EQ-32 | \(\mathbf J\sim-\nabla\Phi\) | S14:111; S02:533 | J,Phi | toy explanatory flow relation; continuum notation | induces flows toward stable regions（source wording） | codeにJ/Phi integrationなし | IDENTITY UNRESOLVED |
| BIO-EQ-33 | \(P_{\mathrm{intel}}\approx P_{\mathrm{life}}\times P_{\mathrm{life}}\) | S19 intelligence:105–112 | Pintel,Plife | working probability expression; numerical measure未指定 | 数値評価ではないとの説明; BIO-EQ-21と別版のまま記録 | 21はconditional factor | WORKING-SOURCE VARIANT |
| BIO-EQ-34 | \(\partial_t I=D\nabla^2 I-\lambda I+\sigma(r,t)\) | S19 development:49–50 | I,t,D,lambda,sigma,r | working continuum source signature thetaなし | ダイナミクス | 14/S02にはthetaあり | WORKING-SOURCE VARIANT |
| BIO-EQ-35 | \(F_k(I,J,r,t)>\theta_k\) | S19 gene:112–118 | Fk,I,J,r,t,thetak,k | working response signature thetaなし | 閾値としてのif/then | 13/S02にはthetaあり | WORKING-SOURCE VARIANT |
| BIO-EQ-36 | `padded[2:,1:-1]+padded[:-2,1:-1]+padded[1:-1,2:]+padded[1:-1,:-2]-4.0*field` | S21 laplacian | field,padded; array slices | finite 2D array→same-shape stencil; edge padding | edge-copy zero-flux Laplacian | paper laplacianにspacing/boundary詳細なし | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-37 | `1.0/(1.0+np.exp(clipped))`; `clipped=np.clip(-SIGMOID_K*z,-60.0,60.0)` / `-K_EYE*z` | S21 sigmoid / eye_sigmoid | z,clipped,SIGMOID_K,K_EYE | scalar/NumPy array elementwise; clipped exponent | stable logistic threshold | 30はone k; runtime8/20 | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-38 | `SOURCE_STRENGTH*np.exp(-((X-0.5)**2)/(2.0*SOURCE_WIDTH**2))` times `np.exp(-((Y-0.5)**2)/(2.0*Y_WIDTH**2))` | S21 make_sigma_m central_band | X,Y,SOURCE_STRENGTH,SOURCE_WIDTH,Y_WIDTH | finite grid coordinate arrays0..1→source array | morphogen source | 39は別source mode | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-39 | `sigma[:,:SIGMA_M_BAND_WIDTH]=SIGMA_M_STRENGTH*vertical_profile[:,None]`; `vertical_profile=np.exp(-(y/0.65)**2)` | S21 make_sigma_m left_edge | sigma,y,vertical_profile,SIGMA_M_BAND_WIDTH,SIGMA_M_STRENGTH | left edge array; y=-1..1, band8columns | source mode | 38はdefault central_band | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-40 | `exp(-((Y-.5)**2)/(2*EYE_Y_WIDTH**2))`; edge_pairはcenters .35/.65の和; single_pairは追加 `exp(-((X-.35)**2)/(2*.18**2))` | S21 make_eye_window（np.expの要約転記） | X,Y,EYE_Y_WIDTH,window,window_1,window_2,x_window | finite array positional gates; modes4名/実質3形 | positional window; central_pairはalias | paper A(x,y)具体形なし | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-41 | `G=np.sqrt(grad_x**2+grad_y**2)`; `G/(float(np.max(G))+1.0e-8)` | S21 gradient_magnitude | field,grad_y,grad_x,G; G_norm at caller | np.gradient→magnitude→global-max normalization | normalized gradient magnitude | 27のGとreturn valueは同一でない | VARIANT FORM |
| BIO-EQ-42 | `M,N,B,E=np.zeros(...)`（各field個別初期化）; `I=PERTURBATION_SCALE*rng.standard_normal((size,size))` | S21 run_simulation | M,I,N,B,E,size,rng,SEED,PERTURBATION_SCALE | 2D floating arrays; separate initialization | initialization（code位置; ROLE NOT YET AUDITED） | paper初期分布の数値詳細なし | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-43 | `M += DT*(D_M*laplacian(M)-LAMBDA_M*M+sigma_M)`; `I += DT*(D_I*laplacian(I)-LAMBDA_I*I+ALPHA*M)` | S21 run_simulation | M,I,DT,D_M,LAMBDA_M,sigma_M,D_I,LAMBDA_I,ALPHA | ordered in-place array update | explicit finite-difference simulation | 24/25の連続表示、newM使用 | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-44 | `N += ETA_N*sigmoid(I-THETA_N)*(1.0-N)`; `B += ETA_B*sigmoid(G_norm-THETA_B)*(1.0-B)`（signal変数展開） | S21 run_simulation | N,B,ETA_N,ETA_B,I,THETA_N,G_norm,THETA_B; neural_signal,boundary_signal | ordered elementwise updates+clips | threshold updates | 26/28のS/Gと実装差 | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-45 | `E += ETA_E*eye_signal*(1.0-E)`; `eye_signal=eye_sigmoid(N-THETA_EN)*eye_sigmoid(B-THETA_EB)*eye_window` | S21 run_simulation | E,ETA_E,eye_signal,N,THETA_EN,B,THETA_EB,eye_window,enable_eye | newN/newBを使うconditional update | conditional eye update | 29のSをeye_sigmoidで具体化 | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-46 | `np.clip(N,0.0,1.0)`, B/E同様; `range(steps+1)`, last stepではbreak | S21 run_simulation | N,B,E,step,steps,frames,GIF_EVERY,enable_gif | bounds0..1; step=0..steps; record-before-update | executable constraints（ROLE NOT YET AUDITED） | paperにexplicit loop/clip指定なし | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-47 | `np.mean(N>0.5)`, B/E同様; means/maxima、E>.5 contour/overlay | S21 print_summary / plotting | M,I,N,B,E; neural_fraction,boundary_fraction,eye_fraction | arrays→means,maxima,threshold fractions/overlay | numerical summary / visualization | model diagnostics; empirical inputなし | CODE IMPLEMENTATION CANDIDATE |
| BIO-EQ-48 | `(field-minimum)/(maximum-minimum)`; maximum<=minimumならzeros | S21 normalize_for_plot | field,minimum,maximum | array→RGB用minmax normalization | plot normalization、biological observableではない | 41のgradient normalizationとは別処理 | SAME GLYPH / DIFFERENT SOURCE ROLE |

## 3. Symbol inventory

各行はsource-local family単位であり、新notationではない。「同じ」は当該source内部に限る。
未固定のcross-layer identityを、同じglyphや英訳で補わない。

| Symbol | Source-local definition | Domain/type | Other uses | Same object? | Conflict / ambiguity |
|---|---|---|---|---|---|
| I | S04/S06 biological structure/constraint density | continuum scalar; toy/codeは2D field/array | IFGT I=f(1-C)、consciousness/CT window I | Bio内対応はclaimed; IFGTと直接非同一を明記 | calibration/field-to-array map未固定 |
| bold J | S06/S07 state-change direction/rate | continuum vector | VED Jij、IFGT flow、J_I/J_log | cross-source非同一 | codeに独立J配列なし |
| plain J | S19 information flow | working notation | manuscript bold J | 同じ説明の版、glyph variant | plain表記からscalarと決めない |
| Phi | S06/S07 Phi[I], specific form unspecified | potential functional / scalar field | CT convolution、consciousness potential | cross-window identity未固定 | codeにPhiなし |
| bold F / plain F | -grad Phi, induced direction field | represented vector; S19 plain | Fk、F(x;theta)、下流F | letterだけで統合しない | typography/signatureを分離 |
| F_k | S08 response function | fields/position/time/parameters→threshold comparison | workingはtheta省略 | signature variant | kは反応index |
| F(x;theta) | S10 state evolution | state→state velocity | intelligence II inference F(x_n) | 同役割/連続性の主張あり、map未表示 | derivativeとdiscrete next-stateを分離 |
| G | S14 magnitude of grad I; S21 local G | continuum / numerical gradient | nucleotide G | continuumとfiniteは対応候補 | returned G_normと別 |
| G_norm | S21 gradient_magnitude(I) return | max-normalized 2D array | paperはGだけ | Gと同一でない | threshold argumentの版差 |
| rho | S06 rho(I,J)、S10 rho(x) progression | unspecified scalar function | VED rhoi / continuum density | cross-source未固定 | Bio内2 signaturesもmap未表示 |
| sigma | S07 local / S08 gene-event source | continuum scalar; S09 sigma(r,t;theta) | VED/IFGT source、sigma_M | source-localに分離 | 具体的gene-event functionなし |
| t | S06/S10 external recording/evolution parameter | real coordinate; toy step subscript | VED/IFGT t | physical clock identity未固定 | code step/DTとのphysical換算なし |
| tau | accumulated internal progression | interpretive scalar | IFGT tau、VED tau_i、cognitive time | 同glyphはtranslationでない | code tau更新なし |
| C | S04引用のIFGT closure quantity | upstream field、Bio dynamical C未導入 | nucleotide C、cell state C、VED Cij | 別用途 | labelsをclosureへ変換しない |
| s | S08 DNA sequence | finite alphabet sequence | code手設定parameters | code sequence inputなし | theta(s)具体実装なし |
| theta | S08 theta(s)、S10 constraints | parameter set | code constants、intelligence theta | same-role claim、value mapなし | DNA→数値定数未固定 |
| theta_k / theta1,theta2 | reaction / cell-fate thresholds | scalar comparisons | theta_N/B/EN/EB | 別threshold families | family間対応未指定 |
| r / x,y / X,Y | spatial coordinates | R3 / 2D / finite mesh | state x | spatial/statespaceを分離 | grid physical scale未指定 |
| x / x_i / n | S10 state vector | n-component biological/environmental state | position x、inference x_n | carrier別 | field projection未固定 |
| Omega | S10 state space | state set | simulation square domain | 同一と記載しない | exact state space未指定 |
| Omega_life | bounded returning region | subset of Omega | downstream quasi-closure regions | source-local naming | operational membershipなし |
| Omega_intel | additional-constraint second attractor | subset of Omega_life | inference domain | transformationなし | probability event対応未形式化 |
| M | S14 morphogen field | 2D field / code array | general I interpretation | code label対応明記 | concentration calibrationなし |
| N | S14 neural commitment | 2D field / clipped array | sequence length N | 別物 | integer lengthとarrayを分離 |
| B | S14 auxiliary boundary stabilization | 2D field / clipped array | cell state B、VED barrier B(L) | 別物 | boundary measure≠membrane identity |
| E | S14 eye-like commitment | 2D field / clipped array | closure energy E(A)、downstream stopping E | 別物 | observed eye/energyへ置換しない |
| S(z) | S14 logistic threshold, one k | scalar function | VED edge strength Sij | 別物 | codeはtwo functions |
| sigmoid / eye_sigmoid | S21 clipped-exponent logistic functions | elementwise scalar/array | paper S | family対応、same parameterでない | slopes8/20 |
| D / D_M / D_I / mu | diffusion/response coefficients | source-local coefficients | code .45/.16; IFGT coefficients | source/subscriptごとに分離 | equality/units/scale未指定 |
| lambda / lambda_M / lambda_I | S09/S14 decay coefficients | source-local coefficients | VED retention lambda | 同一視しない | decay数値はcodeにある |
| alpha | S14 M→I coupling | coefficient; ALPHA=.09 | 他sourceのalpha | source-local | physical calibrationなし |
| eta_N / eta_B / eta_E | commitment update rates | discrete-step parameters | code .030/.020/.020 | labels対応、DTなし | continuous rate換算未指定 |
| sigma_M / code sigma_M | S14 source / S21 mode-dependent array | function(x,y) / array | Bio sigma、local variable sigma | 対応候補; Bio sigma全体と同一でない | source modes別 |
| A(x,y) / eye_window | positional gate | function / array | nucleotide A、cell state A | window対応候補; labelsとは別 | shapeはcode指定 |
| k / SIGMOID_K / K_EYE | logistic steepness | scalar constants | F_k反応index | indexとslopeは別 | one k vs8/20 |
| probability symbols | P_life, P_intel, P_second given life | schematic probability; measure未指定 | S19 repeated P_life | factor版を分離 | 数値/標本空間未指定 |
| DT / step / STEPS | S21 timestep/count | .08; default800updates | paper t | runtime indices | all fieldsにDT適用ではない |
| SEED / noise / masks | SEED7, I noise1e-4, field>.5 | RNG configuration / diagnostics | empirical samplingと別 | biological mapなし | normalizationとstateを分離 |

## 4. Inherited-symbol identity

| Identity family | Upstream identity | Bio identity / located statement | Code / downstream pressure | Inventory result |
|---|---|---|---|---|
| I | IFGT I=f(1-C) | S04/A04/A05 explicitly not direct identity; local proxy | code I; consciousness biological-cognitive I; CT projected I | 非同一注記を保持、mapを補わない |
| J | VED node-indexed Jij; IFGT vector flow | S06/S07 bold J(r,t); S19 plain J | no code J; downstream J_I/J_log window-local | carrier分離、discrete/continuum translationなし |
| Phi / F | IFGT potential/direction vocabulary | Phi[I] unspecified; F=-grad Phi | no code Phi/F; CT convolutionはCTの式 | Bioにkernelを継承しない |
| rho | VED rho_i and continuum density | Bio progression rho(I,J) / rho(x) | code rhoなし | densityとprogressionを分離 |
| sigma | VED source / IFGT decomposition | Bio local/gene source、sigma(r,t;theta) | toy sigma_MはM production | upstream decompositionを補わない |
| t / tau | Vol.1 derivative t/tau_i; IFGT external t/informational tau | Bio external t/internal tau、dtau/dtのみ | code step/DT、downstream時間語彙 | clock map / cross-theory translationなし |
| C / closure | VED causal log vs IFGT closure degree | S04でC引用、Bio dynamical Cなし | nucleotide/state C、toy quasi-closure reading | Cij→Cfield→Bio Iを認定しない |

上流8 bridges RC-005–010 / RC-040 / RC-041は引き続きOPEN。
Phase 00 §7の直接使用/間接関連分類を変更しない。Bio-localな式は上流bridge供給ではない。
rho同glyph比較はRC-007を使用した証拠ではない。上流S、B、Eの用途は
[core equations](../../docs/core_equations.md)のsourceと区別する。
下流はA09のidentity pressureだけを記録し、mechanism/claim監査へ進まない。

## 5. Bio-local symbol collisions

collisionは「区別すべき用法が存在する」の意味で、誤記・不整合の判定ではない。

| Collision ID | Glyph | Meaning A | Meaning B | Same source? | Downstream risk |
|---|---|---|---|---|---|
| COL-01 | I | general Bio density | toy array / IFGT field | Bio内+cross-source | type/calibration同一視 |
| COL-02 | J | continuum vector | VED matrix / working plain J | cross-source/working | scalar/vector/matrix混同 |
| COL-03 | F | direction field | Fk / F(x;theta) | YES | inference operatorも統合 |
| COL-04 | rho | progression | VED log density | cross-source、Bio内2 signatures | clock/densityの同一視 |
| COL-05 | sigma | Bio I source | morphogen source / IFGT / VED | YES+cross-source | 対象場とrateの混同 |
| COL-06 | theta | parameter set | thresholds / downstream set | YES+cross-source | same-role→same-value |
| COL-07 | S | logistic | VED edge strength | cross-source | connectivityとgate混同 |
| COL-08 | D | general diffusion | species / other-source coefficient | YES+cross-source | 数値・単位共有 |
| COL-09 | B | cell state B | boundary field / barrier B(L) | YES+cross-source | label/field/energy混同 |
| COL-10 | E | eye-like commitment | energy / stopping operator | cross-source | physical energyと誤認 |
| COL-11 | x | spatial coordinate | biological / inference state | YES+cross-source | domain取り違え |
| COL-12 | C | nucleotide | cell label / IFGT closure / causal log | YES+cross-source | labelをfieldと読む |
| COL-13 | N | sequence length | neural field | YES | length/array混同 |
| COL-14 | G | nucleotide | gradient magnitude / G_norm | YES | alphabet/raw/normalized混同 |
| COL-15 | A | nucleotide / cell label | positional window | YES | label/spatial gate混同 |
| COL-16 | k | response index | sigmoid steepness | YES | index/parameter混同 |

## 6. Paper/code correspondence

BIO-EQ-24–31を8行で全件照合。S21 run_simulation / helpersとS22が比較先。
continuous式とfinite updateの数学的同値性を判定しない。

| Paper equation | Code implementation | Exact / approximate / variant? | Parameter differences | Update-order differences | Identity status |
|---|---|---|---|---|---|
| 24 M PDE | M += DT*(D_M*laplacian(M)-LAMBDA_M*M+sigma_M) | continuous→finite candidate | .45,.030,DT=.08; 2 source modes | M first; old M stencil | CODE IMPLEMENTATION CANDIDATE |
| 25 I PDE | I += DT*(D_I*laplacian(I)-LAMBDA_I*I+ALPHA*M) | continuous→finite candidate | .16,.020,.09; initial noise | uses new M, old I | CODE IMPLEMENTATION CANDIDATE |
| 26 N step | neural_signal= sigmoid(I-THETA_N); N update then clip | paper structure + implementation details | eta=.030, threshold1.15, slope8; no DT | new I | CODE IMPLEMENTATION CANDIDATE |
| 27 G | np.gradient(I); magnitude; divide by max+1e-8 | raw vs normalized variant | no explicit spacing arg | after I; return named G_norm | VARIANT FORM |
| 28 B step | sigmoid(G_norm-THETA_B); B update then clip | G argument variant | eta=.020, threshold.55, slope8; no DT | after N; depends on new I, not N | CODE IMPLEMENTATION CANDIDATE |
| 29 E step | eye_sigmoid(N-THETA_EN)*eye_sigmoid(B-THETA_EB)*eye_window | gate/finite implementation | eta=.020, thresholds.5/.5, slope20; no DT; switch | new clipped N/B, then E clip | CODE IMPLEMENTATION CANDIDATE |
| 30 S(z) | sigmoid / eye_sigmoid; exponent clip[-60,60] | one k vs two values | 8 / 20 | N/B first function, E second | VARIANT FORM |
| 31 chain | README: M→I→N; I gradient→B; N+B+window→E | sequence vs branching dependency | window input separate | sequential order≠N feeding B | VARIANT FORM |

laplacianはedge-copy paddingの5-point stencil。docstringはzero-fluxと呼ぶ。
np.gradientは別helperで呼ばれ、同じpaddingを直接共有しない。両者にphysical grid-spacing
parameterは渡されない。paperにはboundary/stencil/clipping/具体的update順の表示がない。
これを誤り・精度・stabilityの判定に変換しない。

DTを明示的に掛けるのはM/Iだけ。N/B/Eは別rateでstep更新し0..1へclipする。M/Iには同じclipはない。
range(steps+1)は最後の記録後breakしdefault800updates。GIF frameは更新前に10 stepごと保存。
seed7、I初期noise1e-4、他4fieldsは個別zeros。central_band sourceとeye_windowは別入力。

## 7. Probability/signature variants

| Item | EN / self-contained JA | Working JA Markdown | Build/source resolution | Remaining identity question |
|---|---|---|---|---|
| probability | 21 conditional factor; S12/S02; PDF EN p14 / JA p13 | 33 Plife×Plife; S19 intelligence §9.4 | 配布版はconditional factor; MDはinputでない | typo / shorthand / alternativeの意図は **SOURCE CONFLICT UNRESOLVED** |
| threshold | 13 Fk(I,bold J,bold r,t;theta)>theta_k | 35 Fk(I,J,r,t)>theta_k | manuscripts両方theta argumentあり | omitted thetaの暗黙依存か未確定 |
| source | 14 sigma(bold r,t;theta) | 34 sigma(r,t) | manuscripts両方theta argumentあり | working proseのDNA制約とexact functionの関係未固定 |

S12/S02はconditional factorを数値評価でないと記載する。その自己記述を保存し、確率式の
正当性/生物学的成立確率は評価しない。配布原稿の識別と版差の意図の解決は別である。
source統合・式の修正は行わない。

## 8. Domain inventory

| Expression family | Domain | Source explicit? | Cross-domain reuse? | Identity risk |
|---|---|---|---|---|
| 01–09 fields | R3 spatial + real t | S06 explicit; function spaces未指定 | toy2D/arrays | carrier map仮定 |
| 10–11 DNA | sequence→parameter set | alphabet explicit; concrete mapなし | manually set constants | encoding実装と誤認 |
| 12–14 events | local increment / continuum response | signaturesあり、aggregationなし | discrete→field | 記述をcross-scale mapと読む |
| 15 thresholds | scalar intervals→A/B/C | inequalities explicit | B/C field reuse | label混同 |
| 16–20 state | x(t),Omega,subsets | component例あり、exact setなし | fields/inference | shared coordinates仮定 |
| 21/33 probability | named event probabilities | measure未指定 | factor variant | same sample space仮定 |
| 22–23 correspondence | descriptive layers | prose explicit | intuitive/formal | typed transformationと誤認 |
| 24–32 toy | 2D field; PDE/step混在 | S14 explicit | core3D / arrays | t-step換算仮定 |
| 36/41 operators | size×size finite arrays | default128²; code explicit | continuum operators | spacing/boundary共有 |
| 38–40 source/window | finite mesh, mode-dependent | code explicit | paper sigma_M/A | all modes同一視 |
| 43–46 updates | arrays, ordered loop | code explicit | paper symbolic updates | simultaneousと誤認 |
| 47–48 diagnostics | masks/stats/display | code explicit | observable | plot/state/measurement混同 |

## 9. Units/dimensions

物理単位を式の形から補わない。EXPLICITは明示されたcount等、IMPLIEDは名前/用途から読む範囲、
DIMENSIONLESS / NORMALIZEDは数値的正規化であってbiological calibrationではない。

| Unit ID | Quantity | Status | Located information / absent specification |
|---|---|---|---|
| U01 | I | NOT STATED | density/proxy名、physical unitなし |
| U02 | J | NOT STATED | direction/rate名、flux unitなし |
| U03 | Phi / F | NOT STATED | physical energy/force unitなし |
| U04 | D / mu | NOT STATED | diffusion/responseと命名、unitなし |
| U05 | sigma | NOT STATED | generation rate名、measurement unitなし |
| U06 | rho | NOT STATED | progression rate、unit/具体関数なし |
| U07 | t / tau / step / DT | VERSION-DEPENDENT | continuum parametersとfinite step; DT=.08、秒換算なし |
| U08 | M | NOT STATED | morphogen field、濃度単位なし |
| U09 | D_M / D_I | NOT STATED | .45/.16、physical grid/time calibrationなし |
| U10 | lambda family | NOT STATED | decay; .030/.020、physical time unitなし |
| U11 | theta / thresholds | VERSION-DEPENDENT | paper symbolic; code fixed values; BはG_norm threshold |
| U12 | N / B / E | VERSION-DEPENDENT | paper fields; code0..1 bounds、physical unitなし |
| U13 | G / G_norm | VERSION-DEPENDENT | raw vs max-normalized |
| U14 | source / widths | VERSION-DEPENDENT | code0..1 mesh or y=-1..1、band8columns; physical widthsなし |
| U15 | A(x,y) / eye_window | VERSION-DEPENDENT | paper未指定; code Gaussian gates; edge_pairは和、追加正規化なし |
| U16 | S / sigmoid outputs | IMPLIED | logistic出力をdimensionless gateと読む範囲; zのphysical unitなし |
| U17 | probability factors | IMPLIED | probabilityのsource語彙; measure/calibrationなし |
| U18 | plot normalization / fractions | DIMENSIONLESS / NORMALIZED | minmax RGB / pixel fraction; measurement換算なし |
| U19 | grid size / step count | EXPLICIT | default128² / 800updates |
| U20 | alpha / eta | NOT STATED | .09/.030/.020/.020、physical unitなし; etaにDTなし |

## 10. EN/JA/source-version matrix

### 10.1 Manuscript pair

A01のmacroを展開した式とA02を比較する。exactは数式のglyph/signatureについてであり、
章構成・式番号・文章全体のliteral translationを意味しない。

| Equation family | EN form | JA form | Same? | Difference type |
|---|---|---|---|---|
| field domain / I / J | S06/S07, R3/t/I/bold J | Formal Mapping / Core Equations | YES | exact |
| potential / direction | Phi[I], bold F=-grad Phi | 同式、同sign example | YES | exact |
| flow relation | -D grad I+mu F | 同式 | YES | exact |
| field internal time | rho(I,bold J) | 同signature | YES | exact |
| DNA / gene event | alphabet,theta(s),Delta I | 同式 | YES | exact |
| threshold | Fk(...;theta)>theta_k | thetaを含む同signature | YES | exact |
| development PDE | sigma(r,t;theta) | thetaを含む同signature | YES | exact |
| fate intervals | 3 inequalities, states A/B/C | 同thresholds/labels | YES | exact |
| state/time | x(t),F(x;theta),rho(x) | 同式 | YES | exact |
| life/intelligence regions | Omega_life / Omega_intel subsets | 同subset relations | YES | exact |
| probability | conditional second-given-life factor | 同factor | YES | exact |
| toy | BIO-EQ-24–32, one k, raw G | 同M/I/N/B/E, S, G, chain, explanatory J | YES | exact |
| descriptive correspondences | S06 summary display / S13 descriptive analogies | prose中心の対応説明 | meaning対応、presentation別 | notation-only |

### 10.2 Working Markdown separately

| Equation family | Manuscript form | JA working form | Same? | Difference type |
|---|---|---|---|---|
| vector / position typography | bold J/F/r | plain J/F/r | glyph differs、description対応 | notation-only |
| probability | conditional factor | Plife×Plife | NO; cause未確定 | semantic variant / source conflict unresolved |
| threshold | theta in signature | theta omitted | NO as written | signature variant |
| gene source | sigma(r,t;theta) | sigma(r,t) | NO as written | signature variant |
| cell-fate arrow | Rightarrow | rightarrow | arrow glyph differs | notation-only |
| toy equations | S14/S02 full toy section | 対応するtoy MD fileなし | family absent from13 working files | omitted term（この行はsection単位の欠落） |
| correspondence summary | displayed/prose mapping | prose/list formulations | typography/presentation別 | notation-only |

working probabilityの前後にも「条件付き」「二段階」「数値評価でない」という文章がある。
その文章を根拠に式を自動修正しない。EN/JA本稿間の同形性を、working全体への一致判定に拡張しない。

## 11. Distributed PDF spot-check

A06をpypdfでtext抽出し、既存CoreGraphics rendererで一時PNG化して目視した。
Popplerは利用できなかったためnative rendererを使用。再compile / 配布PDF更新はしていない。
PDFスキルに従い、text抽出だけでなくglyphと周辺表示も確認した。

| PDF / page (1-based) | Checked content | Source counterpart | Spot-check result |
|---|---|---|---|
| EN p6 / JA p6 | core I/J, balance, Phi/F, flow | S07 / S02 §4 | glyph/signature一致 |
| EN p8 / JA p8 | gene event/balance、theta付きFk | S08 / S02 §5 | threshold signature一致 |
| EN p11 / JA p11 | life region; EN x/rho(x)も確認 | S10 / S02 §7 | Omega_life subsetとdefinition label一致 |
| EN p14 / JA p13 | Omega_intel / probability factor | S12 / S02 §9 | conditional factor一致、working productではない |
| EN p16–17 / JA p14 | M/I/N/B/E、raw G、one-k S | S14 / S02 §11 | toy式一致、codeのG_normへ置換されていない |

目視対象はEN6pages + JA5pages = 11pages、2 PDFsのspot-check。
検査対象式にPDF/source mismatchはlocateしなかった。従ってこのspot-checkに
DISTRIBUTION VERSION UNRESOLVEDを付ける根拠は見つけていない。
ただし全ページのprose版一致、reproducible build、artifact freshness全般を確定したものではない。
PDF内日付やtimestampだけを版一致の根拠にしない。

## 12. Simulation provenance

表の「対応」はlabel/実装箇所の所在確認で、empirical mappingの認定ではない。

| Provenance ID | Code variable | Paper counterpart | Exact mapping stated? | Used in plots? | Biological label |
|---|---|---|---|---|---|
| PR-01 | M | morphogen M | label明記、continuous→array map未指定 | individual/colorbar/RGB | morphogen field |
| PR-02 | I | Bio constraint density I | A04/A05でproxy明記、IFGTとは非同一 | individual/colorbar/RGB | constraint-density proxy |
| PR-03 | N | neural commitment N | label明記; discrete details§6 | individual/RGB/overlay | neural-like commitment |
| PR-04 | B | boundary stabilization B | label明記; inputはG_norm | individual/colorbar | boundary/edge stabilization |
| PR-05 | E | eye-like commitment E | label明記; eye window/slope詳細はcode | individual/contour/white overlay | eye-like commitment |
| PR-06 | local G | paper raw G | numerical magnitude対応; spacingなし | direct standalone plotなし | boundary inputの中間量 |
| PR-07 | G_norm | paper B式のG位置 | normalization相違; S22 normalizedと明記 | direct plotなし、Bへ入力 | normalized gradient contribution |
| PR-08 | sigma_M | sigma_M(x,y) | function name対応; 2 modesはcode指定 | sourceそのもののtracked単独plotなし | imposed morphogen source |
| PR-09 | eye_window | A(x,y) | name/用途対応; mode shapesはcode指定 | E gating、独立trackedplotなし | positional window |
| PR-10 | THETA_N/B/EN/EB | corresponding thresholds | label対応; values code指定 | field/contourへ間接反映 | threshold gates |
| PR-11 | D_M/D_I,LAMBDA_M/I,ALPHA | paper diffusion/decay/coupling | label対応、unit mapなし | indirect | DNA-like parameters |
| PR-12 | ETA_N/B/E,DT | update rates / t | labels対応、DTはM/Iだけ | indirect / frame scheduling | model runtime |
| PR-13 | SIGMOID_K/K_EYE | one paper k | two choices; exponent clipping追加 | indirect | response steepness |
| PR-14 | SEED/rng/PERTURBATION_SCALE | initial perturbation | concrete values code、sequence入力でない | initial Iからindirect | initial numerical noise |
| PR-15 | means/maxima | numerical summary | paper observableへのmapなし | stdout; individual plots別 | model statistics |
| PR-16 | neural/boundary/eye_fraction | fractions of array entries>.5 | explicit code threshold; observed tissue ratioでない | stdout; E maskはoverlayにも使用 | thresholded model labels |
| PR-17 | normalize_for_plot/RGB | combined visualization | display minmax rule明記 | YES; N red,I green,M blue | visualization only |
| PR-18 | step/frames/GIF_EVERY | discrete developmental sequence | frame schedule明記、biological time mapなし | GIF/sequence | model step |

| Diagnostic | Recorded category | Source / operation | Observable distinction |
|---|---|---|---|
| M/I/N/B/E arrays | internal model state | run_simulation return | biological labelsは付くがmeasurement arraysとして入力していない |
| N/B/E>.5 masks | thresholded model label | print_summary / overlay | organism/tissue empirical segmentationとのmapなし |
| mean / max / fraction | summary statistic | array reductions | observed biological sampleの集計と同一視しない |
| normalized RGB | plot normalization | normalize_for_plot | raw magnitudeを保存する色表現ではない |
| G_norm | normalized model intermediate | gradient_magnitude | display専用ではなくB updateへ戻る |
| step / GIF frame | runtime index / visualization | frame collection | physical/biological time calibrationなし |

tracked PNG7件を目視した。タイトルはM morphogen、I constraint-density、N neural commitment、
B boundary stabilization、E eye-like commitment、N with E>.5 contour、combined E overlay。
この7件に追加のequation/独立J/Phi variableは表示されない。ignored旧fig番号付き出力を
current tracked版のauthorityへ昇格しない。simulationsは実行せず、画像からパラメータ値を逆算しない。

## 13. Source-conflict ledger

conflictは差の記録名でありcorrectness verdictでない。RESOLVED BY SOURCE AUTHORITYは
「どのartifact/記述を今回の該当用途に読むか」が確定する範囲に限る。

| Conflict ID | Source A | Source B | Difference | Can current source hierarchy resolve it? | Status |
|---|---|---|---|---|---|
| CF-01 | S12/S02 conditional probability | S19 intelligence product | conditional factor vs Plife repetition | printed formは決まるが差の意図は決まらない | UNRESOLVED |
| CF-02 | S08/S02 threshold | S19 gene | theta signature present/absent | 両版を区別できる、function identityは未固定 | VERSIONED VARIANT |
| CF-03 | S09/S02 source | S19 development | sigma(r,t;theta) vs sigma(r,t) | 両版を区別、implicit dependence未固定 | VERSIONED VARIANT |
| CF-04 | S14 raw G | S21 returned G_norm | max normalization added | raw magnitudeとnormalized returnはコード上区別可能 | NOT ACTUALLY SAME OBJECT |
| CF-05 | S14 one-k S | S21 two sigmoid functions | k8/k20 + exponent clip | runtime指定とsymbolic familyを区別 | VERSIONED VARIANT |
| CF-06 | S14 symbolic updates/chain | S21/S22 | sequential new-M/new-N/new-B、DT/clip/branch | current executionは確定、paperとのexact temporal identityは未固定 | VERSIONED VARIANT |
| CF-07 | JA working docs | self-contained JA / EN main | READMEにworkingもあるがbuildは別 | input構造から配布原稿authorityを確定 | RESOLVED BY SOURCE AUTHORITY |
| CF-08 | current PDFs | A01/A02 source | mismatch候補をspot-check | §11の指定式について一致を確認、全体鮮度は主張しない | RESOLVED BY SOURCE AUTHORITY |
| CF-09 | S06/S07 J/Phi | S21 toy arrays | general flow/potential vs indirect toy interpretation | codeに独立J/Phi integrationなし | NOT ACTUALLY SAME OBJECT |
| CF-10 | S06 F / S08 Fk / S10 F | same-letter uses | vector bias / response / state velocity | signature/definitionが別 | NOT ACTUALLY SAME OBJECT |
| CF-11 | S08 theta(s) | S21 constants / A09 theta,F | sequence-derived set vs editable values vs inference constraints | explicit concrete/cross-layer mapをlocateしない | UNRESOLVED |
| CF-12 | S06 rho(I,J) | S10 rho(x) / upstream rho | progression signatures / density用途 | field-state / cross-source mapをlocateしない | UNRESOLVED |
| CF-13 | plot label / diagnostic | S21 plotting + tracked PNG | I label、raw/colorbar vs RGB/maskの候補混同 | code関数とtracked7画像で用途分離可能 | RESOLVED BY SOURCE AUTHORITY |

## 14. Unresolved identity ledger

ここでの未解決は後続監査に必要な入力であり、invalidity / circularity / evidence不足の判定ではない。
source-conflict UNRESOLVEDの件数と、このidentity family件数は異なる集計単位である。

| Open ID | Unresolved identity | Located reason | Later inventory / audit dependency |
|---|---|---|---|
| UI-01 | IFGT I / Bio I / toy I / code array | 非同一注記、具体的carrier/calibration mapなし | source-local role/domainの区別 |
| UI-02 | Bio J / gene aggregation / code flow reading | J fieldは論文、codeでは直接integrateしない | field/finite-model対応 |
| UI-03 | Phi[I]の具体形 / code dynamics | functional unspecified、no Phi array | potential/flow式のrole |
| UI-04 | rho(I,J) / rho(x) / VED rho | signatures・meaning別、explicit mapなし | time/density symbol resolution |
| UI-05 | Bio sigma / sigma_M / VED-IFGT sigma | 対象field/source構成別 | source/projectionの監査 |
| UI-06 | external t / code step / Bio tau / upstream tau | DTとphysical clock/translation未固定 | temporal domainの監査 |
| UI-07 | theta(s) / editable numerical parameters | codeはsequenceを入力しない | DNA-like parameter provenance |
| UI-08 | Fk omitted theta / sigma omitted theta | workingの引数省略意図未固定 | signature variantの扱い |
| UI-09 | conditional probability / repeated Plife | intended typo/shorthand/alternative未固定 | probability/event identity |
| UI-10 | Omega_life / Omega_intel / model labels | exact membership/state representation未指定 | state-space/biological-role監査 |
| UI-11 | symbolic toy updates / concrete finite schedule | normalization/slope/DT/order/boundaryの差 | paper/code equation-role対応 |
| UI-12 | Bio F/theta / cognitive I/Phi / observable labels | 下流にsame-role等の記述、translation/calibration未表示 | 下流に渡すidentity課題、下流監査は未開始 |

## 15. Phase-01 outcome

| Inventory unit | Count / result |
|---|---|
| Phase-00 equation entries verified | 48 / 48、ID維持、欠落0 |
| Equation identity statuses | SAME EXPRESSION / SAME ROLE CLAIMED 10; SAME GLYPH / DIFFERENT SOURCE ROLE 8; VARIANT FORM 10; CODE IMPLEMENTATION CANDIDATE 16; WORKING-SOURCE VARIANT 3; IDENTITY UNRESOLVED 1 |
| Symbol families | 38 rows (§3) |
| Symbol collisions | 16 (§5) |
| Source conflicts | 13 (§13) |
| Resolved by source authority | 3; VERSIONED VARIANT 4; NOT ACTUALLY SAME OBJECT 3; UNRESOLVED 3 |
| Unresolved identity families | 12 (§14; equation-statusの1件とは別集計) |
| Paper/code correspondences | 8 (§6; BIO-EQ-24–31) |
| EN/JA manuscript comparison | 13 families: 12 exact, 1 notation/presentation-only; 比較した式のformula/signature差0 |
| JA working differences | 7 groups: notation/presentation3, signature2, probability semantic1, toy section absence1 |
| PDF spot-check | 2 PDFs / 11 rendered pages; 指定式にmismatch locateせず、全配布監査ではない |
| Simulation provenance | 18 (§12); diagnostic categories6 |
| Units/dimensions | 20: NOT STATED 10, VERSION-DEPENDENT 6, IMPLIED 2, DIMENSIONLESS / NORMALIZED 1, EXPLICIT 1 |
| Equation/source/PDF/code changes | 0 |
| New equations / notation / theory / bridges | 0 |
| Upstream audit reopened | NO |

Phase 02に渡すのは、sourceごとに分離した式・記号・signature・domain・差の一覧である。
Bio equation roleの最終分類、biological mechanism、evidence/empirical validation、
circularity、claim downgradeはまだ行っていない。OPENをclosed/falseにせず、上流dispositionsを保持する。

Validation: new record / audit READMEのlocal links 36 / 5件とsource paths、Markdown fences、
display-math delimiters、table columns、48 equation IDsの一意性・連続性、symbol/ledger/count整合、
git diff --checkはPASS。作業前1428 filesのSHA-256 snapshotとの比較では、既存変更は本枝READMEだけ、
新規は本recordだけ、削除0。既存のtracked変更96件とuntracked research directories3件は今回の変更ではなく保存した。
simulation / TeX build / web research / commit / pushなし。Phase 02へ進まず停止する。
