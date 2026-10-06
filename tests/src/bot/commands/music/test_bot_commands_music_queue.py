from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.app.commands.music.queue import Queue


@pytest.mark.asyncio
async def test_queue_without_voice_client():
    bot = MagicMock()
    cog = Queue(bot)

    ctx = MagicMock()
    ctx.voice_client = None
    ctx.send = AsyncMock()

    with patch(
            "src.app.commands.music.queue.create_embed",
        return_value="embed",
    ):

        await cog.queue.callback(
            cog,
            ctx,
        )

    ctx.send.assert_awaited_once()


@pytest.mark.asyncio
async def test_queue_with_empty_queue():
    bot = MagicMock()
    cog = Queue(bot)

    player = MagicMock()
    player.queue.is_empty = True

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    with patch(
            "src.app.commands.music.queue.create_embed",
        return_value="embed",
    ):

        await cog.queue.callback(
            cog,
            ctx,
        )

    ctx.send.assert_awaited_once()
