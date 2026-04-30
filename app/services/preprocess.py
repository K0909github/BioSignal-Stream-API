from app.schemas.predict import PredictRequest
from ml_engine.preprocess import extract_features


def preprocess_signal(payload: PredictRequest) -> dict:
    return extract_features(values=payload.values, sampling_rate=payload.sampling_rate)
