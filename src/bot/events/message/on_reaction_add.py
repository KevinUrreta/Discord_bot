from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class ReactionAdd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        logger.info(
            translate(
                reaction.message.guild,
                "events.message.on_reaction_add.reaction_added",
                channel=reaction.message.channel, emoji=reaction.emoji, user=user,
            )
        )
