from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class MessageEdit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        logger.info(
            translate(
                after.guild,
                "events.message.on_message_edit.message_edited",
                channel=after.channel, author=after.author, before=before.content, after=after.content,
            )
        )
