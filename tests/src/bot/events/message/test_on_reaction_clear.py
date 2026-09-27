from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_reaction_clear import on_reaction_clear


@pytest.mark.asyncio
async def test_on_reaction_clear_logs():
    message = MagicMock()
    reactions = MagicMock()

    with patch("src.bot.events.message.on_reaction_clear.logger") as logger:
        await on_reaction_clear(message, reactions)

    logger.info.assert_called_once()
