import discord
from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class On_message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return

        if message.guild is None:
            return

        logger.info(
            translate(
                message.guild,
                "events.message.on_message.message_detected",
                server_name=message.guild.name,
                channel_name=getattr(
                    message.channel,
                    "name",
                    "DM",
                ),
                author_name=message.author.name,
                message=message.content,
            )
        )