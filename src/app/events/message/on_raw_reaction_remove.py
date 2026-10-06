from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class RawReactionRemove(commands.Cog):
    """
    Gestiona la eliminación de reacciones mediante el evento raw.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        """
        Registra la eliminación de reacciones a un mensaje.

        :param payload: Datos de la reacción recibidos
        :return:
        """
        logger.info(
            translate(
                self.bot.get_guild(payload.guild_id),
                "app.events.logs.message.on_raw_reaction_remove.reaction_removed",
                message_id=payload.message_id, emoji=payload.emoji, user=payload.user_id,
            )
        )
