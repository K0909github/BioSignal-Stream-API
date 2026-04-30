from app.schemas.predict import PredictRequest
from app.services.preprocess import preprocess_signal
from ml_engine.model_stub import predict_scores


async def run_inference(payload: PredictRequest) -> dict:
    features = preprocess_signal(payload)
    scores = predict_scores(features)
    return {
        "focus_score": scores["focus_score"],
        "stress_score": scores["stress_score"],
        "model_version": scores["model_version"],
    }
