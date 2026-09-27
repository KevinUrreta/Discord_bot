from unittest.mock import AsyncMock, MagicMock, patch

import wavelink

from src.bot.commands.music.loop import Loop


async def test_loop_not_connected():
    bot = MagicMock()
    cog = Loop(bot)

    ctx = MagicMock()
    ctx.voice_client = None
    ctx.send = AsyncMock()

    await cog.loop.callback(cog, ctx)

    ctx.send.assert_awaited_once()


async def test_loop_without_song():
    bot = MagicMock()
    cog = Loop(bot)

    player = MagicMock()
    player.current = None

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.loop.callback(cog, ctx)

    ctx.send.assert_awaited_once()


async def test_loop_enable():
    bot = MagicMock()
    cog = Loop(bot)

    player = MagicMock()
    player.current = MagicMock()
    player.queue.mode = wavelink.QueueMode.normal

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.loop.callback(cog, ctx)

    assert player.queue.mode == wavelink.QueueMode.loop
    ctx.send.assert_awaited_once()


async def test_loop_disable():
    bot = MagicMock()
    cog = Loop(bot)

    player = MagicMock()
    player.current = MagicMock()
    player.queue.mode = wavelink.QueueMode.loop

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.loop.callback(cog, ctx)

    assert player.queue.mode == wavelink.QueueMode.normal
    ctx.send.assert_awaited_once()
