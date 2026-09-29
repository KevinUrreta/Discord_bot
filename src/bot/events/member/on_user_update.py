import discord
from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class On_user_update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_user_update(
        self,
        before: discord.User,
        after: discord.User,
    ):
        if before.name != after.name:
            logger.info(
                translate(
                    None,
                    "events.member.on_user_update.username_updated",
                    before_name=before.name,
                    id=after.id,
                    after_name=after.name,
                )
            )

        if before.global_name != after.global_name:
            logger.info(
                translate(
                    None,
                    "events.member.on_user_update.global_name_updated",
                    before_name=before.global_name,
                    id=after.id,
                    after_name=after.global_name,
                )
            )

        if before.avatar != after.avatar:
            logger.info(
                translate(
                    None,
                    "events.member.on_user_update.avatar_updated",
                    name=after.name,
                    id=after.id,
                )
            )