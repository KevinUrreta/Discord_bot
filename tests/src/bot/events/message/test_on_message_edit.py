from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_message_edit import on_message_edit


@pytest.mark.asyncio
async def test_on_message_edit_logs():
    before = MagicMock()
    after = MagicMock()

    with patch("src.bot.events.message.on_message_edit.logger") as logger:
        await on_message_edit(before, after)

    logger.info.assert_called_once()
