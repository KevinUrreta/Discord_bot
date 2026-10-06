from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class Typing(commands.Cog):
    """
    Gestiona los usuarios escribiendo en un server.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        """
        Registra cuando un usuario escribe.
        :param channel: Canal.
        :param user: Usuario.
        :param when: Momento.
        :return: None
        """
        logger.info(
            translate(
                None,
                "app.events.logs.message.on_typing.typing_detected",
                user=user,
                channel=channel,
            )
        )
