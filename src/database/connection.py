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
    """
    Gestiona la conexión asíncrona con la base de datos.
    """
    def __init__(self, database_url: str | None = None):
        """
        Inicializa la conexión con la base de datos.

        Si no se proporciona una URL de conexión, se utilizan las variables
        de entorno `POSTGRES_DB`, `POSTGRES_USER` y `POSTGRES_PASSWORD`
        para construirla.

        :param database_url: URL de conexión a la base de datos.
        :raises RuntimeError: Si falta alguna de las variables de entorno
        """
        if database_url is None:
            database = os.getenv("POSTGRES_DB")
            user = os.getenv("POSTGRES_USER")
            password = os.getenv("POSTGRES_PASSWORD")

            if not all((database, user, password)):
                errors_logger.error(translate(
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

            database_url = f"postgresql+asyncpg://{user}:{password}@postgres:5432/{database}"

        self.engine: AsyncEngine = create_async_engine(database_url, echo=False)
        self.session_factory = async_sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

        database_logger.info(translate(
                None,
                "database.logs.connection.started",
            ))

    async def create_tables(self):
        """
        Crea las tablas definidas en los modelos de la aplicación.

        :raises Excepcion: Si se produce un error durante la creación de las tablas.
        :return: None
        """
        try:
            async with self.engine.begin() as connection:
                await connection.run_sync(Base.metadata.create_all)
        except Exception as error:
            errors_logger.error(
                translate(
                    None,
                    "database.logs.errors.create_tables",
                    error=error,
                ),
                exc_info=error,
            )
            raise

    async def close(self):
        """
        Cierra la conexión con la base de datos.

        :return: None
        """
        await self.engine.dispose()

        database_logger.info(translate(
                None,
                "database.logs.connection.closed",
            ))