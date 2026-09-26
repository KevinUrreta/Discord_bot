import wavelink
from discord.ext import commands


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

        if player.queue.is_empty and player.queue.mode == wavelink.QueueMode.normal:
            return

        track = player.queue.get()

        await player.play(track)