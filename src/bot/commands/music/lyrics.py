from discord.ext import commands

from src.helpers.embeds import create_embed


class Lyrics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="lyrics")
    async def lyrics(self, ctx, *, query=None):
        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "bot.commands.music.embeds.lyrics.not_available",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            )
        )