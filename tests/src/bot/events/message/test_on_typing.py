from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_typing import on_typing


@pytest.mark.asyncio
async def test_on_typing_logs():
    channel = MagicMock()
    user = MagicMock()
    when = MagicMock()

    with patch("src.bot.events.message.on_typing.logger") as logger:
        await on_typing(channel, user, when)

    logger.info.assert_called_once()
