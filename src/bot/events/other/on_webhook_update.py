from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class WebhookUpdate(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_webhooks_update(self, channel):
        logger.info(
            translate(
                None,
                "bot.events.logs.other.on_webhook_update.webhook_updated",
                channel=channel,
            )
        )
