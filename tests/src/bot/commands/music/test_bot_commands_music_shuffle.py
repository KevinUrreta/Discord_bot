from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.bot.commands.music.shuffle import Shuffle


@pytest.mark.asyncio
async def test_shuffle_without_voice_client():
    bot = MagicMock()
    cog = Shuffle(bot)

    ctx = MagicMock()
    ctx.voice_client = None
    ctx.send = AsyncMock()

    with patch(
        "src.bot.commands.music.shuffle.create_embed",
        return_value="embed",
    ):

        await cog.shuffle.callback(
            cog,
            ctx,
        )

    ctx.send.assert_awaited_once()


@pytest.mark.asyncio
async def test_shuffle_with_not_enough_songs():
    bot = MagicMock()
    cog = Shuffle(bot)

    player = MagicMock()
    player.queue.count = 1

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    with patch(
        "src.bot.commands.music.shuffle.create_embed",
        return_value="embed",
    ):

        await cog.shuffle.callback(
            cog,
            ctx,
        )

    ctx.send.assert_awaited_once()


@pytest.mark.asyncio
async def test_shuffle_shuffles_queue():
    bot = MagicMock()
    cog = Shuffle(bot)

    player = MagicMock()
    player.queue.count = 3

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    with patch(
        "src.bot.commands.music.shuffle.create_embed",
        return_value="embed",
    ):

        await cog.shuffle.callback(
            cog,
            ctx,
        )

    player.queue.shuffle.assert_called_once()
    ctx.send.assert_awaited_once()
