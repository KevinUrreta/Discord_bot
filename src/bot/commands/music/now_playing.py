import asyncio

import wavelink
from discord.ext import commands

from src.helpers.embeds import create_embed
from src.helpers.music_utils import (
    get_original_info,
    format_duration,
    get_thumbnail
)


class Nowplaying(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="nowplaying")
    async def nowplaying(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.now_playing_not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player: wavelink.Player = ctx.voice_client
        track = player.current

        if track is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.now_playing_empty",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        info = await asyncio.to_thread(get_original_info, track.uri)

        return await ctx.send(
            embed=create_embed(
                ctx.guild,
                "music.now_playing",
                title=info["title"],
                duration=format_duration(track.length),
                views=info["views"],
                queue=player.queue.count,
                user=ctx.author.display_name,
                thumbnail=get_thumbnail(track),
                footer_icon=ctx.author.display_avatar.url,
            )
        )