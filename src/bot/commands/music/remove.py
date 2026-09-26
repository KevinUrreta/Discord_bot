from discord.ext import commands

import wavelink

from src.locales.i18n import translate
from src.core.logging import logger


class Remove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="remove")
    async def remove(self, ctx, position: int):
        if ctx.voice_client is None:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "not_connected",
                )
            )

        player: wavelink.Player = ctx.voice_client

        if player.queue.is_empty:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "queue_empty",
                )
            )

        tracks = list(player.queue)

        if position < 1 or position > len(tracks):
            return await ctx.send(
                translate(
                    ctx.guild,
                    "invalid_queue_position",
                )
            )

        track = tracks[position - 1]

        player.queue.remove(track)

        await ctx.send(
            translate(
                ctx.guild,
                "removed_from_queue",
                title=track.title,
            )
        )