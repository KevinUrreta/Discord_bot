from unittest.mock import AsyncMock, MagicMock, patch

import wavelink

from src.bot.commands.music.play import Play


async def test_play_without_voice():
    bot = MagicMock()
    cog = Play(bot)

    ctx = MagicMock()
    ctx.voice_client = None
    ctx.author.voice = None
    ctx.send = AsyncMock()

    await cog.play.callback(
        cog,
        ctx,
        query="test",
    )

    ctx.send.assert_awaited_once()


async def test_play_no_song_found():
    bot = MagicMock()
    cog = Play(bot)

    player = MagicMock()
    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    with patch(
        "src.bot.commands.music.play.wavelink.Playable.search",
        new=AsyncMock(return_value=[]),
    ):
        await cog.play.callback(
            cog,
            ctx,
            query="test",
        )

    ctx.send.assert_awaited_once()


async def test_play_adds_track_to_queue():
    bot = MagicMock()
    cog = Play(bot)

    player = MagicMock()
    player.playing = True
    player.queue.put_wait = AsyncMock()

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    track = MagicMock()
    track.uri = "https://example.com/song"

    with patch(
        "src.bot.commands.music.play.wavelink.Playable.search",
        new=AsyncMock(return_value=[track]),
    ), patch(
        "src.bot.commands.music.play.asyncio.to_thread",
        new=AsyncMock(return_value="Test Song"),
    ):
        await cog.play.callback(
            cog,
            ctx,
            query="test",
        )

    player.queue.put_wait.assert_awaited_once_with(track)
    ctx.send.assert_awaited_once()


async def test_play_starts_track():
    bot = MagicMock()
    cog = Play(bot)

    player = MagicMock()
    player.playing = False
    player.queue.put_wait = AsyncMock()
    player.play = AsyncMock()

    track = MagicMock()
    track.uri = "https://example.com/song"

    player.queue.get.return_value = track

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    with patch(
        "src.bot.commands.music.play.wavelink.Playable.search",
        new=AsyncMock(return_value=[track]),
    ), patch(
        "src.bot.commands.music.play.asyncio.to_thread",
        new=AsyncMock(return_value="Test Song"),
    ):
        await cog.play.callback(
            cog,
            ctx,
            query="test",
        )

    player.queue.put_wait.assert_awaited_once_with(track)
    player.queue.get.assert_called_once()
    player.play.assert_awaited_once_with(track)
    ctx.send.assert_awaited_once()


async def test_play_playlist():
    class FakePlaylist:
        def __init__(self, tracks, name):
            self.tracks = tracks
            self.name = name

    bot = MagicMock()
    cog = Play(bot)

    player = MagicMock()
    player.playing = False
    player.queue.put_wait = AsyncMock()
    player.play = AsyncMock()

    first_track = MagicMock()
    second_track = MagicMock()

    player.queue.get.return_value = first_track

    playlist = FakePlaylist(
        tracks=[
            first_track,
            second_track,
        ],
        name="Test Playlist",
    )

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    with patch(
        "src.bot.commands.music.play.wavelink.Playable.search",
        new=AsyncMock(return_value=playlist),
    ), patch(
        "src.bot.commands.music.play.wavelink.Playlist",
        FakePlaylist,
    ):
        await cog.play.callback(
            cog,
            ctx,
            query="test",
        )

    assert player.queue.put_wait.await_count == 2

    player.queue.put_wait.assert_any_await(first_track)
    player.queue.put_wait.assert_any_await(second_track)

    player.queue.get.assert_called_once()
    player.play.assert_awaited_once_with(first_track)

    ctx.send.assert_awaited_once()


async def test_play_playlist_while_playing():
    class FakePlaylist:
        def __init__(self, tracks, name):
            self.tracks = tracks
            self.name = name

    bot = MagicMock()
    cog = Play(bot)

    player = MagicMock()
    player.playing = True
    player.queue.put_wait = AsyncMock()
    player.play = AsyncMock()

    first_track = MagicMock()
    second_track = MagicMock()

    playlist = FakePlaylist(
        tracks=[
            first_track,
            second_track,
        ],
        name="Test Playlist",
    )

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    with patch(
        "src.bot.commands.music.play.wavelink.Playable.search",
        new=AsyncMock(return_value=playlist),
    ), patch(
        "src.bot.commands.music.play.wavelink.Playlist",
        FakePlaylist,
    ):
        await cog.play.callback(
            cog,
            ctx,
            query="test",
        )

    assert player.queue.put_wait.await_count == 2

    player.queue.put_wait.assert_any_await(first_track)
    player.queue.put_wait.assert_any_await(second_track)

    player.play.assert_not_awaited()
    ctx.send.assert_awaited_once()


async def test_play_playlist_query_with_normal_tracks():
    bot = MagicMock()
    cog = Play(bot)

    player = MagicMock()
    player.playing = False
    player.queue.put_wait = AsyncMock()
    player.play = AsyncMock()

    track = MagicMock()
    track.title = "Test Song"

    player.queue.get.return_value = track

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    with patch(
        "src.bot.commands.music.play.wavelink.Playable.search",
        new=AsyncMock(return_value=[track]),
    ):
        await cog.play.callback(
            cog,
            ctx,
            query="https://youtube.com/watch?v=test&list=test",
        )

    player.queue.put_wait.assert_awaited_once_with(track)
    player.queue.get.assert_called_once()
    player.play.assert_awaited_once_with(track)

    ctx.send.assert_awaited_once()


async def test_get_original_title():
    from src.bot.commands.music.play import get_original_title

    with patch(
        "src.bot.commands.music.play.yt_dlp.YoutubeDL"
    ) as youtube_dl:
        ydl = youtube_dl.return_value

        ydl.extract_info.return_value = {
            "title": "Test Song",
        }

        result = get_original_title(
            "https://example.com/song"
        )

    assert result == "Test Song"


async def test_get_original_title_without_title():
    from src.bot.commands.music.play import get_original_title

    with patch(
        "src.bot.commands.music.play.yt_dlp.YoutubeDL"
    ) as youtube_dl:
        ydl = youtube_dl.return_value

        ydl.extract_info.return_value = {}

        result = get_original_title(
            "https://example.com/song"
        )

    assert result == "Título desconocido"


async def test_play_connects_to_author_voice_channel():
    bot = MagicMock()
    cog = Play(bot)

    player = MagicMock()
    player.playing = True
    player.queue.put_wait = AsyncMock()

    voice_channel = MagicMock()
    voice_channel.connect = AsyncMock(
        return_value=player
    )

    author = MagicMock()
    author.voice = MagicMock()
    author.voice.channel = voice_channel

    ctx = MagicMock()
    ctx.voice_client = None
    ctx.author = author
    ctx.send = AsyncMock()

    track = MagicMock()
    track.uri = "https://example.com/song"

    with patch(
        "src.bot.commands.music.play.wavelink.Playable.search",
        new=AsyncMock(return_value=[track]),
    ), patch(
        "src.bot.commands.music.play.asyncio.to_thread",
        new=AsyncMock(return_value="Test Song"),
    ):
        await cog.play.callback(
            cog,
            ctx,
            query="test",
        )

    voice_channel.connect.assert_awaited_once_with(
        cls=wavelink.Player
    )

    player.queue.put_wait.assert_awaited_once_with(track)
    ctx.send.assert_awaited_once()