from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class GuildRoleCreate(commands.Cog):
    """
    Gestiona la creación de un Rol del server.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        """
        Registra la creación de un rol del server.
        :param role: rol
        :return: None
        """
        logger.info(
            translate(
                None,
                "bot.events.logs.guild.on_guild_role_create.role_created",
                role=role,
            )
        )
