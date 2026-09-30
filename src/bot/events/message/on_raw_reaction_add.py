from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class RawReactionAdd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        logger.info(
            translate(
                self.bot.get_guild(payload.guild_id),
                "bot.events.logs.message.on_raw_reaction_add.reaction_added",
                message_id=payload.message_id, emoji=payload.emoji, user=payload.user_id,
            )
        )
