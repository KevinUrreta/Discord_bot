import asyncio

import wavelink
import yt_dlp
from discord.ext import commands

from src.helpers.embeds import create_embed


def get_original_info(url):
    ydl = yt_dlp.YoutubeDL(
        {
            "quiet": True,
            "no_warnings": True,
        }
    )

    info = ydl.extract_info(url, download=False)

    return {
        "title": info.get("title", "Título desconocido"),
        "views": info.get("view_count", 0),
    }


def format_duration(milliseconds):
    total_seconds = int(milliseconds / 1000)
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes}:{seconds:02d}"


def get_thumbnail(track):
    if track.artwork:
        return track.artwork

    if track.identifier:
        return (
            f"https://img.youtube.com/vi/"
            f"{track.identifier}/hqdefault.jpg"
        )

    return None


class Nowplaying(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="nowplaying",
        aliases=["np"],
    )
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

        info = await asyncio.to_thread(
            get_original_info,
            track.uri,
        )

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