# ReLax Tactical Board 作業記録

## 2026-07-31

- 作業対象を独立アプリ `/Users/oke/Developer/relax-tactical-board-private` に限定。
- 元の ReLax Board `/Users/oke/Developer/relax-board-dev-private` は読み取り確認のみ。既存の未追跡 `backups/` を含め変更していない。
- `codex/mobile-display-fullscreen` ブランチを作成。
- 変更前の `static/tactical_board/index.html`、`docs/index.html`、`README.md`、`IMPLEMENTATION_STATUS.md` を `backup/20260731_mobile_display_fullscreen/` に複製。
- 現行保存形式を確認。駒座標は相対値、描画座標は固定 viewBox 基準で、通常表示と全画面の切替に適した構造。
- 現行の保存・自動保存は状態オブジェクト全体を保持するため、`displaySettings` を状態へ追加し、古いデータには読込時の既定値を補う方針とした。
- 新規プレーの青10人・赤10人の背番号と名前を空欄化。既存保存データは読込時に値を文字列へ正規化するだけで、背番号・名前を保持する。
- ポジション編集を AT / MF / DF / G / FO / SSDM / LMF / その他の選択式へ変更。選択肢外の既存値は「その他」欄へ復元する。
- 駒の見た目をスマートフォンで35pxへ小型化し、操作判定は48pxを維持。表示行数ごとのフォント調整と長い名前の省略を追加。
- `displaySettings`（ポジション、背番号、名前）を状態へ追加。初期値は ON / OFF / OFF。自動保存、保存済みプレー、Undo/Redo、印刷PDFへ状態ごと反映。
- Fullscreen APIとアプリ内疑似全画面を併用。`visualViewport`、`100dvh`、セーフエリアを考慮し、全画面ではヘッダー・左右パネル・通常操作バーを非表示化。
- 全画面の終了ボタン、呼び出し式ツールメニュー、移動・矢印・点線・ペン・追加・その他・Undo・Redoを実装。
- 390×844、844×390、1024×1366、1366×1024で確認。スマートフォン横画面の既存最小高さによるスクロールと縦横比崩れを修正。
- ブラウザ確認: 初期表示、編集、その他ポジション、表示3項目/全OFF、設定再読込、保存/読込、小型駒ドラッグ、全画面メニュー、矢印描画、全画面解除後の座標保持、Undo/Redo、PDF出力準備データ。
- 静的確認: JavaScript構文、旧version 1データの背番号/名前保持、旧データへの表示設定既定値追加、長い名前の省略。
- コミット `1bdb833` を独立アプリの `main` へ反映し、GitHub Pagesのビルド完了を確認。公開HTMLとService Worker v4をオンライン取得して新機能を確認。
- 公開URL: `https://tcz9mn4jh5-svg.github.io/relax-tactical-board-private/`
- 実機確認として iPhone Safari、ホーム画面追加版PWA、Apple Pencil、オフライン再起動を残す。
