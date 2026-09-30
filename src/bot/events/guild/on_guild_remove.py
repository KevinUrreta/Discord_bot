import discord
from discord.ext import commands

from src.core.logging import logger
from src.database.repositories.guild import GuildRepository
from src.database.repositories.member import MemberRepository
from src.locales.i18n import translate


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
    async def on_guild_remove(
        self,
        guild: discord.Guild,
    ):
        deleted_members = await self.member_repository.delete_by_guild(
            guild.id
        )

        deleted_guild = await self.guild_repository.delete(
            guild.id
        )

        logger.info(
            translate(
                None,
                "bot.events.logs.guild.on_guild_remove.members_deleted",
                guild_name=guild.name,
                guild_id=guild.id,
                deleted_members=deleted_members,
            )
        )

        if deleted_guild:
            logger.info(
                translate(
                    None,
                    "bot.events.logs.guild.on_guild_remove.guild_deleted",
                    guild_name=guild.name,
                    guild_id=guild.id,
                )
            )
        else:
            logger.info(
                translate(
                    None,
                    "bot.events.logs.guild.on_guild_remove.guild_not_found",
                    guild_name=guild.name,
                    guild_id=guild.id,
                )
            )