from discord.ext import commands
import wavelink

from src.helpers.embeds import create_embed


class Resume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="resume")
    async def resume(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.resume.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player: wavelink.Player = ctx.voice_client

        if not player.paused:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.resume.no_song_playing",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        await player.pause(False)

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "bot.commands.music.embeds.resume.resumed",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            )
        )