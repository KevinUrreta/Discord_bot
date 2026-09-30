from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class MessageEdit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        # if after.author == self.bot.user:
        #     return

        if before.content == after.content:
            return

        logger.info(
            translate(
                None,
                "bot.events.logs.message.on_message_edit.message_edited",
                server_name=after.guild.name,
                channel_name=after.channel.name,
                author_name=after.author.name,
                before=before.content,
                after=after.content,
            )
        )