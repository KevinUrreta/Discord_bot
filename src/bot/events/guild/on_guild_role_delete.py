from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class GuildRoleDelete(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        logger.info(
            translate(
                None,
                "bot.events.logs.guild.on_guild_role_delete.role_deleted",
                role=role,
            )
        )
