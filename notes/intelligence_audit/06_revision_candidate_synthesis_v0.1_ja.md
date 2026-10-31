# Intelligence independent audit — Phase06 revision candidate synthesis

## 0. Status

```text
Intelligence audit: IN PROGRESS
Phase00–05: COMPLETE / inherited unchanged
Phase06 revision candidate synthesis: COMPLETE
Phase07 final audit / frozen dispositions: NOT STARTED
Candidate status: PROVISIONAL / NOT FROZEN
Theorem/proof validity: NOT AUDITED
Final dispositions: NOT ASSIGNED
Source revision: NOT STARTED
Equation revision: NOT STARTED
Distribution revision: NOT STARTED
```

95 primary claimsの改訂方向を暫定的に統合する。本文のreplacement prose、数式修正、実験計画は作らない。Phase07が独立に再照合するためのcandidate recordであり、source validity・theorem validity・empirical truthの認証ではない。

暫定primary候補: KEEP24 / REVISE8 / DOWNGRADE20 / SPLIT41 / RETIRE0 / OPEN2 =95。SERIOUS001–005は全てRETAINのまま、各中心familyの分割/弱化/研究holdを提案する。Can equation changes safely begin after Phase06?: NO。Global equation-change requirement currently: OPEN（provisional）。

## 1. Authority inheritance / decision order

Phase00–05と監査READMEを継承。Part IはJA (`main_ja.tex` + `sections_ja/`) がcurrent distributed build authority、EN (`main.tex` + `sections/`) はparallel sourceでprimary/authorized-translation status未決。Part IIはJA primary manuscript、EN working draft。appendices A–Eは各言語のappendix authority。JA/ENを先にmergeしない。P1のworking MD/P2 source_mdやPDF/figure/READMEを本文の新しいcontent authorityにしない。

Phase04: support YES25/PARTIAL64/NO3/UNRESOLVED3、strong62（SUPPORTED1/OVERSTATED25/POSSIBLY OVERSTATED26/GUARDED4/VERSION-SPECIFIC5/UNRESOLVED1）、gaps31を保持。FE2/CE2/SE2/BE3（citation-background only）/PE1/XE2/PRE2/OE0は不変。Phase05: COR3 max（formal/cognitive/behavioral/biological/social/AI）、phenomenal COR1、cross-domain X3、OP2。operational artifacts/datasets/simulations/tested/validated=0、OPEN routes24、mapping conflicts14を保持。

Phase03: SERIOUS5 RETAIN、source-level vicious circularity established?: NO、global unfalsifiability established?: NO。これは構造上の立証statusでありevidence sufficiencyに変換しない。C8はcandidateである。Phase06では新しい循環判定を出さない。

判断順序は (1) authority → (2) role consistency → (3) formal clarity → (4) circularity structure → (5) burden/support → (6) correspondence maturity → (7) operational status → (8) guard。優先する最小変更はscope限定・guard・役割区分・分割・強度調整、その後にのみ削除を検討する。PARTIAL→REVISEやYES→KEEPの自動変換はしない。CLM066はYESのlocal scopeを保持しつつ近接する安定保証の読みを防ぐREVISE候補である。

I0=formal/I1=representational-computational/I2=cognitive-functional/I3=social-collective/I4=phenomenalは監査layerで、LF/LR/LE等のsource-native区分ではない。source reuse≠derivation、same glyph≠same object、same equation form≠same signature、homology≠identity、operator≠mechanism、definition≠empirical criterion、guard≠positive supportを固定する。

source locatorはPhase00のsection map、Phase01の式occurrence、Phase02 ROLE、Phase03 CIRC、Phase04 EVID/GAP、Phase05 CORR/OPENへ解決する。以下の§はPart内のsource章番号、OPEN001等はINT-OPEN-001の略記。primary tableでのP1 E/JやP2 E/Jは言語並存を指し同一authorityを意味しない。66 current included TeXはPhase05開始時からhash変更なし。候補判断に関わるP1§10 summary、P2§0/3/5/12、AppendixA/EおよびREADMEのactual wordingを再照合した。

## 2. Candidate taxonomy / limits

| candidate | 意味 | 守る境界 |
|---|---|---|
| KEEP | 現在roleに適したscope/supportで保持 | true/empirically verifiedという意味でない |
| REVISE | coreを保ちscope/authority/guard/termを限定 | 新しい型/仮定を黙って採用しない |
| DOWNGRADE | strong claimをhypothesis/proposal/model-local/conditional/comparisonへ | 最強の書き方でなく最強の正当化可能な読解を残す |
| SPLIT | 異なるrole/burdenを概念的childへ分離 | 子成分のKEEP/DOWNGRADE/OPENは候補で、new source claimsを実装しない |
| RETIRE | 有用なdistinct contentが残らない場合のみ削除候補 | disprovedと同義でない。本phase0 |
| OPEN | content decisionにformal/evidence/authority workが必要 | falseでない。本phaseは39/90、他familyのOPEN childとは別 |

表の作業依存: P=将来のsource prose変更、F=formal work、E=empirical work、A=authority resolution。PのYESも今は未実装。F/EのHOLDはstrong成分を保持/確定するには追加workが要るが、弱いscopeのprose候補を検討するために実施したわけではない。NOも研究OPENのclosureではない。AのNOはbranch全体のEN/JA authorityが解決済という意味ではなく、当該local candidate内容を選ぶ追加の固有authority決定は不要という意味。OPEN primaryのP=HOLDでも、不確実性を記録するdocumentary note自体は禁止されない。

## 3. Primary claim revision table — 95/95

各行にちょうど一つのprimary provisional candidateを与える。current claimはPhase00 familyの要約、C-classはPhase03、support/strong statusはPhase04を変更せず表示。correspondenceはPhase05で関連付けられた候補の所在/局所上限であり、強いclaim全体がその成熟度で支持される意味ではない。NAのguard/futureには経験criterionを自動要求しない。31 GAPの所在はEVID欄から継承し、無表示は新しいgapなしという保証ではない。

CLM081の旧略称「Σ相図」はPhase05§primary claim crosswalkの注意を継承して「三軸相図/狭い安定帯（Σは別の発達量）」と表示する。P2JA§11の三軸と§1.8/Appendix AのΣ発達度を混同しないための索引上の区別であり、旧ID・claimの対象・support・sourceを変更していない。

| REV | Claim | current claim family | source locator | current authority | C-class | support | strong-language status | correspondence / operational status | GAP / OPEN / SERIOUS | provisional candidate | rationale | minimal change required | P | F | E | A |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| INT-REV-001 | INT-CLM-001 | 知性は所有能力でなく持続する動態 | P1 E/J abstract,§1–2 | P1-JA distributed; EN parallel/primary未決 | C1 | YES | 62専用family対象外（強語なしという認定ではない） | CORR030:COR2/OP1 | OPEN021; SERIOUS直接対象外 | KEEP | 枠組み内の持続動態という定義を明示。経験的知性criterionと別 | 局所定義のscopeを維持 | NO | NO | NO | NO |
| INT-REV-002 | INT-CLM-002 | 知覚・認識・知識・知性の四層区別 | P1 E/J §2 | P1-JA distributed; EN parallel/primary未決 | C1 | YES | 62専用family対象外（強語なしという認定ではない） | CORR030:COR2/OP1; CORR029:COR2/OP1 | OPEN021; SERIOUS直接対象外 | KEEP | P1の知覚/認識/知識/知性を役割分解として保持できる | 四役割のlocal性を維持。P2別表の問題は039へ | NO | NO | NO | NO |
| INT-REV-003 | INT-CLM-003 | 知識は安定した停止構造で真理そのものではない | P1 E/J §2,6 | P1-JA distributed; EN parallel/primary未決 | C1 | YES | 62専用family対象外（強語なしという認定ではない） | CORR029:COR2/OP1; CORR006:COR2/OP1 | OPEN002/020; SERIOUS直接対象外 | KEEP | knowledge=暫定停止という命名とnot truthを別scopeで支持 | 定義をGettier確認の証拠へ再利用しない | NO | NO | NO | NO |
| INT-REV-004 | INT-CLM-004 | 知性は全層を横断し知識を産出・改訂、保存されない | P1 E/J §2 | P1-JA distributed; EN parallel/primary未決 | C2 | PARTIAL | STRONG001=POSSIBLY OVERSTATED | CORR030:COR2/OP1; CORR017:COR3/OP2 | INT-GAP-001; OPEN001/007/021; SERIOUS直接対象外 | SPLIT | motionの命名と全層横断・生成/保存不能の機構読解が混在 | 定義と生成/保存一般化を分離 | YES | HOLD | HOLD | NO |
| INT-REV-005 | INT-CLM-005 | 3公理は同時必要な下限、完全理論でない | P1 E/J §3,10 | P1-JA distributed; EN parallel/primary未決 | C1 | PARTIAL | STRONG002=OVERSTATED | CORR001:COR3/OP2; CORR008:COR3/OP2; CORR043:COR3/OP2 | INT-GAP-002; OPEN001/005/021; SERIOUS直接対象外 | SPLIT | 三条件の構成と一般共同必要性は負担が異なる | axioms定義・lower-bound仮説・not sufficient guardを分離 | YES | HOLD | HOLD | NO |
| INT-REV-006 | INT-CLM-006 | connected state spaceは連続空間に限定しない | P1 E/J §3 | P1-JA distributed; EN parallel/primary未決 | C0 | YES | STRONG003=SUPPORTED AT CURRENT STRENGTH | CORR001:COR3/OP2 | OPEN001; SERIOUS直接対象外 | KEEP | connectedをcontinuousに限定しない明示的local scope | 離散reachabilityを許す定義を保持 | NO | NO | NO | NO |
| INT-REV-007 | INT-CLM-007 | temporal orderingで履歴変化が蓄積する | P1 E/J §3 | P1-JA distributed; EN parallel/primary未決 | C0 | PARTIAL | STRONG004=POSSIBLY OVERSTATED | CORR043:COR3/OP2 | INT-GAP-002; OPEN001/007/023; SERIOUS直接対象外 | REVISE | ordered updateはあるが順序だけでは履歴保持を保証しない | orderingと履歴利用の含意を区別 | YES | HOLD | HOLD | NO |
| INT-REV-008 | INT-CLM-008 | global Φは局所更新に非還元 | P1 E/J §3–4 | P1-JA distributed; EN parallel/primary未決 | C5 | PARTIAL | STRONG005=OVERSTATED | CORR008:COR3/OP2 | INT-GAP-003; OPEN005; SERIOUS直接対象外 | SPLIT | scalar global mapと局所則への非還元性を一体化 | map/role定義とirreducibility主張を分離 | YES | HOLD | HOLD | NO |
| INT-REV-009 | INT-CLM-009 | 3公理はVED/IFGTから論理的独立・意味中立 | P1 E/J §3 | P1-JA distributed; EN parallel/primary未決 | C0 | YES | 62専用family対象外（強語なしという認定ではない） | NA: negative/local scope（mapping肯定でない） | OPEN023; SERIOUS直接対象外 | KEEP | 三公理の論理独立と語彙採用scopeのguard | upstream validityを前提化しない | NO | NO | NO | NO |
| INT-REV-010 | INT-CLM-010 | I/J/Φは投影的語彙、IFGT一般量の直接同定でない | P1 E/J §4 | P1-JA distributed; EN parallel/primary未決 | C0 | YES | 62専用family対象外（強語なしという認定ではない） | CORR005:COR3/OP2; CORR008:COR3/OP2; CORR033:COR3/OP2 | OPEN004/005/023; SERIOUS直接対象外 | KEEP | projected coordinatesとgeneral IFGT非同定が明示 | glyph同一性をobject identityへ移さない | NO | NO | NO | NO |
| INT-REV-011 | INT-CLM-011 | Physarum solverと語彙的/構造的対応 | P1 E/J §4 | P1-JA distributed; EN parallel/primary未決 | C4 | YES | STRONG054=GUARDED | CORR005:COR3/OP2; CORR033:COR3/OP2; CORR036:COR3/OP2 | OPEN015/023; SERIOUS直接対象外 | KEEP | Q/D/BC対応表はstrict mathematical identity否定付き | lexical/role comparisonに限定。012の確認主張と非合算 | NO | NO | NO | NO |
| INT-REV-012 | INT-CLM-012 | Physarum研究はglobal Φ非還元性への独立実証的収束 | P1 E/J abstract,§4–5,10 | P1-JA distributed; EN parallel/primary未決 | C6 | PARTIAL | STRONG055=OVERSTATED | CORR008:COR3/OP2; CORR009:COR3/OP2; CORR036:COR3/OP2 | INT-GAP-005; OPEN005/015/023; SERIOUS直接対象外 | DOWNGRADE | 外部研究起源はInt固有Φ非還元性の独立確認でない | convergenceの強度を比較上のmotivationへ下げる | YES | NO | HOLD | NO |
| INT-REV-013 | INT-CLM-013 | PhysarumとTransformerは同じ三条件を満たす | P1 E/J §5 | P1-JA distributed; EN parallel/primary未決 | C6 | PARTIAL | STRONG056=POSSIBLY OVERSTATED | CORR001:COR3/OP2; CORR009:COR3/OP2; CORR010:COR3/OP2; CORR040:COR3/OP2 | INT-GAP-006; OPEN015/016/021/023; SERIOUS直接対象外 | SPLIT | 具体carrier対応と同じ公理充足の一般化が混在 | 3profile比較と検証/必要性の拡張を分離 | YES | HOLD | HOLD | NO |
| INT-REV-014 | INT-CLM-014 | 同一cognition/experience/functionalethicalstatusを主張しない | P1 E/J §5 | P1-JA distributed; EN parallel/primary未決 | C0 | YES | 62専用family対象外（強語なしという認定ではない） | NA: negative/local scope（mapping肯定でない） | OPEN022/023; SERIOUS直接対象外 | KEEP | cognition/experience/ethical identityの否定を明示 | 否定guardを維持しpositive supportへ数えない | NO | NO | NO | NO |
| INT-REV-015 | INT-CLM-015 | Gettierはstopping状態と動的性質の層間不一致 | P1 E/J §6 | P1-JA distributed; EN parallel/primary未決 | C5 | PARTIAL | 62専用family対象外（強語なしという認定ではない） | CORR029:COR2/OP1; CORR006:COR2/OP1 | INT-GAP-007; OPEN002/020; SERIOUS005 | SPLIT | Gettierを用いた再記述と理論確認の負担が異なる | diagnostic interpretationとindependent confirmationを分離 | YES | NO | HOLD | NO |
| INT-REV-016 | INT-CLM-016 | JTBへの静的条件追加では動的保証にならない | P1 E/J §6 | P1-JA distributed; EN parallel/primary未決 | C5 | PARTIAL | STRONG006=OVERSTATED | CORR029:COR2/OP1; CORR004:COR1/OP1 | INT-GAP-008; OPEN002/020; SERIOUS005 | DOWNGRADE | 全JTB修復に及ぶ不可能性の網羅的根拠は未確定 | model-local diagnosticの射程に限定 | YES | HOLD | HOLD | NO |
| INT-REV-017 | INT-CLM-017 | 正しさ蓄積はconnectivity/divergenceを増やす | P1 E/J §7 | P1-JA distributed; EN parallel/primary未決 | C5 | PARTIAL | STRONG007=OVERSTATED | CORR037:COR3/OP2; CORR038:COR2/OP1 | INT-GAP-009; OPEN004/014; SERIOUS直接対象外 | SPLIT | correctness→再利用→graph→心理発散の橋が未同定 | graph条件、認知対応、心理的帰結を分離 | YES | HOLD | HOLD | NO |
| INT-REV-018 | INT-CLM-018 | 結合数二乗・経路指数の分岐爆発 | P1 E/J §7 | P1-JA distributed; EN parallel/primary未決 | C0 | PARTIAL | STRONG008=POSSIBLY OVERSTATED | CORR037:COR3/OP2 | INT-GAP-009; OPEN014; SERIOUS直接対象外 | REVISE | 辺/経路の組合せtemplateは条件依存で実推論とは別 | 所与graphの条件付き数え上げとしてscopeを限定 | YES | HOLD | HOLD | NO |
| INT-REV-019 | INT-CLM-019 | 知識量/推論速度/専門化/能力強化だけでは止まらない | P1 E/J §7 | P1-JA distributed; EN parallel/primary未決 | C5 | PARTIAL | STRONG009=OVERSTATED | CORR022:COR3/OP2; CORR028:COR3/OP2 | INT-GAP-013; OPEN006/012/014; SERIOUS直接対象外 | DOWNGRADE | 能力/速度増強だけで停止しないという一般化は候補方向 | source-local定性的方向へ限定 | YES | NO | HOLD | NO |
| INT-REV-020 | INT-CLM-020 | overexplanation等は不安定性の4症状という読み | P1 J §7 | P1-JA distributed; EN parallel/primary未決 | C4 | PARTIAL | 62専用family対象外（強語なしという認定ではない） | CORR038:COR2/OP1 | INT-GAP-010; OPEN013/014/022; SERIOUS直接対象外 | DOWNGRADE | 四症状は独立行動criterionで確認されていない | 非clinicalなregime interpretationへ限定 | YES | NO | HOLD | NO |
| INT-REV-021 | INT-CLM-021 | 個体内推論には停止演算子がない | P1 E/J §8 | P1-JA distributed; EN parallel/primary未決 | C8 | PARTIAL | STRONG010=OVERSTATED | CORR028:COR3/OP2; CORR039:COR0/OP0 | INT-GAP-011; OPEN001/002/006; SERIOUS001 | SPLIT | 内部stop不在のsource-local論証を任意認知停止へ移す | formal stopping modelとcognitive/architecture主張を分離 | YES | HOLD | HOLD | NO |
| INT-REV-022 | INT-CLM-022 | 疲労/注意/報酬/生理終了は停止でなく中断 | P1 E/J §8（J詳細） | P1-JA distributed; EN parallel/primary未決 | C1 | PARTIAL | STRONG011=POSSIBLY OVERSTATED | CORR028:COR3/OP2 | INT-GAP-012; OPEN006; SERIOUS直接対象外 | SPLIT | 疲労後再開例は全生理的終了の分類を支えない | 中断例とgenuine-stopの全称排除を分離 | YES | NO | HOLD | NO |
| INT-REV-023 | INT-CLM-023 | paperclip/alignment問題は同じ停止不在の構造 | P1 E/J §8（J強化） | P1-JA distributed; EN parallel/primary未決 | C5 | PARTIAL | STRONG012=OVERSTATED | CORR028:COR3/OP2 | INT-GAP-013; OPEN006/016; SERIOUS直接対象外 | DOWNGRADE | paperclip例はalignment一般の原因同定ではない | 構造的thought comparisonに限定 | YES | NO | HOLD | NO |
| INT-REV-024 | INT-CLM-024 | 停止はログ・応答・合意・遅延への越境を必要とする | P1 E/J §8–9 | P1-JA distributed; EN parallel/primary未決 | C5 | PARTIAL | STRONG013=OVERSTATED | CORR017:COR3/OP2; CORR028:COR3/OP2; CORR031:COR3/OP2 | INT-GAP-014; OPEN006/007/017; SERIOUS直接対象外 | SPLIT | ログ/応答/合意/遅延の役割と越境必然性が混在 | 外化のarchitecture proposalと全称必要性を分離 | YES | HOLD | HOLD | NO |
| INT-REV-025 | INT-CLM-025 | DHIは外部停止へのlocal horizon-form | P1 E/J §9 | P1-JA distributed; EN parallel/primary未決 | C4 | PARTIAL | 62専用family対象外（強語なしという認定ではない） | CORR042:COR1/OP1 | INT-GAP-015; OPEN006/023; SERIOUS直接対象外 | REVISE | DHI命名は有用だがVED4の同じboundaryを保証しない | local horizon namingと親理論との対応scopeを区別 | YES | HOLD | HOLD | NO |
| INT-REV-026 | INT-CLM-026 | DHIはVED4とは別の第二絶対境界でない | P1 E/J §1,9 | P1-JA distributed; EN parallel/primary未決 | C0 | YES | 62専用family対象外（強語なしという認定ではない） | CORR042:COR1/OP1 | OPEN023; SERIOUS直接対象外 | KEEP | 第二絶対境界ではないというnegative scope | 新しい絶対境界の導入を防ぐguard維持 | NO | NO | NO | NO |
| INT-REV-027 | INT-CLM-027 | 外化は真理を保証せず持続/改訂可能停止を保証 | P1 E/J §9 | P1-JA distributed; EN parallel/primary未決 | C5 | PARTIAL | STRONG014=OVERSTATED | CORR028:COR3/OP2; CORR031:COR3/OP2 | INT-GAP-014; OPEN006/017; SERIOUS直接対象外 | SPLIT | truth非保証と持続/改訂のpositive guaranteeを混合 | 否定guardと外化の効果仮説を分離 | YES | NO | HOLD | NO |
| INT-REV-028 | INT-CLM-028 | 推論能力/個体理解/責任の全面外化はしない | P1 E/J §9 | P1-JA distributed; EN parallel/primary未決 | C0 | YES | 62専用family対象外（強語なしという認定ではない） | NA: negative/local scope（mapping肯定でない） | OPEN006/022; SERIOUS直接対象外 | KEEP | 能力/理解/責任の全面外化を否定するscope | 外化の対象を停止構造に限定 | NO | NO | NO | NO |
| INT-REV-029 | INT-CLM-029 | 物理/Bio/Con/Int四層はproposed comparison、型付け移送でない | P1 E/J §9 | P1-JA distributed; EN parallel/primary未決 | C4 | YES | 62専用family対象外（強語なしという認定ではない） | X1–X3（関連HOMO/XFER別、typed X4なし） | OPEN023; SERIOUS直接対象外 | KEEP | 異substrate/typed非同一のproposed比較guardがある | 四層role comparisonとして維持 | NO | NO | NO | NO |
| INT-REV-030 | INT-CLM-030 | 生命層はCon/Intを支える必要基盤というJA記述 | P1 J §9 | P1-JA distributed; EN parallel/primary未決 | C4 | PARTIAL | STRONG015=VERSION-SPECIFIC | X1–X3（関連HOMO/XFER別、typed X4なし） | INT-GAP-016; OPEN021/023; SERIOUS直接対象外 | DOWNGRADE | JA生命必要基盤をInt全般へ移す独立bridgeなし | version-specific substrate比較へ限定 | YES | HOLD | HOLD | YES |
| INT-REV-031 | INT-CLM-031 | Conのfast/slow log/windowとIntの越境の相補性 | P1 E/J §1,9 | P1-JA distributed; EN parallel/primary未決 | C3 | PARTIAL | STRONG057=POSSIBLY OVERSTATED | X1–X3（関連HOMO/XFER別、typed X4なし） | INT-GAP-016; OPEN022/023; SERIOUS直接対象外 | REVISE | Con/Int相補性は同じ過程のtyped移送ではない | 同構造/異window表現を比較scopeへ限定 | YES | HOLD | HOLD | YES |
| INT-REV-032 | INT-CLM-032 | selfを経て未来予測・言語・社会へflowback | P1 J §9; Con参照 | P1-JA distributed; EN parallel/primary未決 | C3 | PARTIAL | 62専用family対象外（強語なしという認定ではない） | X1–X3（関連HOMO/XFER別、typed X4なし） | INT-GAP-016; OPEN022/023; SERIOUS直接対象外 | DOWNGRADE | selfから言語/社会へのflowbackは観測bridge未所在 | JA提案的handoffとして限定 | YES | NO | HOLD | YES |
| INT-REV-033 | INT-CLM-033 | 六制約は必要で十分でない、complete/engineering/norm theoryでない | P1 E/J §10 | P1-JA distributed; EN parallel/primary未決 | C0 | PARTIAL | STRONG016=POSSIBLY OVERSTATED | NA: negative/local scope（mapping肯定でない） | INT-GAP-002; OPEN006/021; SERIOUS直接対象外 | SPLIT | not complete/not sufficientは保持できるが六条件の一般必要性は別 | summaryのnegative scopeとnecessary claimsを分離 | YES | HOLD | HOLD | NO |
| INT-REV-034 | INT-CLM-034 | 3条件の収束は恣意性でないことの支持 | P1 E/J §10 | P1-JA distributed; EN parallel/primary未決 | C6 | PARTIAL | STRONG058=POSSIBLY OVERSTATED | X1–X3（関連HOMO/XFER別、typed X4なし） | INT-GAP-005; OPEN015/016/023; SERIOUS直接対象外 | DOWNGRADE | 別研究起源と対応選択の独立性を混同しうる | 非恣意性の確証ではなく比較上の動機に限定 | YES | NO | HOLD | NO |
| INT-REV-035 | INT-CLM-035 | 外部停止・生命意識移行・社会制度・AI設計を後続へ | P1 E/J §10 | P1-JA distributed; EN parallel/primary未決 | C3 | YES | 62専用family対象外（強語なしという認定ではない） | NA: future/editorial（実行mappingなし） | OPEN024; SERIOUS直接対象外 | KEEP | futureに外化/社会/AI/transition課題を置く | 将来課題を実行済として扱わない | NO | NO | NO | NO |
| INT-REV-036 | INT-CLM-036 | PartIIはVED差分原理から三層構造を導出すると宣言 | P2 J §0; E abstract | P2-JA primary; EN draft（補遺は言語別） | C7 | PARTIAL | STRONG017=VERSION-SPECIFIC | X1–X3（関連HOMO/XFER別、typed X4なし） | INT-GAP-017; OPEN023; SERIOUS直接対象外 | DOWNGRADE | VED差分語彙/schemaからtyped cognitive derivationは未所在 | source reuse/動機/構成proposalへ限定 | YES | HOLD | NO | YES |
| INT-REV-037 | INT-CLM-037 | LF/LR/LEの同時動態が個体内外部依存停止を生む | P2 E/J §0,5,12 | P2-JA primary; EN draft（補遺は言語別） | C8 | PARTIAL | STRONG018=OVERSTATED | CORR016:COR3/OP2; CORR017:COR3/OP2; CORR018:COR3/OP2 | INT-GAP-021; OPEN007/008/011/021; SERIOUS002 | SPLIT | 三層の局所構成と停止生成/existence説明を束ねる | architecture naming・生成hypothesis・存在検出OPENを分離 | YES | HOLD | HOLD | NO |
| INT-REV-038 | INT-CLM-038 | 知性史は推論能力だけでなく停止構造の発達史 | P2 E/J §0 | P2-JA primary; EN draft（補遺は言語別） | C4 | PARTIAL | 62専用family対象外（強語なしという認定ではない） | CORR031:COR3/OP2; CORR032:COR3/OP2 | INT-GAP-024; OPEN018; SERIOUS直接対象外 | DOWNGRADE | 知性史を停止発達史として扱うのは歴史的検証でない | historical structural interpretationへ限定 | YES | NO | HOLD | NO |
| INT-REV-039 | INT-CLM-039 | PartI四層の継承説明（JA別表physical/relational/symbolic/cognitive） | P2 J §0.2 | P2-JA primary; EN draft（補遺は言語別） | C3 | UNRESOLVED | 62専用family対象外（強語なしという認定ではない） | X1–X3（関連HOMO/XFER別、typed X4なし） | INT-GAP-018; OPEN021/023; SERIOUS直接対象外 | OPEN | P1再掲の四層が異なる表を指し、継承対象を選べない | 参照artifact/再掲意図のauthority決定までhold | HOLD | NO | NO | YES |
| INT-REV-040 | INT-CLM-040 | Cは操作的安定性で真理でない | P2 E/J §1,10 | P2-JA primary; EN draft（補遺は言語別） | C1 | YES | 62専用family対象外（強語なしという認定ではない） | CORR006:COR2/OP1 | OPEN002/003; SERIOUS005 | KEEP | C=operational stability/not truthというlocal意味を明示 | 測定済のtruth/安定metricへ拡張しない | NO | NO | NO | NO |
| INT-REV-041 | INT-CLM-041 | closure PDE/basic VED formをIntで使用 | P2 J §1,A; E簡略 | P2-JA primary; EN draft（補遺は言語別） | C7 | PARTIAL | STRONG019=POSSIBLY OVERSTATED | CORR034:COR0/OP0 | INT-GAP-019; OPEN003/004/023; SERIOUS直接対象外 | REVISE | 式再用はあるがIntのdomain/IC/BC/継承signatureは不明 | 使用scopeをformal templateとprovenance未確定に限定 | YES | HOLD | NO | YES |
| INT-REV-042 | INT-CLM-042 | Cmax非到達と究極理解/最終判断の非到達 | P2 E/J §1,3 | P2-JA primary; EN draft（補遺は言語別） | C5 | PARTIAL | STRONG020=OVERSTATED | CORR042:COR1/OP1 | INT-GAP-015; OPEN003/006/023; SERIOUS直接対象外 | SPLIT | Cmaxのformal境界と究極理解不能という解釈は別 | barrier/不変領域問題と理解endpointを分離 | YES | HOLD | HOLD | NO |
| INT-REV-043 | INT-CLM-043 | Ωθ内(A)とθ再編(B)、領域外は発散/停止 | P2 E/J §1–2 | P2-JA primary; EN draft（補遺は言語別） | C1 | PARTIAL | STRONG021=POSSIBLY OVERSTATED | CORR013:COR2/OP1; CORR014:COR3/OP2 | INT-GAP-020; OPEN001/009; SERIOUS直接対象外 | SPLIT | A/Bの局所区分と領域外発散/停止の帰結が別 | 領域の命名と帰結の仮説を分離 | YES | HOLD | HOLD | NO |
| INT-REV-044 | INT-CLM-044 | VED-defined emergenceは下位運動+外部Hから上位動態 | P2 E/J §1,E | P2-JA primary; EN draft（補遺は言語別） | C1 | PARTIAL | STRONG022=GUARDED | CORR035:COR2/OP1 | INT-GAP-021; OPEN008/023; SERIOUS直接対象外 | SPLIT | U=Φ(L,H)はlocal schemaで実装済生成則ではない | 定義schemaとcross-domain機構を分離 | YES | HOLD | HOLD | NO |
| INT-REV-045 | INT-CLM-045 | Bio second-attractor予告に対するInt独自下流構成 | P2 E/J §1,B,E | P2-JA primary; EN draft（補遺は言語別） | C3 | YES | 62専用family対象外（強語なしという認定ではない） | X1–X3（関連HOMO/XFER別、typed X4なし） | OPEN008/023; SERIOUS直接対象外 | KEEP | Bio予告とInt固有構成を非identity/typedOPEN付きで区別 | upstream proposalをvalidationにしない | NO | NO | NO | NO |
| INT-REV-046 | INT-CLM-046 | 推論Fは既存概念地形内、確率的/反復/局所正当化 | P2 E/J §2 | P2-JA primary; EN draft（補遺は言語別） | C1 | PARTIAL | 62専用family対象外（強語なしという認定ではない） | CORR003:COR2/OP1 | INT-GAP-011; OPEN001/002/023; SERIOUS直接対象外 | SPLIT | Fの抽象役割と認知過程、single/set-valued版の差 | local operator・認知解釈・型決定を分離 | YES | HOLD | HOLD | YES |
| INT-REV-047 | INT-CLM-047 | Physarum/TransformerをF actionとして読む | P2 E/J §2,5 | P2-JA primary; EN draft（補遺は言語別） | C4 | PARTIAL | STRONG059=POSSIBLY OVERSTATED | CORR016:COR3/OP2; CORR036:COR3/OP2; CORR040:COR3/OP2 | INT-GAP-006; OPEN015/016/023; SERIOUS直接対象外 | REVISE | Physarum/TransformerのF action比較は同じFではない | 各profileのoperator役割と非同一guardを明示 | YES | HOLD | HOLD | NO |
| INT-REV-048 | INT-CLM-048 | Hij応答閾値をCij指数関係で記述 | P2 J §2 | P2-JA primary; EN draft（補遺は言語別） | C4 | PARTIAL | STRONG023=POSSIBLY OVERSTATED | CORR007:COR3/OP2; CORR020:COR3/OP2 | INT-GAP-020; OPEN003/009; SERIOUS直接対象外 | SPLIT | Cij指数関係とresponse/H閾値解釈の負担が別 | formal relationと観測候補/校正OPENを分離 | YES | HOLD | HOLD | NO |
| INT-REV-049 | INT-CLM-049 | μθは内生的閾値移動・E設置領域を組み替える | P2 E/J §2,5 | P2-JA primary; EN draft（補遺は言語別） | C5 | PARTIAL | STRONG024=POSSIBLY OVERSTATED | CORR015:COR3/OP2 | INT-GAP-022; OPEN008/009/010; SERIOUS004 | SPLIT | μのmobility定義からE-site生成への機構的拡張がある | 能力命名・内発性判定・再配置機構を分離 | YES | HOLD | HOLD | NO |
| INT-REV-050 | INT-CLM-050 | BioDNA長期とsapiens対話短期のθ可変性を同一原理で比較 | P2 J §2,B | P2-JA primary; EN draft（補遺は言語別） | C4 | PARTIAL | STRONG060=VERSION-SPECIFIC | CORR014:COR3/OP2; CORR015:COR3/OP2 | INT-GAP-016; OPEN009/023; SERIOUS直接対象外 | DOWNGRADE | DNA長期とInt短期のsame principleには共通尺度なし | time-scale/role comparisonに限定 | YES | HOLD | HOLD | YES |
| INT-REV-051 | INT-CLM-051 | P1/P2仮定下Fに内部不動点なし（定理3.1） | P2 E/J §3,D | P2-JA primary; EN draft（補遺は言語別） | C1 | PARTIAL | STRONG025=POSSIBLY OVERSTATED | CORR003:COR2/OP1; CORR004:COR1/OP1 | INT-GAP-011; OPEN001/002/006; SERIOUS001 | REVISE | strict-J/fixedθ-Aの条件付きsketchは保持対象、証明認証は未実施 | 前提・適用域・proof未監査と認知結論の非継承を明示 | YES | HOLD | NO | YES |
| INT-REV-052 | INT-CLM-052 | 任意内部停止条件Sは推論要求へ戻る（系3.2） | P2 E/J §3; J D | P2-JA primary; EN draft（補遺は言語別） | C8 | PARTIAL | STRONG026=OVERSTATED | CORR039:COR0/OP0 | INT-GAP-011; OPEN001/006; SERIOUS001 | SPLIT | S→fixedpointの定式化と任意認知停止不能を混合 | hypothetical S・F再適用・認知停止bridgeを分離 | YES | HOLD | HOLD | NO |
| INT-REV-053 | INT-CLM-053 | 非閉包とCmax/VED4horizonは同型（系3.3） | P2 E/J §3; J D | P2-JA primary; EN draft（補遺は言語別） | C6 | PARTIAL | STRONG027=OVERSTATED | CORR042:COR1/OP1 | INT-GAP-015; OPEN023; SERIOUS直接対象外 | DOWNGRADE | noFP/Cmax/DHの同じroleから数学的同型は未定義 | role analogyを残しtyped isomorphismはhold | YES | HOLD | HOLD | NO |
| INT-REV-054 | INT-CLM-054 | 個体内知性完結不能、3collapse attractorsへ | P2 E/J §3; J D | P2-JA primary; EN draft（補遺は言語別） | C8 | PARTIAL | STRONG028=OVERSTATED | CORR028:COR3/OP2 | INT-GAP-011; OPEN006/012/013; SERIOUS001 | SPLIT | LF-only制限と個体の病的collapse必然性は異なる | conditional formal scopeとcognitive regime hypothesisを分離 | YES | HOLD | HOLD | NO |
| INT-REV-055 | INT-CLM-055 | 応答的/沈黙的世界は閾値regimeでontologyでない | P2 E/J §4 | P2-JA primary; EN draft（補遺は言語別） | C1 | YES | 62専用family対象外（強語なしという認定ではない） | CORR020:COR3/OP2; CORR014:COR3/OP2 | OPEN003/009; SERIOUS直接対象外 | KEEP | 応答/沈黙を二ontologyではなくmodel-local regimeとする | 非本体論guard維持、計測完成を主張しない | NO | NO | NO | NO |
| INT-REV-056 | INT-CLM-056 | 沈黙世界でregress持続、branch explosionと同じ構造 | P2 E/J §4 | P2-JA primary; EN draft（補遺は言語別） | C0 | PARTIAL | STRONG029=POSSIBLY OVERSTATED | CORR038:COR2/OP1 | INT-GAP-011; OPEN006/014; SERIOUS直接対象外 | SPLIT | 三前提regress議論とbranch explosion/cognitive divergenceが別 | 条件付きargumentとgraph/認知対応を分離 | YES | HOLD | HOLD | NO |
| INT-REV-057 | INT-CLM-057 | nonclosureはtraceを残しLR/LE創発へproductive | P2 E/J §4–5 | P2-JA primary; EN draft（補遺は言語別） | C5 | PARTIAL | STRONG030=POSSIBLY OVERSTATED | CORR017:COR3/OP2; CORR018:COR3/OP2 | INT-GAP-021; OPEN007/008; SERIOUS002 | SPLIT | trace生成/参照とproductive nonclosureによるLE生成が別 | 痕跡/参照命名と生成仮説を分離 | YES | HOLD | HOLD | NO |
| INT-REV-058 | INT-CLM-058 | LRは推論痕跡とその再帰参照、3保存様式 | P2 E/J §5 | P2-JA primary; EN draft（補遺は言語別） | C2 | YES | 62専用family対象外（強語なしという認定ではない） | CORR017:COR3/OP2 | OPEN007; SERIOUS直接対象外 | KEEP | LRを痕跡と再参照の層と命名し保存様式を分ける | 保存の存在を参照実行の証拠へ変換しない | NO | NO | NO | NO |
| INT-REV-059 | INT-CLM-059 | LEは個体内だが外部H依存の動的stopping attractor | P2 E/J §5 | P2-JA primary; EN draft（補遺は言語別） | C1 | PARTIAL | STRONG031=POSSIBLY OVERSTATED | CORR018:COR3/OP2 | INT-GAP-021; OPEN008; SERIOUS002 | SPLIT | stopping-attractor機能定義から存在・収束を説明する | 機能命名を残し存在/収束/独立検出をOPENへ分離 | YES | HOLD | HOLD | NO |
| INT-REV-060 | INT-CLM-060 | μθ→B→E-site projection→LRconvergence→LEの機構 | P2 E/J §5 | P2-JA primary; EN draft（補遺は言語別） | C8 | PARTIAL | STRONG032=OVERSTATED | CORR015:COR3/OP2; CORR018:COR3/OP2; CORR035:COR2/OP1 | INT-GAP-021; OPEN008/009; SERIOUS002 | DOWNGRADE | 四stage arrowはexecuted update/収束機構でない | schematic qualitative mechanism hypothesisへ限定 | YES | HOLD | HOLD | NO |
| INT-REV-061 | INT-CLM-061 | Physarum autonomousenvironmentstop / Transformer injectedstop / sapiensμendo | P2 E/J §5 | P2-JA primary; EN draft（補遺は言語別） | C4 | PARTIAL | 62専用family対象外（強語なしという認定ではない） | CORR016:COR3/OP2; CORR017:COR3/OP2; CORR018:COR3/OP2; CORR019:COR3/OP2 | INT-GAP-006; OPEN008/009/015/016/021; SERIOUS直接対象外 | SPLIT | carrier例とown LE/μの有無・全称profile判定が別 | 具体比較を残し存在/不存在の独立基準をOPENへ分離 | YES | HOLD | HOLD | NO |
| INT-REV-062 | INT-CLM-062 | projectionはConの第四原語を適用、心理防衛でない | P2 E/J §5; J B | P2-JA primary; EN draft（補遺は言語別） | C7 | PARTIAL | STRONG033=POSSIBLY OVERSTATED | X1–X3（関連HOMO/XFER別、typed X4なし） | INT-GAP-004; OPEN022/023; SERIOUS直接対象外 | SPLIT | Con projection語彙と心理非同一guardは同operator具現と別 | reuse/negative guardとtyped transfer主張を分離 | YES | HOLD | HOLD | YES |
| INT-REV-063 | INT-CLM-063 | EはF反復から導出できずLEと現在stateに依存 | P2 E/J §5 | P2-JA primary; EN draft（補遺は言語別） | C1 | PARTIAL | STRONG034=POSSIBLY OVERSTATED | CORR019:COR3/OP2 | INT-GAP-021; OPEN006/008; SERIOUS002 | SPLIT | E外部作用のarchitecture記述とF非導出/作用則を束ねる | external-stop namingとformal nonderivability/updateを分離 | YES | HOLD | HOLD | NO |
| INT-REV-064 | INT-CLM-064 | Φext≡Φnet、外部性はLEnetworkの見え方 | P2 E/J §5,D | P2-JA primary; EN draft（補遺は言語別） | C8 | PARTIAL | STRONG035=OVERSTATED | CORR011:COR2/OP1; CORR012:COR2/OP1 | INT-GAP-023; OPEN011/017; SERIOUS003 | SPLIT | 二視点命名とfield-network identityが同じ説明に使われる | two-view interpretationを残しtyped identity/独立測定をhold | YES | HOLD | HOLD | NO |
| INT-REV-065 | INT-CLM-065 | P1globalΦはΦnetで具体化される | P2 E/J §5,C | P2-JA primary; EN draft（補遺は言語別） | C5 | PARTIAL | STRONG061=POSSIBLY OVERSTATED | CORR008:COR3/OP2; CORR012:COR2/OP1 | INT-GAP-023; OPEN005/011/023; SERIOUS003 | DOWNGRADE | P1 scalarbiasのnetwork実装とするmapはない | 提案的network-role refinementへ限定 | YES | HOLD | HOLD | NO |
| INT-REV-066 | INT-CLM-066 | stabilityはtruthでなくrecoverability/revisability | P2 E/J §5,10 | P2-JA primary; EN draft（補遺は言語別） | C1 | YES | 62専用family対象外（強語なしという認定ではない） | CORR006:COR2/OP1; CORR028:COR3/OP2 | OPEN002/003/017; SERIOUS005 | REVISE | Phase04 YESはlocal stability/revisability読解に限定。§5.8の『担保』を実際の安定保証へ戻さないscopeが必要 | truth非保証を保持し、revisabilityと実測stabilityの十分性を区別 | YES | NO | HOLD | NO |
| INT-REV-067 | INT-CLM-067 | animismは沈黙世界を応答的として扱う停止設置 | P2 E/J §6 | P2-JA primary; EN draft（補遺は言語別） | C4 | PARTIAL | STRONG036=POSSIBLY OVERSTATED | CORR021:COR2/OP1 | INT-GAP-024; OPEN017/018; SERIOUS直接対象外 | SPLIT | animism機能命名とchannel注入による停止生成が別 | 局所社会解釈と機構/歴史仮説を分離 | YES | NO | HOLD | NO |
| INT-REV-068 | INT-CLM-068 | animism低停止コストが普遍性を説明 | P2 J §6 | P2-JA primary; EN draft（補遺は言語別） | C5 | NO | STRONG037=OVERSTATED | CORR021:COR2/OP1 | INT-GAP-025; OPEN018/019; SERIOUS直接対象外 | DOWNGRADE | cost/母集団/史料未所在でuniversality説明のburdenが未充足 | 低costの比較仮説へ限定、普遍性の説明保証を外す方向 | YES | NO | HOLD | NO |
| INT-REV-069 | INT-CLM-069 | Godは未解決→保留演算子、中心化Φext | P2 E/J §7 | P2-JA primary; EN draft（補遺は言語別） | C1 | PARTIAL | STRONG038=POSSIBLY OVERSTATED | CORR011:COR2/OP1; CORR012:COR2/OP1 | INT-GAP-024; OPEN011/018; SERIOUS直接対象外 | SPLIT | Godの保留機能命名とoperator/歴史的中心化が別 | 非存在論的namingと社会的機構解釈を分離 | YES | HOLD | HOLD | NO |
| INT-REV-070 | INT-CLM-070 | 中心化は曖昧性を減らし安定化、単一極限は歴史終点でない | P2 E/J §7 | P2-JA primary; EN draft（補遺は言語別） | C4 | PARTIAL | STRONG039=POSSIBLY OVERSTATED | CORR011:COR2/OP1; CORR012:COR2/OP1 | INT-GAP-024; OPEN018/019; SERIOUS直接対象外 | SPLIT | 中心化効果の仮説とnonprogress guardが同居 | 効果hypothesisと歴史終点否定を分離 | YES | NO | HOLD | NO |
| INT-REV-071 | INT-CLM-071 | religionはLE世代維持・mixed responsive/silent境界管理 | P2 E/J §8 | P2-JA primary; EN draft（補遺は言語別） | C5 | PARTIAL | STRONG040=POSSIBLY OVERSTATED | CORR021:COR2/OP1; CORR031:COR3/OP2 | INT-GAP-024; OPEN018; SERIOUS直接対象外 | SPLIT | religion=維持という機能命名と世代維持/予防説明は別 | 概念的再解釈と歴史因果のburdenを分離 | YES | NO | HOLD | NO |
| INT-REV-072 | INT-CLM-072 | scienceは停止改訂制度化、religionと真理序列でない | P2 E/J §8–9,D | P2-JA primary; EN draft（補遺は言語別） | C1 | PARTIAL | 62専用family対象外（強語なしという認定ではない） | CORR031:COR3/OP2 | INT-GAP-024; OPEN018; SERIOUS直接対象外 | SPLIT | science/religion比較と真理序列否定が別 | role hypothesisとnegative guardを分離 | YES | NO | HOLD | NO |
| INT-REV-073 | INT-CLM-073 | 純粋因果推論は有限sapiensに不安定、病的引力子分類 | P2 E/J §8 | P2-JA primary; EN draft（補遺は言語別） | C5 | PARTIAL | STRONG041=OVERSTATED | CORR026:COR3/OP2 | INT-GAP-010; OPEN012/013; SERIOUS直接対象外 | DOWNGRADE | 非clinical guardは病的帰結/予防の実証を与えない | qualitative regime hypothesisとして限定 | YES | NO | HOLD | NO |
| INT-REV-074 | INT-CLM-074 | social blockchainは分散LE consensusでtechnicalcryptoでない | P2 E/J §9 | P2-JA primary; EN draft（補遺は言語別） | C2 | YES | 62専用family対象外（強語なしという認定ではない） | CORR031:COR3/OP2 | OPEN017; SERIOUS直接対象外 | KEEP | social blockchainを非cryptoのconsensus analogyと明示 | 実装protocol/測定mechanismへ昇格させない | NO | NO | NO | NO |
| INT-REV-075 | INT-CLM-075 | Gitとsocialの分岐/merge/rollback costは対称/逆 | P2 E/J §9 | P2-JA primary; EN draft（補遺は言語別） | C4 | PARTIAL | 62専用family対象外（強語なしという認定ではない） | CORR031:COR3/OP2 | INT-GAP-024; OPEN019; SERIOUS直接対象外 | DOWNGRADE | Git/social cost対比は尺度・比較data未所在 | 条件付きcomparative hypothesisに限定 | YES | NO | HOLD | NO |
| INT-REV-076 | INT-CLM-076 | legitimacyは原理的非計算可能、継続改訂条件 | P2 E/J §9 | P2-JA primary; EN draft（補遺は言語別） | C5 | NO | STRONG042=OVERSTATED | CORR032:COR3/OP2 | INT-GAP-026; OPEN019; SERIOUS直接対象外 | DOWNGRADE | 歴史依存性からprincipled noncomputabilityは定式化未所在 | 社会的文脈依存の考察を残しformal不可能性をhold | YES | HOLD | HOLD | NO |
| INT-REV-077 | INT-CLM-077 | 創造は個体でのみ、社会は事後安定化 | P2 E/J §9 | P2-JA primary; EN draft（補遺は言語別） | C5 | NO | STRONG043=OVERSTATED | CORR031:COR3/OP2 | INT-GAP-027; OPEN019; SERIOUS直接対象外 | DOWNGRADE | 個人生成/社会安定の役割割当は創造の排他性を支えない | 役割分担仮説へ限定、only-individualを一般法則にしない | YES | NO | HOLD | NO |
| INT-REV-078 | INT-CLM-078 | GettierはC≠truthのevidence、原理的解決不能というJA主張 | P2 E/J §10 | P2-JA primary; EN draft（補遺は言語別） | C8 | PARTIAL | STRONG044=OVERSTATED | CORR006:COR2/OP1; CORR029:COR2/OP1 | INT-GAP-007; OPEN002/020; SERIOUS005 | SPLIT | Gettier診断・C≠truth guardとconfirmation/原理的不可能が混在 | local interpretationと独立確認/修復排除を分離 | YES | HOLD | HOLD | YES |
| INT-REV-079 | INT-CLM-079 | knowledgeはaction可能なΦnet暫定block | P2 J §10（EN簡略） | P2-JA primary; EN draft（補遺は言語別） | C1 | YES | 62専用family対象外（強語なしという認定ではない） | CORR029:COR2/OP1; CORR031:COR3/OP2 | OPEN017/020; SERIOUS005 | KEEP | JAのknowledge=暫定blockはmodel-local naming | 一般認識論のcriterion/Φnet検証にしない | NO | NO | NO | NO |
| INT-REV-080 | INT-CLM-080 | error toleranceとμθは構造的同値 | P2 J §10,D; E弱いcoupling | P2-JA primary; EN draft（補遺は言語別） | C8 | PARTIAL | STRONG045=VERSION-SPECIFIC | CORR015:COR3/OP2 | INT-GAP-022; OPEN009/010; SERIOUS004 | SPLIT | μ可動性とerror toleranceの関連から双方向同値へ強化 | 定義/質的関係とformal equivalence/独立endpointを分離 | YES | HOLD | HOLD | YES |
| INT-REV-081 | INT-CLM-081 | 三軸相図/狭い安定帯（Σは別の発達量） | P2 E/J §11 | P2-JA primary; EN draft（補遺は言語別） | C5 | PARTIAL | STRONG046=OVERSTATED | CORR022:COR3/OP2; CORR025:COR3/OP2; CORR026:COR3/OP2; CORR027:COR1/OP1 | INT-GAP-028; OPEN012/013; SERIOUS直接対象外 | SPLIT | 三軸の候補とnarrow exclusive band/Σ混同は別 | axis naming・phase hypothesis・未較正境界を分離 | YES | HOLD | HOLD | NO |
| INT-REV-082 | INT-CLM-082 | Δvintel増大はLR/LE/μ失敗のfourfoldcollapse | P2 E/J §11 | P2-JA primary; EN draft（補遺は言語別） | C5 | PARTIAL | STRONG047=OVERSTATED | CORR024:COR3/OP2 | INT-GAP-028; OPEN012; SERIOUS直接対象外 | SPLIT | 速度差の式と四層崩壊のmechanism chainは別 | rate relationとqualitative collapse仮説を分離 | YES | HOLD | HOLD | NO |
| INT-REV-083 | INT-CLM-083 | zero motionは知性でなく不安定性は構成的 | P2 E/J §11 | P2-JA primary; EN draft（補遺は言語別） | C1 | PARTIAL | STRONG048=POSSIBLY OVERSTATED | CORR022:COR3/OP2; CORR025:COR3/OP2; CORR030:COR2/OP1 | INT-GAP-028; OPEN012/021; SERIOUS直接対象外 | SPLIT | zero-motion除外は定義、構成的不安定性の必然は拡張 | local exclusionとphase necessityを分離 | YES | NO | HOLD | NO |
| INT-REV-084 | INT-CLM-084 | highspeedautonomous human/AIは同じphase制約 | P2 E/J §11 | P2-JA primary; EN draft（補遺は言語別） | C5 | PARTIAL | 62専用family対象外（強語なしという認定ではない） | CORR022:COR3/OP2; CORR024:COR3/OP2 | INT-GAP-013; OPEN012/016/021; SERIOUS直接対象外 | DOWNGRADE | human/AI同phaseは共通observable尺度未定 | 条件付きcross-system comparisonへ限定 | YES | HOLD | HOLD | NO |
| INT-REV-085 | INT-CLM-085 | N1–6 impossibilities/R1–6 necessities/S1sapiens条件 | P2 J §12; E7clauses | P2-JA primary; EN draft（補遺は言語別） | C5 | PARTIAL | STRONG049=VERSION-SPECIFIC | CORR030:COR2/OP1 | INT-GAP-029; OPEN021/023; SERIOUS直接対象外 | SPLIT | N/R/SとEN七条項はscope/必要性が異なる | general local clauses・sapiens追加・全称必要性を分離 | YES | HOLD | HOLD | YES |
| INT-REV-086 | INT-CLM-086 | 一般知性はLF+LR+LE、sapiensはμ移動性追加 | P2 J §12; E §12 | P2-JA primary; EN draft（補遺は言語別） | C1 | PARTIAL | STRONG050=OVERSTATED | CORR030:COR2/OP1; CORR015:COR3/OP2 | INT-GAP-029; OPEN009/021; SERIOUS004 | SPLIT | 一般local定義とsapiensμ追加を普遍criterionへ拡張 | 二つのlocal profileと一般必要十分burdenを分離 | YES | HOLD | HOLD | NO |
| INT-REV-087 | INT-CLM-087 | 停止と可動性が自由な推論を可能にする | P2 E/J §0,5,12 | P2-JA primary; EN draft（補遺は言語別） | C5 | PARTIAL | STRONG051=POSSIBLY OVERSTATED | CORR015:COR3/OP2; CORR018:COR3/OP2 | INT-GAP-022; OPEN009/021/022; SERIOUS004 | SPLIT | free inferenceの機能語と可動停止の必要性/自由読解が別 | I2機能解釈を残し必要性・I4への拡張を分離 | YES | HOLD | HOLD | NO |
| INT-REV-088 | INT-CLM-088 | 理論は使用法/制度正統性/倫理/AGI設計を決定しない | P2 E/J §0,13 | P2-JA primary; EN draft（補遺は言語別） | C0 | YES | 62専用family対象外（強語なしという認定ではない） | NA: negative/local scope（mapping肯定でない） | OPEN024; SERIOUS直接対象外 | KEEP | 倫理/正統性/AGI設計を決定しないnegative scope | positive支持に加算せずscope維持 | NO | NO | NO | NO |
| INT-REV-089 | INT-CLM-089 | Σ定量化・stoppingfunctional・哲学/AI実践はfuture | P2 E/J §5,13,D,E | P2-JA primary; EN draft（補遺は言語別） | C3 | YES | STRONG052=GUARDED | NA: future/editorial（実行mappingなし） | OPEN013/024; SERIOUS直接対象外 | KEEP | Σ/functional/philosophy/AIを明示的futureとする | 実行/成功を暗示しない。093の本文補遺差は別管理 | NO | NO | NO | NO |
| INT-REV-090 | INT-CLM-090 | Masterv2.2はv2.1継承+Int追加と宣言 | P2 J A; E A辞書 | P2-JA primary; EN draft（補遺は言語別） | C7 | UNRESOLVED | 62専用family対象外（強語なしという認定ではない） | X1–X3（関連HOMO/XFER別、typed X4なし） | INT-GAP-030; OPEN023; SERIOUS直接対象外 | OPEN | v2.1というexact predecessorが未所在で再録内容を選べない | Master artifact/versionのauthority決定までhold | HOLD | HOLD | NO | YES |
| INT-REV-091 | INT-CLM-091 | appendixBはCTを含むnonclosure/attractor/horizon対応を拡張 | P2 J B; E B短縮 | P2-JA primary; EN draft（補遺は言語別） | C4 | YES | STRONG062=GUARDED | X1–X3（関連HOMO/XFER別、typed X4なし） | OPEN023; SERIOUS直接対象外 | KEEP | Bの比較拡張とtyped OPEN guardはdocumented comparison | 同型検証へ昇格させない | NO | NO | NO | NO |
| INT-REV-092 | INT-CLM-092 | appendixCはPartIへの4微修正を提案 | P2 J C; §13 | P2-JA primary; EN draft（補遺は言語別） | C3 | YES | 62専用family対象外（強語なしという認定ではない） | NA: future/editorial（実行mappingなし） | OPEN024; SERIOUS直接対象外 | KEEP | P1四微修正はeditorial future | 実装済・現行P1authorityとして扱わない | NO | NO | NO | NO |
| INT-REV-093 | INT-CLM-093 | appendixEはemergence比較とLElocalminの記述を追加 | P2 E/J E | P2-JA primary; EN draft（補遺は言語別） | C6 | UNRESOLVED | STRONG053=UNRESOLVED | CORR035:COR2/OP1; CORR018:COR3/OP2 | INT-GAP-031; OPEN008/023/024; SERIOUS直接対象外 | SPLIT | 有用emergence比較とLElocalmin現在形/future差は別 | role比較を保持しfunctional採用状態をauthority OPENへ分離 | YES | HOLD | NO | YES |
| INT-REV-094 | INT-CLM-094 | AI costをstoppingcostとして読む | P2 E D; revision_notes | P2-JA primary; EN draft（補遺は言語別） | C4 | YES | 62専用family対象外（強語なしという認定ではない） | CORR019:COR3/OP2 | OPEN016/024; SERIOUS直接対象外 | KEEP | EN DのAIcostはfuture comparisonとして限定される | JAへ自動移植/測定済cost扱いしない | NO | NO | NO | NO |
| INT-REV-095 | INT-CLM-095 | NGs：religion/culture/truthhierarchy/clinicalanthropomorphism除外 | P2 E/J §0,8,D | P2-JA primary; EN draft（補遺は言語別） | C0 | YES | 62専用family対象外（強語なしという認定ではない） | NA: negative/local scope（mapping肯定でない） | OPEN013/018/022; SERIOUS直接対象外 | KEEP | culture/religion/clinical/anthropomorphismのnegative scope | 本文のpositive mechanismsのsupportと非合算 | NO | NO | NO | NO |

## 4. KEEP candidates

24件。local definition/negative guard/guarded comparison/future記述を保持する。近接strong claimは別familyまたはSPLIT childとして扱うため、KEEPのscopeをsummaryで拡大しない。特に011と012、040と078、058と059、074と075–077、089と093を独立に保つ。

| candidate ID | primary claim / REV | 保持/調整する内容 | 必要最小方向 | research/authority boundary |
|---|---|---|---|---|
| INT-KEEP-CAND-001 | INT-CLM-001 / INT-REV-001 | 枠組み内の持続動態という定義を明示。経験的知性criterionと別 | 局所定義のscopeを維持 | F:NO / E:NO / A:NO; OPEN021 |
| INT-KEEP-CAND-002 | INT-CLM-002 / INT-REV-002 | P1の知覚/認識/知識/知性を役割分解として保持できる | 四役割のlocal性を維持。P2別表の問題は039へ | F:NO / E:NO / A:NO; OPEN021 |
| INT-KEEP-CAND-003 | INT-CLM-003 / INT-REV-003 | knowledge=暫定停止という命名とnot truthを別scopeで支持 | 定義をGettier確認の証拠へ再利用しない | F:NO / E:NO / A:NO; OPEN002/020 |
| INT-KEEP-CAND-004 | INT-CLM-006 / INT-REV-006 | connectedをcontinuousに限定しない明示的local scope | 離散reachabilityを許す定義を保持 | F:NO / E:NO / A:NO; OPEN001 |
| INT-KEEP-CAND-005 | INT-CLM-009 / INT-REV-009 | 三公理の論理独立と語彙採用scopeのguard | upstream validityを前提化しない | F:NO / E:NO / A:NO; OPEN023 |
| INT-KEEP-CAND-006 | INT-CLM-010 / INT-REV-010 | projected coordinatesとgeneral IFGT非同定が明示 | glyph同一性をobject identityへ移さない | F:NO / E:NO / A:NO; OPEN004/005/023 |
| INT-KEEP-CAND-007 | INT-CLM-011 / INT-REV-011 | Q/D/BC対応表はstrict mathematical identity否定付き | lexical/role comparisonに限定。012の確認主張と非合算 | F:NO / E:NO / A:NO; OPEN015/023 |
| INT-KEEP-CAND-008 | INT-CLM-014 / INT-REV-014 | cognition/experience/ethical identityの否定を明示 | 否定guardを維持しpositive supportへ数えない | F:NO / E:NO / A:NO; OPEN022/023 |
| INT-KEEP-CAND-009 | INT-CLM-026 / INT-REV-026 | 第二絶対境界ではないというnegative scope | 新しい絶対境界の導入を防ぐguard維持 | F:NO / E:NO / A:NO; OPEN023 |
| INT-KEEP-CAND-010 | INT-CLM-028 / INT-REV-028 | 能力/理解/責任の全面外化を否定するscope | 外化の対象を停止構造に限定 | F:NO / E:NO / A:NO; OPEN006/022 |
| INT-KEEP-CAND-011 | INT-CLM-029 / INT-REV-029 | 異substrate/typed非同一のproposed比較guardがある | 四層role comparisonとして維持 | F:NO / E:NO / A:NO; OPEN023 |
| INT-KEEP-CAND-012 | INT-CLM-035 / INT-REV-035 | futureに外化/社会/AI/transition課題を置く | 将来課題を実行済として扱わない | F:NO / E:NO / A:NO; OPEN024 |
| INT-KEEP-CAND-013 | INT-CLM-040 / INT-REV-040 | C=operational stability/not truthというlocal意味を明示 | 測定済のtruth/安定metricへ拡張しない | F:NO / E:NO / A:NO; OPEN002/003 |
| INT-KEEP-CAND-014 | INT-CLM-045 / INT-REV-045 | Bio予告とInt固有構成を非identity/typedOPEN付きで区別 | upstream proposalをvalidationにしない | F:NO / E:NO / A:NO; OPEN008/023 |
| INT-KEEP-CAND-015 | INT-CLM-055 / INT-REV-055 | 応答/沈黙を二ontologyではなくmodel-local regimeとする | 非本体論guard維持、計測完成を主張しない | F:NO / E:NO / A:NO; OPEN003/009 |
| INT-KEEP-CAND-016 | INT-CLM-058 / INT-REV-058 | LRを痕跡と再参照の層と命名し保存様式を分ける | 保存の存在を参照実行の証拠へ変換しない | F:NO / E:NO / A:NO; OPEN007 |
| INT-KEEP-CAND-017 | INT-CLM-074 / INT-REV-074 | social blockchainを非cryptoのconsensus analogyと明示 | 実装protocol/測定mechanismへ昇格させない | F:NO / E:NO / A:NO; OPEN017 |
| INT-KEEP-CAND-018 | INT-CLM-079 / INT-REV-079 | JAのknowledge=暫定blockはmodel-local naming | 一般認識論のcriterion/Φnet検証にしない | F:NO / E:NO / A:NO; OPEN017/020 |
| INT-KEEP-CAND-019 | INT-CLM-088 / INT-REV-088 | 倫理/正統性/AGI設計を決定しないnegative scope | positive支持に加算せずscope維持 | F:NO / E:NO / A:NO; OPEN024 |
| INT-KEEP-CAND-020 | INT-CLM-089 / INT-REV-089 | Σ/functional/philosophy/AIを明示的futureとする | 実行/成功を暗示しない。093の本文補遺差は別管理 | F:NO / E:NO / A:NO; OPEN013/024 |
| INT-KEEP-CAND-021 | INT-CLM-091 / INT-REV-091 | Bの比較拡張とtyped OPEN guardはdocumented comparison | 同型検証へ昇格させない | F:NO / E:NO / A:NO; OPEN023 |
| INT-KEEP-CAND-022 | INT-CLM-092 / INT-REV-092 | P1四微修正はeditorial future | 実装済・現行P1authorityとして扱わない | F:NO / E:NO / A:NO; OPEN024 |
| INT-KEEP-CAND-023 | INT-CLM-094 / INT-REV-094 | EN DのAIcostはfuture comparisonとして限定される | JAへ自動移植/測定済cost扱いしない | F:NO / E:NO / A:NO; OPEN016/024 |
| INT-KEEP-CAND-024 | INT-CLM-095 / INT-REV-095 | culture/religion/clinical/anthropomorphismのnegative scope | 本文のpositive mechanismsのsupportと非合算 | F:NO / E:NO / A:NO; OPEN013/018/022 |

## 5. REVISE candidates

8件。weakeningのみでなくscope・語義・authority境界の明示が中心。051の条件付きtheoremは無効認定せず、前提と認知解釈の非継承を露出させる。066はsource-local読解のYESを保つが、『担保』を独立stability保証へ戻さない限定が必要。

| candidate ID | primary claim / REV | 保持/調整する内容 | 必要最小方向 | research/authority boundary |
|---|---|---|---|---|
| INT-REVISE-CAND-001 | INT-CLM-007 / INT-REV-007 | ordered updateはあるが順序だけでは履歴保持を保証しない | orderingと履歴利用の含意を区別 | F:HOLD / E:HOLD / A:NO; OPEN001/007/023 |
| INT-REVISE-CAND-002 | INT-CLM-018 / INT-REV-018 | 辺/経路の組合せtemplateは条件依存で実推論とは別 | 所与graphの条件付き数え上げとしてscopeを限定 | F:HOLD / E:HOLD / A:NO; OPEN014 |
| INT-REVISE-CAND-003 | INT-CLM-025 / INT-REV-025 | DHI命名は有用だがVED4の同じboundaryを保証しない | local horizon namingと親理論との対応scopeを区別 | F:HOLD / E:HOLD / A:NO; OPEN006/023 |
| INT-REVISE-CAND-004 | INT-CLM-031 / INT-REV-031 | Con/Int相補性は同じ過程のtyped移送ではない | 同構造/異window表現を比較scopeへ限定 | F:HOLD / E:HOLD / A:YES; OPEN022/023 |
| INT-REVISE-CAND-005 | INT-CLM-041 / INT-REV-041 | 式再用はあるがIntのdomain/IC/BC/継承signatureは不明 | 使用scopeをformal templateとprovenance未確定に限定 | F:HOLD / E:NO / A:YES; OPEN003/004/023 |
| INT-REVISE-CAND-006 | INT-CLM-047 / INT-REV-047 | Physarum/TransformerのF action比較は同じFではない | 各profileのoperator役割と非同一guardを明示 | F:HOLD / E:HOLD / A:NO; OPEN015/016/023 |
| INT-REVISE-CAND-007 | INT-CLM-051 / INT-REV-051 | strict-J/fixedθ-Aの条件付きsketchは保持対象、証明認証は未実施 | 前提・適用域・proof未監査と認知結論の非継承を明示 | F:HOLD / E:NO / A:YES; OPEN001/002/006 |
| INT-REVISE-CAND-008 | INT-CLM-066 / INT-REV-066 | Phase04 YESはlocal stability/revisability読解に限定。§5.8の『担保』を実際の安定保証へ戻さないscopeが必要 | truth非保証を保持し、revisabilityと実測stabilityの十分性を区別 | F:NO / E:HOLD / A:NO; OPEN002/003/017 |

## 6. DOWNGRADE candidates

20件。弱い有用なrole/方向/比較を残せるためRETIREやparent OPENへはしない。数学的証明の不正を理由にせず、独立bridge/supportの未所在とcurrent wordingの射程を根拠にする。保留するformal/evidence workはOPEN routesへ残る。

| candidate ID | primary claim / REV | 保持/調整する内容 | 必要最小方向 | research/authority boundary |
|---|---|---|---|---|
| INT-DOWN-CAND-001 | INT-CLM-012 / INT-REV-012 | 外部研究起源はInt固有Φ非還元性の独立確認でない | convergenceの強度を比較上のmotivationへ下げる | F:NO / E:HOLD / A:NO; OPEN005/015/023 |
| INT-DOWN-CAND-002 | INT-CLM-016 / INT-REV-016 | 全JTB修復に及ぶ不可能性の網羅的根拠は未確定 | model-local diagnosticの射程に限定 | F:HOLD / E:HOLD / A:NO; OPEN002/020 |
| INT-DOWN-CAND-003 | INT-CLM-019 / INT-REV-019 | 能力/速度増強だけで停止しないという一般化は候補方向 | source-local定性的方向へ限定 | F:NO / E:HOLD / A:NO; OPEN006/012/014 |
| INT-DOWN-CAND-004 | INT-CLM-020 / INT-REV-020 | 四症状は独立行動criterionで確認されていない | 非clinicalなregime interpretationへ限定 | F:NO / E:HOLD / A:NO; OPEN013/014/022 |
| INT-DOWN-CAND-005 | INT-CLM-023 / INT-REV-023 | paperclip例はalignment一般の原因同定ではない | 構造的thought comparisonに限定 | F:NO / E:HOLD / A:NO; OPEN006/016 |
| INT-DOWN-CAND-006 | INT-CLM-030 / INT-REV-030 | JA生命必要基盤をInt全般へ移す独立bridgeなし | version-specific substrate比較へ限定 | F:HOLD / E:HOLD / A:YES; OPEN021/023 |
| INT-DOWN-CAND-007 | INT-CLM-032 / INT-REV-032 | selfから言語/社会へのflowbackは観測bridge未所在 | JA提案的handoffとして限定 | F:NO / E:HOLD / A:YES; OPEN022/023 |
| INT-DOWN-CAND-008 | INT-CLM-034 / INT-REV-034 | 別研究起源と対応選択の独立性を混同しうる | 非恣意性の確証ではなく比較上の動機に限定 | F:NO / E:HOLD / A:NO; OPEN015/016/023 |
| INT-DOWN-CAND-009 | INT-CLM-036 / INT-REV-036 | VED差分語彙/schemaからtyped cognitive derivationは未所在 | source reuse/動機/構成proposalへ限定 | F:HOLD / E:NO / A:YES; OPEN023 |
| INT-DOWN-CAND-010 | INT-CLM-038 / INT-REV-038 | 知性史を停止発達史として扱うのは歴史的検証でない | historical structural interpretationへ限定 | F:NO / E:HOLD / A:NO; OPEN018 |
| INT-DOWN-CAND-011 | INT-CLM-050 / INT-REV-050 | DNA長期とInt短期のsame principleには共通尺度なし | time-scale/role comparisonに限定 | F:HOLD / E:HOLD / A:YES; OPEN009/023 |
| INT-DOWN-CAND-012 | INT-CLM-053 / INT-REV-053 | noFP/Cmax/DHの同じroleから数学的同型は未定義 | role analogyを残しtyped isomorphismはhold | F:HOLD / E:HOLD / A:NO; OPEN023 |
| INT-DOWN-CAND-013 | INT-CLM-060 / INT-REV-060 | 四stage arrowはexecuted update/収束機構でない | schematic qualitative mechanism hypothesisへ限定 | F:HOLD / E:HOLD / A:NO; OPEN008/009 |
| INT-DOWN-CAND-014 | INT-CLM-065 / INT-REV-065 | P1 scalarbiasのnetwork実装とするmapはない | 提案的network-role refinementへ限定 | F:HOLD / E:HOLD / A:NO; OPEN005/011/023 |
| INT-DOWN-CAND-015 | INT-CLM-068 / INT-REV-068 | cost/母集団/史料未所在でuniversality説明のburdenが未充足 | 低costの比較仮説へ限定、普遍性の説明保証を外す方向 | F:NO / E:HOLD / A:NO; OPEN018/019 |
| INT-DOWN-CAND-016 | INT-CLM-073 / INT-REV-073 | 非clinical guardは病的帰結/予防の実証を与えない | qualitative regime hypothesisとして限定 | F:NO / E:HOLD / A:NO; OPEN012/013 |
| INT-DOWN-CAND-017 | INT-CLM-075 / INT-REV-075 | Git/social cost対比は尺度・比較data未所在 | 条件付きcomparative hypothesisに限定 | F:NO / E:HOLD / A:NO; OPEN019 |
| INT-DOWN-CAND-018 | INT-CLM-076 / INT-REV-076 | 歴史依存性からprincipled noncomputabilityは定式化未所在 | 社会的文脈依存の考察を残しformal不可能性をhold | F:HOLD / E:HOLD / A:NO; OPEN019 |
| INT-DOWN-CAND-019 | INT-CLM-077 / INT-REV-077 | 個人生成/社会安定の役割割当は創造の排他性を支えない | 役割分担仮説へ限定、only-individualを一般法則にしない | F:NO / E:HOLD / A:NO; OPEN019 |
| INT-DOWN-CAND-020 | INT-CLM-084 / INT-REV-084 | human/AI同phaseは共通observable尺度未定 | 条件付きcross-system comparisonへ限定 | F:HOLD / E:HOLD / A:NO; OPEN012/016/021 |

## 7. SPLIT candidates

41件。各parentのchild planは§12に一対一記録。SPLITは必要なDOWNGRADEを回避するラベルではなく、weak/local/negative成分を失わずstrong成分を明示的に弱化またはholdする方法。共通sourceを用いる子成分は独立な証拠として合算しない。

| candidate ID | primary claim / REV | 保持/調整する内容 | 必要最小方向 | research/authority boundary |
|---|---|---|---|---|
| INT-SPLIT-CAND-001 | INT-CLM-004 / INT-REV-004 | motionの命名と全層横断・生成/保存不能の機構読解が混在 | 定義と生成/保存一般化を分離 | F:HOLD / E:HOLD / A:NO; OPEN001/007/021 |
| INT-SPLIT-CAND-002 | INT-CLM-005 / INT-REV-005 | 三条件の構成と一般共同必要性は負担が異なる | axioms定義・lower-bound仮説・not sufficient guardを分離 | F:HOLD / E:HOLD / A:NO; OPEN001/005/021 |
| INT-SPLIT-CAND-003 | INT-CLM-008 / INT-REV-008 | scalar global mapと局所則への非還元性を一体化 | map/role定義とirreducibility主張を分離 | F:HOLD / E:HOLD / A:NO; OPEN005 |
| INT-SPLIT-CAND-004 | INT-CLM-013 / INT-REV-013 | 具体carrier対応と同じ公理充足の一般化が混在 | 3profile比較と検証/必要性の拡張を分離 | F:HOLD / E:HOLD / A:NO; OPEN015/016/021/023 |
| INT-SPLIT-CAND-005 | INT-CLM-015 / INT-REV-015 | Gettierを用いた再記述と理論確認の負担が異なる | diagnostic interpretationとindependent confirmationを分離 | F:NO / E:HOLD / A:NO; OPEN002/020 |
| INT-SPLIT-CAND-006 | INT-CLM-017 / INT-REV-017 | correctness→再利用→graph→心理発散の橋が未同定 | graph条件、認知対応、心理的帰結を分離 | F:HOLD / E:HOLD / A:NO; OPEN004/014 |
| INT-SPLIT-CAND-007 | INT-CLM-021 / INT-REV-021 | 内部stop不在のsource-local論証を任意認知停止へ移す | formal stopping modelとcognitive/architecture主張を分離 | F:HOLD / E:HOLD / A:NO; OPEN001/002/006 |
| INT-SPLIT-CAND-008 | INT-CLM-022 / INT-REV-022 | 疲労後再開例は全生理的終了の分類を支えない | 中断例とgenuine-stopの全称排除を分離 | F:NO / E:HOLD / A:NO; OPEN006 |
| INT-SPLIT-CAND-009 | INT-CLM-024 / INT-REV-024 | ログ/応答/合意/遅延の役割と越境必然性が混在 | 外化のarchitecture proposalと全称必要性を分離 | F:HOLD / E:HOLD / A:NO; OPEN006/007/017 |
| INT-SPLIT-CAND-010 | INT-CLM-027 / INT-REV-027 | truth非保証と持続/改訂のpositive guaranteeを混合 | 否定guardと外化の効果仮説を分離 | F:NO / E:HOLD / A:NO; OPEN006/017 |
| INT-SPLIT-CAND-011 | INT-CLM-033 / INT-REV-033 | not complete/not sufficientは保持できるが六条件の一般必要性は別 | summaryのnegative scopeとnecessary claimsを分離 | F:HOLD / E:HOLD / A:NO; OPEN006/021 |
| INT-SPLIT-CAND-012 | INT-CLM-037 / INT-REV-037 | 三層の局所構成と停止生成/existence説明を束ねる | architecture naming・生成hypothesis・存在検出OPENを分離 | F:HOLD / E:HOLD / A:NO; OPEN007/008/011/021 |
| INT-SPLIT-CAND-013 | INT-CLM-042 / INT-REV-042 | Cmaxのformal境界と究極理解不能という解釈は別 | barrier/不変領域問題と理解endpointを分離 | F:HOLD / E:HOLD / A:NO; OPEN003/006/023 |
| INT-SPLIT-CAND-014 | INT-CLM-043 / INT-REV-043 | A/Bの局所区分と領域外発散/停止の帰結が別 | 領域の命名と帰結の仮説を分離 | F:HOLD / E:HOLD / A:NO; OPEN001/009 |
| INT-SPLIT-CAND-015 | INT-CLM-044 / INT-REV-044 | U=Φ(L,H)はlocal schemaで実装済生成則ではない | 定義schemaとcross-domain機構を分離 | F:HOLD / E:HOLD / A:NO; OPEN008/023 |
| INT-SPLIT-CAND-016 | INT-CLM-046 / INT-REV-046 | Fの抽象役割と認知過程、single/set-valued版の差 | local operator・認知解釈・型決定を分離 | F:HOLD / E:HOLD / A:YES; OPEN001/002/023 |
| INT-SPLIT-CAND-017 | INT-CLM-048 / INT-REV-048 | Cij指数関係とresponse/H閾値解釈の負担が別 | formal relationと観測候補/校正OPENを分離 | F:HOLD / E:HOLD / A:NO; OPEN003/009 |
| INT-SPLIT-CAND-018 | INT-CLM-049 / INT-REV-049 | μのmobility定義からE-site生成への機構的拡張がある | 能力命名・内発性判定・再配置機構を分離 | F:HOLD / E:HOLD / A:NO; OPEN008/009/010 |
| INT-SPLIT-CAND-019 | INT-CLM-052 / INT-REV-052 | S→fixedpointの定式化と任意認知停止不能を混合 | hypothetical S・F再適用・認知停止bridgeを分離 | F:HOLD / E:HOLD / A:NO; OPEN001/006 |
| INT-SPLIT-CAND-020 | INT-CLM-054 / INT-REV-054 | LF-only制限と個体の病的collapse必然性は異なる | conditional formal scopeとcognitive regime hypothesisを分離 | F:HOLD / E:HOLD / A:NO; OPEN006/012/013 |
| INT-SPLIT-CAND-021 | INT-CLM-056 / INT-REV-056 | 三前提regress議論とbranch explosion/cognitive divergenceが別 | 条件付きargumentとgraph/認知対応を分離 | F:HOLD / E:HOLD / A:NO; OPEN006/014 |
| INT-SPLIT-CAND-022 | INT-CLM-057 / INT-REV-057 | trace生成/参照とproductive nonclosureによるLE生成が別 | 痕跡/参照命名と生成仮説を分離 | F:HOLD / E:HOLD / A:NO; OPEN007/008 |
| INT-SPLIT-CAND-023 | INT-CLM-059 / INT-REV-059 | stopping-attractor機能定義から存在・収束を説明する | 機能命名を残し存在/収束/独立検出をOPENへ分離 | F:HOLD / E:HOLD / A:NO; OPEN008 |
| INT-SPLIT-CAND-024 | INT-CLM-061 / INT-REV-061 | carrier例とown LE/μの有無・全称profile判定が別 | 具体比較を残し存在/不存在の独立基準をOPENへ分離 | F:HOLD / E:HOLD / A:NO; OPEN008/009/015/016/021 |
| INT-SPLIT-CAND-025 | INT-CLM-062 / INT-REV-062 | Con projection語彙と心理非同一guardは同operator具現と別 | reuse/negative guardとtyped transfer主張を分離 | F:HOLD / E:HOLD / A:YES; OPEN022/023 |
| INT-SPLIT-CAND-026 | INT-CLM-063 / INT-REV-063 | E外部作用のarchitecture記述とF非導出/作用則を束ねる | external-stop namingとformal nonderivability/updateを分離 | F:HOLD / E:HOLD / A:NO; OPEN006/008 |
| INT-SPLIT-CAND-027 | INT-CLM-064 / INT-REV-064 | 二視点命名とfield-network identityが同じ説明に使われる | two-view interpretationを残しtyped identity/独立測定をhold | F:HOLD / E:HOLD / A:NO; OPEN011/017 |
| INT-SPLIT-CAND-028 | INT-CLM-067 / INT-REV-067 | animism機能命名とchannel注入による停止生成が別 | 局所社会解釈と機構/歴史仮説を分離 | F:NO / E:HOLD / A:NO; OPEN017/018 |
| INT-SPLIT-CAND-029 | INT-CLM-069 / INT-REV-069 | Godの保留機能命名とoperator/歴史的中心化が別 | 非存在論的namingと社会的機構解釈を分離 | F:HOLD / E:HOLD / A:NO; OPEN011/018 |
| INT-SPLIT-CAND-030 | INT-CLM-070 / INT-REV-070 | 中心化効果の仮説とnonprogress guardが同居 | 効果hypothesisと歴史終点否定を分離 | F:NO / E:HOLD / A:NO; OPEN018/019 |
| INT-SPLIT-CAND-031 | INT-CLM-071 / INT-REV-071 | religion=維持という機能命名と世代維持/予防説明は別 | 概念的再解釈と歴史因果のburdenを分離 | F:NO / E:HOLD / A:NO; OPEN018 |
| INT-SPLIT-CAND-032 | INT-CLM-072 / INT-REV-072 | science/religion比較と真理序列否定が別 | role hypothesisとnegative guardを分離 | F:NO / E:HOLD / A:NO; OPEN018 |
| INT-SPLIT-CAND-033 | INT-CLM-078 / INT-REV-078 | Gettier診断・C≠truth guardとconfirmation/原理的不可能が混在 | local interpretationと独立確認/修復排除を分離 | F:HOLD / E:HOLD / A:YES; OPEN002/020 |
| INT-SPLIT-CAND-034 | INT-CLM-080 / INT-REV-080 | μ可動性とerror toleranceの関連から双方向同値へ強化 | 定義/質的関係とformal equivalence/独立endpointを分離 | F:HOLD / E:HOLD / A:YES; OPEN009/010 |
| INT-SPLIT-CAND-035 | INT-CLM-081 / INT-REV-081 | 三軸の候補とnarrow exclusive band/Σ混同は別 | axis naming・phase hypothesis・未較正境界を分離 | F:HOLD / E:HOLD / A:NO; OPEN012/013 |
| INT-SPLIT-CAND-036 | INT-CLM-082 / INT-REV-082 | 速度差の式と四層崩壊のmechanism chainは別 | rate relationとqualitative collapse仮説を分離 | F:HOLD / E:HOLD / A:NO; OPEN012 |
| INT-SPLIT-CAND-037 | INT-CLM-083 / INT-REV-083 | zero-motion除外は定義、構成的不安定性の必然は拡張 | local exclusionとphase necessityを分離 | F:NO / E:HOLD / A:NO; OPEN012/021 |
| INT-SPLIT-CAND-038 | INT-CLM-085 / INT-REV-085 | N/R/SとEN七条項はscope/必要性が異なる | general local clauses・sapiens追加・全称必要性を分離 | F:HOLD / E:HOLD / A:YES; OPEN021/023 |
| INT-SPLIT-CAND-039 | INT-CLM-086 / INT-REV-086 | 一般local定義とsapiensμ追加を普遍criterionへ拡張 | 二つのlocal profileと一般必要十分burdenを分離 | F:HOLD / E:HOLD / A:NO; OPEN009/021 |
| INT-SPLIT-CAND-040 | INT-CLM-087 / INT-REV-087 | free inferenceの機能語と可動停止の必要性/自由読解が別 | I2機能解釈を残し必要性・I4への拡張を分離 | F:HOLD / E:HOLD / A:NO; OPEN009/021/022 |
| INT-SPLIT-CAND-041 | INT-CLM-093 / INT-REV-093 | 有用emergence比較とLElocalmin現在形/future差は別 | role比較を保持しfunctional採用状態をauthority OPENへ分離 | F:HOLD / E:NO / A:YES; OPEN008/023/024 |

## 8. RETIRE candidates

0件。INT-RETIRE-CAND-001は発行しない。NO supportの068/076/077にも比較仮説/社会的考察としてdistinct contentが残り、削除を優先する根拠はない。SERIOUS candidateを理由にclaimを退役させない。

## 9. OPEN candidates

2件。39は継承対象の四層を選ぶこと、90はexact Master predecessorを指定すること自体がauthority未解決である。弱いprovenance noteを書ける可能性と、parentの継承内容を安全に決められることは別。093は比較を保持できるためparent SPLITとし、localminimumのchildだけauthority OPENへ置く。これらの区別をPhase07で再検査する。

| candidate ID | primary claim / REV | 保持/調整する内容 | 必要最小方向 | research/authority boundary |
|---|---|---|---|---|
| INT-OPEN-CAND-001 | INT-CLM-039 / INT-REV-039 | P1再掲の四層が異なる表を指し、継承対象を選べない | 参照artifact/再掲意図のauthority決定までhold | F:NO / E:NO / A:YES; OPEN021/023 |
| INT-OPEN-CAND-002 | INT-CLM-090 / INT-REV-090 | v2.1というexact predecessorが未所在で再録内容を選べない | Master artifact/versionのauthority決定までhold | F:HOLD / E:NO / A:YES; OPEN023 |

## 10. SERIOUS candidate synthesis

sourceは未変更であり5件ともPhase03 RETAINを維持する。Phase04/05のCRITICAL/STRONGはburden分類、ここでのprovisional split/downgradeで循環性をresolveしない。weak readingに独立実証が既にあるとも主張しない。

| SERREV | SERIOUS | Phase03 | Phase04 evidence | Phase05 correspondence | target / provisional treatment | weak reading | strong reading | retainable now | OPEN content | wording direction | split? / routes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| INT-SERREV-001 | INT-SERIOUS-001 | RETAIN | EVIDENCE GAP CRITICAL | CORRESPONDENCE GAP CRITICAL | 内部認知停止: 021 SPLIT / 051 REVISE / 052,054 SPLIT | strict-J/fixedθ-Aのconditional statementとSというformal model | 任意の認知停止の不可能・外部停止必然 | 条件とmodel-local停止の区分 | 停止classifier/認知bridge/前提の適用域 | cognitive impossibility/necessityをconditional proposalへ | YES; OPEN001/002/006 |
| INT-SERREV-002 | INT-SERIOUS-002 | RETAIN | EVIDENCE GAP CRITICAL | CORRESPONDENCE GAP CRITICAL | LE emergence: 037,057,059 SPLIT / 060 DOWNGRADE / 063 SPLIT | 機能命名・LR/H/LEのarchitecture schema | 存在・収束・停止生成mechanismの確立 | local architectureと具体profile比較 | LE独立検出、更新/収束、存在 | 生成保証をqualitative mechanism hypothesisへ | YES; OPEN007/008/009 |
| INT-SERREV-003 | INT-SERIOUS-003 | RETAIN | EVIDENCE GAP CRITICAL | CORRESPONDENCE GAP CRITICAL | Φext / Φnet: 064 SPLIT / 065 DOWNGRADE | 二面性/共有参照のmodel-local naming | typed identity/同型、P1Φのnetwork実装 | 二つのroleの比較 | field/network type、node/edge、aggregation/独立観測 | identity説明をtwo-view interpretationへ、formal identityはhold | YES; OPEN005/011/017/023 |
| INT-SERREV-004 | INT-SERIOUS-004 | RETAIN | EVIDENCE GAP STRONG | CORRESPONDENCE GAP STRONG | μ / error tolerance: 049,080,086,087 SPLIT | threshold mobility定義とrevisabilityの候補関係 | 双方向equivalence/内発性から一般知性・自由を保証 | sapiens追加profileとlocal mobility | μ/error別endpoint、内発性、同値条件 | equivalence/必要性をcorrespondenceへ | YES; OPEN009/010/021/022 |
| INT-SERREV-005 | INT-SERIOUS-005 | RETAIN | EVIDENCE GAP CRITICAL | CORRESPONDENCE GAP CRITICAL | Gettier confirmation: 015,078 SPLIT / 016 DOWNGRADE / 040,079 KEEP | 哲学例の局所structural diagnostic/C≠truth guard | 例によるIntの確認と全修復の原理的排除 | case再記述とnegative scope | 独立C/LE/case criterion・排除scope | confirms/impossibleをlocal interpretationへ | YES; OPEN002/020 |

## 11. Strong-language synthesis — 62/62

各旧INT-STRONG familyにprimary wording classを一つ付与する。mixed familyではweak成分の最大許容classを示し、guard/conditional/formal OPENの別成分は最後の欄に残す。ASSERTIVEは003のlocal connectedness scopeだけであり、一般知性の実証主張をassertive認定するものではない。wording classは実際の翻訳/置換文ではなく編集上の意味強度。

| WORDING | source strong ID / claim | current wording / locator | Phase04 strength status | strongest defensible wording class (provisional) | scope / held component |
|---|---|---|---|---|---|
| INT-WORDING-001 | INT-STRONG-001 / INT-CLM-004 | P1 E/J §2; continually produces / not stored — 知性は全層を横断し知識を産出・改訂、保存されない | POSSIBLY OVERSTATED | MODEL-LOCAL | 産出・保存不能を局所dynamic namingに限定、過程機構は別成分 |
| INT-WORDING-002 | INT-STRONG-002 / INT-CLM-005 | P1 E/J §3,10; necessary / lower bound — 3公理は同時必要な下限、完全理論でない | OVERSTATED | PROPOSED | 三条件の候補的下限。一般必要性の証明とはしない |
| INT-WORDING-003 | INT-STRONG-003 / INT-CLM-006 | P1 E/J §3; connected, not necessarily continuous — connected state spaceは連続空間に限定しない | SUPPORTED AT CURRENT STRENGTH | ASSERTIVE | 非連続も許すconnectedness定義は現在のscopeで維持 |
| INT-WORDING-004 | INT-STRONG-004 / INT-CLM-007 | P1 E/J §3; requires / update — temporal orderingで履歴変化が蓄積する | POSSIBLY OVERSTATED | CONDITIONAL | 順序と履歴保持/利用の条件を分離 |
| INT-WORDING-005 | INT-STRONG-005 / INT-CLM-008 | P1 E/J §3–4; irreducible — global Φは局所更新に非還元 | OVERSTATED | HYPOTHESIZED | global役割は定義可、非還元性は追加formal burden |
| INT-WORDING-006 | INT-STRONG-006 / INT-CLM-016 | P1 E/J §6; cannot guarantee — JTBへの静的条件追加では動的保証にならない | OVERSTATED | MODEL-LOCAL | Gettier診断scope。全修復の原理的不可能を含めない |
| INT-WORDING-007 | INT-STRONG-007 / INT-CLM-017 | P1 E/J §7; increases / generates — 正しさ蓄積はconnectivity/divergenceを増やす | OVERSTATED | HYPOTHESIZED | correctnessから分岐への未測定方向 |
| INT-WORDING-008 | INT-STRONG-008 / INT-CLM-018 | P1 E/J §7; structural not contingent — 結合数二乗・経路指数の分岐爆発 | POSSIBLY OVERSTATED | CONDITIONAL | 所与graphの数え上げ、実推論への適用は別 |
| INT-WORDING-009 | INT-STRONG-009 / INT-CLM-019 | P1 E/J §7; does not solve — 知識量/推論速度/専門化/能力強化だけでは止まらない | OVERSTATED | HYPOTHESIZED | 能力増強だけで停止しない方向。全AIへ一般化しない |
| INT-WORDING-010 | INT-STRONG-010 / INT-CLM-021 | P1 E/J §8; no stopping operator — 個体内推論には停止演算子がない | OVERSTATED | CONDITIONAL | sourceのformal内部stopモデル下。任意認知停止はOPEN |
| INT-WORDING-011 | INT-STRONG-011 / INT-CLM-022 | P1 E/J §8（J詳細）; all / すべて中断 — 疲労/注意/報酬/生理終了は停止でなく中断 | POSSIBLY OVERSTATED | MODEL-LOCAL | 中断/停止のモデル区分。生理的終了全件の独立分類ではない |
| INT-WORDING-012 | INT-STRONG-012 / INT-CLM-023 | P1 E/J §8（J強化）; structural root / 誤っている — paperclip/alignment問題は同じ停止不在の構造 | OVERSTATED | STRUCTURAL ANALOGY | paperclipと停止不在の類似。alignment一般の実証でない |
| INT-WORDING-013 | INT-STRONG-013 / INT-CLM-024 | P1 E/J §8–9; requires / 必然 — 停止はログ・応答・合意・遅延への越境を必要とする | OVERSTATED | PROPOSED | 外化のarchitecture hypothesis。代替排除の定理でない |
| INT-WORDING-014 | INT-STRONG-014 / INT-CLM-027 | P1 E/J §9; does not guarantee truth / guarantees — 外化は真理を保証せず持続/改訂可能停止を保証 | OVERSTATED | HYPOTHESIZED | positive persistence/revisabilityの効果のみ対象。truth非保証は別途保持 |
| INT-WORDING-015 | INT-STRONG-015 / INT-CLM-030 | P1 J §9; 構造的事実 — 生命層はCon/Intを支える必要基盤というJA記述 | VERSION-SPECIFIC | STRUCTURAL ANALOGY | JA substrate relationの提案的比較 |
| INT-WORDING-016 | INT-STRONG-016 / INT-CLM-033 | P1 E/J §10; necessary not sufficient — 六制約は必要で十分でない、complete/engineering/norm theoryでない | POSSIBLY OVERSTATED | CONDITIONAL | 六条件をモデルscopeに限定。not sufficient/not complete guard保持 |
| INT-WORDING-017 | INT-STRONG-017 / INT-CLM-036 | P2 J §0; E abstract; 構造的に導出 / develops — PartIIはVED差分原理から三層構造を導出すると宣言 | VERSION-SPECIFIC | PROPOSED | VEDからの構成動機/語彙再用。typed derivationはOPEN |
| INT-WORDING-018 | INT-STRONG-018 / INT-CLM-037 | P2 E/J §0,5,12; emerges / 同時 — LF/LR/LEの同時動態が個体内外部依存停止を生む | OVERSTATED | PROPOSED | 三層architectureとstop生成の提案 |
| INT-WORDING-019 | INT-STRONG-019 / INT-CLM-041 | P2 J §1,A; E簡略; VED基本式 — closure PDE/basic VED formをIntで使用 | POSSIBLY OVERSTATED | MODEL-LOCAL | JA effective template、domain/authority未確定 |
| INT-WORDING-020 | INT-STRONG-020 / INT-CLM-042 | P2 E/J §1,3; unreachable / 構造的禁止 — Cmax非到達と究極理解/最終判断の非到達 | OVERSTATED | STRUCTURAL ANALOGY | formal境界から理解への読み。invariant/understandingは別OPEN |
| INT-WORDING-021 | INT-STRONG-021 / INT-CLM-043 | P2 E/J §1–2; movement region — Ωθ内(A)とθ再編(B)、領域外は発散/停止 | POSSIBLY OVERSTATED | MODEL-LOCAL | A/B区分の定義。領域外帰結はhypothesis成分 |
| INT-WORDING-022 | INT-STRONG-022 / INT-CLM-044 | P2 E/J §1,E; not deduced from lower alone — VED-defined emergenceは下位運動+外部Hから上位動態 | GUARDED | NEGATIVE SCOPE | lower alone非導出guardを保持。schemaを実生成則へしない |
| INT-WORDING-023 | INT-STRONG-023 / INT-CLM-048 | P2 J §2; 式 / threshold — Hij応答閾値をCij指数関係で記述 | POSSIBLY OVERSTATED | CORRESPONDENCE | Cij/Hと応答の候補対応、未較正 |
| INT-WORDING-024 | INT-STRONG-024 / INT-CLM-049 | P2 E/J §2,5; not mere flexibility — μθは内生的閾値移動・E設置領域を組み替える | POSSIBLY OVERSTATED | MODEL-LOCAL | μmobility定義とE-site生成の追加claimを分離 |
| INT-WORDING-025 | INT-STRONG-025 / INT-CLM-051 | P2 E/J §3,D; Theorem / proof sketch — P1/P2仮定下Fに内部不動点なし（定理3.1） | POSSIBLY OVERSTATED | CONDITIONAL | strict-J/fixedθ-A。proof validという認証は付けない |
| INT-WORDING-026 | INT-STRONG-026 / INT-CLM-052 | P2 E/J §3; J D; no internal S — 任意内部停止条件Sは推論要求へ戻る（系3.2） | OVERSTATED | CONDITIONAL | S/fixedpoint modelに限定。全認知停止の禁止ではない |
| INT-WORDING-027 | INT-STRONG-027 / INT-CLM-053 | P2 E/J §3; J D; isomorphism / 同型 — 非閉包とCmax/VED4horizonは同型（系3.3） | OVERSTATED | STRUCTURAL ANALOGY | Cmax/noFP/DHのrole comparison;型付き同型はhold |
| INT-WORDING-028 | INT-STRONG-028 / INT-CLM-054 | P2 E/J §3; J D; cannot / inevitable — 個体内知性完結不能、3collapse attractorsへ | OVERSTATED | HYPOTHESIZED | 個体collapseをqualitative regimeへ |
| INT-WORDING-029 | INT-STRONG-029 / INT-CLM-056 | P2 E/J §4; continues indefinitely — 沈黙世界でregress持続、branch explosionと同じ構造 | POSSIBLY OVERSTATED | CONDITIONAL | 三前提に依存するregress。branching同一性は別 |
| INT-WORDING-030 | INT-STRONG-030 / INT-CLM-057 | P2 E/J §4–5; because / generates — nonclosureはtraceを残しLR/LE創発へproductive | POSSIBLY OVERSTATED | HYPOTHESIZED | traceから生成への質的proposal |
| INT-WORDING-031 | INT-STRONG-031 / INT-CLM-059 | P2 E/J §5; Definition / arises — LEは個体内だが外部H依存の動的stopping attractor | POSSIBLY OVERSTATED | MODEL-LOCAL | LEの機能命名。存在/収束をdefinitionから確認しない |
| INT-WORDING-032 | INT-STRONG-032 / INT-CLM-060 | P2 E/J §5; emergence mechanism — μθ→B→E-site projection→LRconvergence→LEの機構 | OVERSTATED | HYPOTHESIZED | 四stageは未実装のmechanism schema |
| INT-WORDING-033 | INT-STRONG-033 / INT-CLM-062 | P2 E/J §5; J B; definition itself / not psychological — projectionはConの第四原語を適用、心理防衛でない | POSSIBLY OVERSTATED | STRUCTURAL ANALOGY | ConprojectionとE-siteの役割比較。心理同一性否定も保持 |
| INT-WORDING-034 | INT-STRONG-034 / INT-CLM-063 | P2 E/J §5; E not F^k — EはF反復から導出できずLEと現在stateに依存 | POSSIBLY OVERSTATED | MODEL-LOCAL | 外部Eというarchitecture表現。F非導出のformal claimはhold |
| INT-WORDING-035 | INT-STRONG-035 / INT-CLM-064 | P2 E/J §5,D; equivalent / 同型命題5.4 — Φext≡Φnet、外部性はLEnetworkの見え方 | OVERSTATED | MODEL-LOCAL | 二視点としての命名のみ。literal identityの認証を避ける |
| INT-WORDING-036 | INT-STRONG-036 / INT-CLM-067 | P2 E/J §6; installation / 状態変換 — animismは沈黙世界を応答的として扱う停止設置 | POSSIBLY OVERSTATED | MODEL-LOCAL | animismを応答付与として読む局所解釈 |
| INT-WORDING-037 | INT-STRONG-037 / INT-CLM-068 | P2 J §6; 低コスト / 普遍性 — animism低停止コストが普遍性を説明 | OVERSTATED | HYPOTHESIZED | 低cost方向のみ、普遍性の説明達成ではない |
| INT-WORDING-038 | INT-STRONG-038 / INT-CLM-069 | P2 E/J §7; is / Definition7.1 — Godは未解決→保留演算子、中心化Φext | POSSIBLY OVERSTATED | MODEL-LOCAL | God保留機能の命名、歴史causeは別成分 |
| INT-WORDING-039 | INT-STRONG-039 / INT-CLM-070 | P2 E/J §7; reduces / not progress — 中心化は曖昧性を減らし安定化、単一極限は歴史終点でない | POSSIBLY OVERSTATED | HYPOTHESIZED | 中心化/曖昧性関係。not progress guard保持 |
| INT-WORDING-040 | INT-STRONG-040 / INT-CLM-071 | P2 E/J §8; three functions — religionはLE世代維持・mixed responsive/silent境界管理 | POSSIBLY OVERSTATED | HYPOTHESIZED | 維持機能から世代持続への仮説 |
| INT-WORDING-041 | INT-STRONG-041 / INT-CLM-073 | P2 E/J §8; unstable / prevents・buffer — 純粋因果推論は有限sapiensに不安定、病的引力子分類 | OVERSTATED | HYPOTHESIZED | nonclinical instability/予防の質的仮説 |
| INT-WORDING-042 | INT-STRONG-042 / INT-CLM-076 | P2 E/J §9; cannot be computed — legitimacyは原理的非計算可能、継続改訂条件 | OVERSTATED | PROPOSED | 社会的文脈依存の解釈へ限定。principled noncomputabilityは未決 |
| INT-WORDING-043 | INT-STRONG-043 / INT-CLM-077 | P2 E/J §9; only / 社会では起こらない — 創造は個体でのみ、社会は事後安定化 | OVERSTATED | HYPOTHESIZED | 個人/社会役割分担。onlyという排他性を維持しない |
| INT-WORDING-044 | INT-STRONG-044 / INT-CLM-078 | P2 E/J §10; confirms / 原理的に不可能 — GettierはC≠truthのevidence、原理的解決不能というJA主張 | OVERSTATED | MODEL-LOCAL | Gettierの再記述。confirmation/全修復不能は別burden |
| INT-WORDING-045 | INT-STRONG-045 / INT-CLM-080 | P2 J §10,D; E弱いcoupling; equivalent / 双方向sketch — error toleranceとμθは構造的同値 | VERSION-SPECIFIC | CORRESPONDENCE | μ/errorの候補関係。双方向formal equivalenceはhold |
| INT-WORDING-046 | INT-STRONG-046 / INT-CLM-081 | P2 E/J §11; only narrow band — Σ相図はvinf/rres/η、安定は狭いbandのみ | OVERSTATED | HYPOTHESIZED | qualitative phase band、唯一/幅の測定根拠なし |
| INT-WORDING-047 | INT-STRONG-047 / INT-CLM-082 | P2 E/J §11; collapse / 連鎖 — Δvintel増大はLR/LE/μ失敗のfourfoldcollapse | OVERSTATED | HYPOTHESIZED | 速度差とcollapseの未実行方向 |
| INT-WORDING-048 | INT-STRONG-048 / INT-CLM-083 | P2 E/J §11; not intelligence / constitutive — zero motionは知性でなく不安定性は構成的 | POSSIBLY OVERSTATED | MODEL-LOCAL | zero-motion定義除外。不安定性必然のcomponentと分離 |
| INT-WORDING-049 | INT-STRONG-049 / INT-CLM-085 | P2 J §12; E7clauses; cannot / requires — N1–6 impossibilities/R1–6 necessities/S1sapiens条件 | VERSION-SPECIFIC | MODEL-LOCAL | N/R/Sをモデル内条件として整理しgeneral/sapiensを分離 |
| INT-WORDING-050 | INT-STRONG-050 / INT-CLM-086 | P2 J §12; E §12; final constructive statement — 一般知性はLF+LR+LE、sapiensはμ移動性追加 | OVERSTATED | MODEL-LOCAL | 一般/サピエンスの局所定義。経験的必要十分criterionでない |
| INT-WORDING-051 | INT-STRONG-051 / INT-CLM-087 | P2 E/J §0,5,12; free inference requires movable stopping — 停止と可動性が自由な推論を可能にする | POSSIBLY OVERSTATED | PROPOSED | 可動停止とI2free inferenceの提案関係。phenomenal criterionなし |
| INT-WORDING-052 | INT-STRONG-052 / INT-CLM-089 | P2 E/J §5,13,D,E; future work — Σ定量化・stoppingfunctional・哲学/AI実践はfuture | GUARDED | FUTURE | formal/clinical/philosophical/AIのfutureを維持 |
| INT-WORDING-053 | INT-STRONG-053 / INT-CLM-093 | P2 E/J E; same grammar / proposedtypedOPEN — appendixEはemergence比較とLElocalminの記述を追加 | UNRESOLVED | STRUCTURAL ANALOGY | 比較成分のみの上限。LElocalmin採用はauthority OPEN |
| INT-WORDING-054 | INT-STRONG-054 / INT-CLM-011 | P1 §4; same structure / not strict mathematical isomorphism | GUARDED | CORRESPONDENCE | Q/D/BCのlexical tableとnonidentity guard維持 |
| INT-WORDING-055 | INT-STRONG-055 / INT-CLM-012 | P1 abstract,§4–5,10; independent empirical line / 独立な実証 | OVERSTATED | CORRESPONDENCE | 外部研究のInt対応はcandidateまで、独立確認にしない |
| INT-WORDING-056 | INT-STRONG-056 / INT-CLM-013 | P1 §5; both satisfy / 同一条件 | POSSIBLY OVERSTATED | CORRESPONDENCE | 二系のcarrier/三条件の比較に限定 |
| INT-WORDING-057 | INT-STRONG-057 / INT-CLM-031 | P1 §1,9; different projections of the same structure | POSSIBLY OVERSTATED | STRUCTURAL ANALOGY | Con/Int異projectionのrole比較 |
| INT-WORDING-058 | INT-STRONG-058 / INT-CLM-034 | P1 §10; convergence supports non-arbitrary conditions | POSSIBLY OVERSTATED | PROPOSED | 非恣意性への動機、mapping独立性の証明でない |
| INT-WORDING-059 | INT-STRONG-059 / INT-CLM-047 | P2 §2,5; Physarum flow as F action itself | POSSIBLY OVERSTATED | CORRESPONDENCE | F actionという比較で同一operatorにしない |
| INT-WORDING-060 | INT-STRONG-060 / INT-CLM-050 | P2 J §2,B; 同じ原理でDNAと知性のθ可変性を統一 | VERSION-SPECIFIC | STRUCTURAL ANALOGY | DNA/Int θのtime-scale比較 |
| INT-WORDING-061 | INT-STRONG-061 / INT-CLM-065 | P2 §5,C; P1 global Φ refined / concretized as network | POSSIBLY OVERSTATED | PROPOSED | P1Φのnetwork-role refinementは提案段階 |
| INT-WORDING-062 | INT-STRONG-062 / INT-CLM-091 | P2 J B; same structures across domains / guarded homology | GUARDED | STRUCTURAL ANALOGY | Bのguarded role比較を維持 |

## 12. Claim splitting plan

各SPLIT-CANDと同じ順にINT-SPLITPLANを付す。A/B/C/Dはconceptual childrenであり、新しいsource-native claim IDsや数式を導入しない。[KEEP候補]等は暫定child roleで、parentに二つ以上のprimary dispositionを与えていない。source全体のsummary・figureがこれらを再結合しないことがimplementation/Phase07の重要gateとなる。

| split plan | parent / candidate ID | conceptual children (not source prose) | source loci / recombination risk |
|---|---|---|---|
| INT-SPLITPLAN-001 | INT-CLM-004 / INT-SPLIT-CAND-001 | A [KEEP候補] 持続motionの局所命名 / B [DOWNGRADE候補] 知識産出・全層横断の機能仮説 / C [OPEN] 保存不能の一般criterion | P1 E/J §2; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-002 | INT-CLM-005 / INT-SPLIT-CAND-002 | A [KEEP候補] 三条件のモデル構成 / B [DOWNGRADE候補] joint necessity/lower-bound一般化 / C [KEEP候補] 不完全・not sufficient guard | P1 E/J §3,10; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-003 | INT-CLM-008 / INT-SPLIT-CAND-003 | A [KEEP候補] Φ scalar/global-role宣言 / B [DOWNGRADE候補] 非還元性・全域制御の仮説 / C [OPEN] formal irreducibilityと観測 | P1 E/J §3–4; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-004 | INT-CLM-013 / INT-SPLIT-CAND-004 | A [KEEP候補] 管網/hidden-state等の具体比較 / B [DOWNGRADE候補] 同じ条件充足の一般化 / C [OPEN] 独立mapping検証 | P1 E/J §5; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-005 | INT-CLM-015 / INT-SPLIT-CAND-005 | A [REVISE候補] Gettierの局所構造診断 / B [DOWNGRADE候補] 診断による説明/確認 / C [OPEN] 独立case criterion | P1 E/J §6; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-006 | INT-CLM-017 / INT-SPLIT-CAND-006 | A [REVISE候補] 所与graphの組合せ / B [DOWNGRADE候補] correctness→connectivity→branching方向 / C [OPEN] 認知graph抽出 / D [DOWNGRADE候補] 心理的不安定性 | P1 E/J §7; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-007 | INT-CLM-021 / INT-SPLIT-CAND-007 | A [REVISE候補] source-local formal stop model / B [OPEN] 任意認知停止との対応 / C [DOWNGRADE候補] 外部停止必然のarchitecture reading。CLM051/052と連結し別証拠に数えない | P1 E/J §8; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-008 | INT-CLM-022 / INT-SPLIT-CAND-008 | A [KEEP候補] 疲労後再開等の例 / B [REVISE候補] 中断/完成の局所区分 / C [DOWNGRADE候補] 全生理終了は中断という一般化 | P1 E/J §8（J詳細）; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-009 | INT-CLM-024 / INT-SPLIT-CAND-009 | A [KEEP候補] log/応答/合意/遅延の役割例 / B [DOWNGRADE候補] 越境必要性 / C [OPEN] 外化と停止の独立判定 | P1 E/J §8–9; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-010 | INT-CLM-027 / INT-SPLIT-CAND-010 | A [KEEP候補] truth非保証 / B [DOWNGRADE候補] 外化→持続/改訂可能性 / C [OPEN] 効果条件とendpoint | P1 E/J §9; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-011 | INT-CLM-033 / INT-SPLIT-CAND-011 | A [KEEP候補] not complete/not sufficient/non-normative / B [DOWNGRADE候補] 六制約の一般必要性 / C [REVISE候補] summaryが本文splitを再結合しない接続 | P1 E/J §10; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-012 | INT-CLM-037 / INT-SPLIT-CAND-012 | A [KEEP候補] 三層のmodel-local architecture / B [DOWNGRADE候補] 同時運動が停止を生むという仮説 / C [OPEN] 生成・独立検出 | P2 E/J §0,5,12; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-013 | INT-CLM-042 / INT-SPLIT-CAND-013 | A [REVISE候補] C範囲/境界のformal use / B [OPEN] barrier不達・不変領域 / C [DOWNGRADE候補] ultimate understanding読解 / D [OPEN] 理解endpoint | P2 E/J §1,3; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-014 | INT-CLM-043 / INT-SPLIT-CAND-014 | A [KEEP候補] Ωθ/A/Bの局所区分 / B [DOWNGRADE候補] 領域外発散/停止 / C [OPEN] 領域観測・再配置operator | P2 E/J §1–2; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-015 | INT-CLM-044 / INT-SPLIT-CAND-015 | A [KEEP候補] emergence schemaの命名 / B [DOWNGRADE候補] 上位生成の一般法則 / C [OPEN] Φのtyped inputs/outputと実装 | P2 E/J §1,E; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-016 | INT-CLM-046 / INT-SPLIT-CAND-016 | A [REVISE候補] P2Fの局所formal role / B [DOWNGRADE候補] 認知推論過程とのidentity / C [OPEN] single/set-valued authorityとJ合成 | P2 E/J §2; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-017 | INT-CLM-048 / INT-SPLIT-CAND-017 | A [REVISE候補] 既存Cij formal relationのscope / B [DOWNGRADE候補] response thresholdとの対応 / C [OPEN] 値/係数/observable同定 | P2 J §2; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-018 | INT-CLM-049 / INT-SPLIT-CAND-018 | A [KEEP候補] threshold mobility定義 / B [DOWNGRADE候補] E-siteを作る機構 / C [OPEN] 内発性/境界/μ独立測定 | P2 E/J §2,5; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-019 | INT-CLM-052 / INT-SPLIT-CAND-019 | A [REVISE候補] 仮定的binary Sとfixedpointの関係 / B [REVISE候補] F′再適用というsource argument / C [OPEN] 任意認知stopとのbridge / D [DOWNGRADE候補] 必然的外部停止 | P2 E/J §3; J D; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-020 | INT-CLM-054 / INT-SPLIT-CAND-020 | A [REVISE候補] LF-onlyというformal scope / B [DOWNGRADE候補] 個体完結不能/三collapse reading / C [OPEN] independent collapse criteria | P2 E/J §3; J D; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-021 | INT-CLM-056 / INT-SPLIT-CAND-021 | A [REVISE候補] 三前提下のregress argument / B [DOWNGRADE候補] branchingとのsame-structure / C [OPEN] 実際の認知regress/branching対応 | P2 E/J §4; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-022 | INT-CLM-057 / INT-SPLIT-CAND-022 | A [KEEP候補] traceと再参照のrole / B [DOWNGRADE候補] nonclosureのproductive生成 / C [OPEN] trace保持→LR→LE更新 | P2 E/J §4–5; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-023 | INT-CLM-059 / INT-SPLIT-CAND-023 | A [KEEP候補] LE stopping-function naming / B [DOWNGRADE候補] dynamic emergence/existence explanation / C [OPEN] attractor/収束/独立検出 | P2 E/J §5; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-024 | INT-CLM-061 / INT-SPLIT-CAND-024 | A [KEEP候補] flow/trail/weights/context/EOS例 / B [DOWNGRADE候補] own LE・内発μ有無というprofile / C [OPEN] autonomous/injected/common criterion | P2 E/J §5; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-025 | INT-CLM-062 / INT-SPLIT-CAND-025 | A [KEEP候補] projection語彙の再用 / B [KEEP候補] 心理防衛との非identity / C [DOWNGRADE候補] ConからE-siteへの同じoperator具現 / D [OPEN] typed translation | P2 E/J §5; J B; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-026 | INT-CLM-063 / INT-SPLIT-CAND-026 | A [REVISE候補] E外部作用のarchitecture role / B [OPEN] E非導出とF反復集合のformal関係 / C [OPEN] LEからのupdate / D [DOWNGRADE候補] 外部機構の実在説明 | P2 E/J §5; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-027 | INT-CLM-064 / INT-SPLIT-CAND-027 | A [REVISE候補] 二視点としてのfield/network naming / B [DOWNGRADE候補] 同型の説明的使用 / C [OPEN] literal/typed identityと独立観測 | P2 E/J §5,D; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-028 | INT-CLM-067 / INT-SPLIT-CAND-028 | A [REVISE候補] animismの機能的再解釈 / B [DOWNGRADE候補] channel注入→stop生成 / C [OPEN] 社会case selection/機構指標 | P2 E/J §6; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-029 | INT-CLM-069 / INT-SPLIT-CAND-029 | A [REVISE候補] God=保留の機能命名と非存在論guard / B [DOWNGRADE候補] centralizationの歴史/社会説明 / C [OPEN] operator/field-network対応 | P2 E/J §7; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-030 | INT-CLM-070 / INT-SPLIT-CAND-030 | A [DOWNGRADE候補] 中心化→曖昧性低下/安定化 / B [KEEP候補] 単一極限は歴史終点でないguard / C [OPEN] cost/ambiguity comparison | P2 E/J §7; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-031 | INT-CLM-071 / INT-SPLIT-CAND-031 | A [REVISE候補] religion=維持運用というnaming / B [DOWNGRADE候補] 世代維持/予防の歴史効果 / C [OPEN] independent historical criterion | P2 E/J §8; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-032 | INT-CLM-072 / INT-SPLIT-CAND-032 | A [REVISE候補] science/religionの改訂/維持比較 / B [KEEP候補] 真理優劣の否定 / C [DOWNGRADE候補] 一般史的説明 / D [OPEN] case comparison | P2 E/J §8–9,D; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-033 | INT-CLM-078 / INT-SPLIT-CAND-033 | A [KEEP候補] C≠truth negative scope / B [REVISE候補] Gettierの局所diagnostic / C [DOWNGRADE候補] theory confirmation/全修復不能 / D [OPEN] 独立case分類 | P2 E/J §10; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-034 | INT-CLM-080 / INT-SPLIT-CAND-034 | A [KEEP候補] μthreshold mobilityの定義 / B [DOWNGRADE候補] revisability/error tolerance関係 / C [OPEN] ↔のformal conditionと別々のendpoint | P2 J §10,D; E弱いcoupling; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-035 | INT-CLM-081 / INT-SPLIT-CAND-035 | A [KEEP候補] 三軸の変数候補 / B [DOWNGRADE候補] narrow/exclusive stableband / C [OPEN] scale/phaseboundary / D [KEEP候補] Σ量化futureとの区別 | P2 E/J §11; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-036 | INT-CLM-082 / INT-SPLIT-CAND-036 | A [REVISE候補] Δvのrate relation / B [DOWNGRADE候補] fourfold collapse chain / C [OPEN] common clockと層検出 | P2 E/J §11; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-037 | INT-CLM-083 / INT-SPLIT-CAND-037 | A [KEEP候補] local zero-motion exclusion / B [DOWNGRADE候補] 構成的不安定性の必然 / C [OPEN] phase criterion | P2 E/J §11; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-038 | INT-CLM-085 / INT-SPLIT-CAND-038 | A [REVISE候補] general model N/R clauses / B [KEEP候補] sapiens追加μのscope区別 / C [DOWNGRADE候補] 全称必要性 / D [OPEN] N1/R4・六/七条件authority | P2 J §12; E7clauses; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-039 | INT-CLM-086 / INT-SPLIT-CAND-039 | A [KEEP候補] 一般知性のlocal architecture definition / B [KEEP候補] sapiens内発μの追加profile / C [DOWNGRADE候補] empirical general-intelligence necessity / D [OPEN] 独立criterion | P2 J §12; E §12; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-040 | INT-CLM-087 / INT-SPLIT-CAND-040 | A [REVISE候補] I2free inferenceの機能解釈 / B [DOWNGRADE候補] 可動停止の普遍必要性 / C [OPEN] 自由の独立endpoint / D [KEEP候補] I4意味/主観へのfuture境界 | P2 E/J §0,5,12; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |
| INT-SPLITPLAN-041 | INT-CLM-093 / INT-SPLIT-CAND-041 | A [KEEP候補] emergenceのguarded role comparison / B [OPEN] LElocalminimumの採用status/functional / C [DOWNGRADE候補] same grammarを機構同一性へ使う強度 | P2 E/J E; 同章summary、P1abstract/§10、P2§0/12/13・関連図で再結合しない |

## 13. Formal / equation revision status

全63 EQFを対象とする。1行1primary planning status。NO CHANGEは記録上の既存式を保持できる候補という意味で、数学的正しさ・proof validityの認定ではない。TYPING/ASSUMPTIONは不足を特定するだけで、型・空間・単位・境界条件を新規採用しない。POSSIBLEは将来の選択条件であり、式変更が既に必要と立証されたという意味ではない。

| EQREV | Phase01 EQF / role | source / occurrence locator | signature status | claims | primary planning status | 最小範囲 / hold |
|---|---|---|---|---|---|---|
| INT-EQREV-001 | INT-EQF-001 / P1 ordered update | P1 §3; INT-MATH-P1E-002, INT-MATH-P1J-002, INT-INLINE-008 | PARTIAL | INT-CLM-005–009 | TYPING CLARIFICATION NEEDED | F入出力/可到達性と順序updateの局所scopeを区別。具体空間を追加しない |
| INT-EQREV-002 | INT-EQF-002 / P1 global Φ map | P1 §3; INT-MATH-P1E-003, INT-MATH-P1J-003 | EXPLICIT | INT-CLM-007–010 | PROSE-SCOPE ONLY | scalar map宣言は維持、global roleと非還元性を分離 |
| INT-EQREV-003 | INT-EQF-003 / P1 Φbio map | P1 §5; INT-MATH-P1J-007 | EXPLICIT | INT-CLM-011–014 | PROSE-SCOPE ONLY | Φbioは対応候補であって独立実測fieldではない |
| INT-EQREV-004 | INT-EQF-004 / P1 Φtr map | P1 §5; INT-MATH-P1E-009, INT-MATH-P1J-010 | EXPLICIT | INT-CLM-011–014 | PROSE-SCOPE ONLY | Φtrのweights/loss解釈をcalibrated scalarへ強化しない |
| INT-EQREV-005 | INT-EQF-005 / Physarum Q relation | P1 §4; INT-MATH-P1E-004, INT-MATH-P1J-004 | PARTIAL | INT-CLM-011–013 | NO CHANGE | 引用される管網関係は保持。Int写像の修正を引用式変更にしない |
| INT-EQREV-006 | INT-EQF-006 / Physarum conductance update | P1 §4–5; INT-MATH-P1E-005, INT-MATH-P1E-006, INT-MATH-P1J-005, INT-MATH-P1J-006, INT-INLINE-002, INT-INLINE-015 | PARTIAL | INT-CLM-011–013 | NO CHANGE | 引用conductance updateは保持、Intへの対応はprose burden |
| INT-EQREV-007 | INT-EQF-007 / Physarum power response and μ>0 | P1 J §4; INT-INLINE-011, INT-INLINE-012 | PARTIAL | INT-CLM-011–013 | FORMAL ASSUMPTION REQUIRED | JA power-response例のdomain/range・一般式との適用範囲は未決 |
| INT-EQREV-008 | INT-EQF-008 / Transformer state set | P1 §5; INT-MATH-P1E-007, INT-MATH-P1J-008 | PARTIAL | INT-CLM-013–014 | TYPING CLARIFICATION NEEDED | hidden-state集合とsequence/tensor役割を区別、dimension未決 |
| INT-EQREV-009 | INT-EQF-009 / Transformer layer update | P1 §5; INT-MATH-P1E-008, INT-MATH-P1J-009, INT-INLINE-003, INT-INLINE-016 | PARTIAL | INT-CLM-013–014 | TYPING CLARIFICATION NEEDED | Ftr入出力/layer依存の署名、認知Fと非同一 |
| INT-EQREV-010 | INT-EQF-010 / I(s) increase | P1 §7; INT-MATH-P1E-010, INT-MATH-P1J-011 | PARTIAL | INT-CLM-017 | PROSE-SCOPE ONLY | ↑をqualitative directionに限定、測定densityにしない |
| INT-EQREV-011 | INT-EQF-011 / div J increase / zero comparison | P1 §7; INT-MATH-P1E-011, INT-MATH-P1J-012, INT-INLINE-004, INT-INLINE-017 | PARTIAL | INT-CLM-017–019 | TYPING CLARIFICATION NEEDED | divergenceのgeometryとgraph/認知proxyは未同定 |
| INT-EQREV-012 | INT-EQF-012 / correctness(p) implies nonzero divergence | P1 §7; INT-MATH-P1E-012, INT-MATH-P1J-013 | UNRESOLVED | INT-CLM-017–018 | POSSIBLE EQUATION CHANGE | 命題pでfieldを評価する写像が未型付け。意図次第で式側変更の可能性、未確定 |
| INT-EQREV-013 | INT-EQF-013 / I(si) increase for indexed states | P1 J §7; INT-MATH-P1J-014 | PARTIAL | INT-CLM-017–018 | PROSE-SCOPE ONLY | indexed stateでの増大方向をqualitativeに限定 |
| INT-EQREV-014 | INT-EQF-014 / graph edge-square growth | P1 §7; INT-INLINE-005, INT-INLINE-006, INT-INLINE-018, INT-INLINE-019, INT-INLINE-020 | PARTIAL | INT-CLM-018 | FORMAL ASSUMPTION REQUIRED | 辺数二乗のgraph条件/漸近変数を決めず必要事項としてhold |
| INT-EQREV-015 | INT-EQF-015 / branch count b^d | P1 §7; INT-INLINE-007, INT-INLINE-021 | PARTIAL | INT-CLM-018–019 | FORMAL ASSUMPTION REQUIRED | b/depth/path数の対象条件が必要、実認知branchを同一視しない |
| INT-EQREV-016 | INT-EQF-016 / external T membership | P1 §9; INT-MATH-P1E-015, INT-MATH-P1J-017 | UNRESOLVED | INT-CLM-024–028 | TYPING CLARIFICATION NEEDED | External(R)の集合/演算子所属と境界読解の区別 |
| INT-EQREV-017 | INT-EQF-017 / closure PDE | P2 J §1,3; INT-MATH-P2J-007, INT-MATH-P2J-023 | PARTIAL | INT-CLM-041–042 | FORMAL ASSUMPTION REQUIRED | PDE domain/IC/BC/ranges/invariant burdenをhold。Master provenanceも未解決 |
| INT-EQREV-018 | INT-EQF-018 / C range / endpoint barrier | P2 J §1,3; INT-INLINE-033, INT-INLINE-040, INT-INLINE-041, INT-INLINE-088 | PARTIAL | INT-CLM-042 | FORMAL ASSUMPTION REQUIRED | C rangeの宣言と境界不達のdynamical保証は別 |
| INT-EQREV-019 | INT-EQF-019 / I=f(1−C) | P2 §1,A; INT-MATH-P2E-003, INT-MATH-P2J-008, INT-MATH-P2AJ-005, INT-INLINE-045, INT-INLINE-068 | PARTIAL | INT-CLM-040–042 | FORMAL ASSUMPTION REQUIRED | f出力/range・C normalizationを仮定で補わない |
| INT-EQREV-020 | INT-EQF-020 / f(u)=u example | P2 J §1; INT-INLINE-034 | PARTIAL | INT-CLM-041 | FORMAL ASSUMPTION REQUIRED | linear f例のdomain/適用scope未固定 |
| INT-EQREV-021 | INT-EQF-021 / f(u)=−ln(1−u) example | P2 J §1; INT-INLINE-035 | PARTIAL | INT-CLM-041 | FORMAL ASSUMPTION REQUIRED | log f例のadmissible domainを要するが当phaseは選ばない |
| INT-EQREV-022 | INT-EQF-022 / FI=α∇C | P2 J §1,A; INT-MATH-P2J-009, INT-MATH-P2AJ-005, INT-INLINE-046, INT-INLINE-069 | PARTIAL | INT-CLM-041,046 | FORMAL ASSUMPTION REQUIRED | closure gradientの有効力解釈・幾何/適用条件をhold |
| INT-EQREV-023 | INT-EQF-023 / JC=−ξ∇C | P2 J §1,3,A; INT-INLINE-047, INT-INLINE-067 | PARTIAL | INT-CLM-041,046 | FORMAL ASSUMPTION REQUIRED | flux gradient templateの係数/幾何/境界scopeをhold |
| INT-EQREV-024 | INT-EQF-024 / C:X→[0,Cmax) | P2 J §1; INT-INLINE-039 | EXPLICIT | INT-CLM-040,043 | NO CHANGE | explicit C map宣言を保持。Xの測定/幾何の完成とはしない |
| INT-EQREV-025 | INT-EQF-025 / P2 inference update | P2 §2–3; INT-MATH-P2E-006, INT-MATH-P2J-010, INT-MATH-P2J-013, INT-MATH-P2J-017, INT-INLINE-022, INT-INLINE-023, INT-INLINE-048, INT-INLINE-049, INT-INLINE-052, INT-INLINE-071 | CONFLICTING | INT-CLM-046,051 | AUTHORITY RESOLUTION REQUIRED | single-stateとset-valued Fの採用対象を先に決定。自動修理しない |
| INT-EQREV-026 | INT-EQF-026 / strict justification increase | P2 §2–3,D; INT-MATH-P2E-008, INT-MATH-P2E-011, INT-MATH-P2J-018, INT-MATH-P2J-020, INT-INLINE-072 | PARTIAL | INT-CLM-051 | FORMAL ASSUMPTION REQUIRED | strict-Jとadmissibility/fixedθ-Aの前提を露出、経験的普遍性を前提化しない |
| INT-EQREV-027 | INT-EQF-027 / nonfixed-point theorem / contradiction sequence | P2 §3,D; INT-MATH-P2E-012, INT-MATH-P2E-013, INT-MATH-P2E-014, INT-MATH-P2E-015, INT-MATH-P2J-019, INT-MATH-P2J-021, INT-MATH-P2J-022, INT-MATH-P2AJ-006, INT-INLINE-024, INT-INLINE-053, INT-INLINE-054, INT-INLINE-055, INT-INLINE-080, INT-INLINE-081, INT-INLINE-082, INT-INLINE-083, INT-INLINE-084, INT-INLINE-087 | PARTIAL | INT-CLM-051–054 | PROSE-SCOPE ONLY | 条件付きnoFP statement/sketchを独立証明認証にせず認知一般化と分離 |
| INT-EQREV-028 | INT-EQF-028 / internal stopping predicate | P2 §2–3,D; INT-MATH-P2E-010, INT-INLINE-057, INT-INLINE-058, INT-INLINE-085, INT-INLINE-086 | EXPLICIT | INT-CLM-052 | PROSE-SCOPE ONLY | hypothetical binary Sを採用済cognitive classifierにしない |
| INT-EQREV-029 | INT-EQF-029 / Cij exponential relation | P2 J §2,A; INT-MATH-P2J-015, INT-MATH-P2AJ-005, INT-INLINE-070 | PARTIAL | INT-CLM-048 | FORMAL ASSUMPTION REQUIRED | λρHのrange/unitと応答への適用条件は未固定 |
| INT-EQREV-030 | INT-EQF-030 / Ωθ and A/B reconfiguration | P2 §1–2,A; prose-only; dedicated ledgers below | PARTIAL | INT-CLM-043,049 | TYPING CLARIFICATION NEEDED | Ωθ/parameter/A-Bをlayerや実行operatorと統合しない |
| INT-EQREV-031 | INT-EQF-031 / emergence U=Φ(L,H) | P2 §1,E; INT-MATH-P2E-004, INT-MATH-P2AE-002, INT-MATH-P2J-011, INT-MATH-P2AJ-007, INT-INLINE-026, INT-INLINE-043, INT-INLINE-060, INT-INLINE-077, INT-INLINE-089 | UNRESOLVED | INT-CLM-044,093 | TYPING CLARIFICATION NEEDED | U/calUとΦ演算子のsignature未固定。schema以上へ上げない |
| INT-EQREV-032 | INT-EQF-032 / LE=Φ(LR motion,H) | P2 §5,A; INT-MATH-P2E-005, INT-MATH-P2E-016, INT-MATH-P2J-025, INT-MATH-P2AJ-001, INT-INLINE-063, INT-INLINE-073 | UNRESOLVED | INT-CLM-037,059–060 | TYPING CLARIFICATION NEEDED | LR motion/H入力とLE layer出力は名前だけで共通spaceなし |
| INT-EQREV-033 | INT-EQF-033 / E[LE,xn] and E not in F^k | P2 §5,A; INT-MATH-P2E-018, INT-MATH-P2J-027, INT-MATH-P2AJ-002, INT-INLINE-061, INT-INLINE-074, INT-INLINE-075 | UNRESOLVED | INT-CLM-063 | TYPING CLARIFICATION NEEDED | EそのものとE[LE,x]作用、F反復集合との関係を分ける |
| INT-EQREV-034 | INT-EQF-034 / Φext≡Φnet | P2 §5,D; INT-MATH-P2E-019, INT-MATH-P2E-026, INT-MATH-P2J-028, INT-MATH-P2AJ-003, INT-INLINE-027, INT-INLINE-029, INT-INLINE-076 | UNRESOLVED | INT-CLM-064–065 | POSSIBLE EQUATION CHANGE | field/networkの≡をliteral identityとして保つには型/関係意図が未決。記号変更も将来選択肢 |
| INT-EQREV-035 | INT-EQF-035 / response/silence Hji≈0 and Hji>0 | P2 §4,6; INT-INLINE-025, INT-INLINE-059, INT-INLINE-062 | PARTIAL | INT-CLM-055,067 | PROSE-SCOPE ONLY | 応答/沈黙のthreshold-roleを維持、≈0の観測cutoffを新設しない |
| INT-EQREV-036 | INT-EQF-036 / Ωintel subset Ωlife | P2 J §1; INT-INLINE-044 | UNRESOLVED | INT-CLM-045 | AUTHORITY RESOLUTION REQUIRED | Bio/Int集合の同一ambient space採用とsource intentが未確定 |
| INT-EQREV-037 | INT-EQF-037 / error tolerance ↔ μθ | P2 J §10,D; INT-INLINE-091, INT-INLINE-092, INT-INLINE-093 | UNRESOLVED | INT-CLM-080 | POSSIBLE EQUATION CHANGE | error/μの双方向記号が意図する同値を未定式化。scope/意図決定後に式側要否 |
| INT-EQREV-038 | INT-EQF-038 / Δvintel=vinf−vLR | P2 §11; INT-MATH-P2E-025, INT-MATH-P2J-031, INT-INLINE-028, INT-INLINE-064 | PARTIAL | INT-CLM-082 | TYPING CLARIFICATION NEEDED | 二rateの共通time/単位/stepの署名が未定 |
| INT-EQREV-039 | INT-EQF-039 / Σ development/activity quantity | P2 J §1,A; prose-only; dedicated ledgers below | PARTIAL | INT-CLM-089 | PROSE-SCOPE ONLY | Σを発達度/活性度futureとして保持、相図setにしない |
| INT-EQREV-040 | INT-EQF-040 / three-axis regions / zero-motion condition | P2 §11; INT-INLINE-050, INT-INLINE-065, INT-INLINE-066 | PARTIAL | INT-CLM-081–085 | PROSE-SCOPE ONLY | 三軸/zero-motionをqualitative model diagramに限定、数値境界追加なし |
| INT-EQREV-041 | INT-EQF-041 / VED E(A) / stopping functional minimum comparison | P2 J E; prose-only; dedicated ledgers below | UNRESOLVED | INT-CLM-089,093 | AUTHORITY RESOLUTION REQUIRED | body futureとJA AppendixE present localminimumの採用差が未決 |
| INT-EQREV-042 | INT-EQF-042 / fluid continuity analogy | P2 J §3; INT-INLINE-056 | PARTIAL | INT-CLM-051 | NO CHANGE | fluid continuityは比較用既存式。知性PDEへ採用しない |
| INT-EQREV-043 | INT-EQF-043 / P1 S={si,...} | P1 §3; INT-MATH-P1E-001, INT-MATH-P1J-001 | INFERRED | INT-CLM-005–006 | NO CHANGE | Sの列挙を保持、connectednessとspecific topologyは別 |
| INT-EQREV-044 | INT-EQF-044 / T not in Internal(R) | P1 §8–9; INT-MATH-P1E-013, INT-MATH-P1E-014, INT-MATH-P1J-015, INT-MATH-P1J-016 | UNRESOLVED | INT-CLM-021,025 | TYPING CLARIFICATION NEEDED | Internal(R)と停止Tの集合/作用域をuntyped schematicとしてhold |
| INT-EQREV-045 | INT-EQF-045 / P1 Fbio discrete update | P1 J §5; INT-INLINE-014 | PARTIAL | INT-CLM-013 | TYPING CLARIFICATION NEEDED | Fbio discreteとconductance continuousの変換は未型付け |
| INT-EQREV-046 | INT-EQF-046 / P2 Bio continuous F(x;θ) | P2 J §1–2; INT-MATH-P2J-014, INT-INLINE-038, INT-INLINE-078 | PARTIAL | INT-CLM-045–050 | PROSE-SCOPE ONLY | BioFをinferenceFと区別するguardを維持 |
| INT-EQREV-047 | INT-EQF-047 / J:X→R justification | P2 §2–3; INT-MATH-P2E-007, INT-INLINE-051, INT-INLINE-079 | EXPLICIT | INT-CLM-046,051 | NO CHANGE | J:X→Rの形式宣言を保持、測定済justificationにしない |
| INT-EQREV-048 | INT-EQF-048 / set-valued F continuation | P2 E §2; INT-MATH-P2E-009 | CONFLICTING | INT-CLM-046,051 | AUTHORITY RESOLUTION REQUIRED | EN set-valued branchとJ compositionの扱いをauthor/formal decisionへ。式変更可能性は副次hold |
| INT-EQREV-049 | INT-EQF-049 / C operational stability / denied C=truth | P2 E §10; INT-MATH-P2E-023, INT-MATH-P2E-024, INT-INLINE-032 | PARTIAL | INT-CLM-040,078 | PROSE-SCOPE ONLY | 肯定C=stabilityと否定C=truthを区別しlocal namingに限定 |
| INT-EQREV-050 | INT-EQF-050 / LF→LR→LE architecture sequence | P2 §0–2; INT-MATH-P2E-001, INT-MATH-P2J-005, INT-MATH-P2J-012, INT-MATH-P2J-016, INT-MATH-P2J-024, INT-INLINE-031 | UNRESOLVED | INT-CLM-037,057–060 | PROSE-SCOPE ONLY | 三層矢印をarchitecture schemaとして限定、composed dynamicsにしない |
| INT-EQREV-051 | INT-EQF-051 / difference→F→nonclosure→externalstop chain | P2 §0–1; INT-MATH-P2E-002, INT-MATH-P2J-001, INT-MATH-P2J-002, INT-INLINE-030 | UNRESOLVED | INT-CLM-036,051–054 | PROSE-SCOPE ONLY | exposition chainをVEDからのtyped生成証明にしない |
| INT-EQREV-052 | INT-EQF-052 / H→response threshold→μ→sapiens chain | P2 J §0; INT-MATH-P2J-003, INT-MATH-P2J-004 | UNRESOLVED | INT-CLM-048–049 | PROSE-SCOPE ONLY | H/threshold/μ chainを機能仮説へ限定 |
| INT-EQREV-053 | INT-EQF-053 / LE→Φnet→externally dependent existence | P2 J §0; INT-MATH-P2J-006 | UNRESOLVED | INT-CLM-037,064 | PROSE-SCOPE ONLY | LE→networkの図式をexistence/implementation保証にしない |
| INT-EQREV-054 | INT-EQF-054 / μ→B→E-site→LRconvergence→LE | P2 §5,A; INT-MATH-P2E-017, INT-MATH-P2J-026, INT-MATH-P2AJ-004 | UNRESOLVED | INT-CLM-060 | PROSE-SCOPE ONLY | 四stageをschematic hypothesisへ限定。update/収束はOPEN |
| INT-EQREV-055 | INT-EQF-055 / environmental locus ↦ E site | P2 E §6; INT-MATH-P2E-020 | UNRESOLVED | INT-CLM-067 | PROSE-SCOPE ONLY | environmental locus→E siteを社会的読解として限定 |
| INT-EQREV-056 | INT-EQF-056 / distributed→centralized stopping / singlepole | P2 §7; INT-MATH-P2E-021, INT-MATH-P2J-030 | UNRESOLVED | INT-CLM-069–070 | PROSE-SCOPE ONLY | 中心化/単一極限をhistorical schemaとしnetwork limit theoremにしない |
| INT-EQREV-057 | INT-EQF-057 / centralized→maintained stopping | P2 E §8; INT-MATH-P2E-022 | UNRESOLVED | INT-CLM-071 | PROSE-SCOPE ONLY | maintenance arrowを社会的解釈に限定 |
| INT-EQREV-058 | INT-EQF-058 / God negative identities | P2 J §7; INT-MATH-P2J-029 | UNRESOLVED | INT-CLM-069 | NO CHANGE | Godのnegative identity textは数量式でない。negative scope維持 |
| INT-EQREV-059 | INT-EQF-059 / complete closure implies I→0 | P2 J §1; INT-INLINE-036 | PARTIAL | INT-CLM-042 | FORMAL ASSUMPTION REQUIRED | complete closure→I limitはf/rangeの別前提を必要とする |
| INT-EQREV-060 | INT-EQF-060 / ∇C≈0 / remaining motion | P2 J §1; INT-INLINE-037 | PARTIAL | INT-CLM-042,046 | PROSE-SCOPE ONLY | local quiescenceと全力学/停止の帰結を分離 |
| INT-EQREV-061 | INT-EQF-061 / causal vector closure sums | P2 J §1,E; INT-INLINE-042, INT-INLINE-090, INT-INLINE-094 | PARTIAL | INT-CLM-044,093 | TYPING CLARIFICATION NEEDED | causal vectorsのspace/index/closureとInt対応の署名が未固定 |
| INT-EQREV-062 | INT-EQF-062 / homology kernel incompleteclosure→attractor→sustaineddynamics | P2 E B; INT-MATH-P2AE-001 | UNRESOLVED | INT-CLM-091,093 | PROSE-SCOPE ONLY | homologykernel arrowは提案的役割表で生成法則でない |
| INT-EQREV-063 | INT-EQF-063 / Physarum graph nodes/edges | P1 §4–5; INT-INLINE-001, INT-INLINE-009, INT-INLINE-010, INT-INLINE-013 | PARTIAL | INT-CLM-011–013 | NO CHANGE | Physarum graphの引用的表示は保持、認知graphをそこから創作しない |

## 14. Global equation-change decision

```text
Can equation changes safely begin after Phase06?: NO
Global equation-change requirement currently: OPEN
Decision status: PROVISIONAL / NOT FROZEN
Actual equation changes: NONE
```

NO CHANGE8 / PROSE-SCOPE ONLY22 / TYPING CLARIFICATION NEEDED13 / FORMAL ASSUMPTION REQUIRED13 / AUTHORITY RESOLUTION REQUIRED4 / POSSIBLE EQUATION CHANGE3 / REQUIRED EQUATION CHANGE0 =63。prose/typingの不足整理を先に行うが、全体要否をPROSE/TYPING FIRSTで閉じるだけの根拠はない。

特にEQF012（proposition→field評価）、034（Φext/Φnetの≡）、037（error tolerance↔μ）は、現在の式をどのformal意味で維持するかによって将来の数学変更候補になり得る。EQF025/036/041/048はlanguage/version/adoption authorityを先に確定する。局所極小・set/single F・identityをprose判断だけで修復しない。直接矛盾の新規立証、proofの否定、代替方程式の提示は行っていない。Phase07の独立再照合と必要な別formal decisionまで変更開始はhold。

## 15. Figure revision plan

Phase02 FIGROLE001–014とそのEN/JA比較を継承したpresentation計画。新規描画・画像編集・新しい定量軸・proof図への昇格はない。以下はprimary actionを一つ計数し、caption guard等の併用は説明欄に記す。HOLDは図の廃止ではなくsystem/formal意図の決定待ち。

| FIGREV | figure assets / Phase00 family | section | Phase02 role status | primary action | minimal presentation candidate | boundary |
|---|---|---|---|---|---|---|
| INT-FIGREV-001 | INT-FIG-001 `intelligence-part1/figures/fig1_four_layer_decomposition{,_ja}.{png,svg}` | §2 | CONSISTENT | NO CHANGE | 局所的四役割図として保持 | 新しいcognitive mechanism/計測図の権威を与えない |
| INT-FIGREV-002 | INT-FIG-002 `intelligence-part1/figures/fig2_three_axioms{,_ja}.{png,svg}` | §3 | FIGURE STRONGER | RELABEL | joint conditionsからsufficiencyに読めるlabelを限定; CAPTION GUARD併用 | 三条件構成と一般必要性を図で再結合しない |
| INT-FIGREV-003 | INT-FIG-003 `intelligence-part1/figures/fig3_cross_domain_homology{,_ja}.{png,svg}` | §5 | CONSISTENT | RELABEL | independent convergenceのvalidation読みを比較へ; CAPTION GUARD併用 | 外部実例の証拠とInt mappingの証拠を分離 |
| INT-FIGREV-004 | INT-FIG-004 `intelligence-part1/figures/fig4_branching_explosion{,_ja}.{png,svg}` | §7 | FIGURE STRONGER | RELABEL | necessary連鎖/共通scaleをschematicに限定; CAPTION GUARD併用 | 所与graph曲線≠実測認知branch/必然的心理発散 |
| INT-FIGREV-005 | INT-FIG-005 `intelligence-part1/figures/fig5_four_layer_correspondence{,_ja}.{png,svg}` | §9 | AMBIGUOUS | CAPTION GUARD | 四層はproposed role comparison、substrate必要性は別候補 | 矢印を生成/同じcarrierの証明にしない |
| INT-FIGREV-006 | INT-FIG-006 `intelligence-part2/figures/fig1_c_landscape{,_ja}.{pdf,svg}` | §3 | AMBIGUOUS | CAPTION GUARD | strict-J/fixedθ-A、Cmax barrier、cognitive pathを別burdenとして明記する計画 | 図が理論/認知の同型証明にならない。境界配置のformal解釈はhold |
| INT-FIGREV-007 | INT-FIG-007 `intelligence-part2/figures/fig2_responsive_silent_threshold{,_ja}.{pdf,svg}` | §4 | CONSISTENT | CAPTION GUARD | response thresholdはcandidate regime、未較正 | 境界の位置や移動を測定済としない |
| INT-FIGREV-008 | INT-FIG-008 `intelligence-part2/figures/fig3_mutual_constraint_mu_theta{,_ja}.{pdf,svg}` | §5 | CONSISTENT | RELABEL | μ/H→E-siteの作用表示をschematic hypothesisへ; CAPTION GUARD併用 | 投影/LE生成が実行済と見えないようにする |
| INT-FIGREV-009 | INT-FIG-009 `intelligence-part2/figures/fig4_three_layer_architecture{,_ja}.{pdf,svg}` | §5 | FIGURE STRONGER | HOLD / OPEN | EN Transformer LF/LR/LEが個体profileかwhole systemか先に確定 | sourceのown LE不在と図scopeの整合を選択。自動node追加/削除しない |
| INT-FIGREV-010 | INT-FIG-010 `intelligence-part2/figures/fig5_three_examples_of_emergence{,_ja}.{pdf,svg}` | §5 | BODY STRONGER | NO CHANGE | 提案的三例比較と非identity guardを保持 | bodyの強い同型表現は別のprose candidate |
| INT-FIGREV-011 | INT-FIG-011 `intelligence-part2/figures/fig6_phi_ext_phi_net{,_ja}.{pdf,svg}` | §5 | CONSISTENT | HOLD / OPEN | Φext≡Φnet relationのformal/prose扱い決定と同時に図を計画 | 単純なsymbol typoでない。独立field/network測定を図で保証しない |
| INT-FIGREV-012 | INT-FIG-012 `intelligence-part2/figures/fig7_evolution_of_stopping_structures{,_ja}.{pdf,svg}` | §9 | AMBIGUOUS | CAPTION GUARD | 階段を史実の進歩/因果順序としない運用レパートリーとして限定 | nonprogress guard維持、史料/chronologyの実証図にしない |
| INT-FIGREV-013 | INT-FIG-013 `intelligence-part2/figures/fig8_phase_diagram{,_ja}.{pdf,svg}` | §11 | CONSISTENT | RELABEL | only narrow band/phase boundariesをqualitative hypothesisへ; CAPTION GUARD併用 | 数値axis/測定fitを新規追加しない |
| INT-FIGREV-014 | INT-FIG-014 `intelligence-part2/figures/fig9_cross_domain_homology{,_ja}.{pdf,svg}` | §13 | BODY STRONGER | NO CHANGE | crossdomainのproposed analogy/typed nonidentity guardを保持 | 同じgrammarで実証と呼ばない |

## 16. EN / JA revision asymmetry

36 FVAR全件を個別にreviewする。synchronizeは将来のauthority承認後のscope/guard整合候補であってENへの一律同化ではない。JA-only equationを削除せず、EN-only set-valued FをJAへ移植しない。Phase00 AUTHCONFLICT001–028は未解決事項を含むまま保持し、candidateだけで版選択しない。

| LANGREV | FVAR / subject | source | Phase01 formal variant | candidate action | reason / limit |
|---|---|---|---|---|---|
| INT-LANGREV-001 | INT-FVAR-001 / P1 state S/Φ axiom | §3 | SAME | strengthen guard | 3axiomsの定義と必要性のscopeを両言語で分離 |
| INT-LANGREV-002 | INT-FVAR-002 / P1 update/order | §3 | SAME | strengthen guard | update orderingと履歴保持の過程を区別 |
| INT-LANGREV-003 | INT-FVAR-003 / P1 PhysarumQ,D | §4 | SAME | no action | 引用Q/D式の同一性を維持。mapping proseは別対象 |
| INT-LANGREV-004 | INT-FVAR-004 / P1 powerresponse | J§4 | JA ONLY | preserve language-specific difference | JA power-response例はJAに留め、domain採用を自動補完しない |
| INT-LANGREV-005 | INT-FVAR-005 / P1 Transformerhiddenstates | §5 | SAME | no action | hidden-state数学的表示を変更しない |
| INT-LANGREV-006 | INT-FVAR-006 / P1 biologicalFbio | J§5 | JA ONLY | preserve language-specific difference | JA discrete FbioをENへ強制移植しない |
| INT-LANGREV-007 | INT-FVAR-007 / P1 I/divJ/correctness | §7 | DIFFERENT FORMULATION | strengthen guard | I/divJ/correctnessのrole間橋を未確定のまま分離 |
| INT-LANGREV-008 | INT-FVAR-008 / P1 branch counts | §7 | DIFFERENT FORMULATION | synchronize | edge/path数の条件付きscopeを対応させる計画。式形は未変更 |
| INT-LANGREV-009 | INT-FVAR-009 / P1 internalT | §8–9 | SAME | strengthen guard | TnotInternalを任意認知停止の観測判定としない |
| INT-LANGREV-010 | INT-FVAR-010 / P1 externalT | §9 | SAME | strengthen guard | External(R)所属と社会的外化の仮説を分離 |
| INT-LANGREV-011 | INT-FVAR-011 / P1 horizon/Consymbols | §9 | DIFFERENT FORMULATION | resolve authority first | Con追加変数/時間語のexact sourceと対象を先に特定 |
| INT-LANGREV-012 | INT-FVAR-012 / P2 closure PDE | J§1,3 | JA ONLY | resolve authority first | JA PDEのversion/採用scopeを先に特定。ENを自動強化しない |
| INT-LANGREV-013 | INT-FVAR-013 / P2 C-range mapping | J§1 | JA ONLY | preserve language-specific difference | JA C map宣言は保持、ENとの形式差を明記 |
| INT-LANGREV-014 | INT-FVAR-014 / P2 f examples | J§1 | JA ONLY | preserve language-specific difference | JA f例をoptional/version-localとして維持。domain未決 |
| INT-LANGREV-015 | INT-FVAR-015 / P2 FI/JC | J§1,3,A | JA ONLY | resolve authority first | FI/JC等のupstream適用・JA固有formal scopeを先に確定 |
| INT-LANGREV-016 | INT-FVAR-016 / P2 Fsingle/set | E§2 | EN ONLY | resolve authority first | single/set-valued F選択を翻訳の好みで決めない |
| INT-LANGREV-017 | INT-FVAR-017 / P2 Jsignature | E§2/J§3 | SAME | no action | Jの明示mapと所在差を保持 |
| INT-LANGREV-018 | INT-FVAR-018 / P2 T3.1statement | §3 | SAME | strengthen guard | 条件付きnoFPとproof未監査・認知bridgeを分離 |
| INT-LANGREV-019 | INT-FVAR-019 / P2 P3 | §3 | DIFFERENT FORMULATION | strengthen guard | fixedθ/Aを維持。JAのupstream groundingを証拠へ移さない |
| INT-LANGREV-020 | INT-FVAR-020 / P2 internalS corollary | J§3,D | JA STRONGER | downgrade JA strength | Sのconditional modelから任意認知停止不能への強化を限定 |
| INT-LANGREV-021 | INT-FVAR-021 / P2 Cmaxisomorphism | J§3,D | JA STRONGER | downgrade JA strength | Cmax/nonclosureの同型をrole analogyとtyped OPENへ分離 |
| INT-LANGREV-022 | INT-FVAR-022 / P2 individualclosure | J§3,D | JA STRONGER | downgrade JA strength | individual collapseの必要性をqualitative interpretationへ |
| INT-LANGREV-023 | INT-FVAR-023 / P2 Cij relation | J§2,A | JA ONLY | preserve language-specific difference | JA Cij formal relationは保持しresponse map未較正を明示する方向 |
| INT-LANGREV-024 | INT-FVAR-024 / P2 Ω subset | J§1 | JA ONLY | resolve authority first | Ω subsetのambient space/採用意図を先に確定 |
| INT-LANGREV-025 | INT-FVAR-025 / P2 U/LE schema | §1,5,E | DIFFERENT FORMULATION | resolve authority first | U/calU/Φschemaの意図、formal同一性を自動正規化しない |
| INT-LANGREV-026 | INT-FVAR-026 / P2 E andPhiidentity | §5 | SAME | strengthen guard | shared expressionsでもE作用/二視点とidentityのburdenを分離 |
| INT-LANGREV-027 | INT-FVAR-027 / P2 μ/errortolerance | J§10,D | JA STRONGER | downgrade JA strength | JA↔sketchを独立同値保証にしない。ENの弱いcouplingを自動強化しない |
| INT-LANGREV-028 | INT-FVAR-028 / AppendixD | D | DIFFERENT FORMULATION | preserve language-specific difference | JA proof collectionとEN optional notesを翻訳等価としない。proof監査は別 |
| INT-LANGREV-029 | INT-FVAR-029 / AppendixB | B | JA ONLY | preserve language-specific difference | JA追加CT/θ/F表を保持しrole/typed境界を明記 |
| INT-LANGREV-030 | INT-FVAR-030 / AppendixE | E | DIFFERENT FORMULATION | resolve authority first | JA LE minimum現在形とbody future/EN比較の採用差をhold |
| INT-LANGREV-031 | INT-FVAR-031 / MasterΣ | A | JA ONLY | preserve language-specific difference | Σ development quantityはJA future。相図setへ統合しない |
| INT-LANGREV-032 | INT-FVAR-032 / phase speedgap | §11 | SAME | strengthen guard | speedgap式とcollapse機構のscopeを分離 |
| INT-LANGREV-033 | INT-FVAR-033 / masterprincipalrelations | A | JA ONLY | resolve authority first | Master principal relation summariesのexact predecessor/採用scopeをhold |
| INT-LANGREV-034 | INT-FVAR-034 / fluidcontinuityanalogy | J§3 | JA ONLY | preserve language-specific difference | JA fluid analogyを保持、Int evolutionへ採用しない |
| INT-LANGREV-035 | INT-FVAR-035 / C=truthnegation | E§10 | EN ONLY | no action | ENの否定されたC=truthとJAprose否定は役割等価を維持 |
| INT-LANGREV-036 | INT-FVAR-036 / P1 Φbio mapdisplay | J§5 | JA ONLY | preserve language-specific difference | JA Φbio mapdisplayは対応例の形式差として保持 |

## 17. Revision order — Phase07後の候補

これはsource変更への着手許可ではなく依存順序。navigation/exposition orderを証明順序にしない。各段のauthor/formal holdを解消したと仮定して先へ進まない。

| REVORDER | stage | source / target | gate |
|---|---|---|---|
| INT-REVORDER-001 | authority/documentary scope | P1 EN/JA primary status、P2 JA/EN差、CLM039/090/093を先に分岐 | author/version選択が要る箇所はhold、prose候補は研究解決を先取りしない |
| INT-REVORDER-002 | formal/signature scope | 63 EQREVと同glyph分離、single/set F・identity・localminを整理 | 式変更なし。必要型/仮定の採用は独立decisionまでhold |
| INT-REVORDER-003 | P1 definitions / lower bound | §2–5のlocal definitions・三条件・globalΦ/具体比較 | 保持定義と一般必要性・empirical convergenceを分離 |
| INT-REVORDER-004 | P1 branching / stopping / horizon | §6–9のGettier/graph/中断/外化 | formal/認知/心理/社会を分けてsummaryの前に確定 |
| INT-REVORDER-005 | P2 theorem interpretations | §1–4・Dの条件付きnoFP/S/Cmax | proof review未実施を隠さず、任意認知停止への橋をhold |
| INT-REVORDER-006 | P2 LE / μ / Φnet | §5・10–12の機能命名、生成hypothesis、identity | SERIOUS001–005のbackedgesを候補上切り分ける。解決認定はしない |
| INT-REVORDER-007 | social / historical / intelligence scope | §6–9,12でlocal naming・仮説・negative guardを分ける | general/sapiens/collectiveを統合しない |
| INT-REVORDER-008 | summary synchronization | P1 abstract/§1/10、P2abstract/§0/13 | bodyのsplitを再結合しない。JAabstract未移植を勝手に補わない |
| INT-REVORDER-009 | figures / captions | 14 figure familiesを本文候補に従わせる | FIG009/011のhold解除が必要。測定図へ昇格しない |
| INT-REVORDER-010 | EN/JA synchronization | 36LANGREVに従い、authority確定後に並行sourceを扱う | EN優先/JA自動canonical化はしない。意味差は履歴化 |
| INT-REVORDER-011 | distribution | 選択されたsource/build routeとfiguresが整合後に配布更新 | このphaseではbuildしない。現在freshnessを変更しない |
| INT-REVORDER-012 | independent post-implementation check | 将来実装後のsource/figures/versionsを直接再監査 | 監査record自己申告で完了認定しない |

## 18. Social / historical synthesis

Part II§6–9を中心に§0/10への射程も分離する。概念的再記述・歴史仮説・因果説明・一般社会法則は異なるburden。歴史資料・比較選択規則の未所在を、図のstaircaseやcategory namingで埋めない。non-progress guardとlocal namingは残す。

| SOCREV | claim | subject | current/safely separated class | retainable component | strong component / OPEN |
|---|---|---|---|---|---|
| INT-SOCREV-001 | INT-CLM-038 | historical intelligence | historical hypothesis | 知性史の停止構造としての読み | 独立historiographyなし、停止発達の一般史法則へしない |
| INT-SOCREV-002 | INT-CLM-067 | animism | conceptual reinterpretation retainable | 応答付与/停止設置という局所naming | channel生成の社会機構は仮説、OPEN017/018 |
| INT-SOCREV-003 | INT-CLM-068 | animism universality | unsupported strong claim | 低costの比較hypothesisまで | cost/母集団なし。普遍性説明の達成は残せない |
| INT-SOCREV-004 | INT-CLM-069 | God | conceptual reinterpretation retainable | 保留/委任という機能命名 | operatoridentity/歴史的中心化causeを分離 |
| INT-SOCREV-005 | INT-CLM-070 | centralization | historical hypothesis | 中心化と曖昧性の質的比較 | effectを検証済とせずnonprogress guard維持 |
| INT-SOCREV-006 | INT-CLM-071 | religion | conceptual reinterpretation retainable | 維持運用というrole | 世代持続/予防はcausal historical claimとして別burden |
| INT-SOCREV-007 | INT-CLM-072 | science | conceptual reinterpretation retainable | 改訂運用というroleとtruth序列否定 | science全般の実証歴史法則でない |
| INT-SOCREV-008 | INT-CLM-073 | finite sapiens/pathology | unsupported strong claim | 非clinical regime hypothesis | 症状名をdiagnostic/causal prevention根拠にしない |
| INT-SOCREV-009 | INT-CLM-074 | social blockchain | conceptual reinterpretation retainable | 非crypto consensus analogy | 運用protocol/集団機構の検証でない |
| INT-SOCREV-010 | INT-CLM-075 | Git/social costs | historical hypothesis | 条件付き社会/技術cost comparison | cost単位/対象設定はOPEN019 |
| INT-SOCREV-011 | INT-CLM-076 | legitimacy | unsupported strong claim | 歴史的受容・責任の文脈依存という解釈 | principled noncomputabilityはformal problem未所在 |
| INT-SOCREV-012 | INT-CLM-077 | individual creativity | unsupported strong claim | 個体/社会の役割分担hypothesis | creation only individualというgeneral social lawへしない |

## 19. General-intelligence synthesis

定義の局所性とcross-domain一般化を分離する。知性一般をsapiensの内発μで再定義しない。Transformer/Physarum profileを三層の実証または全知性の必要条件の確認としない。

| GENREV | scope | definitional component retainable | weaken / distinguish | research OPEN / do not generalize | source |
|---|---|---|---|---|---|
| INT-GENREV-001 | intelligence-like lower bound | 3axiomsのmodel-local構成 | 一般共同必要性・全substrate収束の確認 | independent S/order/Φ criterion; OPEN001/005/021 | P1§3–5,10 |
| INT-GENREV-002 | model-local intelligence | motion/三層維持stateの定義 | 定義から実生成・実安定性を説明する強度 | LF/LR/LE同定・生成; OPEN007/008/021 | P1§2; P2§5,12 |
| INT-GENREV-003 | general intelligence | source内のgeneral model profile | 全intelligenceの必要十分law | 適用対象/外部停止源/criterion; OPEN021 | P2§12 N/R/最終条項I |
| INT-GENREV-004 | sapiens intelligence | 内発μ追加のlocal profile | 全人類/自律能力の経験的普遍化 | 内発性/μ/error別endpoint; OPEN009/010/021 | P2§2,5,12最終条項II |
| INT-GENREV-005 | biological intelligence | Physarum source例のrole比較 | 全Bio/生命必要基盤・secondattractor実装 | typed Bio→IntとLE判定; OPEN015/023 | P1§5,9; P2§5,B,E |
| INT-GENREV-006 | artificial intelligence | Transformerのcarrier/stop profile | ownLE不存在/全AIphase constraint | 対象モデル/自前・外部stop; OPEN016 | P1§5; P2§5,11 |
| INT-GENREV-007 | social intelligence | log/block/共同受容の局所naming | 社会mechanismの必然性/個体創造排他性 | node/aggregate/史料/比較; OPEN011/017–019/021 | P2§5,9,12 |

## 20. Homology synthesis

全21HOMOを維持して計画化する。KEEP AS LEXICAL/ROLE ANALOGYはclaim primary KEEPを自動意味しない。同じrowのhomologyとvalidation readingを別burdenへ分ける。domain同士に独立研究があることはInt mappingの独立検証ではない。X3 maxは保持し、typed translationを作らない。

| HOMOREV | Phase00 homology | source/domain relation | preserved role | candidate class | boundary |
|---|---|---|---|---|---|
| INT-HOMOREV-001 | INT-HOMO-001 | P1 §4 Tero Q,D,reinforcement,BC → J,I,projection,Φ | flow/log/bias; I0/I1 | KEEP AS LEXICAL | Q/D/BC対応表とnonidentityを保持。独立実証的確認は別claimで弱化 |
| INT-HOMOREV-002 | INT-HOMO-002 | P1 §5 Physarum ↔ Transformer | S/order/Φ三公理; I1/I2 | KEEP AS ROLE ANALOGY | carrier/三条件比較は保持、一般充足/必要性の検証と分離 |
| INT-HOMOREV-003 | INT-HOMO-003 | P1 §9 VED4DH ↔ Int localhorizon | unreachability/divergence/finiteabsorption; I0/I2 | DOWNGRADE FROM FORMAL | same boundaryのformal読みをrole comparisonへ;typed horizon mapはOPEN |
| INT-HOMOREV-004 | INT-HOMO-004 | P1 §9 physical ↔ Bio ↔ Con ↔ Int | fourlayerroles; I0/I2/I4/I3 | KEEP AS ROLE ANALOGY | substrate/carrier非同一guard維持。生命必要基盤は別claim030 |
| INT-HOMOREV-005 | INT-HOMO-005 | P1 J §8 paperclip ↔ individual nonclosure | nointernalstop; I1/I2 | KEEP AS ROLE ANALOGY | paperclipはthought analogy。alignment一般のroot説明は弱化 |
| INT-HOMOREV-006 | INT-HOMO-006 | P2 §3,D nonfixedF ↔ Cmax ↔ DH | nonclosure; I0/I2 | DOWNGRADE FROM FORMAL | 同一proposition/isomorphismからnonclosure role類似へ |
| INT-HOMOREV-007 | INT-HOMO-007 | P2 §4 regress ↔ branching | sameinferenceextension; I0/I2 | KEEP AS ROLE ANALOGY | regressとbranchingの役割類似まで。graph/cognition同一性はOPEN |
| INT-HOMOREV-008 | INT-HOMO-008 | P2 §1,E physicalparticle ↔ life ↔ LE | lower motion+H→upperattractor; I0/I2 | SPLIT IDENTITY/ANALOGY | local U/Φschemaと実在上位生成/同一機構を分離 |
| INT-HOMOREV-009 | INT-HOMO-009 | P2 J B.1 CT ↔ physical/Bio/Con/Int | closure/attractor/horizon/branching; I0/I1/I2/I4 | KEEP AS ROLE ANALOGY | JA CT列はrole表として保持、CTのclosureをIntvalidationにしない |
| INT-HOMOREV-010 | INT-HOMO-010 | P2 J B.2 / fig5 threeemergencecases | particle/life/stopping; I0/I2 | KEEP AS ROLE ANALOGY | 三emergence例は既存guard付きcomparison |
| INT-HOMOREV-011 | INT-HOMO-011 | P2 §5,B.3 Conprojection ↔ IntE-siteprojection ↔ psychprojection | projection role; I1/I2/I4 | SPLIT IDENTITY/ANALOGY | Conprojection語彙/心理非同一guardと同じoperator具現を分離 |
| INT-HOMOREV-012 | INT-HOMO-012 | P2 J §2,B.4 DNAθ ↔ Intθ ↔ sapiensμ | constraintmobility; I0/I2 | DOWNGRADE FROM FORMAL | DNA/Int θのsame principleをtime-scale correspondenceへ |
| INT-HOMOREV-013 | INT-HOMO-013 | P2 §2,B.5 BioF ↔ inferenceF | localstateevolution role; I0/I1 | KEEP AS ROLE ANALOGY | BioF/IntFのnonidentity guardを保持 |
| INT-HOMOREV-014 | INT-HOMO-014 | P2 §5,B.6 Physarum/Transformer/sapiens | LF/LR/LEstorage/μprofiles; I1/I2 | KEEP AS ROLE ANALOGY | 3profileは具体例の比較。ownLE/内発μの実証は別OPEN |
| INT-HOMOREV-015 | INT-HOMO-015 | P2 §6–9,B.6 animism/God/religion/socialBC | LEinstallation/compression/maintenance/sync; I2/I3 | KEEP AS ROLE ANALOGY | 歴史運用形態の機能比較。因果法則/必然順序にしない |
| INT-HOMOREV-016 | INT-HOMO-016 | P2 §9 Git ↔ socialBC | branch/merge/rollback vsconsensus; I1/I3 | KEEP AS ROLE ANALOGY | Git/social costはanalogous役割。実装protocolでない |
| INT-HOMOREV-017 | INT-HOMO-017 | P2 §5,D Φext ↔ Φnet | same stopping relation external/internalview; I0/I3 | SPLIT IDENTITY/ANALOGY | 二視点namingとliteral field/networkidentityを分離 |
| INT-HOMOREV-018 | INT-HOMO-018 | P2 J §10,D error tolerance ↔ μθ | revisability/endogenousmovement; I0/I2 | SPLIT IDENTITY/ANALOGY | revisabilityの対応とμ/errorのformal↔を分離 |
| INT-HOMOREV-019 | INT-HOMO-019 | P2 §11 ConΔv ↔ IntΔvintel | speedgap/logtracking; I0/I2/I4 | KEEP AS ROLE ANALOGY | 二種Δvのcandidate comparison。同じclock/unitとしない |
| INT-HOMOREV-020 | INT-HOMO-020 | P2 B/E/fig9 physics/Bio/Con/Int/social | nonclosure→attractor→sustaineddynamics; I0–I4 | SPLIT IDENTITY/ANALOGY | 提案的crossdomain role patternとsame grammarの強機構読解を分離 |
| INT-HOMOREV-021 | INT-HOMO-021 | P2 J E VEDemergence ↔ weak/strong/holistic/functional emergence | dynamicrelationalposition; I0/I2 | KEEP AS ROLE ANALOGY | 既存emergence概念との概念比較、外部検証を新設しない |

## 21. OPEN research-route preservation

INT-OPEN-001–024は全件存続、統合0・閉鎖0。primary OPEN2とresearch routes24は異なる分母である。KEEP候補にも研究上のOPENが関連し得る。以下の旧UリンクはPhase05で当該routeに付されたINT-U-189–218を中心とするnavigationで、旧問題の書換えではない。

| OPEN06 | Phase05 route / source problem | source / missing route | related claims | old uncertainty links | provisional revision consequence | still OPEN? |
|---|---|---|---|---|---|---|
| INT-OPEN06-001 | INT-OPEN-001 / 状態・推論stepの同定 | CORR001–003/016; P1§3,5; P2§2; 観測列からS/X/F/LFへの符号化・切出し未所在 | INT-CLM-004, INT-CLM-005, INT-CLM-006, INT-CLM-007, INT-CLM-021, INT-CLM-043, INT-CLM-046, INT-CLM-051, INT-CLM-052 | INT-U-189 | SPLIT/KEEP/REVISE; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-002 | INT-OPEN-002 / 正当化とtruthの独立endpoint | CORR004; GETTIERCORR005; P2§3,10; J、correctness、truthの観測基準が別途未定 | INT-CLM-003, INT-CLM-015, INT-CLM-016, INT-CLM-021, INT-CLM-040, INT-CLM-046, INT-CLM-051, INT-CLM-066, INT-CLM-078 | INT-U-190 | KEEP/SPLIT/DOWNGRADE/REVISE; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-003 | INT-OPEN-003 / C/Cij/Hの観測対応 | CORR006–007/020; P2§1–4; 安定性・双方向応答から値を同定するruleなし | INT-CLM-040, INT-CLM-041, INT-CLM-042, INT-CLM-048, INT-CLM-055, INT-CLM-066 | INT-U-191, INT-U-192 | KEEP/REVISE/SPLIT; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-004 | INT-OPEN-004 / I/fluxと認知分岐 | CORR005/033–034/038; P1§4,7; P2§1; density、flow、closureflux、心理発散の橋未定 | INT-CLM-010, INT-CLM-017, INT-CLM-041 | INT-U-193 | KEEP/SPLIT/REVISE; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-005 | INT-OPEN-005 / Φのglobal-bias同定 | CORR008–010; P1§3–5; boundary/weights/loss等の役割比較からscalar値へのmapなし | INT-CLM-005, INT-CLM-008, INT-CLM-010, INT-CLM-012, INT-CLM-065 | INT-U-194 | SPLIT/KEEP/DOWNGRADE; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-006 | INT-OPEN-006 / 停止の識別 | STOPCORR001–009; P1§8; P2§3,5; 不動点・終了・中断・外部停止の独立区分なし | INT-CLM-019, INT-CLM-021, INT-CLM-022, INT-CLM-023, INT-CLM-024, INT-CLM-025, INT-CLM-027, INT-CLM-028, INT-CLM-033, INT-CLM-042, INT-CLM-051, INT-CLM-052, INT-CLM-054, INT-CLM-056, INT-CLM-063 | INT-U-195, INT-U-196 | DOWNGRADE/SPLIT/REVISE/KEEP; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-007 | INT-OPEN-007 / LR保存・参照の分離 | CORR017; P2§5,9; 痕跡所在と再帰的利用の観測を区別するruleなし | INT-CLM-004, INT-CLM-007, INT-CLM-024, INT-CLM-037, INT-CLM-057, INT-CLM-058 | INT-U-197 | SPLIT/REVISE/KEEP; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-008 | INT-OPEN-008 / LE存在・創発・作用の独立検出 | LECORR001–006; P2§5,E; stop観測だけに依存しないLE/収束判定が未定 | INT-CLM-037, INT-CLM-044, INT-CLM-045, INT-CLM-049, INT-CLM-057, INT-CLM-059, INT-CLM-060, INT-CLM-061, INT-CLM-063, INT-CLM-093 | INT-U-198, INT-U-199 | SPLIT/KEEP/DOWNGRADE; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-009 | INT-OPEN-009 / θ/μの境界・内発性 | MUCORR001–006; P2§2,4,5; 応答境界shiftと内発再配置の独立同定なし | INT-CLM-043, INT-CLM-048, INT-CLM-049, INT-CLM-050, INT-CLM-055, INT-CLM-060, INT-CLM-061, INT-CLM-080, INT-CLM-086, INT-CLM-087 | INT-U-200, INT-U-201 | SPLIT/DOWNGRADE/KEEP; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-010 | INT-OPEN-010 / μとerror tolerance | MUCORR004–005; P2§10,12,D; 改訂能力と誤り/許容の別endpointなし | INT-CLM-049, INT-CLM-080 | INT-U-202 | SPLIT; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-011 | INT-OPEN-011 / Φext/Φnetの個体・network対応 | PHICORR001–006; P2§5,7,9; LE node/edge・field値・独立二面測定なし | INT-CLM-037, INT-CLM-064, INT-CLM-065, INT-CLM-069 | INT-U-203, INT-U-204 | SPLIT/DOWNGRADE; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-012 | INT-OPEN-012 / phase rates/axes/boundaries | PHASECORR001–005; P2§11; vinf/vLRの尺度共有、rres/η/collapse境界が未定 | INT-CLM-019, INT-CLM-054, INT-CLM-073, INT-CLM-081, INT-CLM-082, INT-CLM-083, INT-CLM-084 | INT-U-205, INT-U-206, INT-U-207 | DOWNGRADE/SPLIT; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-013 | INT-OPEN-013 / Σ発達度・clinical boundary | PHASECORR006; P2§1,8,13,A; Σ量化はfuture。clinical指標を本監査で作らない | INT-CLM-020, INT-CLM-054, INT-CLM-073, INT-CLM-081, INT-CLM-089, INT-CLM-095 | INT-U-208 | DOWNGRADE/SPLIT/KEEP; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-014 | INT-OPEN-014 / 認知内容とgraph組合せ | BRANCHCORR001–008; P1§7; 命題/理由からV/E/b/dへの抽出なし | INT-CLM-017, INT-CLM-018, INT-CLM-019, INT-CLM-020, INT-CLM-056 | INT-U-209 | SPLIT/REVISE/DOWNGRADE; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-015 | INT-OPEN-015 / Physarum固有mapping | BIOCORR001–005; P1§4–5; P2§5; 外部文献の生物量とInt変数の独立mapping未実行 | INT-CLM-011, INT-CLM-012, INT-CLM-013, INT-CLM-034, INT-CLM-047, INT-CLM-061 | INT-U-210 | KEEP/DOWNGRADE/SPLIT/REVISE; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-016 | INT-OPEN-016 / Transformer profile/stop provenance | AICORR001–012; P1§5; P2§5,11; 対象モデル・trace・self/external stopの分類なし | INT-CLM-013, INT-CLM-023, INT-CLM-034, INT-CLM-047, INT-CLM-061, INT-CLM-084, INT-CLM-094 | INT-U-211 | SPLIT/DOWNGRADE/REVISE/KEEP; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-017 | INT-OPEN-017 / 社会的record/consensus | SOCCORR005–006/008; P2§9; node・受容block・制度とLEの対応判定未定 | INT-CLM-024, INT-CLM-027, INT-CLM-064, INT-CLM-066, INT-CLM-067, INT-CLM-074, INT-CLM-079 | INT-U-212 | SPLIT/REVISE/KEEP; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-018 | INT-OPEN-018 / 歴史形態・維持/改訂 | HISTCORR001–006; P2§6–9; 史料/corpus/selection/comparatorなし。形態分類≠歴史法則 | INT-CLM-038, INT-CLM-067, INT-CLM-068, INT-CLM-069, INT-CLM-070, INT-CLM-071, INT-CLM-072, INT-CLM-095 | INT-U-213 | DOWNGRADE/SPLIT/KEEP; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-019 | INT-OPEN-019 / 社会cost・正統性・創造帰属 | SOCCORR007/010–012; P2§7,9; cost単位、正統性/創造の独立criterionなし | INT-CLM-068, INT-CLM-070, INT-CLM-075, INT-CLM-076, INT-CLM-077 | INT-U-214 | DOWNGRADE/SPLIT; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-020 | INT-OPEN-020 / Gettier case独立分類 | GETTIERCORR001–006; P1§6; P2§10; theory再記述から独立したC/LE/case分類なし | INT-CLM-003, INT-CLM-015, INT-CLM-016, INT-CLM-078, INT-CLM-079 | INT-U-215 | KEEP/SPLIT/DOWNGRADE; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-021 | INT-OPEN-021 / 一般・sapiens・collective知性criterion | GENCORR001–006; P1§3,5; P2§5,12; profile命名と必要十分観測基準が未分離 | INT-CLM-001, INT-CLM-002, INT-CLM-004, INT-CLM-005, INT-CLM-013, INT-CLM-030, INT-CLM-033, INT-CLM-037, INT-CLM-039, INT-CLM-061, INT-CLM-083, INT-CLM-084, INT-CLM-085, INT-CLM-086, INT-CLM-087 | INT-U-216 | KEEP/SPLIT/DOWNGRADE/OPEN; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-022 | INT-OPEN-022 / phenomenal endpointとscope | PHENCORR001–006; P1§9; P2§7,13; free inference/責任の機能語≠主観報告。futurehandoff維持 | INT-CLM-014, INT-CLM-020, INT-CLM-028, INT-CLM-031, INT-CLM-032, INT-CLM-062, INT-CLM-087, INT-CLM-095 | INT-U-217 | KEEP/DOWNGRADE/REVISE/SPLIT; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-023 | INT-OPEN-023 / cross-domain型・尺度・時間対応 | XCORR001–021; XBRIDGE001–042; P2B–E; homologyを越すtyped/implemented/validatedbridge未所在 | INT-CLM-007, INT-CLM-009, INT-CLM-010, INT-CLM-011, INT-CLM-012, INT-CLM-013, INT-CLM-014, INT-CLM-025, INT-CLM-026, INT-CLM-029, INT-CLM-030, INT-CLM-031, INT-CLM-032, INT-CLM-034, INT-CLM-036, INT-CLM-039, INT-CLM-041, INT-CLM-042, INT-CLM-044, INT-CLM-045, INT-CLM-046, INT-CLM-047, INT-CLM-050, INT-CLM-053, INT-CLM-062, INT-CLM-065, INT-CLM-085, INT-CLM-090, INT-CLM-091, INT-CLM-093 | INT-U-217 | REVISE/KEEP/DOWNGRADE/SPLIT/OPEN; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |
| INT-OPEN06-024 | INT-OPEN-024 / prediction/failure routeの実行境界 | PRED05001–020; FALS05001–016; P2§11,13; source候補はあるがprotocol/threshold/comparator/実行結果なし | INT-CLM-035, INT-CLM-088, INT-CLM-089, INT-CLM-092, INT-CLM-093, INT-CLM-094 | INT-U-218 | KEEP/SPLIT; scope表示・成分分離のみ。missing map/formal/evidenceは未供給 | YES |

## 22. Uncertainty clusters — navigation only

旧INT-U-001–218は一字も書き換えず全件保持。6clusterは重複する索引であり、個数を合算してuncertainty総数にしない。union=218、解決/削除0。新規219–236は次節ではなく§26に別記する。

| UCLUSTER | category | old IDs (INT-U-prefix) | members | navigation / boundary |
|---|---|---|---|---|
| INT-UCLUSTER-001 | authority/documentary | 001–012,023,026,028–029,032–042,090–092,177,187 | 32 | EN/JA primary・再掲・Master・図/PDF/翻訳status。内容選択が要るものはauthor decision |
| INT-UCLUSTER-002 | formal/signature | 013–016,018–019,024,027,030,044,049–094,176 | 57 | 同記号・domain・theorem premise・operator・図式と式の違い。proof監査へ越境しない |
| INT-UCLUSTER-003 | role/definition | 004–005,008–009,017,020–022,025,031,039–040,043,046–048,095–130,186 | 53 | local definition/役割/一般・sapiensの分離。sourceのnative layer番号と監査layerを混ぜない |
| INT-UCLUSTER-004 | circularity | 015,043,048,131–158 | 31 | C0–C8/独立criterion/backedge。RETAINを候補だけでresolveしない |
| INT-UCLUSTER-005 | evidence | 041–042,159–188 | 32 | support/gap/burden/citation provenance。YESはtrueでない |
| INT-UCLUSTER-006 | correspondence/operationalization | 045,060,069,083–089,093–094,189–218 | 42 | COR/OP/X・observable/候補metric/独立endpoint。新しい推定規則を作らない |

## 23. Provisional counts / denominators

| ledger | denominator | primary counts |
|---|---|---|
| claim candidates | 95 claims / each exactly once | {"KEEP":24,"SPLIT":41,"REVISE":8,"DOWNGRADE":20,"OPEN":2} |
| wording classes | 62 prior strong-language families | {"MODEL-LOCAL":15,"PROPOSED":8,"ASSERTIVE":1,"CONDITIONAL":7,"HYPOTHESIZED":14,"STRUCTURAL ANALOGY":9,"NEGATIVE SCOPE":1,"CORRESPONDENCE":6,"FUTURE":1} |
| equation planning | 63 EQF | {"TYPING CLARIFICATION NEEDED":13,"PROSE-SCOPE ONLY":22,"NO CHANGE":8,"FORMAL ASSUMPTION REQUIRED":13,"POSSIBLE EQUATION CHANGE":3,"AUTHORITY RESOLUTION REQUIRED":4} |
| figure planning | 14 families; secondary guards excluded | {"NO CHANGE":3,"RELABEL":5,"CAPTION GUARD":4,"HOLD / OPEN":2} |
| language planning | 36 FVAR | {"strengthen guard":9,"no action":4,"preserve language-specific difference":10,"synchronize":1,"resolve authority first":8,"downgrade JA strength":4} |
| homology synthesis | 21 HOMO | {"KEEP AS LEXICAL":1,"KEEP AS ROLE ANALOGY":12,"DOWNGRADE FROM FORMAL":3,"SPLIT IDENTITY/ANALOGY":5} |
| split plan | 41 parent claims | 41 conceptual child plans; children not new primary families |
| research routes | 24 | 24 YES / 0 consolidation / 0 closure |
| uncertainty | 218 + 18 =236 | old IDs preserved; new219–236 |

これらはCANDIDATES ONLY / NOT FROZEN。support YES25/PARTIAL64/NO3/UNRESOLVED3とcandidate数は独立であり、不一致は計数誤りではない。SERIOUS全5RETAINを変更しない。

## 24. Source-section revision burden

全30unit = P1abstract+§1–10（11） / P2§0–13（14） / appendicesA–E（5）。EN/JAの各source pathを併記。burdenは将来のprose/scope/authority作業量であり、sourceの真偽や数学の成否ではない。HOLDはそのunitのformal/authority成分が実装待ちであることを示し、安全な限定scopeの整理まで禁止する意味ではない。

| SECREV | unit | EN / JA files | related major claims | burden | minimal direction |
|---|---|---|---|---|---|
| INT-SECREV-001 | P1 abstract | intelligence-part1/sections/abstract.tex / intelligence-part1/sections_ja/abstract_ja.tex | INT-CLM-001, INT-CLM-012 | HEAVY | KEEP/DOWNGRADE; summaryでbodyの分割を再結合しない。negative guardを保持 |
| INT-SECREV-002 | P1 §1 | intelligence-part1/sections/01_introduction.tex / intelligence-part1/sections_ja/01_introduction_ja.tex | INT-CLM-001, INT-CLM-009, INT-CLM-010, INT-CLM-012, INT-CLM-026, INT-CLM-031 | MODERATE | KEEP/DOWNGRADE/REVISE; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-003 | P1 §2 | intelligence-part1/sections/02_the_decomposition_perception_recognition_knowledge_and_intelligence.tex / intelligence-part1/sections_ja/02_the_decomposition_perception_recognition_knowledge_and_intelligence_ja.tex | INT-CLM-001, INT-CLM-002, INT-CLM-003, INT-CLM-004 | MODERATE | KEEP/SPLIT; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-004 | P1 §3 | intelligence-part1/sections/03_minimal_axioms_of_intelligence.tex / intelligence-part1/sections_ja/03_minimal_axioms_of_intelligence_ja.tex | INT-CLM-005, INT-CLM-006, INT-CLM-007, INT-CLM-008, INT-CLM-009 | HEAVY | SPLIT/KEEP/REVISE; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-005 | P1 §4 | intelligence-part1/sections/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver.tex / intelligence-part1/sections_ja/04_ifgt_as_vocabulary_with_lexical_correspondence_to_the_physarum_solver_ja.tex | INT-CLM-008, INT-CLM-010, INT-CLM-011, INT-CLM-012 | HEAVY | SPLIT/KEEP/DOWNGRADE; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-006 | P1 §5 | intelligence-part1/sections/05_cross_domain_instantiation_slime_mold_and_transformer.tex / intelligence-part1/sections_ja/05_cross_domain_instantiation_slime_mold_and_transformer_ja.tex | INT-CLM-012, INT-CLM-013, INT-CLM-014 | HEAVY | DOWNGRADE/SPLIT/KEEP; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-007 | P1 §6 | intelligence-part1/sections/06_the_gettier_problem_as_a_structural_diagnostic.tex / intelligence-part1/sections_ja/06_the_gettier_problem_as_a_structural_diagnostic_ja.tex | INT-CLM-003, INT-CLM-015, INT-CLM-016 | HEAVY | KEEP/SPLIT/DOWNGRADE; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-008 | P1 §7 | intelligence-part1/sections/07_the_dynamical_instability_of_accumulated_correctness.tex / intelligence-part1/sections_ja/07_the_dynamical_instability_of_accumulated_correctness_ja.tex | INT-CLM-017, INT-CLM-018, INT-CLM-019, INT-CLM-020 | HEAVY | SPLIT/REVISE/DOWNGRADE; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-009 | P1 §8 | intelligence-part1/sections/08_the_non_closure_of_individual_intelligence.tex / intelligence-part1/sections_ja/08_the_non_closure_of_individual_intelligence_ja.tex | INT-CLM-021, INT-CLM-022, INT-CLM-023, INT-CLM-024 | HEAVY | SPLIT/DOWNGRADE; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-010 | P1 §9 | intelligence-part1/sections/09_the_differential_horizon_of_intelligence.tex / intelligence-part1/sections_ja/09_the_differential_horizon_of_intelligence_ja.tex | INT-CLM-024, INT-CLM-025, INT-CLM-026, INT-CLM-027, INT-CLM-028, INT-CLM-029, INT-CLM-030, INT-CLM-031, INT-CLM-032 | HEAVY | SPLIT/REVISE/KEEP/DOWNGRADE; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-011 | P1 §10 | intelligence-part1/sections/10_summary_convergence_and_outlook.tex / intelligence-part1/sections_ja/10_summary_convergence_and_outlook_ja.tex | INT-CLM-005, INT-CLM-012, INT-CLM-033, INT-CLM-034, INT-CLM-035 | HEAVY | SPLIT/DOWNGRADE/KEEP; summaryでbodyの分割を再結合しない。negative guardを保持 |
| INT-SECREV-012 | P2 §0 | intelligence-part2/sections/00_introduction.tex / intelligence-part2/sections/00_introduction_ja.tex | INT-CLM-036, INT-CLM-037, INT-CLM-038, INT-CLM-039, INT-CLM-087, INT-CLM-088, INT-CLM-095 | HEAVY | DOWNGRADE/SPLIT/OPEN/KEEP; summaryでbodyの分割を再結合しない。negative guardを保持 |
| INT-SECREV-013 | P2 §1 | intelligence-part2/sections/01_preliminaries.tex / intelligence-part2/sections/01_preliminaries_ja.tex | INT-CLM-040, INT-CLM-041, INT-CLM-042, INT-CLM-043, INT-CLM-044, INT-CLM-045 | HEAVY | KEEP/REVISE/SPLIT; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-014 | P2 §2 | intelligence-part2/sections/02_inference_operator.tex / intelligence-part2/sections/02_inference_operator_ja.tex | INT-CLM-043, INT-CLM-046, INT-CLM-047, INT-CLM-048, INT-CLM-049, INT-CLM-050 | HEAVY | SPLIT/REVISE/DOWNGRADE; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-015 | P2 §3 | intelligence-part2/sections/03_nonclosure_theorem.tex / intelligence-part2/sections/03_nonclosure_theorem_ja.tex | INT-CLM-042, INT-CLM-051, INT-CLM-052, INT-CLM-053, INT-CLM-054 | HEAVY | SPLIT/REVISE/DOWNGRADE; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-016 | P2 §4 | intelligence-part2/sections/04_response_channels.tex / intelligence-part2/sections/04_response_channels_ja.tex | INT-CLM-055, INT-CLM-056, INT-CLM-057 | MODERATE | KEEP/SPLIT; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-017 | P2 §5 | intelligence-part2/sections/05_emergent_stopping_layer.tex / intelligence-part2/sections/05_emergent_stopping_layer_ja.tex | INT-CLM-037, INT-CLM-044, INT-CLM-045, INT-CLM-047, INT-CLM-049, INT-CLM-057, INT-CLM-058, INT-CLM-059, INT-CLM-060, INT-CLM-061, INT-CLM-062, INT-CLM-063, INT-CLM-064, INT-CLM-065, INT-CLM-066, INT-CLM-086, INT-CLM-087 | HEAVY | SPLIT/KEEP/REVISE/DOWNGRADE; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-018 | P2 §6 | intelligence-part2/sections/06_animism.tex / intelligence-part2/sections/06_animism_ja.tex | INT-CLM-067, INT-CLM-068 | HEAVY | SPLIT/DOWNGRADE; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-019 | P2 §7 | intelligence-part2/sections/07_god.tex / intelligence-part2/sections/07_god_ja.tex | INT-CLM-069, INT-CLM-070 | HEAVY | SPLIT; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-020 | P2 §8 | intelligence-part2/sections/08_religion.tex / intelligence-part2/sections/08_religion_ja.tex | INT-CLM-071, INT-CLM-072, INT-CLM-073, INT-CLM-095 | HEAVY | SPLIT/DOWNGRADE/KEEP; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-021 | P2 §9 | intelligence-part2/sections/09_social_blockchain.tex / intelligence-part2/sections/09_social_blockchain_ja.tex | INT-CLM-072, INT-CLM-074, INT-CLM-075, INT-CLM-076, INT-CLM-077 | HEAVY | SPLIT/KEEP/DOWNGRADE; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-022 | P2 §10 | intelligence-part2/sections/10_gettier_problem.tex / intelligence-part2/sections/10_gettier_problem_ja.tex | INT-CLM-040, INT-CLM-066, INT-CLM-078, INT-CLM-079, INT-CLM-080 | HEAVY | KEEP/REVISE/SPLIT; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-023 | P2 §11 | intelligence-part2/sections/11_instability_region.tex / intelligence-part2/sections/11_instability_region_ja.tex | INT-CLM-081, INT-CLM-082, INT-CLM-083, INT-CLM-084 | HEAVY | SPLIT/DOWNGRADE; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-024 | P2 §12 | intelligence-part2/sections/12_constructive_clauses.tex / intelligence-part2/sections/12_constructive_clauses_ja.tex | INT-CLM-037, INT-CLM-085, INT-CLM-086, INT-CLM-087 | HEAVY | SPLIT; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-025 | P2 §13 | intelligence-part2/sections/13_conclusion.tex / intelligence-part2/sections/13_conclusion_ja.tex | INT-CLM-088, INT-CLM-089, INT-CLM-092 | HEAVY | KEEP; summaryでbodyの分割を再結合しない。negative guardを保持 |
| INT-SECREV-026 | P2 A | intelligence-part2/appendices/appendix_a_master_table.tex / intelligence-part2/appendices/appendix_a_master_table_ja.tex | INT-CLM-041, INT-CLM-048, INT-CLM-081, INT-CLM-090 | HOLD | REVISE/SPLIT/OPEN; 再掲/局所極小等のauthority採用を先に決定、式は保持 |
| INT-SECREV-027 | P2 B | intelligence-part2/appendices/appendix_b_homology.tex / intelligence-part2/appendices/appendix_b_homology_ja.tex | INT-CLM-045, INT-CLM-050, INT-CLM-062, INT-CLM-091 | MODERATE | KEEP/DOWNGRADE/SPLIT; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-028 | P2 C | intelligence-part2/appendices/appendix_c_part1_mapping.tex / intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex | INT-CLM-039, INT-CLM-065, INT-CLM-092 | LIGHT | OPEN/DOWNGRADE/KEEP; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-029 | P2 D | intelligence-part2/appendices/appendix_d_optional_notes.tex / intelligence-part2/appendices/appendix_d_optional_notes_ja.tex | INT-CLM-051, INT-CLM-052, INT-CLM-053, INT-CLM-054, INT-CLM-064, INT-CLM-078, INT-CLM-080, INT-CLM-094, INT-CLM-095 | HEAVY | REVISE/SPLIT/DOWNGRADE/KEEP; local definition/弱い役割比較を保持し、強い帰結・一般化を分離 |
| INT-SECREV-030 | P2 E | intelligence-part2/appendices/appendix_e_emergence_homology.tex / intelligence-part2/appendices/appendix_e_emergence_homology_ja.tex | INT-CLM-044, INT-CLM-045, INT-CLM-059, INT-CLM-089, INT-CLM-093 | HOLD | SPLIT/KEEP; 再掲/局所極小等のauthority採用を先に決定、式は保持 |

NONE0 / LIGHT1 / MODERATE4 / HEAVY23 / HOLD2 =30。P2EN entryにあるabstract相当とJA側placeholderの非対称はentry authorityの問題としてAUTHCONFLICT/LANGREVで残し、翻訳や新abstractを自動生成しない。P1abstract・§10、P2§0/12/13、caption/READMEはbody強度を復元しやすい箇所として最終gateに含める。

## 25. Questions Phase07 must independently re-check

Phase06の判断を採用前提にせずcurrent P1/P2の各言語source、Phase00 locator、Phase01signature/premise、Phase02role、Phase03C-class、Phase04support/burden、Phase05COR/OP/Xを再照合する。

- 全95候補に対しauthority優先・最小改訂を再判断し、同じ結果でも理由を再確認する。
- KEEP24のlocal/negative/future scope、REVISE066のYESとの両立、DOWNGRADE20の残存する独立内容を確認する。
- SPLIT41の全child成分とsummary/figureの再結合リスクを確認する。子OPENをprimary OPENと混同しない。
- RETIRE0が適切か再確認する。弱い根拠やC8だけで削除しない。
- OPEN039/090とSPLIT093内authority holdを独立照合し、Masterのexact predecessorやfour-layer意図を好みで選ばない。
- SERIOUS001–005のweak/strong reading・独立criterion・explanatory backedgeを再点検する。Phase06候補ではresolveしない。
- 全63EQREV、特にpossible012/034/037とauthority025/036/041/048を再照合する。安全な変更開始NO / globalOPENを独立判断する。proof reviewを実施したとは扱わない。
- AUTHCONFLICT001–028、全36FVAR、P1distributed JA/ENparallel、P2JAprimary/ENdraftを再確認する。
- 全14figuresのprimary actionとEN/JA variant差を確認する。CAPTION GUARDだけでformal identityの問題を解いたとしない。
- Phase03 vicious circularity NO / global unfalsifiability NOを、支持・真理の判定に変換せず再確認する。
- Phase04support95/strong62/gaps31とFE2/CE2/SE2/BE3-background/PE1/XE2/PRE2/OE0を保持して独立点検する。
- Phase05COR3 max/phenCOR1/X3/OP2、artifacts0/tested0/validated0、OPEN routes24を再確認する。
- 218旧uncertaintyと18新規dependencyを保持し、research OPENとaudit freeze blockerを別に扱う。
- final dispositionのfreezeやaudit closureを行うならPhase07に明記し、source/equation/distribution実装へ自動的に進まない。

## 26. New synthesis / revision-dependency uncertainties

新規INT-U-219–236の18件。formal proofや新実験の問題を新規設計して追加するのでなく、既存結果からsafe implementationへ進む依存条件を記す。旧INT-U-001–218は全件不変、総数236。全新規statusはOPEN。

| uncertainty | category | parent / dependency | unresolved synthesis question | status |
|---|---|---|---|---|
| INT-U-219 | KEEP stress / summary adjacency | KEEP24とREVISE066 | 局所YES/guardが近接する強い説明へ戻らないための適用境界をPhase07で再確認する | OPEN |
| INT-U-220 | claim granularity | SPLIT41 | 親familyのweak/strong成分をどこまで独立claimとして分けるか。新理論を加えず独立burdenを保てるか | OPEN |
| INT-U-221 | language authority gate | INT-U-001/002/003; LANGREV | P1 EN primary未決/P2 JA primaryの下で将来同期の承認順序が未決 | OPEN |
| INT-U-222 | conditional theorem retention | REV051; EQREV026–028 | proof未監査のまま保持する条件付きstatementと、proof reviewが必要なassertive部分の境界 | OPEN |
| INT-U-223 | stopping split implementation | SERREV001; REV021/052/054 | formal stop模型と認知stopの子claimがsummaryで再結合されない最小分離単位 | OPEN |
| INT-U-224 | LE functional naming | SERREV002; REV037/059/060 | 機能定義を残して生成説明を弱化した後も、存在の独立burdenを明確に保持できるか | OPEN |
| INT-U-225 | Phi identity prose/math interaction | SERREV003; EQREV034 | 二視点proseと印刷された≡を両立させるformal意図の選択が未決 | OPEN |
| INT-U-226 | mu equivalence prose/math interaction | SERREV004; EQREV037 | 対応へ弱化したproseと↔の採用範囲をどう確定するか、formal review前に選べない | OPEN |
| INT-U-227 | Cmax interpretation boundary | REV042/053; EQREV017–019 | barrier/不変領域/究極理解を分ける際の既存式の適用範囲決定が必要 | OPEN |
| INT-U-228 | graph equation trigger | REV017/018; EQREV012/014/015 | proposition→field評価とgraph条件をproseだけで扱える範囲か、式変更triggerか未決 | OPEN |
| INT-U-229 | F version selection | REV046/051; EQREV025/048 | single/set-valued alternativeとstrict-Jの採用版を選ぶauthority/formal decisionが未決 | OPEN |
| INT-U-230 | general versus sapiens clauses | REV085/086; MAPCONFLICT014 | N1/R4、六/七条件の最小source修正単位とgeneral scope決定が未決 | OPEN |
| INT-U-231 | Master hold release | REV090; INT-U-010/090/187 | exact predecessor不明のままdocumentary disclaimerで進める範囲とholdすべき継承内容 | OPEN |
| INT-U-232 | appendix functional tense | REV093; EQREV041 | 比較は保持してlocalminimumをholdする分割がbody/appendix両方で成立するか | OPEN |
| INT-U-233 | figure system boundary | FIGREV009 | Transformerを個体profile/whole-systemのどちらとして描く意図か、node/label変更前に未決 | OPEN |
| INT-U-234 | wording/figure guard propagation | WORDING001–062; FIGREV001–014 | 弱化したbodyをcaption/図/summaryで再強化しない依存関係の最終確認 | OPEN |
| INT-U-235 | research OPEN versus implementation OPEN | OPEN06全24; OPEN-CAND2 | 研究route24を残しつつprose実装を進められる範囲と、author/formalholdが必要な箇所 | OPEN |
| INT-U-236 | Phase07 closure gate | REV全95; authority / ceiling preservation | 候補を独立再監査する際、残るresearch OPENと監査上のfreeze blockerを分けられるか | OPEN |

## 27. Validation / task-start preservation

Task-start snapshot: `${TEMP_EVIDENCE_ROOT}/int_phase06.qIXFss/baseline.json`（repository全1496 files、.git除外、ignored/untrackedを含む）。
Manifest SHA-256: `1a8f5a4b9bb9e8ba40b945c39ad1db34759ac6a96d8124068881637e63ef9dbf`。
Snapshotは本phaseの最初に作成し、既存dirty worktreeを基準とした。過去phaseのgit差分を本phaseの変更と誤認しない。

| protected authority | task-start SHA-256 |
|---|---|
| Phase00 | ffb891b9039a71a2173574652f72776a307be6618070a74f2fcc64bc0a312d64 |
| Phase01 | ecb64a12dd4d5e4defab076c2118cc6a6f9f842ab278f03c975ce9f082891d14 |
| Phase02 | aee8d40a4241869918d6724305a3c94dc667ec2e352ed496614439d775148318 |
| Phase03 | 1596b90ca99baeeb19cf5e6fb655f5f5a4c925f63b551de33c8b0b4bfac7c05d |
| Phase04 | 9255a79991bb0073e9384ddc2ea6f4a6e051a9179563736b0cf411cc9a7697ee |
| Phase05 | 22acca2adae611ddd0f13cb5692fb4dfedeb56438a5da41bc1cd86c7f8e27060 |
| audit README (変更許可対象) | 2d52a36aaa544ec5241f8580722a205bf744268d32d56f2073a58c35da69a11c |

実行結果: PASS。

| validation gate | result |
|---|---|
| primary REV / CLM | 95/95、各1primary、連番・重複なし、合計95 |
| candidate ledgers | KEEP24 / REVISE8 / DOWNGRADE20 / SPLIT41 / RETIRE0 / OPEN2 |
| split plan | 全41parentにchild plan、primary SPLIT集合と完全一致 |
| inherited support / C-class | 全95行がPhase04 support / Phase03 C-classと一致、support25/64/3/3不変 |
| wording / homology / research routes | 62/62、21/21、24/24。旧family IDへの一対一参照、全route still OPEN=YES |
| equation / figure / language / SERIOUS | 63/63、14/14、36/36、5/5。変更計画のみ、SERIOUS全5RETAIN |
| section / order / uncertainty clusters | 30 source units / 12 order entries / 6 overlapping clusters（旧218のunion） |
| new uncertainties | INT-U-219–236、18 unique IDs、総数236。旧record不変 |
| Markdown table / text | 全tableのcolumn数一致、欠損文字U+FFFDなし |
| repository snapshot | 1496→1497 files。追加は本record1、既存変更はaudit README1、削除0 |
| protected bytes | 既存1495 filesのSHA-256不変。Phase00–05全6records、66 Intelligence TeX、数式/inline/symbol、figures、PDFs、BibTeX、他branchを含む |
| prior history | audit READMEのPhase00–05記述保持、現在statusとPhase06節のみ追加更新 |
| no unauthorized work | source/equation/figure改訂0、PDF build0、simulation0、web0、new theory/bridge0、proof validity/final freezeなし |
| git diff --check | PASS（exit 0） |
| git status --short | 250行、task-startと完全一致。既存dirty/untracked状態を保持 |

検証用metadata script/logはrepository外の `${TEMP_EVIDENCE_ROOT}/int_phase06.qIXFss/validate.py`、`validation.json`、`git_status_after.txt`。これらは文書ID/ファイルhash検査で、理論simulationや新しいmetricではない。audit directoryが開始時からuntrackedであるため、Git statusの行数だけでは新規recordを識別できない。全ファイルsnapshot差分により許可された2file境界を検証した。commit/pushは実施していない。

## 28. Stop boundary

Phase06はrevision candidate synthesisとして完了。候補はPROVISIONAL / NOT FROZEN、final dispositionsはNOT ASSIGNED。SERIOUS5はRETAIN、OPEN routes24はOPEN。Phase07へ進まず停止する。

source prose・equations・symbols・figures・JA/EN translations・PDFs・BibTeX・upstream/downstream sources・Phase00–05 recordsを変更しない。新しい型・空間・metric・estimator・閾値・experiment・operational map・proof・theory・bridgeを追加していない。web/external research・simulation・PDF build・commit/pushを実行しない。
