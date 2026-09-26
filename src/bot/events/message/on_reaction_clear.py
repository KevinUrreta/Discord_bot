# ./src/events/message/on_reaction_clear.py

from src.core.logging import logger


async def on_reaction_clear(message, reactions):
    logger.info(f'Todas las reacciones borradas en {message.id}')
