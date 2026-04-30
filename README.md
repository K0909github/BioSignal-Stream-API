# BioSignal-Stream-API

Scalable real-time EEG/PPG analysis API for learning full-stack ML service development.

## Goals
- Accept biosignal streams from browser/mobile clients.
- Preprocess signals and run inference (stubbed here, swap with Mamba/U-Mamba).
- Persist per-user logs and device metadata to PostgreSQL.
- Provide a production-style, testable FastAPI service.

## Quick Start
1) Build and run

```bash
docker compose up --build
```

2) Test the API

```bash
curl -X POST http://localhost:8000/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user-001",
    "device_id": "device-abc",
    "signal_type": "EEG",
    "sampling_rate": 256,
    "values": [0.1, 0.2, 0.15, 0.05, 0.0, -0.1, -0.05]
  }'
```

## Project Structure
```
.
├── app/
│   ├── api/           # API endpoints
│   ├── core/          # config and settings
│   ├── db/            # database session and init
│   ├── models/        # SQLAlchemy models
│   ├── schemas/       # Pydantic request/response
│   └── services/      # preprocess, inference, logging
├── ml_engine/         # inference stubs (replace with Mamba/U-Mamba)
├── docker/            # Dockerfiles
├── tests/             # tests (empty scaffold)
└── docker-compose.yml
```

## Next Steps
- Replace `ml_engine/model_stub.py` with your trained model.
- Add real preprocessing in `ml_engine/preprocess.py` (MNE, NeuroKit, etc.).
- Add Alembic migrations if you want versioned schemas.
- Add authentication and rate limiting.
