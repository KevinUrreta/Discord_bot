from discord.ext import commands

import wavelink

from src.locales.i18n import translate
from src.core.logging import logger


class Queue(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="queue", aliases=["q"])
    async def queue(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.queue.not_connected",
                )
            )

        player: wavelink.Player = ctx.voice_client

        if player.queue.is_empty:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.queue.queue_empty",
                )
            )

        tracks = list(player.queue)

        message = "\n".join(
            f"{index}. {track.title}"
            for index, track in enumerate(tracks, start=1)
        )

        await ctx.send(
            translate(
                ctx.guild,
                "commands.music.queue.queue_list",
                queue=message,
            )
        )