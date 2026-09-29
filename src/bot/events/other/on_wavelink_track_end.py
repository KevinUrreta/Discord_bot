import wavelink
from discord.ext import commands

from src.core.logging import wavelink_logger
from src.core.player_state import get_music_state
from src.locales.i18n import translate


class On_wavelink_track_end(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_wavelink_track_end(
        self,
        payload: wavelink.TrackEndEventPayload,
    ):
        if payload.player is None:
            return

        player = payload.player
        track = player.current

        if track is not None:
            if player.channel is None:
                return

            guild = player.channel.guild

            # wavelink_logger.info(
            #     translate(
            #         guild,
            #         "events.other.on_wavelink_track_end.track_ended",
            #         server_name=guild.name,
            #         server_id=guild.id,
            #         track_title=track.title,
            #     )
            # )

        if (
            player.queue.is_empty
            and player.queue.mode == wavelink.QueueMode.normal
        ):
            return

        next_track = player.queue.get()

        state = get_music_state(player)
        state.show_now_playing = True

        await player.play(next_track)