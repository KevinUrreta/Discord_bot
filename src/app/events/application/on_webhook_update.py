from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class WebhookUpdate(commands.Cog):
    """
    Gestiona las actualizaciones de webhooks.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_webhooks_update(self, channel):
        """
        Registra la actualización de los webhooks.

        :param channel: Canal
        :return: None
        """
        logger.info(
            translate(
                None,
                "app.events.logs.other.on_webhook_update.webhook_updated",
                channel=channel,
            )
        )
