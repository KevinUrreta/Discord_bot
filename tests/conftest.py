import pytest_asyncio

from src.database.connection import Database


@pytest_asyncio.fixture
async def database(tmp_path):
    database_path = tmp_path / "test.db"

    database = Database(
        f"sqlite+aiosqlite:///{database_path}"
    )

    await database.create_tables()

    yield database

    await database.close()