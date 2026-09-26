from discord.ext import commands

import wavelink

from src.locales.i18n import translate


class Shuffle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="shuffle")
    async def shuffle(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.shuffle.not_connected",
                )
            )

        player: wavelink.Player = ctx.voice_client

        if player.queue.is_empty:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.shuffle.queue_empty",
                )
            )

        player.queue.shuffle()

        await ctx.send(
            translate(
                ctx.guild,
                "commands.music.shuffle.queue_shuffled",
            )
        )