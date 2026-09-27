from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_message_delete import on_message_delete


@pytest.mark.asyncio
async def test_on_message_delete_logs():
    message = MagicMock()

    with patch("src.bot.events.message.on_message_delete.logger") as logger:
        await on_message_delete(message)

    logger.info.assert_called_once()
