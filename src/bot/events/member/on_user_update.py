# ./src/events/member/on_user_update.py

from src.core.logging import logger


async def on_user_update(before, after):
    logger.info(f'Usuario actualizado: {before} → {after}')
