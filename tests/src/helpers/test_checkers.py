from unittest.mock import MagicMock

import discord
import pytest

from src.helpers.checkers import has_manage_guild


def get_predicate():
    @has_manage_guild()
    async def dummy(ctx):
        pass

    return dummy.__commands_checks__[0]


@pytest.mark.asyncio
async def test_has_manage_guild_without_guild():
    ctx = MagicMock()
    ctx.guild = None

    predicate = get_predicate()

    assert await predicate(ctx) is False


@pytest.mark.asyncio
async def test_has_manage_guild_non_member():
    ctx = MagicMock()
    ctx.guild = MagicMock()
    ctx.author = MagicMock()

    predicate = get_predicate()

    assert await predicate(ctx) is False


@pytest.mark.asyncio
async def test_has_manage_guild_without_permission():
    ctx = MagicMock()
    ctx.guild = MagicMock()

    member = MagicMock(spec=discord.Member)
    member.guild_permissions.manage_guild = False

    ctx.author = member

    predicate = get_predicate()

    assert await predicate(ctx) is False


@pytest.mark.asyncio
async def test_has_manage_guild_with_permission():
    ctx = MagicMock()
    ctx.guild = MagicMock()

    member = MagicMock(spec=discord.Member)
    member.guild_permissions.manage_guild = True

    ctx.author = member

    predicate = get_predicate()

    assert await predicate(ctx) is True
