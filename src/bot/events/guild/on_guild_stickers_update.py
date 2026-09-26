# ./src/events/guild/on_guild_stickers_update.py

from src.core.logging import logger


async def on_guild_stickers_update(guild, before, after):
    logger.info(f'Stickers actualizados en {guild}')
