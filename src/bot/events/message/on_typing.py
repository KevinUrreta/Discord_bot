from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class Typing(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        logger.info(
            translate(
                getattr(channel, "guild", None),
                "events.message.on_typing.typing_detected",
                user=user,
                channel=channel,
            )
        )