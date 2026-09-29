from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.bot.tasks.database_sync import DatabaseSync


def create_bot():
    bot = MagicMock()

    bot.database = MagicMock()
    bot.guild_languages = {}
    bot.guilds = []

    bot.wait_until_ready = AsyncMock()

    return bot


@pytest.mark.asyncio
async def test_database_sync_creates_repositories():
    bot = create_bot()

    with patch(
        "src.bot.tasks.database_sync.GuildRepository"
    ) as guild_repository, patch(
        "src.bot.tasks.database_sync.MemberRepository"
    ) as member_repository, patch(
        "src.bot.tasks.database_sync.set_guild_languages"
    ) as set_languages, patch(
        "discord.ext.tasks.Loop.start"
    ) as start:

        cog = DatabaseSync(bot)

        guild_repository.assert_called_once_with(
            bot.database,
        )

        member_repository.assert_called_once_with(
            bot.database,
        )

        set_languages.assert_called_once_with(
            bot.guild_languages,
        )

        start.assert_called_once()

        assert cog.bot is bot


def test_cog_unload_cancels_task():
    bot = create_bot()

    with patch(
        "src.bot.tasks.database_sync.GuildRepository"
    ), patch(
        "src.bot.tasks.database_sync.MemberRepository"
    ), patch(
        "src.bot.tasks.database_sync.set_guild_languages"
    ), patch(
        "discord.ext.tasks.Loop.start"
    ), patch(
        "discord.ext.tasks.Loop.cancel"
    ) as cancel:

        cog = DatabaseSync(bot)

        cog.cog_unload()

        cancel.assert_called_once()
