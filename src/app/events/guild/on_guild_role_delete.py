from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class GuildRoleDelete(commands.Cog):
    """
    Gestiona la eliminación de un rol del server.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        """
        Elimina un rol del server.
        :param role: Rol
        :return: None
        """
        logger.info(
            translate(
                None,
                "app.events.logs.guild.on_guild_role_delete.role_deleted",
                role=role,
            )
        )
