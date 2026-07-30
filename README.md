# ReLax Tactical Board

男子ラクロス専用の独立戦術ボードです。

既存のReLax Boardとは別リポジトリ・別アプリ・別URLで動作します。
既存アプリの入力、分析、履歴、選手登録、設定には依存しません。

## ローカル起動

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/streamlit run app.py
```

## スマートフォン

GitHub Pagesで配信する独立HTTPSアプリをSafariで開きます。
Safariの共有メニューから「ホーム画面に追加」を選択できます。

公開用ファイルは `docs/` にあり、GitHub Pagesの `main` / `/docs` から配信します。

プレーは各端末のブラウザ内に保存されます。ブラウザのサイトデータを削除すると
保存プレーも消えるため、重要な盤面はPDFにも残してください。

## オフライン

独立画面にはmanifestとService Workerがあります。HTTPS環境で一度読み込むと、
主要画面がキャッシュされます。iPhone/iPadではSafariからホーム画面へ追加した後、
機内モードで起動・保存・再読み込みを実機確認してください。
