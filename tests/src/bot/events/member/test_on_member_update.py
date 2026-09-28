from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.bot.events.member.on_member_update import On_member_update


@pytest.mark.asyncio
async def test_on_member_update_without_changes_does_nothing():
    bot = MagicMock()
    bot.database = MagicMock()

    before = MagicMock()
    after = MagicMock()

    before.name = "Kevin"
    after.name = "Kevin"

    before.display_name = "Kevin"
    after.display_name = "Kevin"

    with patch(
        "src.bot.events.member.on_member_update.MemberRepository"
    ) as repository_class:

        repository = repository_class.return_value
        repository.update = AsyncMock()

        cog = On_member_update(bot)

        await cog.on_member_update(before, after)

        repository.update.assert_not_awaited()


@pytest.mark.asyncio
async def test_on_member_update_updates_changed_name():
    bot = MagicMock()
    bot.database = MagicMock()

    before = MagicMock()
    after = MagicMock()

    before.name = "Kevin"
    after.name = "Kevin2"

    before.display_name = "Kevin"
    after.display_name = "Kevin"

    after.id = 123
    after.guild.id = 456

    with patch(
        "src.bot.events.member.on_member_update.MemberRepository"
    ) as repository_class:

        repository = repository_class.return_value
        repository.update = AsyncMock()

        cog = On_member_update(bot)

        await cog.on_member_update(before, after)

        repository.update.assert_awaited_once_with(
            member_id=123,
            guild_id=456,
            name="Kevin2",
        )


@pytest.mark.asyncio
async def test_on_member_update_updates_changed_display_name():
    bot = MagicMock()
    bot.database = MagicMock()

    before = MagicMock()
    after = MagicMock()

    before.name = "Kevin"
    after.name = "Kevin"

    before.display_name = "Kevin"
    after.display_name = "Kevin Nuevo"

    after.id = 123
    after.guild.id = 456

    with patch(
        "src.bot.events.member.on_member_update.MemberRepository"
    ) as repository_class:

        repository = repository_class.return_value
        repository.update = AsyncMock()

        cog = On_member_update(bot)

        await cog.on_member_update(before, after)

        repository.update.assert_awaited_once_with(
            member_id=123,
            guild_id=456,
            display_name="Kevin Nuevo",
        )