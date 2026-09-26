# ./src/events/member/on_member_remove.py

from src.core.logging import logger


async def on_member_remove(member):
    logger.info(f'Miembro salió: {member}')
