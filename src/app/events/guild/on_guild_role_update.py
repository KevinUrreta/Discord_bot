from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class GuildRoleUpdate(commands.Cog):
    """
    Gestiona la modificación de un rol del server.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        """
        Registra la modificación de un rol del server.
        :param before: Estado antes.
        :param after: Estado después.
        :return: None
        """
        logger.info(
            translate(
                None,
                "app.events.logs.guild.on_guild_role_update.role_updated",
                before=before, after=after,
            )
        )
