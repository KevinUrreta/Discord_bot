import discord
from discord.ext import commands


def has_manage_messages():
    """
    Comprueba que el usuario tenga permiso para gestionar mensajes.

    :return: Check que valida el permiso del usuario.
    """

    async def predicate(ctx: commands.Context) -> bool:
        if ctx.guild is None:
            return False

        if not isinstance(ctx.author, discord.Member):
            return False

        return ctx.author.guild_permissions.manage_messages

    return commands.check(predicate)


def has_manage_guild():
    """
    Comprueba que el usuario tenga permiso para gestionar el servidor.

    :return: Check que valida el permiso del usuario.
    """

    async def predicate(ctx: commands.Context) -> bool:
        if ctx.guild is None:
            return False

        if not isinstance(ctx.author, discord.Member):
            return False

        return ctx.author.guild_permissions.manage_guild

    return commands.check(predicate)


class VoiceChannelRequired(commands.CheckFailure):
    """
    Excepción utilizada cuando un comando requiere un canal de voz

    Se lanza cuando el usuario no está conectado a un canal de voz,
    cuando el comando se ejecuta fuera de un servidor o cuando el
    usuario no pertenece al servidor como miembro de Discord.
    """
    pass


def has_voice_channel():
    """
    Comprueba que el usuario esté conectado al canal de voz adecuado.
    :return: Check que valida la conexión al canal de voz.
    """

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
