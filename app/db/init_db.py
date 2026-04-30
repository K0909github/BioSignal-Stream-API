import asyncio

from sqlalchemy.exc import SQLAlchemyError

from app.db.session import engine
from app.models.analysis_log import Base


async def init_db() -> None:
    # DBの起動を待ちながらテーブルを作成（開発用の簡易初期化）
    max_retries = 10
    for attempt in range(1, max_retries + 1):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            return
        except SQLAlchemyError:
            if attempt == max_retries:
                raise
            await asyncio.sleep(1.0)
