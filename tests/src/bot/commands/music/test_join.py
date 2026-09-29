from unittest.mock import AsyncMock, MagicMock

from src.bot.commands.music.join import Join


async def test_join_move_existing_voice_client():
    bot = MagicMock()
    cog = Join(bot)

    channel = MagicMock()
    channel.name = "General"

    voice_state = MagicMock()
    voice_state.channel = channel

    voice_client = MagicMock()
    voice_client.move_to = AsyncMock()

    ctx = MagicMock()
    ctx.author.voice = voice_state
    ctx.voice_client = voice_client

    await cog.join.callback(
        cog,
        ctx,
    )

    voice_client.move_to.assert_awaited_once_with(channel)


async def test_join_connects_when_not_connected():
    bot = MagicMock()
    cog = Join(bot)

    channel = MagicMock()
    channel.name = "General"
    channel.connect = AsyncMock()

    voice_state = MagicMock()
    voice_state.channel = channel

    ctx = MagicMock()
    ctx.author.voice = voice_state
    ctx.voice_client = None

    await cog.join.callback(
        cog,
        ctx,
    )

    channel.connect.assert_awaited_once()