import wavelink

from src.core.config import settings
from src.core.logging import logger
from src.i18n.translator import translate


async def connect_lavalink(bot):
    """
    Conecta el bot con Lavalink.

    :param bot: Instancia principal del bot de Discord.
    :return: None
    """
    if wavelink.Pool.nodes:
        return

    logger.info(translate(
            None,
            "app.events.logs.other.on_ready.connecting_lavalink",
        ))

    await wavelink.Pool.connect(
        nodes=[
            wavelink.Node(
                identifier="main",
                uri=settings.lavalink_uri,
                password=settings.lavalink_password,
            )
        ],
        client=bot,
    )