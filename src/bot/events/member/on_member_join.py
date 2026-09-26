# ./src/events/member/on_member_join.py

from src.core.logging import logger


async def on_member_join(member):
    logger.info(f'Miembro entró: {member}')
