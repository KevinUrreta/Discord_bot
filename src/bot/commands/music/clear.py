from discord.ext import commands

import wavelink

from src.locales.i18n import translate


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear")
    async def clear(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.clear.not_connected",
                )
            )

        player: wavelink.Player = ctx.voice_client

        if player.queue.is_empty:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.clear.queue_empty",
                )
            )

        player.queue.clear()

        await ctx.send(
            translate(
                ctx.guild,
                "commands.music.clear.queue_cleared",
            )
        )