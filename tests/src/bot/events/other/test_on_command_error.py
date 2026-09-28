from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from discord.ext import commands

from src.bot.events.other.on_command_error import On_command_error


@pytest.mark.asyncio
async def test_on_command_error_missing_permissions():
    bot = MagicMock()
    ctx = MagicMock()
    ctx.guild = MagicMock()
    ctx.send = AsyncMock()

    error = commands.MissingPermissions(
        ["manage_messages"]
    )

    cog = On_command_error(bot)

    with patch(
        "src.bot.events.other.on_command_error.translate",
        return_value="missing",
    ) as translate:

        await cog.on_command_error(ctx, error)

        ctx.send.assert_awaited_once_with("missing")
        translate.assert_called_once()

        assert translate.call_args.args[0] is ctx.guild


@pytest.mark.asyncio
async def test_on_command_error_generic_error():
    bot = MagicMock()
    ctx = MagicMock()
    ctx.guild = MagicMock()
    ctx.send = AsyncMock()

    error = ValueError("boom")

    cog = On_command_error(bot)

    with patch(
        "src.bot.events.other.on_command_error.translate",
        return_value="error",
    ) as translate:

        await cog.on_command_error(ctx, error)

        ctx.send.assert_awaited_once_with("error")
        translate.assert_called_once()

        assert translate.call_args.args[0] is ctx.guild
