def extract_features(values: list[float], sampling_rate: int) -> dict:
    if not values:
        return {"mean": 0.0, "std": 0.0, "sampling_rate": sampling_rate}

    mean = sum(values) / len(values)
    variance = sum((v - mean) ** 2 for v in values) / len(values)
    std = variance ** 0.5

    return {
        "mean": mean,
        "std": std,
        "sampling_rate": sampling_rate,
    }
