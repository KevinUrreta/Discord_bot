from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class On_command(commands.Cog):
    """
    Gestiona el uso de un comando.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self, ctx):
        """
        Registra el uso de un comando.

        :param ctx: Contexto
        :return: None
        """
        logger.info(
            translate(
                None,
                "app.events.logs.other.on_command.command_executed",
                command=ctx.command.name,
                author=ctx.author,
                channel=ctx.channel,
            )
        )
