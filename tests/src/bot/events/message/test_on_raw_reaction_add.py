from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_raw_reaction_add import RawReactionAdd


@pytest.mark.asyncio
async def test_on_raw_reaction_add_logs():
    bot = MagicMock()


    payload = MagicMock()

    guild = MagicMock()
    payload.guild_id = 123
    bot.get_guild.return_value = guild



    cog = RawReactionAdd(bot)

    with patch(
        "src.bot.events.message.on_raw_reaction_add.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.message.on_raw_reaction_add.logger",
    ) as logger:

        await cog.on_raw_reaction_add(payload)

        translate.assert_called_once()

        assert translate.call_args.args[0] == guild

        logger.info.assert_called_once_with(
            "translated"
        )
