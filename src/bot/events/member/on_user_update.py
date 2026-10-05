import discord
from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class On_user_update(commands.Cog):
    """
    Gestiona las modificaciones de un usuario.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_user_update(self, before: discord.User, after: discord.User):
        """
        Modifica los valores que hayan cambiado de un usuario en la base de datos.

        :param before: Estado después.
        :param after: Estado antes.
        :return: None
        """
        if before.name != after.name:
            logger.info(
                translate(
                    None,
                    "bot.events.logs.member.on_user_update.username_updated",
                    before_name=before.name,
                    id=after.id,
                    after_name=after.name,
                )
            )

        if before.global_name != after.global_name:
            logger.info(
                translate(
                    None,
                    "bot.events.logs.member.on_user_update.global_name_updated",
                    before_name=before.global_name,
                    id=after.id,
                    after_name=after.global_name,
                )
            )

        if before.avatar != after.avatar:
            logger.info(
                translate(
                    None,
                    "bot.events.logs.member.on_user_update.avatar_updated",
                    name=after.name,
                    id=after.id,
                )
            )