import os

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.core.logging import database_logger, errors_logger
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
                database_logger.error(
                    "Faltan variables de entorno de PostgreSQL."
                )
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

        database_logger.info(
            "Conexión con la base de datos inicializada."
        )

    async def create_tables(self):
        database_logger.info(
            "Creando tablas de la base de datos."
        )

        try:
            async with self.engine.begin() as connection:
                await connection.run_sync(
                    Base.metadata.create_all
                )
        except Exception as error:
            errors_logger.error(
                "Error al crear las tablas de la base de datos: %s",
                error,
                exc_info=error,
            )
            raise

        database_logger.info(
            "Tablas de la base de datos creadas correctamente."
        )

    async def close(self):
        database_logger.info(
            "Cerrando conexión con la base de datos."
        )

        await self.engine.dispose()

        database_logger.info(
            "Conexión con la base de datos cerrada."
        )