from unittest.mock import AsyncMock, MagicMock

from src.bot.commands.music.remove import Remove


async def test_remove_not_connected():
    bot = MagicMock()
    cog = Remove(bot)

    ctx = MagicMock()
    ctx.voice_client = None
    ctx.send = AsyncMock()

    await cog.remove.callback(cog, ctx, 1)

    ctx.send.assert_awaited_once()


async def test_remove_empty_queue():
    bot = MagicMock()
    cog = Remove(bot)

    queue = MagicMock()
    queue.is_empty = True

    player = MagicMock()
    player.queue = queue

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.remove.callback(cog, ctx, 1)

    ctx.send.assert_awaited_once()


async def test_remove_invalid_position():
    bot = MagicMock()
    cog = Remove(bot)

    queue = MagicMock()
    queue.is_empty = False

    track = MagicMock()
    track.title = "Song"

    queue.__iter__.return_value = iter([track])

    player = MagicMock()
    player.queue = queue

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.remove.callback(cog, ctx, 2)

    ctx.send.assert_awaited_once()
    queue.remove.assert_not_called()


async def test_remove_track():
    bot = MagicMock()
    cog = Remove(bot)

    queue = MagicMock()
    queue.is_empty = False

    track = MagicMock()
    track.title = "Song"

    queue.__iter__.return_value = iter([track])

    player = MagicMock()
    player.queue = queue

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.remove.callback(cog, ctx, 1)

    queue.remove.assert_called_once_with(track)
    ctx.send.assert_awaited_once()
