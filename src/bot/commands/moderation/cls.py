from discord.ext import commands

from src.locales.i18n import translate
from src.core.logging import logger

class Cls(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cls(self, ctx, *, limit = 1):

        await ctx.channel.purge(limit=limit + 1)
