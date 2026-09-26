# ./src/events/other/on_webhook_update.py

from src.core.logging import logger


async def on_webhook_update(channel):
    logger.info(f'Webhook actualizado en {channel}')
