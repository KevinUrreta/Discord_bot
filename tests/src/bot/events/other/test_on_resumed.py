from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.other.on_resumed import Resumed


@pytest.mark.asyncio
async def test_on_resumed_logs():
    bot = MagicMock()


    pass


    cog = Resumed(bot)

    with patch(
        "src.bot.events.other.on_resumed.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.other.on_resumed.logger",
    ) as logger:

        await cog.on_resumed()

        translate.assert_called_once()

        assert translate.call_args.args[0] == None

        logger.info.assert_called_once_with(
            "translated"
        )
