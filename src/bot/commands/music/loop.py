from discord.ext import commands

import wavelink

from src.locales.i18n import translate
from src.core.logging import logger


class Loop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="loop")
    async def loop(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.loop.not_connected",
                )
            )

        player: wavelink.Player = ctx.voice_client

        if not player.current:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.loop.no_song_playing",
                )
            )

        player.queue.mode = (
            wavelink.QueueMode.loop
            if player.queue.mode != wavelink.QueueMode.loop
            else wavelink.QueueMode.normal
        )

        if player.queue.mode == wavelink.QueueMode.loop:
            await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.loop.loop_enabled",
                )
            )
        else:
            await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.loop.loop_disabled",
                )
            )