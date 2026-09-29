from discord.ext import commands
import wavelink

from src.helpers.embeds import create_embed


class Pause(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pause")
    async def pause(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.pause.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player: wavelink.Player = ctx.voice_client

        if not player.playing:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.pause.no_song_playing",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        await player.pause(True)

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "music.pause.paused",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            )
        )