from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_role_delete import on_guild_role_delete


@pytest.mark.asyncio
async def test_on_guild_role_delete_logs():
    role = MagicMock()

    with patch("src.bot.events.guild.on_guild_role_delete.logger") as logger:
        await on_guild_role_delete(role)

    logger.info.assert_called_once()
