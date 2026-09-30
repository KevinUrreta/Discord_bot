import discord
from discord.ext import commands

from src.core.logging import logger
from src.database.repositories.member import MemberRepository
from src.locales.i18n import translate


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