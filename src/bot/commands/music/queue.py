import asyncio

import wavelink
from discord.ext import commands

from src.helpers.embeds import create_embed
from src.helpers.music_utils import get_original_info


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

        infos = await asyncio.gather(
            *(
                asyncio.to_thread(get_original_info, track.uri)
                for track in tracks
            )
        )

        titles = [info["title"] for info in infos]
        message = "\n".join(
            f"{index}. {title}"
            for index, title in enumerate(titles, start=1)
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