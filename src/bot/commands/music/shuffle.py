from discord.ext import commands

import wavelink

from src.helpers.embeds import create_embed


class Shuffle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="shuffle")
    async def shuffle(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.shuffle.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player: wavelink.Player = ctx.voice_client

        if player.queue.is_empty:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.shuffle.not_enough_songs",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player.queue.shuffle()

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "music.shuffle.shuffled",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            )
        )