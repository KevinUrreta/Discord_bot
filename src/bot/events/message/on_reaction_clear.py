from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class ReactionClear(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_clear(self, message, reactions):
        logger.info(
            translate(
                None,
                "bot.events.logs.message.on_reaction_clear.reactions_cleared",
                message=message,
            )
        )
