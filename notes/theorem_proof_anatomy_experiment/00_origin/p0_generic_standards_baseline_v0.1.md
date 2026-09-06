# P0 — Generic Standards Baseline

## Null D をケースとして実行した結果

- **バージョン:** 0.1
- **日付:** 2026-08-21
- **種別:** baseline coding result / kill test
- **設計文書:** [`qualification_practices_comparative_study_design_v0.1.md`](./qualification_practices_comparative_study_design_v0.1.md) Part III-2, VIII-2
- **対象ノート:** [`hydrology_negative_knowledge_preservation_note_v0.2.md`](./hydrology_negative_knowledge_preservation_note_v0.2.md)

---

## 0. 目的と停止規則（事前登録どおり）

設計文書 Part VIII-2 で事前に定めた問い。

> ISO/IEC Directives Part 1 の systematic review 規定と、任意の非科学的技術標準 1 件に、`NONEVAL`（未評価の明示）、`OPEN`（未解決課題リスト）、`RET-DOWN`（下流からの上流制限）、`DELEG`（他機関への委譲）は現れるか。

事前の予測（Part VIII-2、原文）。

> **予想:** `VER`、`RET`、`TRIG`、`DEV`、`DOC` は確実に立つ。`NONEVAL` と `OPEN` は立たない可能性がある（標準は通常、未解決課題リストを本文に持たない）。`RET-DOWN` と `DELEG` は不明。したがって P0 の後に残りうるのは、12 コード中せいぜい 4 コードである。

停止規則。

> 全コードが立つなら P1 へ進まず、Part X を D に確定する。

**結果:** 14 コード中 10 が立った。全コードではないため自動終了はしない。ただし後述のとおり、残存候補は実質 1 コードである。

---

## 1. 資料と選定経路

### D1 — ISO/IEC Directives（meta-standard）

| 項目 | 内容 |
|---|---|
| 文書 A | ISO/IEC Directives, Part 1: *Procedures for the technical work*, 4th edition, 2001, 61 pp. |
| 文書 B | ISO/IEC Directives Supplement — *Procedures specific to IEC*, Edition 16.0, 2022-05, 98 pp. |
| 取得経路 | 公式 iso.org / iec.ch は 403。ミラー経由で取得（Part 1: wg5-fortran.org、IEC Sup: agenturacas.gov.cz） |
| 選定理由 | Codex adversarial review が Null D の根拠として名指しした対象。設計文書が baseline に指定 |
| 限界 | **Part 1 は 2001 年版であり最新版ではない。** 現行版では systematic review 規定が本体に統合されている可能性がある。IEC Supplement は 2022 年版で現行に近い |

### D2 — 任意抽出した非科学的技術標準

| 項目 | 内容 |
|---|---|
| 文書 | IETF RFC 9110, *HTTP Semantics*, STD 97, June 2022, R. Fielding / M. Nottingham / J. Reschke (Eds.) |
| 取得経路 | rfc-editor.org 全文（502,941 bytes） |
| **選定経路** | **`convenience`。** 事前規則「全文が自由に取得でき、非科学的技術領域で、要件または手順を規定し、認知された標準化団体が発行したもの」に合致するものから取得可能なものを選んだ |
| **選定時の予備知識（開示）** | RFC が `Obsoletes:` / `Updates:` ヘッダを持つことは既知だった。したがって **`VER` と `RET` が立つことは選定前に予期していた。** 一方、`NONEVAL` と `OPEN` が現れるかは選定前に知らなかった |
| 限界 | **一団体（IETF）の一文書である。** IETF は「rough consensus and running code」の文化を持ち、ISO/ASTM 型の標準とは運用が異なる。技術標準一般の代表とはみなせない |

---

## 2. Coding result

設計文書 Part V の 12 コード + v0.2 で追加した 2 コード。判定は本文の語と条項の直接確認による。

| Code | 内容 | D1 ISO/IEC | D2 RFC 9110 | Generic か |
|---|---|---|---|---|
| `FIX` | 運用上固定された量・手順・推奨 | ✓ 手続が "shall" | ✓✓ `MUST NOT` ×72、`SHOULD NOT` ×28 | **YES** |
| `UNC` | 不確かさの限定 | ✗ 語彙なし | ✗ 語彙なし | 判定不能（§4-b） |
| `SCOPE` | 適用条件・適用範囲 | △ "outside the scope" ×1 | ✓✓ "outside the scope" ×7 | **YES** |
| `NONEVAL` | **未評価の明示** | **✗** | **✗** | **NO** |
| `OPEN` | 未解決課題の記録 | **✓✓ 下記 §3** | ✗ "open issue" ×0 | **YES** |
| `DEV` | 逸脱条件と逸脱時の要求 | ✓ 異議申立手続（cl.5） | △ `MAY`、誤り処理の裁量 | **YES** |
| `TRIG` | 更新・再検討の契機 | ✓✓ stability period / review / review date / stability date | ✗ 文書内にはない（IETF プロセス側） | **YES** |
| `DOWN` | 下流の意思決定規則 | — 該当層なし | — 該当層なし | 判定不能（§4-b） |
| `VER` | 版関係 | ✓✓ 版・改正・技術正誤票 | ✓✓ ヘッダに機械可読な `Obsoletes:` `Updates:` | **YES** |
| `RET` | 退役・撤回・置換 | ✓✓ review 四結果に withdrawal を含む | ✓✓ 二形式（§3-C） | **YES** |
| `REF` | 参照連鎖 | ✓ | ✓✓ 規範的参照 | **YES** |
| `DOC` | 文書化要求 | ✓✓ review report、反対票の理由書、archive 義務 | ✓ IANA レジストリ要求 | **YES** |
| `RET-DOWN` | 下流文書による上流標準の制限 | ✗ | ✗ | **判定不能**（§4-c） |
| `DELEG` | 他機関・他文書への委譲 | ✓ maintenance agencies（2.11）、registration authorities（2.12） | ✓✓ IANA レジストリ（cl.16） | **YES** |

**集計:** 14 コード中、**10 が generic baseline で再現された。** 再現されなかったのは 4 コード（`UNC`, `NONEVAL`, `DOWN`, `RET-DOWN`）。

---

## 3. 決定的な所見

### A. `OPEN` は generic である。しかも Bulletin 17B より形式化されている

ISO/IEC Directives Supplement（IEC）Edition 16.0, 2022-05, **clause 2.7.2**:

> "A National Body may submit comments on positive FDIS votes that are useful solely for the TC/SyC during the next systematic review. These comments are to be noted as **'Non-actionable – Comments preserved for historical record only'**. The Office of the CEO **shall** electronically archive the 'non-actionable' comments."

これは次のすべてを備えている。

1. **公式カテゴリ名**（"Non-actionable – Comments preserved for historical record only"）。
2. **保存の義務**（"shall electronically archive"）。
3. **指定された将来用途**（"during the next systematic review"）。
4. **保存主体の指定**（Office of the CEO）。

**Bulletin 17B の Future Studies リストは、これらのうち 1 と 3 を非形式的に満たすのみである。** 保存義務も保存主体の指定もない。

さらに clause 2.9.1 は maintenance 機構を定義語彙として持つ。

> `stability period`（publication が変更されない期間）／ `review`（使用状況と保守必要性の評価）／ `review date` ／ `maintenance` ／ `maintenance team (MT)` ／ `stability date`（委員会決定（withdrawal, confirmation, amendment, revision）が実施された時点）／ `review report (RR)`

**結論:** 水文学ノート v0.1 が「常設の未解決問題台帳」として当該系列に固有と見た形式は、**技術標準運用の一般形式であり、しかも ISO/IEC 側の方が形式化の程度が高い。** v0.1 §7-A の固有性主張は棄却される。

### B. `NONEVAL` は generic baseline に現れなかった

両文書とも、次の語の出現は 0 回だった。

| 語 | D1 (Part 1 2001) | D1 (IEC Sup 2022) | D2 (RFC 9110) |
|---|---|---|---|
| "not evaluated" / "not been evaluated" | 0 | 0 | 0 |
| "not considered" | 0 | 0 | — |
| "unresolved" | 0 | 0 | — |
| "further study" | 0 | — | — |
| "open issue" | 0 | 0 | 0 |

**ただし重要な区別がある。** RFC 9110 は "does not define" を 8 回、"outside the scope" を 7 回使う。例:

> "HTTP **does not define** specific error handling mechanisms except when they have a direct impact on security, since different applications of the protocol require different error handling strategies."

> "HTTP **does not define** exactly how a PUT method affects the state of an origin server beyond what can be expressed by the intent of the user agent request..."

これらは **specification boundary**（ここでは規定しない）であって、**evaluation status**（調べていないので分からない）ではない。Bulletin 17C の

> "The Work Group **did not evaluate** methods to account for watershed changes and makes no particular recommendations, as additional work is needed in this area."

は、規定しない理由が**未評価**であることを述べている。RFC の "does not define" は、規定しない理由が**設計上の意図的な委譲**（アプリケーションごとに異なる戦略が必要）であることを述べている。

**この区別が P0 の主要な残存所見である。** 一方は「決めていない」、他方は「調べていない」。

### C. `RET` の二形式（generic 側でより機械化されている）

RFC 9110 の退役形式は二つある。

1. **ヘッダレベル・機械可読:** `Obsoletes: 2818, 7230, 7231, 7232, 7233, 7235, 7538, 7615, 7694` / `Updates: 3864`。9 件の先行 RFC を一括退役させる。
2. **本文レベル・理由つき:** 「Accept-Charset is deprecated because UTF-8 has become nearly ubiquitous and sending a detailed list of user-preferred charsets wastes bandwidth, increases latency, and makes passive fingerprinting far too easy」

**Bulletin 17C の Plate 1 退役（水文学ノート NK-05）は形式 2 に相当し、形式 1 に相当する機械可読な退役関係は持たない。** すなわちこの点でも generic 側の方が形式化されている。

---

## 4. P0 の設計上の欠陥（自己申告）

### (a) Part 1 が 2001 年版

現行版を取得できなかった。ただし IEC Supplement 2022 が現行に近く、決定的所見（§3-A）はそちらに由来するため、結論への影響は限定的と判断する。

### (b) `UNC` と `DOWN` は判定不能だった — P0 の構造的欠陥

D1・D2 はいずれも**推定値を産出しない標準**である。ISO/IEC Directives は手続規定、RFC 9110 はプロトコル仕様であり、どちらも不確かさを伴う量を推定しない。

したがって `UNC`（不確かさの限定）と `DOWN`（下流の意思決定規則）の不在は、**分野の差ではなく artifact type の差**で説明される。これは設計文書 Part VII の **Null A そのもの**であり、P0 の baseline 選定がこの二コードを検査できない構造になっていた。

**教訓:** baseline には「推定値を産出する非科学的技術標準」を含めるべきだった。該当例（例えば材料試験規格や構造設計規格）は有料であり本調査では取得していない。

### (c) `RET-DOWN` は検査されていない

D1 は meta-standard、D2 は単一仕様文書であり、**いずれも上流標準に制限を課す下流規制ガイダンス層を持たない。** したがって `RET-DOWN` の不在は「存在しない」ではなく「検査していない」である。

`RET-DOWN` を検査するには、L2（標準）と L3（運用ガイダンス）の両方を持つ generic 系列が必要である。

### (d) D2 が一団体の一文書

IETF の文化は ISO/ASTM 型と異なる。特に IETF は Internet-Draft 段階で "Open Issues" 節を持つ慣行があり、**公開 RFC に "open issue" がないことは、当該文化における編集規約の反映かもしれない。** 単一文書からの `OPEN` 不在の推論は弱い。

**ただし §3-A の所見はこの弱点の影響を受けない。** `OPEN` の generic 性は D1（ISO/IEC）側で肯定的に確認されており、D2 の不在に依存していない。

---

## 5. 判定

### 5.1 停止規則に照らして

全 14 コードが立ったわけではないため、自動終了しない。ただし残存を精査すると次になる。

| 残存候補 | 状態 | 評価 |
|---|---|---|
| `UNC` | 判定不能（artifact type 由来） | **Null A に吸収。field-discriminating ではない** |
| `DOWN` | 判定不能（artifact type 由来） | **Null A に吸収。field-discriminating ではない** |
| `RET-DOWN` | **未検査**（baseline に該当層なし） | 保留。検査には L2+L3 を持つ generic 系列が必要 |
| `NONEVAL` | **不在を確認** | **唯一の実質的な残存候補** |

**14 コード中、比較研究の対象として生き残るのは実質 1 コード（`NONEVAL`）、保留が 1 コード（`RET-DOWN`）である。**

事前予測は「12 中せいぜい 4」だった。実際は 14 中 2（うち 1 は未検査）であり、**予測より厳しい結果である。**

### 5.2 水文学ノートへの影響

| v0.1 の主張 | P0 後 |
|---|---|
| future-work list の版跨ぎ継承は「通常の標準改訂では説明しにくい」 | **棄却。** ISO/IEC はより形式化された同等機構を持つ（§3-A） |
| 明示的退役宣言が固有 | **棄却。** RFC は機械可読な退役関係を持つ（§3-C） |
| non-evaluation declaration が「第三のカテゴリ」 | **保持。** generic baseline に現れず、"does not define" とは区別される（§3-B） |
| 下流文書による上流標準の制限（v0.2 §7-I） | **未検査。** baseline に該当層がない（§4-c） |

v0.2 の N-05 は、この結果により**部分的に確証された**。既に v0.2 本文へ反映済み。

### 5.3 設計文書 Part X の更新

| 設計時 | P0 後 |
|---|---|
| **B. viable comparative review, methodological value unproven**（D への降格リスク高） | **C. organizational synthesis only**、ただし 1 コードの限定的な B remnant を伴う |

**C とする理由。** 14 コード中 10 が generic であり、2 は artifact type で説明され、1 は未検査である。比較研究として問うべき対象が `NONEVAL` 一つに縮小した以上、これは「比較研究プログラム」ではなく「一つの記述形式についての限定的な問い」である。

**D（先行研究に実質吸収）としない理由。** `NONEVAL` の不在は generic baseline において肯定的に確認されており、まだ吸収されていない。また `RET-DOWN` は未検査である。

**B を維持しない理由。** 設計文書は「型別 license 対照表」相当の組織的価値を B の根拠としたが、P0 はその表の 10/14 行が generic であることを示した。表の大半が baseline と同一なら、比較表の情報量は低い。

---

## 6. 次の作業の選択肢

設計文書 Part VIII の P1–P5 をそのまま実行するのは、**対象が 1 コードに縮小した現在では過大である。**

| 選択肢 | 内容 | コスト | 判断 |
|---|---|---|---|
| **(i) 縮小継続** | `NONEVAL` のみを対象に、GUM/VIM と GRADE handbook を検索する。「評価していない」に相当する定型表現が存在するかを見る | 小（検索のみ） | **推奨** |
| (ii) `RET-DOWN` の検査 | L2+L3 を持つ generic 系列（例：ISO 規格＋それを引用する national regulation）を 1 組取得 | 中 | 次点 |
| (iii) 設計どおり P1–P5 | 三分野の完全な artifact chain 復元 | 大 | **非推奨。** 対象が 1 コードでは正当化できない |
| (iv) 終了 | comparative review へ降格して終了 | ゼロ | 許容範囲 |

**推奨は (i)。** 理由は三つ。第一に、検索のみで実行でき、GUM と GRADE handbook は入手可能性が高い。第二に、結果がどちらでも決着する — 両者に non-evaluation の定型表現があれば `NONEVAL` も generic となり、比較研究は (iv) へ移行する。なければ、水文学ノートの唯一の固有性候補が一段強化される。第三に、この一問だけなら独立符号化の負担が小さく、設計文書 Part VI-3 の単一分析者制約に抵触しにくい。

**(iii) を採らないことを明記する。** 設計文書は三分野の完全比較を計画したが、P0 の結果はその計画の前提（比較すべきコードが十分にある）を否定した。**設計どおりに進めることが、設計の目的に反する場合がある。**

---

## 7. Sources

1. ISO/IEC, 2001, *ISO/IEC Directives, Part 1: Procedures for the technical work*, 4th edition, 61 pp. — 取得経路: [wg5-fortran.org N1498](https://wg5-fortran.org/N1451-N1500/N1498.pdf)（公式 iso.org は 403）
   - 参照箇所: cl. 2.9 Maintenance of standards、cl. 2.10 Technical corrigenda and amendments、cl. 2.11 Maintenance agencies、cl. 2.12 Registration authorities、cl. 5 Appeals。

2. IEC, 2022, *ISO/IEC Directives, Part 1 + IEC Supplement — Procedures specific to IEC*, Edition 16.0, 2022-05, 98 pp. — 取得経路: [agenturacas.gov.cz mirror](https://www.agenturacas.gov.cz/wp-content/uploads/isoiecdir1ed16.0en-IECsup.pdf)（公式 iec.ch は取得不可）
   - 参照箇所: **cl. 2.7.2（non-actionable comments の archive 義務）**、cl. 2.9.1 Definitions（stability period, review, review date, maintenance, maintenance team, stability date, review report）、cl. 2.9.2 Review。

3. Fielding, R., Nottingham, M., and Reschke, J. (Eds.), 2022, *HTTP Semantics*: IETF RFC 9110, STD 97, June 2022. — [rfc-editor.org](https://www.rfc-editor.org/rfc/rfc9110.txt)
   - 参照箇所: ヘッダブロック（Obsoletes / Updates）、cl. 3.7、cl. 4.3.3、cl. 9.1、cl. 12.5.2（Accept-Charset deprecation）、cl. 16（IANA Considerations）、cl. 17（Security Considerations）。

### 取得できなかった資料

- ISO/IEC Directives Part 1 現行版（iso.org 403）
- ISO, *Guidance on the Systematic Review process in ISO*, PUB100413（iso.org 403。Codex が引用した文書）

---

## P0 が確立したこと

1. **未処理事項を次回改訂のために保存する機構は、技術標準運用の一般形式である。** ISO/IEC はこれを公式カテゴリ名・archive 義務・保存主体・将来用途つきで制度化しており、Bulletin 17B の Future Studies リストより形式化されている。
2. **退役宣言も generic である。** RFC は機械可読な `Obsoletes:` ヘッダを持ち、Bulletin 17C の本文記述より機械化されている。
3. **14 コード中 10 が generic baseline で再現された。**
4. **`NONEVAL`（未評価の明示）は generic baseline に現れなかった。** RFC の "does not define"（規定しない）とは、規定しない理由が「意図的委譲」か「未評価」かで区別される。
5. **`UNC` と `DOWN` の不在は artifact type で説明され、分野差の証拠にならない。** これは P0 の baseline 選定の欠陥である。
6. **`RET-DOWN` は未検査である。** baseline に下流規制層がなかった。

## P0 が確立しなかったこと

- `NONEVAL` が水文学に固有であること（他分野未検査）。
- `RET-DOWN` が存在しないこと（未検査）。
- 技術標準一般の代表性（D2 は一団体の一文書）。
- 推定値を産出する非科学的技術標準における `UNC` の扱い（未取得）。

## 次の作業

**選択肢 (i)。** GUM/VIM と GRADE handbook において、"did not evaluate" に相当する定型表現の有無のみを検索する。三分野の完全な artifact chain 復元（設計文書 P1–P5）には進まない。
