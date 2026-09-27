from unittest.mock import AsyncMock, MagicMock

from src.bot.commands.music.volume import Volume


async def test_volume_not_connected():
    bot = MagicMock()
    bot.database = MagicMock()

    cog = Volume(bot)

    ctx = MagicMock()
    ctx.voice_client = None
    ctx.send = AsyncMock()

    await cog.volume.callback(cog, ctx, 50)

    ctx.send.assert_awaited_once()


async def test_volume_invalid_low():
    bot = MagicMock()
    bot.database = MagicMock()

    cog = Volume(bot)

    ctx = MagicMock()
    ctx.voice_client = MagicMock()
    ctx.voice_client.set_volume = AsyncMock()
    ctx.send = AsyncMock()

    await cog.volume.callback(cog, ctx, -1)

    ctx.send.assert_awaited_once()
    ctx.voice_client.set_volume.assert_not_awaited()


async def test_volume_invalid_high():
    bot = MagicMock()
    bot.database = MagicMock()

    cog = Volume(bot)

    ctx = MagicMock()
    ctx.voice_client = MagicMock()
    ctx.voice_client.set_volume = AsyncMock()
    ctx.send = AsyncMock()

    await cog.volume.callback(cog, ctx, 101)

    ctx.send.assert_awaited_once()
    ctx.voice_client.set_volume.assert_not_awaited()


async def test_volume_changes_volume():
    bot = MagicMock()
    bot.database = MagicMock()

    cog = Volume(bot)

    cog.guild_repository.update = AsyncMock(
        return_value=MagicMock(
            id=123456789,
            volume=75,
        )
    )

    player = MagicMock()
    player.set_volume = AsyncMock()

    ctx = MagicMock()
    ctx.guild.id = 123456789
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.volume.callback(cog, ctx, 75)

    player.set_volume.assert_awaited_once_with(75)

    cog.guild_repository.update.assert_awaited_once_with(
        guild_id=123456789,
        volume=75,
    )

    ctx.send.assert_awaited_once()
