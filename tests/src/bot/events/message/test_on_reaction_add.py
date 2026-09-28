from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_reaction_add import ReactionAdd


@pytest.mark.asyncio
async def test_on_reaction_add_logs():
    bot = MagicMock()


    reaction = MagicMock()
    user = MagicMock()

    guild = MagicMock()
    reaction.message.guild = guild



    cog = ReactionAdd(bot)

    with patch(
        "src.bot.events.message.on_reaction_add.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.message.on_reaction_add.logger",
    ) as logger:

        await cog.on_reaction_add(reaction, user)

        translate.assert_called_once()

        assert translate.call_args.args[0] == reaction.message.guild

        logger.info.assert_called_once_with(
            "translated"
        )
