from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.bot.events.other.on_wavelink_track_start import (
    On_wavelink_track_start,
)


@pytest.mark.asyncio
async def test_track_start_restores_volume():
    bot = MagicMock()
    bot.database = MagicMock()

    payload = MagicMock()
    payload.player = MagicMock()

    with patch(
        "src.bot.events.other.on_wavelink_track_start.GuildRepository"
    ) as repository_class, patch(
        "src.bot.events.other.on_wavelink_track_start.restore_volume",
        new_callable=AsyncMock,
    ) as restore_volume:

        repository = repository_class.return_value

        cog = On_wavelink_track_start(bot)

        await cog.on_wavelink_track_start(payload)

        restore_volume.assert_awaited_once_with(
            payload.player,
            repository,
        )
