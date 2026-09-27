from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_channel_create import on_guild_channel_create


@pytest.mark.asyncio
async def test_on_guild_channel_create_logs():
    channel = MagicMock()

    with patch("src.bot.events.guild.on_guild_channel_create.logger") as logger:
        await on_guild_channel_create(channel)

    logger.info.assert_called_once()
