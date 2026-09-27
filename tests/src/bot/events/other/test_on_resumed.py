from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.other.on_resumed import on_resumed


@pytest.mark.asyncio
async def test_on_resumed_logs():
    pass

    with patch("src.bot.events.other.on_resumed.logger") as logger:
        await on_resumed()

    logger.info.assert_called_once()
