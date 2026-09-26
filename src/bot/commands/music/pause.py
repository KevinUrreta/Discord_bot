from discord.ext import commands

import wavelink

from src.locales.i18n import translate
from src.core.logging import logger


class Pause(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pause")
    async def pause(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.pause.not_connected",
                )
            )

        player: wavelink.Player = ctx.voice_client

        if not player.playing:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.pause.no_song_playing",
                )
            )

        await player.pause(True)

        await ctx.send(
            translate(
                ctx.guild,
                "commands.music.pause.song_paused",
            )
        )