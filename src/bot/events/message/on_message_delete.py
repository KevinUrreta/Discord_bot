# ./src/events/message/on_message_delete.py

from src.core.logging import logger


async def on_message_delete(message):
    logger.info(f'Mensaje eliminado: {message.content}')
