import discord
from discord.ext import commands

from src.core.logging import logger
from src.database.repositories.guild import GuildRepository
from src.database.repositories.member import MemberRepository


class On_guild_remove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.guild_repository = GuildRepository(
            self.bot.database
        )

        self.member_repository = MemberRepository(
            self.bot.database
        )

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        deleted_members = await self.member_repository.delete_by_guild(
            guild.id
        )

        deleted_guild = await self.guild_repository.delete(
            guild.id
        )

        logger.info(
            f"Miembros eliminados: {deleted_members} "
            f"de {guild.name} ({guild.id})"
        )

        if deleted_guild:
            logger.info(
                f"Servidor eliminado: {guild.name} ({guild.id})"
            )
        else:
            logger.info(
                f"Servidor no encontrado en la BD: "
                f"{guild.name} ({guild.id})"
            )
