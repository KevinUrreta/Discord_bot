from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.bot.commands.config.language import Language


def create_context():
    ctx = MagicMock()
    ctx.guild = MagicMock()
    ctx.guild.id = 123
    ctx.send = AsyncMock()
    return ctx


@pytest.mark.asyncio
async def test_language_without_guild_does_nothing():
    bot = MagicMock()
    bot.database = MagicMock()

    cog = Language(bot)

    ctx = MagicMock()
    ctx.guild = None
    ctx.send = AsyncMock()

    await cog.language.callback(cog, ctx)

    ctx.send.assert_not_awaited()


@pytest.mark.asyncio
async def test_language_without_argument_shows_current_language():
    bot = MagicMock()
    bot.database = MagicMock()
    bot.guild_languages = {123: "en"}

    ctx = create_context()

    with patch(
        "src.bot.commands.config.language.translate",
        return_value="current",
    ):

        cog = Language(bot)

        await cog.language.callback(cog, ctx)

        ctx.send.assert_awaited_once_with("current")


@pytest.mark.asyncio
async def test_language_invalid_language():
    bot = MagicMock()
    bot.database = MagicMock()
    bot.guild_languages = {}

    ctx = create_context()

    with patch(
        "src.bot.commands.config.language.translate",
        side_effect=["invalid", "available"],
    ):

        cog = Language(bot)

        await cog.language.callback(cog, ctx, "xx")

        assert ctx.send.await_count == 2


@pytest.mark.asyncio
async def test_language_updates_language():
    bot = MagicMock()
    bot.database = MagicMock()
    bot.guild_languages = {}

    ctx = create_context()

    with patch(
        "src.bot.commands.config.language.translate",
        return_value="changed",
    ):

        cog = Language(bot)

        guild_data = MagicMock()

        cog.guild_repository.update = AsyncMock(
            return_value=guild_data
        )

        await cog.language.callback(cog, ctx, "EN")

        cog.guild_repository.update.assert_awaited_once_with(
            guild_id=123,
            language="en",
        )

        assert bot.guild_languages[123] == "en"
        ctx.send.assert_awaited_once_with("changed")
