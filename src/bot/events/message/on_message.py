import discord
from discord.ext import commands

from src.locales.i18n import translate
from src.core.logging import logger


class On_message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return

        logger.info(
            translate(
                message.guild,
                "events.message.on_message.message_detected",
                author=message.author.name,
                message=message.content,
            )
        )