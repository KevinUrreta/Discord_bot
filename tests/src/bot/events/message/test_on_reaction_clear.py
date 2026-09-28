from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_reaction_clear import ReactionClear


@pytest.mark.asyncio
async def test_on_reaction_clear_logs():
    bot = MagicMock()


    message = MagicMock()
    reactions = MagicMock()

    guild = MagicMock()
    message.guild = guild



    cog = ReactionClear(bot)

    with patch(
        "src.bot.events.message.on_reaction_clear.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.message.on_reaction_clear.logger",
    ) as logger:

        await cog.on_reaction_clear(message, reactions)

        translate.assert_called_once()

        assert translate.call_args.args[0] == message.guild

        logger.info.assert_called_once_with(
            "translated"
        )
