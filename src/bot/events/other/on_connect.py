from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class Connect(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        logger.info(
            translate(
                None,
                "events.other.on_connect.discord_connected"
            )
        )
