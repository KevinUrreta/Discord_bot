from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.bot.tasks.database_sync import DatabaseSync


@pytest.mark.asyncio
async def test_sync_database_updates_guild_languages():
    bot = MagicMock()

    guild = MagicMock()
    guild.id = 123
    guild.name = "Test Guild"

    bot.guilds = [guild]
    bot.guild_languages = {}

    cog = object.__new__(DatabaseSync)
    cog.bot = bot
    cog.guild_repository = MagicMock()

    guild_data = MagicMock()
    guild_data.language = "en"

    cog.guild_repository.create = AsyncMock(
        return_value=guild_data
    )

    await cog.sync_database.coro(cog)

    cog.guild_repository.create.assert_awaited_once_with(
        guild_id=123,
        name="Test Guild",
    )

    assert bot.guild_languages[123] == "en"


@pytest.mark.asyncio
async def test_before_sync_database_waits_for_bot():
    bot = MagicMock()
    bot.wait_until_ready = AsyncMock()

    cog = object.__new__(DatabaseSync)
    cog.bot = bot

    await cog.before_sync_database()

    bot.wait_until_ready.assert_awaited_once()
