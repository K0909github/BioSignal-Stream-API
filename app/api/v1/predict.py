from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.schemas.predict import PredictRequest, PredictResponse
from app.services.inference import run_inference
from app.services.logger import log_analysis

router = APIRouter()


@router.post("/predict", response_model=PredictResponse)
async def predict(payload: PredictRequest, session: AsyncSession = Depends(get_session)) -> PredictResponse:
    result = await run_inference(payload)
    log_id = await log_analysis(session=session, payload=payload, result=result)
    return PredictResponse(
        focus_score=result["focus_score"],
        stress_score=result["stress_score"],
        model_version=result["model_version"],
        log_id=log_id,
    )
