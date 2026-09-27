import discord
from discord.ext import commands

from src.core.logging import logger
from src.database.repositories.member import MemberRepository


class On_member_remove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.member_repository = MemberRepository(
            self.bot.database
        )

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        deleted = await self.member_repository.delete(
            member_id=member.id,
            guild_id=member.guild.id,
        )

        if deleted:
            logger.info(
                f"Miembro eliminado: {member.name} "
                f"({member.id}) de {member.guild.name} "
                f"({member.guild.id})"
            )
        else:
            logger.info(
                f"Miembro no encontrado en la BD: "
                f"{member.name} ({member.id}) en "
                f"{member.guild.name} ({member.guild.id})"
            )