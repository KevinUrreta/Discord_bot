from unittest.mock import AsyncMock, MagicMock

import pytest

from src.bot.commands.moderation.clear import Cls


@pytest.mark.asyncio
async def test_clear_command():
    bot = MagicMock()

    ctx = MagicMock()
    ctx.channel.purge = AsyncMock()

    cog = Cls(bot)

    await cog.cls.callback(
        cog,
        ctx,
        limit=5,
    )

    ctx.channel.purge.assert_awaited_once_with(
        limit=6,
    )
