from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_stickers_update import GuildStickersUpdate


@pytest.mark.asyncio
async def test_on_guild_stickers_update_logs():
    bot = MagicMock()


    guild = MagicMock()
    before = MagicMock()
    after = MagicMock()



    cog = GuildStickersUpdate(bot)

    with patch(
        "src.bot.events.guild.on_guild_stickers_update.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.guild.on_guild_stickers_update.logger",
    ) as logger:

        await cog.on_guild_stickers_update(guild, before, after)

        translate.assert_called_once()

        assert translate.call_args.args[0] == guild

        logger.info.assert_called_once_with(
            "translated"
        )
