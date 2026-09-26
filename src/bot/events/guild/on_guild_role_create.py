# ./src/events/guild/on_guild_role_create.py

from src.core.logging import logger


async def on_guild_role_create(role):
    logger.info(f'Rol creado: {role}')
