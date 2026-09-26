# ./src/events/guild/on_guild_role_delete.py

from src.core.logging import logger

async def on_guild_role_delete(role):
    logger.info(f'Rol eliminado: {role}')
