from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_reaction_remove import on_reaction_remove


@pytest.mark.asyncio
async def test_on_reaction_remove_logs():
    reaction = MagicMock()
    user = MagicMock()

    with patch("src.bot.events.message.on_reaction_remove.logger") as logger:
        await on_reaction_remove(reaction, user)

    logger.info.assert_called_once()
