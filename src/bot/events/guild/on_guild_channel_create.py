# ./src/events/guild/on_guild_channel_create.py

from src.core.logging import logger


async def on_guild_channel_create(channel):
    logger.info(f'Canal creado: {channel}')
