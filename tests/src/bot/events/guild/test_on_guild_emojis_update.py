from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_emojis_update import GuildEmojisUpdate


@pytest.mark.asyncio
async def test_on_guild_emojis_update_logs():
    bot = MagicMock()


    guild = MagicMock()
    before = MagicMock()
    after = MagicMock()



    cog = GuildEmojisUpdate(bot)

    with patch(
        "src.bot.events.guild.on_guild_emojis_update.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.guild.on_guild_emojis_update.logger",
    ) as logger:

        await cog.on_guild_emojis_update(guild, before, after)

        translate.assert_called_once()

        assert translate.call_args.args[0] == guild

        logger.info.assert_called_once_with(
            "translated"
        )
