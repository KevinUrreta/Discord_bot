from discord.ext import commands

import wavelink

from src.helpers.embeds import create_embed


class Stop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="stop")
    async def stop(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.stop.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player: wavelink.Player = ctx.voice_client

        player.queue.clear()
        await player.stop()

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "music.stop.stopped",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            )
        )