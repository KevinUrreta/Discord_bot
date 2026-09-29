import os

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.core.logging import database_logger, errors_logger
from src.database import Base
from src.locales.i18n import translate


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
                errors_logger.error(
                    translate(
                        None,
                        "database.errors.missing_environment",
                    )
                )

                raise RuntimeError(
                    translate(
                        None,
                        "database.errors.missing_environment",
                    )
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

        database_logger.info(
            translate(
                None,
                "database.connection.started",
            )
        )

    async def create_tables(self):
        try:
            async with self.engine.begin() as connection:
                await connection.run_sync(
                    Base.metadata.create_all
                )
        except Exception as error:
            errors_logger.error(
                translate(
                    None,
                    "database.errors.create_tables",
                    error=error,
                ),
                exc_info=error,
            )
            raise

    async def close(self):
        await self.engine.dispose()

        database_logger.info(
            translate(
                None,
                "database.connection.closed",
            )
        )