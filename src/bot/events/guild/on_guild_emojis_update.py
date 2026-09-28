from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class GuildEmojisUpdate(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        logger.info(
            translate(
                guild,
                "events.guild.on_guild_emojis_update.emojis_updated",
                guild=guild,
            )
        )
