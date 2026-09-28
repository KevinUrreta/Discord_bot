from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.other.on_application_command_error import ApplicationCommandError


@pytest.mark.asyncio
async def test_on_app_command_error_logs():
    bot = MagicMock()


    interaction = MagicMock()
    error = MagicMock()

    guild = MagicMock()
    interaction.guild = guild



    cog = ApplicationCommandError(bot)

    with patch(
        "src.bot.events.other.on_application_command_error.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.other.on_application_command_error.logger",
    ) as logger:

        await cog.on_app_command_error(interaction, error)

        translate.assert_called_once()

        assert translate.call_args.args[0] == interaction.guild

        logger.info.assert_called_once_with(
            "translated"
        )
