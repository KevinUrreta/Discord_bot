# ./src/events/message/on_reaction_add.py

from src.core.logging import logger


async def on_reaction_add(reaction, user):
    logger.info(f'Reacción añadida: {reaction} por {user}')
