# ./src/events/other/on_disconnect.py

from src.core.logging import logger


async def on_disconnect():
    logger.info('Desconectado de Discord')
