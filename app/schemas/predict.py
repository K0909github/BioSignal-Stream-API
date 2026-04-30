from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    user_id: str = Field(..., min_length=1, max_length=64)
    device_id: str = Field(..., min_length=1, max_length=64)
    signal_type: str = Field(..., pattern="^(EEG|PPG)$")
    sampling_rate: int = Field(..., ge=1, le=4096)
    values: list[float] = Field(..., min_length=4)


class PredictResponse(BaseModel):
    focus_score: float
    stress_score: float
    model_version: str
    log_id: int
