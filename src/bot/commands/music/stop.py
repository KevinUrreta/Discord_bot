from discord.ext import commands

from src.locales.i18n import translate
from src.core.logging import logger

class Stop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stop(self, ctx):
        logger.info(
            translate(
                ctx.guild,
                "disconnecting",
            )
        )

        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()
