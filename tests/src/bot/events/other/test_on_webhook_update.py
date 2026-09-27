from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.other.on_webhook_update import on_webhook_update


@pytest.mark.asyncio
async def test_on_webhook_update_logs():
    channel = MagicMock()

    with patch("src.bot.events.other.on_webhook_update.logger") as logger:
        await on_webhook_update(channel)

    logger.info.assert_called_once()
