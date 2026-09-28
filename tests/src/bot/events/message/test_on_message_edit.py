from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_message_edit import MessageEdit


@pytest.mark.asyncio
async def test_on_message_edit_logs():
    bot = MagicMock()


    before = MagicMock()
    after = MagicMock()

    guild = MagicMock()
    after.guild = guild



    cog = MessageEdit(bot)

    with patch(
        "src.bot.events.message.on_message_edit.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.message.on_message_edit.logger",
    ) as logger:

        await cog.on_message_edit(before, after)

        translate.assert_called_once()

        assert translate.call_args.args[0] == after.guild

        logger.info.assert_called_once_with(
            "translated"
        )
