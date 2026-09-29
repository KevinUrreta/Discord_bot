import discord
from discord.ext import commands

from src.core.logging import logger
from src.database.repositories.member import MemberRepository
from src.locales.i18n import translate


class On_member_update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.member_repository = MemberRepository(
            self.bot.database
        )

    @commands.Cog.listener()
    async def on_member_update(
        self,
        before: discord.Member,
        after: discord.Member,
    ):
        changes = {}

        if before.name != after.name:
            changes["name"] = after.name

        if before.display_name != after.display_name:
            changes["display_name"] = after.display_name

        if not changes:
            return

        await self.member_repository.update(
            member_id=after.id,
            guild_id=after.guild.id,
            **changes,
        )

        logger.info(
            translate(
                None,
                "events.member.on_member_update.member_updated",
                name=after.name,
                id=after.id,
                guild_name=after.guild.name,
                guild_id=after.guild.id,
            )
        )