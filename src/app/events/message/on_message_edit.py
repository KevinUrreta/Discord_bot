from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class MessageEdit(commands.Cog):
    """
    Gestiona los mensajes editados.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        """
        Registra los mensajes editados.

        :param before: Estado antes.
        :param after: Estado después.
        :return: None
        """
        # if after.author == self.app.user:
        #     return

        if before.content == after.content:
            return

        logger.info(
            translate(
                None,
                "app.events.logs.message.on_message_edit.message_edited",
                server_name=after.guild.name,
                channel_name=after.channel.name,
                author_name=after.author.name,
                before=before.content,
                after=after.content,
            )
        )