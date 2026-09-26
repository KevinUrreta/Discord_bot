# ./src/events/guild/on_guild_channel_delete.py

from src.core.logging import logger


async def on_guild_channel_delete(channel):
    logger.info(f'Canal eliminado: {channel}')
