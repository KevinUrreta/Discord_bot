from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_raw_reaction_add import on_raw_reaction_add


@pytest.mark.asyncio
async def test_on_raw_reaction_add_logs():
    payload = MagicMock()

    with patch("src.bot.events.message.on_raw_reaction_add.logger") as logger:
        await on_raw_reaction_add(payload)

    logger.info.assert_called_once()
