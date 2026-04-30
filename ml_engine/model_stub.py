def predict_scores(features: dict) -> dict:
    # テスト用の決定論的な疑似モデル
    mean = float(features.get("mean", 0.0))
    std = float(features.get("std", 0.0))
    sr = float(features.get("sampling_rate", 1.0))

    focus = max(0.0, min(1.0, 0.6 + mean * 0.2 - std * 0.1))
    stress = max(0.0, min(1.0, 0.4 + std * 0.2 + (sr / 4096.0) * 0.1))

    return {
        "focus_score": round(focus, 4),
        "stress_score": round(stress, 4),
        "model_version": "stub-0.1.0",
    }
