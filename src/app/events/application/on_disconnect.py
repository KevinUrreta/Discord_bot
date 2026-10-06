from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class Disconnect(commands.Cog):
    """
    Gestiona cuando se desconecta el app.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_disconnect(self):
        """
        Registra cuando se desconecta el app.

        :return: None
        """
        logger.info(
            translate(
                None,
                "app.events.logs.other.on_disconnect.discord_disconnected"
            )
        )
