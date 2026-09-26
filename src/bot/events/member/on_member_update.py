# ./src/events/member/on_member_update.py

from src.core.logging import logger


async def on_member_update(before, after):
    logger.info(f'Miembro actualizado: {before} → {after}')
