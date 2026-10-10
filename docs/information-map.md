# Information / Individual UI figure series

関係はマダラに成立し、概念はその上に輪郭を作る。

このシリーズは生成監査・情報概念監査として独立して読める構成です。VEDと接続可能ですが、VEDの主理論と完全に同一の理論として扱いません。図の順序は読解案内であり、発達・進化・高度化の順序ではありません。

## 公開経路と役割

GitHub Pages base path: `https://yuhki4-hue.github.io/vortical-enclosure-dynamics`

| 経路 | 役割 |
| --- | --- |
| `/information-map/` | 4図の軽量な入口。図の画像・3Dライブラリを読み込まない |
| `/figure1/#view=overview` | 概念境界はどう生成・安定化するか。既存guided viewerとhashを維持 |
| `/figure2a/` | 何を示せば関係を帰属できるか。2Aの2D正本、幅合わせ・拡大・スクロール・SVG download |
| `/figure2b/` | 既存3D exploratory viewer。2D正本へのリンクを明示 |
| `/figure2b/audit/` | 具体的な因果・生成・循環・維持を読む2Bの2D正本 |
| `/figure3/#view=overview` | 身体・維持・感受・作用・履歴・UI・社会制度の境界の重なり |

同じシリーズの各ページに相互ナビと前後移動を設けています。2Aの矢印は成立条件・追加条件・監査関係、2Bの矢印は具体的な因果・生成・維持・更新です。3Dの座標・距離・体積・近接は理論上の距離・階層・含意ではありません。

## 変更前の構造 / Pages

調査時のローカルは `main`、root `index.html` + `.nojekyll` を持つ静的サイトでした。`docs/`、`unsayable/` 等は既存、`figure1/figure2a/figure2b/figure3/information-map` はローカル未配置でした。公開済みの図1・2B・3とローカルが揃っていない状態です。

提供された20261006 ZIPの各index.htmlは、調査時に取得した公開ページとbyte一致しました。ローカルに `.github/workflows` はなく、リモート側にはPagesの動的deployment workflowが見えました。実際のPages設定（branch/path）は未認証APIでは確認できていません。本変更はroot配下静的公開の既存URL構造を維持しますが、Pages設定を変更・断定しません。

ローカルにはこの作業前から大量の未コミット変更があるため、全体pull/mergeや既存変更の取り消しは行っていません。公開済みファイルは指定された最新版パッケージから限定して取り込みました。

## 正本・生成物・監査資料

| 区分 | リポジトリ内の場所 | 管理方針 |
| --- | --- | --- |
| 著者提供のcanonical exported SVG | `assets/information-map/figure-2A-v4.svg`, `figure-2B-v4.svg` | 最新 `*-v4-2.svg` のbyte-exact import。接尾辞`-2`は公開名には持ち込まず、由来を記録 |
| 著者の統合監査 | `audits/information-map/figure-2-v4-audit.html` | 最新 `figure-2-v4-audit-2.html` をbyte-exact保存。DNA＋走化性を含む独立監査本文 |
| 著者の走化性監査 | 同ディレクトリの `chemotaxis-case-audit.html/json` | byte-exact保存。統合HTMLからの既存relative linksも維持 |
| DNA監査の抽出JSON | 同ディレクトリの `dna-case-audit.json` | 最新3D `data.js` の `auditSources.dna` からの構造保持抽出。新規監査・新規承認ではなく、元のproposalOnly等も保持 |
| 著者提供の図1・図3完成HTML | `figure1/index.html`, `figure3/index.html` | ZIPの完成図・文章・操作スクリプトを維持し、共通CSS・シリーズナビだけ追加 |
| 3Dのデータ・実装 | `figure2b/data.js`, `app.js`, `mobile.*`, `style.css`, `vendor/` | 最新ZIP。`data.js`は`twoDConditionsUrl`を`../figure2a/`に接続する変更だけ。app/mobile/科学的データは不変 |
| ローカル管理する表示コード | `information-map/`, `figure2a/`, `figure2b/audit/`, `assets/information-map/series.css`, `svg-viewer.js` | シリーズ入口・表示用wrapper。科学的図を生成・書き換えるコードではない |
| 取り込み元台帳 | `sources/information-map/imports.json` | ZIP・各member・提供単独ファイルのSHA-256。編集可能な科学的生成元コードを装わない |

今回の最新納品には図2SVGを再生成する編集元・generatorは含まれていません。**canonical artifactとeditable canonical sourceは別**です。2A/2Bの科学的変更は、著者の生成元で更新・再監査された新しいSVG/監査のペアを受け取ってから行います。HTML埋め込みSVGを逆変換して生成元にしません。

図1/3の旧boundary-packageには生成スクリプト等がありますが、最新納品の再現手順として確定していないため、今回の公開パッケージに混ぜていません。旧standalone/中間物・Downloads原本は移動・削除していません。整理するなら別途確認後にarchive候補とします。

3D ZIP同梱の `README.md` / `AUDIT.md` は当時の説明を保持しています。統合後のURL・版の位置づけは本書が補足します。フォント・Three.jsの同梱ライセンスは `figure2b/vendor/` に保持しています。

## 版の照合結果

- 2A：2400×5860、SHA-256 `3226e6e74047f4784d8c119469f63ba3a704d19ef559aaa046d6361f667ee26c`
- 2B：2400×6940、SHA-256 `53b9c67eda41c7790b0dc8fbccc5577c436c3597ba0efe3afc114d323a23af26`
- 統合監査HTML内の2図は、`chemA-` / `chemB-` のID衝突防止接頭辞を正規化したXML treeが単独SVGと一致。公開ファイル自体の正規化・再保存はしていません。
- 3D `auditSources.chemotaxis` は提供JSONと構造的に完全一致。表示用41 claimsのrelation/status/evidenceKind/Σ/留保も一致します。これはデータ整合性確認であり、理論内容を独立に再監査したという意味ではありません。
- R/W/K/F/C/N/Mを梯子にせず、Shannon/K&Wは横断解析、M3/N3/Fo/Fsは独立監査。UIは感受―作用―環境帰還の関係構造であり、境界は単一スイッチではないという注意を入口・図2の案内に追加しました。

## ローカル確認と再確認手順

リポジトリrootで `python3 scripts/check_information_map.py` を実行すると、追加HTMLのlocal links/anchors、byte-exact import、既存Explorerコード、SVGの内容一致、監査JSONの整合をネットワークなしで確認できます。

ブラウザ確認はプロジェクトのbase pathを含めて行います。例：リポジトリの親で `python3 -m http.server 8765 --bind 127.0.0.1` を起動し、`http://127.0.0.1:8765/vortical-enclosure-dynamics/information-map/` を開く。検証後はそのサーバーを終了してください。

今回のローカル検証結果：

- `check_information_map.py`：8 HTML、285 local references、原本SHA、SVG一致、走化性41 claimsを確認してPASS。
- 独立一時プロファイルのheadless Chrome：6経路 × 320/390/1440px、計18表示。ページ全体の横はみ出しなし、JavaScript例外なし、当該ページのHTTP resource errorsなし。
- 図1/3：`#view=overview`の初期表示、局所断面への切替、共通ナビ。元のinline SVG/script/styleはすべて提供ZIPと一致。
- 図2A/2B正本：SVG load、拡大で枠内horizontal scroll、幅合わせへの復帰。図2Bの3D：canvas描画、DNA preset、図2Aへの説明リンク。
- 3Dの`app.js`、`mobile.js/css`、元`style.css`、vendorは提供ZIPとSHA一致。科学的`data.js`変更はなし、`twoDConditionsUrl`接続のみ。
- 作業前の全ファイルSHAとの比較：既存ファイルの変更はREADME 2本とroot `index.html`の追記のみ。削除・移動なし。既存の原稿・図・監査記録は不変。
- `git diff --check`：PASS。スクリーンショットと実行ログはrepo外の一時検証ディレクトリへ保存し、公開物には混ぜていない。

新URLの本番公開はまだ行っていません。ローカルHTTP 200はGitHub Pages上でのデプロイ成功を意味しません。既存ページのhash routingを変更していませんが、公開後にも既存リンクを再確認します。

日本語は各提供図の埋め込みフォント／同梱フォントを維持し、新しいwrapperにはsystem-ui、Hiragino、Yu Gothic、Meiryo、sans-serifのfallbackを用います。ローカルChromeのモバイル幅テストは実機iOS/Safari・ATの保証ではありません。

## commit / 公開前の確認

1. 大量の既存未コミット変更を今回の変更に混ぜないこと。root README/indexは今回の追記だけを部分選択すること。
2. リモートとローカルの履歴差分を確認し、既存公開図の別更新を上書きしないこと。自動pull/rebaseはしていません。
3. 最新SVG・監査の採用と、2B入口を3Dのまま維持して2Dを`audit/`に分けた構成を確認すること。
4. Pagesの公開元branch/pathを権限のある画面で確認。設定変更やpushは本作業では実施しないこと。
5. 公開後に4図・入口・監査HTML/JSON・SVG download・既存hash付きURLを実際のbase pathで再確認すること。
