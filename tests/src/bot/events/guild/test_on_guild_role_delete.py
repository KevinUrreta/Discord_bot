from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_role_delete import GuildRoleDelete


@pytest.mark.asyncio
async def test_on_guild_role_delete_logs():
    bot = MagicMock()


    role = MagicMock()

    guild = MagicMock()
    role.guild = guild



    cog = GuildRoleDelete(bot)

    with patch(
        "src.bot.events.guild.on_guild_role_delete.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.guild.on_guild_role_delete.logger",
    ) as logger:

        await cog.on_guild_role_delete(role)

        translate.assert_called_once()

        assert translate.call_args.args[0] == role.guild

        logger.info.assert_called_once_with(
            "translated"
        )
