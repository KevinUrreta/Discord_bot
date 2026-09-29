import wavelink
from discord.ext import commands

from src.core.logging import wavelink_logger
from src.core.player import restore_volume
from src.database.repositories.guild import GuildRepository
from src.locales.i18n import translate


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

        player = payload.player
        track = player.current

        if track is not None and player.channel is not None:
            guild = player.channel.guild

            wavelink_logger.info(
                translate(
                    guild,
                    "events.other.on_wavelink_track_start.track_started",
                    server_name=guild.name,
                    server_id=guild.id,
                    track_title=track.title,
                )
            )

        await restore_volume(
            player,
            self.guild_repository,
        )