from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.other.on_connect import Connect


@pytest.mark.asyncio
async def test_on_connect_logs():
    bot = MagicMock()


    pass


    cog = Connect(bot)

    with patch(
        "src.bot.events.other.on_connect.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.other.on_connect.logger",
    ) as logger:

        await cog.on_connect()

        translate.assert_called_once()

        assert translate.call_args.args[0] == None

        logger.info.assert_called_once_with(
            "translated"
        )
