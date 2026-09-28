from unittest.mock import AsyncMock, MagicMock

import pytest
import wavelink

from src.bot.events.other.on_wavelink_track_end import (
    On_wavelink_track_end,
)


@pytest.mark.asyncio
async def test_track_end_without_player_does_nothing():
    bot = MagicMock()

    payload = MagicMock()
    payload.player = None

    cog = On_wavelink_track_end(bot)

    await cog.on_wavelink_track_end(payload)


@pytest.mark.asyncio
async def test_track_end_with_empty_normal_queue_does_nothing():
    bot = MagicMock()

    player = MagicMock()
    player.queue.is_empty = True
    player.queue.mode = wavelink.QueueMode.normal
    player.play = AsyncMock()

    payload = MagicMock()
    payload.player = player

    cog = On_wavelink_track_end(bot)

    await cog.on_wavelink_track_end(payload)

    player.queue.get.assert_not_called()
    player.play.assert_not_awaited()


@pytest.mark.asyncio
async def test_track_end_plays_next_track():
    bot = MagicMock()

    player = MagicMock()
    player.queue.is_empty = False
    player.queue.mode = wavelink.QueueMode.loop_all

    track = MagicMock()

    player.queue.get.return_value = track
    player.play = AsyncMock()

    payload = MagicMock()
    payload.player = player

    cog = On_wavelink_track_end(bot)

    await cog.on_wavelink_track_end(payload)

    player.queue.get.assert_called_once()
    player.play.assert_awaited_once_with(track)