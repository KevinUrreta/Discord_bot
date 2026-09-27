from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.other.on_connect import on_connect


@pytest.mark.asyncio
async def test_on_connect_logs():
    pass

    with patch("src.bot.events.other.on_connect.logger") as logger:
        await on_connect()

    logger.info.assert_called_once()
