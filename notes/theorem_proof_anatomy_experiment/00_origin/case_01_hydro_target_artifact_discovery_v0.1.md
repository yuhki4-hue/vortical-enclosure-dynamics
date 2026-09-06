# Case 01 Hydro — 対象アーティファクト探索 v0.1

## 地点固有の洪水推定値・対象用途・監査準備可能性

## 状態

- **段階:** アーティファクト探索のみ
- **親ケース:** `validation_basis_transition_case_01_hydro_feasibility_v0.1.md`
- **親研究計画:** `validation_basis_transition_working_note_v0.1.md`
- **日付:** 2026-08-21
- **目的:** 監査可能な地点固有のsource–target連鎖が存在するかを確認する
- **監査実施:** なし
- **positive / negative判定:** この段階では禁止
- **materiality判定:** 未実施
- **bridge adequacy判定:** 未実施

このファイルは検索台帳であり、論証ではない。歴史的な洪水推定値と将来計画を結ぶ筋の通った物語だけでは不十分である。探索対象は、地点固有のsource estimate、日付の確定したtarget artifact、特定された用途を結ぶ、文書で確認可能な連鎖である。

> 読みやすい表を作っただけでは成功としない。この段階の成功条件は、後のtime-sliced auditに必要な文書を実際に特定・取得できるかを確定することである。

---

## 1. 探索上の問い

適否や欠落をまだ判定せず、以下をすべて特定できる連鎖が少なくとも一件存在するか。

1. 地点固有の歴史的な洪水頻度推定値
2. その推定値を使用または引用した、日付の確定した計画・設計・規制・意思決定アーティファクト
3. 対象用途および想定された供用期間
4. 移送された内容が経験的主張、規範的ルール、または文書上その両者を含むものか
5. 下記`q1–q5`に対応するsourceとtargetの条件
6. 固定した同時代文献cutoffまでに利用可能だった文献
7. アーティファクトまたは参照先文書が主張するbridge
8. そのbridgeが実際に何を被覆するかを後で検査するために必要な文書

このファイルで許される結果は、次の検索状態だけである。

- **探索手掛かり:** アーティファクト群またはアーカイブは特定したが、source–target連鎖は未確定
- **部分的連鎖:** 必要要素の一部は接続できたが、少なくとも一つの必須文書が欠けている
- **文書一式を確認した候補:** 最小文書集合を取得できる見込みがあるが、監査は未着手
- **アーカイブ欠落:** 必須文書は特定したが、取得不能または不完全
- **非連鎖として終了:** 取得した文書からはsource estimateからtarget useへの再利用関係を確認できない

これらは探索状態であり、科学的判定ではない。

---

## 2. 探索単位

最小単位は、次の一つの候補連鎖である。

```text
地点固有の水文記録／分析
    → 日付の確定した洪水頻度推定値
    → 日付の確定した対象アーティファクト
    → 明記された計画・設計・規制・運用上の用途
```

Bulletin 17B、stationarity、気候変動、氾濫原管理、設計基準への一般的な言及だけでは連鎖を構成しない。

可能な限り、以下を区別する。

- ある地点について実際に算出された数値的または確率的推定値
- その推定値の使用法を指定するルール
- そのルールを適用する下流の意思決定
- 推定値に対する後年の再解釈

---

## 3. 経験的主張と規範的ルールの区別

すべての候補を暫定的に次のいずれかへ分類する。

- **経験的主張:** 洪水規模、年超過確率、頻度関係、その他の系の性質に関する命題
- **規範的ルール:** 推定値からどのような設計・ゾーニング・安全・規制・受容判断を行うべきかを指定するルール
- **混合:** アーティファクトが経験的推定値と規範的意思決定ルールを含み、現段階では両者を明確に分離できない
- **不明:** 文書からはまだ分類できない

「年超過確率1%の洪水」を用いる設計ルールは、将来の物理的な超過確率が正確に1%のまま保たれるという経験的主張を自動的には意味しない。後の監査では、用語の連続性だけを根拠として経験的主張が移送されたと推論してはならない。

---

## 4. 暫定的な`q1–q5`探索項目

`q1–q5`は検索用の問いであり、普遍的な水文学的分解ではない。その妥当性は、後にfield-nativeな水文学と実際のアーティファクトに照らして確認する必要がある。

| コード | 文書内で探す条件 | 探索段階の問い |
|---|---|---|
| `q1` | 統計記録と標本抽出の基礎 | source estimateを支える記録、期間、独立性・同質性の扱い、分布推定手順、不確かさの記述は何か。 |
| `q2` | 流域・水理構成 | 土地利用、流域状態、河道改変、流量調節、貯水池運用、その他の流域特性について、どのような仮定または記述があるか。 |
| `q3` | 洪水生成条件と気候条件 | 降水、融雪、嵐の型、気候強制、季節性、その他の洪水生成機構について、どのような仮定または記述があるか。 |
| `q4` | 対象期間を通じた確率推定値 | 適合された超過確率・頻度関係はtarget periodへどのように引き継がれているか。時間依存性、シナリオ依存性、期間上の制限は記載されているか。 |
| `q5` | 意思決定用途・信頼性・適応 | 推定値は、設計信頼性、安全余裕、不確かさの許容、robustness、監視、更新、adaptive decision ruleとどのように結び付けられているか。 |

各コードについて、この段階ではsource文書とtarget文書が記述・引用している内容、または検索上まだ解決していない内容だけを記録する。差がmaterialかどうかはまだ判定しない。

---

## 5. 各候補連鎖の必須項目

| 項目 | 記録内容 | 探索上の規則 |
|---|---|---|
| Chain ID | `HYD-A01`のような固定識別子 | IDを再利用しない。 |
| Selection reason / discovery route | なぜ、どの経路で当該アーティファクトへ到達したか | omission疑いを確認する前に記録し、後から上書きしない。 |
| 地点固有のsource estimate | 地点、観測所・流域、量、数値的推定値または参照分析、記録期間、手法、source文書 | 一般的手順だけでは不十分。 |
| アーティファクトの日付 | 版、発行日、承認日、意思決定日 | 版履歴があれば保存する。 |
| 対象用途 | 正確な計画・設計・規制・運用上の用途と想定期間 | タイトルだけから用途を推測しない。 |
| 主張／ルール種別 | 経験的主張／規範的ルール／混合／不明 | 分離できる場合は両層を記録する。 |
| `q1–q5` | 各条件についてのsource記述、target記述、文書内位置 | 「未発見」はまだ「存在しない」を意味しない。 |
| 同時代文献cutoff | 後のtime-sliced corpusに採用する最終日候補 | 原則としてアーティファクトの版または意思決定日に結び付け、2008年を自動採用しない。 |
| 主張されたbridge | アーティファクトが援用する分析、基準、シナリオ、傾向モデル、安全係数、感度分析、adaptive rule、scope statement、参照文書 | 適否を判断せず、アーティファクト自身の主張を記録する。 |
| 実際のbridge coverage | bridgeの明記されたdomainと制約を確定するために必要な文書・正確な節 | この段階では、記述内容を抽出しただけの場合を除き`未評価`とする。 |
| アーティファクトの取得状況 | 全文公開／一部のみ／metadataのみ／所在判明・取得不能／取得申請中 | URL、アーカイブ、識別子、取得日を記録する。 |
| omission疑いの状態 | 下記の統制語彙による検索状態のみ | positive / negative判定やmaterialityラベルを付けない。 |

### 「omission疑いの状態」の統制語彙

- `未調査`
- `関連箇所を未発見`
- `条件への言及あり・bridgeは未追跡`
- `bridge／参照先を発見・coverageは未評価`
- `開示状況不明・監査が必要`
- `探索時の読みではomissionを疑う根拠なし・監査は未実施`
- `source–target連鎖を確認できないため非該当`

「未発見」は、常に**今回の検索作業では未発見**という意味である。完全な記録中に存在しないことを意味しない。

### Selection reason / discovery routeの統制語彙

| Selection route | 内容 | 後の用途に関する制約 |
|---|---|---|
| `source-first` | 地点固有のsource estimateを起点として、下流のtarget artifactを追跡した | confirmatory sample候補になりうる。 |
| `target-first` | 設計・計画・意思決定アーティファクトを起点として、使用されたsource estimateを逆追跡した | confirmatory sample候補になりうるが、targetの選定理由を別途固定する。 |
| `archive-sampled` | 事前に定めたarchiveまたはsample frameから、固定手順で抽出した | confirmatory sampleに最も適する候補。抽出母集団と規則を保存する。 |
| `known-failure-derived` | 後世に知られたfailure、controversy、改訂、訴訟、事故等から過去のアーティファクトを逆引きした | discoveryには使用可。confirmatory sampleには使用しない。 |
| `convenience` | 入手しやすい公開文書から選択した | 探索・手順確認には使用可。代表性を主張せず、confirmatory useには別途根拠が必要。 |
| `other—prespecified` | 上記以外の経路を、検索前に具体的に記述した | 経路と採用規則を原文のまま保存する。 |

同じ連鎖へ複数経路から到達した場合は、**最初に候補化した経路**をprimary routeとして記録し、後続経路をsecondary routeとして追記する。後世のfailureを知っていたかどうかも別欄または検索ログに記録する。

---

## 6. 候補連鎖台帳

地点固有の推定値、対象アーティファクト、対象用途、日付、取得可能なsource–target接続がすべて揃うまで、どの行も`文書一式を確認した候補`へ昇格させない。

| Chain ID | Selection reason / discovery route | 地点固有のsource estimate | アーティファクトの日付 | 対象用途 | 経験的主張／規範的ルール | `q1` | `q2` | `q3` | `q4` | `q5` | 同時代文献cutoff | 主張されたbridge | 実際のbridge coverage | 取得状況 | omission疑いの状態 | 探索状態 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `HYD-A01` | `source-first`。Bulletin 17B準拠の地点別USGS報告書から下流引用を追跡 | USGS SIR 2006–5323。Duck Creek観測所15053200の加重推定値：10% AEP 70.9、4% 92.7、2% 110、1% 128、0.2% 175 ft³/s | Source: 2007。2013年DFIRM有効化を公式ページで確認。取得済みFISは2020-09-18改訂版 | JuneauのFIS/FIRMにおける洪水保険料率設定・氾濫原管理。建設用途ではFISとFIRMの併用を注意書き | 混合 | 1994–2004年の観測記録＋地域回帰式による加重。FISは同じ観測所・期間を掲載 | Sourceは現況の橋梁・カルバートを調査。FISは都市化の影響を注記 | 関連記述の範囲を未追跡 | SourceのAEP推定をFIS discharge／flood profileへ使用。2020 FISは調査完了時の現況に限定し、将来変更時の改訂を明記 | FISは1%+ uncertainty、保険、氾濫原管理、建設利用上の注意を記載 | 2013版を対象とする場合は2013-08-19候補。取得済み文書を対象とする場合は2020-09-18 | USGS SIR 2006–5323、NHC 2008 detailed riverine mapping、FEMAのhydrologic／hydraulic analysis | 未評価。2020 FISのscope・uncertainty・urbanization記述は発見済み | Source全文、2020 FIS全文、州Risk MAP履歴を取得。2013 FIS全文とNHC 2008全文は未取得 | 条件への言及あり・bridgeは未追跡 | アーカイブ欠落を伴う部分的連鎖（2013版）。2020年target artifactは取得済み |
| `HYD-A02` | 未設定 | 未特定 | 未特定 | 橋梁またはカルバート設計。正確なアーティファクトは未特定 | 不明 | 未調査 | 未調査 | 未調査 | 未調査 | 未調査 | 未設定 | 未特定 | 未評価 | 検索未着手 | 未調査 | 探索手掛かり |
| `HYD-A03` | 未設定 | 未特定 | 未特定 | 貯水池計画または信頼性判断。正確なアーティファクトは未特定 | 不明 | 未調査 | 未調査 | 未調査 | 未調査 | 未調査 | 未設定 | 未特定 | 未評価 | 検索未着手 | 未調査 | 探索手掛かり |

これらの行は検索経路にすぎない。具体的な地点、推定値、対象アーティファクトが接続されるまでは候補ケースではない。

---

## 7. 連鎖ごとの資料シート

### Chain `HYD-A01` — Duck Creek / Jordan CreekからJuneau FIS/FIRMへ

#### 識別情報

| 項目 | 記録 |
|---|---|
| Primary selection route | `source-first` |
| Selection reason（候補化前に記録） | pre-2008のBulletin 17B準拠USGS報告書であり、地点固有推定値、観測所、洪水profile、下流のmapping目的が明記され、全文取得できたため。 |
| Secondary discovery route（該当する場合） | 取得容易性の点では`convenience`要素あり。ただしtarget artifactはsource title／report numberの前向き引用検索で発見した。 |
| 候補化時に後世のfailureを知っていたか | この地点固有の既知failureを起点としていない。一般的なstationarity論争は既知。 |
| 地点／流域／観測所 | Duck Creek below Nancy Street near Auke Bay, Alaska（USGS 15053200）。同報告書にはJordan Creek below Egan Drive near Auke Bay（15052475）も含む。 |
| Source estimateと単位 | Duck Creekの加重peak streamflow：10% AEP 70.9、4% 92.7、2% 110、1% 128、0.2% 175 ft³/s。 |
| Source recordの期間 | Duck Creek 1994–2004。Jordan Creek 1996–2005。 |
| Sourceの手法／基準 | 観測所データにBulletin 17B／PEAKFQを適用した推定と、Alaska地域回帰式による推定の加重。 |
| Source文書と該当箇所 | Janet H. Curran, *Hydrology and Flood Profiles of Duck Creek and Jordan Creek Downstream from Egan Drive, Juneau, Alaska*, USGS SIR 2006–5323（2007）、Table 2。 |
| Target artifactの表題 | FEMA, *Flood Insurance Study Report, City and Borough of Juneau, Alaska*, FIS 02110CV000B（取得版）。 |
| 発行主体 | Federal Emergency Management Agency。関連Risk MAP履歴はState of Alaska DCRAが公開。 |
| アーティファクトの版と日付 | 取得版は2020-09-18改訂、Version 2.3.3.4i。州公式履歴ではlegacy Map Modernization DFIRMが2013-08-19に発効。 |
| 対象用途 | Flood hazard dataを保険料率設定およびcommunity floodplain managementへ使用。建設・氾濫原管理ではFISの標高データとFIRMの併用を指示。 |
| 想定供用期間／意思決定期間 | 固定供用年数は未特定。FISは30年mortgageおよび90年期間の累積risk例を示すが、これは個別施設のdesign lifeではない。 |
| 直接のsource–target引用または組込み経路 | 2020 FISの参考文献Table 32がUSGS SIR 2006–5323をReference 10として掲載。FIS Table 12は同一観測所と記録期間、Table 10はDuck/Jordan CreekのAEP別discharge、flood profilesはFIRM用水位を掲載。 |
| 主張／ルール種別 | 混合。AEP別discharge・flood elevationは経験的推定、FIRM zone・保険・氾濫原管理への使用は規範的／制度的ルール。 |

#### `q1–q5`文書一覧

| コード | Source文書の記述＋該当箇所 | Target artifactの記述＋該当箇所 | 組み込まれた参照先 | 検索メモのみ |
|---|---|---|---|---|
| `q1` | SIR Table 1–2、Methods of Analysis。Duck Creek 1994–2004のannual peak、観測所推定のconfidence limits、地域回帰、equivalent years、加重推定を記載。 | FIS Table 12に観測所15053200と1994–2004、Table 10にAEP別discharge、Figure 7にgage analysisを掲載。 | Bulletin 17B、PEAKFQ、Alaska地域回帰報告書。 | 記録・手法の対応は確認。2013版での記載は未確認。 |
| `q2` | 2004年開始の調査が新しいstreamflow data、channel change、engineered structure changeを受け、29 culvertsと15 bridgesを調査したと記載。 | Duck Creek流域と支流がurbanizationの影響を受けること、hydraulic structureが閉塞せず適切に動作する場合のみprofileが有効であることを記載。 | USGS hydraulic model、NHC 2008 mapping study、archived project documentation。 | 言及は発見済み。bridge coverageは未評価。 |
| `q3` | 降水・融雪・気候強制等について、後の監査に必要な範囲をまだ抽出していない。 | 同左。 | 未追跡。 | 関連箇所を未発見。absence判定ではない。 |
| `q4` | Table 2が2–500年recurrence interval／AEPの加重推定を提示。 | FISは10–500年floodを管理・保険上重要とし、分析はstudy completion時のcommunity conditionsを反映し、将来変化を受けperiodically amendすると記載。 | FEMA engineering/mapping procedure。 | 2013版で同じscope文が存在したか未確認。 |
| `q5` | Sourceの目的はfloodplain map更新を支えるhydrologic／hydraulic analysis。 | FISは1%+ profileで追加discharge uncertaintyを表示し、保険、氾濫原管理、建設利用、map revision手続きを記載。 | FIS/FIRM、LOMC/LOMR、CNMS、archived project documentation。 | 意思決定との接続は確認。adequacyは未評価。 |

#### Bridgeと取得状況の一覧

| 項目 | 記録 |
|---|---|
| Target artifactが主張するbridge | USGS SIR 2006–5323のhydrologic／hydraulic results、NHC 2008のdetailed riverine floodplain mapping、FEMAのFIS/FIRM engineering workflow。 |
| 正確な文言／節 | FIS §1.2、§2、§5.0–5.2、Tables 10–13、Table 32 References、Flood Profiles。 |
| Bridgeのsource文書 | USGS SIR 2006–5323全文は取得済み。NHC 2008 *Hydrology for Detailed Riverine Floodplain Mapping, Juneau, Alaska*はFISで特定したが、独立全文は未取得。 |
| Bridgeに明記されたscope | 2020 FISはstudy completion時のcommunity conditionsを反映すると記載。建設・氾濫原管理ではFISとFIRMの併用を指示。hydraulic profileは構造物が閉塞せず正常動作する場合に限定。 |
| Bridgeに明記された制約 | 1%+ uncertainty、Duck Creek urbanization、Jordan Creekの短いgage record、回帰式のdrainage-area範囲外、将来変更時のmap amendment等を発見。 |
| Coverageの状態 | 未評価。記述抽出のみ。 |
| 同時代文献cutoff | 2013版targetを取得できた場合は2013-08-19を候補とする。2020版をtargetとする場合は2020-09-18。後の事前登録で固定する。 |
| Target artifact全文の取得可否 | 2020 FIS全文は取得可能。2013 FIS/FIRM一式は公式履歴上特定したが、今回の検索ではFIS全文未取得。 |
| Source analysis全文の取得可否 | USGS SIR 2006–5323全文・HTML tablesを取得可能。 |
| 組み込まれた参照文書の取得可否 | Bulletin 17Bは取得可能。NHC 2008報告書およびarchived project documentationは未取得。 |
| 意思決定記録／承認記録の取得可否 | 州公式ページで2013 DFIRM発効と2020 Risk MAP手続を確認。2013 adoption／approval recordの完全な一式は未取得。 |
| アーカイブ欠落 | 2013 FIS版、NHC 2008 technical report、当時のproject archive。 |
| Omission疑いの状態 | 条件への言及あり・bridgeは未追跡。 |
| 探索状態 | 2013 time sliceについては部分的連鎖。2020 target artifactについては主要文書を取得済みだが、bridge sourceの一部が未取得。 |

**この記録は監査結果ではない。** 現時点では、source estimateがFEMA FIS/FIRMへ組み込まれたことと、後の監査に必要な文書の所在・欠落を記録しただけである。

### 再利用用の空欄テンプレート

具体的な別アーティファクトを発見した後にのみ、以下を複製する。

### Chain `HYD-___`

#### 識別情報

| 項目 | 記録 |
|---|---|
| Primary selection route |  |
| Selection reason（候補化前に記録） |  |
| Secondary discovery route（該当する場合） |  |
| 候補化時に後世のfailureを知っていたか |  |
| 地点／流域／観測所 |  |
| Source estimateと単位 |  |
| Source recordの期間 |  |
| Sourceの手法／基準 |  |
| Source文書と該当箇所 |  |
| Target artifactの表題 |  |
| 発行主体 |  |
| アーティファクトの版と日付 |  |
| 対象用途 |  |
| 想定供用期間／意思決定期間 |  |
| 直接のsource–target引用または組込み経路 |  |
| 主張／ルール種別 |  |

#### `q1–q5`文書一覧

| コード | Source文書の記述＋該当箇所 | Target artifactの記述＋該当箇所 | 組み込まれた参照先 | 検索メモのみ |
|---|---|---|---|---|
| `q1` |  |  |  |  |
| `q2` |  |  |  |  |
| `q3` |  |  |  |  |
| `q4` |  |  |  |  |
| `q5` |  |  |  |  |

#### Bridgeと取得状況の一覧

| 項目 | 記録 |
|---|---|
| Target artifactが主張するbridge |  |
| 正確な文言／節 |  |
| Bridgeのsource文書 |  |
| Bridgeに明記されたscope |  |
| Bridgeに明記された制約 |  |
| Coverageの状態 | 未評価 |
| 同時代文献cutoff |  |
| Target artifact全文の取得可否 |  |
| Source analysis全文の取得可否 |  |
| 組み込まれた参照文書の取得可否 |  |
| 意思決定記録／承認記録の取得可否 |  |
| アーカイブ欠落 |  |
| Omission疑いの状態 | 未調査 |
| 探索状態 |  |

stationarity、materiality、bridge adequacy、開示、意思決定への影響に関する結論を、このシートへ記載してはならない。

---

## 8. 監査準備可能性の判定ゲート

次の必須検索質問すべてに**はい**と回答できる場合に限り、別ファイルでの事前登録済み監査へ進める。

| 必須検索質問 | はい／いいえ／不明 |
|---|---|
| 地点固有の推定値を特定できるか。 |  |
| 推定値のsource analysisまたは十分な同時代の再構成資料を取得できるか。 |  |
| 日付の確定したtarget artifactを特定・取得できるか。 |  |
| 対象用途が、文脈からの推測だけでなく明示されているか。 |  |
| 経験的主張と規範的ルールの層を区別できるか、または明示的に混合と記録できるか。 |  |
| `q1–q5`に関係するsourceとtargetの記述を、全文または十分に完全な記録から検索できるか。 |  |
| Source–targetの組込み経路が文書化されているか。 |  |
| 後の結果を参照せずに同時代文献cutoffを固定できるか。 |  |
| 主張されたbridgeとそのsource文書を取得できるか。 |  |
| 独立したreviewerが同じ連鎖を再構成できるだけの文書があるか。 |  |
| Selection reason / discovery routeがomission判定前に記録されているか。 |  |

このゲートの通過は事前登録への移行を許可するだけであり、基礎となるtransition仮説を支持しない。

なお、`known-failure-derived`の連鎖は探索資料またはhistorical benchmark候補にはできるが、confirmatory sampleには昇格させない。

---

## 9. 検索ログ

| 日付 | 検索領域／アーカイブ | 検索語または取得経路 | 発見したアーティファクト／識別子 | Chain ID | 次の取得作業 |
|---|---|---|---|---|---|
| 2026-08-21 | 初期台帳の作成 | アーティファクト検索は未実施 | なし | — | 地点固有の推定値を起点として、それを使用した実際のtarget artifactを前向きに追跡する。 |
| 2026-08-21 | USGS Publications／FEMA MSC／Alaska Risk MAP | 公式USGSのpre-2008 Bulletin 17B準拠報告書を探索し、SIR 2006–5323のtitle/report numberを前向き引用検索 | USGS SIR 2006–5323、FEMA FIS 02110CV000B、2013 DFIRM履歴 | `HYD-A01` | 2013 FIS版、NHC 2008 technical report、archived project documentationの取得可否を追跡する。 |
| 2026-08-21 | FEMA MSC／Alaska DCRA／公開ウェブ | `02110CV000A`、2013 effective date、NHC 2008報告書の正確な表題を検索 | 2013 DFIRMの発効事実と2020 FISへの組込みは再確認。2013 FIS全文およびNHC 2008独立全文は未発見 | `HYD-A01` | `HYD-A01`をアーカイブ欠落を伴う部分的連鎖として保持し、次のsource-first系統へ移るかを判断する。 |

### 9.1 今回取得・確認した一次／公式資料

- [USGS SIR 2006–5323 — report index](https://pubs.usgs.gov/sir/2006/5323/)
- [USGS SIR 2006–5323 — Table 2, site-specific peak-streamflow estimates](https://pubs.usgs.gov/sir/2006/5323/table2.html)
- [FEMA Flood Insurance Study 02110CV000B — City and Borough of Juneau](https://map1.msc.fema.gov/data/02/S/PDF/02110CV000B.pdf)
- [State of Alaska — City and Borough of Juneau Risk MAP Study and map history](https://www.commerce.alaska.gov/web/dcra/ResiliencePlanningLandManagement/RiskMAP/CityandBoroughofJuneauRiskMAPStudy)

上記リンクの列挙はavailability記録であり、bridge adequacyまたはomission statusの判定ではない。

---

## 10. この段階の凍結境界

この探索ファイルには、以下を記載しない。

- stationarityが有効だった、または無効だったという判定
- `q1–q5`がmaterialに変化したという判定
- bridgeが適切だった、または不適切だったという判定
- 開示が十分だった、または欠落していたという判定
- 親研究計画に関するpositive / negative判定
- field-native reviewerとの比較結果
- あるアーティファクトがimplementation failure、institutional under-enforcement、field-level conceptual absenceに該当するという主張

これらは、後に別途事前登録する監査の問題である。文書一式を確認した候補が見つからなければ、この段階の正しい結果は、監査可能な連鎖を確立できなかったということだけである。

---

## v0.1で確立するもの

- 検索に限定した分析単位
- 地点固有のsource estimateと日付の確定したtarget artifactのための統制された一覧項目
- selection biasを後から監査するためのSelection reason / discovery route記録
- 経験的主張と規範的ルールの明示的な区別
- field-nativeな水文学文書を検索するための暫定的な`q1–q5`
- ケースを先取りしない監査準備可能性ゲート

## v0.1で確立しないもの

- materialなvalidation-basis changeが起きたこと
- omissionが存在したこと
- 主張されたbridgeが不適切であること
- Case 01がpositiveまたはnegativeであること
- 一般的なsource–target protocolがfield-nativeな水文学レビューを上回ること

## 次の作業

地点固有の洪水頻度推定値を一つ特定し、日付の確定した一つのtarget artifactにおける文書上の使用まで追跡する。最小文書連鎖が監査準備可能性ゲートを通過するまでは、事前登録にも監査にも進まない。
