from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_message_delete import MessageDelete


@pytest.mark.asyncio
async def test_on_message_delete_logs():
    bot = MagicMock()


    message = MagicMock()

    guild = MagicMock()
    message.guild = guild



    cog = MessageDelete(bot)

    with patch(
        "src.bot.events.message.on_message_delete.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.message.on_message_delete.logger",
    ) as logger:

        await cog.on_message_delete(message)

        translate.assert_called_once()

        assert translate.call_args.args[0] == message.guild

        logger.info.assert_called_once_with(
            "translated"
        )
