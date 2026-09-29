import discord
from discord.ext import commands

from src.core.logging import logger
from src.database.repositories.guild import GuildRepository
from src.database.repositories.member import MemberRepository
from src.locales.i18n import translate


class On_guild_join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.guild_repository = GuildRepository(
            self.bot.database
        )

        self.member_repository = MemberRepository(
            self.bot.database
        )

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        await self.guild_repository.create(
            guild_id=guild.id,
            name=guild.name,
        )

        for member in guild.members:
            await self.member_repository.create(
                member_id=member.id,
                guild_id=guild.id,
                name=member.name,
                display_name=member.display_name,
                joined_at=member.joined_at,
            )

        logger.info(
            translate(
                None,
                "events.guild.on_guild_join.guild_added",
                guild_name=guild.name,
                guild_id=guild.id,
            )
        )