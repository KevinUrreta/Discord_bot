from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_message import On_message


@pytest.mark.asyncio
async def test_on_message_ignores_bot_messages():
    bot = MagicMock()
    bot.user = MagicMock()

    message = MagicMock()
    message.author = bot.user

    cog = On_message(bot)

    with patch(
        "src.bot.events.message.on_message.logger"
    ) as logger:

        await cog.on_message(message)

        logger.info.assert_not_called()


@pytest.mark.asyncio
async def test_on_message_logs_user_message():
    bot = MagicMock()
    bot.user = MagicMock()

    message = MagicMock()
    message.author = MagicMock()
    message.guild = MagicMock()
    message.content = "hello"

    cog = On_message(bot)

    with patch(
        "src.bot.events.message.on_message.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.message.on_message.logger"
    ) as logger:

        await cog.on_message(message)

        translate.assert_called_once()
        assert translate.call_args.args[0] is message.guild

        logger.info.assert_called_once_with(
            "translated"
        )
