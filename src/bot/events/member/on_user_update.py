import discord
from discord.ext import commands

from src.core.logging import logger


class On_user_update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_user_update(self, before: discord.User, after: discord.User,):
        if before.name != after.name:
            logger.info(
                f"Usuario actualizado: {before.name} "
                f"({after.id}) -> {after.name} ({after.id})"
            )

        if before.global_name != after.global_name:
            logger.info(
                f"Nombre global actualizado: "
                f"{before.global_name} ({after.id}) -> "
                f"{after.global_name} ({after.id})"
            )

        if before.avatar != after.avatar:
            logger.info(
                f"Avatar actualizado: "
                f"{after.name} ({after.id})"
            )