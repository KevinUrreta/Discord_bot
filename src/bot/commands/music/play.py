import asyncio

import wavelink
import yt_dlp
from discord.ext import commands

from src.core.music_state import get_music_state
from src.helpers.embeds import create_embed


def get_original_info(url):
    ydl = yt_dlp.YoutubeDL(
        {
            "quiet": True,
            "no_warnings": True,
        }
    )

    info = ydl.extract_info(url, download=False)

    return {
        "title": info.get("title", "Título desconocido"),
        "views": info.get("view_count", 0),
    }


def format_duration(milliseconds):
    total_seconds = int(milliseconds / 1000)
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes}:{seconds:02d}"


def get_thumbnail(track):
    if track.artwork:
        return track.artwork

    if track.identifier:
        return (
            f"https://img.youtube.com/vi/"
            f"{track.identifier}/hqdefault.jpg"
        )

    return None


class Play(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="play", aliases=["p"])
    async def play(self, ctx, *, query):
        if ctx.voice_client is None:
            if not ctx.author.voice:
                return await ctx.send(
                    embed=create_embed(
                        ctx.guild,
                        "music.play.voice_not_connected",
                        user=ctx.author.display_name,
                        footer_icon=ctx.author.display_avatar.url,
                    )
                )

            player = await ctx.author.voice.channel.connect(
                cls=wavelink.Player
            )
        else:
            player: wavelink.Player = ctx.voice_client

        state = get_music_state(player)
        state.text_channel = ctx.channel
        state.requester = ctx.author.display_name
        state.footer_icon = ctx.author.display_avatar.url

        tracks = await wavelink.Playable.search(
            query,
            source="ytsearch",
        )

        if not tracks:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.play.no_song_found",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

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

            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.play.playlist_added_to_queue",
                    title=playlist_title,
                    queue=player.queue.count,
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        track = tracks[0]

        await player.queue.put_wait(track)

        if player.playing:
            info = await asyncio.to_thread(
                get_original_info,
                track.uri,
            )

            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "music.play.added_to_queue",
                    title=info["title"],
                    queue=player.queue.count,
                    user=ctx.author.display_name,
                    thumbnail=get_thumbnail(track),
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        track = player.queue.get()

        await player.play(track)

        info = await asyncio.to_thread(
            get_original_info,
            track.uri,
        )

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "music.now_playing",
                title=info["title"],
                duration=format_duration(track.length),
                views=info["views"],
                queue=player.queue.count,
                user=ctx.author.display_name,
                thumbnail=get_thumbnail(track),
                footer_icon=ctx.author.display_avatar.url,
            )
        )