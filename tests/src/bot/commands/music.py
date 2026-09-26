import logging

import discord
import wavelink
from discord.ext import commands

from src.locales.i18n import translate


logger = logging.getLogger("music_bot")


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        logger.info(
            translate(
                ctx.guild,
                "joining_voice",
                channel=channel.name,
            )
        )

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect(cls=wavelink.Player)

        logger.info(
            translate(
                ctx.guild,
                "joined_voice",
                channel=channel.name,
            )
        )

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

            tracks = await wavelink.Playable.search(query)

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

    @commands.command()
    async def stop(self, ctx):
        logger.info(
            translate(
                ctx.guild,
                "disconnecting",
            )
        )

        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()
