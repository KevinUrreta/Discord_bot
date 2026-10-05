import discord
from discord.ext import commands

from src.core.logging import logger
from src.database.repositories.member import MemberRepository
from src.locales.i18n import translate


class On_member_remove(commands.Cog):
    """
    Gestiona la eliminación de un miembro de un server.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot
        self.member_repository = MemberRepository(self.bot.database)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        """
        Elimina un miembro del server de la base de datos.
        :param member: Miembro
        :return: None
        """
        deleted = await self.member_repository.delete(member_id=member.id, guild_id=member.guild.id)

        if deleted:
            logger.info(
                translate(
                    None,
                    "bot.events.logs.member.on_member_remove.member_deleted",
                    name=member.name,
                    id=member.id,
                    guild_name=member.guild.name,
                    guild_id=member.guild.id,
                )
            )
        else:
            logger.info(
                translate(
                    None,
                    "bot.events.logs.member.on_member_remove.member_not_found",
                    name=member.name,
                    id=member.id,
                    guild_name=member.guild.name,
                    guild_id=member.guild.id,
                )
            )