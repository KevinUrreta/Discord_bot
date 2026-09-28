from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class VoiceStateUpdate(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        logger.info(
            translate(
                member.guild,
                "events.other.on_voice_state_update.voice_state_updated",
                member=member, before=before, after=after,
            )
        )
