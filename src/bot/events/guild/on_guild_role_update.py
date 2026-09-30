from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class GuildRoleUpdate(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        logger.info(
            translate(
                None,
                "bot.events.logs.guild.on_guild_role_update.role_updated",
                before=before, after=after,
            )
        )
