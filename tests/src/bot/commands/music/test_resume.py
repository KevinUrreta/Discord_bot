from unittest.mock import AsyncMock, MagicMock

from src.bot.commands.music.resume import Resume


async def test_resume_not_connected():
    bot = MagicMock()
    cog = Resume(bot)

    ctx = MagicMock()
    ctx.voice_client = None
    ctx.send = AsyncMock()

    await cog.resume.callback(cog, ctx)

    ctx.send.assert_awaited_once()


async def test_resume_not_paused():
    bot = MagicMock()
    cog = Resume(bot)

    player = MagicMock()
    player.paused = False
    player.pause = AsyncMock()

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.resume.callback(cog, ctx)

    ctx.send.assert_awaited_once()
    player.pause.assert_not_awaited()


async def test_resume_song():
    bot = MagicMock()
    cog = Resume(bot)

    player = MagicMock()
    player.paused = True
    player.pause = AsyncMock()

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.resume.callback(cog, ctx)

    player.pause.assert_awaited_once_with(False)
    ctx.send.assert_awaited_once()
