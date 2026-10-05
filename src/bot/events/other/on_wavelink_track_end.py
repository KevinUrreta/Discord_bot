import asyncio

import wavelink
from discord.ext import commands

from src.core.player_state import get_music_state
from src.helpers.embeds import create_embed


IDLE_DISCONNECT_DELAY = 60


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

        if player.channel is None:
            return

        if (
            player.queue.is_empty
            and player.queue.mode == wavelink.QueueMode.normal
        ):
            state = get_music_state(player)
            text_channel = state.text_channel
            guild = player.channel.guild

            await asyncio.sleep(IDLE_DISCONNECT_DELAY)

            if player.current is None and player.queue.is_empty:
                await player.disconnect()

                if text_channel is not None:
                    await text_channel.send(
                        embed=create_embed(
                            guild,
                            "bot.events.embeds.other.idle_disconnect",
                        )
                    )

            return

        next_track = player.queue.get()

        state = get_music_state(player)
        state.show_now_playing = True

        await player.play(next_track)