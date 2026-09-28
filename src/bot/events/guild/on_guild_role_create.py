from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class GuildRoleCreate(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        logger.info(
            translate(
                role.guild,
                "events.guild.on_guild_role_create.role_created",
                role=role,
            )
        )
