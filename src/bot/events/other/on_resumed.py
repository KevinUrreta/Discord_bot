# ./src/events/other/on_resumed.py

from src.core.logging import logger


async def on_resumed():
    logger.info('Sesión reanudada')
