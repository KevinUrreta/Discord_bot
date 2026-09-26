# ./src/events/message/on_raw_reaction_remove.py

from src.core.logging import logger


async def on_raw_reaction_remove(payload):
    logger.info(f'Reacción raw eliminada: {payload}')
