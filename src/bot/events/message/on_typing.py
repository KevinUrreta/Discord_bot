from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class Typing(commands.Cog):
    """
    Gestiona los usuarios escribiendo en un server.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
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
                "bot.events.logs.message.on_typing.typing_detected",
                user=user,
                channel=channel,
            )
        )