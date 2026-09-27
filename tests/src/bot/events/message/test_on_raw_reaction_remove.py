from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_raw_reaction_remove import on_raw_reaction_remove


@pytest.mark.asyncio
async def test_on_raw_reaction_remove_logs():
    payload = MagicMock()

    with patch("src.bot.events.message.on_raw_reaction_remove.logger") as logger:
        await on_raw_reaction_remove(payload)

    logger.info.assert_called_once()
