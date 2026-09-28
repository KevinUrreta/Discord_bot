from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.other.on_voice_state_update import VoiceStateUpdate


@pytest.mark.asyncio
async def test_on_voice_state_update_logs():
    bot = MagicMock()


    member = MagicMock()
    before = MagicMock()
    after = MagicMock()

    guild = MagicMock()
    member.guild = guild



    cog = VoiceStateUpdate(bot)

    with patch(
        "src.bot.events.other.on_voice_state_update.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.other.on_voice_state_update.logger",
    ) as logger:

        await cog.on_voice_state_update(member, before, after)

        translate.assert_called_once()

        assert translate.call_args.args[0] == member.guild

        logger.info.assert_called_once_with(
            "translated"
        )
