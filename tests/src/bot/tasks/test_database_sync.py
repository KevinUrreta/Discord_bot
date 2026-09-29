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
        source="sync_database",
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


@pytest.mark.asyncio
async def test_database_sync_init():
    bot = MagicMock()
    bot.database = MagicMock()
    bot.guild_languages = {}

    fake_loop = MagicMock()

    with patch(
        "src.bot.tasks.database_sync.GuildRepository"
    ) as guild_repository, patch(
        "src.bot.tasks.database_sync.set_guild_languages"
    ) as set_languages, patch.object(
        DatabaseSync,
        "sync_database",
        new=fake_loop,
    ):
        cog = DatabaseSync(bot)

    guild_repository.assert_called_once_with(
        bot.database
    )

    set_languages.assert_called_once_with(
        bot.guild_languages
    )

    fake_loop.start.assert_called_once()

    assert cog.bot is bot


def test_database_sync_cog_unload():
    bot = MagicMock()

    cog = object.__new__(DatabaseSync)
    cog.bot = bot

    cog.sync_database = MagicMock()

    cog.cog_unload()

    cog.sync_database.cancel.assert_called_once()