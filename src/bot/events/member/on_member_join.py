import discord
from discord.ext import commands

from src.core.logging import logger
from src.database.repositories.member import MemberRepository
from src.locales.i18n import translate


class On_member_join(commands.Cog):
    """
    Gestiona la unión de un miembro a un server.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot
        self.member_repository = MemberRepository(self.bot.database)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """
        Crea la unión del miembro a la base de datos.
        :param member: Miembro.
        :return: None
        """
        await self.member_repository.create(
            member_id=member.id,
            guild_id=member.guild.id,
            name=member.name,
            display_name=member.display_name,
            joined_at=member.joined_at,
        )

        logger.info(
            translate(
                None,
                "bot.events.logs.member.on_member_join.member_added",
                name=member.name,
                id=member.id,
                guild_name=member.guild.name,
                guild_id=member.guild.id,
            )
        )