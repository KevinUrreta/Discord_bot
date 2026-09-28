from unittest.mock import AsyncMock, MagicMock

import pytest

from src.bot.commands.config.prefix import Prefix


def create_context():
    ctx = MagicMock()
    ctx.guild = MagicMock()
    ctx.guild.id = 123
    ctx.send = AsyncMock()
    return ctx


@pytest.mark.asyncio
async def test_prefix_without_guild_does_nothing():
    bot = MagicMock()
    bot.database = MagicMock()

    cog = Prefix(bot)

    ctx = MagicMock()
    ctx.guild = None
    ctx.send = AsyncMock()

    await cog.prefix.callback(cog, ctx)

    ctx.send.assert_not_awaited()


@pytest.mark.asyncio
async def test_prefix_without_argument_shows_prefix():
    bot = MagicMock()
    bot.database = MagicMock()

    cog = Prefix(bot)

    guild_data = MagicMock()
    guild_data.prefix = "!"

    cog.guild_repository.get = AsyncMock(
        return_value=guild_data
    )

    ctx = create_context()

    with pytest.MonkeyPatch.context() as monkeypatch:
        monkeypatch.setattr(
            "src.bot.commands.config.prefix.translate",
            lambda *args, **kwargs: "prefix",
        )

        await cog.prefix.callback(cog, ctx)

    ctx.send.assert_awaited_once_with("prefix")


@pytest.mark.asyncio
async def test_prefix_without_argument_when_guild_not_found():
    bot = MagicMock()
    bot.database = MagicMock()

    cog = Prefix(bot)

    cog.guild_repository.get = AsyncMock(
        return_value=None
    )

    ctx = create_context()

    await cog.prefix.callback(cog, ctx)

    ctx.send.assert_not_awaited()


@pytest.mark.asyncio
async def test_prefix_updates_prefix():
    bot = MagicMock()
    bot.database = MagicMock()

    cog = Prefix(bot)

    cog.guild_repository.update = AsyncMock(
        return_value=MagicMock()
    )

    ctx = create_context()

    with pytest.MonkeyPatch.context() as monkeypatch:
        monkeypatch.setattr(
            "src.bot.commands.config.prefix.translate",
            lambda *args, **kwargs: "changed",
        )

        await cog.prefix.callback(cog, ctx, "?")

    cog.guild_repository.update.assert_awaited_once_with(
        guild_id=123,
        prefix="?",
    )

    ctx.send.assert_awaited_once_with("changed")


@pytest.mark.asyncio
async def test_prefix_update_when_guild_not_found():
    bot = MagicMock()
    bot.database = MagicMock()

    cog = Prefix(bot)

    cog.guild_repository.update = AsyncMock(
        return_value=None
    )

    ctx = create_context()

    await cog.prefix.callback(cog, ctx, "?")

    ctx.send.assert_not_awaited()