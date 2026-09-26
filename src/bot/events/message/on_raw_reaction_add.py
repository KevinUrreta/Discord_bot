# ./src/events/message/on_raw_reaction_add.py

from src.core.logging import logger


async def on_raw_reaction_add(payload):
    logger.info(f'Reacción raw añadida: {payload}')
