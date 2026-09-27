from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_join import On_guild_join


@pytest.mark.asyncio
async def test_on_guild_join_creates_guild_and_members():
    bot = MagicMock()
    bot.database = MagicMock()

    guild = MagicMock()
    guild.id = 123
    guild.name = "Test Guild"

    member = MagicMock()
    member.id = 456
    member.name = "Kevin"
    member.display_name = "Kevin"
    member.joined_at = None

    guild.members = [member]

    with patch(
        "src.bot.events.guild.on_guild_join.GuildRepository"
    ) as guild_repository_class, patch(
        "src.bot.events.guild.on_guild_join.MemberRepository"
    ) as member_repository_class:

        guild_repository = guild_repository_class.return_value
        member_repository = member_repository_class.return_value

        guild_repository.create = AsyncMock()
        member_repository.create = AsyncMock()

        cog = On_guild_join(bot)

        await cog.on_guild_join(guild)

        guild_repository.create.assert_awaited_once_with(
            guild_id=123,
            name="Test Guild",
        )

        member_repository.create.assert_awaited_once_with(
            member_id=456,
            guild_id=123,
            name="Kevin",
            display_name="Kevin",
            joined_at=None,
        )
