# ./src/events/other/on_connect.py

from src.core.logging import logger


async def on_connect():
    logger.info('Conectado a Discord')
