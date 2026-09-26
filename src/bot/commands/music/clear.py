from datetime import datetime
import discord; from discord.ext import commands

from src.locales.i18n import translate
from src.core.logging import logger

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx):
        ...
        