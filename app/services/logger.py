from sqlalchemy.ext.asyncio import AsyncSession

from app.models.analysis_log import AnalysisLog
from app.schemas.predict import PredictRequest


async def log_analysis(session: AsyncSession, payload: PredictRequest, result: dict) -> int:
    # 推論結果とメタ情報をDBに保存
    row = AnalysisLog(
        user_id=payload.user_id,
        device_id=payload.device_id,
        signal_type=payload.signal_type,
        sampling_rate=payload.sampling_rate,
        focus_score=result["focus_score"],
        stress_score=result["stress_score"],
        model_version=result["model_version"],
    )
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row.id
