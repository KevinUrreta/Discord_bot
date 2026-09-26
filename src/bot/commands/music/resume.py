from discord.ext import commands

from src.locales.i18n import translate
from src.core.logging import logger

class Resume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def resume(self, ctx):
        ...