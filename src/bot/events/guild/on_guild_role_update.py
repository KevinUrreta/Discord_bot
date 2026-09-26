# ./src/events/guild/on_guild_role_update.py

from src.core.logging import logger


async def on_guild_role_update(before, after):
    logger.info(f'Rol actualizado: {before} → {after}')
