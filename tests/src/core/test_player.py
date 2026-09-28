from unittest.mock import AsyncMock, MagicMock

import pytest

from src.core.player import restore_volume


@pytest.mark.asyncio
async def test_restore_volume_without_guild_does_nothing():
    player = MagicMock()
    player.guild = None

    repository = MagicMock()

    await restore_volume(
        player,
        repository,
    )

    repository.get.assert_not_called()


@pytest.mark.asyncio
async def test_restore_volume_without_database_guild_does_nothing():
    player = MagicMock()
    player.guild.id = 123
    player.set_volume = AsyncMock()

    repository = MagicMock()
    repository.get = AsyncMock(
        return_value=None
    )

    await restore_volume(
        player,
        repository,
    )

    repository.get.assert_awaited_once_with(123)
    player.set_volume.assert_not_awaited()


@pytest.mark.asyncio
async def test_restore_volume_sets_saved_volume():
    player = MagicMock()
    player.guild.id = 123
    player.set_volume = AsyncMock()

    guild_data = MagicMock()
    guild_data.volume = 75

    repository = MagicMock()
    repository.get = AsyncMock(
        return_value=guild_data
    )

    await restore_volume(
        player,
        repository,
    )

    repository.get.assert_awaited_once_with(123)
    player.set_volume.assert_awaited_once_with(75)
