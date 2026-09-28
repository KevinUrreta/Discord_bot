from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class GuildChannelDelete(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        logger.info(
            translate(
                channel.guild,
                "events.guild.on_guild_channel_delete.channel_deleted",
                channel=channel,
            )
        )
