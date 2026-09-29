from typing import cast

import wavelink

from src.database.repositories.guild import GuildRepository


async def restore_volume(
    player: wavelink.Player,
    guild_repository: GuildRepository,
) -> None:
    guild = player.guild

    if guild is None:
        return

    guild_data = await guild_repository.get(guild.id)

    if guild_data is None:
        return

    volume = cast(int, guild_data.volume)

    await player.set_volume(volume)