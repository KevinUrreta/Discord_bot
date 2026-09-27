from unittest.mock import AsyncMock, MagicMock

from src.bot.commands.music.skip import Skip


async def test_skip_not_connected():
    bot = MagicMock()
    cog = Skip(bot)

    ctx = MagicMock()
    ctx.voice_client = None
    ctx.send = AsyncMock()

    await cog.skip.callback(cog, ctx)

    ctx.send.assert_awaited_once()


async def test_skip_without_song():
    bot = MagicMock()
    cog = Skip(bot)

    player = MagicMock()
    player.playing = False
    player.skip = AsyncMock()

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.skip.callback(cog, ctx)

    ctx.send.assert_awaited_once()
    player.skip.assert_not_awaited()


async def test_skip_song():
    bot = MagicMock()
    cog = Skip(bot)

    player = MagicMock()
    player.playing = True
    player.skip = AsyncMock()

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.skip.callback(cog, ctx)

    player.skip.assert_awaited_once_with(force=True)
    ctx.send.assert_awaited_once()
