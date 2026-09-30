from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class ReactionRemove(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        logger.info(
            translate(
                None,
                "bot.events.logs.message.on_reaction_remove.reaction_removed",
                channel=reaction.message.channel, emoji=reaction.emoji, user=user,
            )
        )
