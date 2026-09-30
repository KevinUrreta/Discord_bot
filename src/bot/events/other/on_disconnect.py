from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class Disconnect(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_disconnect(self):
        logger.info(
            translate(
                None,
                "bot.events.logs.other.on_disconnect.discord_disconnected"
            )
        )
