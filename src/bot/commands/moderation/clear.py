from discord.ext import commands

from src.helpers.permissions import has_manage_messages


class Cls(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_manage_messages()
    async def cls(
        self,
        ctx,
        *,
        limit: int = 1,
    ):
        if limit < 1:
            return

        await ctx.channel.purge(limit=limit + 1)