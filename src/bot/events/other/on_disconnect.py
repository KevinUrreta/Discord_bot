from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class Disconnect(commands.Cog):
    """
    Gestiona cuando se desconecta el bot.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_disconnect(self):
        """
        Registra cuando se desconecta el bot.

        :return: None
        """
        logger.info(
            translate(
                None,
                "bot.events.logs.other.on_disconnect.discord_disconnected"
            )
        )
