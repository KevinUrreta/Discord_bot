from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class GuildChannelUpdate(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        logger.info(
            translate(
                after.guild,
                "events.guild.on_guild_channel_update.channel_updated",
                before=before, after=after,
            )
        )
