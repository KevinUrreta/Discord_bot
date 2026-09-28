from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_typing import Typing


@pytest.mark.asyncio
async def test_on_typing_logs():
    bot = MagicMock()


    channel = MagicMock()
    user = MagicMock()
    when = MagicMock()

    guild = MagicMock()
    channel.guild = guild



    cog = Typing(bot)

    with patch(
        "src.bot.events.message.on_typing.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.message.on_typing.logger",
    ) as logger:

        await cog.on_typing(channel, user, when)

        translate.assert_called_once()

        assert translate.call_args.args[0] == channel.guild

        logger.info.assert_called_once_with(
            "translated"
        )
