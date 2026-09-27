import wavelink
from discord.ext import commands

from src.core.player import restore_volume
from src.database.repositories.guild import GuildRepository


class On_wavelink_track_start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.guild_repository = GuildRepository(
            self.bot.database
        )

    @commands.Cog.listener()
    async def on_wavelink_track_start(
        self,
        payload: wavelink.TrackStartEventPayload,
    ):
        if payload.player is None:
            return

        await restore_volume(
            payload.player,
            self.guild_repository,
        )