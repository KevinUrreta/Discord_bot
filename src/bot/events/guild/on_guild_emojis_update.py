from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class GuildEmojisUpdate(commands.Cog):
    """
    Gestiona los cambios en emojis de un server.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        """
        Registra cuando hay cambios en los emojis de un server.
        :param guild: Server
        :param before: Estado antes.
        :param after: Estado después.
        :return: None
        """
        logger.info(
            translate(
                None,
                "bot.events.logs.guild.on_guild_emojis_update.emojis_updated",
                guild_name=guild.name,
                guild_id=guild.id,
            )
        )
