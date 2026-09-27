from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.bot.events.member.on_member_remove import On_member_remove


@pytest.mark.asyncio
async def test_on_member_remove_deletes_member():
    bot = MagicMock()
    bot.database = MagicMock()

    member = MagicMock()
    member.id = 123
    member.guild.id = 456
    member.name = "Kevin"

    with patch(
        "src.bot.events.member.on_member_remove.MemberRepository"
    ) as repository_class:

        repository = repository_class.return_value
        repository.delete = AsyncMock(return_value=True)

        cog = On_member_remove(bot)

        await cog.on_member_remove(member)

        repository.delete.assert_awaited_once_with(
            member_id=123,
            guild_id=456,
        )
