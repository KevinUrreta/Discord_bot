from discord.ext import commands

import wavelink

from src.locales.i18n import translate
from src.core.logging import logger


class Resume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="resume")
    async def resume(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "not_connected",
                )
            )

        player: wavelink.Player = ctx.voice_client

        if not player.paused:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "song_not_paused",
                )
            )

        await player.pause(False)

        await ctx.send(
            translate(
                ctx.guild,
                "song_resumed",
            )
        )