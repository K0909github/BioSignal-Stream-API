from fastapi import FastAPI

from app.api.v1.predict import router as predict_router
from app.db.init_db import init_db

# FastAPIアプリ本体。タイトルはSwagger UIに表示されます。
app = FastAPI(title="BioSignal-Stream-API")


@app.on_event("startup")
async def on_startup() -> None:
    # 起動時にテーブルを作成（開発用の簡易初期化）
    await init_db()


@app.get("/health")
async def health() -> dict:
    # ヘルスチェック用の軽量エンドポイント
    return {"status": "ok"}


# 予測APIを /api/v1 配下に登録
app.include_router(predict_router, prefix="/api/v1")
