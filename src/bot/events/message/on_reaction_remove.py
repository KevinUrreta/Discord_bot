# ./src/events/message/on_reaction_remove.py

from src.core.logging import logger


async def on_reaction_remove(reaction, user):
    logger.info(f'Reacción eliminada: {reaction} por {user}')
