from unittest.mock import AsyncMock, MagicMock, patch

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

    ctx = MagicMock()
    ctx.voice_client = MagicMock()
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
