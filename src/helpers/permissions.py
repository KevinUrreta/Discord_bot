import discord
from discord.ext import commands



def has_manage_messages():
    async def predicate(ctx: commands.Context) -> bool:
        if ctx.guild is None:
            return False

        if not isinstance(ctx.author, discord.Member):
            return False

        return ctx.author.guild_permissions.manage_messages

    return commands.check(predicate)


def has_manage_guild():
    async def predicate(ctx: commands.Context) -> bool:
        if ctx.guild is None:
            return False

        if not isinstance(ctx.author, discord.Member):
            return False

        return ctx.author.guild_permissions.manage_guild

    return commands.check(predicate)


class VoiceChannelRequired(commands.CheckFailure):
    pass


def has_voice_channel():
    async def predicate(ctx: commands.Context) -> bool:
        if ctx.guild is None:
            raise VoiceChannelRequired

        if not isinstance(ctx.author, discord.Member):
            raise VoiceChannelRequired

        if ctx.author.voice is None:
            raise VoiceChannelRequired

        if ctx.voice_client is not None:
            if ctx.author.voice.channel != ctx.voice_client.channel:
                raise VoiceChannelRequired

        return True

    return commands.check(predicate)