from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class Connect(commands.Cog):
    """
    Gestiona cuando se conecta el app.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        """
        Registra cuando se conecta el app.

        :return: None
        """
        logger.info(
            translate(
                None,
                "app.events.logs.other.on_connect.discord_connected"
            )
        )
