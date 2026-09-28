from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_role_update import GuildRoleUpdate


@pytest.mark.asyncio
async def test_on_guild_role_update_logs():
    bot = MagicMock()


    before = MagicMock()
    after = MagicMock()

    guild = MagicMock()
    after.guild = guild



    cog = GuildRoleUpdate(bot)

    with patch(
        "src.bot.events.guild.on_guild_role_update.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.guild.on_guild_role_update.logger",
    ) as logger:

        await cog.on_guild_role_update(before, after)

        translate.assert_called_once()

        assert translate.call_args.args[0] == after.guild

        logger.info.assert_called_once_with(
            "translated"
        )
