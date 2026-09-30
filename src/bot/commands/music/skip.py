from discord.ext import commands

import wavelink

from src.helpers.embeds import create_embed


class Skip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.skip.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player: wavelink.Player = ctx.voice_client

        if player.current is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.skip.no_song_playing",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        await player.skip(force=True)

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "bot.commands.music.embeds.skip.skipped",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            )
        )