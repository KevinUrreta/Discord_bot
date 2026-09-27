from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_channel_delete import on_guild_channel_delete


@pytest.mark.asyncio
async def test_on_guild_channel_delete_logs():
    channel = MagicMock()

    with patch("src.bot.events.guild.on_guild_channel_delete.logger") as logger:
        await on_guild_channel_delete(channel)

    logger.info.assert_called_once()
