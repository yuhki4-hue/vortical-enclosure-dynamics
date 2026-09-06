# 定理の「証明の解剖」v1.1

## 読み方

本稿でいう「逃走経路」「閉じ方」「封鎖」「残差」は、定理の条件が果たす機能を比較するための解剖的メタ記述であり、標準数学用語ではない。`R0 / R1 / R2` も数学上の定理分類ではなく、条件除去後の挙動を記録するための作業ラベルである。

- **R0 — no clear residual:** 定理が偽になる、または枠組みが定義不能になるが、自然な補正項は確認できない。
- **R1 — altered freedom:** 非一意性、新しい自由度、別の極限、別の構造などが現れる。
- **R2 — explicit residual term:** 一般化された式に境界項・補正項・追加項が明示的に戻る。

複数版を持つ定理は、`standard_statement` で採用版を限定する。また、条件除去が別の定理へ移るだけで独立な「仮定除去」にならない場合は、そのことを明記する。

# I. 重点再確認した8定理

## 1. Heine–Borel の定理

1. **theorem_name:** Heine–Borel の定理

2. **domain:** 実解析・位相

3. **standard_statement:** (K\subset\mathbb R^n) がコンパクトであることと、(K) が閉かつ有界であることは同値である。以下の条件解剖は主に非自明な向き「閉かつ有界 \(\Rightarrow\) コンパクト」を扱う。

4. **assumptions_ABC:**
   - A: (K) が閉集合である
   - B: (K) が有界である
   - C: 周囲の空間が有限次元ユークリッド空間 (\mathbb R^n) である

5. **hypothesis_levels:**
   - A: object
   - B: object
   - C: ambient（有限次元性と実数体を含む）

6. **condition_types:**
   - A: 閉性
   - B: 有界性
   - C: 有限次元性・ユークリッド構造

7. **closure_roles:**
   - A: ambient closure / finite-limit escape prevention
   - B: domain enclosure / infinity escape prevention
   - C: finite-dimensional closure

8. **conclusion_P:** 任意の開被覆から有限部分被覆を選べる。等価に、距離空間として任意の列が収束部分列を持つ。

9. **blocked_escape_routes:**
   - A: 集積点だけが集合外へ抜ける逃げ道を塞ぐ
   - B: 点が無限遠へ逃げることを防ぐ
   - C: 無限に独立な方向へ分散することを防ぐ

10. **what_fails_if_removed:**
   - Aを外すと: ((0,1)) は有界だがコンパクトでない
   - Bを外すと: (\mathbb R) は閉だがコンパクトでない
   - Cを外すと: 無限次元 Hilbert 空間の閉単位球は閉かつ有界だがコンパクトでない

11. **what_reappears_if_removed:**
   - A: **R1** — 欠落した極限点という追加成分が集合の閉包 (\overline K\setminus K) に現れる
   - B: **R1** — 無限遠への逃走列が許される。通常の定理内に明示的補正項はない
   - C: **R1** — 無限個の独立方向、すなわち bounded だが precompact でない自由度が現れる

12. **proof_resources:**
   - representative_route: 区間の二分法と有限次元への拡張
   - resources:
     - 実数の完備性または Bolzano–Weierstrass
     - (\mathbb R^n) における全有界性
     - Lebesgue 数補題または逐次コンパクト性とコンパクト性の同値
   - note: これらは証明資源であり、A・Bに追加される定理文上の仮定ではない。逆向き「コンパクトなら閉かつ有界」は Hausdorff 性や距離構造を用いる。

13. **closure_style:** 三方向逃走封鎖型

14. **theorem_vs_proof_comment:** 定理文が固定するのは (K) の閉性・有界性と有限次元ユークリッド空間という舞台である。証明は実数の完備性や全有界性を使って、これらの固定から有限部分被覆を抽出する。完備性を新たな独立仮定として数えると、(\mathbb R^n) という ambient にすでに埋め込まれた構造と証明手段が二重計上される。

15. **short_comment:** 「閉かつ有界」がコンパクト性になるのは有限次元空間に特有である。有限位置、無限遠、無限方向という三種類の逃走可能性をまとめて塞いでいる。

---

## 2. Bolzano–Weierstrass の定理

1. **theorem_name:** Bolzano–Weierstrass の定理

2. **domain:** 実解析

3. **standard_statement:** (\mathbb R^n) の任意の有界数列は、収束する部分列を持つ。

4. **assumptions_ABC:**
   - A: 数列が有界である
   - B: 空間が有限次元である
   - C: 基礎体が完備な (\mathbb R) である

5. **hypothesis_levels:**
   - A: object
   - B: ambient
   - C: background（標準定理文の (\mathbb R^n) に含まれ、Bから独立に追加された仮定ではない）

6. **condition_types:**
   - A: 有界性
   - B: 有限次元性
   - C: 完備性

7. **closure_roles:**
   - A: escape prevention
   - B: finite-dimensional closure
   - C: ambient closure / completeness

8. **conclusion_P:** ある部分列が (\mathbb R^n) 内の点へ収束する。

9. **blocked_escape_routes:**
   - A: 部分列が無限遠へ逃げることを防ぐ
   - B: 項が互いに独立な方向へ移り続けることを防ぐ
   - C: Cauchy 的に近づきながら極限だけが空間外にある事態を防ぐ

10. **what_fails_if_removed:**
   - Aを外すと: (x_n=n) は収束部分列を持たない
   - Bを外すと: (\ell^2) の正規直交列 (e_n) は有界だが収束部分列を持たない
   - Cを外すと: (\mathbb Q) 内で (\sqrt2) に近づく有理数列は (\mathbb Q) 内に収束部分列を持たない。ただしこれは ambient を (\mathbb R^n) から変えた別定理であり、Cだけの独立除去ではない

11. **what_reappears_if_removed:**
   - A: **R1** — 無限遠への逃走列
   - B: **R1** — 無限個の相互分離方向。全有界性の欠如として現れる
   - C: **R1** — 完備化 (\widehat X\setminus X) に位置する欠落極限

12. **proof_resources:**
   - representative_route: 区間・箱の逐次二分法
   - resources:
     - 入れ子区間原理
     - 実数の完備性
     - 対角部分列抽出（(n>1)）
   - note: Heine–Borel から導く証明もある。どのルートでも、証明資源としての完備性を標準定理文へ別仮定として追加しない。

13. **closure_style:** 収束逃走封鎖型

14. **theorem_vs_proof_comment:** 定理が直接固定するのは、(\mathbb R^n) という舞台と数列の有界性である。二分法や完備性は、そこから部分列を構成する証明資源である。これを混同すると、「有界性だけではなぜ無限次元で足りないか」という ambient の役割が見えにくくなる。

15. **short_comment:** 有界性だけでは収束は保証されない。有限次元性が方向への拡散を、完備性が極限の空間外流出を止めることで、部分列収束が成立する。

---

## 3. Banach 不動点定理

1. **theorem_name:** Banach 不動点定理

2. **domain:** 解析・距離空間論

3. **standard_statement:** 空でない完備距離空間 (X) 上の縮小写像 (T:X\to X)、すなわちある (0\le q<1) に対して (d(Tx,Ty)\le qd(x,y)) を満たす写像は唯一の不動点を持ち、任意の初期値からの反復 (x_{n+1}=T(x_n)) はそこへ収束する。

4. **assumptions_ABC:**
   - A: (X) が空でない完備距離空間
   - B: (T) が一様な縮小率 (q<1) を持つ
   - C: (T(X)\subseteq X)

5. **hypothesis_levels:**
   - A: ambient（「空でない」は definitional）
   - B: object
   - C: object（写像型の一部でもある）

6. **condition_types:**
   - A: 完備性・非空性
   - B: 収縮性
   - C: 自己写像性

7. **closure_roles:**
   - A: completeness / ambient closure
   - B: contraction / uniqueness / convergence forcing
   - C: self-map closure

8. **conclusion_P:** 不動点がただ一つ存在し、反復列がそこへ幾何級数的速度で収束する。

9. **blocked_escape_routes:**
   - A: Cauchy 軌道の極限が空間外へ逃げることを防ぐ
   - B: 軌道の巡回・拡散と、複数の不動点が離れて存在することを防ぐ
   - C: 反復途中で定義域外へ出ることを防ぐ

10. **what_fails_if_removed:**
   - Aを外すと: (X=(0,1), T(x)=x/2) は縮小写像だが、不動点0は (X) 外
   - Bを外すと: 恒等写像は不動点を無数に持つ。平行移動は不動点を持たない
   - Cを外すと: 反復を (X) 内で継続できず、定理の反復構造自体が閉じない

11. **what_reappears_if_removed:**
   - A: **R1** — 完備化 (\widehat X\setminus X) にある「欠落不動点」または欠落極限
   - B: **R1** — 非一意性、周期軌道、発散などの動力学的自由度
   - C: **R1** — 外部領域への流出。反復には不変集合などの追加条件が必要になる

12. **proof_resources:**
   - representative_route: Picard 反復
   - resources:
     - 距離差の幾何級数評価
     - Cauchy 列
     - 完備性による極限の存在
     - 縮小不等式の極限移行と一意性評価
   - note: 幾何級数評価は証明道具であり、独立の定理仮定ではない。

13. **closure_style:** 収縮封鎖型

14. **theorem_vs_proof_comment:** 定理は完備な舞台、自己写像性、一様収縮を固定する。証明は反復列を作り、幾何級数評価で Cauchy 性を示して完備性へ渡す。反復法を仮定と取り違えると、この定理が存在定理であると同時に構成的近似法を与える点が見えなくなる。

15. **short_comment:** 収縮性が軌道を一本に絞り、完備性がその終点を空間内に確保する。存在・一意性・計算法を同じ不等式で同時に閉じる点が特徴的である。

---

## 4. 階数・退化次数定理

1. **theorem_name:** 階数・退化次数定理（rank–nullity theorem）

2. **domain:** 線形代数

3. **standard_statement:** 同じ体上のベクトル空間 (V,W) と線形写像 (T:V\to W) について、(V) が有限次元なら (\dim V=\dim\ker T+\dim\operatorname{im}T) が成り立つ。

4. **assumptions_ABC:**
   - A: (V) が有限次元
   - B: (T) が線形
   - C: (V,W) が同じ体上のベクトル空間

5. **hypothesis_levels:**
   - A: ambient
   - B: object
   - C: ambient（通常は定式化に埋め込まれる型条件）

6. **condition_types:**
   - A: 有限性
   - B: 線形構造
   - C: 代数構造

7. **closure_roles:**
   - A: finite-dimensional closure
   - B: conservation/accounting
   - C: transport compatibility / common scalar accounting

8. **conclusion_P:** 入力自由度が、消失する自由度と像に残る自由度へ過不足なく分解される。

9. **blocked_escape_routes:**
   - A: 次元計算が無限基数の吸収則に埋没することを防ぐ
   - B: 核・像と基底の対応が非線形変形で崩れることを防ぐ
   - C: 次元、核、像を共通のスカラー体系で数えられなくなることを防ぐ

10. **what_fails_if_removed:**
   - Aを外すと: 定理は無限基数を用いる次元公式としてなお成立するが、有限整数の加法としての情報量は弱くなる。したがって単純な反例ではなく結論の意味の弱化である
   - Bを外すと: (f(x)=x^2) の像は一般に部分空間でなく、通常の rank–nullity の枠組みが定義できない
   - Cを外すと: 核・像・次元を同じ線形カテゴリーで比較できず、枠組み自体が成立しない

11. **what_reappears_if_removed:**
   - A: **R1** — 無限基数では (\kappa+n=\kappa) となり、有限個の kernel 自由度が総次元の等式から見えなくなる
   - B: **R0** — 一般の非線形写像には自然な「補正項付き rank–nullity」はない。局所微分へ移れば別定理になる
   - C: **R0** — 共通の会計単位が消え、自然な残差項より先に定式化が失われる

12. **proof_resources:**
   - representative_route: kernel 基底の延長
   - resources:
     - (\ker T) の基底
     - 基底延長定理
     - 延長された基底の像が (\operatorname{im}T) の基底になること
   - note: 基底延長は証明道具であり、定理文へ追加する条件ではない。無限次元版では選択公理に関わる基底存在が背景に入る。

13. **closure_style:** 自由度会計型

14. **theorem_vs_proof_comment:** 定理が固定するのは線形性、有限次元性、共通の体である。証明は kernel の基底を定義域の基底へ延長して、消えた基底と像へ運ばれた基底を数える。基底延長を仮定と混同すると、線形性そのものが自由度保存則を担っている点が隠れる。

15. **short_comment:** 線形写像が入力自由度を「消す部分」と「残す部分」に完全分配する定理である。有限次元ではこの会計が通常の整数加法として情報を保つ。

---

## 5. Stokes の定理

1. **theorem_name:** Stokes の定理

2. **domain:** 微分幾何・多様体論

3. **standard_statement:** 向き付けられた滑らかな (n) 次元多様体 (M) と滑らかな ((n-1))-形式 (\omega) について、(M) がコンパクトであるか (\omega) がコンパクトな台を持つなら、誘導された境界の向きに対して (\int_Md\omega=\int_{\partial M}\omega) が成り立つ。

4. **assumptions_ABC:**
   - A: (M) と境界が整合的に向き付けられている
   - B: (M) と (\omega) が十分滑らか
   - C: (M) がコンパクト、または (\omega) がコンパクトな台を持つ

5. **hypothesis_levels:**
   - A: ambient
   - B: ambient（多様体）＋ object（微分形式）
   - C: ambient または object（採用する二つの標準形に対応）

6. **condition_types:**
   - A: 向き・境界条件
   - B: 正則性
   - C: コンパクト性・台条件

7. **closure_roles:**
   - A: transport compatibility / sign coherence
   - B: regularity
   - C: boundary-at-infinity suppression

8. **conclusion_P:** 内部における外微分の総量が、通常の境界上の積分へ完全に移される。

9. **blocked_escape_routes:**
   - A: 局所片の内部境界が同符号で残り、相殺しない可能性を防ぐ
   - B: 外微分や局所積分が未定義になることを防ぐ
   - C: 無限遠へ流出する寄与を、右辺にないまま残すことを防ぐ

10. **what_fails_if_removed:**
   - Aを外すと: 通常の微分形式の符号付き積分を大域的に整合させられない。密度や向き局所系を用いる別形式が必要
   - Bを外すと: (d\omega) が存在しない、または積分不能になり得る。弱微分・current を使う一般化は別枠である
   - Cを外すと: (M=\mathbb R), (\omega=\arctan x) では (\int_{\mathbb R}d\omega=\pi) だが通常の境界は空であり、無限遠の寄与が漏れる

11. **what_reappears_if_removed:**
   - A: **R1** — 向き局所系、twisted form、密度などの追加構造が必要になる
   - B: **R1** — 特異集合や分布的微分が defect measure/current として現れ得る。ただし一般に一意の補正項が自動的にあるわけではない
   - C: **R2** — exhaustion (M_R) を使えば (\int_{M_R}d\omega=\int_{\partial M_R}\omega) となり、極限で「無限遠の境界項」が明示的に戻る

12. **proof_resources:**
   - representative_route: 座標近傍への分割と局所 Stokes の貼り合わせ
   - resources:
     - 1変数微積分の基本定理
     - partition of unity
     - 局所座標と境界チャート
     - 向きによる内部境界の符号相殺
   - note: partition of unity は代表的証明の資源であり、定理文の独立仮定ではない。

13. **closure_style:** 内部相殺・境界集約型

14. **theorem_vs_proof_comment:** 定理は向き、正則性、無限遠への漏出を止める台条件を固定する。証明は partition of unity で局所化し、微積分の基本定理と符号相殺で境界だけを残す。局所分割を仮定と誤認すると、右辺の境界項が「証明の都合」ではなく結論に残る本質的成分であることが見えなくなる。

15. **short_comment:** 局所領域を分割すると内部境界は反対向きで相殺され、外側の境界だけが残る。コンパクト台条件を外すと、無限遠が新たな境界として再出現する。

---

## 6. Gauss–Bonnet の定理

1. **theorem_name:** Gauss–Bonnet の定理（閉曲面版）

2. **domain:** 微分幾何・位相幾何

3. **standard_statement:** コンパクトで境界を持たない滑らかな Riemann 曲面 (M) について、(\int_MK\,dA=2\pi\chi(M)) が成り立つ。

4. **assumptions_ABC:**
   - A: (M) がコンパクト
   - B: (M) が境界を持たない
   - C: (M) と Riemann 計量が曲率を定義できる程度に滑らか

5. **hypothesis_levels:**
   - A: ambient
   - B: ambient
   - C: ambient

6. **condition_types:**
   - A: コンパクト性
   - B: 境界条件
   - C: 正則性・幾何構造

7. **closure_roles:**
   - A: global enclosure / infinity escape prevention
   - B: boundary suppression
   - C: regularity / local curvature definition

8. **conclusion_P:** 局所的 Gauss 曲率の総和が、大域的位相不変量 (2\pi\chi(M)) に一致する。

9. **blocked_escape_routes:**
   - A: 曲率会計が無限遠の end へ漏れることを防ぐ
   - B: 境界の曲がりが未計上のまま残ることを防ぐ
   - C: 曲率密度が未定義、または特異点に集中することを防ぐ

10. **what_fails_if_removed:**
   - Aを外すと: 非コンパクト平面では (\int KdA=0) だが通常の Euler 標数は1で、閉曲面版の式はそのまま成立しない
   - Bを外すと: 平坦な円板では内部曲率積分は0だが (\chi=1)。境界測地曲率項が必要
   - Cを外すと: (K) や面積要素を通常の形で定義できず、円錐特異点などには別の補正が必要

11. **what_reappears_if_removed:**
   - A: **R1** — end、無限遠の曲率損失、可積分性条件が現れる。十分制御された一般化では無限遠の境界項として R2 化する
   - B: **R2** — (\int_MK\,dA+\int_{\partial M}k_g\,ds=2\pi\chi(M))。区分的滑らかな境界では角の外角和も戻る
   - C: **R1/R2** — 一般には別理論が必要。円錐特異点など制御された場合は角欠損が明示的補正項として戻る

12. **proof_resources:**
   - representative_route: 測地三角形分割による証明
   - resources:
     - 局所 Gauss–Bonnet
     - 三角形分割
     - 内部辺の境界寄与の相殺
     - (V-E+F=\chi(M)) という組合せ論的会計
   - note: moving frame と Stokes の定理を使う別証明もある。三角形分割や Stokes は証明資源であり、閉曲面版の仮定ではない。

13. **closure_style:** 局所大域接合型

14. **theorem_vs_proof_comment:** 定理は閉じた滑らかな曲面という舞台を固定し、局所曲率の総量を位相へ結びつける。証明は分割、局所公式、内部辺の相殺を使う。証明上の分割と定理上の境界なし条件を混同すると、境界を外した瞬間に測地曲率が R2 として戻る構造が見えなくなる。

15. **short_comment:** 局所的な曲がりを全面で集計すると計量の細部が消え、位相だけが残る。境界なしという条件は単なる簡略化ではなく、明示的な境界曲率項をゼロに固定している。

---

## 7. 一階述語論理のコンパクト性定理

1. **theorem_name:** 一階述語論理のコンパクト性定理

2. **domain:** 数理論理・モデル理論

3. **standard_statement:** 一階述語論理の文の集合 (T) について、(T) のすべての有限部分集合が充足可能なら、(T) 全体も充足可能である。

4. **assumptions_ABC:**
   - A: (T) が通常の有限的な一階述語論理の文からなる
   - B: 任意の有限部分集合 (T_0\subseteq T) がモデルを持つ
   - C: 通常の Tarski 意味論における構造をモデルとして認める

5. **hypothesis_levels:**
   - A: ambient（論理体系・表現力の指定）
   - B: object（理論 (T) の有限充足可能性）
   - C: background（通常は標準意味論として埋め込まれる）

6. **condition_types:**
   - A: 有限構文・表現力制限
   - B: 有限局所整合性
   - C: 意味論的モデル条件

7. **closure_roles:**
   - A: finitary closure / expressive restriction
   - B: local consistency
   - C: local-to-global connection / semantic closure

8. **conclusion_P:** (T) の全ての文を同時に満たす一つのモデルが存在する。

9. **blocked_escape_routes:**
   - A: 一つの無限長式で、全有限段階では見えない矛盾を直接記述する可能性を塞ぐ
   - B: 矛盾がすでに有限個の文から生じている可能性を除く
   - C: モデルを有限構造などへ限定して大域モデルを排除することを防ぐ

10. **what_fails_if_removed:**
   - Aを外すと: (L_{\omega_1,\omega}) では「構造は有限」という可算選言と「少なくとも (n) 元ある」という全ての文を組み合わせ、各有限部分は充足可能だが全体は充足不能にできる
   - Bを外すと: 有限部分に矛盾があれば、当然 (T) 全体もモデルを持たない
   - Cを外すと: 有限モデルだけを許す意味論では、「少なくとも (n) 元ある」を全 (n) について要求する理論は各有限部分が有限モデルを持つが全体は有限モデルを持たない

11. **what_reappears_if_removed:**
   - A: **R1** — 無限長論理式が持つ新しい表現自由度により、有限部分へ還元できない大域制約が現れる
   - B: **R0** — 有限矛盾がそのまま残るだけで、自然な補正項はない
   - C: **R1** — 標準性・有限性などのモデル制約が未処理成分として戻り、単なる充足可能性より強い要請になる

12. **proof_resources:**
   - representative_route: Henkin 構成と完全性定理を経由する証明
   - resources:
     - 言語への Henkin 定数の追加
     - 有限充足可能性を保つ理論拡張
     - 極大整合理論
     - term model または完全性定理
   - note: ultraproduct・超フィルターによる別証明もある。任意言語に対する一般形では Boolean prime ideal theorem 相当の弱い選択原理がメタ理論上関係するが、これは通常の定理文の A–C と同列ではない。

13. **closure_style:** 有限矛盾捕捉型

14. **theorem_vs_proof_comment:** 定理が固定するのは一階・有限構文という論理舞台と、理論の有限充足可能性である。証明は Henkin 化や極大整合拡張によって一つのモデルを作る。完全性定理や超フィルターを仮定に昇格させると、表現力制限こそがコンパクト性の範囲を決めている点が見えなくなる。

15. **short_comment:** 一階論理では、大域的な充足不能性は必ず有限個の文の段階ですでに露呈する。ただし得られるモデルは有限・標準的・意図されたモデルとは限らず、定理が閉じるのはモデルの存在までである。

---

## 8. 代数学の基本定理

1. **theorem_name:** 代数学の基本定理

2. **domain:** 代数・複素解析

3. **standard_statement:** 複素係数の任意の非定数一変数多項式は少なくとも一つ複素根を持つ。従って重複度を込めて次数個の一次因子へ分解できる。

4. **assumptions_ABC:**
   - A: 対象が有限次数の一変数多項式
   - B: 多項式が非定数
   - C: 係数と根を複素数体で考える

5. **hypothesis_levels:**
   - A: object
   - B: definitional（無根の定数多項式を除く非退化条件）
   - C: ambient

6. **condition_types:**
   - A: 多項式構造・有限性
   - B: 非退化性
   - C: 体・複素数構造

7. **closure_roles:**
   - A: finite algebraic form
   - B: nondegeneracy
   - C: root ambient / field-extension ceiling（複素数体が実際に全ての根を収容すること自体は結論であり、仮定ではない）

8. **conclusion_P:** (p(z)=0) を満たす (z\in\mathbb C) が存在し、反復して一次因子分解が得られる。

9. **blocked_escape_routes:**
   - A: 非定数でありながら零点を持たない一般正則関数へ逃げる可能性を除く
   - B: 定数関数という明白な無根例を除く
   - C: 根が係数体の外部の代数拡大へ逃げることを防ぐ

10. **what_fails_if_removed:**
   - Aを外すと: 非定数整関数 (e^z) は零点を持たない
   - Bを外すと: (p(z)=1) は根を持たない
   - Cを外すと: 実係数多項式 (x^2+1) は実根を持たない

11. **what_reappears_if_removed:**
   - A: **R0** — 一般の整関数には零点なしという挙動が許されるが、統一的な補正項が戻るわけではない
   - B: **R0** — 定数という退化例が戻るだけで自然な残差はない
   - C: **R1** — 根を収容する代数拡大が必要になる。実数上では非実根が共役対として未処理成分に現れる

12. **proof_resources:**
   - representative_route: Liouville の定理を用いる解析的証明
   - resources:
     - 根がないと仮定した (1/p(z)) の整関数性
     - 多項式の無限遠での増大
     - Liouville の定理
     - 一つの根を得た後の多項式除法と帰納法
   - note: 最大値原理、Rouché の定理、偏角原理、位相的次数などによる別証明がある。複素数の完備性や Liouville は証明資源であり、「複素数体が代数的に閉じている」という結論を仮定してはならない。

13. **closure_style:** 根の体外逃走封鎖型

14. **theorem_vs_proof_comment:** 定理文は有限次数多項式、非定数性、複素数という舞台だけを固定する。解析的証明は (1/p) と Liouville を使って根の不在を矛盾へ変える。Liouville や複素完備性を定理の追加仮定と数えると、代数的結論を解析的資源で証明しているという重要な層の差が消える。

15. **short_comment:** 結論は複素数体の代数的閉性そのものである。複素数を舞台に選ぶことと、その舞台が実際に全ての多項式根を収容すると証明することは区別されなければならない。

# II. 残り13定理

## 9. 中間値の定理

1. **theorem_name:** 中間値の定理
2. **domain:** 実解析
3. **standard_statement:** (f:[a,b]\to\mathbb R) が連続で、(y) が (f(a)) と (f(b)) の間にあるなら、ある (c\in[a,b]) が存在して (f(c)=y) となる。
4. **assumptions_ABC:**
   - A: 定義域が区間 ([a,b])
   - B: (f) が連続
   - C: (y) が端点値の間にある
5. **hypothesis_levels:**
   - A: ambient
   - B: object
   - C: definitional（結論の探索値を非自明な範囲に置く条件）
6. **condition_types:** A: 連結性／B: 連続性／C: 境界値条件
7. **closure_roles:** A: domain enclosure / connectedness／B: continuity / jump prevention／C: bracketing / nondegeneracy
8. **conclusion_P:** (f(c)=y) を満たす点が存在する。
9. **blocked_escape_routes:**
   - A: 定義域の切断部を通って値域が分かれる逃げ道を塞ぐ
   - B: (y) を飛び越える逃げ道を塞ぐ
   - C: (y) を横切る必要のない配置を除く
10. **what_fails_if_removed:**
   - A: ([-1,0)\cup(0,1]) 上で負値・正値を別成分に置けば0を取らない
   - B: 符号関数型の段差は0を飛び越える
   - C: (f(x)=x) on ([0,1]) は2を取らない
11. **what_reappears_if_removed:** A: **R1** — 連結成分という選択自由度／B: **R1** — jump discontinuity と飛び越された値の区間／C: **R0** — 探索値が像の外にあるだけ
12. **proof_resources:**
   - representative_route: 上限を用いる証明
   - resources: 実数の上限性、連続性、区間の順序構造
   - note: 連結性を用いる位相的証明や二分法もある。上限性は証明資源であり、Bとは別の関数仮定ではない。
13. **closure_style:** 飛躍禁止型
14. **theorem_vs_proof_comment:** 定理は区間、連続関数、挟まれた目的値を固定する。証明は実数の上限性または連結像の連結性を使う。証明資源と仮定を混同すると、関数側の連続性と実数側の連結・完備構造の分担が見えなくなる。
15. **short_comment:** 連結な入力区間を連続写像が分断できないことを、値の存在として表す。核心は目的値を避ける跳躍自由度の消去である。

---

## 10. 最大最小値定理

1. **theorem_name:** 最大最小値定理
2. **domain:** 実解析
3. **standard_statement:** 空でない閉区間 ([a,b]) 上の連続関数 (f:[a,b]\to\mathbb R) は最大値と最小値を実際に取る。
4. **assumptions_ABC:**
   - A: 定義域が閉じている
   - B: 定義域が有界かつ空でない
   - C: (f) が連続
5. **hypothesis_levels:** A: ambient／B: ambient（非空部分は definitional）／C: object
6. **condition_types:** A: 閉性／B: 有界性・非空性／C: 連続性
7. **closure_roles:** A: finite-limit escape prevention／B: infinity escape prevention / nondegeneracy／C: continuity / extremum transport
8. **conclusion_P:** 最大値・最小値を達成する点が定義域内に存在する。
9. **blocked_escape_routes:** A: 極値候補が欠落した有限端点へ逃げることを防ぐ／B: 無限遠への逃走と対象不在を防ぐ／C: 極限点で値だけが離脱することを防ぐ。
10. **what_fails_if_removed:**
   - A: (f(x)=x) on ((0,1]) は最小値を取らない
   - B: (f(x)=x) on ([0,\infty)) は最大値を持たない。空集合なら達成点自体がない
   - C: (f(x)=x (x<1), f(1)=0) on ([0,1]) は上限1を取らない
11. **what_reappears_if_removed:** A: **R1** — 閉包上の欠落極値／B: **R1** — 無限遠への極値逃走（空集合の場合は R0）／C: **R1** — 上半連続・下半連続など、最大・最小を片側だけ回復する追加条件
12. **proof_resources:**
   - representative_route: 極値近似列と収束部分列
   - resources: 実数の上限・下限、逐次コンパクト性、連続性による極限移行
   - note: 連続像のコンパクト性からも直ちに従う。
13. **closure_style:** 極値逃走防止型
14. **theorem_vs_proof_comment:** 閉区間版の定理は、有限端点を含む有界な舞台と連続な対象を固定する。証明は Heine–Borel によるコンパクト性または収束部分列を使って極限を回収する。ここでは閉性・有界性が定理文の条件であり、Heine–Borel や逐次コンパクト性が証明資源である。
15. **short_comment:** コンパクト性が位置の逃走を、連続性が値の離脱を止める。両者が極値の「近似」を実際の達成へ変える。

---

## 11. 平均値の定理

1. **theorem_name:** 平均値の定理
2. **domain:** 微分積分学
3. **standard_statement:** (f:[a,b]\to\mathbb R) が ([a,b]) で連続、((a,b)) で微分可能、(a<b) なら、ある (c\in(a,b)) で (f'(c)=(f(b)-f(a))/(b-a)) となる。
4. **assumptions_ABC:** A: 閉区間で連続／B: 内部で微分可能／C: (a<b)
5. **hypothesis_levels:** A: object／B: object／C: definitional
6. **condition_types:** A: 端点連続性／B: 正則性／C: 非退化性
7. **closure_roles:** A: endpoint compatibility／B: regularity / local slope availability／C: nondegeneracy
8. **conclusion_P:** 割線勾配と等しい接線勾配が内部に存在する。
9. **blocked_escape_routes:** A: 端点値と内部グラフの切離し／B: 角や跳びへの変化集中／C: 割線勾配の未定義化を防ぐ。
10. **what_fails_if_removed:** A: (f(0)=1,f(x)=x (x>0)) では割線勾配0、内部微分1／B: (|x|) on ([-1,1])／C: (a=b) では商が未定義。
11. **what_reappears_if_removed:** A: **R1** — 端点 jump が全体変化の未処理成分になる／B: **R1** — corner・nondifferentiable variation。絶対連続関数なら積分形など別枠へ移る／C: **R0** — 定義上の退化。
12. **proof_resources:** representative_route: Rolle の定理への還元／resources: 補助関数、最大最小値定理、Fermat の停留点定理／note: これらは証明道具である。
13. **closure_style:** 勾配捕捉型
14. **theorem_vs_proof_comment:** 定理は端点連続性、内部微分可能性、非退化区間を固定する。証明は割線を差し引いた補助関数へ Rolle を適用する。最大最小値定理は導出資源であり、平均値の定理の追加仮定ではない。
15. **short_comment:** 全体変化を局所微分のどこかへ必ず担わせる。条件を外すと、変化は端点 jump や角へ再配置される。

---

## 12. スペクトル定理

1. **theorem_name:** スペクトル定理（有限次元実自己共役版）
2. **domain:** 線形代数
3. **standard_statement:** 有限次元実内積空間上の自己共役線形作用素は、実固有値からなる正規直交固有基底を持ち、直交行列で対角化できる。
4. **assumptions_ABC:** A: 有限次元実内積空間／B: 線形作用素／C: 自己共役
5. **hypothesis_levels:** A: ambient／B: object／C: object
6. **condition_types:** A: 有限次元性・内積／B: 線形性／C: 対称性
7. **closure_roles:** A: finite-dimensional closure／B: algebraic decomposition／C: symmetry restriction / orthogonality
8. **conclusion_P:** 作用素が互いに直交する一次元固有方向へ完全分解される。
9. **blocked_escape_routes:** A: 連続スペクトル／B: 非線形変形／C: 複素固有値、Jordan block、非直交剪断を除く。
10. **what_fails_if_removed:** A: 無限次元自己共役作用素には固有ベクトル基底を持たないものがある／B: 固有値分解の枠組みが一般にない／C: 実平面の90度回転や Jordan block は直交対角化不能。
11. **what_reappears_if_removed:** A: **R1** — 連続スペクトル・spectral measure／B: **R0** — 一般的補正項なし／C: **R1** — Jordan nilpotent part、複素回転成分、非直交固有方向。
12. **proof_resources:** representative_route: 固有値の存在と直交補空間への帰納／resources: 特性多項式または Rayleigh 商の極値、自己共役性による固有値の実性、固有空間の直交性、有限次元帰納／note: 無限次元版は spectral measure を使う別定理。
13. **closure_style:** 直交分解型
14. **theorem_vs_proof_comment:** 定理は有限次元内積空間と自己共役性を固定する。証明は一つの固有方向を取り、その直交補空間の不変性を使って帰納する。Rayleigh 商や特性多項式は証明資源であり、自己共役条件の代替ではない。
15. **short_comment:** 自己共役性が回転・剪断・非直交結合を排除する。無限次元化すると結論は消えるのでなく、連続スペクトルを含む測度的分解へ移る。

---

## 13. Cayley–Hamilton の定理

1. **theorem_name:** Cayley–Hamilton の定理
2. **domain:** 線形代数・環論
3. **standard_statement:** 有限次元ベクトル空間上の線形作用素 (T) は、自身の特性多項式 (p_T(\lambda)=\det(\lambda I-T)) を満たす。
4. **assumptions_ABC:** A: 有限次元／B: 線形作用素／C: 係数が可換体（または適切な可換環）
5. **hypothesis_levels:** A: ambient／B: object／C: ambient
6. **condition_types:** A: 有限次元性／B: 線形性／C: 可換代数構造
7. **closure_roles:** A: finite-dimensional closure／B: iteration compatibility／C: determinant compatibility
8. **conclusion_P:** (T) の高次冪が次数 (n-1) 以下の冪へ還元される。
9. **blocked_escape_routes:** A: 冪が無限に新しい作用を生成すること／B: 多項式代入不能／C: 係数非可換による行列式論法の破綻を防ぐ。
10. **what_fails_if_removed:** A: (F[x]) 上の (T(f)=xf) は非零多項式で消えない／B: 非線形写像には特性多項式がない／C: 非可換係数では通常形は保証されない。
11. **what_reappears_if_removed:** A: **R1** — 非代数的作用素と無限冪自由度／B: **R0** — 枠組みが定義不能／C: **R1** — 交換子や順序依存性。一般化には別の determinant 概念が必要。
12. **proof_resources:** representative_route: adjugate identity／resources: (\operatorname{adj}(\lambda I-T)(\lambda I-T)=p_T(\lambda)I)、係数比較、行列多項式代入／note: exterior algebra や Jordan 標準形による証明もある。
13. **closure_style:** 冪生成封鎖型
14. **theorem_vs_proof_comment:** 定理は有限次元線形作用素と可換係数環を固定する。証明は形式変数での adjugate 恒等式を作用素恒等式へ移す。adjugate は証明資源であり、有限次元性が冪生成を閉じる本体条件である。
15. **short_comment:** 特性多項式は作用素自身に対する有限の自己制約として働く。無限次元では非代数的な反復自由度が再出現する。

---

## 14. Sylow の定理

1. **theorem_name:** Sylow の定理
2. **domain:** 有限群論
3. **standard_statement:** (|G|=p^nm, p\nmid m) の有限群では位数 (p^n) の部分群が存在し、全 Sylow (p)-部分群は共役で、その個数 (n_p) は (n_p\equiv1\pmod p, n_p\mid m) を満たす。
4. **assumptions_ABC:** A: (G) が有限群／B: (p) が素数／C: (p^n) が (|G|) を割る最大の (p) 冪
5. **hypothesis_levels:** A: object／B: definitional／C: definitional（位数分解から対象を指定）
6. **condition_types:** A: 有限性／B: 素因数構造／C: 最大性・整除条件
7. **closure_roles:** A: finite counting closure／B: prime orbit arithmetic／C: maximality / extension closure
8. **conclusion_P:** 最大 (p)-部分群の存在・共役同値性・個数制約。
9. **blocked_escape_routes:** A: 軌道計数の無限化／B: 複数素因数の混在／C: さらに大きな (p)-部分群への拡張余地を塞ぐ。
10. **what_fails_if_removed:** A: 位数による有限計数が使えない／B: (A_4) は位数12だが位数6の部分群を持たない／C: 非最大 (p)-部分群には同じ共役性・個数公式がない。
11. **what_reappears_if_removed:** A: **R1** — 無限群では局所有限性、最大 (p)-部分群の存在など別条件が必要／B: **R1** — 異なる素因数間の相互作用／C: **R1** — 上位 (p)-部分群への埋込み方と複数共役類。
12. **proof_resources:** representative_route: 群作用と軌道安定化／resources: Lagrange の定理、共役作用、軌道の位数、mod (p) 計数／note: 三つの Sylow 定理で証明段階は異なる。
13. **closure_style:** 素因数軌道封鎖型
14. **theorem_vs_proof_comment:** 定理は有限群と最大素数冪を固定する。証明は群作用の軌道を (p) で数える。群作用は証明資源であり、有限性と素数性が合同式を可能にする条件である。
15. **short_comment:** 候補の存在だけでなく、非一意性を共役と個数合同式の内部へ閉じ込める。条件除去後には部分群の埋込み自由度が戻る。

---

## 15. 中国剰余定理

1. **theorem_name:** 中国剰余定理
2. **domain:** 数論・可換環論
3. **standard_statement:** 単位元を持つ可換環 (R) のイデアル (I_1,\ldots,I_k) が二つずつ comaximal なら、(R/\bigcap I_i\cong\prod R/I_i)。
4. **assumptions_ABC:** A: 単位的可換環／B: (I_i) がイデアル／C: 二つずつ comaximal
5. **hypothesis_levels:** A: ambient／B: object／C: object
6. **condition_types:** A: 代数構造／B: 商構造／C: 独立性・互いに素
7. **closure_roles:** A: ambient algebraic closure／B: quotient compatibility／C: independence / local-to-global connection
8. **conclusion_P:** 各剰余条件の同時解が存在し、(\bigcap I_i) を法として一意。
9. **blocked_escape_routes:** A: 再結合演算不能／B: 合同関係の非整合／C: 共有因子上の局所条件衝突を防ぐ。
10. **what_fails_if_removed:** A・B: 通常の商環写像が定義不能／C: (x\equiv0\pmod4, x\equiv1\pmod6) は解なし。
11. **what_reappears_if_removed:** A: **R0**／B: **R0**／C: **R2** — 非 comaximal な場合、像は積全体でなく重なり上の整合条件を満たす組に限られる。二イデアルでは fiber product (R/I\times_{R/(I+J)}R/J) が現れ、(R/(I\cap J)) と同型になる。
12. **proof_resources:** representative_route: Bézout 型分解／resources: (I_i+I_j=R)、1の分割、自然準同型、kernel の計算／note: 整数版では Bézout の等式を使う。
13. **closure_style:** 局所条件接合型
14. **theorem_vs_proof_comment:** 定理は商を作れる環構造と comaximal な局所条件を固定する。証明は1の分割を構成して各成分を接合する。Bézout 係数は証明資源であり、comaximal 性を具体化する witness である。
15. **short_comment:** comaximal 性を外すと定理は単に消えず、重なり上の互換条件が fiber product として R2 的に戻る。残差分析が特によく働く例である。

---

## 16. 大数の法則

1. **theorem_name:** 大数の法則（Khinchin の弱法則版）
2. **domain:** 確率論
3. **standard_statement:** iid な (X_i) が (E|X_1|<\infty)、(E[X_1]=\mu) を満たすなら、標本平均は (\mu) へ確率収束する。
4. **assumptions_ABC:** A: 独立性／B: 同一分布性／C: 有限絶対一次モーメント
5. **hypothesis_levels:** A: object／B: object／C: object
6. **condition_types:** A: 独立性／B: 同質性／C: 可積分性
7. **closure_roles:** A: independence / correlation suppression／B: normalization target fixation／C: tail control
8. **conclusion_P:** 標本平均が母平均へ確率収束。
9. **blocked_escape_routes:** A: 共通揺らぎ／B: 観測ごとの尺度変化／C: 稀な巨大値による平均支配を防ぐ。
10. **what_fails_if_removed:** A: (X_i=Y)／B: 独立な (X_i=\pm i) は平均が0へ集中しない／C: iid Cauchy の平均は Cauchy のまま。
11. **what_reappears_if_removed:** A: **R1** — 共通因子・長距離相関／B: **R1** — drift、heterogeneity。別の中心化・三角配列条件が必要／C: **R1** — heavy tail と stable scaling、母平均自体の不存在。
12. **proof_resources:** representative_route: truncation を用いる Khinchin 証明／resources: truncation、有限分散版の Chebyshev、不良尾部の評価／note: 有限分散を仮定する初等版もあるが、ここではそれを定理仮定へ昇格させない。
13. **closure_style:** 揺らぎ平均化型
14. **theorem_vs_proof_comment:** 定理は iid と可積分性を固定する。代表証明は切断して有限分散の問題へ移す。Chebyshev 不等式を使うからといって有限分散を元の定理の必須仮定にすると、標準形を不必要に狭める。
15. **short_comment:** 独立性が共通揺らぎを切り、同一分布性が基準点を固定する。条件を外すと相関・drift・heavy tail が別々の未処理成分として現れる。

---

## 17. 中心極限定理

1. **theorem_name:** 中心極限定理（Lindeberg–Lévy 版）
2. **domain:** 確率論
3. **standard_statement:** iid で平均 (\mu)、分散 (0<\sigma^2<\infty) の (X_i) について、((\sum X_i-n\mu)/(\sigma\sqrt n)\Rightarrow N(0,1))。
4. **assumptions_ABC:** A: 独立性／B: 同一分布性／C: 分散が有限かつ正
5. **hypothesis_levels:** A: object／B: object／C: object（正値部分は definitional）
6. **condition_types:** A: 独立性／B: 同質性／C: モーメント条件・非退化性
7. **closure_roles:** A: dependence suppression／B: uniform contribution／C: normalization / tail control
8. **conclusion_P:** 正規化和が標準正規分布へ分布収束。
9. **blocked_escape_routes:** A: 共通依存構造／B: 一項支配／C: heavy tail による別の scaling と退化を除く。
10. **what_fails_if_removed:** A: (X_i=Y)／B: 稀な巨大跳躍を持つ独立非同分布列は Lindeberg 条件を破り得る／C: Cauchy は正規極限でなく、(\sigma=0) は規格化不能。
11. **what_reappears_if_removed:** A: **R1** — dependence-specific limit／B: **R1** — triangular array、Lindeberg 条件、Poisson 型極限など／C: **R1** — stable law と異なる規格化。正規分布は有限分散安定領域の一例になる。
12. **proof_resources:** representative_route: 特性関数／resources: 独立性による積、(t=0) 近傍の二次展開、指数極限、Lévy の連続性定理／note: 特性関数は証明資源であり仮定ではない。
13. **closure_style:** 普遍形収束型
14. **theorem_vs_proof_comment:** 定理は寄与の独立同質性と二次モーメント尺度を固定する。証明は特性関数で和を積へ変え、二次項だけを極限に残す。Taylor 展開を仮定とみなすと、有限分散がなぜ二次項を支配させるかという役割が隠れる。
15. **short_comment:** 条件除去後には単なる失敗でなく、stable law、Poisson 型極限、依存構造固有の極限が現れる。典型的な R1 型定理である。

---

## 18. Bayes の定理

1. **theorem_name:** Bayes の定理
2. **domain:** 確率論・統計学
3. **standard_statement:** 可算分割 (H_i) と (P(B)>0) に対し、(P(H_i|B)=P(B|H_i)P(H_i)/\sum_jP(B|H_j)P(H_j))。
4. **assumptions_ABC:** A: (H_i) が排反かつ網羅的分割／B: (P(B)>0)／C: 通常の条件付き確率が定義される確率空間
5. **hypothesis_levels:** A: object／B: definitional／C: background
6. **condition_types:** A: 分割・網羅性／B: 非退化性／C: 確率構造
7. **closure_roles:** A: probability enclosure／B: nondegeneracy / normalization／C: accounting compatibility
8. **conclusion_P:** 事後確率が尤度×事前確率の正規化として得られる。
9. **blocked_escape_routes:** A: 未列挙仮説への確率漏出／B: 0除算／C: 結合確率の分解不能を防ぐ。
10. **what_fails_if_removed:** A: 分母が (P(B)) にならない／B: 通常の条件付き確率は未定義／C: 枠組み自体がない。
11. **what_reappears_if_removed:** A: **R2** — 「その他」仮説の尤度×事前確率が分母へ追加項として戻る／B: **R1** — regular conditional probability など零事象条件付けの別構造が必要／C: **R0**。
12. **proof_resources:** representative_route: 結合確率の二重分解／resources: (P(A\cap B)=P(A|B)P(B))、全確率の公式／note: ほぼ代数的恒等式で、証明資源と仮定の距離が小さい。
13. **closure_style:** 確率再配分型
14. **theorem_vs_proof_comment:** 定理は仮説分割と正の証拠確率を固定する。証明は同じ結合確率を二方向から分解するだけである。全確率の公式を追加仮定と数えると、確率公理からの会計恒等式である点が見えなくなる。
15. **short_comment:** 分割条件を外すと、欠落仮説は分母の追加項として明示的に戻る。R2 の簡潔な会計例である。

---

## 19. Neyman–Pearson 補題

1. **theorem_name:** Neyman–Pearson 補題
2. **domain:** 数理統計
3. **standard_statement:** 単純仮説 (P_0) 対 (P_1) では、尤度比の大きい領域から棄却し必要なら境界で無作為化する検定が、サイズ (\alpha) 以下の全検定中で最大検出力を持つ。
4. **assumptions_ABC:** A: 両仮説が単純／B: 同一可測空間上の確率測度で尤度比を定義できる／C: (0\le\phi\le1,E_0\phi\le\alpha)
5. **hypothesis_levels:** A: object／B: ambient／C: definitional（最適化問題の許容集合）
6. **condition_types:** A: 仮説特定性／B: 測度構造／C: 制約付き最適化
7. **closure_roles:** A: alternative fixation／B: comparison compatibility／C: normalization / admissible-set closure
8. **conclusion_P:** 尤度比検定が水準 (\alpha) の最強力検定。
9. **blocked_escape_routes:** A: パラメータごとの最適域変化／B: 尤度比較不能／C: 常時棄却という自明解を防ぐ。
10. **what_fails_if_removed:** A: 複合仮説では UMP が存在しないことが多い／B: 尤度比・検出力が未定義／C: (\phi\equiv1) が自明に最大。
11. **what_reappears_if_removed:** A: **R1** — nuisance parameter、異なる対立ごとの power trade-off／B: **R0** — 枠組み不能。ただし二確率測度は (P_0+P_1) で常に共通支配できるため「共通密度」は本質的制限ではない／C: **R1** — 第一種過誤が無制約自由度として戻る。
12. **proof_resources:** representative_route: 点ごとの符号比較／resources: ((\phi^*-\phi)(p_1-kp_0)\ge0) の積分、サイズ制約、境界無作為化／note: 共通支配測度 (P_0+P_1) は構成可能。
13. **closure_style:** 検出力配分型
14. **theorem_vs_proof_comment:** 定理は二つの単純分布とサイズ制約を固定する。証明は各標本点の「対立に有利な度合い」を尤度比で順位付けし、積分比較する。尤度比という証明・構成道具と、単純仮説という対象固定を区別する必要がある。
15. **short_comment:** 許された第一種過誤を最も有利な標本点へ配分する。複合化すると単一順位が崩れ、power trade-off が再出現する。

---

## 20. Brouwer 不動点定理

1. **theorem_name:** Brouwer 不動点定理
2. **domain:** 位相幾何
3. **standard_statement:** 空でないコンパクト凸集合 (K\subset\mathbb R^n) の連続自己写像 (f:K\to K) は不動点を持つ。
4. **assumptions_ABC:** A: (K) が空でないコンパクト凸集合／B: (K\subset\mathbb R^n)／C: (f) が連続自己写像
5. **hypothesis_levels:** A: ambient（空でないは definitional）／B: ambient／C: object
6. **condition_types:** A: コンパクト性・凸性／B: 有限次元性／C: 連続性・自己写像性
7. **closure_roles:** A: domain enclosure / hole suppression／B: finite-dimensional closure／C: continuity / self-map closure
8. **conclusion_P:** 少なくとも一つの不動点が存在。
9. **blocked_escape_routes:** A: 無限遠と穴回避／B: 新座標方向への逐次移動／C: jump と集合外流出を防ぐ。
10. **what_fails_if_removed:** A: 円周の回転、または (x\mapsto x+1)／B: (\ell^2) 単位球の (f(x)=(\sqrt{1-\|x\|^2},x_1,x_2,\ldots))／C: (f(0)=1,f(x)=0 (x>0))。
11. **what_reappears_if_removed:** A: **R1** — hole、retraction、無限遠方向／B: **R1** — infinite-coordinate shift freedom／C: **R1** — jump または外部への displacement。一般に単一補正項ではない。
12. **proof_resources:** representative_route: no-retraction theorem への帰着／resources: 不動点なしから境界への retraction 構成、球の homology または degree、retraction 不可能性／note: Sperner の補題を使う組合せ論的証明もある。
13. **closure_style:** 位相逃走封鎖型
14. **theorem_vs_proof_comment:** 定理は有限次元のコンパクト凸領域と連続自己写像を固定する。証明は不動点がないなら境界への retraction が作れると示し、位相的不可能性へ還元する。homology や Sperner は証明資源で、凸性そのものと同じ層ではない。
15. **short_comment:** 凸性は穴を、コンパクト性は外への逃走を、有限次元性は無限方向への shift を塞ぐ。存在のみを保証し、一意性は閉じない。

---

## 21. Jordan 曲線定理

1. **theorem_name:** Jordan 曲線定理
2. **domain:** 平面位相
3. **standard_statement:** (S^1) の (\mathbb R^2) への埋め込みの像は、平面をちょうど二つの連結成分に分け、その双方の境界となる。
4. **assumptions_ABC:** A: 曲線が閉じている／B: 連続かつ単純で自己交差しない／C: ambient が二次元平面
5. **hypothesis_levels:** A: object／B: object／C: ambient
6. **condition_types:** A: 閉包条件／B: 単純性・連続性／C: 次元条件
7. **closure_roles:** A: boundary completion／B: regularity / multiplicity suppression／C: codimension-one separation
8. **conclusion_P:** 補集合がちょうど二つの連結成分に分かれる。
9. **blocked_escape_routes:** A: 端点間の通路／B: 自己交差による領域増殖／C: 第三方向からの迂回を防ぐ。
10. **what_fails_if_removed:** A: 線分や開弧は平面を二分しない／B: 8の字は三領域を作り得る／C: (\mathbb R^3) 内の単純閉曲線の補集合は連結。
11. **what_reappears_if_removed:** A: **R1** — 端点を回る通路／B: **R1** — 交点ごとの追加領域と planar graph 的自由度／C: **R1** — 余次元2の迂回自由度、さらに knot type が現れる。
12. **proof_resources:** representative_route: polygonal approximationと平面分離／resources: 局所連結性、交点数または winding number、平面の位相／note: Schönflies 定理や homology を用いる別ルートがある。
13. **closure_style:** 迂回路封鎖型
14. **theorem_vs_proof_comment:** 定理は単純閉曲線と二次元 ambient を固定する。証明は平面固有の交差数や winding を使って内外を構成する。それらを仮定と混同すると、曲線の性質だけでなく余次元1という舞台が分離を担うことが見えなくなる。
15. **short_comment:** 閉性が端からの回避を、平面性が上下方向への回避を、単純性が壁の重複を排除する。三次元化すると分離は消え、代わりに knot 構造が現れる。

# III. 横断比較

## A. hypothesis level の分布

厳密な個数は、一つの前提が複数機能を持つため符号化規則に依存する。主タグで数えると、**object と ambient が大半を占める**。object では連続性・線形性・独立性・自己共役性など対象の挙動を縛る条件が、ambient では有限次元性・コンパクト性・完備性・平面性・論理体系など逃走可能性そのものを決める条件が反復して現れた。

background は少数であり、実数の完備性、共通スカラー体、Tarski 意味論、通常の確率構造など、標準定式化へ埋め込まれたものに限定した。definitional は (a<b)、(P(B)>0)、非定数、正分散、非空性など、主張の退化・未定義を防ぐ条件に集中した。

## B. closure role の主要クラスター

1. **逃走・極限回収:** compactness、completeness、domain enclosure。Heine–Borel、Bolzano–Weierstrass、最大最小値、Banach に集中する。
2. **有限次元閉包:** 無限方向、連続スペクトル、無限冪生成を抑える。Heine–Borel、スペクトル定理、Cayley–Hamilton、Brouwer に反復する。
3. **正則性・飛躍禁止:** continuity、differentiability、smoothness。中間値、平均値、Stokes、Gauss–Bonnet に現れる。
4. **会計・正規化:** conservation/accounting、normalization。rank–nullity、Bayes、Neyman–Pearson、中国剰余に現れる。
5. **独立性・対称性制限:** independence、symmetry restriction。大数、中心極限定理、スペクトル定理で、相関・剪断・一項支配を排除する。
6. **局所から大域への接続:** local-to-global connection。Stokes、Gauss–Bonnet、中国剰余、論理コンパクト性で、局所データの接合可能性を保証する。

## C. residual behavior

- **R0 の代表:** 平均値定理の (a<b)、代数学の基本定理の非定数性、rank–nullity の線形性除去。退化または定式化喪失が起きるが、自然な補正項はない。
- **R1 の代表:** 無限次元スペクトル定理の連続スペクトル、中心極限定理の stable law、Banach の非一意性・周期軌道、Jordan 曲線の三次元化による knot freedom。
- **R2 の代表:** Gauss–Bonnet の境界測地曲率、中国剰余の fiber-product compatibility、Bayes の欠落仮説項、Stokes の無限遠境界項。

R2 は全体では少数である。多くの条件除去は、単一の追加項よりも「別の理論へ移る自由度」すなわち R1 を生む。

## D. 特に重要な反例・一般化（5件）

1. **Heine–Borel:** 無限次元 Hilbert 空間の閉単位球。閉かつ有界だけでは、無限方向への逃走を塞げない。
2. **Banach:** (X=(0,1), T(x)=x/2)。収縮は十分でも、完備性がなければ不動点は完備化の側へ逃げる。
3. **Gauss–Bonnet:** 平坦円板。境界なしを外すと測地曲率項が明示的に戻る。
4. **中国剰余:** mod 4 と mod 6。comaximal 性を外すと、積全体でなく重なり上の互換条件を持つ fiber product が現れる。
5. **中心極限定理:** 有限分散を外した heavy-tail 和。正規極限の単純な失敗ではなく、別の規格化と stable law へ遷移する。

## E. 暫定判断

**H2: 定理横断で再現可能な機能分類が見える。**

根拠は、object / ambient / definitional の分離、および「極限回収」「有限次元閉包」「会計・正規化」「局所大域接合」が複数領域で再現したことである。一方、条件除去後に明示的残差項が戻る R2 は Stokes、Gauss–Bonnet、中国剰余、Bayes など一部に偏り、多数は R1 または R0 だった。したがって現段階で H3、すなわち残差再出現まで含む強い普遍パターンを主張する証拠は不足している。

## v1.1 の検査結果

この分析枠は、少なくとも通常の21定理に対して次の区別を安定して記録できた。

- 対象条件と ambient 条件
- 定理文の仮定と proof resources
- 単純な偽化、意味の弱化、枠組みの定義不能
- R1 型の自由度再出現と R2 型の明示的補正項

ただし、`closure_style` はなお説明用の要約ラベルであり、排他的分類ではない。また R0/R1/R2 は同じ条件除去でも採用する一般化の範囲によって変わり得る。Gödel 第1・第2不完全性定理を「閉包反転型」として検査する前に、この依存性を保持したまま使う必要がある。
