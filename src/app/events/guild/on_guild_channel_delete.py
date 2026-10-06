from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class GuildChannelDelete(commands.Cog):
    """
    Gestiona la eliminación de un canal de un server.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        """
        Registra el borrado de un canal de un server.
        :param channel: Canal del server.
        :return: None
        """
        logger.info(
            translate(
                None,
                "app.events.logs.guild.on_guild_channel_delete.channel_deleted",
                channel=channel,
            )
        )
