from unittest.mock import AsyncMock, MagicMock

from src.bot.commands.music.stop import Stop


async def test_stop_not_connected():
    bot = MagicMock()
    cog = Stop(bot)

    ctx = MagicMock()
    ctx.voice_client = None
    ctx.send = AsyncMock()

    await cog.stop.callback(cog, ctx)

    ctx.send.assert_awaited_once()


async def test_stop_playback():
    bot = MagicMock()
    cog = Stop(bot)

    queue = MagicMock()
    player = MagicMock()
    player.queue = queue
    player.stop = AsyncMock()

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.stop.callback(cog, ctx)

    queue.clear.assert_called_once()
    player.stop.assert_awaited_once()
    ctx.send.assert_awaited_once()
