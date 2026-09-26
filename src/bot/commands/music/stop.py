from discord.ext import commands

import wavelink

from src.locales.i18n import translate
from src.core.logging import logger


class Stop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="stop")
    async def stop(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.stop.not_connected",
                )
            )

        player: wavelink.Player = ctx.voice_client

        player.queue.clear()
        await player.stop()

        await ctx.send(
            translate(
                ctx.guild,
                "commands.music.stop.playback_stopped",
            )
        )