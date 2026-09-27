from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_stickers_update import on_guild_stickers_update


@pytest.mark.asyncio
async def test_on_guild_stickers_update_logs():
    guild = MagicMock()
    before = MagicMock()
    after = MagicMock()

    with patch("src.bot.events.guild.on_guild_stickers_update.logger") as logger:
        await on_guild_stickers_update(guild, before, after)

    logger.info.assert_called_once()
