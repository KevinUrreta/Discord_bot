from discord.ext import commands
import wavelink

from src.helpers.embeds import create_embed
from src.helpers.permissions import has_voice_channel


class Pause(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @has_voice_channel()
    @commands.command(name="pause")
    async def pause(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.pause.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player: wavelink.Player = ctx.voice_client

        if not player.playing:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.pause.no_song_playing",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        await player.pause(True)

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "bot.commands.music.embeds.pause.paused",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            )
        )