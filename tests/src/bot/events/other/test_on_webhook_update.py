from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.other.on_webhook_update import WebhookUpdate


@pytest.mark.asyncio
async def test_on_webhooks_update_logs():
    bot = MagicMock()


    channel = MagicMock()

    guild = MagicMock()
    channel.guild = guild



    cog = WebhookUpdate(bot)

    with patch(
        "src.bot.events.other.on_webhook_update.translate",
        return_value="translated",
    ) as translate, patch(
        "src.bot.events.other.on_webhook_update.logger",
    ) as logger:

        await cog.on_webhooks_update(channel)

        translate.assert_called_once()

        assert translate.call_args.args[0] == channel.guild

        logger.info.assert_called_once_with(
            "translated"
        )
