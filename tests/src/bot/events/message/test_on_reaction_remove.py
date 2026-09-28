from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.message.on_reaction_remove import ReactionRemove


@pytest.mark.asyncio
async def test_on_reaction_remove_logs():
    bot = MagicMock()


    reaction = MagicMock()
    user = MagicMock()

    guild = MagicMock()
    reaction.message.guild = guild



    cog = ReactionRemove(bot)

    with patch(
        "src.bot.events.message.on_reaction_remove.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.message.on_reaction_remove.logger",
    ) as logger:

        await cog.on_reaction_remove(reaction, user)

        translate.assert_called_once()

        assert translate.call_args.args[0] == reaction.message.guild

        logger.info.assert_called_once_with(
            "translated"
        )
