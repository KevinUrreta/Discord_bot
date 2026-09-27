from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_channel_update import on_guild_channel_update


@pytest.mark.asyncio
async def test_on_guild_channel_update_logs():
    before = MagicMock()
    after = MagicMock()

    with patch("src.bot.events.guild.on_guild_channel_update.logger") as logger:
        await on_guild_channel_update(before, after)

    logger.info.assert_called_once()
