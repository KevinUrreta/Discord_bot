from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.other.on_disconnect import Disconnect


@pytest.mark.asyncio
async def test_on_disconnect_logs():
    bot = MagicMock()


    pass


    cog = Disconnect(bot)

    with patch(
        "src.bot.events.other.on_disconnect.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.other.on_disconnect.logger",
    ) as logger:

        await cog.on_disconnect()

        translate.assert_called_once()

        assert translate.call_args.args[0] == None

        logger.info.assert_called_once_with(
            "translated"
        )
