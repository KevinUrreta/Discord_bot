from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.other.on_voice_state_update import on_voice_state_update


@pytest.mark.asyncio
async def test_on_voice_state_update_ignores_bots():
    member = MagicMock()
    member.bot = True

    before = MagicMock()
    after = MagicMock()

    with patch(
        "src.bot.events.other.on_voice_state_update.logger"
    ) as logger:

        await on_voice_state_update(member, before, after)

        logger.info.assert_called_once()
        logger.debug.assert_not_called()


@pytest.mark.asyncio
async def test_on_voice_state_update_logs_human_member():
    member = MagicMock()
    member.bot = False

    before = MagicMock()
    after = MagicMock()

    before.channel = MagicMock()
    before.channel.name = "General"

    after.channel = MagicMock()
    after.channel.name = "Music"

    with patch(
        "src.bot.events.other.on_voice_state_update.logger"
    ) as logger:

        await on_voice_state_update(member, before, after)

        logger.info.assert_called_once()
        logger.debug.assert_called_once()
