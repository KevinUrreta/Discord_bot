from discord.ext import commands

from src.helpers.embeds import create_embed


class Leave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="leave", aliases=["disconnect"])
    async def leave(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.leave.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        await ctx.voice_client.disconnect()

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "bot.commands.music.embeds.leave.disconnected",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            )
        )