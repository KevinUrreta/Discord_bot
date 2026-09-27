from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.bot.events.guild.on_guild_remove import On_guild_remove


@pytest.mark.asyncio
async def test_on_guild_remove_deletes_members_and_guild():
    bot = MagicMock()
    bot.database = MagicMock()

    guild = MagicMock()
    guild.id = 123
    guild.name = "Test Guild"

    with patch(
        "src.bot.events.guild.on_guild_remove.GuildRepository"
    ) as guild_repository_class, patch(
        "src.bot.events.guild.on_guild_remove.MemberRepository"
    ) as member_repository_class:

        guild_repository = guild_repository_class.return_value
        member_repository = member_repository_class.return_value

        member_repository.delete_by_guild = AsyncMock(
            return_value=3
        )
        guild_repository.delete = AsyncMock(
            return_value=True
        )

        cog = On_guild_remove(bot)

        await cog.on_guild_remove(guild)

        member_repository.delete_by_guild.assert_awaited_once_with(123)
        guild_repository.delete.assert_awaited_once_with(123)


@pytest.mark.asyncio
async def test_on_guild_remove_handles_missing_guild():
    bot = MagicMock()
    bot.database = MagicMock()

    guild = MagicMock()
    guild.id = 123
    guild.name = "Test Guild"

    with patch(
        "src.bot.events.guild.on_guild_remove.GuildRepository"
    ) as guild_repository_class, patch(
        "src.bot.events.guild.on_guild_remove.MemberRepository"
    ) as member_repository_class:

        guild_repository = guild_repository_class.return_value
        member_repository = member_repository_class.return_value

        member_repository.delete_by_guild = AsyncMock(
            return_value=0
        )
        guild_repository.delete = AsyncMock(
            return_value=False
        )

        cog = On_guild_remove(bot)

        await cog.on_guild_remove(guild)

        member_repository.delete_by_guild.assert_awaited_once_with(123)
        guild_repository.delete.assert_awaited_once_with(123)
