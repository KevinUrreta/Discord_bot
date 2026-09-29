from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class VoiceStateUpdate(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        guild = member.guild

        before_channel = before.channel
        after_channel = after.channel

        if before_channel is None and after_channel is not None:
            action = "JOIN"
            channel = after_channel

        elif before_channel is not None and after_channel is None:
            action = "LEAVE"
            channel = before_channel

        elif before_channel != after_channel:
            action = "MOVE"
            channel = after_channel

        else:
            action = "UPDATE"
            channel = after_channel

        channel_name = channel.name if channel else "Ninguno"
        channel_id = channel.id if channel else "N/A"

        logger.info(
            translate(
                guild,
                "events.other.on_voice_state_update.voice_state_updated",
                server_name=guild.name,
                member_name=member.name,
                channel_name=channel_name,
                action=action,
            )
        )