from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class GuildStickersUpdate(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_stickers_update(self, guild, before, after):
        logger.info(
            translate(
                None,
                "bot.events.logs.guild.on_guild_stickers_update.stickers_updated",
                guild_name=guild.name,
                guild_id=guild.id,
            )
        )
