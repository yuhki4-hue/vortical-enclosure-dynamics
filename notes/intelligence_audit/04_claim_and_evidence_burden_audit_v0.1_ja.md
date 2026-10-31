# Intelligence Phase04 — claim / evidence burden audit v0.1

## 0. Status

```text
Intelligence audit: IN PROGRESS
Phase00–03: COMPLETE
Phase04: COMPLETE
Phase05–07: NOT STARTED
Theorem/proof validity / empirical truth: NOT AUDITED
Final dispositions: NOT ASSIGNED
Source / equation / distribution revision: NOT STARTED
```

2026-09-12のcurrent repository-local sourceに対するsupport/burden監査。YESは真理認定ではなく、記載されたscopeに適したsupportの所在判定。NOは偽ではなく要求された種類のsupport未所在。Phase03のsource-level vicious circularity NO、global unfalsifiability NOはそのまま保持し、evidence sufficiencyへ変換しない。

## 1. Authority inheritance / method

[Phase00](00_dependency_inheritance_and_authority_record_v0.1_ja.md)、[Phase01](01_equation_symbol_object_inventory_v0.1_ja.md)、[Phase02](02_role_definition_homology_audit_v0.1_ja.md)、[Phase03](03_preload_selfreference_circularity_audit_v0.1_ja.md)、[README](README_ja.md)を継承する。

P1 JA=current distributed build authority、P1 EN=current parallel source / primary未確定。P2 JA=primary manuscript、P2 EN=working draft。JA/EN、main/appendix、source/figure/distributionを分離する。source_mdは履歴でcurrent TeXを上書きしない。CTのEN canonical方針や他branchのclosureを移入しない。

P1E/P1J§n、P2E/P2J§n、P2AE/P2AJ A–Eの短縮locatorは§27のsource-artifact mapで現行fileへ展開する。66 included TeXのhashを確認し、現行本文の定義・前提・supportを直接照合した。§3/5/10/11/12とJA D、Physarum/Transformerのcitation paragraphs、社会§6–9、future宣言を重点再読。図のsupport statusはcurrent caption/figurenoteと既存SVGの文字・構造に基づくpresentation provenance判定でありPDF freshness再認証ではない。

same glyph ≠ same object、source reuse ≠ derivation、formal sketch ≠ theorem validation、analogy ≠ evidence、external citation ≠ exact Int mapping validation、figure ≠ simulation、negative guard ≠ positive support。I0–I4は監査層、LF/LR/LEはsource用語である。

E番号は種類であり大小の順位ではない。E11をE2より強いとはしない。claim表の「最強support」は適合する種類と到達範囲を文章で示す。定義をempirical criterionへ昇格しない。proof sketchはE0として数えるが、その正しさはこのphaseで判定しない。

## 2. Support taxonomy

- YES: stated/local scope内で適切な種類のsupportあり。定義・negative scope・限定比較・future記載のYESは実証を含まない。
- PARTIAL: supportはあるがscope/typeが要求より弱い、formal/operational bridgeや独立criterionが欠ける。
- NO: 要求される種類のsupport未所在。説明文やrhetorical例が存在してもNOになりうる。
- UNRESOLVED: version/provenance/authorityにより何を支持対象とするかを安全に固定できない。

family内の弱い定義と強い帰結を併記し、primary statusはfamily全体について一つだけ付す。局所定義自体を不当に否定しない。数学的妥当性未監査の定理claimは、sketchの存在を認めたPARTIALとし、証明不正という判定にはしない。

## 3. Evidence taxonomy

E0 source-internal definitions/equations/logical sketches; E1 internal structural comparison/schema/figures; E2 cited literature（same-seriesを別表示）; E3 direct behavioral observations; E4 computation/simulation; E5 sourced historical/social observations; E6 direct biological/neural measurements; E7 direct controlled mechanism test; E8 independent replication; E9 operational map/calibration; E10 implemented typed/formal bridge; E11 prospective/future; E12 no required evidence/rhetorical example-only。

E2に指示される外部実験を、repository内で実行されたE3/E6/E7として二重計上しない。社会的物語そのものはE1/E12であって、史料に基づくE5ではない。E12は正の証拠artifactではない。

## 4. Burden taxonomy

B0 definitional; B1 formal consistency; B2 theorem/formal necessity; B3 representational correspondence; B4 cognitive mechanism; B5 behavioral/empirical; B6 biological/neural; B7 social/historical; B8 phenomenal; B9 cross-domain generalization; B10 universality/general intelligence; B11 predictive/operational。

## 5. Primary claim evidence table — 95/95

直接support locatorはclaimのcurrent source位置。indirect欄は本文が再利用する背景であり独立証拠ではない。GAPは§25のfamily ID。GAPなしは限定scopeへの判定であって研究課題全体の閉鎖ではない。

| EVID | Claim | Current locator | Claim summary | Claim type | Burden | Support | Types present | Strongest scoped support | Direct support | Indirect support | Missing burden | Strong marker | Gap? | Notes / boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| INT-EVID-001 | INT-CLM-001 | P1 E/J abstract,§1–2 | 知性は所有能力でなく持続する動態 | DEF COG FUNC | B0 | YES | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J abstract,§1–2 | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | 持続する動態という枠組み内の定義を本文が明示する。一般認知性能criterionへの実証はこのYESに含めない |
| INT-EVID-002 | INT-CLM-002 | P1 E/J §2 | 知覚・認識・知識・知性の四層区別 | DEF REP COG | B0 B3 | YES | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P1 E/J §2 | 独立実証は要求scopeに含めない; §28のreference背景 | 限定scope内NONE | 専用62family対象外 | NO | 四つの役割を区別するmodel-local decompositionとして支持。GibsonはJA知覚の部分的背景で四層の検証ではない |
| INT-EVID-003 | INT-CLM-003 | P1 E/J §2,6 | 知識は安定した停止構造で真理そのものではない | DEF REP NEG | B0 | YES | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §2,6 | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | 保存・引用可能な局所停止としてのknowledge命名とnot truthを確認。Gettier説明の負担は015/078で別採点 |
| INT-EVID-004 | INT-CLM-004 | P1 E/J §2 | 知性は全層を横断し知識を産出・改訂、保存されない | COG MECH NEC | B0 B4 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §2 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 機能命名以上の過程同定 (INT-GAP-001) | INT-STRONG-001 | YES | 産出・改訂・保存不能の機能記述はあるが全層を横断する過程の独立同定はない |
| INT-EVID-005 | INT-CLM-005 | P1 E/J §3,10 | 3公理は同時必要な下限、完全理論でない | FORM NEC NEG | B0 B2 B10 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §3,10 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 条件の独立必要性・非自明な一般対象範囲 (INT-GAP-002) | INT-STRONG-002 | YES | 三条件と欠如例の表はある。intelligence-like限定とnot sufficientを保っても共同必要性の一般burdenは残る |
| INT-EVID-006 | INT-CLM-006 | P1 E/J §3 | connected state spaceは連続空間に限定しない | FORM DEF NEG | B0 B1 | YES | E0 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §3 | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | INT-STRONG-003 | NO | 離散的reachabilityを許すconnectednessの局所定義。連続位相不要というscopeのみ |
| INT-EVID-007 | INT-CLM-007 | P1 E/J §3 | temporal orderingで履歴変化が蓄積する | FORM REP | B1 B3 | PARTIAL | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P1 E/J §3 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 条件の独立必要性・非自明な一般対象範囲 (INT-GAP-002) | INT-STRONG-004 | YES | 順序updateは明示されるが順序だけから履歴保持・学習的累積への橋は未定 |
| INT-EVID-008 | INT-CLM-008 | P1 E/J §3–4 | global Φは局所更新に非還元 | FORM NEC MECH | B1 B2 B4 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §3–4 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | global mapと局所則の関係、制御帰結 (INT-GAP-003) | INT-STRONG-005 | YES | 実数値mapとglobal役割の宣言はあるが局所則への非還元性や制御効果の独立formalizationはない |
| INT-EVID-009 | INT-CLM-009 | P1 E/J §3 | 3公理はVED/IFGTから論理的独立・意味中立 | META NEG | B0 | YES | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §3 | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | 公理の採用範囲・意味中立性とIFGTを論証前提にしない方針のsource support。形式体系間独立性定理の認定ではない |
| INT-EVID-010 | INT-CLM-010 | P1 E/J §4 | I/J/Φは投影的語彙、IFGT一般量の直接同定でない | REP XSC NEG | B0 B3 | YES | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P1 E/J §4 | 独立実証は要求scopeに含めない; §28のreference背景 | 限定scope内NONE | 専用62family対象外 | NO | projected-use/nonidentityの明示的scope guard。typed inheritanceを成立させたというYESではない |
| INT-EVID-011 | INT-CLM-011 | P1 E/J §4 | Physarum solverと語彙的/構造的対応 | HOMOLOGY CORR XSC | B3 | YES | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P1 E/J §4 | 独立実証は要求scopeに含めない; §28のreference背景 | 限定scope内NONE | INT-STRONG-054 | NO | Q/D/BCの役割対応表とstrict identity否定が、語彙的比較という限定burdenに対応 |
| INT-EVID-012 | INT-CLM-012 | P1 E/J abstract,§4–5,10 | Physarum研究はglobal Φ非還元性への独立実証的収束 | HOMOLOGY META | B3 B6 B9 | PARTIAL | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P1 E/J abstract,§4–5,10 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 比較mappingの独立評価、三条件選択の由来 (INT-GAP-005) | INT-STRONG-055 | YES | 外部研究のcitationはあるがIntのΦ非還元性を独立実証したmappingは未所在 |
| INT-EVID-013 | INT-CLM-013 | P1 E/J §5 | PhysarumとTransformerは同じ三条件を満たす | HOMOLOGY COMP XSC | B3 B9 B10 | PARTIAL | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P1 E/J §5 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 三公理・F・LE/μへの独立接続 (INT-GAP-006) | INT-STRONG-056 | YES | 両系のS/order/Φ対応を構造化。ただし同じ三条件の充足を一般性のsupportにする対応検証はない |
| INT-EVID-014 | INT-CLM-014 | P1 E/J §5 | 同一cognition/experience/functionalethicalstatusを主張しない | NEG | B0 | YES | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §5 | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | cognitive/experience/ethical identityを明示的に除外 |
| INT-EVID-015 | INT-CLM-015 | P1 E/J §6 | Gettierはstopping状態と動的性質の層間不一致 | COG CORR | B3 B4 | PARTIAL | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P1 E/J §6 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 外部問題と独自再記述を区別するcriterion (INT-GAP-007) | 専用62family対象外 | YES | Gettier引用と層間診断の解釈はある。外部事例が停止モデルを選別する独立基準はない |
| INT-EVID-016 | INT-CLM-016 | P1 E/J §6 | JTBへの静的条件追加では動的保証にならない | NEC NEG FORM | B2 B3 | PARTIAL | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P1 E/J §6 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 修正対象classと不可能性のscope (INT-GAP-008) | INT-STRONG-006 | YES | 停止/動態の区別と修復例の議論。すべての静的条件追加に対する不可能性を支える範囲は未確定 |
| INT-EVID-017 | INT-CLM-017 | P1 E/J §7 | 正しさ蓄積はconnectivity/divergenceを増やす | MECH FORM COG | B1 B4 B5 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §7 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | correctness/edge/pathのmapと実際の枝選択 (INT-GAP-009) | INT-STRONG-007 | YES | 再利用→結合→分岐の鎖を式/文章で提示。correctnessからgraph量への抽出・観測はない |
| INT-EVID-018 | INT-CLM-018 | P1 E/J §7 | 結合数二乗・経路指数の分岐爆発 | FORM MECH | B1 B4 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §7 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | correctness/edge/pathのmapと実際の枝選択 (INT-GAP-009) | INT-STRONG-008 | YES | 可能辺とb^dのcombinatorial templateはあるが現実の推論がその増殖域を取ることは別 |
| INT-EVID-019 | INT-CLM-019 | P1 E/J §7 | 知識量/推論速度/専門化/能力強化だけでは止まらない | NEC COG COMP | B2 B4 B5 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §7 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 対象architecture条件と比較結果 (INT-GAP-013) | INT-STRONG-009 | YES | 能力増加を同じbranching論に戻す。知識量・速度・専門化の比較testなし |
| INT-EVID-020 | INT-CLM-020 | P1 J §7 | overexplanation等は不安定性の4症状という読み | COG CORR | B4 B5 | PARTIAL | E1 | E1限定比較／E11予定 | P1 J §7 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | nonclinical命名を超える行動criterionと比較 (INT-GAP-010) | 専用62family対象外 | YES | 四症状は構造的例示。症状の測定・分類criterionとbranchingの独立接続なし |
| INT-EVID-021 | INT-CLM-021 | P1 E/J §8 | 個体内推論には停止演算子がない | FORM NEC COG | B2 B4 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §8 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | F/J署名、S→FP、F'条件、認知endpoint (INT-GAP-011) | INT-STRONG-010 | YES | 内部停止不在のrecursive argument、P2条件付きsketchがある。任意認知停止への移送は未支持 |
| INT-EVID-022 | INT-CLM-022 | P1 E/J §8（J詳細） | 疲労/注意/報酬/生理終了は停止でなく中断 | COG MECH NEC | B0 B4 B6 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §8（J詳細） | P1§3–5/§10（同じ公理・比較。外部citationは§28） | completion/interruptionの独立criterion (INT-GAP-012) | INT-STRONG-011 | YES | 中断/完成の定義区分と疲労等の例示。生理的終了をすべて中断と分類する独立criterionなし |
| INT-EVID-023 | INT-CLM-023 | P1 E/J §8（J強化） | paperclip/alignment問題は同じ停止不在の構造 | COMP COG XSC NEC | B4 B9 B10 | PARTIAL | E1 | E1限定比較／E11予定 | P1 E/J §8（J強化） | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 対象architecture条件と比較結果 (INT-GAP-013) | INT-STRONG-012 | YES | paperclip思考例はあるがalignment一般の失敗や同じ構造根源のInt固有testではない |
| INT-EVID-024 | INT-CLM-024 | P1 E/J §8–9 | 停止はログ・応答・合意・遅延への越境を必要とする | NEC SOCIAL | B2 B4 B7 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §8–9 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 外化機能から保証への条件/社会観測 (INT-GAP-014) | INT-STRONG-013 | YES | ログ・応答・合意・遅延の機能列挙と必要性論証。代替構成の排除や社会的測定はない |
| INT-EVID-025 | INT-CLM-025 | P1 E/J §9 | DHIは外部停止へのlocal horizon-form | DEF XSC | B0 B9 | PARTIAL | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P1 E/J §9 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 不変域、typed relation、理解criterion (INT-GAP-015) | 専用62family対象外 | YES | DHI命名は明示、VED4とのsame-boundary読みは役割対応を超えるため追加burden |
| INT-EVID-026 | INT-CLM-026 | P1 E/J §1,9 | DHIはVED4とは別の第二絶対境界でない | NEG XSC | B0 | YES | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P1 E/J §1,9 | 独立実証は要求scopeに含めない; §28のreference背景 | 限定scope内NONE | 専用62family対象外 | NO | 第二絶対境界ではないというnegative scopeを明示。horizon対応の正当化には加算しない |
| INT-EVID-027 | INT-CLM-027 | P1 E/J §9 | 外化は真理を保証せず持続/改訂可能停止を保証 | SUFF NEG SOCIAL | B4 B7 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §9 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 外化機能から保証への条件/社会観測 (INT-GAP-014) | INT-STRONG-014 | YES | 真理保証否定は支持。外化が持続/改訂可能停止を保証するpositive clauseの条件/観測はない |
| INT-EVID-028 | INT-CLM-028 | P1 E/J §9 | 推論能力/個体理解/責任の全面外化はしない | NEG COG SOCIAL PHEN | B0 | YES | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §9 | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | 能力・理解・責任の全面外化を否定する限定。責任の実証的分配は認定しない |
| INT-EVID-029 | INT-CLM-029 | P1 E/J §9 | 物理/Bio/Con/Int四層はproposed comparison、型付け移送でない | HOMOLOGY XSC NEG | B3 B9 | YES | E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P1 E/J §9 | 独立実証は要求scopeに含めない; §28のreference背景 | 限定scope内NONE | 専用62family対象外 | NO | proposed comparisonとしての四層表とno carrier/mechanism/typed translationのguardが一致 |
| INT-EVID-030 | INT-CLM-030 | P1 J §9 | 生命層はCon/Intを支える必要基盤というJA記述 | NEC XSC COG | B6 B9 B10 | PARTIAL | E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P1 J §9 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 各domainの独立criteriaとtranslation (INT-GAP-016) | INT-STRONG-015 | YES | Bioのsubstrate比較はあるがCon/Int全般に必要な基盤という証拠は別 |
| INT-EVID-031 | INT-CLM-031 | P1 E/J §1,9 | Conのfast/slow log/windowとIntの越境の相補性 | CORR XSC | B3 B8 B9 | PARTIAL | E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P1 E/J §1,9 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 各domainの独立criteriaとtranslation (INT-GAP-016) | INT-STRONG-057 | YES | Conのfast/slowとIntの外化を比較。同一構造・相補的過程のtyped/observed接続なし |
| INT-EVID-032 | INT-CLM-032 | P1 J §9; Con参照 | selfを経て未来予測・言語・社会へflowback | COG SOCIAL XSC | B4 B7 B8 B9 | PARTIAL | E1 E2 E11 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P1 J §9; Con参照 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 各domainの独立criteriaとtranslation (INT-GAP-016) | 専用62family対象外 | YES | flowbackの系列記述はあるがself/言語/社会へのtransition dynamicsはfuture |
| INT-EVID-033 | INT-CLM-033 | P1 E/J §10 | 六制約は必要で十分でない、complete/engineering/norm theoryでない | NEC NEG FUTURE | B2 B10 | PARTIAL | E0 E1 E11 | E0 definition/sketch＋E1解釈（該当時） | P1 E/J §10 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 条件の独立必要性・非自明な一般対象範囲 (INT-GAP-002) | INT-STRONG-016 | YES | complete/engineering/norm theory否定は明示。六制約の一般必要性がそれだけで支持されるわけではない |
| INT-EVID-034 | INT-CLM-034 | P1 E/J §10 | 3条件の収束は恣意性でないことの支持 | META HOMOLOGY | B3 B9 | PARTIAL | E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P1 E/J §10 | P1§3–5/§10（同じ公理・比較。外部citationは§28） | 比較mappingの独立評価、三条件選択の由来 (INT-GAP-005) | INT-STRONG-058 | YES | 外部研究の別起源はcitationで指示、三条件の選択・mapping独立性は未確認 |
| INT-EVID-035 | INT-CLM-035 | P1 E/J §10 | 外部停止・生命意識移行・社会制度・AI設計を後続へ | FUTURE SOCIAL COMP | B0 | YES | E11 | future記載のみ | P1 E/J §10 | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | 後続研究予定というsource記載のsupportのみ。予告の実現・将来成功は含めない |
| INT-EVID-036 | INT-CLM-036 | P2 J §0; E abstract | PartIIはVED差分原理から三層構造を導出すると宣言 | FORM XSC META | B1 B2 B9 | PARTIAL | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P2 J §0; E abstract | P1§8–9; P2 D/E（同じpremise/schema、非独立） | 語彙/schema再利用と導出の差 (INT-GAP-017) | INT-STRONG-017 | YES | VED語彙とemergence schemaを再利用。JAの構造的導出宣言に対応するtyped cognitive derivationは未所在 |
| INT-EVID-037 | INT-CLM-037 | P2 E/J §0,5,12 | LF/LR/LEの同時動態が個体内外部依存停止を生む | MECH COG NEC | B1 B4 B10 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §0,5,12 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | attractor存在/update/独立LE検出 (INT-GAP-021) | INT-STRONG-018 | YES | 三層と停止生成のschemaはあるが生成則・識別criterion・計算実行なし |
| INT-EVID-038 | INT-CLM-038 | P2 E/J §0 | 知性史は推論能力だけでなく停止構造の発達史 | SOCIAL CORR | B3 B7 | PARTIAL | E1 | E1限定比較／E11予定 | P2 E/J §0 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | case/史料/比較資料、社会変数の独立mapping (INT-GAP-024) | 専用62family対象外 | YES | 知性史を停止運用史として読む構造的仮説。歴史資料・比較case selectionなし |
| INT-EVID-039 | INT-CLM-039 | P2 J §0.2 | PartI四層の継承説明（JA別表physical/relational/symbolic/cognitive） | META REP | B0 B3 | UNRESOLVED | E1 | source所在; authority未確定 | P2 J §0.2 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | 再掲対象のexact artifact (INT-GAP-018) | 専用62family対象外 | YES | Part I継承とされるJA四層表がP1知覚/認識/知識/知性と異なる。継承対象のauthority未確定 |
| INT-EVID-040 | INT-CLM-040 | P2 E/J §1,10 | Cは操作的安定性で真理でない | DEF NEG | B0 | YES | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §1,10 | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | Cをoperational stability/not truthとする局所定義は明示。operationalという語は校正を意味しない |
| INT-EVID-041 | INT-CLM-041 | P2 J §1,A; E簡略 | closure PDE/basic VED formをIntで使用 | FORM XSC | B1 B9 | PARTIAL | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P2 J §1,A; E簡略 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | state/signature/IC/BC/preservationの契約 (INT-GAP-019) | INT-STRONG-019 | YES | JA closure PDEとMaster表はあるがInt state space/signature/適用条件の継承は未確定 |
| INT-EVID-042 | INT-CLM-042 | P2 E/J §1,3 | Cmax非到達と究極理解/最終判断の非到達 | FORM NEC COG XSC | B1 B2 B4 B9 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §1,3 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | 不変域、typed relation、理解criterion (INT-GAP-015) | INT-STRONG-020 | YES | barrierとnoFPの対応を提示。invariant-domainと究極理解endpointは未提示 |
| INT-EVID-043 | INT-CLM-043 | P2 E/J §1–2 | Ωθ内(A)とθ再編(B)、領域外は発散/停止 | FORM COMP | B0 B1 B3 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §1–2 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | range/parameter/observable抽出と校正 (INT-GAP-020) | INT-STRONG-021 | YES | Ωθ内A/B区分は明示。領域外の帰結と独立領域検出は未formalized |
| INT-EVID-044 | INT-CLM-044 | P2 E/J §1,E | VED-defined emergenceは下位運動+外部Hから上位動態 | DEF MECH XSC | B0 B4 B9 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §1,E | P1§8–9; P2 D/E（同じpremise/schema、非独立） | attractor存在/update/独立LE検出 (INT-GAP-021) | INT-STRONG-022 | YES | U=Φ(L,H)というlocal schemaはあるが上位生成を実現するupdate/typed bridgeとは別 |
| INT-EVID-045 | INT-CLM-045 | P2 E/J §1,B,E | Bio second-attractor予告に対するInt独自下流構成 | XSC CORR FUTURE NEG | B0 B3 | YES | E1 E2 E11 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P2 E/J §1,B,E | 独立実証は要求scopeに含めない; §28のreference背景 | 限定scope内NONE | 専用62family対象外 | NO | Bio予告とInt独自提案、not Bio-established implementationのguardが明示 |
| INT-EVID-046 | INT-CLM-046 | P2 E/J §2 | 推論Fは既存概念地形内、確率的/反復/局所正当化 | DEF COMP REP | B0 B1 B3 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §2 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | F/J署名、S→FP、F'条件、認知endpoint (INT-GAP-011) | 専用62family対象外 | YES | F性質/署名はあるがsingle-valued/set-valuedとJ適用のvariantを一律支持できない |
| INT-EVID-047 | INT-CLM-047 | P2 E/J §2,5 | Physarum/TransformerをF actionとして読む | COMP HOMOLOGY | B3 B6 B9 | PARTIAL | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P2 E/J §2,5 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | 三公理・F・LE/μへの独立接続 (INT-GAP-006) | INT-STRONG-059 | YES | 外部モデルをF actionへ読む比較。strict-J適合性や同じoperatorの測定/証明はない |
| INT-EVID-048 | INT-CLM-048 | P2 J §2 | Hij応答閾値をCij指数関係で記述 | FORM MECH | B1 B3 B11 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 J §2 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | range/parameter/observable抽出と校正 (INT-GAP-020) | INT-STRONG-023 | YES | Cij指数関係と閾値表現はある。係数・range・抽出・校正は未指定 |
| INT-EVID-049 | INT-CLM-049 | P2 E/J §2,5 | μθは内生的閾値移動・E設置領域を組み替える | DEF MECH COG | B0 B4 B5 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §2,5 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | 二endpointの独立性と能力から効果へのbridge (INT-GAP-022) | INT-STRONG-024 | YES | μの定義とB/E-site役割は明示。独立能力指標と領域再編の実装なし |
| INT-EVID-050 | INT-CLM-050 | P2 J §2,B | BioDNA長期とsapiens対話短期のθ可変性を同一原理で比較 | HOMOLOGY XSC | B3 B6 B9 | PARTIAL | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P2 J §2,B | P1§8–9; P2 D/E（同じpremise/schema、非独立） | 各domainの独立criteriaとtranslation (INT-GAP-016) | INT-STRONG-060 | YES | DNA長期とsapiens短期の表比較。same principleのtyped translation/検証なし |
| INT-EVID-051 | INT-CLM-051 | P2 E/J §3,D | P1/P2仮定下Fに内部不動点なし（定理3.1） | FORM NEC | B1 B2 | PARTIAL | E0 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §3,D | P1§8–9; P2 D/E（同じpremise/schema、非独立） | F/J署名、S→FP、F'条件、認知endpoint (INT-GAP-011) | INT-STRONG-025 | YES | strict-J/fixedθ-A下のcontradiction sketchを確認。proof/signature validityは本phase未監査のため定理認証としてYESにしない |
| INT-EVID-052 | INT-CLM-052 | P2 E/J §3; J D | 任意内部停止条件Sは推論要求へ戻る（系3.2） | FORM NEC | B2 B4 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §3; J D | P1§8–9; P2 D/E（同じpremise/schema、非独立） | F/J署名、S→FP、F'条件、認知endpoint (INT-GAP-011) | INT-STRONG-026 | YES | S→fixedpoint、F'再適用のsketchがある。停止判定と不動点の対応burdenを別途残す |
| INT-EVID-053 | INT-CLM-053 | P2 E/J §3; J D | 非閉包とCmax/VED4horizonは同型（系3.3） | HOMOLOGY ID XSC | B2 B9 | PARTIAL | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P2 E/J §3; J D | P1§8–9; P2 D/E（同じpremise/schema、非独立） | 不変域、typed relation、理解criterion (INT-GAP-015) | INT-STRONG-027 | YES | noFP/Cmax/horizon表とsketchあり。same proposition/isomorphismの定義済mapはない |
| INT-EVID-054 | INT-CLM-054 | P2 E/J §3; J D | 個体内知性完結不能、3collapse attractorsへ | NEC COG | B2 B4 B5 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §3; J D | P1§8–9; P2 D/E（同じpremise/schema、非独立） | F/J署名、S→FP、F'条件、認知endpoint (INT-GAP-011) | INT-STRONG-028 | YES | LF-only制限はあるが個体のcollapse attractor列挙への独立bridgeなし |
| INT-EVID-055 | INT-CLM-055 | P2 E/J §4 | 応答的/沈黙的世界は閾値regimeでontologyでない | DEF REP NEG | B0 B3 | YES | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §4 | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | 応答/沈黙を二ontologyではなくmodel-local閾値regimeとして区分するscopeに支持 |
| INT-EVID-056 | INT-CLM-056 | P2 E/J §4 | 沈黙世界でregress持続、branch explosionと同じ構造 | FORM HOMOLOGY COG | B2 B4 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §4 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | F/J署名、S→FP、F'条件、認知endpoint (INT-GAP-011) | INT-STRONG-029 | YES | 沈黙主体に限定した三前提とregress argument。branching同相/実際の認知発散は別burden |
| INT-EVID-057 | INT-CLM-057 | P2 E/J §4–5 | nonclosureはtraceを残しLR/LE創発へproductive | MECH | B4 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §4–5 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | attractor存在/update/独立LE検出 (INT-GAP-021) | INT-STRONG-030 | YES | trace生成からproductive nonclosureを叙述。trace保持・recursive参照・LE生成をつなぐupdateなし |
| INT-EVID-058 | INT-CLM-058 | P2 E/J §5 | LRは推論痕跡とその再帰参照、3保存様式 | DEF REP | B0 B3 | YES | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §5 | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | LR=trace＋recursive referenceというlocal definitionと保存様式の分類。各系の機構実証を含めない |
| INT-EVID-059 | INT-CLM-059 | P2 E/J §5 | LEは個体内だが外部H依存の動的stopping attractor | DEF MECH COG | B0 B1 B4 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §5 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | attractor存在/update/独立LE検出 (INT-GAP-021) | INT-STRONG-031 | YES | LEの機能定義はあるがattractorの存在・収束・停止源の独立検出なし |
| INT-EVID-060 | INT-CLM-060 | P2 E/J §5 | μθ→B→E-site projection→LRconvergence→LEの機構 | MECH COG | B1 B4 B11 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §5 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | attractor存在/update/独立LE検出 (INT-GAP-021) | INT-STRONG-032 | YES | 四stageのschematic arrowはある。実行可能生成機構/介入結果なし |
| INT-EVID-061 | INT-CLM-061 | P2 E/J §5 | Physarum autonomousenvironmentstop / Transformer injectedstop / sapiensμendo | COMP COG HOMOLOGY | B3 B5 B6 B9 | PARTIAL | E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P2 E/J §5 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | 三公理・F・LE/μへの独立接続 (INT-GAP-006) | 専用62family対象外 | YES | 三profileの比較表。PhysarumのLE自律性、Transformerの不在、sapiens内生μの共通判定法なし |
| INT-EVID-062 | INT-CLM-062 | P2 E/J §5; J B | projectionはConの第四原語を適用、心理防衛でない | XSC ID NEG | B0 B3 B9 | PARTIAL | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P2 E/J §5; J B | P1§8–9; P2 D/E（同じpremise/schema、非独立） | 同じoperator/quantityを示すtyped bridge (INT-GAP-004) | INT-STRONG-033 | YES | projectionの語彙再利用と心理防衛否定は明示。Con→E-siteの同じ演算子を保証しない |
| INT-EVID-063 | INT-CLM-063 | P2 E/J §5 | EはF反復から導出できずLEと現在stateに依存 | FORM NEC | B1 B2 B4 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §5 | P1§8–9; P2 D/E（同じpremise/schema、非独立） | attractor存在/update/独立LE検出 (INT-GAP-021) | INT-STRONG-034 | YES | E not F^kが書かれるがnon-derivabilityとLEからの作用則を独立に確立していない |
| INT-EVID-064 | INT-CLM-064 | P2 E/J §5,D | Φext≡Φnet、外部性はLEnetworkの見え方 | ID FORM SOCIAL | B1 B2 B7 B9 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §5,D | P1§8–9; P2 D/E（同じpremise/schema、非独立） | network aggregation、二対象同定、identity基準 (INT-GAP-023) | INT-STRONG-035 | YES | 二視点同定と同型sketch。独立network aggregation/対応map/社会観測なし |
| INT-EVID-065 | INT-CLM-065 | P2 E/J §5,C | P1globalΦはΦnetで具体化される | XSC META | B1 B3 B9 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §5,C | P1§8–9; P2 D/E（同じpremise/schema、非独立） | network aggregation、二対象同定、identity基準 (INT-GAP-023) | INT-STRONG-061 | YES | P1globalΦをnetworkで具体化する叙述。scalar biasからnetworkへの変換規則なし |
| INT-EVID-066 | INT-CLM-066 | P2 E/J §5,10 | stabilityはtruthでなくrecoverability/revisability | DEF NEG FUNC | B0 | YES | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §5,10 | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | stability/recoverability/revisabilityの枠組み内読解、truth保証否定は明示。測定validityは別 |
| INT-EVID-067 | INT-CLM-067 | P2 E/J §6 | animismは沈黙世界を応答的として扱う停止設置 | DEF SOCIAL MECH | B0 B4 B7 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §6 | P2§3/5/11（内部architecture、非独立） | case/史料/比較資料、社会変数の独立mapping (INT-GAP-024) | INT-STRONG-036 | YES | animismの操作的命名と例はあるが応答注入が停止を生成する社会/認知効果は未測定 |
| INT-EVID-068 | INT-CLM-068 | P2 J §6 | animism低停止コストが普遍性を説明 | MECH SOCIAL | B5 B7 B10 | NO | E1 E12 | 要求typeは未所在; E1は説明のみ | P2 J §6 | P2§3/5/11（内部architecture、非独立） | cost測定と歴史的対象範囲 (INT-GAP-025) | INT-STRONG-037 | YES | low-costの説明文はあるが普遍性を説明する比較史料・コスト測定・対象範囲のsupportなし |
| INT-EVID-069 | INT-CLM-069 | P2 E/J §7 | Godは未解決→保留演算子、中心化Φext | DEF SOCIAL MECH | B0 B4 B7 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §7 | P2§3/5/11（内部architecture、非独立） | case/史料/比較資料、社会変数の独立mapping (INT-GAP-024) | INT-STRONG-038 | YES | Godを未解決→保留と命名。実社会でその演算が働く因果supportなし |
| INT-EVID-070 | INT-CLM-070 | P2 E/J §7 | 中心化は曖昧性を減らし安定化、単一極限は歴史終点でない | SOCIAL MECH NEG | B4 B7 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §7 | P2§3/5/11（内部architecture、非独立） | case/史料/比較資料、社会変数の独立mapping (INT-GAP-024) | INT-STRONG-039 | YES | 中心化で競合が減る内部比較とnonprogress guard。一般安定性効果・歴史的endpointは実証されない |
| INT-EVID-071 | INT-CLM-071 | P2 E/J §8 | religionはLE世代維持・mixed responsive/silent境界管理 | DEF SOCIAL MECH | B0 B4 B7 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §8 | P2§3/5/11（内部architecture、非独立） | case/史料/比較資料、社会変数の独立mapping (INT-GAP-024) | INT-STRONG-040 | YES | 儀礼・伝承等を三機能へ配置する内部解釈。世代維持やcollapse予防の比較データなし |
| INT-EVID-072 | INT-CLM-072 | P2 E/J §8–9,D | scienceは停止改訂制度化、religionと真理序列でない | SOCIAL CORR NEG | B3 B7 | PARTIAL | E1 | E1限定比較／E11予定 | P2 E/J §8–9,D | P2§3/5/11（内部architecture、非独立） | case/史料/比較資料、社会変数の独立mapping (INT-GAP-024) | 専用62family対象外 | YES | 宗教/科学のtruth序列否定は明示。改訂制度化という一般社会説明への外部出典なし |
| INT-EVID-073 | INT-CLM-073 | P2 E/J §8 | 純粋因果推論は有限sapiensに不安定、病的引力子分類 | COG MECH | B4 B5 B7 | PARTIAL | E1 | E1限定比較／E11予定 | P2 E/J §8 | P2§3/5/11（内部architecture、非独立） | nonclinical命名を超える行動criterionと比較 (INT-GAP-010) | INT-STRONG-041 | YES | 有限sapiensの負荷・病的引力子の命名。nonclinical guardはあるが必要帰結/予防効果のデータなし |
| INT-EVID-074 | INT-CLM-074 | P2 E/J §9 | social blockchainは分散LE consensusでtechnicalcryptoでない | DEF SOCIAL CORR NEG | B0 B3 | YES | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §9 | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | social blockchainを非cryptoのconsensus analogyとして明示。社会機構の検証というYESではない |
| INT-EVID-075 | INT-CLM-075 | P2 E/J §9 | Gitとsocialの分岐/merge/rollback costは対称/逆 | COMP SOCIAL HOMOLOGY | B3 B7 | PARTIAL | E1 | E1限定比較／E11予定 | P2 E/J §9 | P2§3/5/11（内部architecture、非独立） | case/史料/比較資料、社会変数の独立mapping (INT-GAP-024) | 専用62family対象外 | YES | Git/社会cost対比表はある。cost単位・対象条件・社会比較結果なし |
| INT-EVID-076 | INT-CLM-076 | P2 E/J §9 | legitimacyは原理的非計算可能、継続改訂条件 | FORM SOCIAL NEC | B2 B7 | NO | E1 E12 | 要求typeは未所在; E1は説明のみ | P2 E/J §9 | P2§3/5/11（内部architecture、非独立） | 計算問題の定式化、適用仮定、formal support (INT-GAP-026) | INT-STRONG-042 | YES | 歴史依存性からprincipled noncomputabilityへの主張。計算問題/モデル/不可計算性証明support未所在 |
| INT-EVID-077 | INT-CLM-077 | P2 E/J §9 | 創造は個体でのみ、社会は事後安定化 | NEC SOCIAL COG | B4 B7 B10 | NO | E1 E12 | 要求typeは未所在; E1は説明のみ | P2 E/J §9 | P2§3/5/11（内部architecture、非独立） | 個体/集団寄与の区別と排他性のsupport (INT-GAP-027) | INT-STRONG-043 | YES | 個体創造/社会安定化の役割割当以外にonly-individualを排他的に支える証拠なし |
| INT-EVID-078 | INT-CLM-078 | P2 E/J §10 | GettierはC≠truthのevidence、原理的解決不能というJA主張 | META FORM NEC | B2 B3 B4 | PARTIAL | E0 E1 E2 | E2 citation背景＋E0/E1局所構成; exact mapping未検証 | P2 E/J §10 | P2§3/5/11（内部architecture、非独立） | 外部問題と独自再記述を区別するcriterion (INT-GAP-007) | INT-STRONG-044 | YES | Gettier問題の引用と再解釈はあるがC/LE/nonclosureの独立確証にするbridgeなし |
| INT-EVID-079 | INT-CLM-079 | P2 J §10（EN簡略） | knowledgeはaction可能なΦnet暫定block | DEF SOCIAL | B0 | YES | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 J §10（EN簡略） | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | Φnet暫定blockというJA model-local知識定義。認識論一般への証拠ではない |
| INT-EVID-080 | INT-CLM-080 | P2 J §10,D; E弱いcoupling | error toleranceとμθは構造的同値 | FORM ID NEC | B2 B4 B5 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 J §10,D; E弱いcoupling | P2§3/5/11（内部architecture、非独立） | 二endpointの独立性と能力から効果へのbridge (INT-GAP-022) | INT-STRONG-045 | YES | JA双方向sketchはある。error/threshold mobility独立endpointと必要な同値条件なし |
| INT-EVID-081 | INT-CLM-081 | P2 E/J §11 | Σ相図はvinf/rres/η、安定は狭いbandのみ | FORM COG PRED | B1 B4 B11 | PARTIAL | E0 E1 E11 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §11 | P2§3/5/11（内部architecture、非独立） | 三軸尺度、境界、量化、測定/fit (INT-GAP-028) | INT-STRONG-046 | YES | 三軸と質的領域を提示。narrow幅・境界・Σ発達量の量化/fitなし |
| INT-EVID-082 | INT-CLM-082 | P2 E/J §11 | Δvintel増大はLR/LE/μ失敗のfourfoldcollapse | MECH COG PRED | B4 B11 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §11 | P2§3/5/11（内部architecture、非独立） | 三軸尺度、境界、量化、測定/fit (INT-GAP-028) | INT-STRONG-047 | YES | Δv差と四重崩壊の順方向schema。critical値・層崩壊の検出・観測なし |
| INT-EVID-083 | INT-CLM-083 | P2 E/J §11 | zero motionは知性でなく不安定性は構成的 | DEF NEC | B0 B2 B4 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §11 | P2§3/5/11（内部architecture、非独立） | 三軸尺度、境界、量化、測定/fit (INT-GAP-028) | INT-STRONG-048 | YES | zero-motion除外はlocal definition、狭い領域と不安定性必然は定義以上 |
| INT-EVID-084 | INT-CLM-084 | P2 E/J §11 | highspeedautonomous human/AIは同じphase制約 | XSC COMP PRED | B5 B9 B11 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §11 | P2§3/5/11（内部architecture、非独立） | 対象architecture条件と比較結果 (INT-GAP-013) | 専用62family対象外 | YES | human/AIを同じ相図へ置く提案。共通尺度・同じfailure境界の検証なし |
| INT-EVID-085 | INT-CLM-085 | P2 J §12; E7clauses | N1–6 impossibilities/R1–6 necessities/S1sapiens条件 | NEC COG | B2 B4 B10 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 J §12; E7clauses | P2§3/5/11（内部architecture、非独立） | model-local naming以上の独立対象criterion (INT-GAP-029) | INT-STRONG-049 | YES | N/R/Sと七条項の整理はある。必要性のsupportは前章のpremise/schemaへ戻り、scope差も残る |
| INT-EVID-086 | INT-CLM-086 | P2 J §12; E §12 | 一般知性はLF+LR+LE、sapiensはμ移動性追加 | DEF NEC COG | B0 B2 B10 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 J §12; E §12 | P2§3/5/11（内部architecture、非独立） | model-local naming以上の独立対象criterion (INT-GAP-029) | INT-STRONG-050 | YES | 一般LF/LR/LEとsapiensμ追加の命名は明示。一般必要性を独立criterionで検証していない |
| INT-EVID-087 | INT-CLM-087 | P2 E/J §0,5,12 | 停止と可動性が自由な推論を可能にする | NEC FUNC | B4 B8 B10 | PARTIAL | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §0,5,12 | P2§3/5/11（内部architecture、非独立） | 二endpointの独立性と能力から効果へのbridge (INT-GAP-022) | INT-STRONG-051 | YES | movable stopとfree inferenceの機能関係はある。自由の独立criterion/phenomenal reportなし |
| INT-EVID-088 | INT-CLM-088 | P2 E/J §0,13 | 理論は使用法/制度正統性/倫理/AGI設計を決定しない | NEG FUTURE | B0 | YES | E0 E11 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §0,13 | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | 倫理・制度正統性・AGI設計を決定しないというnegative scope明示 |
| INT-EVID-089 | INT-CLM-089 | P2 E/J §5,13,D,E | Σ定量化・stoppingfunctional・哲学/AI実践はfuture | FUTURE FORM | B0 | YES | E11 | future記載のみ | P2 E/J §5,13,D,E | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | INT-STRONG-052 | NO | Σ量化/functional/哲学AIをfutureと明記。実行/成功を含まない |
| INT-EVID-090 | INT-CLM-090 | P2 J A; E A辞書 | Masterv2.2はv2.1継承+Int追加と宣言 | META XSC | B1 B9 | UNRESOLVED | E0 E1 | source所在; authority未確定 | P2 J A; E A辞書 | P2§13/A–E（文書/未来、非独立） | exact predecessor artifact/version (INT-GAP-030) | 専用62family対象外 | YES | v2.1再掲という記載はあるがexact Master artifact/version同一性未解決 |
| INT-EVID-091 | INT-CLM-091 | P2 J B; E B短縮 | appendixBはCTを含むnonclosure/attractor/horizon対応を拡張 | HOMOLOGY XSC | B3 B9 | YES | E1 | E1限定比較／E11予定 | P2 J B; E B短縮 | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | INT-STRONG-062 | NO | 補遺の比較拡張という記載とtyped OPEN guardに支持。同型検証への昇格は含まない |
| INT-EVID-092 | INT-CLM-092 | P2 J C; §13 | appendixCはPartIへの4微修正を提案 | META FUTURE | B0 | YES | E11 | future記載のみ | P2 J C; §13 | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | 四微修正のeditorial提案として支持。P1への実装済supportではない |
| INT-EVID-093 | INT-CLM-093 | P2 E/J E | appendixEはemergence比較とLElocalminの記述を追加 | HOMOLOGY FORM XSC | B1 B9 | UNRESOLVED | E0 E1 E11 | source所在; authority未確定 | P2 E/J E | P2§13/A–E（文書/未来、非独立） | 採用statusと未定functionalのauthority (INT-GAP-031) | INT-STRONG-053 | YES | emergence比較は所在。LE localmin現在形とbody futureの採用状態が異なり統一formal supportを決めない |
| INT-EVID-094 | INT-CLM-094 | P2 E D; revision_notes | AI costをstoppingcostとして読む | COMP CORR FUTURE | B0 B3 | YES | E1 E11 | E1限定比較／E11予定 | P2 E D; revision_notes | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | EN Dのcostを停止設計costとして読むfuture comparisonに限定した支持 |
| INT-EVID-095 | INT-CLM-095 | P2 E/J §0,8,D | NGs：religion/culture/truthhierarchy/clinicalanthropomorphism除外 | NEG META | B0 | YES | E0 E1 | E0 definition/sketch＋E1解釈（該当時） | P2 E/J §0,8,D | 独立実証は要求scopeに含めない; 同位置の定義/guard/比較 | 限定scope内NONE | 専用62family対象外 | NO | NG群とclinical/anthropomorphism等のnegative scopeを確認。肯定的mechanismのsupportへ流用しない |

## 6. Definition claims — 32 definitions

局所定義にはempirical evidenceを自動要求しない。以下は定義の所在と、説明・一般criterionへ使うときの追加burdenを分ける。DEF031のPhase00旧Σ/region表記はPhase01に従いΣ発達/activity量と三軸領域を分離する。

| ID | Definition | Current source | Source support | Related claim | Burden outside definition |
|---|---|---|---|---|---|
| INT-DEFEVID-001 | INT-DEF-001 perception=input availability | P1 §2 | model-local definition | INT-CLM-002 | 局所定義は支持。独立測定/経験criterionとはしない |
| INT-DEFEVID-002 | INT-DEF-002 recognition=existing structureへのmapping | P1 §2 | model-local definition | INT-CLM-002 | 局所定義は支持。独立測定/経験criterionとはしない |
| INT-DEFEVID-003 | INT-DEF-003 knowledge=stopping structure | P1 §2 | explanatory naming | INT-CLM-003 | 局所定義は支持。独立測定/経験criterionとはしない |
| INT-DEFEVID-004 | INT-DEF-004 intelligence=ongoing revisable motion | P1 §1–2 | model-local / explanatory definition | INT-CLM-001 | 局所定義は支持。独立測定/経験criterionとはしない |
| INT-DEFEVID-005 | INT-DEF-005 connected S | P1 §3 | formal condition | INT-CLM-006 | 局所定義は支持。独立測定/経験criterionとはしない |
| INT-DEFEVID-006 | INT-DEF-006 temporal ordering | P1 §3 | formal condition | INT-CLM-007 | 順序updateは明示されるが順序だけから履歴保持・学習的累積への橋は未定 |
| INT-DEFEVID-007 | INT-DEF-007 global Φ:S→R | P1 §3 | formal signature + global-role definition | INT-CLM-008 | 実数値mapとglobal役割の宣言はあるが局所則への非還元性や制御効果の独立formalizationはない |
| INT-DEFEVID-008 | INT-DEF-008 I accumulation density | P1 §4 | model-local projected naming | INT-CLM-010 | 局所定義は支持。独立測定/経験criterionとはしない |
| INT-DEFEVID-009 | INT-DEF-009 J direction/flow | P1 §4 | model-local projected naming | INT-CLM-010 | 局所定義は支持。独立測定/経験criterionとはしない |
| INT-DEFEVID-010 | INT-DEF-010 Φ normative-neutral bias | P1 §4 | model-local naming | INT-CLM-008 | 実数値mapとglobal役割の宣言はあるが局所則への非還元性や制御効果の独立formalizationはない |
| INT-DEFEVID-011 | INT-DEF-011 interruption vs stopping | P1 §8 | explanatory distinction, not operational test | INT-CLM-022 | 中断/完成の定義区分と疲労等の例示。生理的終了をすべて中断と分類する独立criterionなし |
| INT-DEFEVID-012 | INT-DEF-012 differential horizon of intelligence | P1 §9 | explanatory boundary naming | INT-CLM-025 | DHI命名は明示、VED4とのsame-boundary読みは役割対応を超えるため追加burden |
| INT-DEFEVID-013 | INT-DEF-013 C operational stability not truth | P2 §1 | model-local; word operational≠observable calibration | INT-CLM-040 | 局所定義は支持。独立測定/経験criterionとはしない |
| INT-DEFEVID-014 | INT-DEF-014 C-landscape (X,C) | P2 §1 | formal representation | INT-CLM-041 | JA closure PDEとMaster表はあるがInt state space/signature/適用条件の継承は未確定 |
| INT-DEFEVID-015 | INT-DEF-015 Ωθ / θ | P2 §1 | formal/model-local region | INT-CLM-043 | Ωθ内A/B区分は明示。領域外の帰結と独立領域検出は未formalized |
| INT-DEFEVID-016 | INT-DEF-016 emergence U=Φ(L,H) | P2 J definition1.1; E§1 | model-local definition; crossdomainanalogy | INT-CLM-044 | U=Φ(L,H)というlocal schemaはあるが上位生成を実現するupdate/typed bridgeとは別 |
| INT-DEFEVID-017 | INT-DEF-017 inference F / LF | P2 §2 | formal/operator and model-local layer; JA2.1 | INT-CLM-046 | F性質/署名はあるがsingle-valued/set-valuedとJ適用のvariantを一律支持できない |
| INT-DEFEVID-018 | INT-DEF-018 justification J:X→R | P2 E §2; J §3 | formal premise | INT-CLM-051 | strict-J/fixedθ-A下のcontradiction sketchを確認。proof/signature validityは本phase未監査のため定理認証としてYESにしない |
| INT-DEFEVID-019 | INT-DEF-019 μθ threshold mobility | P2 J2.3; E§1,2 | model-local ability definition | INT-CLM-049 | μの定義とB/E-site役割は明示。独立能力指標と領域再編の実装なし |
| INT-DEFEVID-020 | INT-DEF-020 movement A/B | P2 §2 | model-local classification | INT-CLM-043 | Ωθ内A/B区分は明示。領域外の帰結と独立領域検出は未formalized |
| INT-DEFEVID-021 | INT-DEF-021 responsive/silent worlds | P2 §4 | model-local regimes | INT-CLM-055 | 局所定義は支持。独立測定/経験criterionとはしない |
| INT-DEFEVID-022 | INT-DEF-022 LR=trace + recursive reference | P2 J5.1; E§5 | model-local definition | INT-CLM-058 | 局所定義は支持。独立測定/経験criterionとはしない |
| INT-DEFEVID-023 | INT-DEF-023 LE=externally dependent stopping attractor | P2 J5.2 / E5.1 | model-local definition; numbering differs | INT-CLM-059 | LEの機能定義はあるがattractorの存在・収束・停止源の独立検出なし |
| INT-DEFEVID-024 | INT-DEF-024 external E | P2 J5.3; E§5 | formal schematic operator | INT-CLM-063 | E not F^kが書かれるがnon-derivabilityとLEからの作用則を独立に確立していない |
| INT-DEFEVID-025 | INT-DEF-025 Φext / Φnet | P2 §5 | representational identification / network naming | INT-CLM-064 | 二視点同定と同型sketch。独立network aggregation/対応map/社会観測なし |
| INT-DEFEVID-026 | INT-DEF-026 animism | P2 J6.1; E§6 | explanatory naming | INT-CLM-067 | animismの操作的命名と例はあるが応答注入が停止を生成する社会/認知効果は未測定 |
| INT-DEFEVID-027 | INT-DEF-027 God: unresolved→suspended | P2 J7.1; E§7 | explanatory operator naming | INT-CLM-069 | Godを未解決→保留と命名。実社会でその演算が働く因果supportなし |
| INT-DEFEVID-028 | INT-DEF-028 religion | P2 §8 | social maintenance naming | INT-CLM-071 | 儀礼・伝承等を三機能へ配置する内部解釈。世代維持やcollapse予防の比較データなし |
| INT-DEFEVID-029 | INT-DEF-029 social blockchain | P2 §9 | conceptual analogy / consensus naming | INT-CLM-074 | 局所定義は支持。独立測定/経験criterionとはしない |
| INT-DEFEVID-030 | INT-DEF-030 knowledge provisional block | P2 J10.1 | social model-local redefinition | INT-CLM-079 | 局所定義は支持。独立測定/経験criterionとはしない |
| INT-DEFEVID-031 | INT-DEF-031 Σ / speed-resolution-stiffness | P2 §11,A | E0/E1: Σは量化future、三軸は質的 | INT-CLM-081 | 三軸と質的領域を提示。narrow幅・境界・Σ発達量の量化/fitなし |
| INT-DEFEVID-032 | INT-DEF-032 general vs sapiens intelligence | P2 §12 | necessary-condition / functional definition | INT-CLM-086 | 一般LF/LR/LEとsapiensμ追加の命名は明示。一般必要性を独立criterionで検証していない |

## 7. Theorem evidence — THM001–013

proof sourceの存在とvalidityを分離。前提のsource supportはassumption/定義としての所在であり実際の認知系で成立するというsupportではない。全行proof validity audited?: NO。

| ID | THM / statement | Premise support | Proof source / type | Formal burden | Additional evidence burden | Support | Proof validity audited? |
|---|---|---|---|---|---|---|---|
| INT-THMEVID-001 | INT-THM-001 Non-Closure Theorem3.1 | P1 justificationextension;P2 strictJ; scopeP3fixedθ/A：source-local premise、外部成立未検証 | P2 EN/JA§3; J D.1; contradiction sketch | B1/B2; INT-GAP-011 | 固定θ/A条件を超える認知停止criterionは別 | PARTIAL | NO |
| INT-THMEVID-002 | INT-THM-002 internal stoppingpredicate cor3.2 | T3.1; hypotheticalS; stopjudgment→fixedpoint; S-as-F'：source-local premise、外部成立未検証 | P2 J§3,D.2; EN§3Consequence; prose argument / contradiction sketch | B1/B2; INT-GAP-011 | 認知/社会/他domainの対応はE0からは追加支持されない | PARTIAL | NO |
| INT-THMEVID-003 | INT-THM-003 Cmax/horizonisomorphism cor3.3 | barrierdivergence+claimedunreachability;T3.1;cor3.2：source-local premise、外部成立未検証 | P2 J§3,D.3; table + prose argument | B1/B2; INT-GAP-015 | 認知/社会/他domainの対応はE0からは追加支持されない | PARTIAL | NO |
| INT-THMEVID-004 | INT-THM-004 individualclosure cor3.4 | T3.1+cor3.2; LF-onlyscope：source-local premise、外部成立未検証 | P2 J§3,D.4; EN§3; prose argument | B1/B2; INT-GAP-011 | 認知/社会/他domainの対応はE0からは追加支持されない | PARTIAL | NO |
| INT-THMEVID-005 | INT-THM-005 VEDemergence definition1.1 three-caseverification | lowerLmotion+H; particle/Bio/Intcases：source-local premise、外部成立未検証 | P2 J§1,D.5,E; appendix-only comparison sketch | B1/B2; INT-GAP-021 | 認知/社会/他domainの対応はE0からは追加支持されない | PARTIAL | NO |
| INT-THMEVID-006 | INT-THM-006 Φext≡Φnet claim5.4 | functionalexternalview;networkofindividualLE：source-local premise、外部成立未検証 | P2§5; JA D.6,A; prose argument / appendix sketch | B1/B2; INT-GAP-023 | 認知/社会/他domainの対応はE0からは追加支持されない | PARTIAL | NO |
| INT-THMEVID-007 | INT-THM-007 three-layer architecture cor5.5 | LFnonclosure; LRtrace; LEexternallydependent：source-local premise、外部成立未検証 | P2 J§5; EN§5summary; prose argument | B1/B2; INT-GAP-021 | 認知/社会/他domainの対応はE0からは追加支持されない | PARTIAL | NO |
| INT-THMEVID-008 | INT-THM-008 error tolerance↔μθ equivalence | μ=endogenousθchange; revisable stop：source-local premise、外部成立未検証 | P2 J§10,D.7; two-direction prose sketch | B1/B2; INT-GAP-022 | 認知/社会/他domainの対応はE0からは追加支持されない | PARTIAL | NO |
| INT-THMEVID-009 | INT-THM-009 LElocalminimum stoppingfunctional | energy/attractorcomparison; functionalnotexplicit：source-local premise、外部成立未検証 | P2 JA E; §13future; appendix-only assertion | B1/B2; INT-GAP-031 | 未定functionalとbody future/appendix assertionのauthority | UNRESOLVED | NO |
| INT-THMEVID-010 | INT-THM-010 Σ/speed phase-regime necessity | vinf,rres,eta; internal/externalstop; μroles：source-local premise、外部成立未検証 | P2§11–12; prose argument | B1/B2; INT-GAP-028 | 認知/社会/他domainの対応はE0からは追加支持されない | PARTIAL | NO |
| INT-THMEVID-011 | INT-THM-011 P1nointernalstop/differentialhorizon | inference/correctness expansion; Rboundary：source-local premise、外部成立未検証 | P1§8–9; prose argument | B1/B2; INT-GAP-014 | 認知/社会/他domainの対応はE0からは追加支持されない | PARTIAL | NO |
| INT-THMEVID-012 | INT-THM-012 threshold-dependent dichotomy claim2.2 | Hparameter + (vinf,rres,eta), same environment：source-local premise、外部成立未検証 | P2J§2.6:118;§4.3;EN§4prose; prose argument | B1/B2; INT-GAP-020 | 認知/社会/他domainの対応はE0からは追加支持されない | PARTIAL | NO |
| INT-THMEVID-013 | INT-THM-013 silent-world regress conditional | no response; justificationonlyinference; noinferredstop：source-local premise、外部成立未検証 | P2J§4.4:65–79;EN§4; prose argument | B1/B2; INT-GAP-011 | 認知/社会/他domainの対応はE0からは追加支持されない | PARTIAL | NO |

## 8. Non-closure theorem burden

| Component | Source | Formal support | Cognitive bridge | Empirical / operational | Gap |
|---|---|---|---|---|---|
| strict-J conditional noFP | P2§2–3; AJD.1 | E0: strict increaseとcontradiction sketch | 条件付きF/Jの定義に限定 | Int-linked test/map未所在 | signatureとproof validityは未監査。一般停止の証拠でない |
| internal S impossible | P2§3; AJD.2 | E0: S=1→F(x)=xとF'再帰sketch | no further need / fixedpointの同定が追加 | 独立stop criterion未所在 | INT-GAP-011 |
| individual cognitive closure impossible | P1§8; P2§3; AJD.4 | LF-only corollaryとscope guard | LFから個体の一般停止への解釈 | 個体の停止/中断を独立同定するdatasetなし | 三層全体の外部依存停止を排除する定理ではない |
| external stopping necessity | P1§9; P2§3,5 | 内部から来ない→外側の論述 | 外側をLE/log/socialへ具体化 | 代替architecture排除/実行なし | INT-GAP-014/021 |
| Cmax/horizon isomorphism | P2§1,3; AJD.3 | E0/E1 barrier/対応表 | 究極理解をclosure境界に対応 | 理解endpoint/typed mapなし | INT-GAP-015 |

Phase03が条件付きstrict-Jの帰結をdefinitional/conditional readingとして分けたことは引き継ぐが、ここでは新たな証明判定を行わない。Jの正当化はtruthやperformance scoreではない。EN set-valued FとJ適用、JA P3のfixedθ/A限定は保持する。

## 9. Three axioms burden

| Component | Source | Present support | Required beyond current scope | Status |
|---|---|---|---|---|
| connected state space | P1§3 | E0 discrete reachability定義 | 採用されたlocal conditionにempirical test不要 | YES (local) |
| temporal ordering | P1§3 | E0 update template | 履歴累積/適応へのprocess条件 | PARTIAL |
| global Φ | P1§3–5 | E0 scalar-map; E1 role; E2背景 | global biasから非還元制御への形式関係 | PARTIAL |
| joint necessity | P1§3 table/fig2 | 欠如すると退化するモデル例 | 一般必要性の対象範囲と独立burden | PARTIAL |
| lower bound | P1§3,10 | not sufficient/not complete guard | guardは全系のnecessary lower boundを証明しない | PARTIAL |
| cross-domain recurrence | P1§5 | E1 three-property table; E2二領域引用 | mapping自体の独立検証 | PARTIAL |
| non-arbitrariness | P1§4,10 | 異なる研究起源のcitation | 独自枠組みへの選択・写像と独立確認の区別 | PARTIAL |

## 10. Physarum evidence

| ID | Target | Source | Present support | Independence / evidence limitation | Burden |
|---|---|---|---|---|---|
| INT-PHYS-EVID-001 | maze/path behavior | P1§1,4,5 | E2 Nakagaki2000 | 外部観察のsource内紹介のみ。元データをrepoで再解析していない | B6; exact Int criterion未対応 |
| INT-PHYS-EVID-002 | rhythmic protoplasm | P1§5 | E2 Kobayashi2006 | 外部数理モデル紹介、Int独自time/order実証ではない | B3/B6 |
| INT-PHYS-EVID-003 | flow reinforcement/decay | P1§4–5 | E0 quoted relation + E2 Tero2007 | solver式の再掲とIntモデルのsimulationを分離 | B1/B6 |
| INT-PHYS-EVID-004 | Q/D/BC→J/I/Φ | P1§4 table | E1＋上記E2 | 語彙/役割表はある。校正・typed transformationなし | B3/B9 |
| INT-PHYS-EVID-005 | global Φ irreducibility | P1J§4.4,§5 | E1/E2 | 外部BCモデルの存在はInt Φの非還元性を直接試験しない | B2/B9 |
| INT-PHYS-EVID-006 | three-axiom mapping | P1§5 | E1 comparison | S/order/Φに整理する手続きは記述的。Int-specific detectionなし | B3/B10 |
| INT-PHYS-EVID-007 | independent empirical convergence | P1abstract,§10 | E2 origin＋E1 reading | 別起源の研究とmappingの独立性を分離。公理の制作過程は未確定 | B9 |
| INT-PHYS-EVID-008 | LE/μ profile | P2§5,6; B | E1; P1 citations indirect | 環境log/自律LE/固定μのprofileを直接測定するcitation/データなし | B4/B6; general intelligenceへは追加burden |

## 11. Transformer evidence

| ID | Target | Source | Present support | Independence / evidence limitation | Burden |
|---|---|---|---|---|---|
| INT-TR-EVID-001 | attention/layer architecture | P1§5 | E2 Vaswani2017＋E0 notation | architectureのsource説明はある。元論文の全仕様検証は未実施 | B3 |
| INT-TR-EVID-002 | ordered hidden-state update | P1§5 | E0/E1 | layer orderをphysical timeと区別。Int dynamicsの実行結果ではない | B1/B3 |
| INT-TR-EVID-003 | training distribution/weights as Φtr | P1§5 | E1/E2 | loss・学習済構造をscalar/globalbiasに対応。calibrationなし | B3/B9 |
| INT-TR-EVID-004 | three axioms/intelligence-like | P1§5 | E1 table | 心理/経験identity否定を保持。三公理一般必要性のtestではない | B9/B10 |
| INT-TR-EVID-005 | frozen weights/context logs | P2§5 | E1 architecture profile | 訓練log/volatile contextの区分は命名。LR同定法はなし | B3 |
| INT-TR-EVID-006 | no own LE / EOS/task stop | P2§5 | E1 | EOS/decoding/taskの例はsource内にあるがLE不在の独立criterionなし | B2/B4 |
| INT-TR-EVID-007 | autonomy/safety extrapolation | P1§8;P2§11 | E1/E11 | thought experimentとphase hypothesis、AI benchmark未所在 | B5/B9/B11 |

## 12. Gettier evidence

| ID | Target | Source | Present support | Independence / evidence limitation | Burden |
|---|---|---|---|---|---|
| INT-GETTIER-EVID-001 | philosophical cases | P1J§6;P1§1 | E2 Gettier1963 | 外部哲学的反例の紹介。human response datasetではない | B3 |
| INT-GETTIER-EVID-002 | stopped state / dynamic property | P1§2,6 | E0/E1 interpretation | 定義からの再解釈と外部問題の存在を分離 | B3/B4 |
| INT-GETTIER-EVID-003 | C not truth | P2§1,10 | E0 local definition; E1 Gettier use | 定義自体はsupportあり。GettierをCの実証とするmapはない | B0→B3 |
| INT-GETTIER-EVID-004 | nonclosure confirmation | P2§10 | E1 plus indirect E2 | C/停止として読んだ同じ例を第一中心の独立確認へ戻せない | B2/B3 |
| INT-GETTIER-EVID-005 | LE architecture confirmation | P2§10 | E1 plus indirect E2 | 事例はLEを独立検出せず、三層の選別を行わない | B4 |
| INT-GETTIER-EVID-006 | principled insolubility | P1J§6;P2J§10 | E0/E1 prose argument | 修復例/哲学的背景からすべての解法不可能性を認証しない | B2 |

## 13. LE emergence evidence

| ID | Target | Source | Present support | Independence / evidence limitation | Burden |
|---|---|---|---|---|---|
| INT-LE-EVID-001 | LR traces | P2§5 | E0 definition/E1 examples | trace所在とrecursive referenceの機能命名 | B0支持、保持過程B4は未実装 |
| INT-LE-EVID-002 | H dependence | P2§1,5 | E0 U=Φ(L,H) schema | 入力/出力の型と生成operator未指定 | B1/B4 |
| INT-LE-EVID-003 | μ causes B | P2§5 | E0 arrow/E1 four-stage prose | 再構成能力の命名と更新mechanismの区別 | B4 |
| INT-LE-EVID-004 | E-site projection | P2§5 | E1 Con-projection comparison | domain/site detectionやprojection実装なし | B3/B4 |
| INT-LE-EVID-005 | LR convergence | P2§5,D,E | E0 arrow/E1 assertion | 収束mode・conditions・実行なし | B1/B4 |
| INT-LE-EVID-006 | LE attractor | P2§5,E | E0 functional naming | stopping functionalをbodyはfutureと明示 | B1; authority差保持 |
| INT-LE-EVID-007 | external E | P2§5 | E0 E=E[LE,x],not F^k | action/update derivationなし | B1/B2/B4 |
| INT-LE-EVID-008 | three profiles | P2§5 table/fig5 | E1; P1 E2 indirect | 環境/Transformer/sapiensの分類は独立LE検証ではない | B5/B6/B9 |

## 14. μθ evidence

| ID | Target | Source | Present support | Independence / evidence limitation | Burden |
|---|---|---|---|---|---|
| INT-MU-EVID-001 | threshold mobility | P2§2 | E0 model-local definition | 操作的能力名で数値単位/尺度未提示 | B0 versus B11 |
| INT-MU-EVID-002 | reconfiguration | P2§2,5 | E0/E1 A/B distinction | Bを実装するupdate mapなし | B1/B4 |
| INT-MU-EVID-003 | sapiens endogenous status | P2§5,12 | E1 profile | 定義上同じとのJA明示。比較生物/認知測定なし | B6/B10 |
| INT-MU-EVID-004 | error tolerance equivalence | P2J§10,D.7 | E0 two-direction sketch | 二endpointがrevisabilityを共有。独立metricなし | B2/B5 |
| INT-MU-EVID-005 | freedom | P2§5,12 | E1 functional account | 行為能力/自由感の区別、report基準未提示 | B4/B8 |
| INT-MU-EVID-006 | phase recovery | P2§11 | E1 phase interpretation | 復帰trajectory・recovery測定・数値境界なし | B5/B11 |
| INT-MU-EVID-007 | Bio θ comparison | P2§2,B | E1 same-series comparison | DNA/生物longtermとdialogue短期のmapなし | B6/B9 |

## 15. Φext / Φnet evidence

| ID | Target | Source | Present support | Independence / evidence limitation | Burden |
|---|---|---|---|---|---|
| INT-PHINET-EVID-001 | external reference definition | P2§5,D.6 | E0/E1 | 機能的命名は存在、測定場ではない | B0 |
| INT-PHINET-EVID-002 | network interpretation | P2§5 | E1 diagram/network prose | 個体LEのnode/edge抽出とaggregation modelなし | B3/B7 |
| INT-PHINET-EVID-003 | identity/isomorphism | P2§5,D.6 | E0 sketch/E1 two views | 同じ停止relationの二視点を超える独立mapなし | B1/B2/B9 |
| INT-PHINET-EVID-004 | P1 Φ refinement | P2§5,C | E1 documentary refinement | P1 scalarbias→networkの実装・typed conversionなし | B1/B3 |
| INT-PHINET-EVID-005 | social reference function | P2§6–10 | E1 norms/God/value examples | network data・coupling simulation・independent社会endpointなし | B7 |

## 16. Branching explosion evidence

| ID | Target | Source | Present support | Independence / evidence limitation | Burden |
|---|---|---|---|---|---|
| INT-BRANCH-EVID-001 | possible edges/path growth | P1§7 | E0 \|E\|~\|V\|² and b^d | 条件付きcombinatorial templateの所在。実現graphデータではない | B1 |
| INT-BRANCH-EVID-002 | correctness→connectivity | P1§7 | E1 reuse argument | correctnessと実辺の抽出mapなし | B3/B5 |
| INT-BRANCH-EVID-003 | connectivity→branching | P1§7 | E0/E1 | 可能枝と実際に探索した枝を分離する証拠なし | B1/B4 |
| INT-BRANCH-EVID-004 | branching→symptoms | P1J§7;P2§3,11 | E1 symptom examples | 心理/clinical guardあり、behavior dataなし | B4/B5 |
| INT-BRANCH-EVID-005 | branching→no stopping | P1§7–8;P2§3 | E0/E1 | internalstop定義へのbridgeに依存 | B2/B4 |
| INT-BRANCH-EVID-006 | figure4 curves | P1fig4/§7 | E1 SVG/PNG schema | データ点・run provenanceなし。数式growthの図示をsimulation結果に数えない | B11未充足 |

## 17. Phase diagram evidence

| ID | Target | Source | Present support | Independence / evidence limitation | Burden |
|---|---|---|---|---|---|
| INT-PHASE-EVID-001 | vinf/vLR | P2§11 | E0 verbal rates | per-unit-timeの名はあるが測定単位・推論step抽出なし | B11 |
| INT-PHASE-EVID-002 | rres | P2§11 | E1 finer distinctions | resolution scale/estimator未提示 | B11 |
| INT-PHASE-EVID-003 | η | P2§11 | E1 stopping hardness | hardness測定・calibration・thresholdなし | B11 |
| INT-PHASE-EVID-004 | Δvintel | P2§11 | E0 difference | 差の定義は数値入力や共通clockの確定でない | B1/B11 |
| INT-PHASE-EVID-005 | stable narrow band | P2§11 fig8 | E1 schematic band | 測定幅・数値境界・fitなし | B5/B11 |
| INT-PHASE-EVID-006 | rigid/divergent regions | P2§11 | E1 named regimes | 分類器・境界抽出・独立検証なし | B4/B11 |
| INT-PHASE-EVID-007 | fourfold collapse | P2§11 | E1 chained mechanism | time series・parameter sweep・executionなし | B4/B11 |
| INT-PHASE-EVID-008 | human/AI and Σ | P2§11–13,A | E1/E11 | human/AI共通calibrationなし。Σは発達/activity量で定量化future | B9/B11 |

## 18. Social / historical evidence

| ID | Target | Source | Present support | Independence / evidence limitation | Burden |
|---|---|---|---|---|---|
| INT-SOC-EVID-001 | animism installation | P2§6 | E0 naming/E1 examples | 山/川などの例はcase-study dataでない | B7 |
| INT-SOC-EVID-002 | low cost / universality | P2J§6.4 | E1/E12 | anthropology/history citation・cost比較なし | B7/B10 support NO |
| INT-SOC-EVID-003 | God / compression | P2§7 | E0 naming/E1 network comparison | 独立社会map・history dataなし | B4/B7 |
| INT-SOC-EVID-004 | centralization / ambiguity | P2§7 | E1 definition-based contrast | nonprogress guardあり。安定性差の測定なし | B7 |
| INT-SOC-EVID-005 | religion / generations | P2§8 | E1 ritual/transmission narrative | 実践名はあるが資料選択・比較・効果検証なし | B4/B7 |
| INT-SOC-EVID-006 | science / revision | P2§8–9,D | E1 conceptual comparison | 科学史recordを用いた検証なし | B7 |
| INT-SOC-EVID-007 | social blockchain / Git | P2§9 | E0 analogy/E1 cost table | 技術protocolと社会正統性は別。社会datasetなし | B3/B7 |
| INT-SOC-EVID-008 | legitimacy | P2§9 | E1/E12 | 受容史の叙述は不可計算性proofでもdataでもない | B2/B7 support NO |
| INT-SOC-EVID-009 | individual creativity only | P2§9 | E1/E12 | 社会を安定化と定義した役割分業以上の排他証拠なし | B4/B7/B10 support NO |
| INT-SOC-EVID-010 | historical order / institutions | P2§7–9 fig7 | E1 structural-order guard | 時間的進歩をsourceは否定。図の階段をhistoriography evidenceにしない | B7 |

## 19. Phenomenal / subjective evidence

| ID | Target | Source | Present support | Independence / evidence limitation | Burden |
|---|---|---|---|---|---|
| INT-PHEN-EVID-001 | felt understanding | P2§13; P1§5 | E11/negative scope | understandingは哲学層へ。独立felt reportのtestなし | B8 direct support未所在 |
| INT-PHEN-EVID-002 | freedom | P2§5,12 | E1 functional interpretation | 持続可能推論とsubjective freedomは同じ測度でない | B8未充足 |
| INT-PHEN-EVID-003 | responsibility | P1§9;P2§6 | E1 social role | 社会分担から主観的責任経験へのmapなし | B7/B8 |
| INT-PHEN-EVID-004 | cognitive burden | P1J§7;P2§8 | E1 examples | 経験語/負荷名は測定済endpointでない | B5/B8 |
| INT-PHEN-EVID-005 | conscious access | P1§9;P2§5,B | E1/E2 Con comparison | companion語彙はInt-specific phenomenal dataでない | B8/B9 |
| INT-PHEN-EVID-006 | subjectivity/meaning | P1scope;P2§13 | E11 | futureのみ。phenomenal explanation認定なし | B8 |

## 20. Biological evidence

| ID | Target | Source | Present support | Independence / evidence limitation | Burden |
|---|---|---|---|---|---|
| INT-BIO-EVID-001 | Physarum observation | P1§5 | E2 Nakagaki2000 | 本文が外部観察を指示。repo直接測定0 | B6: background only |
| INT-BIO-EVID-002 | Physarum models | P1§4–5 | E2 Kobayashi2006/Tero2007 | quoted equationsとInt mappingのvalidation別 | B3/B6 |
| INT-BIO-EVID-003 | Bio-IFGT comparison | P1§9;P2B/E | E1/E2 same-series | Bio closure/実装結果をIntへ転送しない | B9 |
| INT-BIO-EVID-004 | life substrate | P1J§9 | E1/E2 | 生命が全Intに必要との一般化は別burden | B6/B10 |
| INT-BIO-EVID-005 | evolution θ / second attractor | P2§2,5,B,E | E0/E1/E2 | longterm/body parameterとLE同定のmapなし | B6/B9 |
| INT-BIO-EVID-006 | physiological interruption | P1§8 | E1 examples | 疲労・reward等の例は記録された生理testでない | B6 |

## 21. AI / LLM — all nine families

| ID | Phase00 AI | Source / target | Present evidence | Missing / scope |
|---|---|---|---|---|
| INT-AI-EVID-001 | INT-AI-001 | P1 §5 Transformer hidden layers/attention/trainingloss | E0/E1/E2 Vaswani2017 | 3axiomssatisfied; computationalhomology; not literalcognition/experience; Int-specific benchmark/map/data未所在 |
| INT-AI-EVID-002 | INT-AI-002 | P1 §7 moreknowledge/reasoning/speed/specialization | E1 comparison/thought experiment | categorical nonremedy forstopping; notempiricalbenchmarkinventory; Int-specific benchmark/map/data未所在 |
| INT-AI-EVID-003 | INT-AI-003 | P1 §8 paperclip/Bostrom/alignment | E1 comparison/thought experiment | structuralroot; JA六十年/誤った応答のstrongclaim; Bostrom bibkeynotlocated; externalfactnotverified; Int-specific benchmark/map/data未所在 |
| INT-AI-EVID-004 | INT-AI-004 | P1 J §8 artificialsystemswithoutBiointerruptions | E1 comparison/thought experiment | inferencecontinuesresourcespermitting; sourceclaimnotmodernAIknowledge; Int-specific benchmark/map/data未所在 |
| INT-AI-EVID-005 | INT-AI-005 | P1 §10 externalstopdesign futurePartII | E1/E11 future | futureengineeringdirection; noimplementation authorized; Int-specific benchmark/map/data未所在 |
| INT-AI-EVID-006 | INT-AI-006 | P2 §2,5 Transformer LF/weights/context/EOS | E1 comparison/thought experiment | no ownLE; stopinjectedtask/decoding; architectureprofile vs P1lowerbound; Int-specific benchmark/map/data未所在 |
| INT-AI-EVID-007 | INT-AI-007 | P2 §11 highspeedautonomoussystem | E1 comparison/thought experiment | qualitativeinstabilitysamephasehuman/AI; no AGIdesignendorsement; Int-specific benchmark/map/data未所在 |
| INT-AI-EVID-008 | INT-AI-008 | P2 E D; source_md/revision_notes AIcost | E1/E11 future | stoppingdesigncost beyondcompute/electricity; conceptualfuturecomparison; Int-specific benchmark/map/data未所在 |
| INT-AI-EVID-009 | INT-AI-009 | P2 §0,13 AI implementation/ethicsnonintervention | E0/E11 negative scope | negative scope; no AGI blueprint / normative decision; Int-specific benchmark/map/data未所在 |

## 22. Homology — all 21 families

source/targetが別領域で独立に研究されていることと、Intが提案する両者のhomologyが独立に確かめられたことを分ける。全21familyについて、mapping test・invariant measurement・独立replication未所在。一般的な同型の真偽は判定しない。

| ID | HOMO | Source / relation | Preserved role claimed | Types | Domain independence | Source guard / formal status | Mapping evidence |
|---|---|---|---|---|---|---|---|
| INT-HOMOEVID-001 | INT-HOMO-001 | P1 §4 Tero Q,D,reinforcement,BC → J,I,projection,Φ | flow/log/bias; I0/I1 | E0/E1/E2（Physarum/Transformer citations） | 外部領域研究の出典あり; exact mappingは内部比較 | lexicaltable explicit; invertibletypedmap未提示; citesTero2007; currentJA+EN | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-002 | INT-HOMO-002 | P1 §5 Physarum ↔ Transformer | S/order/Φ三公理; I1/I2 | E0/E1/E2（Physarum/Transformer citations） | 外部領域研究の出典あり; exact mappingは内部比較 | 3propertycomparison; inverse未提示; namedliterature; no cognitiveidentityguard | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-003 | INT-HOMO-003 | P1 §9 VED4DH ↔ Int localhorizon | unreachability/divergence/finiteabsorption; I0/I2 | E1（same-series; P1 cited時E2） | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | descriptiverole; inverse/invariant未指定; VEDVol4cite | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-004 | INT-HOMO-004 | P1 §9 physical ↔ Bio ↔ Con ↔ Int | fourlayerroles; I0/I2/I4/I3 | E1（same-series; P1 cited時E2） | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | table/fig5; no sharedcarrier/mechanism/typedmapguard | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-005 | INT-HOMO-005 | P1 J §8 paperclip ↔ individual nonclosure | nointernalstop; I1/I2 | E1 | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | structuralanalogy strongrootlanguage; no commonstate mapping | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-006 | INT-HOMO-006 | P2 §3,D nonfixedF ↔ Cmax ↔ DH | nonclosure; I0/I2 | E1 | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | same structure/isomorphism, proofsketchcrosswalk nottypedbijective map | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-007 | INT-HOMO-007 | P2 §4 regress ↔ branching | sameinferenceextension; I0/I2 | E1 | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | qualitativestructure; invariant未指定 | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-008 | INT-HOMO-008 | P2 §1,E physicalparticle ↔ life ↔ LE | lower motion+H→upperattractor; I0/I2 | E1 | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | U=Φ(L,H)schematic; no typedinverse; appendixevidenceはsource-localcomparison | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-009 | INT-HOMO-009 | P2 J B.1 CT ↔ physical/Bio/Con/Int | closure/attractor/horizon/branching; I0/I1/I2/I4 | E1（same-series; P1 cited時E2） | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | CTcolumnJAonly; no CTversion/operationalmap | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-010 | INT-HOMO-010 | P2 J B.2 / fig5 threeemergencecases | particle/life/stopping; I0/I2 | E1 | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | guardedformalroles; no mechanismidentity | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-011 | INT-HOMO-011 | P2 §5,B.3 Conprojection ↔ IntE-siteprojection ↔ psychprojection | projection role; I1/I2/I4 | E1（same-series; P1 cited時E2） | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | definitionapplicationlanguage、psych用語guard; commonoperator未定義 | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-012 | INT-HOMO-012 | P2 J §2,B.4 DNAθ ↔ Intθ ↔ sapiensμ | constraintmobility; I0/I2 | E1 | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | time-scalecomparison; sameprinciplewording; no domain/codomainmap | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-013 | INT-HOMO-013 | P2 §2,B.5 BioF ↔ inferenceF | localstateevolution role; I0/I1 | E1（same-series; P1 cited時E2） | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | explicitsource-localtypingguard; sameglyphnotsharedvectorfield | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-014 | INT-HOMO-014 | P2 §5,B.6 Physarum/Transformer/sapiens | LF/LR/LEstorage/μprofiles; I1/I2 | E1 | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | tablecomparisons; empiricaldatasetnotlocatedinbranch | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-015 | INT-HOMO-015 | P2 §6–9,B.6 animism/God/religion/socialBC | LEinstallation/compression/maintenance/sync; I2/I3 | E1 | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | historicaloperatingforms; notlinearprogressguard | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-016 | INT-HOMO-016 | P2 §9 Git ↔ socialBC | branch/merge/rollback vsconsensus; I1/I3 | E1 | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | costcontrast ratherthan literalprotocolisomorphism | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-017 | INT-HOMO-017 | P2 §5,D Φext ↔ Φnet | same stopping relation external/internalview; I0/I3 | E0/E1（JA D sketch） | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | equivalence sign/proofsketch; no explicitinverse/map signature | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-018 | INT-HOMO-018 | P2 J §10,D error tolerance ↔ μθ | revisability/endogenousmovement; I0/I2 | E0/E1（JA D sketch） | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | bidirectionalsketchpresent; independentcriterionnotfixedhere | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-019 | INT-HOMO-019 | P2 §11 ConΔv ↔ IntΔvintel | speedgap/logtracking; I0/I2/I4 | E1（same-series; P1 cited時E2） | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | analogousdifference; sameclock/unitnotstated | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-020 | INT-HOMO-020 | P2 B/E/fig9 physics/Bio/Con/Int/social | nonclosure→attractor→sustaineddynamics; I0–I4 | E1（same-series; P1 cited時E2） | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | proposedcomparison guards; ENE samegrammarwordingretained | mapping/invariantの独立test未所在 |
| INT-HOMOEVID-021 | INT-HOMO-021 | P2 J E VEDemergence ↔ weak/strong/holistic/functional emergence | dynamicrelationalposition; I0/I2 | E1（same-series; P1 cited時E2） | 領域別sourceとの比較。domain研究の妥当性は本auditへ輸入しない | conceptcomparison; notnewexternalempiricalsupport | mapping/invariantの独立test未所在 |

## 23. Authority / EN–JA burden asymmetry

ENの穏当な表現でJA primaryの強いclaimを消さず、JAの追加式/sketchでENの不足を黙って埋めない。

| Variant | Source | Support / authority consequence |
|---|---|---|
| P1 Physarum convergence | P1J§4.4/abstract versus E§4–5 | JAの『独立な実証で確認』はmapping支持以上。Eのnot-final-proof guardもexact mappingの検証にはならない |
| P1 Gettier | P1J§6 versus E§6 | JAの詳細修復史とprincipled impossibilityは追加burden。Gettier1件のcitationで全修復史を裏付けない |
| P1 four symptoms/Bio substrate | P1J§7,9 | JA追加の認知・基盤必要性は外部観測として数えない |
| P2 theorem/corollaries | P2J§3,D versus E§3 | JA追加sketchはE0増分、E3/E7増分ではない |
| P2 closure/Cij | P2J§1–2 versus E§1–2 | JA追加式はformal supportだがcalibration・typed bridgeではない |
| P2 μ equivalence | P2J§10,D.7 versus E§10 | JA同値とENcouplingを分離。SERIOUS004のindependent endpoints未所在 |
| P2 social history | P2J§6–9 versus E短縮 | 詳細さは史料supportではない。nonprogress/NG guardと強い普遍説明を両記 |
| P1/P2四層・Master | P2J§0.2,A | CLM039/090はauthority uncertaintyを優先しUNRESOLVED |
| LE local minimum | P2§5/13 future versus E appendix | CLM093はpresent/future採用status UNRESOLVED。定義不足を文章で修復しない |

## 24. Strong-language burden — 62/62

SUPPORTEDは当該語のlocal scope、OVERSTATEDは対応するsupport typeを超える強さ、POSSIBLY OVERSTATEDは条件/定義読みに依存、GUARDEDはfuture/analogy限定が明示、VERSION-SPECIFICは言語差が中心、UNRESOLVEDは採用authority未確定。これらはrevision dispositionではない。

| ID | Phase00 strong family | Claim | Source / wording | Burden status | Current support / missing burden |
|---|---|---|---|---|---|
| INT-STRONG04-001 | INT-STRONG-001 | INT-CLM-004 | P1 E/J §2; continually produces / not stored — 知性は全層を横断し知識を産出・改訂、保存されない | POSSIBLY OVERSTATED | 産出・改訂・保存不能の機能記述はあるが全層を横断する過程の独立同定はない |
| INT-STRONG04-002 | INT-STRONG-002 | INT-CLM-005 | P1 E/J §3,10; necessary / lower bound — 3公理は同時必要な下限、完全理論でない | OVERSTATED | 三条件と欠如例の表はある。intelligence-like限定とnot sufficientを保っても共同必要性の一般burdenは残る |
| INT-STRONG04-003 | INT-STRONG-003 | INT-CLM-006 | P1 E/J §3; connected, not necessarily continuous — connected state spaceは連続空間に限定しない | SUPPORTED AT CURRENT STRENGTH | 離散的reachabilityを許すconnectednessの局所定義。連続位相不要というscopeのみ |
| INT-STRONG04-004 | INT-STRONG-004 | INT-CLM-007 | P1 E/J §3; requires / update — temporal orderingで履歴変化が蓄積する | POSSIBLY OVERSTATED | 順序updateは明示されるが順序だけから履歴保持・学習的累積への橋は未定 |
| INT-STRONG04-005 | INT-STRONG-005 | INT-CLM-008 | P1 E/J §3–4; irreducible — global Φは局所更新に非還元 | OVERSTATED | 実数値mapとglobal役割の宣言はあるが局所則への非還元性や制御効果の独立formalizationはない |
| INT-STRONG04-006 | INT-STRONG-006 | INT-CLM-016 | P1 E/J §6; cannot guarantee — JTBへの静的条件追加では動的保証にならない | OVERSTATED | 停止/動態の区別と修復例の議論。すべての静的条件追加に対する不可能性を支える範囲は未確定 |
| INT-STRONG04-007 | INT-STRONG-007 | INT-CLM-017 | P1 E/J §7; increases / generates — 正しさ蓄積はconnectivity/divergenceを増やす | OVERSTATED | 再利用→結合→分岐の鎖を式/文章で提示。correctnessからgraph量への抽出・観測はない |
| INT-STRONG04-008 | INT-STRONG-008 | INT-CLM-018 | P1 E/J §7; structural not contingent — 結合数二乗・経路指数の分岐爆発 | POSSIBLY OVERSTATED | 可能辺とb^dのcombinatorial templateはあるが現実の推論がその増殖域を取ることは別 |
| INT-STRONG04-009 | INT-STRONG-009 | INT-CLM-019 | P1 E/J §7; does not solve — 知識量/推論速度/専門化/能力強化だけでは止まらない | OVERSTATED | 能力増加を同じbranching論に戻す。知識量・速度・専門化の比較testなし |
| INT-STRONG04-010 | INT-STRONG-010 | INT-CLM-021 | P1 E/J §8; no stopping operator — 個体内推論には停止演算子がない | OVERSTATED | 内部停止不在のrecursive argument、P2条件付きsketchがある。任意認知停止への移送は未支持 |
| INT-STRONG04-011 | INT-STRONG-011 | INT-CLM-022 | P1 E/J §8（J詳細）; all / すべて中断 — 疲労/注意/報酬/生理終了は停止でなく中断 | POSSIBLY OVERSTATED | 中断/完成の定義区分と疲労等の例示。生理的終了をすべて中断と分類する独立criterionなし |
| INT-STRONG04-012 | INT-STRONG-012 | INT-CLM-023 | P1 E/J §8（J強化）; structural root / 誤っている — paperclip/alignment問題は同じ停止不在の構造 | OVERSTATED | paperclip思考例はあるがalignment一般の失敗や同じ構造根源のInt固有testではない |
| INT-STRONG04-013 | INT-STRONG-013 | INT-CLM-024 | P1 E/J §8–9; requires / 必然 — 停止はログ・応答・合意・遅延への越境を必要とする | OVERSTATED | ログ・応答・合意・遅延の機能列挙と必要性論証。代替構成の排除や社会的測定はない |
| INT-STRONG04-014 | INT-STRONG-014 | INT-CLM-027 | P1 E/J §9; does not guarantee truth / guarantees — 外化は真理を保証せず持続/改訂可能停止を保証 | OVERSTATED | 真理保証否定は支持。外化が持続/改訂可能停止を保証するpositive clauseの条件/観測はない |
| INT-STRONG04-015 | INT-STRONG-015 | INT-CLM-030 | P1 J §9; 構造的事実 — 生命層はCon/Intを支える必要基盤というJA記述 | VERSION-SPECIFIC | Bioのsubstrate比較はあるがCon/Int全般に必要な基盤という証拠は別 |
| INT-STRONG04-016 | INT-STRONG-016 | INT-CLM-033 | P1 E/J §10; necessary not sufficient — 六制約は必要で十分でない、complete/engineering/norm theoryでない | POSSIBLY OVERSTATED | complete/engineering/norm theory否定は明示。六制約の一般必要性がそれだけで支持されるわけではない |
| INT-STRONG04-017 | INT-STRONG-017 | INT-CLM-036 | P2 J §0; E abstract; 構造的に導出 / develops — PartIIはVED差分原理から三層構造を導出すると宣言 | VERSION-SPECIFIC | VED語彙とemergence schemaを再利用。JAの構造的導出宣言に対応するtyped cognitive derivationは未所在 |
| INT-STRONG04-018 | INT-STRONG-018 | INT-CLM-037 | P2 E/J §0,5,12; emerges / 同時 — LF/LR/LEの同時動態が個体内外部依存停止を生む | OVERSTATED | 三層と停止生成のschemaはあるが生成則・識別criterion・計算実行なし |
| INT-STRONG04-019 | INT-STRONG-019 | INT-CLM-041 | P2 J §1,A; E簡略; VED基本式 — closure PDE/basic VED formをIntで使用 | POSSIBLY OVERSTATED | JA closure PDEとMaster表はあるがInt state space/signature/適用条件の継承は未確定 |
| INT-STRONG04-020 | INT-STRONG-020 | INT-CLM-042 | P2 E/J §1,3; unreachable / 構造的禁止 — Cmax非到達と究極理解/最終判断の非到達 | OVERSTATED | barrierとnoFPの対応を提示。invariant-domainと究極理解endpointは未提示 |
| INT-STRONG04-021 | INT-STRONG-021 | INT-CLM-043 | P2 E/J §1–2; movement region — Ωθ内(A)とθ再編(B)、領域外は発散/停止 | POSSIBLY OVERSTATED | Ωθ内A/B区分は明示。領域外の帰結と独立領域検出は未formalized |
| INT-STRONG04-022 | INT-STRONG-022 | INT-CLM-044 | P2 E/J §1,E; not deduced from lower alone — VED-defined emergenceは下位運動+外部Hから上位動態 | GUARDED | U=Φ(L,H)というlocal schemaはあるが上位生成を実現するupdate/typed bridgeとは別 |
| INT-STRONG04-023 | INT-STRONG-023 | INT-CLM-048 | P2 J §2; 式 / threshold — Hij応答閾値をCij指数関係で記述 | POSSIBLY OVERSTATED | Cij指数関係と閾値表現はある。係数・range・抽出・校正は未指定 |
| INT-STRONG04-024 | INT-STRONG-024 | INT-CLM-049 | P2 E/J §2,5; not mere flexibility — μθは内生的閾値移動・E設置領域を組み替える | POSSIBLY OVERSTATED | μの定義とB/E-site役割は明示。独立能力指標と領域再編の実装なし |
| INT-STRONG04-025 | INT-STRONG-025 | INT-CLM-051 | P2 E/J §3,D; Theorem / proof sketch — P1/P2仮定下Fに内部不動点なし（定理3.1） | POSSIBLY OVERSTATED | strict-J/fixedθ-A下のcontradiction sketchを確認。proof/signature validityは本phase未監査のため定理認証としてYESにしない |
| INT-STRONG04-026 | INT-STRONG-026 | INT-CLM-052 | P2 E/J §3; J D; no internal S — 任意内部停止条件Sは推論要求へ戻る（系3.2） | OVERSTATED | S→fixedpoint、F'再適用のsketchがある。停止判定と不動点の対応burdenを別途残す |
| INT-STRONG04-027 | INT-STRONG-027 | INT-CLM-053 | P2 E/J §3; J D; isomorphism / 同型 — 非閉包とCmax/VED4horizonは同型（系3.3） | OVERSTATED | noFP/Cmax/horizon表とsketchあり。same proposition/isomorphismの定義済mapはない |
| INT-STRONG04-028 | INT-STRONG-028 | INT-CLM-054 | P2 E/J §3; J D; cannot / inevitable — 個体内知性完結不能、3collapse attractorsへ | OVERSTATED | LF-only制限はあるが個体のcollapse attractor列挙への独立bridgeなし |
| INT-STRONG04-029 | INT-STRONG-029 | INT-CLM-056 | P2 E/J §4; continues indefinitely — 沈黙世界でregress持続、branch explosionと同じ構造 | POSSIBLY OVERSTATED | 沈黙主体に限定した三前提とregress argument。branching同相/実際の認知発散は別burden |
| INT-STRONG04-030 | INT-STRONG-030 | INT-CLM-057 | P2 E/J §4–5; because / generates — nonclosureはtraceを残しLR/LE創発へproductive | POSSIBLY OVERSTATED | trace生成からproductive nonclosureを叙述。trace保持・recursive参照・LE生成をつなぐupdateなし |
| INT-STRONG04-031 | INT-STRONG-031 | INT-CLM-059 | P2 E/J §5; Definition / arises — LEは個体内だが外部H依存の動的stopping attractor | POSSIBLY OVERSTATED | LEの機能定義はあるがattractorの存在・収束・停止源の独立検出なし |
| INT-STRONG04-032 | INT-STRONG-032 | INT-CLM-060 | P2 E/J §5; emergence mechanism — μθ→B→E-site projection→LRconvergence→LEの機構 | OVERSTATED | 四stageのschematic arrowはある。実行可能生成機構/介入結果なし |
| INT-STRONG04-033 | INT-STRONG-033 | INT-CLM-062 | P2 E/J §5; J B; definition itself / not psychological — projectionはConの第四原語を適用、心理防衛でない | POSSIBLY OVERSTATED | projectionの語彙再利用と心理防衛否定は明示。Con→E-siteの同じ演算子を保証しない |
| INT-STRONG04-034 | INT-STRONG-034 | INT-CLM-063 | P2 E/J §5; E not F^k — EはF反復から導出できずLEと現在stateに依存 | POSSIBLY OVERSTATED | E not F^kが書かれるがnon-derivabilityとLEからの作用則を独立に確立していない |
| INT-STRONG04-035 | INT-STRONG-035 | INT-CLM-064 | P2 E/J §5,D; equivalent / 同型命題5.4 — Φext≡Φnet、外部性はLEnetworkの見え方 | OVERSTATED | 二視点同定と同型sketch。独立network aggregation/対応map/社会観測なし |
| INT-STRONG04-036 | INT-STRONG-036 | INT-CLM-067 | P2 E/J §6; installation / 状態変換 — animismは沈黙世界を応答的として扱う停止設置 | POSSIBLY OVERSTATED | animismの操作的命名と例はあるが応答注入が停止を生成する社会/認知効果は未測定 |
| INT-STRONG04-037 | INT-STRONG-037 | INT-CLM-068 | P2 J §6; 低コスト / 普遍性 — animism低停止コストが普遍性を説明 | OVERSTATED | low-costの説明文はあるが普遍性を説明する比較史料・コスト測定・対象範囲のsupportなし |
| INT-STRONG04-038 | INT-STRONG-038 | INT-CLM-069 | P2 E/J §7; is / Definition7.1 — Godは未解決→保留演算子、中心化Φext | POSSIBLY OVERSTATED | Godを未解決→保留と命名。実社会でその演算が働く因果supportなし |
| INT-STRONG04-039 | INT-STRONG-039 | INT-CLM-070 | P2 E/J §7; reduces / not progress — 中心化は曖昧性を減らし安定化、単一極限は歴史終点でない | POSSIBLY OVERSTATED | 中心化で競合が減る内部比較とnonprogress guard。一般安定性効果・歴史的endpointは実証されない |
| INT-STRONG04-040 | INT-STRONG-040 | INT-CLM-071 | P2 E/J §8; three functions — religionはLE世代維持・mixed responsive/silent境界管理 | POSSIBLY OVERSTATED | 儀礼・伝承等を三機能へ配置する内部解釈。世代維持やcollapse予防の比較データなし |
| INT-STRONG04-041 | INT-STRONG-041 | INT-CLM-073 | P2 E/J §8; unstable / prevents・buffer — 純粋因果推論は有限sapiensに不安定、病的引力子分類 | OVERSTATED | 有限sapiensの負荷・病的引力子の命名。nonclinical guardはあるが必要帰結/予防効果のデータなし |
| INT-STRONG04-042 | INT-STRONG-042 | INT-CLM-076 | P2 E/J §9; cannot be computed — legitimacyは原理的非計算可能、継続改訂条件 | OVERSTATED | 歴史依存性からprincipled noncomputabilityへの主張。計算問題/モデル/不可計算性証明support未所在 |
| INT-STRONG04-043 | INT-STRONG-043 | INT-CLM-077 | P2 E/J §9; only / 社会では起こらない — 創造は個体でのみ、社会は事後安定化 | OVERSTATED | 個体創造/社会安定化の役割割当以外にonly-individualを排他的に支える証拠なし |
| INT-STRONG04-044 | INT-STRONG-044 | INT-CLM-078 | P2 E/J §10; confirms / 原理的に不可能 — GettierはC≠truthのevidence、原理的解決不能というJA主張 | OVERSTATED | Gettier問題の引用と再解釈はあるがC/LE/nonclosureの独立確証にするbridgeなし |
| INT-STRONG04-045 | INT-STRONG-045 | INT-CLM-080 | P2 J §10,D; E弱いcoupling; equivalent / 双方向sketch — error toleranceとμθは構造的同値 | VERSION-SPECIFIC | JA双方向sketchはある。error/threshold mobility独立endpointと必要な同値条件なし |
| INT-STRONG04-046 | INT-STRONG-046 | INT-CLM-081 | P2 E/J §11; only narrow band — Σ相図はvinf/rres/η、安定は狭いbandのみ | OVERSTATED | 三軸と質的領域を提示。narrow幅・境界・Σ発達量の量化/fitなし |
| INT-STRONG04-047 | INT-STRONG-047 | INT-CLM-082 | P2 E/J §11; collapse / 連鎖 — Δvintel増大はLR/LE/μ失敗のfourfoldcollapse | OVERSTATED | Δv差と四重崩壊の順方向schema。critical値・層崩壊の検出・観測なし |
| INT-STRONG04-048 | INT-STRONG-048 | INT-CLM-083 | P2 E/J §11; not intelligence / constitutive — zero motionは知性でなく不安定性は構成的 | POSSIBLY OVERSTATED | zero-motion除外はlocal definition、狭い領域と不安定性必然は定義以上 |
| INT-STRONG04-049 | INT-STRONG-049 | INT-CLM-085 | P2 J §12; E7clauses; cannot / requires — N1–6 impossibilities/R1–6 necessities/S1sapiens条件 | VERSION-SPECIFIC | N/R/Sと七条項の整理はある。必要性のsupportは前章のpremise/schemaへ戻り、scope差も残る |
| INT-STRONG04-050 | INT-STRONG-050 | INT-CLM-086 | P2 J §12; E §12; final constructive statement — 一般知性はLF+LR+LE、sapiensはμ移動性追加 | OVERSTATED | 一般LF/LR/LEとsapiensμ追加の命名は明示。一般必要性を独立criterionで検証していない |
| INT-STRONG04-051 | INT-STRONG-051 | INT-CLM-087 | P2 E/J §0,5,12; free inference requires movable stopping — 停止と可動性が自由な推論を可能にする | POSSIBLY OVERSTATED | movable stopとfree inferenceの機能関係はある。自由の独立criterion/phenomenal reportなし |
| INT-STRONG04-052 | INT-STRONG-052 | INT-CLM-089 | P2 E/J §5,13,D,E; future work — Σ定量化・stoppingfunctional・哲学/AI実践はfuture | GUARDED | Σ量化/functional/哲学AIをfutureと明記。実行/成功を含まない |
| INT-STRONG04-053 | INT-STRONG-053 | INT-CLM-093 | P2 E/J E; same grammar / proposedtypedOPEN — appendixEはemergence比較とLElocalminの記述を追加 | UNRESOLVED | emergence比較は所在。LE localmin現在形とbody futureの採用状態が異なり統一formal supportを決めない |
| INT-STRONG04-054 | INT-STRONG-054 | INT-CLM-011 | P1 §4; same structure / not strict mathematical isomorphism | GUARDED | Q/D/BCの役割対応表とstrict identity否定が、語彙的比較という限定burdenに対応 |
| INT-STRONG04-055 | INT-STRONG-055 | INT-CLM-012 | P1 abstract,§4–5,10; independent empirical line / 独立な実証 | OVERSTATED | 外部研究のcitationはあるがIntのΦ非還元性を独立実証したmappingは未所在 |
| INT-STRONG04-056 | INT-STRONG-056 | INT-CLM-013 | P1 §5; both satisfy / 同一条件 | POSSIBLY OVERSTATED | 両系のS/order/Φ対応を構造化。ただし同じ三条件の充足を一般性のsupportにする対応検証はない |
| INT-STRONG04-057 | INT-STRONG-057 | INT-CLM-031 | P1 §1,9; different projections of the same structure | POSSIBLY OVERSTATED | Conのfast/slowとIntの外化を比較。同一構造・相補的過程のtyped/observed接続なし |
| INT-STRONG04-058 | INT-STRONG-058 | INT-CLM-034 | P1 §10; convergence supports non-arbitrary conditions | POSSIBLY OVERSTATED | 外部研究の別起源はcitationで指示、三条件の選択・mapping独立性は未確認 |
| INT-STRONG04-059 | INT-STRONG-059 | INT-CLM-047 | P2 §2,5; Physarum flow as F action itself | POSSIBLY OVERSTATED | 外部モデルをF actionへ読む比較。strict-J適合性や同じoperatorの測定/証明はない |
| INT-STRONG04-060 | INT-STRONG-060 | INT-CLM-050 | P2 J §2,B; 同じ原理でDNAと知性のθ可変性を統一 | VERSION-SPECIFIC | DNA長期とsapiens短期の表比較。same principleのtyped translation/検証なし |
| INT-STRONG04-061 | INT-STRONG-061 | INT-CLM-065 | P2 §5,C; P1 global Φ refined / concretized as network | POSSIBLY OVERSTATED | P1globalΦをnetworkで具体化する叙述。scalar biasからnetworkへの変換規則なし |
| INT-STRONG04-062 | INT-STRONG-062 | INT-CLM-091 | P2 J B; same structures across domains / guarded homology | GUARDED | 補遺の比較拡張という記載とtyped OPEN guardに支持。同型検証への昇格は含まない |

## 25. Claim/evidence gap families

31 gap familiesは同一missing burdenを束ねたもの。70 non-YES claimsへの主gap割当で、claim数と同じではない。severityはLOW=局所的表示、MEDIUM=scope/authority/documentary、HIGH=主要claimへの型/観測不足、CRITICAL=中心的説明・普遍的formal強度に対し要求support typeが欠けるもの。CRITICAL≠false/invalid。

| ID | Severity | Mismatch | Required burden | Source | Missing support | Primary linked claims |
|---|---|---|---|---|---|---|
| INT-GAP-001 | MEDIUM | 局所定義から一般産出/保存不能へ | B0→B4 | P1§2 | 機能命名以上の過程同定 | INT-CLM-004 |
| INT-GAP-002 | HIGH | 三公理・六制約の必要性/下限 | B2 B10 | P1§3,10 | 条件の独立必要性・非自明な一般対象範囲 | INT-CLM-005, INT-CLM-007, INT-CLM-033 |
| INT-GAP-003 | HIGH | global Φの非還元性と制御 | B1 B2 B4 | P1§3–5 | global mapと局所則の関係、制御帰結 | INT-CLM-008 |
| INT-GAP-004 | HIGH | projection/同記号の型継承 | B3 B9 | P1§4;P2§5,B | 同じoperator/quantityを示すtyped bridge | INT-CLM-062 |
| INT-GAP-005 | HIGH | 外部研究からInt固有empirical convergenceへ | B6 B9 | P1§4–5,10 | 比較mappingの独立評価、三条件選択の由来 | INT-CLM-012, INT-CLM-034 |
| INT-GAP-006 | HIGH | Transformer/Physarum/profile対応 | B3 B5 B9 | P1§5;P2§2,5 | 三公理・F・LE/μへの独立接続 | INT-CLM-013, INT-CLM-047, INT-CLM-061 |
| INT-GAP-007 | CRITICAL | GettierからC/LE/nonclosureの確証へ | B3 B4 | P1§6;P2§10 | 外部問題と独自再記述を区別するcriterion | INT-CLM-015, INT-CLM-078 |
| INT-GAP-008 | HIGH | 静的JTB修正すべての排除 | B2 | P1§6 | 修正対象classと不可能性のscope | INT-CLM-016 |
| INT-GAP-009 | HIGH | graph増殖を正しさ/認知不停止へ | B1 B4 B5 | P1§7 | correctness/edge/pathのmapと実際の枝選択 | INT-CLM-017, INT-CLM-018 |
| INT-GAP-010 | HIGH | 症状・負荷・collapse/予防効果 | B4 B5 | P1J§7;P2§3,8,11 | nonclinical命名を超える行動criterionと比較 | INT-CLM-020, INT-CLM-073 |
| INT-GAP-011 | CRITICAL | 条件付きnoFPから任意認知停止排除へ | B2 B4 | P1§8;P2§2–4,D | F/J署名、S→FP、F'条件、認知endpoint | INT-CLM-021, INT-CLM-046, INT-CLM-051, INT-CLM-052, INT-CLM-054, INT-CLM-056 |
| INT-GAP-012 | HIGH | 生理的終了をすべて中断へ | B4 B6 | P1§8 | completion/interruptionの独立criterion | INT-CLM-022 |
| INT-GAP-013 | HIGH | 能力強化/AI/humanへ同一failure一般化 | B5 B9 B10 | P1§7–8;P2§11 | 対象architecture条件と比較結果 | INT-CLM-019, INT-CLM-023, INT-CLM-084 |
| INT-GAP-014 | HIGH | 外化が停止・持続・改訂を保証 | B4 B7 | P1§8–9 | 外化機能から保証への条件/社会観測 | INT-CLM-024, INT-CLM-027 |
| INT-GAP-015 | HIGH | Cmax/horizon/究極理解の同型 | B1 B2 B4 B9 | P2§1,3,D | 不変域、typed relation、理解criterion | INT-CLM-025, INT-CLM-042, INT-CLM-053 |
| INT-GAP-016 | HIGH | Bio/Con/Intの必要基盤・移行 | B6 B8 B9 | P1§9;P2§2,B,E | 各domainの独立criteriaとtranslation | INT-CLM-030, INT-CLM-031, INT-CLM-032, INT-CLM-050 |
| INT-GAP-017 | HIGH | VEDから三層の導出宣言 | B1 B2 B9 | P2J§0,1 | 語彙/schema再利用と導出の差 | INT-CLM-036 |
| INT-GAP-018 | MEDIUM | P1四層継承のauthority差 | B0 B3 | P2J§0.2;P1§2 | 再掲対象のexact artifact | INT-CLM-039 |
| INT-GAP-019 | HIGH | closure PDEのInt適用 | B1 B9 | P2J§1,A | state/signature/IC/BC/preservationの契約 | INT-CLM-041 |
| INT-GAP-020 | HIGH | 閾値領域/Cijのformal-operational対応 | B1 B3 B11 | P2§1–4 | range/parameter/observable抽出と校正 | INT-CLM-043, INT-CLM-048 |
| INT-GAP-021 | CRITICAL | LR/HからLEを生成し停止を供給 | B1 B4 | P2§5,D,E | attractor存在/update/独立LE検出 | INT-CLM-037, INT-CLM-044, INT-CLM-057, INT-CLM-059, INT-CLM-060, INT-CLM-063 |
| INT-GAP-022 | HIGH | μ/error tolerance/自由の同値と効果 | B2 B4 B8 | P2§2,10–12,D | 二endpointの独立性と能力から効果へのbridge | INT-CLM-049, INT-CLM-080, INT-CLM-087 |
| INT-GAP-023 | CRITICAL | Φext≡ΦnetとglobalΦ具体化 | B1 B2 B7 B9 | P2§5,C,D | network aggregation、二対象同定、identity基準 | INT-CLM-064, INT-CLM-065 |
| INT-GAP-024 | HIGH | 社会・歴史の機構的再解釈 | B4 B7 | P2§6–9 | case/史料/比較資料、社会変数の独立mapping | INT-CLM-038, INT-CLM-067, INT-CLM-069, INT-CLM-070, INT-CLM-071, INT-CLM-072, INT-CLM-075 |
| INT-GAP-025 | HIGH | animism低cost→普遍性 | B7 B10 | P2J§6.4 | cost測定と歴史的対象範囲 | INT-CLM-068 |
| INT-GAP-026 | CRITICAL | legitimacyの原理的非計算可能性 | B2 B7 | P2§9 | 計算問題の定式化、適用仮定、formal support | INT-CLM-076 |
| INT-GAP-027 | HIGH | 創造は個体でのみ | B4 B7 B10 | P2§9 | 個体/集団寄与の区別と排他性のsupport | INT-CLM-077 |
| INT-GAP-028 | HIGH | 相図の狭い帯・閾値・fourfold collapse | B1 B4 B11 | P2§11–13,A | 三軸尺度、境界、量化、測定/fit | INT-CLM-081, INT-CLM-082, INT-CLM-083 |
| INT-GAP-029 | HIGH | 一般知性/サピエンスの必要条件 | B2 B10 | P2§5,12 | model-local naming以上の独立対象criterion | INT-CLM-085, INT-CLM-086 |
| INT-GAP-030 | MEDIUM | Master v2.1/v2.2 provenance | B1 B9 | P2A | exact predecessor artifact/version | INT-CLM-090 |
| INT-GAP-031 | MEDIUM | LE local minimumの現在形/future差 | B1 | P2§5,13,E | 採用statusと未定functionalのauthority | INT-CLM-093 |

## 26. Evidence ceilings

0=no support; 1=source-internal qualitative; 2=structured/formal comparison; 3=external observational/literature support; 4=operationally tested; 5=independently validated/replicated。これは今回のburden ceilingで、CTのCE2等やPhase05 correspondence scaleとは別である。

| Domain | Frozen Phase04 ceiling | What reaches ceiling | What does NOT follow |
|---|---|---|---|
| Formal | FE2 | definitions/equations/conditional sketches/structured tables | proof validity/well-posedness/typed derivationの認証ではない |
| Cognitive | CE2 | LF/LR/LE、停止・閾値・相図の構造化された仮説 | 認知機構測定・行動test未所在 |
| Social | SE2 | 命名を整理した構造比較/運用profile | 歴史的説明・一般社会法則まで達しない |
| Biological | BE3 (citation background only) | P1の外部Physarum観察/モデルへの出典 | Int-specific biological mappingのceilingは2。repo独立生物測定を意味しない |
| Phenomenal | PE1 | free inference/負荷等のqualitative interpretation | report/experienceの独立criterion未所在。phenomenal empirical support 0 |
| Cross-domain/homology | XE2 | 表・役割・sketch比較 | 二領域の外部出典からmapping独立検証は導かれない |
| Predictive | PRE2 | 変数名を伴う構造比較・定性的条件方向 | 数値境界・executable protocol・予測testなし |
| Operational | OE0 | 明示calibration/extraction/estimator未所在 | observable候補名・式・operationalという語はE9でない |

社会領域はconceptual reinterpretationを構造化したcomparative historical hypothesisまでであり、出典に基づくhistorical explanationやgeneral social lawのsupportには達していない。historicalという対象名でE5へ昇格しない。BE3は他者研究をsourceが引用する狭い範囲に限るため、CE/XE/全体Int empirical statusを3へ上げない。全domain level4/5は未所在。

## 27. Evidence artifact inventory / deduplication

artifactは独立証拠数ではなく、support provenanceを追跡するdocumentary unitである。textは同じsectionのEN/JAを1bundle（ただし内容同一視しない）、figureはEN/JAと複数formatを1family、文献は同じkeyを1entryとして数える。30 text bundles＋14 figure families＋13 citation references＝57 units。definitions32、EQF63、theorems13は所在textへのclaim linksであり、追加独立artifactに数えない。各unitに複数EタグがありE別件数は合算不可。summary/appendixによる再述は非独立と明記する。E12はabsence/rhetoricラベルなので正のartifact数0。

| ART | Source unit | Exact EN / JA paths | Types present | Claim links | Independence |
|---|---|---|---|---|---|
| INT-ART-001 | P1 abstract | intelligence-part1/sections/abstract.tex; intelligence-part1/sections_ja/abstract_ja.tex | E1 | INT-CLM-001, INT-CLM-012 | same-source; main/summary/appendix非独立 |
| INT-ART-002 | P1 §1 | intelligence-part1/sections/01_introduction.tex; intelligence-part1/sections_ja/01_introduction_ja.tex | E1 | INT-CLM-001, INT-CLM-009, INT-CLM-010, INT-CLM-012, INT-CLM-026, INT-CLM-031 | same-source; main/summary/appendix非独立 |
| INT-ART-003 | P1 §2 | intelligence-part1/sections/02_the_decomposition_perception_recognition_knowledge_and_intelligence.tex; intelligence-part1/sections_ja/02_the_decomposition_perception_recognition_knowledge_and_intelligence_ja.tex | E0 E1 | INT-CLM-001, INT-CLM-002, INT-CLM-003, INT-CLM-004 | same-source; main/summary/appendix非独立 |
| INT-ART-004 | P1 §3 | intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex; intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex | E0 E1 | INT-CLM-005, INT-CLM-006, INT-CLM-007, INT-CLM-008, INT-CLM-009 | same-source; main/summary/appendix非独立 |
| INT-ART-005 | P1 §4 | intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex; intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex | E0 E1 | INT-CLM-008, INT-CLM-010, INT-CLM-011, INT-CLM-012 | same-source; main/summary/appendix非独立 |
| INT-ART-006 | P1 §5 | intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex; intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex | E0 E1 | INT-CLM-012, INT-CLM-013, INT-CLM-014 | same-source; main/summary/appendix非独立 |
| INT-ART-007 | P1 §6 | intelligence-part1/sections/06_the_gettier_problem_as_a_structural_diagnostic.tex; intelligence-part1/sections_ja/06_the_gettier_problem_as_a_structural_diagnostic_ja.tex | E1 | INT-CLM-003, INT-CLM-015, INT-CLM-016 | same-source; main/summary/appendix非独立 |
| INT-ART-008 | P1 §7 | intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex; intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex | E0 E1 | INT-CLM-017, INT-CLM-018, INT-CLM-019, INT-CLM-020 | same-source; main/summary/appendix非独立 |
| INT-ART-009 | P1 §8 | intelligence-part1/sections/08_the_non_closure_of_individual_intelligence.tex; intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex | E0 E1 | INT-CLM-021, INT-CLM-022, INT-CLM-023, INT-CLM-024 | same-source; main/summary/appendix非独立 |
| INT-ART-010 | P1 §9 | intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex; intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex | E0 E1 | INT-CLM-024, INT-CLM-025, INT-CLM-026, INT-CLM-027, INT-CLM-028, INT-CLM-029, INT-CLM-030, INT-CLM-031, INT-CLM-032 | same-source; main/summary/appendix非独立 |
| INT-ART-011 | P1 §10 | intelligence-part1/sections/10_summary_convergence_and_outlook.tex; intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex | E1 E11 | INT-CLM-005, INT-CLM-012, INT-CLM-033, INT-CLM-034, INT-CLM-035 | same-source; main/summary/appendix非独立 |
| INT-ART-012 | P2 §0 | intelligence-part2/sections/00_introduction.tex; intelligence-part2/sections/00_introduction_ja.tex | E0 E1 | INT-CLM-036, INT-CLM-037, INT-CLM-038, INT-CLM-039, INT-CLM-087, INT-CLM-088, INT-CLM-095 | same-source; main/summary/appendix非独立 |
| INT-ART-013 | P2 §1 | intelligence-part2/sections/01_preliminaries.tex; intelligence-part2/sections/01_preliminaries_ja.tex | E0 E1 | INT-CLM-040, INT-CLM-041, INT-CLM-042, INT-CLM-043, INT-CLM-044, INT-CLM-045 | same-source; main/summary/appendix非独立 |
| INT-ART-014 | P2 §2 | intelligence-part2/sections/02_inference_operator.tex; intelligence-part2/sections/02_inference_operator_ja.tex | E0 E1 | INT-CLM-043, INT-CLM-046, INT-CLM-047, INT-CLM-048, INT-CLM-049, INT-CLM-050 | same-source; main/summary/appendix非独立 |
| INT-ART-015 | P2 §3 | intelligence-part2/sections/03_nonclosure_theorem.tex; intelligence-part2/sections/03_nonclosure_theorem_ja.tex | E0 E1 | INT-CLM-042, INT-CLM-051, INT-CLM-052, INT-CLM-053, INT-CLM-054 | same-source; main/summary/appendix非独立 |
| INT-ART-016 | P2 §4 | intelligence-part2/sections/04_response_channels.tex; intelligence-part2/sections/04_response_channels_ja.tex | E0 E1 | INT-CLM-055, INT-CLM-056, INT-CLM-057 | same-source; main/summary/appendix非独立 |
| INT-ART-017 | P2 §5 | intelligence-part2/sections/05_emergent_stopping_layer.tex; intelligence-part2/sections/05_emergent_stopping_layer_ja.tex | E0 E1 | INT-CLM-037, INT-CLM-044, INT-CLM-045, INT-CLM-047, INT-CLM-049, INT-CLM-057, INT-CLM-058, INT-CLM-059, INT-CLM-060, INT-CLM-061, INT-CLM-062, INT-CLM-063, INT-CLM-064, INT-CLM-065, INT-CLM-066, INT-CLM-086, INT-CLM-087 | same-source; main/summary/appendix非独立 |
| INT-ART-018 | P2 §6 | intelligence-part2/sections/06_animism.tex; intelligence-part2/sections/06_animism_ja.tex | E1 | INT-CLM-067, INT-CLM-068 | same-source; main/summary/appendix非独立 |
| INT-ART-019 | P2 §7 | intelligence-part2/sections/07_god.tex; intelligence-part2/sections/07_god_ja.tex | E0 E1 | INT-CLM-069, INT-CLM-070 | same-source; main/summary/appendix非独立 |
| INT-ART-020 | P2 §8 | intelligence-part2/sections/08_religion.tex; intelligence-part2/sections/08_religion_ja.tex | E1 | INT-CLM-071, INT-CLM-072, INT-CLM-073, INT-CLM-095 | same-source; main/summary/appendix非独立 |
| INT-ART-021 | P2 §9 | intelligence-part2/sections/09_social_blockchain.tex; intelligence-part2/sections/09_social_blockchain_ja.tex | E0 E1 | INT-CLM-072, INT-CLM-074, INT-CLM-075, INT-CLM-076, INT-CLM-077 | same-source; main/summary/appendix非独立 |
| INT-ART-022 | P2 §10 | intelligence-part2/sections/10_gettier_problem.tex; intelligence-part2/sections/10_gettier_problem_ja.tex | E0 E1 | INT-CLM-040, INT-CLM-066, INT-CLM-078, INT-CLM-079, INT-CLM-080 | same-source; main/summary/appendix非独立 |
| INT-ART-023 | P2 §11 | intelligence-part2/sections/11_instability_region.tex; intelligence-part2/sections/11_instability_region_ja.tex | E0 E1 | INT-CLM-081, INT-CLM-082, INT-CLM-083, INT-CLM-084 | same-source; main/summary/appendix非独立 |
| INT-ART-024 | P2 §12 | intelligence-part2/sections/12_constructive_clauses.tex; intelligence-part2/sections/12_constructive_clauses_ja.tex | E0 E1 | INT-CLM-037, INT-CLM-085, INT-CLM-086, INT-CLM-087 | same-source; main/summary/appendix非独立 |
| INT-ART-025 | P2 §13 | intelligence-part2/sections/13_conclusion.tex; intelligence-part2/sections/13_conclusion_ja.tex | E1 E11 | INT-CLM-088, INT-CLM-089, INT-CLM-092 | same-source; main/summary/appendix非独立 |
| INT-ART-026 | P2 A | intelligence-part2/appendices/appendix_a_master_table.tex; intelligence-part2/appendices/appendix_a_master_table_ja.tex | E0 E1 | INT-CLM-041, INT-CLM-048, INT-CLM-081, INT-CLM-090 | same-source; main/summary/appendix非独立 |
| INT-ART-027 | P2 B | intelligence-part2/appendices/appendix_b_homology.tex; intelligence-part2/appendices/appendix_b_homology_ja.tex | E0 E1 | INT-CLM-045, INT-CLM-050, INT-CLM-062, INT-CLM-091 | same-source; main/summary/appendix非独立 |
| INT-ART-028 | P2 C | intelligence-part2/appendices/appendix_c_part1_mapping.tex; intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex | E1 E11 | INT-CLM-039, INT-CLM-065, INT-CLM-092 | same-source; main/summary/appendix非独立 |
| INT-ART-029 | P2 D | intelligence-part2/appendices/appendix_d_optional_notes.tex; intelligence-part2/appendices/appendix_d_optional_notes_ja.tex | E0 E1 E11 | INT-CLM-051, INT-CLM-052, INT-CLM-053, INT-CLM-054, INT-CLM-064, INT-CLM-078, INT-CLM-080, INT-CLM-094, INT-CLM-095 | same-source; main/summary/appendix非独立 |
| INT-ART-030 | P2 E | intelligence-part2/appendices/appendix_e_emergence_homology.tex; intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex | E0 E1 E11 | INT-CLM-044, INT-CLM-045, INT-CLM-059, INT-CLM-089, INT-CLM-093 | same-source; main/summary/appendix非独立 |

| ART | Figure family | Asset family | Types | Claim links | Independence |
|---|---|---|---|---|---|
| INT-ART-031 | P1 FIG1 | intelligence-part1/figures/fig1_four_layer_decomposition.*; _ja.* | E1 | INT-CLM-001, INT-CLM-002, INT-CLM-003, INT-CLM-004 | caption/figurenoteとsourceの図示。independent measurement/runでない |
| INT-ART-032 | P1 FIG2 | intelligence-part1/figures/fig2_three_axioms.*; _ja.* | E1 | INT-CLM-005, INT-CLM-006, INT-CLM-007, INT-CLM-008 | caption/figurenoteとsourceの図示。independent measurement/runでない |
| INT-ART-033 | P1 FIG3 | intelligence-part1/figures/fig3_cross_domain_homology.*; _ja.* | E1 | INT-CLM-011, INT-CLM-012, INT-CLM-013 | caption/figurenoteとsourceの図示。independent measurement/runでない |
| INT-ART-034 | P1 FIG4 | intelligence-part1/figures/fig4_branching_explosion.*; _ja.* | E1 | INT-CLM-017, INT-CLM-018, INT-CLM-019 | caption/figurenoteとsourceの図示。independent measurement/runでない |
| INT-ART-035 | P1 FIG5 | intelligence-part1/figures/fig5_four_layer_correspondence.*; _ja.* | E1 | INT-CLM-025, INT-CLM-029, INT-CLM-030, INT-CLM-031 | caption/figurenoteとsourceの図示。independent measurement/runでない |
| INT-ART-036 | P2 FIG1 | intelligence-part2/figures/fig1_c_landscape.*; _ja.* | E1 | INT-CLM-051, INT-CLM-052, INT-CLM-053, INT-CLM-054 | caption/figurenoteとsourceの図示。independent measurement/runでない |
| INT-ART-037 | P2 FIG2 | intelligence-part2/figures/fig2_responsive_silent_threshold.*; _ja.* | E1 | INT-CLM-055, INT-CLM-056 | caption/figurenoteとsourceの図示。independent measurement/runでない |
| INT-ART-038 | P2 FIG3 | intelligence-part2/figures/fig3_mutual_constraint_mu_theta.*; _ja.* | E1 | INT-CLM-049, INT-CLM-060 | caption/figurenoteとsourceの図示。independent measurement/runでない |
| INT-ART-039 | P2 FIG4 | intelligence-part2/figures/fig4_three_layer_architecture.*; _ja.* | E1 | INT-CLM-037, INT-CLM-059, INT-CLM-060, INT-CLM-086 | caption/figurenoteとsourceの図示。independent measurement/runでない |
| INT-ART-040 | P2 FIG5 | intelligence-part2/figures/fig5_three_examples_of_emergence.*; _ja.* | E1 | INT-CLM-044, INT-CLM-045, INT-CLM-093 | caption/figurenoteとsourceの図示。independent measurement/runでない |
| INT-ART-041 | P2 FIG6 | intelligence-part2/figures/fig6_phi_ext_phi_net.*; _ja.* | E1 | INT-CLM-064, INT-CLM-065 | caption/figurenoteとsourceの図示。independent measurement/runでない |
| INT-ART-042 | P2 FIG7 | intelligence-part2/figures/fig7_evolution_of_stopping_structures.*; _ja.* | E1 | INT-CLM-067, INT-CLM-069, INT-CLM-070, INT-CLM-071, INT-CLM-072, INT-CLM-074 | caption/figurenoteとsourceの図示。independent measurement/runでない |
| INT-ART-043 | P2 FIG8 | intelligence-part2/figures/fig8_phase_diagram.*; _ja.* | E1 | INT-CLM-081, INT-CLM-082, INT-CLM-083, INT-CLM-084 | caption/figurenoteとsourceの図示。independent measurement/runでない |
| INT-ART-044 | P2 FIG9 | intelligence-part2/figures/fig9_cross_domain_homology.*; _ja.* | E1 | INT-CLM-091, INT-CLM-093 | caption/figurenoteとsourceの図示。independent measurement/runでない |

| ART | Citation artifact | Location | Type | Claim links | Independence |
|---|---|---|---|---|---|
| INT-ART-045 | VEDVol1 | intelligence-part1/refs.bib; intelligence-part1/sections/01_introduction.tex; intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex; intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex; intelligence-part1/sections_ja/01_introduction_ja.tex | E2 | INT-CLM-009, INT-CLM-036, INT-CLM-041 | same-series; independent validationではない |
| INT-ART-046 | VEDVol2 | intelligence-part1/refs.bib; intelligence-part1/sections/01_introduction.tex; intelligence-part1/sections_ja/01_introduction_ja.tex | E2 | INT-CLM-036, INT-CLM-044, INT-CLM-093 | same-series; independent validationではない |
| INT-ART-047 | VEDVol3 | intelligence-part1/refs.bib; intelligence-part1/sections/01_introduction.tex; intelligence-part1/sections_ja/01_introduction_ja.tex | E2 | INT-CLM-036 | same-series; independent validationではない |
| INT-ART-048 | VEDVol4 | intelligence-part1/refs.bib; intelligence-part1/sections/01_introduction.tex; intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex; intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex; intelligence-part1/sections_ja/01_introduction_ja.tex | E2 | INT-CLM-025, INT-CLM-026, INT-CLM-029, INT-CLM-042, INT-CLM-053 | same-series; independent validationではない |
| INT-ART-049 | IFGT | intelligence-part1/refs.bib; intelligence-part1/sections/01_introduction.tex; intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex; intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex; intelligence-part1/sections_ja/01_introduction_ja.tex | E2 | INT-CLM-010, INT-CLM-011, INT-CLM-041 | same-series; independent validationではない |
| INT-ART-050 | BioIFGT | intelligence-part1/refs.bib; intelligence-part1/sections/01_introduction.tex; intelligence-part1/sections_ja/01_introduction_ja.tex | E2 | INT-CLM-029, INT-CLM-030, INT-CLM-045, INT-CLM-050, INT-CLM-091 | same-series; independent validationではない |
| INT-ART-051 | Consciousness | intelligence-part1/refs.bib; intelligence-part1/sections/01_introduction.tex; intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex; intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex; intelligence-part1/sections_ja/01_introduction_ja.tex | E2 | INT-CLM-031, INT-CLM-032, INT-CLM-062 | same-series; independent validationではない |
| INT-ART-052 | Gettier1963 | intelligence-part1/refs.bib; intelligence-part1/sections/01_introduction.tex; intelligence-part1/sections_ja/06_the_gettier_problem_as_a_structural_diagnostic_ja.tex; intelligence-part1/sections_ja/01_introduction_ja.tex | E2 | INT-CLM-015, INT-CLM-016, INT-CLM-078 | external origin cited; full paper/data未検証、Int mappingには非直接 |
| INT-ART-053 | Gibson1986 | intelligence-part1/refs.bib; intelligence-part1/sections_ja/02_the_decomposition_perception_recognition_knowledge_and_intelligence_ja.tex | E2 | INT-CLM-002 | external origin cited; full paper/data未検証、Int mappingには非直接 |
| INT-ART-054 | Nakagaki2000 | intelligence-part1/refs.bib; intelligence-part1/sections/01_introduction.tex; intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex; intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex; intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex; intelligence-part1/sections_ja/01_introduction_ja.tex | E2 | INT-CLM-012, INT-CLM-013 | external origin cited; full paper/data未検証、Int mappingには非直接 |
| INT-ART-055 | Kobayashi2006 | intelligence-part1/refs.bib; intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex; intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex | E2 | INT-CLM-012, INT-CLM-013 | external origin cited; full paper/data未検証、Int mappingには非直接 |
| INT-ART-056 | Tero2007 | intelligence-part1/refs.bib; intelligence-part1/sections/01_introduction.tex; intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex; intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex; intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex; intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex; intelligence-part1/sections_ja/01_introduction_ja.tex | E2 | INT-CLM-011, INT-CLM-012, INT-CLM-013, INT-CLM-034 | external origin cited; full paper/data未検証、Int mappingには非直接 |
| INT-ART-057 | Vaswani2017 | intelligence-part1/refs.bib; intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex; intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex; intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex | E2 | INT-CLM-013, INT-CLM-047, INT-CLM-061 | external origin cited; full paper/data未検証、Int mappingには非直接 |

| Type | Artifact units | Scope / claim links |
|---|---|---|
| E0 | 22 | 上記text bundle内のformal fragments、validity未監査 |
| E1 | 44 | 30 source bundles＋14 figure bundles。独立実証44件ではない |
| E2 | 13 | 13 referenced works（same-series7 / external6）、同じcitation再使用は1件 |
| E3 | 0 | Int-linked direct artifact未所在 |
| E4 | 0 | Int-linked direct artifact未所在 |
| E5 | 0 | Int-linked direct artifact未所在 |
| E6 | 0 | Int-linked direct artifact未所在 |
| E7 | 0 | Int-linked direct artifact未所在 |
| E8 | 0 | Int-linked direct artifact未所在 |
| E9 | 0 | Int-linked direct artifact未所在 |
| E10 | 0 | Int-linked direct artifact未所在 |
| E11 | 5 | 5 text bundlesのfuture記載。scientific testとeditorial workを分離 |
| E12 | 0 | positive artifactとして数えない。NO claimのrhetorical presenceに使用 |

E0/E1/E11の同じtextを3つの独立証拠と数えない。E2の外部研究内部に測定や数値計算が存在すると本文が述べても、外部論文未取得の今回それをIntのE3–E8/E10実行artifactへ移さない。

## 28. Bibliography burden

Part I refs.bib 13 entries、cited unique keys EN12/JA13、JA-only Gibson1986、未解決citation key 0。Part II refs.bibは56 bytesのコメントのみ、entries0/cited keys0。空のbibliographyを『理論は出典なし』と一般化せず、本文の節参照・系列名・歴史的例を別provenanceとして記録する。

| ID | Reference | Cited set / source role | Exact Int claim supported? | Additional burden |
|---|---|---|---|---|
| INT-CITEBURDEN-001 | VEDVol1 | EN/JA; 差分発展/順序の系列背景 | 語彙/比較/navigational originのみ | same-series result/closureをInt validationへ流用不可 |
| INT-CITEBURDEN-002 | VEDVol2 | EN/JA; 粒子/閉包energyとの比較背景 | 語彙/比較/navigational originのみ | same-series result/closureをInt validationへ流用不可 |
| INT-CITEBURDEN-003 | VEDVol3 | EN/JA; 理論treeのnavigation背景 | 語彙/比較/navigational originのみ | same-series result/closureをInt validationへ流用不可 |
| INT-CITEBURDEN-004 | VEDVol4 | EN/JA; DHI parent-language/horizon比較 | 語彙/比較/navigational originのみ | same-series result/closureをInt validationへ流用不可 |
| INT-CITEBURDEN-005 | IFGT | EN/JA; projected vocabulary | 語彙/比較/navigational originのみ | same-series result/closureをInt validationへ流用不可 |
| INT-CITEBURDEN-006 | BioIFGT | EN/JA; quasi-closure/second-attractor予告、typed OPEN guard | 語彙/比較/navigational originのみ | same-series result/closureをInt validationへ流用不可 |
| INT-CITEBURDEN-007 | Consciousness | EN/JA; fast/slow log/projection比較 | 語彙/比較/navigational originのみ | same-series result/closureをInt validationへ流用不可 |
| INT-CITEBURDEN-008 | Gettier1963 | EN/JA; JTBへの反例という哲学的背景 | Gettier問題のoriginのみ; C/LEの確証ではない | 元文献全内容・引用帰属を検証していない。必要なら後続の外部検証だが今回は実施しない |
| INT-CITEBURDEN-009 | Gibson1986 | JA only; 知覚をavailabilityとする部分的類比（JAのみ） | 部分的perception比較のみ | 元文献全内容・引用帰属を検証していない。必要なら後続の外部検証だが今回は実施しない |
| INT-CITEBURDEN-010 | Nakagaki2000 | EN/JA; maze behaviorの外部報告紹介 | 外部domain descriptionを引用; Int-specific mappingは直接支持しない | 元文献全内容・引用帰属を検証していない。必要なら後続の外部検証だが今回は実施しない |
| INT-CITEBURDEN-011 | Kobayashi2006 | EN/JA; rhythmic motionモデルの外部紹介 | 外部domain descriptionを引用; Int-specific mappingは直接支持しない | 元文献全内容・引用帰属を検証していない。必要なら後続の外部検証だが今回は実施しない |
| INT-CITEBURDEN-012 | Tero2007 | EN/JA; flow reinforcement/decay式の出典 | 外部domain descriptionを引用; Int-specific mappingは直接支持しない | 元文献全内容・引用帰属を検証していない。必要なら後続の外部検証だが今回は実施しない |
| INT-CITEBURDEN-013 | Vaswani2017 | EN/JA; attention/layer/training architectureの出典 | 外部domain descriptionを引用; Int-specific mappingは直接支持しない | 元文献全内容・引用帰属を検証していない。必要なら後続の外部検証だが今回は実施しない |

| ID | Named material without dedicated P2 bibliography | Burden |
|---|---|---|
| INT-CITEBURDEN-014 | P2 VED/IFGT/CT/Con/Bio、Master | 節/語彙pointerはあるがhistorical exact versionとtyped inheritance未確定 |
| INT-CITEBURDEN-015 | P2 animism/God/religion/science/legitimacy/creation | historical/anthropological/sociological source anchor、case corpus未所在 |
| INT-CITEBURDEN-016 | P1 paperclip/Bostrom;P2 AIcost/Git | Bostrom専用bibkeyなし。思考例/比較でありInt empiricalAI testではない |
| INT-CITEBURDEN-017 | P1 Nakagaki attributed wording / Gettier repair history | 引用先の存在とexact wording/全repair史の裏付けを区別。専用pinpoint未確認 |

## 29. Evidence provenance ledger

| ID | Provenance | Source | Independence / ceiling |
|---|---|---|---|
| INT-PROV-001 | same-source formal | P2§3;AJD.1–4 | same premise/sketch再掲。追加validationではない |
| INT-PROV-002 | same-source definition | P1§2;P2§1/2/5/10 | 局所定義のsupport。経験的truth criterionでない |
| INT-PROV-003 | same-series | P1refs VED/IFGT/Bio/Con;P2B/E | 系列のproof/audit closureの移送禁止 |
| INT-PROV-004 | external citation | P1refs external6 | 外部originとInt mapping独立性を分離 |
| INT-PROV-005 | historical narrative | P2§6–9 | E1再解釈、E5出典付き観測ではない |
| INT-PROV-006 | uncited general example | P1§8 fatigue/paperclip;P2profiles | 事例名は直接testではない |
| INT-PROV-007 | figure-derived | P1fig4;P2fig8ほか14families | 理論から作られたschema。simulation/outputではない |
| INT-PROV-008 | appendix-derived | P2A–E | mainと同じ前提の再述・追加構成。独立性なし |
| INT-PROV-009 | prospective/editorial | P1§10;P2§13,C,D/E | future scientific directionと編集作業を分離 |
| INT-PROV-010 | other repo branches' code/results | Phase00 crossbranch pointers | Int専用mapping/bridgeがなければInt E4/E10へ算入しない |

## 30. Prediction / future maturity — 20/20

P0 example/agenda only; P1 qualitative direction; P2 testable in principle（sourceに比較可能な候補方向あり、実行可能性認証ではない）; P3 operationalized; P4 executed; P5 validated; P6 replicated。予定だけをP2にしない。formal/editorial/philosophical futureには科学的予測maturityが本来N/Aなので、20entry crosswalk内の管理分類としてP0に置き、実証予測の件数へ数えない。

| ID | Phase00 | Source / target | Maturity | Variables / observable / task scope | Threshold / dataset / protocol | Executed / result / validated |
|---|---|---|---|---|---|---|
| INT-PRED04-001 | INT-PRED-DRAFT-001 | P1 §4–5; Physarumnetwork/maze/rhythmexample | P0 | 外部実例。Intの新規予測でない; behavior/source citationあり、mappingは未試験 | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-002 | INT-PRED-DRAFT-002 | P1 §5; Transformerlayertransition/attentionunderaxioms | P0 | architecture比較例。hidden/layer記号はあるがInt固有testなし | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-003 | INT-PRED-DRAFT-003 | P1 §7; accumulatedcorrectness→morebranching | P1 | I/J/graph増大の方向、correctness/edgeの独立observable extractionなし | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-004 | INT-PRED-DRAFT-004 | P1 §7–8; speed/knowledge/capabilityincreasewillnotselfstop | P1 | 速度・能力増加でselfstopしない方向、genuine-stop endpoint未定 | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-005 | INT-PRED-DRAFT-005 | P1 J §8; fatiguedinferencecanresume | P0 | 疲労後再開のsource例、観察report/datasetはない | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-006 | INT-PRED-DRAFT-006 | P1 §9–10; externalizedstop/AI safetyarchitecture | P0 | future design agendaで数値予測ではない | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-007 | INT-PRED-DRAFT-007 | P1 §9–10; Bio-Con-Inttransitiondynamics | P0 | cross-layer transitionのfuture agenda、変数間map未定 | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-008 | INT-PRED-DRAFT-008 | P1 §10; otherbiologicalsystems / convergence extensions | P0 | 他生物へのfuture比較、指定taskなし | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-009 | INT-PRED-DRAFT-009 | P2 §2,4; changingthresholdresponse/silentregime | P2 | 同じ環境のresponse/nonresponseと速度・resolution差を比較するsource方向。実行protocolではない | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-010 | INT-PRED-DRAFT-010 | P2 §5; Physarum/Transformer/sapienslog-stopprofiles | P0 | 三層profile比較例。独立LE/μ分類未提示 | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-011 | INT-PRED-DRAFT-011 | P2 §5,13,E; stoppingfunctional localmin formalization | P0 | stopping-functional formalization予定。scientific predictionではなくformal future task | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-012 | INT-PRED-DRAFT-012 | P2 §6–7; animismcost / centralizationambiguity | P1 | 低cost/中心化→曖昧性低下の社会方向。cost/ambiguity尺度なし | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-013 | INT-PRED-DRAFT-013 | P2 §8–9; religion/science/BCmaintenance/revision | P1 | 維持・改訂・同期の比較方向。史料選択・測定なし | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-014 | INT-PRED-DRAFT-014 | P2 §9; branch/merge/rollbackcostsocialvsGit | P1 | branch/merge/rollbackの比較方向。cost定義/データなし | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-015 | INT-PRED-DRAFT-015 | P2 §11; vinf/rres/η and speedgapcollapse | P2 | vinf/vLR gap増大と崩壊の比較候補。rate名はあるがstep extraction/critical値なし | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-016 | INT-PRED-DRAFT-016 | P2 §8,11,13; clinical/pathologicalattractorapplication | P0 | clinical応用はfuture/guard。診断予測ではない | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-017 | INT-PRED-DRAFT-017 | P2 §10–12; μθ relocation / error tolerance | P1 | μ relocationと改訂/error tolerance方向。独立error endpointなし | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-018 | INT-PRED-DRAFT-018 | P2 §13; philosophymeaning/understanding/subjectivity | P0 | 哲学的意味/主観へのfuture課題。経験予測ではない | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-019 | INT-PRED-DRAFT-019 | P2 E D; J §13; revision_notes; AIcost/stoppingengineeringpracticalproblems | P0 | AIcost/practical design問題。プロトコルや結果でない | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |
| INT-PRED04-020 | INT-PRED-DRAFT-020 | P2 J §13,C; P1§5/6/8/9微修正 | P0 | P1四微修正はeditorial task。scientific prediction母数に含めない | Int-specific threshold/dataset/protocol未所在 | NO / 未所在 / NO |

20entry中、direction/comparisonとしてP1以上は8（P1 6/P2 2）。残り12は例・予定・編集等のP0管理分類。したがって『20個の実証予測』とは呼ばない。Intelligence-specific tested predictions0 / validated0 / replicated0。外部論文の実行履歴をInt予測の成功に換算しない。

## 31. Source-implied falsification directions

sourceが述べる方向が対応先で成立しない、というfailure directionのみを抽出した。新しい課題・操作・測定・閾値を設計していない。「measurable candidate」はsourceに観察可能な対象名があるだけで、E9/P3ではない。global falsifiabilityのfinal verdictには進まない。

| ID | Target | Source | Source direction could fail if | Maturity | Limit |
|---|---|---|---|---|---|
| INT-FALS-001 | Physarum path/flow correspondence | P1§4–5 | 記述されたflow/path挙動が対応するglobal-bias説明に合わない | measurable candidate | 外部modelの挙動対象、Int写像の選別法未定 |
| INT-FALS-002 | Transformer ordered layer profile | P1§5 | 記述したlayer/attentionの順序関係と対象architectureが合わない | measurable candidate | 特定モデル/run未指定 |
| INT-FALS-003 | global Φ lower bound | P1§3–5 | global役割を持たないとされた系が定義対象の持続motionを示す | conceptual only | global役割と対象motionの独立判定未定 |
| INT-FALS-004 | correctness→branching | P1§7 | 正しさ蓄積が推論枝増加に対応しない | conceptual only | correctness/graph extraction未定 |
| INT-FALS-005 | capability increase→nonstop | P1§7–8 | 能力/速度増加がsourceでいう停止不在を伴わない | conceptual only | genuine-stop criterion未定 |
| INT-FALS-006 | fatigue→resumption | P1§8 | 中断後に再開しうるというsource例が対応しない | measurable candidate | 例であって全疲労の再開予測ではない |
| INT-FALS-007 | external log/response→revisability | P1§8–9 | 外化が改訂可能停止を支えない | conceptual only | 外化/持続条件が未限定 |
| INT-FALS-008 | response/silent threshold | P2§2,4 | 時間/解像度に応じたresponse区分がsource方向に移動しない | measurable candidate | response対象は名付け済、測定規則なし |
| INT-FALS-009 | LR/H→LE | P2§5 | recursive logsとHの下で想定LEが生じない | conceptual only | LE独立検出が未定 |
| INT-FALS-010 | μ/error tolerance | P2§10–12 | threshold可変性と改訂/error toleranceが結びつかない | conceptual only | 独立endpoint未定 |
| INT-FALS-011 | centralization→ambiguity | P2§7 | 中心化により停止曖昧性が減らない | conceptual only | ambiguity/cost尺度なし |
| INT-FALS-012 | religion/science operation comparison | P2§8–9 | 維持/改訂の割当が対象の運用に対応しない | conceptual only | case-selection criteriaなし |
| INT-FALS-013 | Git/social cost contrast | P2§9 | 分岐/merge/rollback costの対比方向が成立しない | conceptual only | 単位・対象条件なし |
| INT-FALS-014 | speed/log gap→collapse | P2§11 | 生成速度と参照速度の差が層崩壊方向に対応しない | measurable candidate | rate候補のみ; critical値/層検出なし |
| INT-FALS-015 | high η→rigidity | P2§11 | stopping hardness増加が想定硬直に対応しない | conceptual only | hardnessとrigidity独立criterionなし |
| INT-FALS-016 | human/AI same-phase extension | P2§11 | 同条件とされたhuman/AIで同failure方向が成立しない | conceptual only | common operational scaleなし |

## 32. SERIOUS evidence burden — five retained candidates

Phase03の循環status RETAINは変更しない。下記は追加のevidence-burden statusであり解決・dispositionではない。critical/strongはrequired typeとのgapの強さであって理論の偽判定ではない。

| ID | Phase03 Serious | Target | Current support | Missing evidence / bridge | Independent endpoint | Support | Phase04 evidence status |
|---|---|---|---|---|---|---|---|
| INT-SEREVID-001 | INT-SERIOUS-001 (RETAIN) | internal cognitive stopping | E0 conditional sketch/E1 completion interpretation | strict-J条件を超えるS/停止criterion、F'に同じ前提を適用するbridge | formal endpointは記述、認知endpoint未所在 | PARTIAL | EVIDENCE GAP CRITICAL |
| INT-SEREVID-002 | INT-SERIOUS-002 (RETAIN) | LE emergence | E0 schematic equation/E1 stages/profiles | update/収束条件、停止機能と独立なLE検出・生成test | attractor名はあるがoperational endpointなし | PARTIAL | EVIDENCE GAP CRITICAL |
| INT-SEREVID-003 | INT-SERIOUS-003 (RETAIN) | Φext/Φnet | E0 two-view sketch/E1 network | network aggregation、二対象の独立同定、identity map・社会観測 | social reference名はあるが測定fieldなし | PARTIAL | EVIDENCE GAP CRITICAL |
| INT-SEREVID-004 | INT-SERIOUS-004 (RETAIN) | μ/error tolerance | E0 definition/two-way sketch/E1 profile | 独立μ能力/誤り・自由endpoint、θ変更必要性条件 | revisability共有、独立criterionなし | PARTIAL | EVIDENCE GAP STRONG |
| INT-SEREVID-005 | INT-SERIOUS-005 (RETAIN) | Gettier confirmation | E2 Gettier origin＋E0/E1 interpretation | GettierからC/LEを独立に選別するbridge、arch確認 | 外部哲学例あり、Int empirical endpointなし | PARTIAL | EVIDENCE GAP CRITICAL |

## 33. General-intelligence burden

| ID | Scope | Source | Strongest support | Unmet extension |
|---|---|---|---|---|
| INT-GENINT-EVID-001 | intelligence-like motion | P1§2–5 | local definition＋structured comparison | 三公理の一般必要性は定義以上 |
| INT-GENINT-EVID-002 | model-local intelligence | P1§2;P2§5,12 | 採用architecture/functional vocabulary | operational criterionではない |
| INT-GENINT-EVID-003 | general intelligence | P2§12 | LF/LR/LE＋external sourceの構成的命名 | 全intelligenceへの必要性・代替排除を支える独立supportなし |
| INT-GENINT-EVID-004 | sapiens | P2§2,5,12 | endogenous μというprofile/定義 | species/能力の測定で一般化していない |
| INT-GENINT-EVID-005 | biological | P1§5;P2§5,B | E2 Physarum背景＋E1 Bio比較 | biological-general intelligenceとLE mappingは未検証 |
| INT-GENINT-EVID-006 | artificial | P1§5,8;P2§5,11 | E2 architecture背景＋E1 profiles | Int固有benchmark/自律停止criterionなし |
| INT-GENINT-EVID-007 | social/collective | P2§6–9 | shared-stop/maintenanceの再解釈 | historical validation/一般社会法則ではない |

P2J§12の『μを内発的に持つこととsapiensであることは定義上同じ』は定義の所在としてsupportされるが、それを一般生物学的分類の証拠にしない。一般知性にμ不要のguard、Transformerのown LE不在profile、N/R条項の範囲差はPhase02から保留する。

## 34. New evidence/burden uncertainties

INT-U-001–158は変更・解決しない。新規30件はINT-U-159–188。旧formal/role/circularity issueと関連する場合も、ここでの未解決項はevidence type/criterion/provenanceに限る。総数188。

| ID | Evidence issue | Cross-reference | Uncertainty |
|---|---|---|---|
| INT-U-159 | B0/B4境界 | CLM001–004; GAP001 | local definitionのsupportを生成・保存不能の経験的supportへ移すための独立criteriaは何か |
| INT-U-160 | 公理必要性 | GAP002; P1§3 | 欠如例の比較を一般lower boundへ拡張する対象範囲・支持形式が未確定 |
| INT-U-161 | global bias | GAP003; P1§3–5 | global-role定義と局所則非還元性の要求supportをどう分離するか |
| INT-U-162 | Physarum citation | PHYS-EVID001–003 | 引用された外部観察/モデルのexact passagesとIntへの帰属は外部検証未実施 |
| INT-U-163 | empirical convergence | GAP005; STRONG055 | 別研究起源とmapping選択の独立性を支えるprovenance未確定 |
| INT-U-164 | Transformer Φ | TR-EVID003–004 | training loss/weightsをΦtrへ対応づける独立calibration未所在 |
| INT-U-165 | profile endpoints | GAP006; P2§5 | 三profileのown LE/内生μを比較する独立endpoint未所在 |
| INT-U-166 | Gettier confirmation | GAP007; SERIOUS005 | 哲学的反例からC/LE/nonclosureを選別する独立support未所在 |
| INT-U-167 | 修復史 | GAP008; CITEBURDEN017 | 全JTB修復を排除する主張に対応する網羅的source scope未確認 |
| INT-U-168 | branching | GAP009; P1§7 | 可能辺/経路を実際の認知branch生成へ対応づけるevidence未所在 |
| INT-U-169 | 症状/負荷 | GAP010; P2§8 | nonclinical命名を超える機構/予防効果の行動support未所在 |
| INT-U-170 | noFP/stop | GAP011; SERIOUS001 | 条件付きformal supportの範囲と任意認知停止criterionとのbridge未確定 |
| INT-U-171 | 中断/完成 | GAP012; P1§8 | 生理的終了を例外なく中断へ分類する独立criteria未所在 |
| INT-U-172 | human/AI | GAP013; P2§11 | 同phaseへの配置に必要なhuman/AI共通observable未所在 |
| INT-U-173 | 外化保証 | GAP014; P1§9 | 持続/改訂可能停止を保証する条件と社会観測support未所在 |
| INT-U-174 | Cmax/理解 | GAP015; P2§1,3 | 究極理解というendpointをboundaryから独立に支えるsupport未所在 |
| INT-U-175 | Bio/Con transfer | GAP016; HOMOEVID | 外部/系列sourceのどの結果がInt固有関係を支持するか未確定 |
| INT-U-176 | 導出宣言 | GAP017/019; P2§0–1 | 同形式のreuseとtyped cognitive derivationのsupport差を埋めるartifact未所在 |
| INT-U-177 | 四層継承 | GAP018; CLM039 | 継承とされる表のexact content authorityがsupport判定を妨げる |
| INT-U-178 | threshold calibration | GAP020; P2§2,4 | Cij/Hij/rangeと観測応答の校正・parameter estimator未所在 |
| INT-U-179 | LE存在/生成 | GAP021; SERIOUS002 | schemaと停止機能命名から独立したattractor識別/機構test未所在 |
| INT-U-180 | μ/error equivalence | GAP022; SERIOUS004 | 二方向をrevisability共有以上に支持する独立error/μendpoint未所在 |
| INT-U-181 | Φnetwork identity | GAP023; SERIOUS003 | 二視点命名から独立したaggregation/identity criterion未所在 |
| INT-U-182 | 社会/歴史case | GAP024; SOC-EVID | conceptual comparisonを歴史的説明へ上げる史料・case-selection provenance未所在 |
| INT-U-183 | 低cost/普遍性 | GAP025; CLM068 | cost比較と文化/歴史的対象母集団のsupport未所在 |
| INT-U-184 | 非計算可能性/創造排他性 | GAP026–027 | 社会的命名からprincipled noncomputability/only-individualへ進むrequired type未所在 |
| INT-U-185 | 相図境界 | GAP028; PRED04-015 | narrow band/critical gapの測定値・数値境界・fit未所在 |
| INT-U-186 | 一般知性のscope | GAP029; CLM085–087 | model-local/sapiens定義からgeneral-intelligence必要性への独立criterion未所在 |
| INT-U-187 | Master/localmin authority | GAP030–031 | exact Master predecessorとLE functional採用statusがsupport ceilingを未確定にする |
| INT-U-188 | future/citation ceiling | PRED04/CITEBURDEN/ART | future/外部引用の現状からInt-specific test/operational/validationを認定する追加provenance未所在 |

## 35. Validation / immutable task-start boundary

開始時snapshotは2026-09-12、継続・記録完了は2026-09-13。ユーザーの「作業続行」後もsnapshotを取り直さず、全sourceが開始時と同じことを確認した。

- Snapshot: `${TEMP_EVIDENCE_ROOT}/int_phase04.Iudsvs/baseline.json`（1494 files; .git除外、ignored/untrackedも含む）
- Snapshot SHA-256: `53984ce354a374deade522096cd193034969f83866b52ee938cb4e01687403e0`
- 新規record以外の差分はaudit READMEのみ許可。Phase00–03、66 included TeX、math/captions/figures/JA/refs.bib/PDF、他branchを全file hashで保護する。
- 既存dirty worktreeはユーザーの変更として保持。git statusだけではuntracked directory内の差分が見えないためsnapshot比較を併用する。
- validation scriptは文書ID/coverage/集計/hashの静的検証のみ。theory test・model execution・simulationではない。

### Coverage / counts

| Check | Count / result |
|---|---|
| Primary claim/support/burden | 95/95; exactly one support per claim |
| Support | YES25 / PARTIAL64 / NO3 / UNRESOLVED3 =95 |
| Definitions | 32/32 crosswalk |
| Theorem evidence | 13/13; proof validity NO |
| Homology | 21/21; independent mapping test未所在 |
| Strong language | 62/62; POSSIBLY OVERSTATED:26 / OVERSTATED:25 / SUPPORTED AT CURRENT STRENGTH:1 / VERSION-SPECIFIC:5 / GUARDED:4 / UNRESOLVED:1 |
| Gaps | 31 families; LOW:0 / MEDIUM:4 / HIGH:22 / CRITICAL:5 |
| Prediction/future | 20/20; P0:12 / P1:6 / P2:2 / P3:0 / P4:0 / P5:0 / P6:0 |
| Falsification directions | 16; conceptual11 / measurable candidate5 / operationalized0 / executed0 |
| Serious | 5/5; Phase03全5RETAIN; evidence CRITICAL4 / STRONG1 |
| Artifacts | 57 documentary units; E0:22 / E1:44 / E2:13 / E11:5; E3–10,E12 positive artifacts:0; overlapping tags |
| Bibliography | P1 13 entries; EN12 / JA13 keys; P2 0 entries/keys; unresolved keys0 |
| Ceilings | FE2 / CE2 / SE2 / BE3(citation background; Int mapping2) / PE1 / XE2 / PRE2 / OE0 |
| Int-specific data / tests | operational maps0 / empirical datasets0 / simulations0 / tested0 / validated0 |
| Uncertainties | new30 INT-U-159–188 / total188 |
| Source/math invariance | PASS: task-start 1494中1493不変、変更はaudit READMEのみ、新規はPhase04記録のみ、削除0。66 included TeX不変 |
| git diff --check | PASS: exit0、diagnosticなし。untracked新規record/READMEもno-index --checkで確認 |

### Final static validation result

`${TEMP_EVIDENCE_ROOT}/int_phase04.Iudsvs/validate.py` により24 ledgersの連番・一意性、95/32/13/21/62/20/5 crosswalk、primary support合計95、burden記載、table列数、source path、citation keys、INT-U-159–188、全file hash差分を確認した。結果は `${TEMP_EVIDENCE_ROOT}/int_phase04.Iudsvs/validation.json`。git status --shortは250行で開始時表示と同一（audit directoryは既存untracked）。これは変更なしという意味ではなく、directory内の許可2ファイル差分はhashで別途確認した。

保護されたPhase00–03のSHA-256:

| Record | SHA-256 |
|---|---|
| Phase00 | ffb891b9039a71a2173574652f72776a307be6618070a74f2fcc64bc0a312d64 |
| Phase01 | ecb64a12dd4d5e4defab076c2118cc6a6f9f842ab278f03c975ce9f082891d14 |
| Phase02 | aee8d40a4241869918d6724305a3c94dc667ec2e352ed496614439d775148318 |
| Phase03 | 1596b90ca99baeeb19cf5e6fb655f5f5a4c925f63b551de33c8b0b4bfac7c05d |

### Scope of artifact search

両Intelligence directoriesをfile inventory・拡張子・current sourceのdataset/simulation/measurement/protocol/test語で再走査。Int-specific scientific code/notebook/data/result/logは未所在。Part II Makefileはbuild-supportでE4/E10ではない。TeX auxiliary/log、PDF、SVG/PNG等はpresentation/build artifactでsimulation logsではない。sourceがいうtraining data、slime traces、歴史、実験、社会合意は概念/例/外部指示であり、対応するrepo datasetではない。P1 refs13とP2コメントのみを直接確認した。repository他branchのコード存在を否定していない。Intがそれを使ったmodel-linked実行/typed bridgeとして提示していなければIntのsupportへ加算しない。

### Assessment limits

- Claim truth / empirical truth / theorem-proof validity: NOT AUDITED。
- Evidence burden/statusのみを判定し、KEEP/REVISE/DOWNGRADE/SPLIT/OPEN/RETIREのfinal dispositionを付けていない。
- 外部論文を取得・検証していない。引用の存在、source内の帰属、exact mappingとの距離を記録した。
- Phase03 serious/circularity verdictは変更しない。NOをevidence sufficiencyへ流用しない。
- 新しいoperational map/metric/experiment/bridgeを設計しない。未所在箇所を補完しない。
- Source、equations、symbols、figures、JA、BibTeX、PDF/build、upstream/downstreamを変更しない。

## 36. Stop boundary

Phase04 COMPLETE。Intelligence audit IN PROGRESS。Phase05 NOT STARTED。
Source / equation / distribution revision NOT STARTED。
No web research / PDF build / simulation / new theory / new bridge / commit / push。
この記録とaudit READMEをhandoffして停止し、Phase05、final dispositions、source implementationには進まない。
