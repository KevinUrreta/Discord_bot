from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.app.commands.music.skip import Skip


@pytest.mark.asyncio
async def test_skip_without_current_track():
    bot = MagicMock()
    cog = Skip(bot)

    player = MagicMock()
    player.current = None

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    with patch(
            "src.app.commands.music.skip.create_embed",
        return_value="embed",
    ):

        await cog.skip.callback(
            cog,
            ctx,
        )

    ctx.send.assert_awaited_once()


@pytest.mark.asyncio
async def test_skip_current_track():
    bot = MagicMock()
    cog = Skip(bot)

    player = MagicMock()
    player.current = MagicMock()
    player.skip = AsyncMock()

    ctx = MagicMock()
    ctx.voice_client = player
    ctx.send = AsyncMock()

    await cog.skip.callback(
        cog,
        ctx,
    )

    player.skip.assert_awaited_once()
