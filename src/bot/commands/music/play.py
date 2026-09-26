from discord.ext import commands
from typing import cast
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

            if isinstance(tracks, wavelink.Playlist):
                for track in tracks.tracks:
                    await player.queue.put_wait(track)

                if player.playing:
                    return await ctx.send(
                        translate(
                            ctx.guild,
                            "playlist_added_to_queue",
                            title=tracks.name,
                            count=len(tracks.tracks),
                        )
                    )

                track = player.queue.get()
            else:
                track = tracks[0]
                logger.info(f"TÍTULO RECIBIDO: {track.title}")

                await player.queue.put_wait(track)

                if player.playing:
                    return await ctx.send(
                        translate(
                            ctx.guild,
                            "commands.music.play.added_to_queue",
                            title=track.title,
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