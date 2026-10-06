from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class VoiceStateUpdate(commands.Cog):
    """
    Gestiona el estado de audio de los usuarios.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        """
        Registra los estados de audio de los usuarios.

        :param member: Miembro
        :param before: Estado antes.
        :param after: Estado después.
        :return: None
        """
        guild = member.guild

        before_channel = before.channel
        after_channel = after.channel

        if before_channel is None and after_channel is not None:
            action = translate(
                None,
                "app.events.logs.other.on_voice_state_update.join",
            )

            message = translate(
                None,
                "app.events.logs.other.on_voice_state_update.voice_state_updated",
                server_name=guild.name,
                member_name=member.name,
                channel_name=after_channel.name,
                action=action,
            )

        elif before_channel is not None and after_channel is None:
            action = translate(
                None,
                "app.events.logs.other.on_voice_state_update.leave",
            )

            message = translate(
                None,
                "app.events.logs.other.on_voice_state_update.voice_state_updated",
                server_name=guild.name,
                member_name=member.name,
                channel_name=before_channel.name,
                action=action,
            )

        elif (
                before_channel is not None
                and after_channel is not None
                and before_channel != after_channel
        ):
            message = translate(
                None,
                "app.events.logs.other.on_voice_state_update.voice_state_moved",
                server_name=guild.name,
                member_name=member.name,
                before_channel_name=before_channel.name,
                after_channel_name=after_channel.name,
            )

        else:
            if after_channel is None:
                return

            if before.self_deaf != after.self_deaf:
                action = translate(
                    None,
                    "app.events.logs.other.on_voice_state_update.deaf_enabled"
                    if after.self_deaf
                    else "app.events.logs.other.on_voice_state_update.deaf_disabled",
                )

            elif before.self_mute != after.self_mute:
                action = translate(
                    None,
                    "app.events.logs.other.on_voice_state_update.mute_enabled"
                    if after.self_mute
                    else "app.events.logs.other.on_voice_state_update.mute_disabled",
                )

            elif before.self_video != after.self_video:
                action = translate(
                    None,
                    "app.events.logs.other.on_voice_state_update.video_enabled"
                    if after.self_video
                    else "app.events.logs.other.on_voice_state_update.video_disabled",
                )

            elif before.self_stream != after.self_stream:
                action = translate(
                    None,
                    "app.events.logs.other.on_voice_state_update.stream_enabled"
                    if after.self_stream
                    else "app.events.logs.other.on_voice_state_update.stream_disabled",
                )

            else:
                return

            message = translate(
                None,
                "app.events.logs.other.on_voice_state_update.voice_state_updated",
                server_name=guild.name,
                member_name=member.name,
                channel_name=after_channel.name,
                action=action,
            )

        logger.info(message)
