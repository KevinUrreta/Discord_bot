from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class MessageDelete(commands.Cog):
    """
    Gestiona la eliminación de mensajes de los servers.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        """
        Registra la eliminación de los mensajes.

        :param message:
        :return:
        """
        logger.info(
            translate(
                None,
                "bot.events.logs.message.on_message_delete.message_deleted",
                channel=message.channel,
                author=message.author,
                message=message.content,
            )
        )
