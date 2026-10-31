# Post-audit implementation 23 — Bounded Source Migration: F / J Active-Historical Split

## 1. Status / authority / execution boundary

```text
Post-audit implementation 23: COMPLETE — IMPLEMENTATION SELF-CHECK ONLY
Result: SOURCE MIGRATION IMPLEMENTED — PENDING INDEPENDENT AUDIT
Migration accepted: NO
EQF025 / EQF047 / EQF048: IMPLEMENTED within impl22 authorization
EQF026 new predicate: NOT INSERTED
EQF027 / theorem3.1 / new-J proof migration: HOLD / UNCHANGED / NO
Modified TeX: 28 (all within the maximum allowlist)
Old math: display98 / inline2199 preserved, byte mismatches0
New math: display6 / inline0 (descriptive ports only)
PS21-001–008: PRESERVED 8/8
Figures / captions / P1 / PDF / BibTeX: UNCHANGED
Independent migration acceptance / build / distribution: NOT PERFORMED
```

2026-09-23。[impl22](impl22_independent_authorization_review_amended_migration_packet_v0.1_ja.md) の明示許可に従い、[impl21](impl21_migration_design_amendment_source_dependency_gaps_v0.1_ja.md) U21 canonical packetを一つのsource transactionとして実装した。[impl20](impl20_independent_migration_design_review_f_j_active_historical_split_v0.1_ja.md) の発見履歴と[impl19](impl19_equation_migration_design_packet_f_j_active_historical_split_v0.1_ja.md) のPB19は保持する。signature authorityは[impl18](impl18_selected_formal_contract_adoption_and_type_scope_acceptance_v0.1_ja.md)、候補履歴は[impl17](impl17_selected_formal_object_signature_specification_v0.1_ja.md)、意味・言語authorityは[impl16](impl16_author_clarification_and_formal_specification_contract_v0.1_ja.md)。[impl11](impl11_proof_theorem_review_v0.1_ja.md) のoldkernel/proof負担、[impl10](impl10_formal_equation_review_v0.1_ja.md) の形式負担、[Phase07](07_final_audit_and_frozen_dispositions_v1.0_ja.md) の凍結を変更しない。

保存: KEEP23 / REVISE8 / DOWNGRADE21 / SPLIT41 / RETIRE0 / OPEN2 =95 FROZEN。SERIOUS001–005 all RETAIN、research OPEN24/24、uncertainties236、blockers13 global status不変。Evidence FE2/CE2/SE2/BE3 citation-background-only/PE1/XE2/PRE2/OE0、correspondence formal/cognitive/behavioral/biological/social/AI COR3、phenomenal COR1、cross-domain X3、OP2、operational maps/data/sims/tested/validated=0不変。impl08 PASS/CLOSEDは旧prose系列の受入履歴であり、今回diffの独立受入を意味しない。impl18 ACCEPTED WITH PROOF HOLD、impl22 AUTHORIZED WITH HOLDSはproof/empirical/figure/build受入へ昇格しない。

今回のself-checkは実装担当による再読・機械検証であり、独立acceptance auditではない。coreだけ先にacceptedとせず、historical enclosure、proof外側境界、active ports、全列挙consumer、table、figure body guardをまとめて実装した。中間状態のcommit・build・配布はない。

## 2. Preflight / protected-span verification

編集前に `${TEMP_EVIDENCE_ROOT}/int_impl23.l32RV7/baseline.json` を作成。SHA-256 `06d39d80de2b487d3dc15a55276eb36a13092f695a2aafcc32b76a746ecf9f2e`、1520 regular files（`.git`内部以外、ignored/untracked含む）。Intelligence66TeXのtask-start bytesも格納し、所有diffだけのrollbackに備えた。git status全文は同directoryの `task_start_git_status.txt` とbaselineに保存。298行（M289 / ??9）の既存dirtyworktreeを維持する。

impl22 baselineと66TeXを比較しdrift0。literal paragraphと前後contextで28fileの対象を解決した。行番号は検索補助に限定し、反復するfigure beginはincludegraphics・前後文脈で区別した。J02の四性質導入は40、LF導入62・説明71、J03小結は270/280/282という実際の文字列を、許可範囲内で解決した。source drift・曖昧anchor・design選択を要する差はない。保護hashを更新せず、以下が一致した後にsource patchを適用した。

| Protected span | Baseline locator → current locator | Raw SHA-256 (inclusive LF bytes) | Preflight / after |
|---|---|---|---|
| PS21-001 | E03:17–56 →19–58 | `b8e86d7a7ed2f41deb91a6dfc50081122f561c79cebf397e3a15c684773144cb` | MATCH / PRESERVED |
| PS21-002 | J03:23–101 →25–103 | `7e7065d95db537b922cb5b80e503af107b2bb185cd0c38d8f35c383387e7628a` | MATCH / PRESERVED |
| PS21-003 | DJ:13–43 →15–45 | `68b731204c16ff5e7ce4b2f99a2ba345d780f86c92f9ceb6a44748d93ab26553` | MATCH / PRESERVED |
| PS21-004 | E01:26–28 →26–28 | `990686f859ca6a3b9644805a02fd6a90d6b3ee70bddaad134f65f67200c62f6b` | MATCH / PRESERVED |
| PS21-005 | E05:21–27 →25–31 | `aa28aa7e4e560e908955d291c0b04f3f373f98489798a356f94c1bb15885893b` | MATCH / PRESERVED |
| PS21-006 | J05:24–30 →28–34 | `bcfd14301dbd469f1c39da9ba70f5f4055057e4d7d4e46812044bd8baed4f1e2` | MATCH / PRESERVED |
| PS21-007 | E05:92–94 →98–100 | `ccc9ca9dff3426ed462f320935195f12254dbc583faf9ac7e85dfcad5fedb1a6` | MATCH / PRESERVED |
| PS21-008 | J05:267–269 →273–275 | `a194358a834ec2df4ef6f4bef40c5bdf27ef36b1ea1cb27ce2879445325a8011` | MATCH / PRESERVED |

旧math・figure環境・参照等の検査をpatch生成前にも適用し、実ファイル適用後に再実行した。補助的なbrace検査は既存P1のTeX構文を単純parserで扱えないため、絶対判定でなくbaselineとの差を検査する方式に訂正した。sourceや保護hashの変更で検査を通したものではない。保護内容の実際の破損・rollback発動は0。

## 3. Modified-file allowlist / exact change record

以下は実際に変更した28file全部。E/J aliasは各rowのfileを指す。pathは `intelligence-part2/` 相対、sections/appendicesを省略しない。旧locatorはtask-start、**exact before/afterは§15のtask-owned unified diff**に全件収録した。diffはHEAD比較ではなくtask-start bytes比較なので、既存ユーザー変更を混入しない。各rowのold mathはすべてbyte-identical・同順序、新mathは記載の2file以外0。

| File / alias | U21 owners | Modification reason / bounded fragments | New math / old math |
|---|---|---|---|
| `main.tex` / mainEN | 009 | abstract18のnoFPをhistorical local-state modelへ帰属 | 0 / KEEP |
| `sections/00_introduction.tex` / E00 | 009 | 9,38 oldmodelのLF/strict参照 | 0 / KEEP |
| `sections/00_introduction_ja.tex` / J00 | 009,012 | 29外側schema guard、137/167/203/271帰属 | 0 / KEEP |
| `sections/01_preliminaries.tex` / E01 | 001,009 | 25導入historical、28後guard、44oldtheorem帰属 | 0 / KEEP |
| `sections/01_preliminaries_ja.tex` / J01 | 009,023 | 163trajectory、175shared tag一回、200/369旧模型参照 | 0 / KEEP |
| `sections/02_inference_operator.tex` / E02 | 007,015,016,018,019,021,022 | scope、core/adapter、別position、oldscalar/set history、LF/S帰属 | display3 / KEEP |
| `sections/02_inference_operator_ja.tex` / J02 | 003,007,015,017,020,021,022,024 | 同契約ports、旧F四性質/LF/Int比較、小結223–225/234 | display3 / KEEP |
| `sections/03_nonclosure_theorem.tex` / E03 | 003,008 | 7帰属、FIG006前guard、60/62/66。proof17–56非変更 | 0 / KEEP |
| `sections/03_nonclosure_theorem_ja.tex` / J03 | 003,008 | 8帰属、図前guard、270/280/282。premises/corollaries非変更 | 0 / KEEP |
| `sections/04_response_channels.tex` / E04 | 010 | 7/35/37/43 oldregress/noFP帰属 | 0 / KEEP |
| `sections/04_response_channels_ja.tex` / J04 | 010 | 70/112旧模型scope。条件・論証内容は保持 | 0 / KEEP |
| `sections/05_emergent_stopping_layer.tex` / E05 | 005,010,012 | 11章帰属/31、FIG009直前、E block外側 | 0 / KEEP |
| `sections/05_emergent_stopping_layer_ja.tex` / J05 | 005,010,012 | 12章帰属/38/44、FIG009直前、E block外側 | 0 / KEEP |
| `sections/07_god_ja.tex` / J07 | 010 | 61系3.2をoldmodelへ帰属 | 0 / KEEP |
| `sections/08_religion_ja.tex` / J08 | 010 | 40social/regressの旧前提scope | 0 / KEEP |
| `sections/10_gettier_problem_ja.tex` / J10 | 025,026 | 22oldscalarとnewport非同一、32/128旧引用 | 0 / KEEP |
| `sections/11_instability_region_ja.tex` / J11 | 026 | 90/173oldnoFP帰属、相図無変更 | 0 / KEEP |
| `sections/12_constructive_clauses.tex` / E12 | 026 | 11general-intelligence consumerの条件帰属 | 0 / KEEP |
| `sections/12_constructive_clauses_ja.tex` / J12 | 026 | 39旧局所模型の条件帰属 | 0 / KEEP |
| `sections/13_conclusion.tex` / E13 | 026 | 11結語のoldmodel帰属 | 0 / KEEP |
| `sections/13_conclusion_ja.tex` / J13 | 006,011,026 | 47/129旧引用、107heading/108verbatim quote外側、111旧提案 | 0 / KEEP |
| `appendices/appendix_a_master_table.tex` / AE | 004 | table前outerstatus、F21/LF22 proseのみ | 0 / KEEP |
| `appendices/appendix_a_master_table_ja.tex` / AJ | 004,012 | 5にshared outerstatus一回、F59/J60/LF61 attribution | 0 / KEEP |
| `appendices/appendix_b_homology.tex` / BE | 011 | 29Int noFPのhistorical conditional tag | 0 / KEEP |
| `appendices/appendix_b_homology_ja.tex` / BJ | 011,024 | 25/122/177のoldmodel帰属、Bio row無変更 | 0 / KEEP |
| `appendices/appendix_c_part1_mapping.tex` / CE | 011 | 11と後続の未実装editorial guard | 0 / KEEP |
| `appendices/appendix_c_part1_mapping_ja.tex` / CJ | 011 | 34table旧提案、78quoteの旧未実装帰属 | 0 / KEEP |
| `appendices/appendix_d_optional_notes_ja.tex` / DJ | 008 | 12外側guardのみ、13以降全文KEEP | 0 / KEEP |

main_ja.tex、E11、DE、P1、assets、caption Markdownは変更しない。JAにset-valued display/EN J rowを補う編集はない。原U19を追加実行せず、U21 shared ownerのAJ5とJ01:175は一度だけ実装した。

## 4. U21 execution table

| Unit | Execution / preservation result | Status |
|---|---|---|
| U21-001 | EN §1 historical schema導入・外側guard、PS004KEEP | IMPLEMENTED |
| U21-002 | theorem/proof3fragmentをraw保護 | PROTECTED / NO-EDIT |
| U21-003 | E03後段/J02小結/J03小結のみoldmodel帰属 | IMPLEMENTED |
| U21-004 | EN F/LF、JA F/J/LF rows、table外側scope | IMPLEMENTED |
| U21-005 | EN/JA FIG009直前body boundary | IMPLEMENTED |
| U21-006 | J13:107旧提案heading、108引用と外側guard、105KEEP | IMPLEMENTED |
| U21-007 | 先行slice/identityと事後uniquenessを016/017へ統合 | IMPLEMENTED AS CRITERIA |
| U21-008 | E03/J03/DJの外側oldmodel帰属、FIG006境界 | IMPLEMENTED |
| U21-009 | abstract/intro/prelimの直接consumer帰属 | IMPLEMENTED |
| U21-010 | response/LE章/social/regress旧モデル帰属 | IMPLEMENTED |
| U21-011 | homology/P1mapping/結語proposalのhistory tag | IMPLEMENTED |
| U21-012 | E block/JA intro schema/AJ shared outerstatus | IMPLEMENTED |
| U21-013 | assets/figure environments/captions/notes/workingMD | PROTECTED / NO-EDIT |
| U21-014 | P1/Bio F/flow J/J_C/非target署名 | PROTECTED / NO-EDIT |
| U21-015 | §2旧authority履歴とactive契約を分離 | IMPLEMENTED |
| U21-016 | EN realized coreとoptional adapter、旧state式可視 | IMPLEMENTED |
| U21-017 | JA同契約、旧state式可視 | IMPLEMENTED |
| U21-018 | EN oldscalar/strictのhistorical scope | IMPLEMENTED |
| U21-019 | EN set-valued歴史化、推薦voice変更、式KEEP | IMPLEMENTED |
| U21-020 | JA overview/四性質を旧模型へ帰属 | IMPLEMENTED |
| U21-021 | EN/JA別position partial port、新predicateなし | IMPLEMENTED |
| U21-022 | LF/S引用の旧模型帰属、定義・番号・式KEEP | IMPLEMENTED |
| U21-023 | JA旧trajectoryと一般record連接の区別 | IMPLEMENTED |
| U21-024 | Int/Bio比較のIntのみoldscope、Bio式KEEP | IMPLEMENTED |
| U21-025 | Gettier参照oldscalarJとpositionを分離 | IMPLEMENTED |
| U21-026 | phase/general/conclusionの旧条件参照 | IMPLEMENTED |
| U21-027 | 新EQF026挿入なし、EQF027/proof移行なし | HOLD / NO-EDIT |

22 edit units＋1criteria統合、3保護、1HOLD=27。全体の実装者self-check完了は独立受入ではない。

## 5. EQF025 migration result

| Component | Current implementation | Guard / residual |
|---|---|---|
| Realized core | E02:11–16/J02:16–21。before/afterはAcceptedRealizedRecord→Occurrence | actual successorをglobal future lawとしない。record基準の存在は実証ではない |
| Optional adapter | E02:18–23/J02:23–28、partial successor signature | matching record存在、canonical endpoints、一意after。複数afterならundefined、recordsはKEEP、selectorなし |
| Declared scope | window/context/rule-version/identity/eligibilityを結果と独立に宣言 | uniquenessの事後検査は可、strict/noFP後選択は不可 |
| Identity / iteration | StateView≠Occurrence、同viewの再訪可、alias規約明示 | record連接≠同一Fの冪。adapter反復には同slice/version/carrierと各段definedness |
| Old state model | E02:34以降/J02:39以降、元のstate式をその場に保存 | 新portへの置換でない、旧proofは旧model内 |

新記述は採用済みcontractの明示化に限る。future branchの完成集合、全履歴archive、state/context/ruleの同一視、fresh IDsによるnoFP、rule-plasticity法則を追加しない。

## 6. EQF047 / EQF048 results and hard holds

| Family | Implemented split | Preservation / not implemented |
|---|---|---|
| EQF047 | E02:25–30/J02:30–35に別position port。fixed Scope/EvaluationProfile、部分性、非単射の許容、同一評価carrier | oldscalarJは旧kernel/Master/Gettierに保持。positionは可用記憶・hardness・justification・truthでない。実数値継承・自動単調性なし |
| EQF048 | EN subsection Historical Branching Formulation、earlier/proposedという過去のvoice | 元の集合式可視。JAにdisplay非追加。候補集合をscalarJへ渡さず、lift/selector非導入 |
| EQF026 | 旧strict premise保持、新contractから分離 | 新strictBefore source predicateは0、active all-step lawなし |
| EQF027 | old proof/statement/heading/numberを全文保持、外側のhistory scopeのみ | 新J proof移行・theorem restatementなし。bookkeeping/non-tautology HOLD継続 |

## 7. Consumer migration table

| Consumer group | Implemented ownership | Preserved ceiling / self-check |
|---|---|---|
| Abstract / EN,JA intro | 009/012 | oldnoFPの帰属、schemaはhistory。universal stopping theoremでない |
| EN schema / JA trajectory | 001/023/009 | display可視、LF入力をrecord入力にしない、連接と冪を区別 |
| §2 properties / LF / S / summary | 015–024/003 | oldmodelの定義・番号・式KEEP、新portへの性質流入なし |
| §3 proof / later summaries | 008/002/003 | proof内0edit、oldstrict/fixedθ/A/admissible kernel限定、新prooftransferなし |
| §4 / §5 | 010/012 | historical conditional/regressとLE hypothesis分離、E型未解決 |
| Social / religion | 010 | analogyのまま、newF由来のsocial lawなし |
| Gettier | 025/026 | diagnostic、oldscalarJ参照、newposition evidenceでない |
| Phase / general intelligence | 026 | fixed-region結果をrule-changing/一般知性へ昇格しない |
| Conclusions / P1 proposal | 006/011/026 | 105guardKEEP、108の元文をverbatim quoteとして保存、P1未実装 |
| Master / homology / mapping / Appendix D | 004/011/024/008 | F/Jのみdocumentary scope、same role≠typed identity、v2.1 gap不変 |

列挙済みconsumerを旧模型に帰属させるbounded relabelであり、95claims全体の再cleanupは行わない。本文の他の未実装author directionsを勝手に採用せず、unrelated proseは保持した。

## 8. Figure body guards / E block boundary

| Object | New outer body location | Preserved content / status |
|---|---|---|
| FIG006 EN | E03:9 Historical local-model boundary、figureより前 | whole figure環境/caption/figurenote KEEP。oldscalarJ/fixed模型の図、新position証明でない |
| FIG006 JA | J03:12 旧局所模型の境界、figureより前 | 同じ境界、Cbarrier等は修理しない |
| FIG009 EN | E05:23 Historical architecture figure、FIG008後/009前 | PS005KEEP、新record/positionからLE生成・own-layer証明なし |
| FIG009 JA | J05:26 歴史的architecture図の境界 | PS006KEEP、system boundaryを図で決めない |
| FIG011 / FIG013 | 新guard/asset修理なし | 既存captionのidentity/HOLD・未較正status保持、修理/配布readyでない |
| E/F iterations EN | E05:95 outerstatus、旧91–95 blockはcurrent97–101でKEEP | activeadapter代入なし、Eの型未解決、非導出性/非計算可能性/large-k theoremなし |
| E/F iterations JA | J05:264 outerstatus、旧260–279 blockは266–285でKEEP | 小節末尾まで旧notation、E形式化なし |
| E in JA Master | AJ6 shared outerstatus一回 | E row/displayの内側非変更、旧iteration family保持 |

body共存guardを実装しただけで、stale図を受入済みとはしない。FIG009/011 repair readiness NO、build/distribution NO。

## 9. Old / new math preservation

| Category | Count / exact location | Verification |
|---|---|---|
| OLD display | 98 | byte-identical、file内相対順序同一 |
| OLD inline | 2199 | byte-identical、file内相対順序同一 |
| OLD mismatches | 0 | newport marker下の許可6displayのみ除外した全segment列をbaselineと比較 |
| NEW EN endpoints | E02:13–15、U016 | before/after: AcceptedRealizedRecord→Occurrence |
| NEW EN adapter | E02:20–22、U007/016 | realizedSuccessor[slice]: EligibleOccurrence ⇀ Occurrence |
| NEW EN position | E02:27–29、U021 | position: Occurrence ⇀ GenerativePosition |
| NEW JA endpoints | J02:18–20、U017 | ENと同じ許可port |
| NEW JA adapter | J02:25–27、U007/017 | ENと同じ許可port |
| NEW JA position | J02:32–34、U021 | ENと同じ許可port |
| NEW totals | display6 / inline0 | 2filesのみ、newstrict/theorem/operator追加0 |
| Current totals | display104 / inline2199 | old98＋new6、旧置換なし |

parserは従来inventoryに合わせたdelimiter/environment scan。countだけでなく全旧segmentのbytesと順序を照合した。旧式のdelete/reinsertや移動はない。新portsはunnumbered displayで、labelやcounterを増やしていない。厳密な型・意味の妥当性受入は次の独立監査に残る。

## 10. Protected-content verification

| Protected group | Verification | Result |
|---|---|---|
| PS001–008 | raw fragments再定位、SHA-256、各fragment一意に存在 | PASS |
| Broader JA theorem/corollaries | baseline J03:23–268全文、heading/論証含む | PASS |
| Appendix D proof-like material | baseline DJ:13–EOF全文 | PASS |
| E blocks / JA intro schema / definition2.1 | E05:91–95/J05:260–279/AJ80,169–171/J00:30–36/J02:64–68全文 | PASS |
| Figure environments | Intelligence28環境全文のordered comparison | PASS、caption/figurenote/includegraphics/label不変 |
| All figures/PDF/BibTeX/source_md/working Markdown | full repository file hash、許可差分以外不変 | PASS |
| P1 / main_ja / E11 / DE / upstream | full file hash不変 | PASS |
| Bio F / flow J / J_C | 旧全math列、非targetfile、引用row/本文非変更を照合 | PASS |
| Theorem/definition headings and numbering | numbered heading列・proof headings、section構造保持 | PASS、proof rewriteなし |
| labels/refs/cites/macros/counters | 各66TeXの既存token列/定義行比較 | PASS、既存追加削除0 |
| Master structure / neighbors | AE23以降・AJ非targetrows、table列/begin/end、v2.1guard保持 | PASS |
| Phase00–07 / impl01–22 | 30records full hash不変 | PASS |

negative allowlistは8hashだけでなく、上表と全旧math列・許可target外bytesを含めて検査した。追加後に古いline番号で切り出すのでなくliteral fragmentを追跡した。latex buildは行わず、layout/overfull box・PDFparityは未検査である。

## 11. EN / JA asymmetry

| Aspect | Implementation handling | Self-check |
|---|---|---|
| P2 metadata | JA primary、EN working draft不変 | PASS |
| F active contract | 共通の意味/型portだけ各言語へ明示、旧式は各版のまま | PASS |
| Old scalar J | EN定義・JAproof/Master/Gettierの別来歴を保持 | PASS |
| Set-valued F | ENだけhistorical display、JAへ輸入しない | PASS |
| Master J row | EN no-J-row、JA既存J-row保持 | PASS |
| Appendix D | JA強いsketch全保持、DEへ同期なし | PASS |
| P1 AR007 | JA意味/著者意図とEN構造安定化を統一せず、全P1非変更 | PASS |
| Abstract | ENの帰属だけ修正、JA placeholder非変更 | PASS |

## 12. Implementer self-check / remaining HOLD

changed sourceをcore EN/JA全文、consumer diffと周辺guard、figure/E境界、table/appendixの順に再読した。これは独立auditと呼ばない。

| Check | Result / witness |
|---|---|
| Audit notesなしでactive/historyが読める | YES、§2のactive見出しとPreserved local-state model、後段各章帰属 |
| Old theoremが旧模型として可視 | YES、図以前のbody boundary＋proof全文KEEP |
| Position≠old scalar J | YES、別signature/partialcarrier・非同一の本文明示 |
| F≠global deterministic law | YES、actualrecordとoptionaladapter、multipleafterはundefined |
| Set-valued Fがhistory | YES、ENheading/過去voice/非active successor説明 |
| 新strict-step theoremなし | YES、新predicate0、proof移行0 |
| F-powerの暗黙代入なし | YES、record連接と反復の区別、E block外側boundary |
| Stale figuresに境界あり | YES、FIG006/009body、asset/caption保持 |
| EN/JA非対称 | YES、setdisplay/Jrow/DJ/abstractの来歴保持 |
| P1非変更 | YES、whole-file hash |
| Bio/flow-J非変更 | YES、旧math/非targetparts保持 |
| Accidental new claim strength | self-checkで検出0。実証・新proof・blocker解消は主張しない |

| Remaining HOLD | Owner / next boundary |
|---|---|
| Migration acceptance | 独立post-migration auditが必要。今回acceptedではない |
| EQF026 / EQF027 | conditional design / proof・non-tautology HOLD。新J移行なし |
| E / LE emergence / Φ / μ / rule plasticity | type/formal/proof/research作業は今回非実施 |
| FIG009 / FIG011 / other stale figures | presentation/architecture仕様・repair別task。図受入・build未許可 |
| Frozen SERIOUS5 / blockers13 / OPEN24 | global status変更なし。実装によるclosureなし |
| Provenance / authority debt | v2.1 exact artifact等不変、言語priorityを数学的真偽へ使わない |
| Build / distribution | NO。source-only状態、PDFは旧配布物のまま |

## 13. Explicit answers

| No. | Question | Answer |
|---|---|---|
| 1 | Preflight passed? | YES |
| 2 | PS21-001–008 preserved? | YES |
| 3 | EQF025 implemented within authorization? | YES |
| 4 | EQF047 documentary split implemented? | YES |
| 5 | EQF048 historical EN treatment implemented? | YES |
| 6 | Old scalar J preserved? | YES |
| 7 | New position port inserted separately? | YES |
| 8 | Old set-valued F equation preserved? | YES |
| 9 | EQF026 new predicate inserted? | NO |
| 10 | EQF027 theorem/proof changed? | NO |
| 11 | Any old math mutated? | NO |
| 12 | Any new-J proof transfer introduced? | NO |
| 13 | Any hidden global F law introduced? | NO in implementer self-check |
| 14 | Consumer guards complete? | YES for authorized U21 scope, self-check only |
| 15 | FIG006 outer guard implemented? | YES |
| 16 | FIG009 outer guard implemented? | YES |
| 17 | Figure assets/captions unchanged? | YES |
| 18 | P1 unchanged? | YES |
| 19 | Bio F / flow J unchanged? | YES |
| 20 | EN/JA asymmetry preserved? | YES |
| 21 | Build performed? | NO |
| 22 | Commit/push performed? | NO |
| 23 | Ready for independent post-migration audit? | YES |
| 24 | Migration accepted? | NO — pending independent audit |

## 14. Validation / stop boundary

source validationをPASSさせた後に本recordを作成し、READMEを追記する。検証scriptはrepo外 `${TEMP_EVIDENCE_ROOT}/int_impl23.l32RV7/validate.py`、結果は `validation.json`、所有差分は `owned.patch` / `owned_diff.json`。preflight baselineと旧66TeX bytesを保持する。

| Validation | Final result |
|---|---|
| Full repository comparison | PASS。1520→1521 files、変更は許可28TeX＋README、追加は本impl23のみ、削除0 |
| Task-start baseline | 全hash・旧66TeX bytes・git statusを保持。既存ユーザー変更のreset/削除なし |
| Allowed source diff | 28/28 allowlist内、exact diffを§15へ保存。許可外TeX38は不変 |
| Old/new math | 旧98/2199同一・同順序、新6displayのみ。byte mismatch0 |
| Protected content | PS8/8、広い保護9block、figure環境28、旧heading/refs/macros等PASS |
| History / non-source artifacts | Phase00–07/impl01–22の30records、figures/PDF/BibTeX/source_md/既存workingMarkdownは不変 |
| README | task-start bytesを完全prefixとして保持、末尾追記のみ。source validation PASS後に追記 |
| git diff --check | PASS、exit0、出力なし |
| git status --short | 開始時全文と同一、M289 / ??9。28sourceは既存modified集合内、audit directoryは既存untracked内なのでfullhash/diffで今回分を検証 |
| Validation limits | static/source検査とimplementer再読のみ。build/render/独立acceptanceは未実施 |
| Forbidden follow-on actions | proof/figure repair、追加式移行、独立audit、build/distribution、web、simulation、commit/pushは全てNO |

source migrationとself-checkで停止し、独立audit・proof repair・figure repair・build/distribution・web・simulation・commit/pushへ進まない。新portの追加は限定許可された今回の実装であり、他の式を編集できる一般許可ではない。

## 15. Exact task-owned source diff

以下はtask-start→currentの全28TeX diff。既存ユーザー変更・audit record・README差分は含まない。削除行と追加行が同じmathを含む場合も、そのparagraphのprose帰属だけが変わり、math bytesは§9の独立機械比較で同一確認済み。行移動を示すcontextはproof修理を意味しない。

### intelligence-part2/appendices/appendix_a_master_table.tex

```diff
--- baseline/intelligence-part2/appendices/appendix_a_master_table.tex
+++ current/intelligence-part2/appendices/appendix_a_master_table.tex
@@ -5,6 +5,8 @@
 
 
 This appendix collects the principal variables used in Intelligence Part II.
+
+\noindent\textbf{Historical inference inventory.} In this appendix, inference F, scalar justification (where discussed), and no-fixed-point references retain their old local-state-model scope. They do not define the active record or position ports. Other field-flow objects keep their distinct signatures. The absent English J row is not supplied by bilingual synchronization.
 
 \begin{longtable}{@{}p{0.18\linewidth}p{0.30\linewidth}p{0.42\linewidth}@{}}
 \toprule
@@ -18,8 +20,8 @@
 $C$ & closure degree & operational stability, not truth \\
 $C_{\max}$ & complete closure limit & unattainable boundary of closure \\
 $I$ & information-field drive & drive generated by non-closure \\
-$F$ & inference operator & advances inferential states \\
-$L_F$ & inference layer & layer on which $F$ operates \\
+$F$ & inference operator & historical local-state model: advances inferential states \\
+$L_F$ & inference layer & historical local-state model: layer on which $F$ operates \\
 $L_R$ & log layer & recursive reference to traces of inference \\
 $L_E$ & emergent stopping layer & externally dependent stopping attractor \\
 $E$ & external stopping operator & stopping action supplied through $L_E$ \\
```

### intelligence-part2/appendices/appendix_a_master_table_ja.tex

```diff
--- baseline/intelligence-part2/appendices/appendix_a_master_table_ja.tex
+++ current/intelligence-part2/appendices/appendix_a_master_table_ja.tex
@@ -2,6 +2,8 @@
 \section{変数表 Master Table v2.2}
 
 \noindent\textbf{記述の射程。} 文書的status。本表は原稿の変数inventoryを保存するものであり、特定されたMaster Table v2.1からの検証済み継承ではない。正確な来歴、当時の署名、採用範囲は未解決である。保存する表中の確立・実装・同一・同型等の語はsourceの強い定式化を記録するもので、その積極的な形式statusは保留される。表の項目から独立証明・操作的map・新たな仮定を与えない。
+
+\noindent\textbf{旧推論模型のinventory境界。} 本補遺末尾までの推論F・scalar正当化J・noFP参照は旧局所状態模型に属し、active record/position portの定義ではない。後段の比較・要約も同じ帰属で読む。外部停止のrowと反復からの非所属表示は、周囲の説明を含め保存する旧notationであり、active optional adapterを旧反復へ代入しない。Eの型は未解決で、非導出性・大きい反復数からのE成立を認定しない。他のfield-flow objectの署名と、未同定v2.1 artifactに関する文書的制約は変更しない。
 
 
 
@@ -56,9 +58,9 @@
 記号 & 名称 & 導入章 & 定義・役割 \\
 \midrule
 \endhead
-$F$ & 推論演算子 & \S{}2.1 & 正当化拡張作用素。$x_{n+1} = F(x_n)$。VED/Bio-IFGT の流れ・状態発展演算子と類似した形式的役割を持つが、source-localでありsame dynamicsやtyped identityを意味しない \\
-$J$ & 正当化測度 & \S{}3.1 & $F$ の作用による正当化の進行を測る測度。$J(F(x)) > J(x)$ が成立(前提 P2) \\
-$L_F$ & 推論層 & \S{}2.3 & $F$ の作用域全体。推論軌道を含む。内部停止条件を持たない(定理 3.1) \\
+$F$ & 推論演算子 & \S{}2.1 & 旧局所状態模型の正当化拡張作用素。$x_{n+1} = F(x_n)$。VED/Bio-IFGT の流れ・状態発展演算子と類似した形式的役割を持つが、source-localでありsame dynamicsやtyped identityを意味しない \\
+$J$ & 旧模型のscalar正当化測度 & \S{}3.1 & $F$ の作用による正当化の進行を測る測度。$J(F(x)) > J(x)$ が成立(前提 P2) \\
+$L_F$ & 推論層 & \S{}2.3 & $F$ の作用域全体。推論軌道を含む（旧局所状態模型）。内部停止条件を持たない(定理 3.1) \\
 $L_R$ & ログ層 & \S{}5.2 & $L_F$ の運動の痕跡(ログ)への再帰参照運動の層。$L_E$ 創発の基盤。所在は系によって異なる(個体内・環境外部化・凍結) \\
 $L_E$ & 創発停止層 & \S{}5.3 & $L_R$ の再帰運動と外部相互拘束 $H_{ij}$ の関数として創発する停止層。$L_E = \Phi(L_R, H_{ij})$。個体内にありながら外部依存的 \\
 \bottomrule
```

### intelligence-part2/appendices/appendix_b_homology.tex

```diff
--- baseline/intelligence-part2/appendices/appendix_b_homology.tex
+++ current/intelligence-part2/appendices/appendix_b_homology.tex
@@ -26,7 +26,7 @@
 Physics & differential flow and quasi-closure & particle-like attractor \\
 Life & non-equilibrium informational exchange & life attractor $\Omega_{\text{life}}$ \\
 Consciousness & temporal non-closure and speed-scale difference & conscious state as windowed stabilization \\
-Intelligence & no internal fixed point in $L_F$ & emergent stopping layer $L_E$ \\
+Intelligence & historical conditional model: no internal fixed point in $L_F$ & emergent stopping layer $L_E$ \\
 Society & distributed disagreement and non-final legitimacy & $\Phi_{\text{net}}$ synchronization \\
 \bottomrule
 \end{longtable}
```

### intelligence-part2/appendices/appendix_b_homology_ja.tex

```diff
--- baseline/intelligence-part2/appendices/appendix_b_homology_ja.tex
+++ current/intelligence-part2/appendices/appendix_b_homology_ja.tex
@@ -22,7 +22,7 @@
 知性 Part II(本論文) & Vol.1〜4(物理層) & Bio-IFGT(生命層) & 意識編 & 概念地形編 \\
 \midrule
 \endhead
-内部不動点不在($L_F$ の非閉包) & $C_{max}$ 不到達性 & 準閉包の維持限界 & 意識の状態遷移が完結しない & 概念の完全閉包は到達不能 \\
+旧局所状態模型の内部不動点不在($L_F$ の非閉包) & $C_{max}$ 不到達性 & 準閉包の維持限界 & 意識の状態遷移が完結しない & 概念の完全閉包は到達不能 \\
 創発停止層 $L_E$(アトラクター) & 粒子 = $E(A)$ の局所極小(Vol.2) & 生命アトラクター $\Omega_{\text{life}}$ & 意識の安定状態 & 概念の準安定点 \\
 第二アトラクター($L_E$) & ゲージ群の安定構造 & 第二アトラクター $\Omega_{\text{intel}}$ & — & — \\
 差分の地平線(知性層) & 差分の地平線 $C_{max}$(Vol.4) & 生命の非平衡限界 & 意識の差分地平 & 概念地形の境界 \\
@@ -119,7 +119,7 @@
 \midrule
 \endhead
 Bio-IFGT & 生命系の状態発展演算子 $\dot{x} = F(x;\theta)$ & Bio-IFGT \texttt{core\_equations} \\
-本論文 知性層 & 推論演算子 $x_{n+1} = F(x_n)$。Bio-IFGTの $F(x;\theta)$ と類似した形式的役割を持つsource-local object & 本論文 \S{}2.1 \\
+本論文 知性層 & 旧局所状態模型の推論演算子 $x_{n+1} = F(x_n)$。Bio-IFGTの $F(x;\theta)$ と類似した形式的役割を持つsource-local object & 本論文 \S{}2.1 \\
 \bottomrule
 \end{longtable}
 
@@ -174,7 +174,7 @@
 差分の地平線(知性層) & \S{}9 知性の差分の地平線 & 役割上の比較 \\
 ゲティア問題と $\mu_\theta$ の関係（同値は保留） & \S{}6 ゲティアの構造的診断 & Part II の $\mu_\theta$ との強い同値主張は未解決 \\
 三層プロファイル比較 & \S{}5 Physarum・Transformer & Part II が三層で再位置づけ \\
-分岐爆発と内部不動点不在の比較 & \S{}7 動力学的不安定性 & 別の負担を持つ役割比較 \\
+旧模型における分岐爆発と内部不動点不在の比較 & \S{}7 動力学的不安定性 & 別の負担を持つ役割比較 \\
 $L_E$ と第二アトラクターの比較 & — & Bio-IFGT のforward proposalをPart IIが知性層固有の構成へ展開。identity / typed translationは未確立 \\
 \bottomrule
 \end{longtable}
```

### intelligence-part2/appendices/appendix_c_part1_mapping.tex

```diff
--- baseline/intelligence-part2/appendices/appendix_c_part1_mapping.tex
+++ current/intelligence-part2/appendices/appendix_c_part1_mapping.tex
@@ -8,7 +8,9 @@
 
 \subsection{Individual Non-Closure}
 
-Part I stated that individual intelligence does not close. Part II proposes a conditional formal statement: the inference layer $L_F$ has no internal fixed point under fixed $\theta$. This refines non-closure into the non-closure theorem.
+Part I stated that individual intelligence does not close. Part II preserves a historical local-state model's conditional formal statement: the inference layer $L_F$ has no internal fixed point under fixed $\theta$. This refines non-closure into the non-closure theorem.
+
+This remains an unimplemented editorial proposal for Part I, not a derivation from the active record/position contract or a proof of rule-changing capacity.
 
 \subsection{Branching Explosion}
 
```

### intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex

```diff
--- baseline/intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex
+++ current/intelligence-part2/appendices/appendix_c_part1_mapping_ja.tex
@@ -31,7 +31,7 @@
 \S{}4 IFGT を語彙として / Physarum 語彙対応 & IFGT 基本語彙 & \S{}1 で知性層用再定式化。\S{}2.1 で $F(x;\theta)$ との接続 & 継承・拡張 \\
 \S{}5 Physarum・Transformer インスタンス化 & 領域横断インスタンス & \S{}5.4 で三層プロファイルとして精密化。三者は「異なるプロファイル」であって「$L_F$ のみ」ではない & \textbf{精密化(要修正)} \\
 \S{}6 ゲティア問題の構造的診断 & 知識の構造的問題 & \S{}10 で継承・拡張。「排除不能性 = $\mu_\theta$ の存在の代償」を追加 & 継承・拡張 \\
-\S{}7 蓄積された正しさの動力学的不安定性 & 分岐爆発 & \S{}3.7 で「内部不動点不在の動力学的表現」として統合 & 継承・統合 \\
+\S{}7 蓄積された正しさの動力学的不安定性 & 分岐爆発 & \S{}3.7 の旧模型で「内部不動点不在の動力学的表現」として統合する旧提案 & 継承・統合 \\
 \S{}8 個体知性の非閉包 & 個体は閉じない & \S{}3 で条件付き非閉包議論として扱う。\S{}5 で「$L_F$ 単独では閉じないが $L_E$ で閉じうる」と精密化 & 継承・\textbf{精密化(要修正)} \\
 \S{}9 知性の差分の地平線 & 差分の地平線 & \S{}1.5 で $C_{max}$ 不到達性と役割上比較（同型は未確立）。\S{}3.6 で系 3.3 として接続 & 継承・\textbf{精密化(要修正)} \\
 \S{}10 収束と展望 & 総括 & \S{}13.6 の微修正リストとして引き継ぎ & 引き渡し \\
@@ -75,7 +75,7 @@
 \textbf{追加する内容}: 三層動力学との接続注記を追加する。
 
 \begin{quote}
-知性の差分の地平線は、三層動力学の語彙では次のように再記述される。$C_{max}$ への接近は推論演算子 $F$ に内部不動点を許さず(非閉包定理、Part II \S{}3)、完全閉包への到達は構造的に不可能である(系 3.3)。これは差分の地平線(本章)・$C_{max}$ 不到達性(VED Vol.4)・内部不動点不在(Part II \S{}3)が、役割上比較されることを提案するが、同一の動力学を確立しない。領域横断ホモロジーの最重要例のひとつ。
+以下は旧局所状態模型に基づく未実装の編集提案として保存する。知性の差分の地平線は、三層動力学の語彙では次のように再記述される。$C_{max}$ への接近は推論演算子 $F$ に内部不動点を許さず(非閉包定理、Part II \S{}3)、完全閉包への到達は構造的に不可能である(系 3.3)。これは差分の地平線(本章)・$C_{max}$ 不到達性(VED Vol.4)・内部不動点不在(Part II \S{}3)が、役割上比較されることを提案するが、同一の動力学を確立しない。領域横断ホモロジーの最重要例のひとつ。
 \end{quote}
 
 
```

### intelligence-part2/appendices/appendix_d_optional_notes_ja.tex

```diff
--- baseline/intelligence-part2/appendices/appendix_d_optional_notes_ja.tex
+++ current/intelligence-part2/appendices/appendix_d_optional_notes_ja.tex
@@ -9,6 +9,8 @@
 
 \bigskip
 
+
+\noindent\textbf{歴史的スケッチの境界。} 以下の推論F・scalar正当化J・不動点・停止述語への参照は旧局所状態模型の履歴であり、active record/position契約の証明ではない。全状態への厳密増加を置く強い版も歴史として保存するが、本文のadmissible-domain scopeを上書きせず、新positionへ移行しない。この帰属は補遺末尾までの旧F/J参照に限り、Bioの状態発展やflowの同字形を再定義しない。元のheading・前提・proof textは変更しない。
 
 \subsection{定理 3.1(非閉包定理 / Non-Closure Theorem)}
 
```

### intelligence-part2/main.tex

```diff
--- baseline/intelligence-part2/main.tex
+++ current/intelligence-part2/main.tex
@@ -15,7 +15,7 @@
 
 
 \begin{abstract}
-This paper develops a structural proposal for Intelligence Part II of the VED/IFGT theory tree. The no-fixed-point discussion of the inference layer $L_F$ is conditional on the stated justification premise and does not establish the impossibility of all internal cognitive stopping. The three-layer dynamics $L_F/L_R/L_E$ is a model-local architecture; the emergent stopping layer $L_E$ names a functional role, while its emergence, convergence, and independent detection remain unresolved. Animism, God, religion, science, institutions, and social blockchain are considered as conceptual or historical interpretations, not validated social laws. The phase diagram is a qualitative hypothesis, not a measured or derived operating band. Movable and revisable stopping is proposed as a resource for sustained inference, not as an established condition for subjective freedom. Field/network identity, threshold mobility/error-tolerance equivalence, and general-intelligence necessity remain open.
+This paper develops a structural proposal for Intelligence Part II of the VED/IFGT theory tree. The historical local-state model's no-fixed-point discussion of the inference layer $L_F$ is conditional on the stated justification premise and does not establish the impossibility of all internal cognitive stopping. The three-layer dynamics $L_F/L_R/L_E$ is a model-local architecture; the emergent stopping layer $L_E$ names a functional role, while its emergence, convergence, and independent detection remain unresolved. Animism, God, religion, science, institutions, and social blockchain are considered as conceptual or historical interpretations, not validated social laws. The phase diagram is a qualitative hypothesis, not a measured or derived operating band. Movable and revisable stopping is proposed as a resource for sustained inference, not as an established condition for subjective freedom. Field/network identity, threshold mobility/error-tolerance equivalence, and general-intelligence necessity remain open.
 \end{abstract}
 
 \setcounter{tocdepth}{2}
```

### intelligence-part2/sections/00_introduction.tex

```diff
--- baseline/intelligence-part2/sections/00_introduction.tex
+++ current/intelligence-part2/sections/00_introduction.tex
@@ -6,7 +6,7 @@
 
 This paper is Intelligence Part II in the VED/IFGT theory tree. Part I described intelligence as a non-closed dynamical phenomenon. Part II asks a more specific question: if inference does not close itself, how can intelligence nevertheless stop, judge, act, and persist?
 
-The answer developed here is that intelligence is not merely the growth of inference. Intelligence is the co-evolution of inference and stopping. The inference layer $L_F$ expands justification, generates branches, and moves along gradients of closure. The fixed-point discussion applies only under the formal premises stated later. If inference is left to inference alone, it can enter infinite regress, branching explosion, or premature pathological closure.
+The answer developed here is that intelligence is not merely the growth of inference. Intelligence is the co-evolution of inference and stopping. In the historical local-state model retained in Sections 2--3, the inference layer $L_F$ expands justification, generates branches, and moves along gradients of closure. The fixed-point discussion applies only under the formal premises stated later. If inference is left to inference alone, it can enter infinite regress, branching explosion, or premature pathological closure.
 
 The central structure of this paper is therefore:
 \[
@@ -35,7 +35,7 @@
 
 \subsection{How to Read the History of Intelligence}
 
-The inference operator $F$ is discussed under strict-increase and fixed-region premises. Relating that conditional model to the history of intelligence or to branching and cognitive stability is a separate hypothesis, not a consequence of nonclosure alone.
+In that historical model, the inference operator $F$ is discussed under strict-increase and fixed-region premises. Relating that conditional model to the history of intelligence or to branching and cognitive stability is a separate hypothesis, not a consequence of nonclosure alone.
 
 Finite resources motivate considering inference and stopping together. The proposed co-evolution account does not establish that every cognitive system without a specified stopping structure must be unsustainable.
 
```

### intelligence-part2/sections/00_introduction_ja.tex

```diff
--- baseline/intelligence-part2/sections/00_introduction_ja.tex
+++ current/intelligence-part2/sections/00_introduction_ja.tex
@@ -26,6 +26,8 @@
 本論文を貫く論理は三本の線に展開される:
 
 \textbf{第一線 — 非閉包と外部停止}:
+
+\noindent 以下の第一線のschemaは旧局所状態模型の推論鎖を歴史的に保存する。active record/position接口から導出したものではなく、矢印だけから外部停止の普遍的必要性やEの型・存在を証明しない。
 
 \[
 \text{差がある} \;\longrightarrow\; F(L_F) \;\longrightarrow\; \text{内部不動点不在} \;\longrightarrow\; \text{無限後退}
@@ -134,7 +136,7 @@
 \subsubsection{分岐爆発}
 
 
-Part I \S{}7 の分岐爆発と $L_F$ の内部停止模型を比較するが、グラフ増大と不動点不在の同一性は確立していない(\S{}3.7)。
+旧局所状態模型への参照として、Part I \S{}7 の分岐爆発と $L_F$ の内部停止模型を比較するが、グラフ増大と不動点不在の同一性は確立していない(\S{}3.7)。
 
 \subsubsection{個体知性の非閉包}
 
@@ -164,7 +166,7 @@
 \end{longtable}
 
 
-\S{}3 の条件付き不動点議論と、\S{}5 の停止構成案を区別する。二つの接続は三層動力学の提案を動機づけるが、認知的停止の説明達成を意味しない。
+旧局所状態模型の \S{}3 の条件付き不動点議論と、\S{}5 の停止構成案を区別する。二つの接続は三層動力学の提案を動機づけるが、認知的停止の説明達成を意味しない。
 
 \S{}4 と \S{}6〜\S{}10 は両中心の間を埋める章であり、\S{}11〜\S{}13 は両者を統合する章である。
 
@@ -200,7 +202,7 @@
 
 \subsection{知性の歴史をどう読むか}
 
-本論文は知性の歴史を「推論能力の発達史」としてだけは読まない。推論演算子 $F$ の非閉包は、後述の固定領域・厳密増加などの条件下の議論である。推論能力の増大と分岐・回帰・停止点の選択との関係は、別途検討される仮説である。
+本論文は知性の歴史を「推論能力の発達史」としてだけは読まない。保存する旧局所状態模型の推論演算子 $F$ の非閉包は、後述の固定領域・厳密増加などの条件下の議論である。推論能力の増大と分岐・回帰・停止点の選択との関係は、別途検討される仮説である。
 
 推論と停止を共同で考えるのが本稿の構成案である。有限な資源のもとで停止構造を問う動機はあるが、停止の未指定から任意の認知の持続不能を導くものではない。
 
@@ -268,7 +270,7 @@
 \endhead
 \S{}1 & 準備 & VED・IFGT の知性層用再定式化、創発の VED 内定義、三層予告 \\
 \S{}2 & 推論演算子 $F$ と推論層 $L_F$ & $L_F$ の定義、相互拘束と閾値、$\mu_\theta$ の開放窓 \\
-\textbf{\S{}3} & \textbf{非閉包定理} & \textbf{$L_F$ の構造命題: 内部不動点不在(第一中心)} \\
+\textbf{\S{}3} & \textbf{非閉包定理} & \textbf{$L_F$ の旧局所模型の条件付き命題: 内部不動点不在(第一中心)} \\
 \S{}4 & 応答チャネルと沈黙世界 & 閾値現象としての C-幾何学、$L_R$ の予兆 \\
 \textbf{\S{}5} & \textbf{創発停止層 $L_E$} & \textbf{$L_R$ → $L_E$ → $E$ → $\Phi_{\text{net}}$ の動力学(第二中心)} \\
 \S{}6 & アニミズム & $L_E$ を環境直接相互干渉で維持 \\
```

### intelligence-part2/sections/01_preliminaries.tex

```diff
--- baseline/intelligence-part2/sections/01_preliminaries.tex
+++ current/intelligence-part2/sections/01_preliminaries.tex
@@ -22,10 +22,12 @@
 
 \subsection{VED Basic Form}
 
-VED begins from difference. Where there is difference, there is a gradient; where there is a gradient, there is flow; where flow is constrained, quasi-closure and attractors can emerge. In the intelligence layer, this grammar appears as:
+VED begins from difference. Where there is difference, there is a gradient; where there is a gradient, there is flow; where flow is constrained, quasi-closure and attractors can emerge. The following preserved schema records the historical local-state/justification reasoning in the intelligence layer:
 \[
 \text{difference} \;\longrightarrow\; F(L_F) \;\longrightarrow\; \text{non-closure} \;\longrightarrow\; \text{externalized stopping}.
 \]
+
+\noindent\textbf{Historical schema boundary.} The preceding arrows are not derived from the active realized-record or generative-position interfaces in Section 2. They neither establish universal external stopping nor specify the type or existence of E. The historical application to the inference layer is not an application of the new record core.
 
 The closure degree $C$ measures how close a state is to operable stability. The information-field drive can be written schematically as a function of non-closure:
 \[
@@ -41,7 +43,7 @@
 \item \textbf{(B) reconfiguration of the region}: $\theta$ itself changes, thereby changing $\Omega_\theta$.
 \end{itemize}
 
-The non-closure theorem in \S{}3 applies to (A), movement within fixed $\theta$. The emergence hypothesis in \S{}5 invokes (B), region reconfiguration. This distinction is essential. The fixed-point discussion additionally depends on the stated strict-increase premise and the chosen stopping model. Region reconfiguration motivates a separate emergence hypothesis, not an established route from nonclosure to stopping.
+The historical local-state model's non-closure theorem in \S{}3 applies to (A), movement within fixed $\theta$. The emergence hypothesis in \S{}5 invokes (B), region reconfiguration. This distinction is essential. The fixed-point discussion additionally depends on the stated strict-increase premise and the chosen stopping model. Region reconfiguration motivates a separate emergence hypothesis, not an established route from nonclosure to stopping.
 
 \subsection{Emergence}
 
```

### intelligence-part2/sections/01_preliminaries_ja.tex

```diff
--- baseline/intelligence-part2/sections/01_preliminaries_ja.tex
+++ current/intelligence-part2/sections/01_preliminaries_ja.tex
@@ -160,7 +160,9 @@
 \end{longtable}
 
 
-\textbf{推論軌道}: 推論演算子 $F$ の反復作用によって C-landscape 上に描かれる軌道:
+\textbf{旧局所状態模型の推論軌道}: 推論演算子 $F$ の反復作用によって C-landscape 上に描かれる軌道:
+
+これは保存する旧状態mapの軌道表現であり、active recordの連接を同一mapの冪と定義するものではない。
 
 \[
 x_0 \xrightarrow{F} x_1 \xrightarrow{F} x_2 \xrightarrow{F} \cdots
@@ -172,7 +174,7 @@
 
 \begin{itemize}
 \item \S{}2: 推論軌道の基本性質
-\item \S{}3: 軌道に内部不動点が存在しないこと(非閉包定理)
+\item \S{}3: 旧局所状態模型の軌道に内部不動点が存在しないこと(非閉包定理)
 \item \S{}4: 軌道が応答的環境と沈黙的環境で異なる挙動を示すこと
 \item \S{}11: 軌道の不安定性が速度・解像度・停止硬度の三軸で記述されること
 \end{itemize}
@@ -197,7 +199,7 @@
 \end{itemize}
 
 
-Part I \S{}9 の「知性の差分の地平線」と、本論文 \S{}3 の \textbf{推論演算子 $F$ の内部不動点不在} は、役割上の比較対象である。前者の認知的解釈を後者の条件付き形式的結論と同一視しない。
+Part I \S{}9 の「知性の差分の地平線」と、本論文の旧局所状態模型の \S{}3 の \textbf{推論演算子 $F$ の内部不動点不在} は、役割上の比較対象である。前者の認知的解釈を後者の条件付き形式的結論と同一視しない。
 
 VED Vol.4 と Part I \S{}9 と本論文 \S{}3 は、異なる領域を共通の役割語彙で比較したものであり、同じ対象・法則の証明ではない。これは Part I で示された領域横断ホモロジーの最も重要な例である。
 
@@ -366,6 +368,6 @@
 
 \S{}2 前半では、$F$ の四性質を局所的な記述として提示し、Part I \S{}4 の語彙と Part I \S{}5 の Physarum・Transformer を比較する。\S{}2 後半では、相互拘束 $H_{ij}$ と応答性閾値の候補的関係、閾値移動能力 $\mu_\theta$ の定義を扱う。\S{}2 末尾の $\mu_\theta$ と $L_F$・$L_R$・$L_E$ の接続は機構仮説であり、生成の確認ではない。
 
-\S{}3 では、$F$ に関する厳密増加と固定された閾値・領域内移動などの条件を明示した非閉包の議論を扱う。任意の認知的停止を排除する結論とは区別する。
-
-\bigskip
+旧局所状態模型の \S{}3 では、$F$ に関する厳密増加と固定された閾値・領域内移動などの条件を明示した非閉包の議論を扱う。任意の認知的停止を排除する結論とは区別する。
+
+\bigskip
```

### intelligence-part2/sections/02_inference_operator.tex

```diff
--- baseline/intelligence-part2/sections/02_inference_operator.tex
+++ current/intelligence-part2/sections/02_inference_operator.tex
@@ -1,20 +1,43 @@
 % English draft based on sections/02_inference_operator_ja.tex
 \section{The Inference Operator $F$}
 
-\noindent\textbf{Scope of the account.} The inference operator is source-local. Its cognitive reading and the Physarum/Transformer comparisons are proposed correspondences, not implementations of one shared operator. The single-state and set-valued English formulations are not silently reconciled with the Japanese form; their composition with justification remains a formal/authority question. The indexed constraint relation is distinct from a calibrated response threshold. Threshold mobility retains its local definition, while endogenous detection and the production of stopping sites remain unresolved. Biological and cognitive constraint changes are compared by role and timescale, not identified as the same law.
+\noindent\textbf{Scope of the account.} The inference operator is source-local. Its cognitive reading and the Physarum/Transformer comparisons are proposed correspondences, not implementations of one shared operator. The active account now distinguishes a realized-record core and an optional local adapter from the preserved historical state-map and scalar-justification model. The English set-valued formulation remains historical, not an active successor type; its unresolved composition is not repaired by language priority. The old proof does not transfer to the new contract. The indexed constraint relation is distinct from a calibrated response threshold. Threshold mobility retains its local definition, while endogenous detection and the production of stopping sites remain unresolved. Biological and cognitive constraint changes are compared by role and timescale, not identified as the same law.
 
 
-This chapter defines the inference operator used throughout the paper. The operator $F$ is not tied to one implementation such as deduction, induction, Bayesian update, neural generation, or statistical prediction. It denotes the minimal operation by which a state of understanding is advanced into a more justified state.
+This chapter separates the active realized-transition account from the historical inference model cited later. The next description records the old local-state model: The operator $F$ is not tied to one implementation such as deduction, induction, Bayesian update, neural generation, or statistical prediction. It denotes the minimal operation by which a state of understanding is advanced into a more justified state.
 
 \subsection{Definition}
 
-Let $\mathcal{X}$ be the state space of inferential states. An inference operator is a map
+\noindent\textbf{Active realized-transition interface.} In the active account, F names the description of an actually generated transition, not a total law of unrealized futures. For a declared Scope, accepted records carry canonical occurrence endpoints, context/rule-version references, and a stated basis for describing realization:
+% impl23 authorized addition: record endpoint ports
+\[
+\mathrm{before},\mathrm{after}:\mathrm{AcceptedRealizedRecord}\to\mathrm{Occurrence}.
+\]
+Occurrence is distinct from StateView. State views may depend on currently surfaced, compressed or reconstructed history without containing a complete archive. Equal surface views imply neither equal occurrences nor equal generative positions. Alias resolution follows the declared identity convention; endpoint inequality is not a record-acceptance requirement. Scope fixes the analytical sides, observation window/timescale, and identity conventions, not a permanent subject. A change of scope or evaluation convention requires a new version and an explicit correspondence before cross-scope composition.
+
+An optional local adapter is available only on a declared slice:
+% impl23 authorized addition: optional successor port
+\[
+\mathrm{realizedSuccessor}[\mathrm{slice}]:\mathrm{EligibleOccurrence}\rightharpoonup\mathrm{Occurrence}.
+\]
+Declare slice, window, context, rule-version metadata, identity convention, and eligibility fields independently of strictness or no-fixed-point outcomes. After records exist, check that at least one matching record exists, endpoint identities are unambiguous, and all records for the same canonical before-occurrence in that slice have the same after-occurrence. If distinct after-values remain, leave the adapter undefined and retain the records; introduce no selector and do not re-partition context or identity to obtain a desired conclusion. Further records may require an explicitly versioned reassessment. This structural check establishes neither global determinism nor a pre-existing completed future branch set. General record chaining is not a power of one map; adapter iteration requires defined intermediate inputs and the same declared slice/version and composition carrier. State, context, and rule changes remain distinct.
+
+\noindent\textbf{Active generative-position interface.} For a fixed Scope and EvaluationProfile, use a separate descriptive port:
+% impl23 authorized addition: position port
+\[
+\mathrm{position}:\mathrm{Occurrence}\rightharpoonup\mathrm{GenerativePosition}.
+\]
+GenerativePosition has its own declared identity carrier; it is not a real-valued measure, StateView, or an occurrence identifier. The port is partial and need not be injective. Before/after evaluation requires both ports to be defined under the same scope/profile, without an implicit cast from surface state or a switch of evaluation rules. Position represents generative placement, not accessible memory amount, retention hardness, visible distinction, effective constraint, justification, or truth. No strict-step predicate, automatic monotonicity, or theorem is asserted here. The scalar justification J retained below is a distinct historical local-model object; its proof is not transferred. Surface recurrence is allowed, and fresh occurrence IDs do not establish substantive nonclosure.
+
+\noindent\textbf{Preserved local-state model.} The following state-map and scalar-justification expressions remain visible in their original form. References to their premises, powers, or no-fixed-point conclusions later in the paper retain this historical scope, not the new interfaces above.
+
+In the preserved historical local-state formulation, let $\mathcal{X}$ be the state space of inferential states. An inference operator is a map
 \[
 x_{n+1}=F(x_n),
 \]
 where $x_n\in\mathcal{X}$ is a provisional state and $F(x_n)$ is the next state generated by inference.
 
-The defining property of $F$ is justification extension. There exists a justification measure
+In the historical scalar-justification model, the defining property of $F$ is justification extension. There exists a justification measure
 \[
 J:\mathcal{X}\to\mathbb{R}
 \]
@@ -28,24 +51,24 @@
 
 In VED terms, inference follows a gradient of closure. It is interpreted through an analogy with a flow driven by non-closure. A state that appears unresolved generates a direction of further movement. Thus $F$ may be read as a proposed intelligence-layer counterpart of closure-gradient flow, not the same typed dynamics.
 
-The important consequence is that inference is inherently dynamic. It is an operation for moving, not an operation for terminating movement. External termination is proposed as distinct from $F$ as modeled here; universal necessity is not established.
+In the historical local-state interpretation, the important consequence is that inference is inherently dynamic. It is an operation for moving, not an operation for terminating movement. External termination is proposed as distinct from $F$ as modeled here; universal necessity is not established.
 
-\subsection{Branching}
+\subsection{Historical Branching Formulation}
 
-Inference is not necessarily deterministic. In many cases,
+The earlier English candidate-set formulation expressed possible branching as follows:
 \[
 F(x_n)=\{x_{n+1}^{(1)},x_{n+1}^{(2)},\ldots\}
 \]
-is better understood as a branching set of possible continuations. This branching structure connects Part II to the branching explosion described in Part I. The more inference is refined, the more branches can be generated.
+This expression was proposed as a branching set of possible continuations. That historical interpretation connected Part II to the branching explosion in Part I and suggested that refinement could generate more branches. It is not the active successor type or a completed set of future states; the candidate set is not an input to the old scalar justification measure, and no selection or lifted evaluation is supplied here.
 
-For this reason, stronger inference does not automatically mean stronger stability. It may mean that the system has more ways to continue and therefore more ways not to stop.
+Within that historical interpretation, stronger inference does not automatically mean stronger stability. It may mean that the system has more ways to continue and therefore more ways not to stop.
 
 \subsection{Internal Stopping Predicate}
 
-One might attempt to define a stopping predicate inside inference itself:
+Within that historical stopping model, one might attempt to define a stopping predicate inside inference itself:
 \[
 S(x)=1 \quad \text{if inference should stop at } x.
 \]
-But if $S$ is justified by inference, then $S$ requires further inference to justify its own stopping authority. The attempt to define stopping from inside $F$ therefore risks infinite regress. This point is formalized in \S{}3.
+In that historical sketch, if $S$ is justified by inference, then $S$ requires further inference to justify its own stopping authority. The attempt to define stopping from inside $F$ therefore risks infinite regress. This point is formalized in \S{}3.
 
 \bigskip
```

### intelligence-part2/sections/02_inference_operator_ja.tex

```diff
--- baseline/intelligence-part2/sections/02_inference_operator_ja.tex
+++ current/intelligence-part2/sections/02_inference_operator_ja.tex
@@ -1,11 +1,11 @@
 % Source: source_md/intelligence_part2_combined_ja.md
 \section{推論演算子 $F$ と推論層 $L_F$ — 相互拘束・閾値・開放窓}
 
-\noindent\textbf{記述の射程。} 推論演算子はsource-localである。認知的読解と粘菌・Transformerとの比較は対応提案であり、共通演算子の実装を意味しない。英語版の単一状態型・集合値型と日本語版を暗黙に統一せず、正当化との合成は形式・authority判断として残す。添字付き相互拘束関係は較正された応答閾値とは別である。閾値移動の局所定義は保持し、内発性の検出や停止設置場所の生成は未解決とする。生物と認知の拘束変化は役割・時間尺度の比較であり、同じ法則と同定しない。
-
-
-
-本章は三つの部分からなる。前半(\S{}2.1〜\S{}2.4)では推論演算子 $F$ を定義し、その作用域として推論層 $L_F$ を確立する。後半(\S{}2.5〜\S{}2.7)では、推論が作用する環境を相互拘束 $H_{ij}$ のパラメータとして捉え、応答的/沈黙的の区別が本体論的範疇ではなく閾値現象であることを示し、閾値移動能力 $\mu_\theta$ を導入する。末尾(\S{}2.8)では、$\mu_\theta$ が三層動力学における開放窓であることを予告する。
+\noindent\textbf{記述の射程。} 推論演算子はsource-localである。認知的読解と粘菌・Transformerとの比較は対応提案であり、共通演算子の実装を意味しない。active accountでは実現record coreとoptional local adapterを、保存する旧状態map・scalar正当化模型から区別する。英語版の集合値型はactive successor型でなく歴史的定式化として残し、その未解決の合成を言語priorityで修理しない。旧proofは新契約へ移行しない。添字付き相互拘束関係は較正された応答閾値とは別である。閾値移動の局所定義は保持し、内発性の検出や停止設置場所の生成は未解決とする。生物と認知の拘束変化は役割・時間尺度の比較であり、同じ法則と同定しない。
+
+
+
+本章は三つの部分からなる。前半(\S{}2.1〜\S{}2.4)では旧局所状態模型の推論演算子 $F$ を定義し、その作用域として推論層 $L_F$ を確立する。後半(\S{}2.5〜\S{}2.7)では、推論が作用する環境を相互拘束 $H_{ij}$ のパラメータとして捉え、応答的/沈黙的の区別が本体論的範疇ではなく閾値現象であることを示し、閾値移動能力 $\mu_\theta$ を導入する。末尾(\S{}2.8)では、$\mu_\theta$ が三層動力学における開放窓であることを予告する。
 
 \bigskip
 
@@ -13,15 +13,38 @@
 \subsection{推論演算子 $F$ の定義}
 
 
-推論の最小構造は、状態から状態への遷移である:
+\noindent\textbf{Active realized-transition interface。} active accountのFは実際に生成された遷移の記述を名指し、未実現の未来全体への固定法則ではない。宣言したScope内で、accepted recordはcanonicalなoccurrenceの両endpoint、context/rule-version参照、実現を記述する根拠を備える:
+% impl23 authorized addition: record endpoint ports
+\[
+\mathrm{before},\mathrm{after}:\mathrm{AcceptedRealizedRecord}\to\mathrm{Occurrence}.
+\]
+OccurrenceとStateViewは別である。現在の状態viewに、浮上した圧縮・再構成履歴が関与しても完全archiveは仮定しない。同じsurface viewからoccurrenceやgenerative positionの同一性を導かない。aliasは宣言済みidentity規約で解決し、endpointの非同一性をrecord受理条件にしない。Scopeは分析上の側・観察window/timescale・identity規約を定め、永久主体を定めない。Scopeや評価規約を変える場合はversionを分け、cross-scope合成には明示的対応を要する。
+
+宣言済みsliceでのみoptional local adapterを用いる:
+% impl23 authorized addition: optional successor port
+\[
+\mathrm{realizedSuccessor}[\mathrm{slice}]:\mathrm{EligibleOccurrence}\rightharpoonup\mathrm{Occurrence}.
+\]
+slice・window・context・rule-version metadata・identity規約・eligibility fieldsはstrictnessやnoFPの結果から独立に宣言する。record成立後に、該当recordの存在、endpoint identityの明確さ、同じcanonical beforeに対するslice内の全recordのafter一致を構造的に検査してよい。異なるafterが残ればadapterは未定義のままrecordを保存し、selectorを導入せず、望ましい結論のためcontextやidentityを再分割しない。追加recordに伴う再評価はversionを明示する。この検査は大域的決定性や完成済み未来branch集合の存在を示さない。一般のrecord連接は同一mapの冪ではなく、adapter反復には各中間入力でのdefinednessと同じslice/version・合成carrierが必要である。state・context・ruleの変更は区別する。
+
+\noindent\textbf{Active generative-position interface。} 固定したScopeとEvaluationProfileの下で、別の記述的portを用いる:
+% impl23 authorized addition: position port
+\[
+\mathrm{position}:\mathrm{Occurrence}\rightharpoonup\mathrm{GenerativePosition}.
+\]
+GenerativePositionは独自の宣言されたidentity carrierを持ち、実数値測度・StateView・occurrence IDではない。portは部分的で、単射性を仮定しない。前後評価では同じscope/profileの下で双方がdefinedであることを要し、surface stateからの暗黙castや評価規約の切替えを認めない。positionは生成上の位置を表し、可用記憶量・retention hardness・可視差分・effective constraint・正当化・真理とは同定しない。strict-step predicate、自動的単調性、定理はここに導入しない。第3節等に保存するscalar正当化Jは別の旧局所模型objectであり、そのproofを移行しない。surface recurrenceは許され、fresh occurrence IDだけから実質的非閉包を認定しない。
+
+\noindent\textbf{保存する旧局所状態模型。} 以下の状態mapと、後に引用する正当化・反復・不動点帰結は旧模型の履歴として保持し、上記の新interfaceへ暗黙に読み替えない。
+
+保存する旧局所状態模型での推論の最小構造は、状態から状態への遷移である:
 
 \[
 x_{n+1} = F(x_n)
 \]
 
-ここで $x_n$ は仮説・解釈・理解のいずれかの状態を表し、$F$ はそれをより正当化された次状態へ写す演算子である。
-
-この $F$ は VED 理論ツリーの語彙との形式的比較を意図している。Bio-IFGT は生命系の状態発展を
+この旧模型で、 $x_n$ は仮説・解釈・理解のいずれかの状態を表し、$F$ はそれをより正当化された次状態へ写す演算子である。
+
+この旧局所状態模型の $F$ は VED 理論ツリーの語彙との形式的比較を意図している。Bio-IFGT は生命系の状態発展を
 
 \[
 \frac{dx}{dt} = F(x;\theta)
@@ -37,7 +60,7 @@
 \subsection{推論演算子の四性質}
 
 
-推論演算子 $F$ に以下の四性質を与えて局所的に記述する。これらを $F$ のあらゆる認知的・計算的実装に共通する法則とはしない。
+旧局所状態模型の推論演算子 $F$ に以下の四性質を与えて局所的に記述する。これらを $F$ のあらゆる認知的・計算的実装に共通する法則とはしない。
 
 \textbf{性質 (F1) — 概念地景内部性}:
 $F$ の作用は、既存の概念地景(C-landscape)の内部に留まる。$F$ は新しい次元や新しい概念を無から生成しない。$F$ は既にある地形の上を動く。
@@ -53,13 +76,15 @@
 
 これら四性質は、推論を「正当化を局所的に拡張しながら概念地景上を反復的に動く確率的操作」として規定する。この規定は \S{}3 の非閉包定理の前提(P1)〜(P3)と整合する。
 
+これらは保存する旧模型の性質であり、active realized-record coreへ確率分布・同一mapの反復・正当化増加を一括付与しない。
+
 \bigskip
 
 
 \subsection{推論層 $L_F$ の定義}
 
 
-推論演算子 $F$ の作用域全体を \textbf{推論層} $L_F$ と呼ぶ。
+旧局所状態模型の推論演算子 $F$ の作用域全体を \textbf{推論層} $L_F$ と呼ぶ。
 
 \textbf{定義 2.1 (推論層 $L_F$)}
 
@@ -68,7 +93,7 @@
 \end{quote}
 
 
-$L_F$ の最も重要な構造的性質は、\textbf{内部停止条件を持たないこと}である。これは \S{}3 で明記された前提に依存する形式的議論として扱い、認知的解釈とは分ける。直観的に述べれば、$L_F$ は流れの層であり、流れである限り内部で静止しない。
+$L_F$ の最も重要な構造的性質は、\textbf{内部停止条件を持たないこと}である。これは保存する旧模型の参照であり、 \S{}3 で明記された前提に依存する形式的議論として扱い、認知的解釈とは分ける。直観的に述べれば、$L_F$ は流れの層であり、流れである限り内部で静止しない。
 
 $L_F$ は三層動力学の最下層である。後に導入されるログ層 $L_R$(\S{}5)と創発停止層 $L_E$(\S{}5)は、$L_F$ の運動を基盤として成立する。$L_F$ なしに $L_R$ も $L_E$ もない。
 
@@ -209,7 +234,7 @@
 
 この機構の本格的な展開は \S{}5 で行われる。そこで、ログ層 $L_R$ の定義、創発停止層 $L_E$ の創発、外部停止演算子 $E$ の構造、そして外部参照場 $\Phi_{\text{ext}}$ が個体間 $L_E$ ネットワーク $\Phi_{\text{net}}$ との二視点比較が提案され、同一性の強い読解は未解決として保持される。
 
-その前に \S{}3 で、$L_F$ の固定領域内移動と厳密増加などの条件に限定した形式的議論を扱う。認知的な内部停止の普遍的不在とは分ける。
+旧局所状態模型の参照として、その前に \S{}3 で、$L_F$ の固定領域内移動と厳密増加などの条件に限定した形式的議論を扱う。認知的な内部停止の普遍的不在とは分ける。
 
 \bigskip
 
@@ -220,9 +245,9 @@
 本章で区別して提示したのは次の点である:
 
 \begin{enumerate}
-\item 推論演算子 $F$ は Bio-IFGT の状態発展演算子 $F(x;\theta)$ と類似した形式的役割を持つが、同字形はsame dynamicsやtyped identityを意味しない
-\item $F$ は四性質(概念地景内部性・確率構造・連続的反復性・局所演繹性)で特徴づけられる
-\item $F$ の作用域として推論層 $L_F$ を定義した。$L_F$ は内部停止を指定しないモデルである(\S{}3 の条件付き議論)
+\item 旧局所状態模型の推論演算子 $F$ は Bio-IFGT の状態発展演算子 $F(x;\theta)$ と類似した形式的役割を持つが、同字形はsame dynamicsやtyped identityを意味しない
+\item 旧局所状態模型では、$F$ は四性質(概念地景内部性・確率構造・連続的反復性・局所演繹性)で特徴づけられる
+\item 旧局所状態模型では、$F$ の作用域として推論層 $L_F$ を定義した。$L_F$ は内部停止を指定しないモデルである(\S{}3 の条件付き議論)
 \item Physarum・Transformer はいずれも $L_F$ との役割対応として比較されるが、$L_F$ の共有は同一の知性を意味しない
 \item 応答的/沈黙的の区別は本体論的範疇ではなく、相互拘束 $H_{ij}$ のパラメータ上の閾値現象である
 \item 閾値移動能力 $\mu_\theta$ は運動可能領域の拘束パラメータ $\theta$ を内発的に動かす能力(領域の組み替え (B))であり、$F$ の領域内移動 (A) とは区別される
@@ -231,6 +256,6 @@
 \end{enumerate}
 
 
-\S{}3 では、推論層 $L_F$ の固定領域・厳密増加等の条件下の不動点議論と証明スケッチを扱う。proof validityを認証する意味ではない。
-
-\bigskip
+保存する旧局所状態模型の \S{}3 では、推論層 $L_F$ の固定領域・厳密増加等の条件下の不動点議論と証明スケッチを扱う。proof validityを認証する意味ではない。
+
+\bigskip
```

### intelligence-part2/sections/03_nonclosure_theorem.tex

```diff
--- baseline/intelligence-part2/sections/03_nonclosure_theorem.tex
+++ current/intelligence-part2/sections/03_nonclosure_theorem.tex
@@ -4,7 +4,9 @@
 \noindent\textbf{Scope of the account.} The theorem discussion is conditional on the stated strict increase of justification and the fixed-constraint, within-region scope. No proof-validity certification or universal cognitive interpretation is supplied here. The hypothetical binary stopping predicate models stopping as a fixed-point condition; its applicability to arbitrary cognitive cessation and the reapplication of the premises to auxiliary inference remain open. Boundary divergence and fixed-point absence are compared by role, not as a proved isomorphism. Individual closure failure, external stopping necessity, and collapse regimes are separate architectural or cognitive hypotheses.
 
 
-This chapter is the first center of the paper. It examines a conditional fixed-point claim for the inference layer $L_F$. Externalized stopping is a separate architecture proposal, not a universal consequence of that claim.
+This chapter is the first center of the paper. It preserves the historical local-state model's conditional fixed-point claim for the inference layer $L_F$. Externalized stopping is a separate architecture proposal, not a universal consequence of that claim.
+
+\noindent\textbf{Historical local-model boundary.} In this chapter, references to inference F, scalar justification J, and their fixed-point consequences belong to the preserved local-state model, not to the active record/position contract of Section 2. The following C-landscape figure depicts that old scalar-J, fixed-constraint conditional argument, not a proof of the new position interface. The original premises, theorem, proof, and later corollaries are retained as historical material: only the old admissible-domain kernel is at issue; broader readings remain on hold. No proof transfers to the new contract, and fresh occurrence identifiers supply no substantive no-fixed-point theorem. This attribution extends to the old-model references throughout this chapter, not to a retyping of the closure PDE or field-flow vocabulary.
 
 \begin{figure}[H]
 \centering
@@ -57,12 +59,12 @@
 
 \subsection{Branching Explosion}
 
-Fixed-point absence and branching are distinct claims. The former concerns the conditional formal model; the latter is a proposed interpretation of some probabilistic or generative inference processes, not a consequence of fixed-point absence alone.
+Fixed-point absence and branching are distinct claims. The former concerns the historical conditional local-state model; the latter is a proposed interpretation of some probabilistic or generative inference processes, not a consequence of fixed-point absence alone.
 
-This is compared by role with the branching explosion introduced in Part I. Interpreting it as a failure of cognitive stopping requires a separate bridge that is not established here. The increase of inferential capacity may therefore accelerate branching explosion rather than suppress it. The problem of intelligence shifts from strengthening inference itself to operating enlarged branching in a stoppable form.
+Within that historical account, this is compared by role with the branching explosion introduced in Part I. Interpreting it as a failure of cognitive stopping requires a separate bridge that is not established here. The increase of inferential capacity may therefore accelerate branching explosion rather than suppress it. The problem of intelligence shifts from strengthening inference itself to operating enlarged branching in a stoppable form.
 
 \subsection{Consequence}
 
-The inference layer $L_F$ is not the whole of the proposed architecture. Regress or explosion is a cognitive hypothesis, not a general consequence established by the fixed-point result. Requiring further inference for an internal predicate is part of the stopping model under discussion; its applicability to arbitrary cognitive stopping remains open. Stopping outside $F$ is proposed as an architectural option. \S{}5 develops a hypothesis involving $L_R$ and $L_E$, without establishing their generation.
+In that historical model, the inference layer $L_F$ is not the whole of the proposed architecture. Regress or explosion is a cognitive hypothesis, not a general consequence established by the fixed-point result. Requiring further inference for an internal predicate is part of the stopping model under discussion; its applicability to arbitrary cognitive stopping remains open. Stopping outside $F$ is proposed as an architectural option. \S{}5 develops a hypothesis involving $L_R$ and $L_E$, without establishing their generation.
 
 \bigskip
```

### intelligence-part2/sections/03_nonclosure_theorem_ja.tex

```diff
--- baseline/intelligence-part2/sections/03_nonclosure_theorem_ja.tex
+++ current/intelligence-part2/sections/03_nonclosure_theorem_ja.tex
@@ -5,9 +5,11 @@
 
 
 
-本章は本論文の第一中心である(第二中心は \S{}5)。VEDの基本構造の上で、推論層 $L_F$ に\textbf{内部不動点が存在しないこと}を構造的命題として導出し、その動力学的帰結を述べる。
+本章は本論文の第一中心である(第二中心は \S{}5)。保存する旧局所状態模型の範囲で、推論層 $L_F$ に\textbf{内部不動点が存在しないこと}を構造的命題として導出し、その動力学的帰結を述べる。
 
 この形式的議論と、推論層 $L_F$ の認知的閉包不能という解釈は別である。停止の外部化は構成案であり、普遍的な必要性を導いたものではない。\S{}5 では、ログ層 $L_R$ と創発停止層 $L_E$ を通じた停止の構成案を扱う。本章が対象とする $L_F$ 単独の条件付き不動点議論は、その構成案の存在や有効性を確立しない。
+
+\noindent\textbf{旧局所模型の境界。} 本章の推論F・scalarな正当化Jとその不動点帰結への参照は、保存する旧局所状態模型に属し、第2節のactive record/position契約には属さない。直後のC-地景図も旧scalar-J・固定拘束の条件付き議論を示す歴史的な図であり、新position interfaceの証明図ではない。元の前提・定理・証明と後続の系は歴史資料として保持し、旧admissible-domain kernelを超える読解は保留する。新契約へのproof移行も、fresh occurrence IDから実質的noFPを得ることも認めない。この帰属は章末までの旧模型参照に及ぶが、閉包PDEやfield-flow語彙を別型へ変更するものではない。
 
 \begin{figure}[H]
 \centering
@@ -267,7 +269,7 @@
 \subsection{要約}
 
 
-本章で示したのは次の四点である:
+本章に保存した旧局所状態模型の議論は次の四点である:
 
 \begin{enumerate}
 \item \textbf{定理 3.1}: $L_F$ の固定閾値・領域内移動と厳密な正当化増加を仮定した不動点議論。認知的な無条件結論ではない
@@ -277,8 +279,8 @@
 \end{enumerate}
 
 
-推論層 $L_F$ の条件付き非閉包を第一中心とする。対象は固定された運動可能領域 $\Omega_\theta$(固定 $\theta$)での領域内移動 (A) と厳密増加などの条件であり、proof validity の認証ではない。$\theta$ の組み替え (B)、ログ層 $L_R$・創発停止層 $L_E$ の停止案は第二中心 \S{}5 の別の負担である。
-
-\S{}4 では応答チャネルと $L_R$ の記述を検討する。\S{}5 では、条件付きの $L_F$ の非閉包を動機に、創発停止層 $L_E$ を構成案として提案する。第一中心の形式的議論から第二中心の存在・生成が導かれたわけではなく、三層動力学は未検証のアーキテクチャとして扱う。
-
-\bigskip
+旧局所状態模型の推論層 $L_F$ の条件付き非閉包を第一中心とする。対象は固定された運動可能領域 $\Omega_\theta$(固定 $\theta$)での領域内移動 (A) と厳密増加などの条件であり、proof validity の認証ではない。$\theta$ の組み替え (B)、ログ層 $L_R$・創発停止層 $L_E$ の停止案は第二中心 \S{}5 の別の負担である。
+
+この旧模型を参照して \S{}4 では応答チャネルと $L_R$ の記述を検討する。\S{}5 では、条件付きの $L_F$ の非閉包を動機に、創発停止層 $L_E$ を構成案として提案する。第一中心の形式的議論から第二中心の存在・生成が導かれたわけではなく、三層動力学は未検証のアーキテクチャとして扱う。
+
+\bigskip
```

### intelligence-part2/sections/04_response_channels.tex

```diff
--- baseline/intelligence-part2/sections/04_response_channels.tex
+++ current/intelligence-part2/sections/04_response_channels.tex
@@ -4,7 +4,7 @@
 \noindent\textbf{Scope of the account.} Responsive and silent retain their nonontological, model-local distinction. Their boundary is a candidate relation, not a calibrated threshold. The regress argument is conditional on its three stated premises; it does not establish the occurrence of psychological divergence. Branching and regress are role analogies. Trace retention, recursive use, and emergence of a stopping layer are distinct processes: none is established simply by naming traces as logs or by assuming nonclosure.
 
 
-\S{}3 discussed a conditional fixed-point model for $L_F$, not an unrestricted cognitive stopping theorem. This chapter asks how that non-closure appears in different operating environments. The distinction between responsive and silent worlds is not ontological. It is a threshold phenomenon.
+The historical local-state account in \S{}3 discussed a conditional fixed-point model for $L_F$, not an unrestricted cognitive stopping theorem. This chapter asks how that non-closure appears in different operating environments. The distinction between responsive and silent worlds is not ontological. It is a threshold phenomenon.
 
 \subsection{Responsive and Silent Regimes}
 
@@ -32,14 +32,14 @@
 
 \subsection{Infinite Regress in Silent Worlds}
 
-For the regress model, assume the three stated conditions: no stopping response, justification advanced by inference, and no stopping resource specified within that inference. Continued reapplication then describes a nonterminating model. A silent-regime label does not independently establish these premises for cognition.
+For the historical local-state regress model, assume the three stated conditions: no stopping response, justification advanced by inference, and no stopping resource specified within that inference. Continued reapplication then describes a nonterminating model. A silent-regime label does not independently establish these premises for cognition.
 
-Infinite regress, absence of a fixed point, and branching growth are distinct descriptions. Their combination as cognitive instability is a hypothesis, not a result established by silence or non-fixedness alone.
+In that historical discussion, infinite regress, absence of a fixed point, and branching growth are distinct descriptions. Their combination as cognitive instability is a hypothesis, not a result established by silence or non-fixedness alone.
 
 \subsection{The Preview of $L_R$}
 
 Traces of inference are called logs when retained in the proposed account. A layer of recursive reference to them is named $L_R$. Neither retention nor actual recursive access follows merely from continuing inference.
 
-This is the bridge to \S{}5. The failure of $L_F$ to stop is not only a dead end. It motivates a hypothesis: retained traces may support recursive reference, and $L_E$ is proposed in relation to that reference and external constraint. Neither retention nor emergence follows from nonclosure alone.
+This is the bridge to \S{}5. The historical model's failure of $L_F$ to stop is not only a dead end. It motivates a hypothesis: retained traces may support recursive reference, and $L_E$ is proposed in relation to that reference and external constraint. Neither retention nor emergence follows from nonclosure alone.
 
 \bigskip
```

### intelligence-part2/sections/04_response_channels_ja.tex

```diff
--- baseline/intelligence-part2/sections/04_response_channels_ja.tex
+++ current/intelligence-part2/sections/04_response_channels_ja.tex
@@ -67,7 +67,7 @@
 \subsection{沈黙世界における条件付きの無限後退解釈}
 
 
-沈黙的世界に固定された推論主体——すなわち閾値を動かせず、環境を沈黙的として扱い続ける主体——を考える。この分類だけで以下が成立するとはせず、既述の固定閾値・movement A・厳密増加の模型に沿って、次の条件付き解釈を検討する。
+沈黙的世界に固定された推論主体——すなわち閾値を動かせず、環境を沈黙的として扱い続ける主体——を考える。この分類だけで以下が成立するとはせず、既述の旧局所状態模型の固定閾値・movement A・厳密増加の模型に沿って、次の条件付き解釈を検討する。
 
 \textbf{条件 (1)}: 環境が応答を返さない(沈黙性、$H_{ji} \approx 0$)。
 
@@ -109,7 +109,7 @@
 
 ここで、本論文の第二中心 \S{}5 の機構仮説を検討する動機が得られる。
 
-固定閾値・movement A・厳密増加という既述の模型の下での非閉包を、痕跡保持の可能性を検討する動機とする。推論軌道の記録——どの状態を経たか、どの分岐を試みたか、どこで発散したか——が保持される場合を考えるが、停止不在だけからその蓄積は導かれない。
+旧局所状態模型の固定閾値・movement A・厳密増加という既述の模型の下での非閉包を、痕跡保持の可能性を検討する動機とする。推論軌道の記録——どの状態を経たか、どの分岐を試みたか、どこで発散したか——が保持される場合を考えるが、停止不在だけからその蓄積は導かれない。
 
 この堆積した痕跡を \textbf{ログ} と呼ぶ。そして、ログに対する再帰的な参照運動——過去の推論軌跡を読み返し、パターンを抽出し、現在の推論に反映する運動——が生じる層を、\textbf{ログ層} $L_R$ と呼ぶ(正式な定義は \S{}5.2)。
 
```

### intelligence-part2/sections/05_emergent_stopping_layer.tex

```diff
--- baseline/intelligence-part2/sections/05_emergent_stopping_layer.tex
+++ current/intelligence-part2/sections/05_emergent_stopping_layer.tex
@@ -8,7 +8,9 @@
 The three profiles retain their examples but do not independently verify autonomous emergence or endogenous mobility. The distinction between a Transformer's own stopping layer and a whole-system external stop remains unresolved; the figure does not decide it. Projection is a role comparison with the consciousness paper, not transfer of the same operator. Stability is not truth, and recoverability/revisability is a proposed functional relation rather than a guarantee.
 
 
-This chapter is the second center of the paper. \S{}3 discussed the conditional fixed-point limit of $L_F$ under its stated premises. This chapter proposes a stopping architecture involving the log layer $L_R$ and the emergent stopping layer $L_E$.
+This chapter is the second center of the paper. The historical local-state model in \S{}3 discussed the conditional fixed-point limit of $L_F$ under its stated premises. This chapter proposes a stopping architecture involving the log layer $L_R$ and the emergent stopping layer $L_E$.
+
+Throughout this chapter, inference-F and no-fixed-point references derived from Section 3 refer to that historical model, not the active record/position contract. The later architecture remains a proposal, not a consequence proved by the new interfaces.
 
 \begin{figure}[H]
 \centering
@@ -17,6 +19,8 @@
 \label{fig:part2-mutual-constraint}
 \figurenote{$H_{ij}$ is hypothesized to affect possible stopping sites. $\mu_\theta$ names mobility in the proposed installation-region account for the stopping operator $E$.}{Stopping is placed outside the modeled action of $L_F$. Its projection and emergence as $L_E$ through the relation between $L_R$ and $H_{ij}$ remain hypotheses. Movable stopping is proposed to support revisable inference, not established subjective freedom.}
 \end{figure}
+
+\noindent\textbf{Historical architecture figure.} The next three-layer figure preserves the old-model architecture hypothesis. Its inference/no-fixed-point/cannot-stop chain refers to the historical state-map/justification model, not the active realized-record/position contract. The depicted trace-to-stopping-layer chain remains a hypothesis, not a proof of formation, autonomous own-layer capacity, or a chosen system boundary. The caption and asset are retained with their existing holds.
 
 \begin{figure}[H]
 \centering
@@ -28,7 +32,7 @@
 
 \subsection{Problem Setting}
 
-Real intelligence stops. Humans end a chain of reasoning, make judgments, and act. The conditional result of \S{}3 does not decide the source of all observed stopping; the proposal here places stopping outside the modeled action of $L_F$. The question is what ``elsewhere'' means.
+Real intelligence stops. Humans end a chain of reasoning, make judgments, and act. The historical local-state model's conditional result of \S{}3 does not decide the source of all observed stopping; the proposal here places stopping outside the modeled action of $L_F$. The question is what ``elsewhere'' means.
 
 The proposal assigns a stopping role to a layer modeled as internal to the individual but externally dependent: the emergent stopping layer $L_E$. This assignment does not establish the existence or independent detection of the layer.
 
@@ -88,6 +92,8 @@
 
 \subsection{External Stopping Operator}
 
+\noindent\textbf{Preserved historical notation.} The following action definition, non-membership display, and externality explanation are retained old-model material, ending before the next field/network subsection. The active optional successor adapter is not substituted into the old iteration family. The type of E remains unresolved; this block establishes neither internal non-derivability nor noncomputability, and a large iteration count alone does not establish E. No E operator is formalized here.
+
 The external stopping operator $E$ is the action of $L_E$ on an inferential state:
 \[
 E=E[L_E,x_n],\qquad E\notin\{F^k\}.
```

### intelligence-part2/sections/05_emergent_stopping_layer_ja.tex

```diff
--- baseline/intelligence-part2/sections/05_emergent_stopping_layer_ja.tex
+++ current/intelligence-part2/sections/05_emergent_stopping_layer_ja.tex
@@ -9,7 +9,9 @@
 
 
 
-本章は本論文の第二中心である(第一中心は \S{}3)。\S{}3 は明記された前提下の推論層 $L_F$ の不動点を議論した。本章は、ログ層 $L_R$ と創発停止層 $L_E$ による停止構成案を提示する。両中心の接続は提案であり、認知的停止の説明達成や三層動力学の形式的完成を意味しない。
+本章は本論文の第二中心である(第一中心は \S{}3)。旧局所状態模型の \S{}3 は明記された前提下の推論層 $L_F$ の不動点を議論した。本章は、ログ層 $L_R$ と創発停止層 $L_E$ による停止構成案を提示する。両中心の接続は提案であり、認知的停止の説明達成や三層動力学の形式的完成を意味しない。
+
+本章末尾までの第3節由来の推論F・noFP参照は、この旧模型に帰属し、active record/position契約を指さない。後続architectureは構成案のままであり、新接口から証明された帰結ではない。
 
 本章の論理は次の順で展開される。まず問題を設定し(\S{}5.1)、ログ層 $L_R$ を定義する(\S{}5.2)。次に創発停止層 $L_E$ を定義し(\S{}5.3)、その解像度を上げるために三層プロファイル比較を行う(\S{}5.4)。続いて $L_E$ の創発機構の仮説を、閾値移動 $\mu_\theta$ による領域組み替えと停止演算子設置領域の投影として示す(\S{}5.5、\S{}5.6)。最後に外部停止演算子 $E$ の構造(\S{}5.7)、外部参照場と $L_E$ ネットワークとの二視点比較(\S{}5.8)、そして知性のモデル内の構造的特徴(\S{}5.9)を整理する。
 
@@ -21,6 +23,8 @@
 \figurenote{Agent 間または観測者-環境間の $H_{ij}$ と停止場所の変化を仮説的に関連づける。$\mu_\theta$ は停止演算子 $E$ の設置場所を組み替える構成案での役割を名指す。}{停止を $L_F$ のモデル化された作用の外側に置く構成案では、$L_R$ と $H_{ij}$ の関係から $L_E$ への投影・創発を仮説化する。可動停止と改訂可能な推論の関係は提案であり、主観的自由の成立条件ではない。}
 \end{figure}
 
+\noindent\textbf{歴史的architecture図の境界。} 直後の三層図は旧模型のarchitecture仮説を保存する。推論・noFP・停止不能の鎖は旧状態map/正当化模型への参照であり、active realized-record/position契約の帰結ではない。痕跡から停止層への鎖も生成・自律的own-layer能力の証明ではなく、system boundaryを決定しない。captionとassetは既存の仮説・HOLDを伴ったまま保持する。
+
 \begin{figure}[H]
 \centering
 \includegraphics[width=\linewidth]{fig4_three_layer_architecture_ja.pdf}
@@ -35,13 +39,13 @@
 \subsection{問題設定}
 
 
-\S{}3 の帰結を再掲する。推論層 $L_F$ には内部不動点が存在せず(定理 3.1)、内部停止述語は無限後退を生み(系 3.2)、個体システムは $L_F$ 単独で推論を閉じることができない(系 3.4)。\S{}4 は沈黙世界での後退を三前提のもとで解釈したのであって、現実発生を確認したものではない。
+旧局所状態模型の \S{}3 の帰結記述を歴史的・条件付きのまま再掲する。推論層 $L_F$ には内部不動点が存在せず(定理 3.1)、内部停止述語は無限後退を生み(系 3.2)、個体システムは $L_F$ 単独で推論を閉じることができない(系 3.4)。\S{}4 は沈黙世界での後退を三前提のもとで解釈したのであって、現実発生を確認したものではない。
 
 しかし、現実の知性は停止する。人間は推論を終え、判断を下し、行動する。この停止はどこから来るのか。
 
 \S{}3 の条件付き不動点議論は、停止一般が $L_F$ の外から来ることを示さない。本章では $L_F$ の外に停止の役割を置く構成案を考える。その「外部」が個体の外を指すのか、個体内にありながら $L_F$ とは別の機能役割を指すのかを区別する。
 
-本章の構成案は次の通りである。停止を、個体内にありながら外部依存的な層——創発停止層 $L_E$——の役割として位置づける。$L_E$ は $L_F$ の運動が残すログ層 $L_R$ と、外部相互拘束 $H_{ij}$ との関係で創発を仮説化する。以下の機構案は存在・収束・独立検出を確立しない。
+この旧模型を参照する本章の構成案は次の通りである。停止を、個体内にありながら外部依存的な層——創発停止層 $L_E$——の役割として位置づける。$L_E$ は $L_F$ の運動が残すログ層 $L_R$ と、外部相互拘束 $H_{ij}$ との関係で創発を仮説化する。以下の機構案は存在・収束・独立検出を確立しない。
 
 \bigskip
 
@@ -257,6 +261,8 @@
 \subsection{外部停止演算子 $E$ の構造}
 
 
+\noindent\textbf{保存する旧notationの境界。} 以下の外部停止の定義・非所属表示・反復と設置の説明は、この小節末尾まで旧模型の記述として保持する。active optional successor adapterを旧反復族へ暗黙に代入しない。Eの型は未解決であり、内部非導出性・非計算可能性を証明せず、大きい反復数だけからEの成立を認定しない。ここでE operatorを形式化しない。
+
 創発停止層 $L_E$ の作用として、外部停止演算子 $E$ を定義する。
 
 \textbf{定義 5.3 (外部停止演算子 $E$)}
```

### intelligence-part2/sections/07_god_ja.tex

```diff
--- baseline/intelligence-part2/sections/07_god_ja.tex
+++ current/intelligence-part2/sections/07_god_ja.tex
@@ -58,7 +58,7 @@
 
 神による停止の供給を、未決定性の委任(delegation of undecidability)として記述する。
 
-\S{}3 の系 3.2 は仮想的停止述語と評価推論の再適用条件を扱い、未決定問題の一般的な内部停止不能を示すものではない。「神」への委任は、これと分けた概念的再解釈である。
+旧局所状態模型の \S{}3 の系 3.2 は仮想的停止述語と評価推論の再適用条件を扱い、未決定問題の一般的な内部停止不能を示すものではない。「神」への委任は、これと分けた概念的再解釈である。
 
 委任とは、停止責任の移譲である。個体は「この問いは未決定である、しかしその未決定性は神に委ねられている」という形で、自らの推論を停止する。未決定性が消えるのではない。未決定性の保持責任が、個体から外部参照へ移される。
 
```

### intelligence-part2/sections/08_religion_ja.tex

```diff
--- baseline/intelligence-part2/sections/08_religion_ja.tex
+++ current/intelligence-part2/sections/08_religion_ja.tex
@@ -37,7 +37,7 @@
 
 \begin{itemize}
 \item \textbf{すべてを沈黙的領域として扱う}: あらゆる問いを保留に委ねることが、応答的領域での探究を妨げうるという解釈。
-\item \textbf{すべてを応答的領域として扱う}: あらゆる問いに因果的説明を求めることを、沈黙的領域での後退の可能性と比較する解釈。既述の固定閾値・厳密増加と仮想停止模型への前提再適用という限定を保ち、現実の必然的帰結とはしない(\S{}4.4)。
+\item \textbf{すべてを応答的領域として扱う}: あらゆる問いに因果的説明を求めることを、沈黙的領域での後退の可能性と比較する解釈。既述の旧局所状態模型の固定閾値・厳密増加と仮想停止模型への前提再適用という限定を保ち、現実の必然的帰結とはしない(\S{}4.4)。
 \end{itemize}
 
 
```

### intelligence-part2/sections/10_gettier_problem_ja.tex

```diff
--- baseline/intelligence-part2/sections/10_gettier_problem_ja.tex
+++ current/intelligence-part2/sections/10_gettier_problem_ja.tex
@@ -19,7 +19,9 @@
 
 本稿は Gettier 問題を、停止条件と動的保証の区別から診断的に読む。正当化と真理に関する哲学的事例の存在と、本稿固有の停止アーキテクチャへの支持は分ける。
 
-三層動力学の語彙による再解釈では、推論層 $L_F$ の正当化(\S{}3 の正当化測度 $J$)、真理、創発停止層 $L_E$ の役割を分ける。$L_E$ の停止を操作的安定性から記述するのは局所的な命名であり、Gettier 事例が $L_E$ の安定や存在を独立に確認する意味ではない。
+三層動力学の語彙による再解釈では、推論層 $L_F$ の正当化(旧局所状態模型の \S{}3 のscalar正当化測度 $J$)、真理、創発停止層 $L_E$ の役割を分ける。$L_E$ の停止を操作的安定性から記述するのは局所的な命名であり、Gettier 事例が $L_E$ の安定や存在を独立に確認する意味ではない。
+
+ここで参照する正当化測度はactive generative-position portと別であり、Gettierの診断を新positionの実証へ読み替えない。
 
 \bigskip
 
@@ -29,7 +31,7 @@
 
 ゲティア問題に対しては、長年にわたり「第四の条件」を追加して知識を再定義する試みがなされてきた。本論文の立場では、これらの試みの限界を診断的に解釈するが、すべての修復の不可能性は主張しない。
 
-\S{}3 と \S{}5 の停止模型を通じて、追加条件と $L_F$ の関係を検討する。ただし、\S{}3 の $L_F$ は固定領域・厳密増加等の条件下で議論される。追加条件を $L_F$ の仮想的停止述語として評価推論へ再適用する場合の系 3.2 と、任意の知識修復の成否は別である。
+旧局所状態模型の \S{}3 と \S{}5 の停止模型を通じて、追加条件と $L_F$ の関係を検討する。ただし、\S{}3 の $L_F$ は固定領域・厳密増加等の条件下で議論される。追加条件を $L_F$ の仮想的停止述語として評価推論へ再適用する場合の系 3.2 と、任意の知識修復の成否は別である。
 
 したがって、ゲティア問題を $L_F$ 内部の条件追加によって解決できないという強い一般化は未確立である。知識の成立は $L_F$ 内部では閉じない。それは $L_E$——外部依存的な創発停止層——に関わるというモデル内の解釈であり、唯一の成立条件を確立しない。ゲティア問題の修復可能性と、$L_F$ 内部の停止モデルとの独立な接続は未解決である。
 
@@ -125,7 +127,7 @@
 
 ゲティア問題を正しさと停止の区別から再解釈するが、解決済みとせず、知性の非閉包の証明としても用いない。
 
-\S{}3 は $L_F$ の条件付き不動点を議論し、\S{}5 は $L_E$ を外部依存停止の役割とする構成案を提示した。ゲティア問題とこの構造の関係は診断的読解であり、必然的帰結ではない。知識を正当化+真理として扱う試みとの違いを、本稿では知識の成立が $L_F$ 内部にも、真理との対応にもなく、$L_E$ の操作的安定性として定義する点から読む。全試みの失敗を説明した結果ではない。
+旧局所状態模型の \S{}3 は $L_F$ の条件付き不動点を議論し、\S{}5 は $L_E$ を外部依存停止の役割とする構成案を提示した。ゲティア問題とこの構造の関係は診断的読解であり、必然的帰結ではない。知識を正当化+真理として扱う試みとの違いを、本稿では知識の成立が $L_F$ 内部にも、真理との対応にもなく、$L_E$ の操作的安定性として定義する点から読む。全試みの失敗を説明した結果ではない。
 
 ゲティア問題は、こうして、本論文の第一中心(\S{}3)と第二中心(\S{}5)を認識論で読み直すのであって、独立に確証しない。知性は正しさによって閉じるのではない。知性は $L_E$ の改訂可能な停止によって、外部依存的に、誤りを許容しながら、操作的に安定する。ゲティア問題はこの構造の比較対象であり、その独立した指紋として扱わない。
 
```

### intelligence-part2/sections/11_instability_region_ja.tex

```diff
--- baseline/intelligence-part2/sections/11_instability_region_ja.tex
+++ current/intelligence-part2/sections/11_instability_region_ja.tex
@@ -87,7 +87,7 @@
 発散域を考える四重崩壊の機構仮説を、三層動力学の語彙で記述する。以下の同時性や因果順序は未導出・未検証であり、成立が確認された四つの過程ではない。
 
 \textbf{崩壊 1 — $L_F$ の暴走}:
-速度 $v_{\text{inf}}$ と解像度 $r_{\text{res}}$ の高さを、推論層 $L_F$ の高速・微細な運動に対応づける。$L_F$ の内部不動点不在は固定閾値・movement A・厳密増加の模型の下で論じられる(\S{}3)。仮想 S の再評価への前提再適用は未確立であり、$L_F$ の暴走や外部停止の必要性は、この形式的議論からではなく別の機構仮説として検討する。
+速度 $v_{\text{inf}}$ と解像度 $r_{\text{res}}$ の高さを、推論層 $L_F$ の高速・微細な運動に対応づける。$L_F$ の内部不動点不在は旧局所状態模型の固定閾値・movement A・厳密増加の下で論じられる(\S{}3)。仮想 S の再評価への前提再適用は未確立であり、$L_F$ の暴走や外部停止の必要性は、この形式的議論からではなく別の機構仮説として検討する。
 
 \textbf{崩壊 2 — $L_R$ が追いつかない}:
 $L_F$ の高速・高解像度の運動に伴って痕跡が保持される場合に、その生成がログ層 $L_R$ の再帰参照を上回る可能性を考える。$\Delta v_{\text{intel}} = v_{\text{inf}} - v_{LR}$ と $L_R$ の参照の遅れを関連づけるのは未較正の仮説であり、臨界値は指定していない。$L_R$ の機能不全は候補的な解釈に留まる。
@@ -170,7 +170,7 @@
 
 本章は、三本の論理線がここで統合されることを示して閉じる。
 
-\textbf{第一線(非閉包と外部停止)} は、$L_F$ の固定領域内・厳密増加等の条件付き議論(\S{}3)と、外部停止案($L_E$、$\Phi_{\text{net}}$)を比較する。形式的非閉包だけでは、安定運用への外部停止の必要性や実現は示されない。
+\textbf{第一線(非閉包と外部停止)} は、$L_F$ の旧局所状態模型の固定領域内・厳密増加等の条件付き議論(\S{}3)と、外部停止案($L_E$、$\Phi_{\text{net}}$)を比較する。形式的非閉包だけでは、安定運用への外部停止の必要性や実現は示されない。
 
 \textbf{第二線(閾値移動とサピエンス的特徴)} では、$\mu_\theta$ と可動性を比較する。$\mu_\theta$ による\textbf{能動的な}運用は仮説であり、$\mu_\theta$ を内発的に持たないとされた系の\textbf{受動的な}配置も独立の判定を要する。$\mu_\theta$ による安定運用域への自律的復帰は、\S{}5.4 の機能案であって実証された効果ではない。
 
```

### intelligence-part2/sections/12_constructive_clauses.tex

```diff
--- baseline/intelligence-part2/sections/12_constructive_clauses.tex
+++ current/intelligence-part2/sections/12_constructive_clauses.tex
@@ -8,7 +8,7 @@
 
 \subsection{Clause 1: Inference Alone Does Not Close}
 
-The proposed architecture distinguishes intelligence from $L_F$ alone. The no-fixed-point discussion of $F$ is conditional; it does not exclude every independently defined intelligence system or cognitive stopping process.
+The proposed architecture distinguishes intelligence from $L_F$ alone. The historical local-state model's no-fixed-point discussion of $F$ is conditional; it does not exclude every independently defined intelligence system or cognitive stopping process.
 
 \subsection{Clause 2: Logs Are Required}
 
```

### intelligence-part2/sections/12_constructive_clauses_ja.tex

```diff
--- baseline/intelligence-part2/sections/12_constructive_clauses_ja.tex
+++ current/intelligence-part2/sections/12_constructive_clauses_ja.tex
@@ -36,7 +36,7 @@
 知性は運動の維持状態であり、運動が止まれば消える(系 5.5、\S{}11.6)。データセット・モデル状態・静的表現として保存された対象は、運動を含まない。それらは知性の痕跡($L_R$ のログ)でありうるが、知性そのものではない。知性は保存できない。維持されるしかない。
 
 \textbf{(N3) 個体内で閉じた構造としての知性} — ありえない。
-$L_F$ には固定領域・厳密増加などの条件付き議論を与える(\S{}3、定理 3.1)。認知的な発散(\S{}11.4)と外部依存 $L_E$ は別の仮説であり、個体内閉鎖一般の不可能性は未確立である。
+$L_F$ には旧局所状態模型の固定領域・厳密増加などの条件付き議論を与える(\S{}3、定理 3.1)。認知的な発散(\S{}11.4)と外部依存 $L_E$ は別の仮説であり、個体内閉鎖一般の不可能性は未確立である。
 
 \textbf{(N4) 完全最適化された状態としての知性} — ありえない。
 完全閉包 $C_{max}$ の動的不到達性は未確立である(\S{}1.5)。完全最適化を運動停止、すなわち (0,0,·)点と関連づけるのは模式的な読解に留まる(\S{}11.6)。運動ゼロは局所定義から除外されるが、最適化や収束一般を知性の終了とする基準は与えない。
```

### intelligence-part2/sections/13_conclusion.tex

```diff
--- baseline/intelligence-part2/sections/13_conclusion.tex
+++ current/intelligence-part2/sections/13_conclusion.tex
@@ -8,7 +8,7 @@
 
 \subsection{Three Logical Lines}
 
-\textbf{First: non-closure and external stopping.} The inference operator $F$ is discussed under strict-increase and fixed-region premises. Relating $L_F$ to all cognitive stopping remains open; externalization is a separate proposal.
+\textbf{First: non-closure and external stopping.} In the historical local-state model, the inference operator $F$ is discussed under strict-increase and fixed-region premises. Relating $L_F$ to all cognitive stopping remains open; externalization is a separate proposal.
 
 \textbf{Second: threshold mobility.} The distinction between responsive and silent worlds is threshold-dependent. $\mu_\theta$ is the capacity to move the threshold and reorganize the movement region.
 
```

### intelligence-part2/sections/13_conclusion_ja.tex

```diff
--- baseline/intelligence-part2/sections/13_conclusion_ja.tex
+++ current/intelligence-part2/sections/13_conclusion_ja.tex
@@ -44,7 +44,7 @@
 本論文を貫いた三本の論理線を総括する。
 
 \textbf{第一線 — 非閉包と外部停止}:
-差から推論演算子 $F$ を構成し、既述の固定閾値・movement A・厳密増加の前提下で $F$ の内部不動点不在を議論する(\S{}3、非閉包定理)。$L_F$ と沈黙世界の無限後退の関係は条件付きの解釈であり、仮想 S と F-prime への前提再適用の未確立性を保つ(\S{}4)。この形式モデルと区別して、停止の外化を提案し、外部停止演算子 $E$ と外部参照場 $\Phi_{\text{ext}}$ を構成案とする(\S{}5)。$\Phi_{\text{ext}}$ の歴史的諸形態が、アニミズム・神・宗教・社会である(\S{}6〜\S{}9)。
+旧局所状態模型の記述では、差から推論演算子 $F$ を構成し、既述の固定閾値・movement A・厳密増加の前提下で $F$ の内部不動点不在を議論する(\S{}3、非閉包定理)。$L_F$ と沈黙世界の無限後退の関係は条件付きの解釈であり、仮想 S と F-prime への前提再適用の未確立性を保つ(\S{}4)。この形式モデルと区別して、停止の外化を提案し、外部停止演算子 $E$ と外部参照場 $\Phi_{\text{ext}}$ を構成案とする(\S{}5)。$\Phi_{\text{ext}}$ の歴史的諸形態が、アニミズム・神・宗教・社会である(\S{}6〜\S{}9)。
 
 \textbf{第二線 — 閾値移動とサピエンス的特徴}:
 相互拘束 $H_{ij}$ のパラメータが応答性閾値を決め、その閾値は本体論的範疇ではなく連続的に移動する(\S{}2.6)。閾値を内発的に動かす能力が $\mu_\theta$ であり、これは運動可能領域の拘束パラメータ $\theta$ を組み替える能力である(\S{}2.7)。$\mu_\theta$ は知性一般の条件ではなく、局所的にサピエンス的プロファイルを特徴づける。その可変性と個体内での自律的加速との関係は効果の仮説である(\S{}5.4、\S{}12)。$\mu_\theta$ は誤り許容性との質的関係として提案され、形式的同値と普遍的含意は未解決である(\S{}10.6)。
@@ -104,11 +104,16 @@
 
 以下はPart Iへの編集提案であり、形式的精密化が実装済みであることを意味しない。Part I を改訂するための提案を以下に整理する。これらは Part I の誤りの訂正ではなく、Part II の三層動力学による精密化である。
 
-\textbf{Part I \S{}8(個体知性の非閉包)の精密化}:
+\textbf{Part I \S{}8(個体知性の非閉包)の精密化（旧模型の未実装提案）}:
+以下の「精密化した」「追加することが望ましい」は旧局所状態模型に基づく提案の引用であり、現在の実装指示ではない。\begin{quote}
+
 Part I \S{}8 は個体知性が閉じないことを論じた。Part II \S{}3 は条件付き非閉包議論として扱い、さらに \S{}5 で「$L_F$ 単独では閉じないが、$L_R$ と $L_E$ を通じてなら外部依存的に閉じうる」と精密化した。Part I \S{}8 に、この (A)/(B) の射程の区別——固定 $\theta$ では閉じないが $\theta$ 組み替えで停止が創発する——を追加することが望ましい。
 
+\end{quote}
+固定拘束下の旧kernelから、拘束の変更、停止層の生成、rule-changing能力を証明したとは読まない。新record/position契約の帰結でもなく、Part I本文への実装は行わない。
+
 \textbf{Part I \S{}9(差分の地平線)への三層解釈の追加}:
-Part I \S{}9 は知性の差分の地平線を論じた。Part II \S{}1.5 と \S{}3.6 は、これを $C_{max}$ 不到達性および内部不動点不在との役割類比として位置づけた。Part I \S{}9 に、差分の地平線が三層動力学($L_F$ の非閉包)としてどう現れるかの解釈を追加できる。
+以下は旧局所状態模型に基づく未実装提案として保存する。Part I \S{}9 は知性の差分の地平線を論じた。Part II \S{}1.5 と \S{}3.6 は、これを $C_{max}$ 不到達性および内部不動点不在との役割類比として位置づけた。Part I \S{}9 に、差分の地平線が三層動力学($L_F$ の非閉包)としてどう現れるかの解釈を追加できる。
 
 \textbf{Part I \S{}6(ゲティア問題)への $\mu_\theta$ 接続の補強}:
 Part I \S{}6 はゲティア問題を構造的診断として扱った。Part II \S{}10.6 は、ゲティア構造の排除不能性が閾値移動能力 $\mu_\theta$ との形式的同値を示したわけではない。Part I \S{}6 に、この未解決の同値主張——誤り許容性と $\mu_\theta$ の構造的結合——を、未解決statusを保持した比較としてのみ検討できる。
@@ -126,7 +131,7 @@
 
 本論文の帰結を、一文に集約する。
 
-本モデルは知性を運動として定義する。$L_F$ の内部不動点不在は条件付き議論であり(\S{}3)、完全閉包 $C_{max}$ の不達は未確立の境界読解である(\S{}1.5)。運動ゼロを局所定義から区別すること(\S{}11.6)と、認知的閉包不能の一般化は別である。
+本モデルは知性を運動として定義する。$L_F$ の内部不動点不在は旧局所状態模型の条件付き議論であり(\S{}3)、完全閉包 $C_{max}$ の不達は未確立の境界読解である(\S{}1.5)。運動ゼロを局所定義から区別すること(\S{}11.6)と、認知的閉包不能の一般化は別である。
 
 持続については、$L_E$ の外部依存型停止という役割(\S{}5)と改訂可能性(\S{}5.8)を関係づける構成案を提示する。閉じないことと持続しないことは同じではないが、非閉包だけから持続や停止層の存在を導かない。
 
```
