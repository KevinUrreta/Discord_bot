# ./src/events/other/on_voice_state_update.py

from src.core.logging import logger


async def on_voice_state_update(member, before, after):
    """
    Evento de Discord para cambios de estado de voz.

    La gestión real de la conexión de voz la realiza Wavelink.
    No debemos manipular manualmente session_id, token ni endpoint.
    """
    logger.info(f'Estado de voz cambiado: {member}')


    # Ignorar cambios que no sean relevantes para Kizy.
    if member.bot:
        return

    logger.debug(
        "Cambio de voz: %s | %s -> %s",
        member,
        getattr(before.channel, "name", None),
        getattr(after.channel, "name", None),
    )