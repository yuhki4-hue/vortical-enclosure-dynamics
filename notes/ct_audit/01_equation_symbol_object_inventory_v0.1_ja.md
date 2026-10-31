# CT Phase 01 — equation / symbol / object / signature inventory v0.1

## 0. Status

CT audit: IN PROGRESS。Phase00 COMPLETEを保持、Phase01 COMPLETE、Phase02以降NOT STARTED。
実施日: 2026-09-10。CT source revision: NOT STARTED。CT equations revised: NO。

signature classificationはsourceがどこまで記述しているかのinventoryであり、well-typedness・妥当性・証拠十分性・dispositionの判定ではない。新type、domain、unit、mapを付け足さない。

## 1. Authority / scope

最上位: [Phase00](00_dependency_inheritance_and_authority_record_v0.1_ja.md)、[README](README_ja.md)。EN canonicalとJA WORKINGの非対称を変更しない。
Phase00のCT-S00–S12 / CT-OBJ001–032 / CT-GLYPH001–012をそのままlocatorとして使う。

| Source ID | Canonical EN path | JA WORKING counterpart |
| --- | --- | --- |
| CT-S00 | [conceptual-topography/main.tex](../../conceptual-topography/main.tex) | canonical JA entry NOT LOCATED |
| CT-S01 | [conceptual-topography/sections/abstract.tex](../../conceptual-topography/sections/abstract.tex) | JA:24 Abstract (WORKING) |
| CT-S02 | [conceptual-topography/sections/introduction.tex](../../conceptual-topography/sections/introduction.tex) | JA:49 §1 (WORKING) |
| CT-S03 | [conceptual-topography/sections/intuitive_picture.tex](../../conceptual-topography/sections/intuitive_picture.tex) | JA:114 §2 (WORKING) |
| CT-S04 | [conceptual-topography/sections/formal_mapping.tex](../../conceptual-topography/sections/formal_mapping.tex) | JA:159 §3 (WORKING) |
| CT-S05 | [conceptual-topography/sections/core_equations.tex](../../conceptual-topography/sections/core_equations.tex) | JA:208 §4 (WORKING) |
| CT-S06 | [conceptual-topography/sections/structural_interpretation.tex](../../conceptual-topography/sections/structural_interpretation.tex) | JA:288 §5 (WORKING) |
| CT-S07 | [conceptual-topography/sections/dynamics.tex](../../conceptual-topography/sections/dynamics.tex) | JA:339 §6 (WORKING) |
| CT-S08 | [conceptual-topography/sections/multiscale.tex](../../conceptual-topography/sections/multiscale.tex) | JA:386 §7 (WORKING) |
| CT-S09 | [conceptual-topography/sections/pathologies.tex](../../conceptual-topography/sections/pathologies.tex) | JA:434 §8 (WORKING) |
| CT-S10 | [conceptual-topography/sections/relation_to_note.tex](../../conceptual-topography/sections/relation_to_note.tex) | JA:474 §9 (WORKING) |
| CT-S11 | [conceptual-topography/sections/discussion.tex](../../conceptual-topography/sections/discussion.tex) | JA:516 §10 (WORKING) |
| CT-S12 | [conceptual-topography/sections/conclusion.tex](../../conceptual-topography/sections/conclusion.tex) | JA:552 §11 (WORKING) |

JA=[working MD](../../conceptual-topography/conceptual_topography_ja.md)。JA locatorsはこのファイルの1-based行番号。
S01 abstract↔JA24; S02 introduction↔JA49; S03 intuitive↔JA114; S04 formal↔JA159; S05 core↔JA208; S06 structural↔JA288; S07 dynamics↔JA339; S08 multiscale↔JA386; S09 pathologies↔JA434; S10 note↔JA474; S11 discussion↔JA516; S12 conclusion↔JA552。12/12 headings、draft履歴JA580–589はcanonical entryではない。
[bibliography](../../conceptual-topography/refs.bib)、[CT README](../../conceptual-topography/README.md)、[EN distribution](../../conceptual-topography/main.pdf)もread-only照合。


上流照合は[IFGT fundamental](../../Information-Field-Geometry-Theory/sections/fundamental_dynamics.tex)、[IFGT unified](../../Information-Field-Geometry-Theory/sections/unified_equation.tex)、[VED closure](../../paper/vol1/sections/closure.tex)、[Con log loop](../../consciousness/sections/dynamics_log_referencing.tex)、[Con TCA](../../consciousness/sections/torque_converter_attention.tex)、[Intelligence homology JA](../../intelligence-part2/appendices/appendix_b_homology_ja.tex)のsymbol reuseだけ。継承の成立を認定しない。

same glyph ≠ same object、same formula shape ≠ same signature、definition ≠ empirical observable、formal object ≠ semantic quantity ≠ cognitive mechanism、EN canonical ≠ JA working authority、imported notation ≠ typed inheritance established。

重要な文字同定: sourceはC_*（下付きstar）とPhi^*（上付きstar）を使う。要求文のC^*は新たに導入しない。理解式のcalRは領域であり、scalar cost R、path gamma、ds、R<thetaはsourceに未発見。これらを推定式として補わない。Phase00のOBJ018/020の平文略記R/C*はIDを変更せず、ここでraw glyphへ対応づける。

## 2. Canonical EN displayed equations

独立抽出: equation11 + align1 = **12 blocks**。alignを3行に分けたrelation-row occurrencesは**14**、named labelsは**13**。
EQ003は同一row内にflow relationとforce equality chainを含むので、意味上の2句を分ける補助カウントは15。この補助数をPhase00の14 row countと混同しない。
gather/multline/displaymath/eqnarray/alignat/flalign、全starred variants、bracket display、double-dollarも探索しENでの追加検出0。commentsは検出対象から除外、rawは元のsubstringから取得する。

以下の表のRaw欄は直後の同ID verbatim blockを指す。rawは環境・label・改行・空白・句読点も含み、正規化しない。

| EQ | Source | Raw expression | Environment | Label | Family | Imported/local |
| --- | --- | --- | --- | --- | --- | --- |
| CT-EQ-001 | S04:33 | verbatim CT-EQ-001 below | equation | eq:Phi_primary | EQF001 | imported/projected |
| CT-EQ-002 | S05:11 | verbatim CT-EQ-002 below | equation | eq:I_evolution | EQF002 | imported/projected |
| CT-EQ-003 | S05:16 | verbatim CT-EQ-003 below | equation | eq:JI | EQF003/004 | imported/projected |
| CT-EQ-004 | S05:21 | verbatim CT-EQ-004 below | equation | eq:sigma | EQF005 | imported/projected |
| CT-EQ-005 | S05:27 | verbatim CT-EQ-005 below | align | eq:sigma_drive, eq:sigma_dissip, eq:sigma_barrier | EQF006/007/008 | imported/projected |
| CT-EQ-006 | S05:82 | verbatim CT-EQ-006 below | equation | eq:coupling | EQF009 | CT-local |
| CT-EQ-007 | S05:114 | verbatim CT-EQ-007 below | equation | eq:sedimentation | EQF010 | CT-local |
| CT-EQ-008 | S05:129 | verbatim CT-EQ-008 below | equation | eq:concept | EQF011 | CT-local |
| CT-EQ-009 | S05:142 | verbatim CT-EQ-009 below | equation | eq:understanding | EQF012 | CT-local |
| CT-EQ-010 | S05:158 | verbatim CT-EQ-010 below | equation | eq:positivity | EQF013 | inherited positivity |
| CT-EQ-011 | S06:72 | verbatim CT-EQ-011 below | equation | eq:vocabulary | EQF014 | CT-local |
| CT-EQ-012 | S07:37 | verbatim CT-EQ-012 below | equation | none | EQF007 | imported repeat |

### CT-EQ-001 raw

SHA-256: `857ffcf0c7411773e9db33ea703cbab73a79072b276763e557948d8607365e7e`

```tex
\begin{equation}
  \Phi(x,\tau) = (K * I)(x,\tau)
  \label{eq:Phi_primary}
\end{equation}
```

### CT-EQ-002 raw

SHA-256: `d249183f986f5e35e9406786bdf1137416cbfb5b174b4d81c07523de5e06eec3`

```tex
\begin{equation}
  \frac{\partial I}{\partial\tau} + \nabla\cdot\JI = \sigma,
  \label{eq:I_evolution}
\end{equation}
```

### CT-EQ-003 raw

SHA-256: `1dedc97a11ba4d237ac3299baee6c9dcd19f695d24efddc6c1bbea7be64e1276`

```tex
\begin{equation}
  \JI = -D\nabla I + \mu F_I, \qquad F_I = -\nabla\Phi = \alpha\nabla C,
  \label{eq:JI}
\end{equation}
```

### CT-EQ-004 raw

SHA-256: `0f04e764f09b06f2ed219a29a34eae4e3ac18bb3efc7c6e6f802a06a2d3b2e53`

```tex
\begin{equation}
  \sigma = \sigma_{\mathrm{drive}} - \sigma_{\mathrm{dissip}} - \sigma_{\mathrm{barrier}}.
  \label{eq:sigma}
\end{equation}
```

### CT-EQ-005 raw

SHA-256: `bf6a334bd64904e58795ab4daaf82fe0cfeb5ad7838c8e51e867a6b9d75fa64c`

```tex
\begin{align}
  \sigma_{\mathrm{drive}}  &= a\Delta\!\left(1 - \frac{C}{C_*}\right),
  \label{eq:sigma_drive}\\
  \sigma_{\mathrm{dissip}} &= \Gamma C,
  \label{eq:sigma_dissip}\\
  \sigma_{\mathrm{barrier}}&= \frac{\kappa_B}{\Cmax - C}.
  \label{eq:sigma_barrier}
\end{align}
```

### CT-EQ-006 raw

SHA-256: `28bd1c4343eee78af4ebcd478c02fd7ccf6b6962dfa5f829b8d6a8f3b013746f`

```tex
\begin{equation}
  \mathcal{L}_{\mathrm{eff}} = \mathcal{L}_{\mathrm{field}}[I]
  + \mathcal{L}_{\mathrm{token}}[\ell]
  + \lambda \sum_i \ell_i \cdot \nabla\Phi.
  \label{eq:coupling}
\end{equation}
```

### CT-EQ-007 raw

SHA-256: `3e9e75b241a685dd50db448ad1ce1a03f85b910e2696ee205e4e0b65069e215e`

```tex
\begin{equation}
  \Phi(x,\tau) \;\xrightarrow{\;\tau\to\infty\;}\; \Phistar(x).
  \label{eq:sedimentation}
\end{equation}
```

### CT-EQ-008 raw

SHA-256: `f3b585f6dd0661f1b68517fb79c6b847f97a9df85e5f07ba6c0ad8fce13e49a4`

```tex
\begin{equation}
  \nabla\Phi(x) \approx 0, \qquad
  \text{with stability under small perturbations of } \JI.
  \label{eq:concept}
\end{equation}
```

### CT-EQ-009 raw

SHA-256: `f44000544f21a1a030c8d0641b92651bc13b102ef4d632e497c05bfb8d5a83b9`

```tex
\begin{equation}
  \int_{\mathcal{R}} |\nabla\Phi|\,dx < \theta.
  \label{eq:understanding}
\end{equation}
```

### CT-EQ-010 raw

SHA-256: `4afaa12916deaee2a1360a7ff82fc3a9ee4bd29411a4dfe7e48cbb0a93cd3913`

```tex
\begin{equation}
  \boxed{I(x,\tau) > 0 \qquad \forall\,x,\,\tau,}
  \label{eq:positivity}
\end{equation}
```

### CT-EQ-011 raw

SHA-256: `ffd8974f3f20ffb060d8810e3586e29b500201a4b254eb3e36e1ad856bb2c8cc`

```tex
\begin{equation}
  \mathcal{V} = \bigl\{\ell_i \;\big|\; S(\ell_i) > \epsilon \bigr\},
  \label{eq:vocabulary}
\end{equation}
```

### CT-EQ-012 raw

SHA-256: `e65b55a53d047234d67e22937daba9e8ce979ff39ff073a543baed9084300804`

```tex
\begin{equation}
  \sigma_{\mathrm{dissip}} = \Gamma C.
\end{equation}
```

## 3. JA working displayed equations

**14 double-dollar blocks**。canonical扱いしない。raw全blockのENとのbyte EXACT MATCHは0（環境、macro、句読点、空白、翻訳差を含むため）。
candidate pairingは数学shapeの対照でありidentity認定でない。JAEQ006/014はJA内ではraw一致のrepeat。

| JA-EQ | Working locator | Raw expression | Candidate EN | Match class |
| --- | --- | --- | --- | --- |
| CT-JAEQ-001 | JA:171 | verbatim CT-JAEQ-001 below | CT-EQ-001 | notational variant; exact-byte match NO |
| CT-JAEQ-002 | JA:214 | verbatim CT-JAEQ-002 below | CT-EQ-002 | notational variant; exact-byte match NO |
| CT-JAEQ-003 | JA:218 | verbatim CT-JAEQ-003 below | CT-EQ-003 | notational variant; exact-byte match NO |
| CT-JAEQ-004 | JA:222 | verbatim CT-JAEQ-004 below | CT-EQ-004 | notational variant; exact-byte match NO |
| CT-JAEQ-005 | JA:226 | verbatim CT-JAEQ-005 below | CT-EQ-005 row1 | notational variant; exact-byte match NO |
| CT-JAEQ-006 | JA:228 | verbatim CT-JAEQ-006 below | CT-EQ-005 row2 | notational variant; exact-byte match NO |
| CT-JAEQ-007 | JA:230 | verbatim CT-JAEQ-007 below | CT-EQ-005 row3 | notational variant; exact-byte match NO |
| CT-JAEQ-008 | JA:245 | verbatim CT-JAEQ-008 below | CT-EQ-006 | notational variant; exact-byte match NO |
| CT-JAEQ-009 | JA:254 | verbatim CT-JAEQ-009 below | CT-EQ-007 | notational variant; exact-byte match NO |
| CT-JAEQ-010 | JA:263 | verbatim CT-JAEQ-010 below | CT-EQ-008 | text/notation variant |
| CT-JAEQ-011 | JA:269 | verbatim CT-JAEQ-011 below | CT-EQ-009 | notational variant; exact-byte match NO |
| CT-JAEQ-012 | JA:276 | verbatim CT-JAEQ-012 below | CT-EQ-010 | notational variant; exact-byte match NO |
| CT-JAEQ-013 | JA:329 | verbatim CT-JAEQ-013 below | CT-EQ-011 | notational variant; exact-byte match NO |
| CT-JAEQ-014 | JA:363 | verbatim CT-JAEQ-014 below | CT-EQ-012 | notational variant; exact-byte match NO |

### CT-JAEQ-001 raw

SHA-256: `c541cc4d5fd69f7933cf3a711fc6f04c3683e4d39d073b0a932d46db9227179d`

```tex
$$\Phi(x,\tau) = (K \ast I)(x,\tau)$$
```

### CT-JAEQ-002 raw

SHA-256: `41b229857792fc8e25c3a0075ca999a4e9fced2e2e074c595965aea57babfbe7`

```tex
$$\frac{\partial I}{\partial\tau} + \nabla \cdot J_I = \sigma$$
```

### CT-JAEQ-003 raw

SHA-256: `9c495baf74b4114ba75f40277005e74ac1eabbcd3640cb7c8c2cc88a811449ab`

```tex
$$J_I = -D\nabla I + \mu F_I, \qquad F_I = -\nabla\Phi = \alpha\nabla C$$
```

### CT-JAEQ-004 raw

SHA-256: `2e6d92fe10e674c7564d9dbbdafbe013fd2af9b3260e51ad8fbbe595d14b097b`

```tex
$$\sigma = \sigma_{\mathrm{drive}} - \sigma_{\mathrm{dissip}} - \sigma_{\mathrm{barrier}}$$
```

### CT-JAEQ-005 raw

SHA-256: `5c6dd64f5780d54eae7c630410a630760f1ac292d83c30ee2838ba6c9e0ef7d8`

```tex
$$\sigma_{\mathrm{drive}} = a\Delta\!\left(1 - \frac{C}{C_*}\right)$$
```

### CT-JAEQ-006 raw

SHA-256: `60d4b029cf715fd0e6140b99de66aee88fcb91bcb23ff49e5cc6db00f0546b51`

```tex
$$\sigma_{\mathrm{dissip}} = \Gamma C$$
```

### CT-JAEQ-007 raw

SHA-256: `3efeb6f4750320b1ef003dcb020f26476e4d003e36d6f8dce61564a0763dc39a`

```tex
$$\sigma_{\mathrm{barrier}} = \frac{\kappa_B}{C_{\max} - C}$$
```

### CT-JAEQ-008 raw

SHA-256: `779dd2bf4842af59c92835bd2821e2e96e983dfd7e4ee4620966dd4f97de8d00`

```tex
$$\mathcal{L}_{\mathrm{eff}} = \mathcal{L}_{\mathrm{field}}[I] + \mathcal{L}_{\mathrm{token}}[\ell] + \lambda \sum_i \ell_i \cdot \nabla\Phi$$
```

### CT-JAEQ-009 raw

SHA-256: `0308901a514c25288449b581b88957093bd36fa9b15b58fb8ab55df1a2dd474d`

```tex
$$\Phi(x,\tau) \;\xrightarrow{\;\tau\to\infty\;}\; \Phi^*(x)$$
```

### CT-JAEQ-010 raw

SHA-256: `55a89704f03941ac6bee312c34149997588766f4ccdd02dd70d22ac813d37290`

```tex
$$\nabla\Phi(x) \approx 0, \qquad J_I \text{ の小摂動に対して安定}$$
```

### CT-JAEQ-011 raw

SHA-256: `e877a0cffc1ea0ef75168ff583d999e26aa0dc1f9848e3541c0f6cd68e701015`

```tex
$$\int_{\mathcal{R}} \lvert\nabla\Phi\rvert\,dx < \theta$$
```

### CT-JAEQ-012 raw

SHA-256: `611180adc9973e8fc1626e0506e8807366ea075419a125207a2f97525539c184`

```tex
$$\boxed{I(x,\tau) > 0 \qquad \forall\, x,\,\tau}$$
```

### CT-JAEQ-013 raw

SHA-256: `ce633ac82c6ab9258a23426191a667b0c1bf714be8ad2a12a6ff8478fb517b06`

```tex
$$\mathcal{V} = \bigl\{\ell_i \;\big|\; S(\ell_i) > \epsilon \bigr\}$$
```

### CT-JAEQ-014 raw

SHA-256: `60d4b029cf715fd0e6140b99de66aee88fcb91bcb23ff49e5cc6db00f0546b51`

```tex
$$\sigma_{\mathrm{dissip}} = \Gamma C$$
```

## 4. Equation families

| EQF | Name | EN occurrences | JA occurrences | Shape (not raw) | Source role | Imported/local | Signature |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CT-EQF-001 | potential/convolution | 001 | 001 | Phi(x,tau)=(K*I)(x,tau) | primary definition; F0/F2/F3 | projected IFGT / claimed inheritance | PARTIAL |
| CT-EQF-002 | information balance | 002 | 002 | partial_tau I + div J_I = sigma | evolution; F1/F2/F4 | imported template | PARTIAL |
| CT-EQF-003 | information flow | 003 (first relation) | 003 (first relation) | J_I=-D grad I+mu F_I | flow; F1/F2/F4 | imported/projected | PARTIAL |
| CT-EQF-004 | constraint force | 003 (second chain) | 003 (second chain) | F_I=-grad Phi=alpha grad C | force/linear context; F1/F2 | imported/projected | PARTIAL |
| CT-EQF-005 | source decomposition | 004 | 004 | sigma=drive-dissip-barrier | decomposition; F0/F1/F2/F4 | imported; sign convention separate | PARTIAL |
| CT-EQF-006 | drive | 005 row1 | 005 | a Delta (1-C/C_*) | effective input; F1/F2/F4 | projected IFGT | PARTIAL |
| CT-EQF-007 | dissipation | 005 row2;012 repeat | 006;014 repeat | Gamma C | effective decay; F1/F2/F4 | projected IFGT, repeat same family | PARTIAL |
| CT-EQF-008 | barrier | 005 row3 | 007 | kappa_B/(Cmax-C) | effective resistance; F1/F2/F3/F4 | projected IFGT | PARTIAL |
| CT-EQF-009 | token coupling | 006 | 008 | L_eff=L_field[I]+L_token[ell]+lambda sum ell_i dot grad Phi | local coupling; F1/F3/F4/F9 | CT-local expression (no separate source attribution) | UNRESOLVED |
| CT-EQF-010 | sedimentation | 007 | 009 | Phi(x,tau) → Phi*(x), tau→infinity | long-time attractor; F3/F4/F6 | CT-local application | PARTIAL |
| CT-EQF-011 | concept stability | 008 | 010 | grad Phi(x)≈0 + small J_I perturbation stability | definition; F0/F3 | CT-local definition | PARTIAL |
| CT-EQF-012 | understanding | 009 | 011 | integral over calR of abs(grad Phi) dx < theta | definition; F0/F4/F5 | CT-local definition | PARTIAL |
| CT-EQF-013 | positivity | 010 | 012 | I(x,tau)>0 for all x,tau | constraint/proposition context; F2/F3 | VED/IFGT inherited claim | PARTIAL |
| CT-EQF-014 | vocabulary | 011 | 013 | V={ell_i given S(ell_i)>epsilon} | definition; F0/F3 | CT-local definition | PARTIAL |

14 families。flow/forceは同一blockでも別family、dissipation repeatは同じfamilyに対応する。shape欄は検索用の略記に過ぎず、raw authorityは§2/3。
全familyのdomain/unit不足を他のfamilyの定義から自動補完しない。inline-only relationsは次節に独立計上する。

## 5. Inline formal relations

| CT-INLINE | Relation/name (locator shorthand) | Source | Role | F-tags | Signature |
| --- | --- | --- | --- | --- | --- |
| CT-INLINE-001 | I=f(1-C), I(x,tau)=f(1-C(x,tau)), I=f(1-C)>0 | S01:18,S04:14/55,S05:162;JA32/163/278 | projected information relation | F0/F2/F3 | PARTIAL |
| CT-INLINE-002 | Phi=K*I / K ast I | S00:88,S01:18,S04:58,S10:24,S12:24;JA17/32/182/484/561 | EQF001 aliases; macro/space retained | F0/F2/F3 | PARTIAL |
| CT-INLINE-003 | Phi≈-alpha C+Phi0 | S00:89;JA18 | explicitly linear approximation | F2 | PARTIAL |
| CT-INLINE-004 | C<Cmax | S00:93,S05:162–164;JA20/278 | strict bound / boundary prose | F0/F2/F3 | PARTIAL |
| CT-INLINE-005 | C in [0,Cmax) | S04:54;JA180 | range given; not unit declaration | F0/F2/F3 | PARTIAL |
| CT-INLINE-006 | C_*<Cmax | S05:39;JA説明未発見 | EN effective saturation vs ideal boundary | F0/F2 | PARTIAL |
| CT-INLINE-007 | ell_i=Q[I,Phi,C;constraints] / ;dot | S01:21,S04:79;JA33/189 | token extraction; argument variants | F0/F3/F4/F9 | PARTIAL |
| CT-INLINE-008 | Delta→C→I→Phi→JI→Delta | S01:25,S05:107;JA34;FIG003 bare J separately | recursive loop | F1/F2/F4/F8 | PARTIAL |
| CT-INLINE-009 | Phi seddto Phistar / Phi→Phi* | S01:27;JA34 | sedimentation macro vs unlabeled arrow | F3/F4/F6 | PARTIAL |
| CT-INLINE-010 | grad Phi(x)≈0 / grad Phi≈0 | S01:30,S02:75,S03:39,S06:22/23,S10:22,S12:24;JA37/87/297/298/482/561 | concept predicate; x omitted variants | F0/F3 | PARTIAL |
| CT-INLINE-011 | I(x,tau)>0 / I>0 | S01:33,S02:89,S04:26/57,S05:168,S08:83,S12:38;JA41/95/167/181/280/430/567 | positivity repeated | F2/F3 | PARTIAL |
| CT-INLINE-012 | JI=-D grad I+mu F_I | S04:64;JA184 | table flow; EQF003 | F1/F2/F4 | PARTIAL |
| CT-INLINE-013 | sigma=sigma_d-sigma_p-sigma_b | S04:67;JA185 | short suffixes; long-form alias not explicitly fixed | F0/F1/F2/F9 | UNRESOLVED |
| CT-INLINE-014 | grad Phi / -grad Phi / abs(grad Phi) | S03:48/49,S04:61,S06:21/25;JA130/131/183/296/300 | direction vs magnitude; all raw token uses below | F3/F4 | INFERRED |
| CT-INLINE-015 | lambda sum ell_i dot grad Phi | S05:69 caption;FIG002 | coupling short form; not full L expression | F1/F4/F8/F9 | UNRESOLVED |
| CT-INLINE-016 | JA I>0 implies grad Phi≠0 implies J_I≠0（一般に） | JA280;EN S05:168–177 different prose | three math spans joined by prose; no new implication equation | F2/F3 | PARTIAL |
| CT-INLINE-017 | C→Cmax | S07:58;JA374 | limit-like boundary approach, not ordinary state | F2/F3/F6 | PARTIAL |
| CT-INLINE-018 | -min Phi | S06:35;JA307 | depth measured within well | F3/F4 | INFERRED |
| CT-INLINE-019 | {ell_i}, S(ell_i), epsilon | S06:69/76/77;JA326/331 | vocabulary stability objects | F0/F3 | PARTIAL |
| CT-INLINE-020 | -Phi(x,tau); high passability = low Phi | S10:25;JA485 | note correspondence; no new passability variable | F3/F4 | PARTIAL |
| CT-INLINE-021 | integral abs(grad Phi) dx (without domain/threshold) | S10:28;JA488 | sense of understanding correspondence; distinct from EQF012 | F4/F5 | PARTIAL |
| CT-INLINE-022 | JC=-D grad C-mu alpha C grad C | CT README Variable Convention (backtick notation) | supporting README-only closure flow, not TeX display | F2/F7 | PARTIAL |
| CT-INLINE-023 | JI/JC/Cmax/Phistar/seddto macros | S00:47–51;notation declarations outside math mode | literal aliases; no typed cross-theory inheritance | F0 | EXPLICIT |
| CT-INLINE-024 | tau as experiential order; Phi* as attractor; collective Phi | S04:76–86,S05:119–122,S08:59;JA188/190/256/417 | formal names with prose roles, no new equations | F3/F4/F5/F6/F7/F9 | PARTIAL |

24 meaning-bearing families（最後の行はsourceのformal-name/prose role bundle）。display countsに加算しない。
proseで結ばれたJA positivity chainやREADMEのbacktick数学も別行で記録する。F-tagは§23。

### 5.1 Exhaustive inline math token index

EN entry+12 sections / JA workingから表示blockを除外して得たsingle-dollarまたはparenthesized mathの全出現索引。
同じraw文字列だけをまとめる。これにより単独記号、caption/table、関係式の全inline候補を保持し、24意味familyに入らない単独glyphも捨てない。
360 occurrences (202 EN / 158 JA), 84 raw groups.

### Inline raw group 001

Occurrences (18): S00:71, S00:83, S01:8, S01:14, S01:17, S01:42, S02:9, S02:37, S02:39, S02:50, S02:103, S04:8, S04:48, S05:105, S05:168, S06:10, S12:10, S12:65

```tex
$\times$
```

### Inline raw group 002

Occurrences (6): S00:86, S00:94, S02:44, S05:108, JA:15, JA:68

```tex
$C$
```

### Inline raw group 003

Occurrences (18): S00:86, S00:94, S04:16, S04:19, S04:24, S04:24, S04:75, S05:108, S05:176, S07:16, S11:61, JA:15, JA:164, JA:166, JA:166, JA:187, JA:347, JA:548

```tex
$I$
```

### Inline raw group 004

Occurrences (59): S00:86, S00:94, S01:30, S03:55, S03:92, S04:83, S04:86, S04:110, S05:90, S05:108, S05:152, S05:172, S06:26, S06:43, S06:48, S06:53, S07:23, S07:35, S07:71, S08:59, S09:65, S10:21, S10:23, S10:25, S10:26, S10:27, S10:30, S11:34, S11:49, S11:61, JA:15, JA:26, JA:37, JA:135, JA:155, JA:189, JA:190, JA:200, JA:247, JA:272, JA:301, JA:311, JA:313, JA:317, JA:351, JA:361, JA:379, JA:417, JA:467, JA:481, JA:483, JA:484, JA:485, JA:486, JA:487, JA:490, JA:531, JA:541, JA:548

```tex
$\Phi$
```

### Inline raw group 005

Occurrences (14): S00:86, S01:32, S02:81, S03:47, S03:48, S04:63, S04:113, S05:140, S05:173, S06:24, S07:17, S10:29, S10:30, S11:61

```tex
$\JI$
```

### Inline raw group 006

Occurrences (1): S00:86

```tex
$\JC$
```

### Inline raw group 007

Occurrences (2): S00:86, JA:15

```tex
$\sigma$
```

### Inline raw group 008

Occurrences (7): S00:87, S04:20, S04:76, S05:109, JA:15, JA:164, JA:188

```tex
$\tau$
```

### Inline raw group 009

Occurrences (4): S00:88, S04:58, S10:24, S12:24

```tex
$\Phi = K*I$
```

### Inline raw group 010

Occurrences (2): S00:89, JA:18

```tex
$\Phi \approx -\alpha C + \Phi_0$
```

### Inline raw group 011

Occurrences (3): S00:93, S05:162, S05:163

```tex
$C < \Cmax$
```

### Inline raw group 012

Occurrences (6): S01:10, S02:75, S03:38, S03:46, JA:87, JA:129

```tex
$\Phi(x,\tau)$
```

### Inline raw group 013

Occurrences (3): S01:16, S12:15, JA:556

```tex
$I(x,\tau)$
```

### Inline raw group 014

Occurrences (1): S01:18

```tex
$I=f(1-C)$
```

### Inline raw group 015

Occurrences (1): S01:18

```tex
$\Phi = K * I$
```

### Inline raw group 016

Occurrences (1): S01:21

```tex
$\ell_i = \mathcal{Q}[I,\Phi,C;\,\text{constraints}]$
```

### Inline raw group 017

Occurrences (17): S01:22, S02:82, S02:86, S04:61, S04:116, S05:67, S06:21, S10:31, S12:34, JA:33, JA:91, JA:93, JA:183, JA:202, JA:296, JA:491, JA:565

```tex
$\nabla\Phi$
```

### Inline raw group 018

Occurrences (1): S01:25

```tex
$\Delta \to C \to I \to \Phi \to \JI \to \Delta$
```

### Inline raw group 019

Occurrences (1): S01:27

```tex
$\Phi \seddto \Phistar$
```

### Inline raw group 020

Occurrences (3): S01:30, JA:37, JA:87

```tex
$\nabla\Phi(x) \approx 0$
```

### Inline raw group 021

Occurrences (5): S01:33, JA:41, JA:95, JA:167, JA:567

```tex
$I(x,\tau) > 0$
```

### Inline raw group 022

Occurrences (1): S02:75

```tex
$\nabla\Phi(x)\approx 0$
```

### Inline raw group 023

Occurrences (3): S02:89, S04:26, S12:38

```tex
$I(x,\tau)>0$
```

### Inline raw group 024

Occurrences (5): S03:39, JA:297, JA:298, JA:482, JA:561

```tex
$\nabla\Phi \approx 0$
```

### Inline raw group 025

Occurrences (16): S03:40, S05:68, S05:108, JA:15, JA:39, JA:91, JA:129, JA:130, JA:183, JA:201, JA:267, JA:299, JA:348, JA:489, JA:490, JA:548

```tex
$J_I$
```

### Inline raw group 026

Occurrences (2): S03:48, JA:130

```tex
$-\nabla\Phi$
```

### Inline raw group 027

Occurrences (3): S03:49, S06:25, JA:131

```tex
$|\nabla\Phi|$
```

### Inline raw group 028

Occurrences (2): S04:14, JA:163

```tex
$I(x,\tau) = f(1-C(x,\tau))$
```

### Inline raw group 029

Occurrences (7): S04:20, S04:53, S05:127, S05:134, JA:164, JA:180, JA:261

```tex
$x$
```

### Inline raw group 030

Occurrences (2): S04:52, JA:180

```tex
$C(x,\tau)$
```

### Inline raw group 031

Occurrences (1): S04:54

```tex
$C \in [0,\Cmax)$
```

### Inline raw group 032

Occurrences (3): S04:55, JA:32, JA:181

```tex
$I(x,\tau) = f(1-C)$
```

### Inline raw group 033

Occurrences (4): S04:57, JA:181, JA:280, JA:430

```tex
$I > 0$
```

### Inline raw group 034

Occurrences (1): S04:64

```tex
$\JI = -D\nabla I + \mu F_I$
```

### Inline raw group 035

Occurrences (2): S04:67, JA:185

```tex
$\sigma = \sigma_d - \sigma_p - \sigma_b$
```

### Inline raw group 036

Occurrences (5): S04:70, S05:108, S07:15, JA:186, JA:347

```tex
$\Delta$
```

### Inline raw group 037

Occurrences (2): S04:73, JA:187

```tex
$\delta I$
```

### Inline raw group 038

Occurrences (1): S04:79

```tex
$\ell_i = \mathcal{Q}[I,\Phi,C;\cdot]$
```

### Inline raw group 039

Occurrences (4): S04:84, S05:119, S07:51, S10:33

```tex
$\Phistar$
```

### Inline raw group 040

Occurrences (3): S04:87, S05:37, S05:164

```tex
$\Cmax$
```

### Inline raw group 041

Occurrences (4): S04:95, S10:32, JA:193, JA:492

```tex
$\mathcal{Q}$
```

### Inline raw group 042

Occurrences (7): S04:115, S05:67, S05:80, S10:31, JA:202, JA:243, JA:491

```tex
$\ell_i$
```

### Inline raw group 043

Occurrences (1): S05:36

```tex
$C_*$
```

### Inline raw group 044

Occurrences (1): S05:39

```tex
$C_* < \Cmax$
```

### Inline raw group 045

Occurrences (10): S05:42, S07:15, S09:33, S10:21, S11:33, JA:234, JA:347, JA:449, JA:481, JA:531

```tex
$\sigma_{\mathrm{drive}}$
```

### Inline raw group 046

Occurrences (4): S05:44, S09:41, JA:235, JA:454

```tex
$\sigma_{\mathrm{dissip}}$
```

### Inline raw group 047

Occurrences (6): S05:46, S07:57, S09:32, JA:236, JA:374, JA:449

```tex
$\sigma_{\mathrm{barrier}}$
```

### Inline raw group 048

Occurrences (1): S05:69

```tex
$\lambda \sum_i \ell_i \cdot \nabla\Phi$
```

### Inline raw group 049

Occurrences (2): S05:107, JA:34

```tex
$\Delta \to C \to I \to \Phi \to J_I \to \Delta$
```

### Inline raw group 050

Occurrences (4): S05:139, S05:140, JA:267, JA:267

```tex
$\mathcal{R}$
```

### Inline raw group 051

Occurrences (4): S05:141, S05:146, JA:267, JA:271

```tex
$\theta$
```

### Inline raw group 052

Occurrences (6): S05:149, S09:63, S11:44, JA:271, JA:466, JA:537

```tex
$D$
```

### Inline raw group 053

Occurrences (6): S05:149, S09:63, S11:44, JA:271, JA:466, JA:537

```tex
$\mu$
```

### Inline raw group 054

Occurrences (6): S05:149, S09:64, S11:44, JA:271, JA:466, JA:537

```tex
$\alpha$
```

### Inline raw group 055

Occurrences (2): S05:162, JA:278

```tex
$I = f(1-C) > 0$
```

### Inline raw group 056

Occurrences (2): S05:168, S08:83

```tex
$I>0$
```

### Inline raw group 057

Occurrences (1): S05:177

```tex
$\nabla\Phi\neq0$
```

### Inline raw group 058

Occurrences (4): S06:22, S06:23, S10:22, S12:24

```tex
$\nabla\Phi\approx 0$
```

### Inline raw group 059

Occurrences (2): S06:35, JA:307

```tex
$-\min\Phi$
```

### Inline raw group 060

Occurrences (2): S06:69, JA:326

```tex
$\{\ell_i\}$
```

### Inline raw group 061

Occurrences (2): S06:76, JA:331

```tex
$S(\ell_i)$
```

### Inline raw group 062

Occurrences (2): S06:77, JA:331

```tex
$\epsilon$
```

### Inline raw group 063

Occurrences (1): S07:58

```tex
$C\to\Cmax$
```

### Inline raw group 064

Occurrences (4): S09:63, S11:43, JA:466, JA:537

```tex
$K$
```

### Inline raw group 065

Occurrences (4): S09:64, S11:44, JA:466, JA:537

```tex
$\Gamma$
```

### Inline raw group 066

Occurrences (4): S09:64, S11:44, JA:466, JA:537

```tex
$\kappa_B$
```

### Inline raw group 067

Occurrences (2): S10:25, JA:485

```tex
$-\Phi(x,\tau)$
```

### Inline raw group 068

Occurrences (1): S10:25

```tex
$=$
```

### Inline raw group 069

Occurrences (1): S10:28

```tex
$\int|\nabla\Phi|dx$
```

### Inline raw group 070

Occurrences (1): JA:15

```tex
$J_C$
```

### Inline raw group 071

Occurrences (5): JA:17, JA:32, JA:182, JA:484, JA:561

```tex
$\Phi = K \ast I$
```

### Inline raw group 072

Occurrences (3): JA:20, JA:278, JA:278

```tex
$C < C_{\max}$
```

### Inline raw group 073

Occurrences (1): JA:33

```tex
$\ell_i = \mathcal{Q}[I, \Phi, C\,;\,\text{制約}]$
```

### Inline raw group 074

Occurrences (1): JA:34

```tex
$\Phi \to \Phi^*$
```

### Inline raw group 075

Occurrences (1): JA:180

```tex
$C \in [0, C_{\max})$
```

### Inline raw group 076

Occurrences (1): JA:184

```tex
$J_I = -D\nabla I + \mu F_I$
```

### Inline raw group 077

Occurrences (1): JA:189

```tex
$\ell_i = \mathcal{Q}[I,\Phi,C\,;\cdot]$
```

### Inline raw group 078

Occurrences (4): JA:190, JA:256, JA:371, JA:493

```tex
$\Phi^*$
```

### Inline raw group 079

Occurrences (1): JA:191

```tex
$C_{\max}$
```

### Inline raw group 080

Occurrences (1): JA:280

```tex
$\nabla\Phi \neq 0$
```

### Inline raw group 081

Occurrences (1): JA:280

```tex
$J_I \neq 0$
```

### Inline raw group 082

Occurrences (1): JA:300

```tex
$\lvert\nabla\Phi\rvert$
```

### Inline raw group 083

Occurrences (1): JA:374

```tex
$C \to C_{\max}$
```

### Inline raw group 084

Occurrences (1): JA:488

```tex
$\int\lvert\nabla\Phi\rvert dx$
```

VED×IFGTのtimesやnote tableの単独等号は形式記号の索引には含むが、新たな理論関係familyには数えない。
READMEのbacktick数式は上表INLINE022と、INLINE001/002/011/012に対応する。main.texの5 notation macrosはINLINE023、typesetting色・幅・font等は理論notationではなく除外した。

## 6. Symbol inventory

NS=no unit specified、EA=effective/arbitrary scale（校正値なし）、QO=qualitative only、UC=unclear across contexts。
PARTIAL等はsource descriptionの完備度。vectorらしい演算構文はINFERREDと明記し、fontや太字から型を断定しない。
「First」は本台帳scope内の初出（詳細な定義locatorを括弧に併記）。macroはentryで宣言されるため初出がentryとなる場合がある。

| SYM | Glyph | First locator / definition | Mathematical role | Semantic/cognitive label | Signature | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| CT-SYM-001 | x | S01:10 (definition S04:20) | field argument / position | conceptual position | PARTIAL | NS |
| CT-SYM-002 | x_1,x_2 | FIG001 | coordinate labels, axes inferred | landscape visualization | INFERRED | NS |
| CT-SYM-003 | \tau | S00:87 (roles S04:20/76) | evolution/order argument | experiential irreversible ordering | PARTIAL | UC |
| CT-SYM-004 | C | S00:86 (definition S04:52–54) | closure field/range [0,Cmax) | cognitive fixation | PARTIAL | NS |
| CT-SYM-005 | C_* | S05:28/37 | effective saturation parameter | conceptual quasi-closure | PARTIAL | EA |
| CT-SYM-006 | C_{\max} / \Cmax | S00:49/93;S05:38 | ideal upper boundary | complete closure limit | PARTIAL | NS |
| CT-SYM-007 | I | S00:86 (definition S04:14) | information density field | unresolved tension | PARTIAL | NS |
| CT-SYM-008 | f | S01:18;S04:14 | function in I=f(1-C) | projected density relation | UNRESOLVED | NS |
| CT-SYM-009 | \delta I | S04:73 | perturbation/residue notation | past-experience residue | PARTIAL | NS |
| CT-SYM-010 | \Phi | S00:86/88 (scalar field S04:39) | scalar field explicitly named; domain missing | landscape, not primitive meaning field | PARTIAL | NS |
| CT-SYM-011 | \Phi^{*} / \Phistar | S00:50;S01:27;S05:114 | asymptotic landscape | sedimented history | PARTIAL | NS |
| CT-SYM-012 | K | S00:88;S04:33 | convolution kernel role | field geometry | PARTIAL | NS |
| CT-SYM-013 | \nabla\Phi | S01:22 (direction S04:61) | gradient output, vector-like inferred | least-resistance direction | INFERRED | NS |
| CT-SYM-014 | \nabla I | S04:64;S05:17 | gradient output, vector-like inferred | flow diffusion component | INFERRED | NS |
| CT-SYM-015 | \nabla C | S05:17;README | gradient output, vector-like inferred | closure force direction | INFERRED | NS |
| CT-SYM-016 | J (flow) | FIG003;README convention | bare flow glyph | information flow/search/integration | UNRESOLVED | UC |
| CT-SYM-017 | J_I / J_{\!I} / \JI | S00:47;S04:64 | flow field; vector-like via divergence | thought trajectory role | PARTIAL | NS |
| CT-SYM-018 | J_C / J_{\!C} / \JC | S00:48;README | closure flow expression | closure-side flow | PARTIAL | NS |
| CT-SYM-019 | \sigma | S00:72;S04:67;S05:21 | net source term | generation/decay/barrier | PARTIAL | NS |
| CT-SYM-020 | \sigma_d,\sigma_p,\sigma_b | S04:67;JA185 | short source components; aliases unspecified | input/decay/barrier table | UNRESOLVED | NS |
| CT-SYM-021 | \sigma_{\mathrm{drive}} | S05:22/28 | source contribution | novel input | PARTIAL | NS |
| CT-SYM-022 | \sigma_{\mathrm{dissip}} | S05:22/30;S07:37 | subtracted positive expression Gamma C | forgetting/habituation | PARTIAL | NS |
| CT-SYM-023 | \sigma_{\mathrm{barrier}} | S05:22/32 | subtracted barrier expression | overclosure resistance | PARTIAL | NS |
| CT-SYM-024 | F_I | S04:64;S05:17 | force-like gradient relation | landscape directional force | PARTIAL | NS |
| CT-SYM-025 | \alpha | S00:89;S05:17/149 | coefficient; linear approximation context | force/threshold context | PARTIAL | NS |
| CT-SYM-026 | \mu | S04:64;S05:17/149 | flow coefficient | mobility-like / upstream roles distinct | PARTIAL | UC |
| CT-SYM-027 | D | S04:64;S05:17/149 | diffusion-like coefficient | flow and cost context | PARTIAL | NS |
| CT-SYM-028 | \Gamma | S05:30;S07:37 | decay coefficient | forgetting | PARTIAL | NS |
| CT-SYM-029 | a | S05:28 | multiplicative coefficient inferred | input strength | INFERRED | NS |
| CT-SYM-030 | \kappa_B | S05:32;S11 | barrier coefficient | resistance | PARTIAL | NS |
| CT-SYM-031 | \ell_i | S01:21;S04:79;S05:80 | explicit discrete token; vector realization absent | re-addressable, meaning-neutral unit | PARTIAL | NS |
| CT-SYM-032 | \ell (unindexed) | S05:84 | argument of L_token; collection vs element unstated | token sector | UNRESOLVED | NS |
| CT-SYM-033 | i | S01:21;S05:85 | token index inferred | token enumeration | INFERRED | NS |
| CT-SYM-034 | \lambda | S05:69 (EQ006 S05:85) | coupling coefficient inferred | reuse coupling strength | INFERRED | NS |
| CT-SYM-035 | \mathcal L_{\mathrm{eff}} | S05:83 | effective L expression; scalar/action status unstated | coupled evolution | UNRESOLVED | NS |
| CT-SYM-036 | \mathcal L_{\mathrm{field}}[I] | S05:83 | functional-like bracketed dependence | field contribution | PARTIAL | NS |
| CT-SYM-037 | \mathcal L_{\mathrm{token}}[\ell] | S05:84 | functional-like bracketed dependence | token contribution | PARTIAL | NS |
| CT-SYM-038 | \mathcal Q | S01:21;S04:79/83 | extraction operator, input tuple supplied | continuous → discrete unit | PARTIAL | NS |
| CT-SYM-039 | constraints / \cdot (Q slot) | S01:21;S04:79;JA33/189 | unspecified fourth slot, not inner product | extraction constraints | UNRESOLVED | NS |
| CT-SYM-040 | \mathcal R | S05:139/143 | conceptual region, not scalar cost R | understanding region | PARTIAL | NS |
| CT-SYM-041 | \theta | S05:141/143/146 | effective system-dependent threshold | allowable recursive cost | PARTIAL | EA |
| CT-SYM-042 | \mathcal V | S06:73 | set comprehension; prose says distribution | vocabulary | PARTIAL | NS |
| CT-SYM-043 | S(\ell_i) | S06:73/76 | stability functional named | reuse/persistence/depth | PARTIAL | NS |
| CT-SYM-044 | \epsilon | S06:73/77 | threshold | vocabulary membership | PARTIAL | NS |
| CT-SYM-045 | \Phi_0 | S00:89;JA18;IFGT fundamental | additive offset; constancy upstream explicit | linear approximation offset | INFERRED | NS |
| CT-SYM-046 | \|\nabla\Phi\| / \lvert\nabla\Phi\rvert | S05:143;JA269 | magnitude/norm, metric unspecified | traversal cost integrand | PARTIAL | NS |
| CT-SYM-047 | -\min\Phi | S06:35;JA307 | within-well minimum sign reversal | depth/resistance | INFERRED | NS |
| CT-SYM-048 | collective \Phi | S08:59;JA417 | social landscape, aggregation unspecified | shared sedimentation | UNRESOLVED | UC |
| CT-SYM-049 | A / B | FIG001 | explicit names of two pictured basins | concept basins | EXPLICIT | QO |
| CT-SYM-050 | \JI,\JC,\Cmax,\Phistar,\seddto (macros) | S00:47–51 | explicit literal expansion only | presentation aliases | EXPLICIT | NS |
| CT-SYM-051 | 0 / 1 / \infty | S04:14/54;S05:115 | literal constants / endpoint notation | zero slope, complement, long time | EXPLICIT | NS |
| CT-SYM-052 | J (language label) | S10:18 | literal Japanese-original column code; nonmath | note translation layer | EXPLICIT | QO |
| CT-SYM-053 | \Delta | S01:25;S04:70;S05:28 | residual asymmetry/input object | novelty / loop residual | PARTIAL | NS |

## 7. Signature classification

EXPLICIT: 指定された役割/alias/ラベルがsourceに明記され、その限定された記録対象は特定できる。
INFERRED: indexやvector-like output等を演算構文から読むがsourceのtyped宣言ではない。
PARTIAL: field/parameter/operator等の役割またはargumentsだけが記され、domain/codomain/metric等は未固定。
UNRESOLVED: 曖昧な名称/引数、複数contextの接続が未特定。
CONFLICTING: 同一source-local signatureに相容れない明示指定がある場合だけ。単なる未指定、上流差、figure naming差から採点しない。

| Signature status | Symbol families |
| --- | --- |
| EXPLICIT | 4 |
| INFERRED | 9 |
| PARTIAL | 33 |
| UNRESOLVED | 7 |
| CONFLICTING | 0 |

Mother set: 53 CT-SYM rows。EQF status: PARTIAL13 / UNRESOLVED1。

symbol summaryを母数とし、equation-family/inline/operator ledgerのstatusは別母数。PARTIAL≠数学的不正、EXPLICIT≠完全なempirical map。

## 8. Domain / codomain ledger

「未記載」はsourceにないtypeを監査で足さない意味。signatureをcompleteにする提案ではない。

| CT-SIG | Object/map | Domain → codomain supplied? | Continuous/discrete / scope | Status |
|---|---|---|---|---|
| CT-SIG-001 | x,tau | position/timeという説明まで、空間集合・次元・clock未指定 | conceptual / evolution | PARTIAL |
| CT-SIG-002 | I=f(1-C) | scalar-like composition; fの定義域・値域・形未指定 | projected closure→density | PARTIAL |
| CT-SIG-003 | K*I | convolutionとscalar Phi; kernel domain・measure・boundary未指定 | continuous field picture | PARTIAL |
| CT-SIG-004 | grad Phi / div J_I | calculus syntaxあり、metric・dimension・vector bundle未指定 | field | INFERRED |
| CT-SIG-005 | J_I | gradients/forceを入力とする式、codomainのCT-local宣言未指定 | cognitive flow interpretation | PARTIAL |
| CT-SIG-006 | F_I | gradient chain、線形近似はS00:89; general convolutionとのsignature統合未指定 | field | PARTIAL |
| CT-SIG-007 | source components | C,Deltaを入力とする式、Deltaのdomain未固定 | drive/decay/barrier | PARTIAL |
| CT-SIG-008 | Q | [I,Phi,C;constraints/dot]→discrete re-addressable tokenとの説明 | continuous/discrete | PARTIAL |
| CT-SIG-009 | ell_i dot grad Phi | tokenという説明はあるが共通vector space/embeddingなし | discrete vs field gradient | UNRESOLVED |
| CT-SIG-010 | L_eff,L_field,L_token | bracketed inputsのみ、functional/action/densityの型未固定 | token/field | UNRESOLVED |
| CT-SIG-011 | Phi* | x依存landscape、収束空間・topology・norm未指定 | long-time / nonstatic qualification | PARTIAL |
| CT-SIG-012 | concept predicate | position x + J_I perturbation、neighborhood/norm/horizon未指定 | local region | PARTIAL |
| CT-SIG-013 | integral over calR | conceptual region、dx、absolute gradient; measure/metric未指定 | region integral (not supplied path integral) | PARTIAL |
| CT-SIG-014 | S(ell_i),calV | stability functional→threshold selection; numerical codomain/measure未指定 | discrete token set | PARTIAL |
| CT-SIG-015 | collective Phi | individualからcollectiveへのaggregate mapなし | individual/social domain関係未指定 | UNRESOLVED |
| CT-SIG-016 | J_C | README closure-gradient expression; CT正文のflowと同一spaceか未指定 | supporting notation | PARTIAL |
| CT-SIG-017 | projection/window | projected-use proseのみ、named operatorなし | domain-specific reuse | UNRESOLVED |

## 9. Unit / dimensional status

unit台帳は同じunit状況を持つmajor-symbol群単位。すべてsource記述の状態でありdimensional analysis/correctionを行わない。
explicit physical unit=0、明示dimensionless指定=0。数値範囲[0,Cmax)やliteral 1はdimensionless宣言として数えない。

| CT-UNIT | Symbols / locator | Source unit status | What remains unspecified |
|---|---|---|---|
| CT-UNIT-001 | x,x1,x2 / S04,FIG001 | no unit specified | position scale/dimension |
| CT-UNIT-002 | tau / S04,S05,S08 | unclear across contexts | evolution/experiential/social clocks |
| CT-UNIT-003 | C,Cmax / S04–05 | no unit specified | closure scale/normalization |
| CT-UNIT-004 | C_* / S05:37 | effective / arbitrary scale | effective saturation calibration |
| CT-UNIT-005 | I,deltaI,f / S04 | no unit specified | density measure/complement scale |
| CT-UNIT-006 | Phi,Phi*,Phi0,K / S00,S04–05 | no unit specified | potential/kernel normalization |
| CT-UNIT-007 | gradient/divergence / S05 | no unit specified | coordinate metric and resulting units |
| CT-UNIT-008 | J_I,J_C,F_I,bare J / S05,README,FIG003 | no unit specified | flux/force vs representational roles |
| CT-UNIT-009 | sigma and six short/long suffixes / S04–05 | no unit specified | source scales and sign convention correspondence |
| CT-UNIT-010 | D / S05 | no unit specified | diffusion coefficient dimensions |
| CT-UNIT-011 | mu / S05,Con TCA | unclear across contexts | CT flow coefficient vs Con viscosity |
| CT-UNIT-012 | alpha / S00,S05 | no unit specified | linear conversion factor |
| CT-UNIT-013 | Gamma / S05,S07 | no unit specified | decay rate units/clock |
| CT-UNIT-014 | a,Delta,kappa_B / S05 | no unit specified | input/barrier scales |
| CT-UNIT-015 | ell_i,ell,Q,constraints / S04–05 | no unit specified | token numeric realization |
| CT-UNIT-016 | lambda,L_eff,L_field,L_token / S05 | no unit specified | coupling/action/density dimensions |
| CT-UNIT-017 | calR,dx,absolute gradient / S05 | no unit specified | region measure and cost units |
| CT-UNIT-018 | theta / S05:146 | effective / arbitrary scale | allowable cost, value not specified |
| CT-UNIT-019 | V,S,epsilon / S06 | no unit specified | set vs distribution, score scale |
| CT-UNIT-020 | depth,width,curvature / S06 | qualitative only (depth shorthand present) | no calibrated geometric/semantic units |
| CT-UNIT-021 | collective Phi / S08 | unclear across contexts | common social/individual scale |
| CT-UNIT-022 | labels A/B,language J / figures,S10 | qualitative only | labels, not physical quantities |

## 10. Object-to-symbol crosswalk

Phase00 IDsとT-layer tagsを保持。T0 formal / T1 semantic / T2 cognitive / T3 phenomenalは監査層。role併記は同一視ではない。

| OBJ | Symbol(s) | EQF / inline | T-layer roles | Ambiguity |
|---|---|---|---|---|
| CT-OBJ-001 | x,x1,x2 | 001;FIG001 | T0/T1 | conceptual domain未固定 |
| CT-OBJ-002 | tau | 002/010 | T0/T2/T3 | evolution/experience/order |
| CT-OBJ-003 | C | 002–008;INLINE001 | T0/T1 | scalar vs cognitive fixation |
| CT-OBJ-004 | I,f | 001/002;INLINE001 | T0/T1/T2 | f未指定 |
| CT-OBJ-005 | Phi | 001 | T0/T1/T2 | field vs landscape |
| CT-OBJ-006 | K | 001 | T0 | kernel domain |
| CT-OBJ-007 | grad Phi | 004/011/012 | T0/T2 | direction/norm |
| CT-OBJ-008 | J_I | 002/003 | T0/T2 | vector-like vs trajectory |
| CT-OBJ-009 | J_C | INLINE022 | T0 | README-only relation |
| CT-OBJ-010 | sigma variants | 005–008 | T0/T2 | suffix/sign conventions |
| CT-OBJ-011 | Delta | 006;INLINE008 | T0/T2 | residual/input |
| CT-OBJ-012 | deltaI | INLINE token index | T0/T1 | residue perturbation |
| CT-OBJ-013 | ell_i | 009/014 | T0/T1/T2 | discrete token vs dot operand |
| CT-OBJ-014 | Q | INLINE007 | T0/T1 | extraction signature partial |
| CT-OBJ-015 | L family,lambda | 009 | T0/T2 | effective L type unresolved |
| CT-OBJ-016 | Phi* | 010 | T0/T1/T2 | limit vs continued change |
| CT-OBJ-017 | grad Phi≈0;stability | 011 | T0/T1 | tolerance/perturbation |
| CT-OBJ-018 | calR,integral,theta | 012 | T0/T2 | calR region, scalar R not located |
| CT-OBJ-019 | Cmax | 008/013 | T0/T1 | ideal boundary |
| CT-OBJ-020 | C_* | 006;INLINE006 | T0/T1 | subscript star, not C^* |
| CT-OBJ-021 | D,mu,alpha,F_I,Phi0 | 003/004;INLINE003 | T0 | effective coefficients |
| CT-OBJ-022 | a,Gamma,kappa_B | 006–008 | T0/T2 | unit/calibration |
| CT-OBJ-023 | -min Phi;width;curvature | INLINE018 | T0/T1/T2 | only depth shorthand |
| CT-OBJ-024 | ridge/boundary | FIG001;S06 | T0/T1/T2 | no separate boundary operator |
| CT-OBJ-025 | V,S,epsilon | 014 | T0/T1 | set vs prose distribution |
| CT-OBJ-026 | limit cycle | S06:24/S10:29 prose | T0/T2 | no separate cycle equation |
| CT-OBJ-027 | topology/insight | S07 prose | T0/T1/T2/T3 | no bifurcation parameter law |
| CT-OBJ-028 | collective Phi | S08 prose | T0/T1/T2 | same glyph; aggregate absent |
| CT-OBJ-029 | projection/window | S02,S04,S11 prose | T0/T1 | no typed operator |
| CT-OBJ-030 | distance/similarity/adjacency | S03,S06 prose | T1/T2 | metric not defined |
| CT-OBJ-031 | Gamma C;Phi* | 007/010 | T0/T2 | forgetting/sedimentation reading |
| CT-OBJ-032 | meaning/trajectory | J_I,Phi prose | T1/T2/T3 | not intrinsic token semantics |

## 11. Glyph collision expansion

全12既存familiesを展開。CONFLICTING signatureとの自動同一視はしない。

| CT-GLYPH | Raw role distinctions / exact locators | Same object explicitly claimed? | Unresolved boundary |
|---|---|---|---|
| CT-GLYPH-001 | CT S04:33 Phi=K*I; S00:89 linear Phi≈-alpha C+Phi0; IFGT fundamental:20 Phi linear | formal reuse wording; exact signature UNCLEAR | kernel vs linear approximation |
| CT-GLYPH-002 | CT S04:38 scalar potential/S04:58 landscape; Con dynamics_log_referencing:132 analogous gradient role | current Con denies quantity identity | CT local vs Con meaning role |
| CT-GLYPH-003 | CT S05:114–122 Phi*; Con dynamics_log_referencing CT sedimentation comparison | comparison, not typed identity | Con logs vs CT limit |
| CT-GLYPH-004 | CT S04:76 tau experiential order/S05:115 infinity; Con dynamics_log_referencing:61 internal delay distinction; IFGT fundamental:23 order | NO cross-source equality fixed | three temporal roles |
| CT-GLYPH-005 | S00:47–48 JI/JC macros; S05:17 JI; FIG003 bare J; README bare-J convention | intended flow label association; not algebraic alias declaration for picture | body/caption/picture names |
| CT-GLYPH-006 | CT S04:54 C cognitive fixation; VED closure:50 C_ij; IFGT unified:6 scalar not node matrix | projected reuse, not supplied aggregation | scalar/node-level |
| CT-GLYPH-007 | S04:67 sigma_d-p-b; S05:22 drive-dissip-barrier; IFGT unified:26/34 signed negative components | short/long alias UNCLEAR | sign accounting separate |
| CT-GLYPH-008 | S04:79/83 ell_i discrete operator; S05:85 ell_i dot grad Phi; L_token[ell] | same token name used; numeric type not declared | discrete/vector/collection |
| CT-GLYPH-009 | S05:119 individual Phi*; S08:59 collective Phi | same-dynamics wording | no collective-domain signature |
| CT-GLYPH-010 | S05:17 mu flow coefficient; Con torque_converter_attention mu effective viscosity | no typed equality | unit and carrier distinction |
| CT-GLYPH-011 | S05:28 C_*; S05:32 Cmax; S05:37–39 explicit distinction | explicitly distinct scales | JA explanation absence |
| CT-GLYPH-012 | CT S04:33 Phi field; Intelligence appendix_b_homology_ja:34/53 U=Phi(L,H_ij) | comparison context, exact identity UNCLEAR | field glyph vs emergence mapping |

## 12. Figure notation

3/3 original PNGsを画像として開いて確認。図はpresentationのみ。source formatはPNG、editable vector/code sourceはPhase00同様未発見。
EN distribution PDF (19 pages) page11も既存Ghostscriptで一時renderして画像確認。Poppler未搭載のためread-only fallback。rebuildなし。
全矢印は以下で列挙し、図の描写を新式へ変換しない。

| CT-FIGSYM | Figure / inspected labels and arrows | Symbol/body relation | Inventory note |
|---|---|---|---|
| CT-FIGSYM-001 | [FIG001](../../conceptual-topography/figures/fig1_potential_geometry.png): Phi(x,tau),vertical Phi,x1,x2 | S04 scalar potential; x1/x2 figure-only | axes/domain dimension not defined |
| CT-FIGSYM-002 | FIG001: Concept basin A/B, grad Phi≈0 | EQF011; A/B only labels | basin→concept naming |
| CT-FIGSYM-003 | FIG001: gray -grad Phi arrows, thick curved J_I thought trajectory | EQF003/004; S03 caption | local descent vs trajectory picture |
| CT-FIGSYM-004 | FIG001: conceptual boundary ridge between basins | S06 category boundary prose | no formal boundary operator |
| CT-FIGSYM-005 | [FIG002](../../conceptual-topography/figures/fig2_token_field_coupling.png): ell_i purple token before/after | S05:80 | discrete token; no vector embedding shown |
| CT-FIGSYM-006 | FIG002: -grad Phi weak/reinforced; J_I arrows | S05:66–69 | weak/strong labels lack numeric scale |
| CT-FIGSYM-007 | FIG002: lambda sum_i ell_i dot grad Phi | EQF009 coupling term | dot product typing still unprovided |
| CT-FIGSYM-008 | FIG002: Before reuse → After repeated reuse; repeated token-field coupling (reuse) arrow | S05:89–92 | repeated-use direction, not executed dynamics |
| CT-FIGSYM-009 | FIG002: shallow/deepened basin, lower traversal cost, J_I more easily attracted; meaning-neutral discrete token acts locally | EQF012/S05 text | cognitive/semantic annotations |
| CT-FIGSYM-010 | [FIG003](../../conceptual-topography/figures/fig3_minimal_recursive_loop.png): Delta residual/asymmetry → C closure/fixation | INLINE008 | labels plus directed arrow |
| CT-FIGSYM-011 | FIG003: C → I information density/accumulation → Phi information potential/concept attractors | S05:107 caption | directed representation |
| CT-FIGSYM-012 | FIG003: Phi → bare J information flow/search/integration/transmission → Delta residual reemerges | caption J_I vs image J vs README convention | naming discrepancy retained |
| CT-FIGSYM-013 | FIG003: bottom full Delta→C→I→Phi→J→Delta; tau irreversible ordering; unidirectional/irreversible causality labels | S05:107–110 | no inverse arrow/formal causal theorem added |

## 13. EN / JA formal variants

All EQF001–014 covered. EXACT MATCHここではraw byte equality、同じfamily=同じsignatureではない。

| CT-FORMALVAR | Family / locators | Classification | Difference retained |
|---|---|---|---|
| CT-FORMALVAR-001 | EQF001 EN001/JA001 | NOTATIONAL VARIANT | convolution * vs ast / spacing / environment |
| CT-FORMALVAR-002 | EQF002 EN002/JA002 | NOTATIONAL VARIANT | JI macro vs literal, frac formatting |
| CT-FORMALVAR-003 | EQF003/004 EN003/JA003 | NOTATIONAL VARIANT | JI macro and spacing; chain retained |
| CT-FORMALVAR-004 | EQF005 EN004/JA004 | NOTATIONAL VARIANT | net source decomposition formatting |
| CT-FORMALVAR-005 | EQF006–008 EN005/JA005–007;EN012/JA014 | NOTATIONAL VARIANT | one align vs three displays; repeated Gamma C |
| CT-FORMALVAR-006 | EQF009 EN006/JA008 | NOTATIONAL VARIANT | L arguments/dot present both; no repaired type |
| CT-FORMALVAR-007 | EQF010 EN007/JA009;S05:119–122/JA256 | PROSE-STRENGTH VARIANT | not necessarily unique/static vs 一意でも静的でもない |
| CT-FORMALVAR-008 | EQF011 EN008/JA010;S03/S06/JA concept prose | PROSE-STRENGTH VARIANT | stability text translation; JA re-addressability emphasis |
| CT-FORMALVAR-009 | EQF012 EN009/JA011 | NOTATIONAL VARIANT | absolute bars vs lvert/rvert; calR region both |
| CT-FORMALVAR-010 | EQF013 EN010/JA012;S05:168–177/JA280 | PROSE-STRENGTH VARIANT | EN explicit not-pointwise guard vs JA general implication chain |
| CT-FORMALVAR-011 | EQF014 EN011/JA013 | NOTATIONAL VARIANT | set/spacing; distribution prose remains |
| CT-FORMALVAR-012 | C_*<Cmax S05:37–39 | EN ONLY | explicit saturation/ideal-boundary distinction absent JA counterpart prose |
| CT-FORMALVAR-013 | Cmax positivity S05:163–177/JA278–280 | PROSE-STRENGTH VARIANT | ideal-boundary/unattainability and quiescence qualifiers |
| CT-FORMALVAR-014 | Q S04:79–101/JA189–202 | PROSE-STRENGTH VARIANT | extraction/quantization and isomorphism comparison wording |
| CT-FORMALVAR-015 | meaning S04:110–116/S10:48–53/JA200–202/JA note table | NOTATIONAL VARIANT; negative scope SAME | Phi/J_I/ell_i nonidentity guards both present; no independent meaning equation supplied |
| CT-FORMALVAR-016 | underclosure S09 / JA 過開放 | UNRESOLVED (translation intent) | no parameter or equation merge |
| CT-FORMALVAR-017 | same-equation/generative grammar S12/JA560–573 | PROSE-STRENGTH VARIANT | projected regime wording vs solution-class / same-grammar wording |
| CT-FORMALVAR-018 | J_C closure flow README vs EN/JA body | EN ONLY supporting source | no canonical display counterpart |
| CT-FORMALVAR-019 | barrier S05:46–50 / JA236 | PROSE-STRENGTH VARIANT | projected/coarse-grained resistance vs structural prohibition wording; formula kept |

19 comparison familiesを数え、同強度確認行も含む（全行を差異ありとは数えない）。No unmatched JA displayed family。JA-only general implicationはprose-linked inline relation (INLINE016)、canonical equationへ格上げしない。

## 14. Imported vs CT-local notation

「imported」はsource自身のattribution。現行上流と同一signatureであるという監査判断ではない。

| CT-IMPORT | Relation / locator | Source wording category | Signature boundary |
|---|---|---|---|
| CT-IMPORT-001 | I=f(1-C),S04:14–16 | projected from VED/IFGT | f/domain unspecified |
| CT-IMPORT-002 | Phi=K*I,S04:33 | inherited IFGT potential | kernel not supplied locally |
| CT-IMPORT-003 | linear Phi,S00:89 | imported approximation | not general identity automatically |
| CT-IMPORT-004 | balance,EQF002 | IFGT template reuse | CT domain not typed |
| CT-IMPORT-005 | J_I,EQF003 | IFGT flow reuse | local carrier absent |
| CT-IMPORT-006 | F_I,EQF004 | IFGT force reuse | equality chain/approximation scope separate |
| CT-IMPORT-007 | sigma decomposition/drive/dissipation,EQF005–007 | projected effective terms | short/long suffix and signed source conventions |
| CT-IMPORT-008 | barrier,EQF008,S05:43–50 | explicitly cognitive analogue / coarse-grained | no new fundamental prohibition |
| CT-IMPORT-009 | Q,INLINE007 | CT-local extraction description; quantization analogy | no operational typed Q |
| CT-IMPORT-010 | coupling,EQF009 | CT-local expression | L/token signature unresolved |
| CT-IMPORT-011 | Phi*,EQF010 | CT-local sedimentation application | imported history not convergence proof |
| CT-IMPORT-012 | concept,EQF011 | CT-local Definition environment | geometric predicate incomplete signature |
| CT-IMPORT-013 | understanding,EQF012 | CT-local Definition environment | region/norm/threshold |
| CT-IMPORT-014 | positivity,EQF013 | VED×IFGT inherited proposition | conditional/pointwise distinctions |
| CT-IMPORT-015 | vocabulary,EQF014 | CT-local set definition | S functional unspecified |
| CT-IMPORT-016 | J_C,README | upstream closure-flow notation | supporting not displayed CT law |
| CT-IMPORT-017 | collective Phi,S08 | CT-local extension, same dynamics wording | no aggregation rule |
| CT-IMPORT-018 | Con tau/Phi,Int Phi | repository comparison / unclear exact provenance | reused glyph not typed inheritance |

## 15. Operator inventory

| CT-OP | Syntax / locator | Domain known? | Output type known? | Semantic interpretation / status |
|---|---|---|---|---|
| CT-OP-001 | f(1-C),S04 | no f domain | density role | projected relation; PARTIAL |
| CT-OP-002 | K*I,EQ001 | kernel/measure absent | scalar Phi named | convolution; PARTIAL |
| CT-OP-003 | grad Phi/I/C,EQ003 | metric/domain absent | vector-like inferred | direction; INFERRED |
| CT-OP-004 | div J_I,EQ002 | ambient dimension absent | scalar-like via balance | flow divergence; INFERRED |
| CT-OP-005 | partial_tau I,EQ002 | clock type partial | field rate-like | evolution; PARTIAL |
| CT-OP-006 | sum_i,EQ006 | token index set absent | depends on summands | coupling sum; PARTIAL |
| CT-OP-007 | ell_i dot grad Phi,EQ006 | common vector space absent | scalar contraction only if typing supplied | UNRESOLVED |
| CT-OP-008 | Q[...;dot],INLINE007 | tuple named, constraints absent | discrete token named | extraction; PARTIAL |
| CT-OP-009 | L_field[I],L_token[ell],EQ006 | arguments only | functional/action/density unclear | UNRESOLVED |
| CT-OP-010 | arrow with tau→infty,EQ007 | convergence space absent | Phi* landscape named | asymptotic; PARTIAL |
| CT-OP-011 | approx0,EQ008 | neighborhood/tolerance absent | predicate role | concept; PARTIAL |
| CT-OP-012 | small perturbations of J_I,EQ008 text | norm/horizon absent | stability predicate prose | PARTIAL |
| CT-OP-013 | integral_calR ... dx,EQ009 | region named, measure absent | cost-like value | understanding; PARTIAL |
| CT-OP-014 | absolute gradient,EQ009 | norm/metric absent | magnitude-like | PARTIAL |
| CT-OP-015 | <theta,>epsilon,>0,<Cmax | scale/range partial | predicate | threshold/positivity; PARTIAL |
| CT-OP-016 | forall x,tau,EQ010 | quantifier domains absent | proposition | PARTIAL |
| CT-OP-017 | set comprehension,EQ011 | token collection partial | set | vocabulary; PARTIAL |
| CT-OP-018 | S(ell_i),EQ011 | token named | score scale absent | functional; PARTIAL |
| CT-OP-019 | -min Phi,S06:35 | within-well scope given | minimum value scale absent | depth; PARTIAL |
| CT-OP-020 | 1-C,products,ratios,+/−,EQ001–012 | operand scales not supplied | algebraic combinations | no dimensional correction; PARTIAL |
| CT-OP-021 | loop arrows,INLINE008,FIG003 | named object sequence | not a typed composite map | F8/F9; UNRESOLVED |
| CT-OP-022 | projection/coarse-graining,S04/S05 | prose only | no explicit operator | UNRESOLVED |

## 16. Asymptotic formal relations

| CT-ASYMFORM | Locator | Formal relation / wording | Inventory class |
|---|---|---|---|
| CT-ASYMFORM-001 | EQ007/JA009 | Phi(x,tau) arrow Phi*(x) | limit notation + attractor naming |
| CT-ASYMFORM-002 | EQ007 annotation | tau→infty | ordering limit, topology unspecified |
| CT-ASYMFORM-003 | S05:119–122/JA256 | not necessarily unique/static; continued reshaping/decreasing rate | qualitative qualification, not a fixed-point equation |
| CT-ASYMFORM-004 | EQ008;S06 concept | small J_I perturbation stability | local predicate, tolerance unspecified |
| CT-ASYMFORM-005 | S07 learning/forgetting;EQ012 | Gamma C repeated decay | dynamical/effective interpretation |
| CT-ASYMFORM-006 | S06:21–26 / S10:29 | metastable trajectory / limit cycle | qualitative trajectory naming; no cycle solution supplied |
| CT-ASYMFORM-007 | S07 topology/insight | merge/split/displacement and rapid bifurcation | topology interpretation, no bifurcation theorem entered |
| CT-ASYMFORM-008 | S05:168–185;S07:58 | no ordinary complete closure; local quiescence; C→Cmax | formal/prose boundary distinction |
| CT-ASYMFORM-009 | S08 collective Phi | history-shaped shared landscape | collective sedimentation interpretation |
| CT-ASYMFORM-010 | S01:27;S12;JA34/567 | sedimentation summary / always revisable | cross-section asymptotic summary |

The ledger distinguishes notation, naming and prose. No convergence theorem is certified or rejected in Phase01.

## 17. Concept formal criteria

| CT-CONCEPTDEF | Criterion / locator | Mathematical specificity | Definition vs interpretation |
|---|---|---|---|
| CT-CONCEPTDEF-001 | basin/well, S03/S05 Definition | local region in Phi | explicit prose definition |
| CT-CONCEPTDEF-002 | grad Phi(x)≈0,EQ008 | approximate slope condition; no tolerance | explicit mathematical predicate |
| CT-CONCEPTDEF-003 | stability under small J_I perturbations,EQ008 | no norm/size/duration | prose predicate inside display |
| CT-CONCEPTDEF-004 | depth, S05:134/S06:35 | -min Phi within well | resistance interpretation |
| CT-CONCEPTDEF-005 | width,S05:135/S06 | subthreshold-region extent; threshold not fixed | contextual range |
| CT-CONCEPTDEF-006 | curvature,S06 | no Hessian/eigenvalue formula | discrimination/precision |
| CT-CONCEPTDEF-007 | ridge/category boundary,S06/FIG001 | dividing geometry picture, extraction absent | semantic boundary |
| CT-CONCEPTDEF-008 | JA concept/re-addressability;S04 tokens | prose recurrence/re-addressability | no additional canonical criterion |

## 18. Understanding formal criteria

| CT-UNDERSTAND | Element | Exact source status | Not added |
|---|---|---|---|
| CT-UNDERSTAND-001 | EQ009/JA011 | integral_calR absolute gradient dx < theta | no scalar R=cost definition |
| CT-UNDERSTAND-002 | calR,S05:138 | conceptual region | no path gamma or endpoints |
| CT-UNDERSTAND-003 | absolute gradient | bars/lvert-rvert | no metric/norm specification |
| CT-UNDERSTAND-004 | dx | integration element written | no arc-length ds or measure defined |
| CT-UNDERSTAND-005 | theta,S05:146–150 | effective threshold, depends on system including D,mu,alpha; value unspecified | no numeric estimator |
| CT-UNDERSTAND-006 | J_I traversal / selected concepts | prose trajectory through region | no token/endpoint selection algorithm |
| CT-UNDERSTAND-007 | nonbinary entry/exit,S05:151–152 | dynamical condition as Phi evolves | no binary empirical classifier |
| CT-UNDERSTAND-008 | S10:28;JA488 | felt understanding ↔ low integral (no calR/theta in table) | no phenomenal criterion or new identity |

## 19. Token coupling signature

| CT-COUPLING | Element / locator | Supplied | Signature status |
|---|---|---|---|
| CT-COUPLING-001 | ell_i,S04/S05:80 | discrete re-addressable unit/operator | PARTIAL; vector realization not supplied |
| CT-COUPLING-002 | grad Phi,EQ006 | local gradient | INFERRED vector-like, domain not declared |
| CT-COUPLING-003 | dot,EQ006 | printed dot operation | UNRESOLVED common space / pairing |
| CT-COUPLING-004 | lambda,EQ006 | coefficient occurrence | INFERRED; no unit/value |
| CT-COUPLING-005 | sum_i,EQ006 | indexed token sum | PARTIAL; index domain/finite count absent |
| CT-COUPLING-006 | L_eff,EQ006 | effective expression | UNRESOLVED scalar/action/density type |
| CT-COUPLING-007 | L_field[I],EQ006 | I bracket argument | PARTIAL functional-like only |
| CT-COUPLING-008 | L_token[ell],EQ006 | unindexed ell argument | PARTIAL; collection identity unresolved |
| CT-COUPLING-009 | Q→ell_i,S04 | extraction description, constraints slot | PARTIAL; no operational signature completion |
| CT-COUPLING-010 | repeated reuse,FIG002/S05 | bias/deepening/cost prose | mathematical update rule not supplied for each reuse |

A printed dot is recorded, not accepted/rejected as a legitimate product. No embedding is invented.

## 20. Positivity relation

| CT-POS | Locator | Raw/formal components | Conditions / scope retained |
|---|---|---|---|
| CT-POS-001 | EN EQ010 | I(x,tau)>0 forall x,tau | quantified domains not specified |
| CT-POS-002 | EN S05:162–164 | C<Cmax and I=f(1-C)>0 | source says follows; f not supplied |
| CT-POS-003 | EN S04:26–30/S05:173–177 | positivity is not pointwise gradPhi≠0 | explicit qualification |
| CT-POS-004 | EN S05:169–173 | residual asymmetry / inhomogeneity / boundary → generically available gradients and directions | conditional prose, not new equation |
| CT-POS-005 | EN S05:180–185 | local quiescence allowed; further differentiation under perturbation/wider window | local vs global distinction |
| CT-POS-006 | JA EQ012 / JA278 | same positive-I boxed display; C<Cmax explanation | working authority only |
| CT-POS-007 | JA280 | I>0, gradPhi≠0, J_I≠0 connected by 一般に prose | stronger chain retained as variant |
| CT-POS-008 | Cmax vs C_*,EN S05:37–39;JA226/230 | saturation below ideal boundary explicit EN | neither parameter is renamed |

No implication is proved, disproved, or repaired here.

## 21. Collective/social extension

| CT-COLLECTIVE | Element / locator | Supplied | Unspecified signature |
|---|---|---|---|
| CT-COLLECTIVE-001 | same dynamics,S08 opening | extension to collective stated in prose | no separate social PDE |
| CT-COLLECTIVE-002 | collective Phi,S08:59 | same glyph with social meaning | no aggregate operator |
| CT-COLLECTIVE-003 | multiple agents,S08 | shared/prior landscapes and inputs named | no agent index field definition |
| CT-COLLECTIVE-004 | common semantic domain | shared terrain language | no domain-identification rule |
| CT-COLLECTIVE-005 | common tau | no collective clock equation | synchrony/order relation unspecified |
| CT-COLLECTIVE-006 | common K | no collective kernel equation | kernel equality unspecified |
| CT-COLLECTIVE-007 | inputs/transmission | communication/reuse described | numerical coupling/weights unspecified |
| CT-COLLECTIVE-008 | observables/institutions/intelligence | social/cognitive examples | no observable extraction map |

## 22. Theorem-like / strong formal wording

Source wordingを記録する欄。burden/validity採点ではない。

| CT-FORMALCLAIM | Locator | Wording marker | Formal object concerned |
|---|---|---|---|
| CT-FORMALCLAIM-001 | S04:94–101 | structurally isomorphic / quantization analogy | Q |
| CT-FORMALCLAIM-002 | S05:10 | governed by | balance |
| CT-FORMALCLAIM-003 | S05:54–58 | cannot sustain / requires / generically expensive | token recursion |
| CT-FORMALCLAIM-004 | S05:89–92 | purely dynamical / each reuse reinforces | coupling |
| CT-FORMALCLAIM-005 | S05:96–97 | approaches a long-time attractor | Phi* |
| CT-FORMALCLAIM-006 | S05:127–135 | Definition / satisfying / measures | concept |
| CT-FORMALCLAIM-007 | S05:138–152 | Definition / threshold / dynamical condition | understanding |
| CT-FORMALCLAIM-008 | S05:162 | follows from | positivity |
| CT-FORMALCLAIM-009 | S05:166–177 | Proposition / excludes / generically / not pointwise | complete closure |
| CT-FORMALCLAIM-010 | S06:21–26;S07:67–77 | metastable / limit cycle / bifurcation | inference/insight |
| CT-FORMALCLAIM-011 | S08 | same dynamics / collective | social Phi |
| CT-FORMALCLAIM-012 | S12;JA conclusion | projected regimes / same equation / solution class | physical/conceptual comparison |
| CT-FORMALCLAIM-013 | JA280 | 一般に ... !=0 | positivity chain |
| CT-FORMALCLAIM-014 | S06:69–77 | stable vocabulary / stability functional | set threshold |
| CT-FORMALCLAIM-015 | S07:24–31 | ensures / self-sustaining | reuse/deepening |
| CT-FORMALCLAIM-016 | S06:10–13 | admits solution classes / analysis deferred | unified equation |
| CT-FORMALCLAIM-017 | S04:118–119;S08:62–65 | methodological necessities / follows from / sufficient | negative scope / collective depth |

## 23. Equation-context role tags

F0 formal definition; F1 dynamical law/template; F2 imported relation; F3 semantic interpretation; F4 cognitive interpretation; F5 phenomenal interpretation; F6 asymptotic; F7 cross-scale; F8 figure/presentation; F9 unresolved.
These are descriptive surroundings, not equations proving the attached role.

| EN occurrence | Family | Context tags | JA counterpart / figure |
| --- | --- | --- | --- |
| CT-EQ-001 | EQF001 | F0/F2/F3 | CT-JAEQ-001 |
| CT-EQ-002 | EQF002 | F1/F2/F4 | CT-JAEQ-002 |
| CT-EQ-003 | EQF003/004 | F1/F2/F4; F1/F2 | CT-JAEQ-003 |
| CT-EQ-004 | EQF005 | F0/F1/F2/F4 | CT-JAEQ-004 |
| CT-EQ-005 | EQF006/007/008 | F1/F2/F4; F1/F2/F4; F1/F2/F3/F4 | CT-JAEQ-005, CT-JAEQ-006, CT-JAEQ-007 |
| CT-EQ-006 | EQF009 | F1/F3/F4/F9 | CT-JAEQ-008; FIG002 |
| CT-EQ-007 | EQF010 | F3/F4/F6 | CT-JAEQ-009; FIG003 |
| CT-EQ-008 | EQF011 | F0/F3 | CT-JAEQ-010; FIG001 |
| CT-EQ-009 | EQF012 | F0/F4/F5 | CT-JAEQ-011 |
| CT-EQ-010 | EQF013 | F2/F3 | CT-JAEQ-012 |
| CT-EQ-011 | EQF014 | F0/F3 | CT-JAEQ-013 |
| CT-EQ-012 | EQF007 | F1/F2/F4 | CT-JAEQ-014 |

Every meaningful inline family has explicit F-tags in §5. Its exhaustive single-symbol/math occurrence appendix does not create additional role transitions merely by glyph repetition.

## 24. Definition inventory

| CT-DEF | Object / locator | Source class | Exact scope |
|---|---|---|---|
| CT-DEF-001 | concept,S05 Definition | explicit mathematical + prose definition | basin/slope/stability |
| CT-DEF-002 | meaning,S04 negative scope/S06/S10 | interpretation / correspondence | not intrinsic token substance; no separate meaning operator |
| CT-DEF-003 | understanding,S05 Definition | explicit mathematical + prose definition | region traversal below theta |
| CT-DEF-004 | insight,S07 | interpretation / heuristic label | rapid topology transition / suddenness |
| CT-DEF-005 | thought,S04 table | explicit prose interpretation | trajectories/flow on Phi |
| CT-DEF-006 | intelligence,S08/S12 | cognitive interpretation / extension | sustained landscape differentiation; no standalone equation |
| CT-DEF-007 | category boundary,S06/FIG001 | geometric interpretation | ridge / separation |
| CT-DEF-008 | vocabulary,S06 | explicit mathematical definition | set with S>epsilon; prose distribution |
| CT-DEF-009 | topology,S07 | heuristic geometric usage | merge/split/displacement; no axiomatic space |
| CT-DEF-010 | projection,S02/S04 | scope / analogy | domain-specific use, operator absent |
| CT-DEF-011 | observation window,S02/S04 | scope terminology | no extraction rule |
| CT-DEF-012 | token,S04/S05 | explicit prose definition + Q notation | discrete re-addressable unit, meaning-neutral |
| CT-DEF-013 | Phi,S04 | explicit mathematical definition + interpretation | K*I, scalar landscape |
| CT-DEF-014 | Phi*,S05 | asymptotic notation / naming | sedimented landscape |
| CT-DEF-015 | Q constraints,S04 | undefined slot with operator description | not algorithm |
| CT-DEF-016 | calR/metric/path,S05 | region named / metric undefined | gamma/ds absent |
| CT-DEF-017 | tau,S04 | explicit prose interpretation | evolution/experiential ordering, not calibration |
| CT-DEF-018 | collective Phi,S08 | extension / interpretation | no new definition of aggregate field |

## 25. Phase01 uncertainty ledger

| CT-U | Unresolved family | Source | Signature question |
| --- | --- | --- | --- |
| CT-U-041 | xのdomain/次元 | S04:20,FIG001 | positionとx1/x2描写の関係、continuous spaceの指定 |
| CT-U-042 | tauのclock/ordering | S04:76,S05:115,S08 | 形式時間・体験時間・集団時間を同一視しない |
| CT-U-043 | fのdomain/codomain | S04:14,S05:162 | functional form、C補数との関係 |
| CT-U-044 | K convolution domain | EQ001 | kernel support/measure/boundary/normalization |
| CT-U-045 | scalar Phiとlinear approximation | S00:89,EQ001/003 | 一般convolutionとforce equality chainの適用範囲 |
| CT-U-046 | J_I/trajectory type | S04:64–66,EQ002/003 | vector field/trajectoryの関係、ambient dimension |
| CT-U-047 | J_C CT-local role | README,S00:48 | supporting closure-flowとcanonical equationの関係 |
| CT-U-048 | figure bare J | FIG003/README/S05 caption | 名前の統一意図、J_I/上流Jとの同一性 |
| CT-U-049 | sigma suffix/sign conventions | S04:67,EQ004/005,IFGT unified | short d/p/b、long names、signed componentsの対応 |
| CT-U-050 | Delta/deltaI distinction | S04:70–75 | input/residual/traceのsignature |
| CT-U-051 | ell_i token type | S04:79–83,EQ006 | discrete token/operatorとnumeric operand |
| CT-U-052 | dot product pairing | EQ006/FIG002 | 共通space、embedding、pairing |
| CT-U-053 | Q constraints | S01:21,S04:79/95 | 入力constraints、出力集合、quantization類比のformal範囲 |
| CT-U-054 | L expression type | EQ006 | effective L/action/density/functional、unindexed ell |
| CT-U-055 | lambda/index domain | EQ006 | sum_iの対象・lambdaのscale |
| CT-U-056 | unit/dimensional status | §9 | 無単位指定とdimensionlessを混同しない |
| CT-U-057 | C_*/Cmax | S05:37–39,JA226/230 | effective/ideal尺度、JA説明差 |
| CT-U-058 | Phi* convergence notion | EQ007,S05:119–122 | topology/norm、unique/static否定の意味 |
| CT-U-059 | small perturbation stability | EQ008 | J_I perturbation norm/tolerance/time horizon |
| CT-U-060 | concept geometric criteria | S06:35–44 | width threshold/curvature/neighborhood |
| CT-U-061 | calR and integral measure | EQ009 | region dx、path gamma/dsは未発見、endpoint selection |
| CT-U-062 | gradient norm / metric | EQ009 | 絶対値記号のmetricとcost解釈 |
| CT-U-063 | theta dependence | S05:146–150 | system-dependent thresholdとD/mu/alphaの関数関係 |
| CT-U-064 | S/epsilon/vocabulary | EQ011,S06:69–77 | set vs distribution、stability score/threshold |
| CT-U-065 | positivity EN/JA chain | S04:28,S05:168–177,JA167/280 | pointwise否定guardと一般含意の差 |
| CT-U-066 | collective domain/aggregation | S08:18/42–59 | agent index、共有domainと集合Phi |
| CT-U-067 | collective K/tau/input | S08 | 共通kernel/clock/入力同期のsignature |
| CT-U-068 | topology / insight formal relation | S07:49–77 | merge/split/bifurcationの数学的対象とsubjective説明 |
| CT-U-069 | projection operation | S04/S05 | prose projected-useとoperator未定義の区別 |
| CT-U-070 | upstream glyph correspondence | §11 | CT/IFGT/Con/Intelligence同glyphを継承typeとしない |
| CT-U-071 | figure-only notation | FIG001–003 | x1/x2,A/B,J,arrowのbody関係 |
| CT-U-072 | JA working formal strength | §13 | barrier、Phi*、same-equation、quantization等のversion意図 |

既存CT-U-001–040を変更・解決・再番号化しない。新件はsignature/notation/formal presentationの未指定事項であり、欠陥・falsehood・disposition判定ではない。

## 26. Phase01 limits

token couplingのwell-typedness、positivityの正誤、Phi*の収束、concept criterionの妥当性、understanding integralの意味、semantic circularity、insight mapping、collective extension、IFGT specializationの成立、必要な式変更、claim dispositionは一切未判定。
経験データ・empirical supportの十分性も判定しない。演算・symbol・source-roleのinventoryだけを固定した。
EN canonical/JA WORKINGのauthority非対称、Consciousness/Intelligenceとのtyped translation未確定を維持する。

## 27. Validation


### Counts and counting boundaries

| Inventory | Count |
| --- | --- |
| enBlocks | 12 |
| enRelations | 14 |
| enLabels | 13 |
| jaBlocks | 14 |
| eqFamilies | 14 |
| inlineFamilies | 24 |
| inlineOccurrences | 360 |
| inlineRawGroups | 84 |
| symbols | 53 |
| units | 22 |
| operators | 22 |
| figsymbols | 13 |
| variants | 19 |
| imports | 18 |
| asym | 10 |
| concept | 8 |
| understand | 8 |
| coupling | 10 |
| positivity | 8 |
| collective | 8 |
| formalclaim | 17 |
| definitions | 18 |
| newU | 32 |
| totalU | 72 |

signature countsは§7。台帳の各ID定義行を母数とし、参照の再出現やraw appendixは新familyとして数えない。
32/32 OBJ、12/12 GLYPH、12/12 included EN sections、12/12 JA working headings、3/3 PNGs。
canonical JA entry remains NOT LOCATED。EN13 canonical text files; JA1 working source。

### Repository-local checks

実測結果（最終確認時）:

| Check | Result / counting rule |
|---|---|
| Canonical include closure | EN main + 12/12 sections; missing path 0 |
| JA authority | canonical JA entry NOT LOCATED; 12/12 working section headings (subtitle/history除外) |
| EN extraction | 12 display blocks / 14 relation rows / 13 named labels |
| JA extraction | 14 display blocks; canonical equivalenceを認定しない |
| Raw inventory | original substring bytesと26/26一致; 各block SHA-256を§2/3に保持 |
| Inline extraction | 360 occurrences / 84 raw groups; raw stringsと全locatorを再照合、一致 |
| ID/count coverage | EQ/EQF/INLINE/SYM/SIG/UNIT/OP/FIGSYM/VAR/IMPORT等のprimary ID行を再集計、duplicate/missing 0 |
| Phase00 crosswalk | OBJ32/32、GLYPH12/12; object T-layer tags保持 |
| New uncertainties | CT-U-041–072、32件連続; 既存40件不変、計72件 |
| Figures / distribution | 3/3 PNGを直接画像確認; EN既存PDF19頁のpage11を表示確認、presentation cross-checkのみ |
| Paths / links | record中の28 local Markdown linksが存在; source figure references 3件解決 |
| Bibliography / references | refs.bib 8 entries; optional cite argumentsを含む7 unique cited keys、unresolved cite/ref 0 |
| Markdown | numbered sections0–28; tables/fencesを機械点検、未閉鎖/列数不整合0 |
| README | Phase00履歴保持、Phase01 COMPLETE、Phase02 NOT STARTED、record link一致 |
| Repository diff check | git diff --check: PASS、出力なし |
| Untracked record whitespace | git diff --no-index --check /dev/null record: whitespace diagnosticなし (exit1は新規file差分) |

### Task-start SHA-256 boundary

開始時、.gitを除くrepository内の全既存file **1461件**をSHA-256 snapshotした。
snapshotは作業用 ${TEMP_EVIDENCE_ROOT}/ct_phase01.8ia84l/start_sha256.json に保持し、比較はGit HEADではなくこのtask-start状態とのbyte差分。
検証用extract/validation scriptとPDF page renderも同じrepository外temporary directoryのみ。

| Change class | Exact target / count |
|---|---|
| Existing file modified | notes/ct_audit/README_ja.md — 1 |
| New file | notes/ct_audit/01_equation_symbol_object_inventory_v0.1_ja.md — 1 |
| Existing unchanged | 1460/1460 non-target files |
| Deleted / missing | 0 |
| Source / equation / figure / PDF / BibTeX / code changes | 0 |
| Phase00 authority record | byte unchanged; SHA-256 405c7e9a54a7980253a609ea1b7f192c9e31855b6d8f159b0f0181a0e49f60a1 |

git status --shortには開始前からのupstream/Consciousness/Intelligence等の多数のdirty files、および未追跡notes directoriesが表示される。
今回の変更判定には使用していない。task-start hash比較によって上記2file以外の変更0を確認。
No source/equation/notation/figure/PDF/bibliography modification; no external research, simulation, build, new theory, new bridge, commit/push。


## 28. Stop boundary

Phase01 COMPLETEで停止。Phase02 formal / semantic / cognitive role auditには進まない。
No CT source revised / No CT equation revised / No new theory introduced。
Build・simulation・external research・citation追加・commit/pushなし。
