from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # 環境変数 DATABASE_URL で上書き可能
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/biosignal"


# 設定を1箇所にまとめて読み出す
settings = Settings()
