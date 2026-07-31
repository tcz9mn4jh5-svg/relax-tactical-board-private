# ReLax Tactical Board セットアップ・引き継ぎ

## 正式な場所と公開先

- 別PCで開くiCloudコピー: `/Users/oke/Library/Mobile Documents/com~apple~CloudDocs/ReLax-Tactical-Board`
- このMacで実装・公開に使ったGit作業コピー: `/Users/oke/Developer/relax-tactical-board-private`
- GitHub: `https://github.com/tcz9mn4jh5-svg/relax-tactical-board-private.git`
- 公開URL: `https://tcz9mn4jh5-svg.github.io/relax-tactical-board-private/`
- GitHub Pagesソース: `main` ブランチの `/docs`

元のReLax Board本体 `/Users/oke/Developer/relax-board-dev-private` とは別リポジトリです。本体側をこのアプリのファイルで置き換えないでください。

## 必要なソフト

- Git（確認環境: 2.55.0）
- Python 3.9以上（確認環境: 3.9.6）
- 任意: Streamlit 1.59以上2未満（`requirements.txt` から導入）

このアプリの公開版は静的HTMLなので、Node.js、`package.json`、ビルド処理は不要です。

## iCloudから別PCで開く

1. FinderでiCloud Driveの同期完了を待ちます。雲マークや進捗表示が消えてから開いてください。
2. `ReLax-Tactical-Board` フォルダを開き、`.git`、`docs/index.html`、`static/tactical_board/index.html` があることを確認します。
3. ターミナルで次を実行します。

```bash
cd "$HOME/Library/Mobile Documents/com~apple~CloudDocs/ReLax-Tactical-Board"
git status
git remote -v
git pull --ff-only
python3 -m http.server 8765 --directory docs
```

4. ブラウザで `http://localhost:8765/` を開きます。

iCloud同期とGitを併用するため、2台で同時編集しないでください。作業前後に同期完了を待ち、Gitのcommit/pushまで終えてから別PCへ移ります。

## Git cloneから始める方法（推奨）

iCloudの`.git`競合を避けたい場合は、別PC上でGitHubから新しくcloneする方が安全です。

```bash
git clone https://github.com/tcz9mn4jh5-svg/relax-tactical-board-private.git
cd relax-tactical-board-private
python3 -m http.server 8765 --directory docs
```

## Streamlitで起動する場合

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/streamlit run app.py
```

通常の画面確認とPages公開にはStreamlitは不要です。

## 変更とGitHub Pages公開

編集元は `static/tactical_board/`、Pages公開物は `docs/` です。両方の対応ファイルを同じ内容に保ちます。

```bash
git pull --ff-only
git status
git add static/tactical_board docs TODO.md WORKLOG.md SETUP.md
git commit -m "Describe the change"
git push origin main
```

push後、GitHub Pagesのデプロイ完了を確認し、公開URLを再読み込みします。Service Workerの更新直後は古い画面が残ることがあるため、Safariを閉じて再起動するか、ホーム画面版を一度終了して開き直してください。

## iCloud競合コピーができた場合

- 競合コピーを削除せず、まず両方の `git status`、更新日時、`git log -5 --oneline` を比較します。
- 片方を `archive/` または `backup/` に残してから、必要な差分だけGitで取り込みます。
- `.git` をFinderで手作業マージしないでください。不明な場合はGitHubの最新mainからcloneし直し、競合コピーは保管します。

## 容量・秘密情報

- 現在は `node_modules` もビルド生成物もありません。将来追加する場合、iCloudへ大量同期せずGit管理対象か再生成可能物かを確認してください。
- `.venv` は別PCで作り直せます。巨大になった場合はiCloud外に置く運用も可能です。
- APIキーやパスワードはリポジトリ、HTML、iCloud共有フォルダへ保存しないでください。現在のアプリは秘密情報を必要としません。
