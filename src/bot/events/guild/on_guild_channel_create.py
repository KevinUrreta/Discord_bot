from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class GuildChannelCreate(commands.Cog):
    """
    Gestiona la creación de canales de un server.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        """
        Registra la creación de un nuevo canal de un server.

        :param channel: Canal del server.
        :return: None
        """
        logger.info(
            translate(
                None,
                "bot.events.logs.guild.on_guild_channel_create.channel_created",
                channel=channel,
            )
        )
