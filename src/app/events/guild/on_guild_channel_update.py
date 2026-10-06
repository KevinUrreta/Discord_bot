from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class GuildChannelUpdate(commands.Cog):
    """
    Gestiona los cambios de un canal de un server.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        """
        Registra los cambios de un canal de un server.
        :param before: Estado antes.
        :param after: Estado después.
        :return: None
        """
        logger.info(
            translate(
                None,
                "app.events.logs.guild.on_guild_channel_update.channel_updated",
                before=before, after=after,
            )
        )
