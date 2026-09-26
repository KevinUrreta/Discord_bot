from discord.ext import commands

import wavelink

from src.locales.i18n import translate
from src.core.logging import logger


class Skip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.skip.not_connected",
                )
            )

        player: wavelink.Player = ctx.voice_client

        if not player.playing:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.skip.no_song_playing",
                )
            )

        await player.skip(force=True)

        await ctx.send(
            translate(
                ctx.guild,
                "commands.music.skip.song_skipped",
            )
        )