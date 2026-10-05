from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class ReactionClear(commands.Cog):
    """
    Gestiona la limpieza de reacciones.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_clear(self, message, reactions):
        """
        Registra la limpieza de reacciones.

        :param message: Mensaje.
        :param reactions: Reacciones.
        :return: None
        """
        logger.info(
            translate(
                None,
                "bot.events.logs.message.on_reaction_clear.reactions_cleared",
                message=message,
            )
        )
