import pytest

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
