from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class RawReactionAdd(commands.Cog):
    """
    Gestiona la recepción de reacciones mediante el evento raw.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """
        Registra la adición de una reacción a un mensaje.

        :param payload: Datos de la reacción recibidos.
        :return: None
        """
        logger.info(
            translate(
                self.bot.get_guild(payload.guild_id),
                "app.events.logs.message.on_raw_reaction_add.reaction_added",
                message_id=payload.message_id, emoji=payload.emoji, user=payload.user_id,
            )
        )
