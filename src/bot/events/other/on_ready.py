import wavelink

from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class On_ready(commands.Cog):
    """
    Gestiona cuando el bot esta preparado.
    """
    def __init__(self, bot, lavalink_password):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot
        self.lavalink_password = lavalink_password

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Cuando el bot esta preparado, hace la conexión con Lavalink.

        :return: None
        """
        logger.info(
            translate(
                None,
                "bot.events.logs.other.on_ready.bot_connected",
                bot=self.bot.user,
            )
        )

        if not wavelink.Pool.nodes:
            logger.info(
                translate(
                    None,
                    "bot.events.logs.other.on_ready.connecting_lavalink",
                )
            )

            await wavelink.Pool.connect(
                nodes=[
                    wavelink.Node(
                        identifier="main",
                        uri="http://lavalink:2333",
                        password=self.lavalink_password,
                    )
                ],
                client=self.bot,
            )