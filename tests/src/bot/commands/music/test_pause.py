from unittest.mock import AsyncMock, MagicMock

from src.bot.commands.music.pause import Pause


async def test_pause_not_connected():
    bot = MagicMock()
    cog = Pause(bot)

    ctx = MagicMock()
    ctx.voice_client = None
    ctx.send = AsyncMock()

    await cog.pause.callback(cog, ctx)

    ctx.send.assert_awaited_once()


async def test_pause_without_song():
    bot = MagicMock()
    cog = Pause(bot)

    player = MagicMock()
    player.playing = False
    player.pause = AsyncMock()

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.pause.callback(cog, ctx)

    ctx.send.assert_awaited_once()
    player.pause.assert_not_awaited()


async def test_pause_song():
    bot = MagicMock()
    cog = Pause(bot)

    player = MagicMock()
    player.playing = True
    player.pause = AsyncMock()

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.pause.callback(cog, ctx)

    player.pause.assert_awaited_once_with(True)
    ctx.send.assert_awaited_once()
