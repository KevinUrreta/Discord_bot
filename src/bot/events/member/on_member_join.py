import discord
from discord.ext import commands

from src.core.logging import logger
from src.database.repositories.member import MemberRepository


class On_member_join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.member_repository = MemberRepository(
            self.bot.database
        )

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        await self.member_repository.create(
            member_id=member.id,
            guild_id=member.guild.id,
            name=member.name,
            display_name=member.display_name,
            joined_at=member.joined_at,
        )

        logger.info(
            f"Miembro añadido: {member.name} "
            f"({member.id}) en {member.guild.name} "
            f"({member.guild.id})"
        )