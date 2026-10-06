from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class On_ready(commands.Cog):
    """
    Gestiona cuando el app está preparado.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Registra cuando la app esté preparada.

        :return: None
        """
        logger.info(
            translate(
                None,
                "app.events.logs.other.on_ready.bot_connected",
                bot=self.bot.user,
            )
        )
