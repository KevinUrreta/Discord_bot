import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from src.database.connection import Database


@pytest.mark.asyncio
async def test_database_create_tables(tmp_path):
    database_path = tmp_path / "test.db"

    database = Database(
        f"sqlite+aiosqlite:///{database_path}"
    )

    await database.create_tables()

    async with database.engine.connect() as connection:
        tables = await connection.run_sync(
            lambda sync_connection: (
                sync_connection.dialect.get_table_names(
                    sync_connection
                )
            )
        )

    assert "guilds" in tables
    assert "guild_members" in tables

    await database.close()


@pytest.mark.asyncio
async def test_database_close(tmp_path):
    database_path = tmp_path / "test.db"

    database = Database(
        f"sqlite+aiosqlite:///{database_path}"
    )

    await database.create_tables()
    await database.close()

    assert database.engine.sync_engine.pool is not None


def test_database_init_from_environment():
    with patch.dict(
        "os.environ",
        {
            "POSTGRES_DB": "test_db",
            "POSTGRES_USER": "test_user",
            "POSTGRES_PASSWORD": "test_password",
        },
        clear=True,
    ), patch(
        "src.database.connection.create_async_engine"
    ) as create_engine:
        engine = MagicMock()
        create_engine.return_value = engine

        database = Database()

    create_engine.assert_called_once_with(
        "postgresql+asyncpg://test_user:test_password@postgres:5432/test_db",
        echo=False,
    )

    assert database.engine is engine


def test_database_init_without_environment_variables():
    with patch.dict(
        "os.environ",
        {},
        clear=True,
    ):
        with pytest.raises(
            RuntimeError,
            match="Faltan variables de entorno de PostgreSQL.",
        ):
            Database()


@pytest.mark.asyncio
async def test_database_create_tables_error():
    database = object.__new__(Database)

    connection = MagicMock()
    connection.run_sync = AsyncMock(
        side_effect=Exception("Database error")
    )

    begin_context = MagicMock()
    begin_context.__aenter__ = AsyncMock(
        return_value=connection
    )
    begin_context.__aexit__ = AsyncMock(
        return_value=False
    )

    database.engine = MagicMock()
    database.engine.begin.return_value = begin_context

    with pytest.raises(
        Exception,
        match="Database error",
    ):
        await database.create_tables()