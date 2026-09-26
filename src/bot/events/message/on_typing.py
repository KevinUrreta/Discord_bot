# ./src/events/message/on_typing.py

from src.core.logging import logger


async def on_typing(channel, user, when):
    logger.info(f'{user} está escribiendo en {channel}')
