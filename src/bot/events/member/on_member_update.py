import discord
from discord.ext import commands

from src.core.logging import logger
from src.database.repositories.member import MemberRepository
from src.locales.i18n import translate


class On_member_update(commands.Cog):
    """
    Gestiona la modificación de un miembro de un server.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot
        self.member_repository = MemberRepository(self.bot.database)

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        """
        Actualiza los valores nuevos de un miembro de un server.
        :param before: Estado antes.
        :param after: Estado después.
        :return: None
        """
        changes = {}

        if before.name != after.name:
            changes["name"] = after.name

        if before.display_name != after.display_name:
            changes["display_name"] = after.display_name

        if not changes:
            return

        await self.member_repository.update(member_id=after.id, guild_id=after.guild.id, **changes)

        logger.info(
            translate(
                None,
                "bot.events.logs.member.on_member_update.member_updated",
                name=after.name,
                id=after.id,
                guild_name=after.guild.name,
                guild_id=after.guild.id,
            )
        )