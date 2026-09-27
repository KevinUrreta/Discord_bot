from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.bot.events.member.on_member_join import On_member_join


@pytest.mark.asyncio
async def test_on_member_join_creates_member():
    bot = MagicMock()
    bot.database = MagicMock()

    member = MagicMock()
    member.id = 123
    member.guild.id = 456
    member.name = "Kevin"
    member.display_name = "Kevin"
    member.joined_at = None

    with patch(
        "src.bot.events.member.on_member_join.MemberRepository"
    ) as repository_class:

        repository = repository_class.return_value
        repository.create = AsyncMock()

        cog = On_member_join(bot)

        await cog.on_member_join(member)

        repository.create.assert_awaited_once_with(
            member_id=123,
            guild_id=456,
            name="Kevin",
            display_name="Kevin",
            joined_at=None,
        )
