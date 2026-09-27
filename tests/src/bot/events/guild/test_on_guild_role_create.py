from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_role_create import on_guild_role_create


@pytest.mark.asyncio
async def test_on_guild_role_create_logs():
    role = MagicMock()

    with patch("src.bot.events.guild.on_guild_role_create.logger") as logger:
        await on_guild_role_create(role)

    logger.info.assert_called_once()
