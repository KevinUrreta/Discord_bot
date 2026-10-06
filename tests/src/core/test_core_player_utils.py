from unittest.mock import AsyncMock, MagicMock

import pytest

from helpers.player_utils import restore_volume


@pytest.mark.asyncio
async def test_restore_volume_returns_when_player_has_no_guild():
    player = MagicMock()
    player.guild = None

    repository = MagicMock()

    await restore_volume(
        player,
        repository,
    )

    repository.get.assert_not_called()


@pytest.mark.asyncio
async def test_restore_volume_returns_when_guild_is_not_in_database():
    player = MagicMock()

    player.guild = MagicMock()
    player.guild.id = 123
    player.set_volume = AsyncMock()

    repository = MagicMock()
    repository.get = AsyncMock(
        return_value=None,
    )

    await restore_volume(
        player,
        repository,
    )

    repository.get.assert_awaited_once_with(123)
    player.set_volume.assert_not_awaited()


@pytest.mark.asyncio
async def test_restore_volume_restores_saved_volume():
    player = MagicMock()

    player.guild = MagicMock()
    player.guild.id = 123
    player.set_volume = AsyncMock()

    guild_data = MagicMock()
    guild_data.volume = 75

    repository = MagicMock()
    repository.get = AsyncMock(
        return_value=guild_data,
    )

    await restore_volume(
        player,
        repository,
    )

    repository.get.assert_awaited_once_with(123)
    player.set_volume.assert_awaited_once_with(75)
