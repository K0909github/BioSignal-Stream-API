from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.schemas.predict import PredictRequest, PredictResponse
from app.services.inference import run_inference
from app.services.logger import log_analysis

# v1用のルーター。main.pyで /api/v1 にぶら下げています。
router = APIRouter()


@router.post("/predict", response_model=PredictResponse)
async def predict(payload: PredictRequest, session: AsyncSession = Depends(get_session)) -> PredictResponse:
    # 1) 前処理 + 推論
    result = await run_inference(payload)
    # 2) DBへログ保存
    log_id = await log_analysis(session=session, payload=payload, result=result)
    # 3) APIレスポンスを返す
    return PredictResponse(
        focus_score=result["focus_score"],
        stress_score=result["stress_score"],
        model_version=result["model_version"],
        log_id=log_id,
    )
