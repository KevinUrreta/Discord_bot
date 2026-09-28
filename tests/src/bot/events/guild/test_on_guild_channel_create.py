from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_channel_create import GuildChannelCreate


@pytest.mark.asyncio
async def test_on_guild_channel_create_logs():
    bot = MagicMock()


    channel = MagicMock()

    guild = MagicMock()
    channel.guild = guild



    cog = GuildChannelCreate(bot)

    with patch(
        "src.bot.events.guild.on_guild_channel_create.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.guild.on_guild_channel_create.logger",
    ) as logger:

        await cog.on_guild_channel_create(channel)

        translate.assert_called_once()

        assert translate.call_args.args[0] == channel.guild

        logger.info.assert_called_once_with(
            "translated"
        )
