# ベースイメージを指定
FROM python:3.12

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# requirements.txtをコンテナにコピー
COPY requirements.lock .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.lock

# アプリケーションのソースコードをコピー
COPY ./ ./app

# コンテナ起動時の実行コマンド
CMD ["python", "app2_main.py"]