from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class MessageDelete(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        logger.info(
            translate(
                None,
                "bot.events.logs.message.on_message_delete.message_deleted",
                channel=message.channel,
                author=message.author,
                message=message.content,
            )
        )
