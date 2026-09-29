from discord.ext import commands

import wavelink

from src.helpers.embeds import create_embed


class Loop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="loop")
    async def loop(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.loop.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player: wavelink.Player = ctx.voice_client

        if not player.current:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.loop.no_song_playing",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player.queue.mode = (
            wavelink.QueueMode.loop
            if player.queue.mode != wavelink.QueueMode.loop
            else wavelink.QueueMode.normal
        )

        if player.queue.mode == wavelink.QueueMode.loop:
            await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.loop.enabled",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )
        else:
            await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.loop.disabled",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )