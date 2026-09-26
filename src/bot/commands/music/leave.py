from discord.ext import commands

from src.locales.i18n import translate
from src.core.logging import logger


class Leave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="leave", aliases=["disconnect"])
    async def leave(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "not_connected",
                )
            )

        await ctx.voice_client.disconnect()

        await ctx.send(
            translate(
                ctx.guild,
                "bot_disconnected",
            )
        )