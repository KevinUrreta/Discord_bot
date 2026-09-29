import asyncio

import wavelink
import yt_dlp
from discord.ext import commands

from src.helpers.embeds import create_embed


def get_original_title(url):
    ydl = yt_dlp.YoutubeDL(
        {
            "quiet": True,
            "no_warnings": True,
        }
    )

    info = ydl.extract_info(url, download=False)

    return info.get(
        "title",
        "Título desconocido",
    )


class Queue(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="queue", aliases=["q"])
    async def queue(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.queue.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player: wavelink.Player = ctx.voice_client

        if player.queue.is_empty:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.queue.empty",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        tracks = list(player.queue)

        titles = await asyncio.gather(
            *(
                asyncio.to_thread(
                    get_original_title,
                    track.uri,
                )
                for track in tracks
            )
        )

        message = "\n".join(
            f"{index}. {title}"
            for index, title in enumerate(
                titles,
                start=1,
            )
        )

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "music.queue.list",
                queue=message,
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            )
        )