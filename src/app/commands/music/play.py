import asyncio

import wavelink
from discord.ext import commands

from src.core.player_state import get_music_state
from src.helpers.permissions import has_voice_channel
from src.helpers.embeds import create_embed
from src.helpers.music_utils import (
    format_duration,
    get_original_info,
    get_thumbnail,
)


class Play(commands.Cog):
    """
    Gestiona el comando para reproducir música.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @has_voice_channel()
    @commands.command(name="play", aliases=["p"])
    async def play(self, ctx, *, query):
        """
        Reproduce una canción que solicite el miembro.

        :param ctx: Contexto del comando.
        :param query: Canción a reproducir.
        :return: None
        """
        if ctx.voice_client is None:
            if not ctx.author.voice:
                return await ctx.send(embed=create_embed(
                        ctx.guild,
                        "app.commands.music.embeds.play.voice_not_connected",
                        user=ctx.author.display_name,
                        footer_icon=ctx.author.display_avatar.url,
                    ))

            player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            player: wavelink.Player = ctx.voice_client

        tracks = await wavelink.Playable.search(query, source="ytsearch")

        if not tracks:
            return await ctx.send(embed=create_embed(
                    ctx.guild,
                    "app.commands.music.embeds.play.no_song_found",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                ))

        state = get_music_state(player)
        state.text_channel = ctx.channel
        state.requester = ctx.author.display_name
        state.footer_icon = ctx.author.display_avatar.url

        is_playlist = "list=" in query

        if isinstance(tracks, wavelink.Playlist) or is_playlist:
            if isinstance(tracks, wavelink.Playlist):
                playlist_tracks = tracks.tracks
                playlist_title = tracks.name
            else:
                playlist_tracks = tracks
                playlist_title = (
                    playlist_tracks[0].title
                    if playlist_tracks
                    else "Lista"
                )

            for track in playlist_tracks:
                await player.queue.put_wait(track)

            if not player.playing:
                track = player.queue.get()
                await player.play(track)

            return await ctx.send(embed=create_embed(
                    ctx.guild,
                    "app.commands.music.embeds.play.playlist_added_to_queue",
                    title=playlist_title,
                    queue=player.queue.count,
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                ))

        track = tracks[0]
        await player.queue.put_wait(track)
        info = await asyncio.to_thread(get_original_info, track.uri)

        if player.playing:
            return await ctx.send(embed=create_embed(
                    ctx.guild,
                    "app.commands.music.embeds.play.added_to_queue",
                    title=info["title"],
                    queue=player.queue.count,
                    user=ctx.author.display_name,
                    thumbnail=get_thumbnail(track),
                    footer_icon=ctx.author.display_avatar.url,
                ))

        track = player.queue.get()
        await player.play(track)

        await ctx.send(embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.now_playing",
                title=info["title"],
                duration=format_duration(track.length),
                views=info["views"],
                queue=player.queue.count,
                user=ctx.author.display_name,
                thumbnail=get_thumbnail(track),
                footer_icon=ctx.author.display_avatar.url,
            ))