async def get_prefix(bot, message: discord.Message) -> str:
    """
    Obtiene el prefijo de comandos configurado para un servidor.

    :param bot: Instancia de app del server.
    :param message: Mensaje cuyo server quiere consultar.
    :return: Prefijo de comandos configurado para un server.
    """
    if message.guild is None:
        return "!"

    guild = await bot.guild_repository.get(message.guild.id)

    if guild is None:
        return "!"

    prefix = guild.prefix

    if prefix == "<" and message.content.startswith("<@"):
        return "\0"

    return prefix
