from unittest.mock import AsyncMock, MagicMock

from src.bot.commands.music.queue import Queue


async def test_queue_not_connected():
    bot = MagicMock()
    cog = Queue(bot)

    ctx = MagicMock()
    ctx.voice_client = None
    ctx.send = AsyncMock()

    await cog.queue.callback(cog, ctx)

    ctx.send.assert_awaited_once()


async def test_queue_empty():
    bot = MagicMock()
    cog = Queue(bot)

    queue = MagicMock()
    queue.is_empty = True

    player = MagicMock()
    player.queue = queue

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.queue.callback(cog, ctx)

    ctx.send.assert_awaited_once()


async def test_queue_with_tracks():
    bot = MagicMock()
    cog = Queue(bot)

    track_one = MagicMock()
    track_one.title = "Song 1"

    track_two = MagicMock()
    track_two.title = "Song 2"

    queue = MagicMock()
    queue.is_empty = False
    queue.__iter__.return_value = iter(
        [track_one, track_two]
    )

    player = MagicMock()
    player.queue = queue

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.queue.callback(cog, ctx)

    ctx.send.assert_awaited_once()
