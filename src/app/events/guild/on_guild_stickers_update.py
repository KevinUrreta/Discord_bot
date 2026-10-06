from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class GuildStickersUpdate(commands.Cog):
    """
    Gestiona la modificación de stickers de un server.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_stickers_update(self, guild, before, after):
        """
        Registra la modificación de stickers de un server.
        :param guild: Server.
        :param before: Estado antes.
        :param after: Estado después.
        :return: None
        """
        logger.info(
            translate(
                None,
                "app.events.logs.guild.on_guild_stickers_update.stickers_updated",
                guild_name=guild.name,
                guild_id=guild.id,
            )
        )
