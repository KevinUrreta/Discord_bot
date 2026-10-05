async def get_prefix(bot, message: discord.Message) -> str:
    if message.guild is None:
        return "!"

    guild = await bot.guild_repository.get(message.guild.id)

    if guild is None:
        return "!"

    prefix = guild.prefix

    if prefix == "<" and message.content.startswith("<@"):
        return "\0"

    return prefix