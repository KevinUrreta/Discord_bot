# ./src/events/guild/on_guild_emojis_update.py

from src.core.logging import logger


async def on_guild_emojis_update(guild, before, after):
    logger.info(f'Emojis actualizados en {guild}')
