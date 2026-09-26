from discord.ext import commands
import wavelink
import asyncio
import yt_dlp

from src.locales.i18n import translate
from src.core.logging import logger


def get_original_title(url):
    ydl = yt_dlp.YoutubeDL()

    info = ydl.extract_info(url, download=False)

    return info.get("title", "Título desconocido")


class Play(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="play", aliases=["p"])
    async def play(self, ctx, *, query):
        async with ctx.typing():
            if ctx.voice_client is None:
                if not ctx.author.voice:
                    return await ctx.send(
                        translate(
                            ctx.guild,
                            "commands.music.play.voice_not_connected",
                        )
                    )

                player = await ctx.author.voice.channel.connect(
                    cls=wavelink.Player
                )
            else:
                player: wavelink.Player = ctx.voice_client

            tracks = await wavelink.Playable.search(
                query,
                source="ytsearch",
            )

            if not tracks:
                return await ctx.send(
                    translate(
                        ctx.guild,
                        "commands.music.play.no_song_found",
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
                    translate(
                        ctx.guild,
                        "commands.music.play.playlist_added_to_queue",
                        title=playlist_title,
                        count=len(playlist_tracks),
                    )
                )

            track = tracks[0]

            logger.info(
                f"TÍTULO RECIBIDO: {track.title}"
            )

            await player.queue.put_wait(track)

            if player.playing:
                original_title = await asyncio.to_thread(
                    get_original_title,
                    track.uri,
                )

                return await ctx.send(
                    translate(
                        ctx.guild,
                        "commands.music.play.added_to_queue",
                        title=original_title,
                    )
                )

            track = player.queue.get()

            await player.play(track)

        original_title = await asyncio.to_thread(
            get_original_title,
            track.uri,
        )

        await ctx.send(
            translate(
                ctx.guild,
                "commands.music.play.now_playing",
                title=original_title,
            )
        )