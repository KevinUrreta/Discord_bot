from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_role_update import on_guild_role_update


@pytest.mark.asyncio
async def test_on_guild_role_update_logs():
    before = MagicMock()
    after = MagicMock()

    with patch("src.bot.events.guild.on_guild_role_update.logger") as logger:
        await on_guild_role_update(before, after)

    logger.info.assert_called_once()
