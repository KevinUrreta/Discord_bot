from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_reaction_add import on_reaction_add


@pytest.mark.asyncio
async def test_on_reaction_add_logs():
    reaction = MagicMock()
    user = MagicMock()

    with patch("src.bot.events.message.on_reaction_add.logger") as logger:
        await on_reaction_add(reaction, user)

    logger.info.assert_called_once()
