import pytest

from src.infrastructure.database.connection.connection import Database


def test_database_raises_when_environment_is_missing(
    monkeypatch,
):
    monkeypatch.delenv(
        "POSTGRES_DB",
        raising=False,
    )

    monkeypatch.delenv(
        "POSTGRES_USER",
        raising=False,
    )

    monkeypatch.delenv(
        "POSTGRES_PASSWORD",
        raising=False,
    )

    with pytest.raises(RuntimeError):
        Database()


def test_database_accepts_explicit_url():
    database = Database(
        "sqlite+aiosqlite:///:memory:",
    )

    assert database.engine is not None


@pytest.mark.asyncio
async def test_close_disposes_engine():
    database = Database(
        "sqlite+aiosqlite:///:memory:",
    )

    await database.close()
