from unittest.mock import AsyncMock, MagicMock

from src.bot.commands.music.shuffle import Shuffle


async def test_shuffle_not_connected():
    bot = MagicMock()
    cog = Shuffle(bot)

    ctx = MagicMock()
    ctx.voice_client = None
    ctx.send = AsyncMock()

    await cog.shuffle.callback(cog, ctx)

    ctx.send.assert_awaited_once()


async def test_shuffle_empty_queue():
    bot = MagicMock()
    cog = Shuffle(bot)

    queue = MagicMock()
    queue.is_empty = True

    player = MagicMock()
    player.queue = queue

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.shuffle.callback(cog, ctx)

    ctx.send.assert_awaited_once()
    queue.shuffle.assert_not_called()


async def test_shuffle_queue():
    bot = MagicMock()
    cog = Shuffle(bot)

    queue = MagicMock()
    queue.is_empty = False

    player = MagicMock()
    player.queue = queue

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.shuffle.callback(cog, ctx)

    queue.shuffle.assert_called_once()
    ctx.send.assert_awaited_once()
