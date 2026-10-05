from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class Resumed(commands.Cog):
    """
    Gestiona la reconexión.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_resumed(self):
        """
        Registra la reconexión.

        :return: None
        """
        logger.info(
            translate(
                None,
                "other.on_resumed.discord_resumed"
            )
        )
