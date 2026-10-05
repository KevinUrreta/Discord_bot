from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class ReactionRemove(commands.Cog):
    """
    Gestiona la eliminación de reacciones.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        """
        Registra la eliminación de reacciones.

        :param reaction: Reacciones.
        :param user: Usuario.
        :return: None
        """
        logger.info(
            translate(
                None,
                "bot.events.logs.message.on_reaction_remove.reaction_removed",
                channel=reaction.message.channel, emoji=reaction.emoji, user=user,
            )
        )
