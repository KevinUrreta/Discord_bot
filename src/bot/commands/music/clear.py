from discord.ext import commands

import wavelink

from src.helpers.embeds import create_embed


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear")
    async def clear(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.clear.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player: wavelink.Player = ctx.voice_client

        if player.queue.is_empty:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.clear.queue_empty",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player.queue.clear()

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "music.clear.cleared",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            )
        )