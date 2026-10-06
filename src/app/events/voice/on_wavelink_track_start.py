import asyncio

import wavelink
from discord.ext import commands

from src.core.player_state import get_music_state
from src.helpers.embeds import create_embed
from src.helpers.formatting import format_duration
from src.helpers.music_utils import (
    get_original_info,
    get_thumbnail
)
from src.helpers.music_utils import restore_volume
from src.infrastructure.database.repositories.guild import GuildRepository


class On_wavelink_track_start(commands.Cog):
    """
    Gestiona el inicio de una reproducción.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot
        self.guild_repository = GuildRepository(self.bot.database)

    @commands.Cog.listener()
    async def on_wavelink_track_start(self, payload: wavelink.TrackStartEventPayload):
        """
        Comprueba si el usuario está presente en el canal de audio y reproduce.

        :param payload: Datos
        :return: None
        """
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
        #         "app.events.logs.other.on_wavelink_track_start.track_started",
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
                "app.commands.music.embeds.now_playing",
                title=info["title"],
                duration=format_duration(track.length),
                views=info["views"],
                queue=player.queue.count,
                user=state.requester or "Desconocido",
                thumbnail=get_thumbnail(track),
                footer_icon=state.footer_icon,
            )
        )
