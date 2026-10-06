from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class ApplicationCommandError(commands.Cog):
    """
    Gestiona cuando hay un error en el app.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_app_command_error(self, interaction, error):
        """
        Registra cuando un error en el app.

        :param interaction: Interacción en la que ha ocurrido.
        :param error: Error
        :return: None
        """
        logger.info(
            translate(
                None,
                "app.events.logs.other.on_application_command_error.command_error",
                command=interaction.command, error=error,
            )
        )
