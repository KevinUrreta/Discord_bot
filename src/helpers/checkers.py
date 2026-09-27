import discord
from discord.ext import commands


def has_manage_guild():
    async def predicate(
        ctx: commands.Context,
    ) -> bool:
        if ctx.guild is None:
            return False

        if not isinstance(ctx.author, discord.Member):
            return False

        return ctx.author.guild_permissions.manage_guild

    return commands.check(predicate)
