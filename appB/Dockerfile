# ベースイメージを指定
FROM python:3.12

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# requirements.txtをコンテナにコピー
# 開発時はdocker-compose.ymlで指定したvolumeを使うため、このCOPYは不要
# 逆に本番時は、docker-compose.ymlで指定したvolumeを使わず、このCOPYを使う
COPY requirements.lock .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.lock

# アプリケーションのソースコードをコピー
# 開発時はdocker-compose.ymlで指定したvolumeを使うため、このCOPYは不要
# 逆に本番時は、docker-compose.ymlで指定したvolumeを使わず、このCOPYを使う
# COPY ./ ./app

# コンテナ起動時の実行コマンド
# CMD ["python", "appB_main.py"]