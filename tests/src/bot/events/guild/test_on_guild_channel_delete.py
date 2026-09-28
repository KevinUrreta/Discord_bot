from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_channel_delete import GuildChannelDelete


@pytest.mark.asyncio
async def test_on_guild_channel_delete_logs():
    bot = MagicMock()


    channel = MagicMock()

    guild = MagicMock()
    channel.guild = guild



    cog = GuildChannelDelete(bot)

    with patch(
        "src.bot.events.guild.on_guild_channel_delete.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.guild.on_guild_channel_delete.logger",
    ) as logger:

        await cog.on_guild_channel_delete(channel)

        translate.assert_called_once()

        assert translate.call_args.args[0] == channel.guild

        logger.info.assert_called_once_with(
            "translated"
        )
