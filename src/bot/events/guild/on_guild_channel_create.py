from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class GuildChannelCreate(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        logger.info(
            translate(
                None,
                "bot.events.logs.guild.on_guild_channel_create.channel_created",
                channel=channel,
            )
        )
