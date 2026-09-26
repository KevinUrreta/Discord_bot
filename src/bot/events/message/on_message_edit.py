# ./src/events/message/on_message_edit.py

from src.core.logging import logger


async def on_message_edit(before, after):
    logger.info(f'Mensaje editado: {before.content} → {after.content}')
