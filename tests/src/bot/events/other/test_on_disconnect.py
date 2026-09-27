from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.other.on_disconnect import on_disconnect


@pytest.mark.asyncio
async def test_on_disconnect_logs():
    pass

    with patch("src.bot.events.other.on_disconnect.logger") as logger:
        await on_disconnect()

    logger.info.assert_called_once()
