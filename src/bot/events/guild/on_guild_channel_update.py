# ./src/events/guild/on_guild_channel_update.py

from src.core.logging import logger


async def on_guild_channel_update(before, after):
    logger.info(f'Canal actualizado: {before} → {after}')
