from unittest.mock import AsyncMock, MagicMock

from src.bot.commands.music.leave import Leave


async def test_leave_not_connected():
    bot = MagicMock()
    cog = Leave(bot)

    ctx = MagicMock()
    ctx.voice_client = None
    ctx.send = AsyncMock()

    await cog.leave.callback(cog, ctx)

    ctx.send.assert_awaited_once()


async def test_leave_disconnects():
    bot = MagicMock()
    cog = Leave(bot)

    voice_client = MagicMock()
    voice_client.disconnect = AsyncMock()

    ctx = MagicMock()
    ctx.voice_client = voice_client
    ctx.send = AsyncMock()

    await cog.leave.callback(cog, ctx)

    voice_client.disconnect.assert_awaited_once()
    ctx.send.assert_awaited_once()
