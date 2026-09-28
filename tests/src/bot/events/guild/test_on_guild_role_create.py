from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_role_create import GuildRoleCreate


@pytest.mark.asyncio
async def test_on_guild_role_create_logs():
    bot = MagicMock()


    role = MagicMock()

    guild = MagicMock()
    role.guild = guild



    cog = GuildRoleCreate(bot)

    with patch(
        "src.bot.events.guild.on_guild_role_create.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.guild.on_guild_role_create.logger",
    ) as logger:

        await cog.on_guild_role_create(role)

        translate.assert_called_once()

        assert translate.call_args.args[0] == role.guild

        logger.info.assert_called_once_with(
            "translated"
        )
