from discord.ext import commands

from src.locales.i18n import translate

class Lyrics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lyrics(self, ctx):
        ...