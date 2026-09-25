from discord.ext import commands

import wavelink

from src.locales.i18n import translate
from src.core.logging import logger


class Play(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="play", aliases=["p"])
    async def play(self, ctx, *, query):
        async with ctx.typing():
            if ctx.voice_client is None:
                if not ctx.author.voice:
                    return await ctx.send(
                        translate(
                            ctx.guild,
                            "voice_not_connected",
                        )
                    )

                player = await ctx.author.voice.channel.connect(
                    cls=wavelink.Player
                )
            else:
                player: wavelink.Player = ctx.voice_client

            if player.playing:
                await player.stop()

            tracks = await wavelink.Playable.search(
                query,
                source=wavelink.TrackSource.YouTube,
            )

            if not tracks:
                return await ctx.send(
                    translate(
                        ctx.guild,
                        "no_song_found",
                    )
                )

            track = tracks[0]

            await player.play(track)

        await ctx.send(
            translate(
                ctx.guild,
                "now_playing",
                title=track.title,
            )
        )
