from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.other.on_command import On_command


@pytest.mark.asyncio
async def test_on_command_logs():
    bot = MagicMock()
    ctx = MagicMock()

    ctx.guild = MagicMock()
    ctx.command.name = "test"
    ctx.author = MagicMock()
    ctx.channel = MagicMock()

    cog = On_command(bot)

    with patch(
        "src.bot.events.other.on_command.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.other.on_command.logger"
    ) as logger:

        await cog.on_command(ctx)

        translate.assert_called_once()
        assert translate.call_args.args[0] is ctx.guild

        logger.info.assert_called_once_with(
            "translated"
        )
