from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class ReactionAdd(commands.Cog):
    """
    Gestiona la adición de reacciones a mensajes.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        """
        Registra la eliminación de reacciones a un mensaje.

        :param reaction: Emoji de reacción.
        :param user: Usuario que ha reaccionado.
        :return: None
        """
        logger.info(
            translate(
                None,
                "app.events.logs.message.on_reaction_add.reaction_added",
                channel=reaction.message.channel, emoji=reaction.emoji, user=user,
            )
        )
