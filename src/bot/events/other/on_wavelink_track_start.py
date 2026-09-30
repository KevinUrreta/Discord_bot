import asyncio

import wavelink
from discord.ext import commands

from src.core.logging import wavelink_logger
from src.core.player_state import get_music_state
from src.core.player_utils import restore_volume
from src.database.repositories.guild import GuildRepository
from src.helpers.embeds import create_embed
from src.locales.i18n import translate
from src.helpers.music_utils import (
    format_duration,
    get_original_info,
    get_thumbnail
)



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

        if track is None or player.channel is None:
            return

        guild = player.channel.guild
        state = get_music_state(player)

        # wavelink_logger.info(
        #     translate(
        #         guild,
        #         "events.other.on_wavelink_track_start.track_started",
        #         server_name=guild.name,
        #         server_id=guild.id,
        #         track_title=track.title,
        #     )
        # )

        await restore_volume(
            player,
            self.guild_repository,
        )

        if not state.show_now_playing:
            return

        state.show_now_playing = False

        if state.text_channel is None:
            return

        info = await asyncio.to_thread(
            get_original_info,
            track.uri,
        )

        await state.text_channel.send(
            embed=create_embed(
                guild,
                "music.now_playing",
                title=info["title"],
                duration=format_duration(track.length),
                views=info["views"],
                queue=player.queue.count,
                user=state.requester or "Desconocido",
                thumbnail=get_thumbnail(track),
                footer_icon=state.footer_icon,
            )
        )