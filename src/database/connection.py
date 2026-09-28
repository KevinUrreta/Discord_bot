import os

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.database import Base


class Database:
    def __init__(
        self,
        database_url: str | None = None,
    ):
        if database_url is None:
            database = os.getenv("POSTGRES_DB")
            user = os.getenv("POSTGRES_USER")
            password = os.getenv("POSTGRES_PASSWORD")

            if not all((database, user, password)):
                raise RuntimeError(
                    "Faltan variables de entorno de PostgreSQL."
                )

            database_url = (
                "postgresql+asyncpg://"
                f"{user}:{password}@postgres:5432/{database}"
            )

        self.engine: AsyncEngine = create_async_engine(
            database_url,
            echo=False,
        )

        self.session_factory = async_sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    async def create_tables(self):
        async with self.engine.begin() as connection:
            await connection.run_sync(
                Base.metadata.create_all
            )

    async def close(self):
        await self.engine.dispose()