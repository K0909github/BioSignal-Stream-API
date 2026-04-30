# 軽量なPythonベースイメージ
FROM python:3.11-slim

# 作業ディレクトリ
WORKDIR /app

# 依存関係を先に入れてレイヤーキャッシュを活用
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# アプリ本体と推論エンジンをコピー
COPY app /app/app
COPY ml_engine /app/ml_engine

# コンテナ内で公開するポート
EXPOSE 8000

# 起動コマンド
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
