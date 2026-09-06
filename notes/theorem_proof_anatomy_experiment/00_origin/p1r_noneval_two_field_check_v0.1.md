# P1-reduced — `NONEVAL` Two-Field Check

## 唯一の残存候補を計量学と臨床医学で検査した結果

- **バージョン:** 0.1
- **日付:** 2026-08-22
- **種別:** reduced comparison result / kill test
- **先行:** [`p0_generic_standards_baseline_v0.1.md`](./p0_generic_standards_baseline_v0.1.md) §6 選択肢 (i)
- **設計文書:** [`qualification_practices_comparative_study_design_v0.1.md`](./qualification_practices_comparative_study_design_v0.1.md)
- **対象ノート:** [`hydrology_negative_knowledge_preservation_note_v0.2.md`](./hydrology_negative_knowledge_preservation_note_v0.2.md)

---

## 0. 検査対象と事前登録した判定基準

P0 の結果、14 コード中で比較対象として生き残ったのは `NONEVAL` 一つだった。本検査はこの一コードのみを扱う。

### 事前登録した `NONEVAL` の定義（検索前に固定）

> **`NONEVAL` = 記述の欠落を、著者・作業部会という行為主体の活動に帰属させる記述。**

次と区別する。

| 区別対象 | 特徴 | 例 |
|---|---|---|
| **`NONEVAL`** | **行為主体の活動に帰属**（我々は調べていない） | "The Work Group did not evaluate methods to account for watershed changes" |
| `SCOPE` | 文書の範囲に帰属（ここでは扱わない） | "HTTP does not define specific error handling mechanisms" |
| limitation | 世界の状態に帰属（できない） | "flood frequency computations are not reliable with records composed of less than 10 annual flood observations" |
| evidence-state | 証拠の状態に帰属（証拠がない） | "has not been tested against its alternative ... in randomized controlled trials" |

**判定の要点は「誰に欠落が帰属されているか」である。** 文書か、世界か、証拠か、著者か。

### 対象文書

| 分野 | 文書 | 層 |
|---|---|---|
| **計量学** | JCGM 100:2008 (GUM) — *Evaluation of measurement data: Guide to the expression of uncertainty in measurement*, 134 pp. | L2 |
| **計量学** | JCGM 200:2012 (VIM, 3rd ed.) — *International vocabulary of metrology*, 108 pp. | L2 |
| **臨床医学** | GRADE Handbook (Schünemann, Brożek, Guyatt, Oxman eds., updated October 2013), 49 pp. PDF | L2′ |
| 参照 | Bulletin 17C、Bulletin 17B | L2 |

---

## 1. 方法上の失敗と訂正（先に記録する）

**最初の検索は無効だった。**

GRADE handbook の PDF 抽出において、**語間スペースが失われていた**（"Recommendationsandtheirstrength" のように連結）。このため複数語からなる検索語がすべて一致せず、初回スキャンは GRADE について全項目 0 という結果を返した。

`evidence` は 1,102 回出現する一方 `not ` が 0 回という不整合から発覚した。単語単位の出現数を照合していなければ、**「GRADE には非評価宣言も証拠欠如の記述も一切ない」という完全な誤結論に到達していた。**

**訂正:** 全文書について、英数字以外を除去した正規化文字列上で検索し直した。検索語も同様に正規化した。以下の結果はすべて訂正後のものである。

**この失敗を記録する理由。** P0 で私は Codex のキーワード検索に基づく推論を採用し、自分でも同じ方法を使った。キーワード不一致による偽陰性は、この一連の作業で最も起こりやすい失敗様式であり、実際に起きた。以後の全文検索には単語数の健全性検査を必須とする。

---

## 2. 検索結果（訂正後）

正規化文字列上での出現数。

| 文書 | `NONEVAL` 候補 | 内訳 | `SCOPE` | `OPEN` |
|---|---|---|---|---|
| **GUM (JCGM 100:2008)** | **0** | — | 1（"beyond the scope"） | 0 |
| **VIM (JCGM 200:2012)** | **0** | — | 0 | 0 |
| **GRADE handbook (2013)** | **1 → 0**（§3 で棄却） | "not been tested" ×1 | 0 | 3（"further research"） |
| Bulletin 17C | **9** | "the Work Group did not" ×4、"did not evaluate" ×3、"not been evaluated" ×1、"did not conduct" ×1 | 3 | 11 |
| Bulletin 17B | **2** | "not been evaluated" ×1、"were not evaluated" ×1 | 3 | 3 |

---

## 3. 棄却した偽陽性

事前定義に照らして、以下を `NONEVAL` から除外した。

### GUM「not evaluated」（1 件）— 技術的用法

> "Those input estimates **not evaluated** from repeated observations must be obtained by other methods, such as those indicated in the second category of 4.1.3."

反復観測から評価されなかった**入力推定値**を指す技術的記述であり、著者の活動についての記述ではない。**棄却。**

### VIM「is not given」（1 件）— 定義上の記述

> "The concept 'measurement accuracy' is not a quantity and **is not given** a numerical quantity value."

概念の性質についての定義的記述。**棄却。**

### GRADE「not been tested」（1 件）— 証拠の状態

> "The principle of administering appropriate antibiotics rapidly in the setting of severe infection or sepsis **has not been tested** against its alternative of no rush of delivering antibiotics in randomized controlled trials."

**介入が RCT で試験されていない**という証拠の状態についての記述であり、GRADE 作成者が何かを評価しなかったという記述ではない。事前定義の `evidence-state` に該当する。**棄却。**

**棄却後の確定値: GUM 0、VIM 0、GRADE 0。**

---

## 4. 対照 — Bulletin 17C の `NONEVAL` は誰に帰属しているか

17C の該当箇所を全件確認した。

> "**The Work Group did not evaluate** methods to account for watershed changes and makes no particular recommendations, as additional work is needed in this area."

> "**The Work Group did not evaluate** methods to account for climate variability in flood frequency. Additional work in this area is warranted."

> "**The Work Group did not conduct an evaluation** of these procedures. Additional efforts are needed to provide guidance on the identification and treatment of mixed distributions."

> "Alternative procedures for making such studies or criteria for deciding when available flood records should be combined or extended by such procedures **have not been evaluated**."

**4 件中 3 件が "The Work Group" という名指しされた作業部会に明示的に帰属している。** 残る 1 件は受動態。

この形式は、**版をまたいで存続する名前を持つ作成主体が、自らの活動範囲について一人称的に述べる**ことによって成立している。

---

## 5. 判定

### 5.1 一次的判定 — `NONEVAL` は generic ではない

GUM、VIM、GRADE handbook のいずれにも、事前定義に合致する `NONEVAL` は存在しない。P0 の generic standards baseline（ISO/IEC Directives、RFC 9110）にも存在しなかった。

**5 文書中 0 件、Bulletin 系列のみ 11 件。** 形式としての `NONEVAL` は、本調査が検査した範囲では洪水頻度ガイダンス系列に限られる。

### 5.2 しかし二次的判定 — これは分野差の証拠にならない

**同じ機能は三分野すべてに存在する。実装形式が異なるだけである。**

| 分野 | 「基礎が不十分である」ことの記録形式 | 帰属先 |
|---|---|---|
| **洪水頻度** | "The Work Group did not evaluate..." | **作成主体の活動** |
| **臨床医学** | 証拠の確実性評価（very low certainty）、`§6.1.3 Recommendations to use interventions only in research`、`§6.1.4 No recommendation`、および「重要なアウトカムについて証拠が欠けている場合は、無視するのではなく認めるべきである」という指示 | **証拠の状態と出力の地位** |
| **計量学** | 不確かさの定量化そのもの。GUM 全体が「どれだけ分からないか」を数値化する体系である | **推定量の性質** |

すなわち、三分野とも「不十分さ」を記録する。**洪水頻度ガイダンスだけが、それを「我々が調べていない」という形で記録する。** 他の二分野は「証拠がこうである」「不確かさがこれだけある」という形で記録する。

**したがって観察されたのは、認識論的態度の差ではなく、不十分さの帰属先の差である。**

### 5.3 三次的判定 — Null F（governance）が最も有力な説明

`NONEVAL` が成立する条件を、観察から逆算すると次になる。

1. **名前を持ち、版をまたいで存続する作成主体があること**（"The Work Group"）。
2. **文書が問題空間を踏破する性格を持ち、被覆の欠落が生じうること。**

条件 2 が重要である。GUM は不確かさの計算法を定義し、VIM は用語を定義する。**定義する文書には「調べ残し」という概念が構造的に生じにくい。** Bulletin 17C は「どの流域で、どの条件下で、どの手法が使えるか」を踏破しようとする文書であり、踏破の欠落が生じる。

**これは設計文書 Part VII の Null A（artifact type）と Null F（governance）の連言であり、分野の差ではない。**

なお条件 1 だけでは不十分である。GUM・VIM も JCGM の作業部会が作成しており、名前を持つ主体は存在する。それでも `NONEVAL` を使わない。**条件 2（踏破性）が効いている公算が高い。**

### 5.4 決定的な制約 — n=1

`NONEVAL` の形式を持つのは Bulletin 系列のみである。**一つの文書系列にしか現れない形式について、それが分野の性質なのか、当該作業部会の編集習慣なのかを区別する手段が本調査にはない。**

Bulletin 17B（1982）と 17C（2018）は連続する版であり、独立標本ではない。実質的な n は 1 である。

---

## 6. 設計文書 Part X の更新

| 段階 | 判定 |
|---|---|
| 設計時 | B. viable comparative review, methodological value unproven |
| P0 後 | C. organizational synthesis only（1 コードの B remnant） |
| **P1-reduced 後** | **D 相当。terminate as comparative methodology; downgrade to comparative review** |

### 発火した kill criterion

設計文書 Part IX より。

| # | 条件 | 状態 |
|---|---|---|
| 4 | 分野差が artifact type / governance structure の差で十分説明できる | **発火**（§5.3） |
| 6 | 分野差が法的地位・賭け金・組織構造で説明できる（Null F） | **発火**（§5.3） |
| — | 残存候補が n=1 で、分野の性質と編集習慣を区別できない | **発火**（§5.4） |

設計文書 Part IX の規定どおり、最終成果は次に降格する。

> **comparative review of qualification practices in scientific and technical guidance**

### D としない留保を一点だけ残す

§5.2 の観察 — **同一機能が三つの異なる帰属先で実装されている** — は、既存の先行研究（GRADE、GUM、standards lifecycle）のいずれもが自分の分野内でしか記述していない事柄である。これは比較レビューの内容としては報告に値する。ただし**方法論ではない。** 診断を変えず、設計を変えず、判断を変えない。

---

## 7. 本検査が確立したこと

1. **`NONEVAL` という記述形式は、検査した 5 文書のうち Bulletin 系列にのみ現れた。** GUM 0、VIM 0、GRADE 0、ISO/IEC Directives 0、RFC 9110 0。
2. **しかし「基礎が不十分であること」を記録する機能は三分野すべてに存在する。** 帰属先が異なる — 洪水頻度は作成主体の活動へ、臨床医学は証拠の状態と出力の地位へ、計量学は推定量の不確かさへ。
3. **`NONEVAL` の成立条件は、名前を持つ存続的作成主体と、問題空間を踏破する文書性格の連言である。** これは Null A と Null F の連言であり、分野の認識論的態度の差ではない。
4. **残存候補は n=1 であり、分野の性質と一作業部会の編集習慣を区別できない。**
5. **方法上の失敗を一件記録した。** PDF 抽出でスペースが失われ、初回検索が完全な偽陰性を返した。単語数の健全性検査なしにキーワード検索の結果を採用してはならない。

## 本検査が確立しなかったこと

- `NONEVAL` が水文学に固有であること（n=1 のため判定不能）。
- 三分野に共通の認識論的構造が存在すること。
- 帰属先の差が診断・設計・判断に影響すること。
- GRADE §6.1.3 / §6.1.4 の本文内容（取得した PDF は §1–5 のみを収録しており、§6 は目次のみ。本文未確認）。

---

## 8. Sources

### 本検査で取得・全文検索した資料

1. JCGM, 2008, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*, JCGM 100:2008 (GUM 1995 with minor corrections), 134 pp. — [BIPM](https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf)
2. JCGM, 2012, *International vocabulary of metrology — Basic and general concepts and associated terms (VIM)*, JCGM 200:2012, 3rd edition, 108 pp. — [BIPM](https://www.bipm.org/documents/20126/2071204/JCGM_200_2012.pdf)
3. Schünemann, H., Brożek, J., Guyatt, G., and Oxman, A. (eds.), 2013, *GRADE Handbook — Handbook for grading the quality of evidence and the strength of recommendations using the GRADE approach*, updated October 2013, 49 pp. PDF — 取得経路: [Mahidol University mirror](https://www.rama.mahidol.ac.th/ceb/sites/default/files/public/pdf/journal_club/2017/GRADE%20handbook.pdf)。オンライン版: [gdt.gradepro.org](https://gdt.gradepro.org/app/handbook/handbook.html)
   - **限界:** 取得した PDF は本文が §1–5 に限られ、§6（Going from evidence to recommendations）は各ページに繰り返されるナビゲーション目次としてのみ現れる。§6.1.3 および §6.1.4 の存在は目次から `documented` だが、本文は未確認。

### 参照した既取得資料

4. Bulletin 17C（USGS TM 4-B5, ver. 1.1, 2019）
5. Bulletin 17B（IACWD 1982）
6. ISO/IEC Directives Part 1 (2001) + IEC Supplement (Ed. 16.0, 2022)
7. IETF RFC 9110 (STD 97, 2022)

---

## 9. 次の作業

**比較方法論としては終了する。** 設計文書 Part IX の規定に従う。

残す作業は次の二つのみであり、いずれも比較研究ではなく個別ノートの完成に属する。

1. **水文学ノート v0.3** — 本検査の結果を反映する。具体的には、§7-C（non-evaluation declaration）の固有性主張を「検査した 5 文書中で唯一だが、n=1 であり、artifact type と governance の連言で説明されうる」へ後退させる。「現時点で最も固有性の見込みが高い形式」という v0.2 の表現を削除する。
2. **Case 01 への引き継ぎ** — 本検査は Case 01 の検査候補を変えない。v0.2 §10.3 の優先順位（Plate 1 残存 → expected probability 残存 → 照合義務 → CI 過小）を維持する。

**設計文書 Part VIII の P1–P5(三分野の完全な artifact chain 復元)には進まない。** P0 と本検査により、その計画の前提は二段階にわたって否定された。
