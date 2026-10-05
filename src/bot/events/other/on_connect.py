from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class Connect(commands.Cog):
    """
    Gestiona cuando se conecta el bot.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        """
        Registra cuando se conecta el bot.

        :return: None
        """
        logger.info(
            translate(
                None,
                "bot.events.logs.other.on_connect.discord_connected"
            )
        )
