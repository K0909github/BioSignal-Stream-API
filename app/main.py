from fastapi import FastAPI

from app.api.v1.predict import router as predict_router
from app.db.init_db import init_db

app = FastAPI(title="BioSignal-Stream-API")


@app.on_event("startup")
async def on_startup() -> None:
    await init_db()


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


app.include_router(predict_router, prefix="/api/v1")
