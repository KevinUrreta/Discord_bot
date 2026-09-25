from discord.ext import commands

from src.locales.i18n import translate
from src.core.logging import logger

class Volume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "not_connected",
                )
            )

        await ctx.voice_client.set_volume(volume)

        await ctx.send(
            translate(
                ctx.guild,
                "volume_changed",
                volume=volume,
            )
        )