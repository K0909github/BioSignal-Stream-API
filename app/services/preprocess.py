from app.schemas.predict import PredictRequest
from ml_engine.preprocess import extract_features


def preprocess_signal(payload: PredictRequest) -> dict:
    # 生体信号の特徴量抽出（ここを本格的な前処理に差し替える）
    return extract_features(values=payload.values, sampling_rate=payload.sampling_rate)
