from unittest.mock import AsyncMock, MagicMock

from src.bot.commands.music.clear import Clear


async def test_clear_not_connected():
    bot = MagicMock()
    cog = Clear(bot)

    ctx = MagicMock()
    ctx.voice_client = None
    ctx.send = AsyncMock()

    await cog.clear.callback(cog, ctx)

    ctx.send.assert_awaited_once()


async def test_clear_empty_queue():
    bot = MagicMock()
    cog = Clear(bot)

    queue = MagicMock()
    queue.is_empty = True

    player = MagicMock()
    player.queue = queue

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.clear.callback(cog, ctx)

    ctx.send.assert_awaited_once()
    queue.clear.assert_not_called()


async def test_clear_queue():
    bot = MagicMock()
    cog = Clear(bot)

    queue = MagicMock()
    queue.is_empty = False

    player = MagicMock()
    player.queue = queue

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.clear.callback(cog, ctx)

    queue.clear.assert_called_once()
    ctx.send.assert_awaited_once()
