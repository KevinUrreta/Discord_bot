from unittest.mock import MagicMock, patch

import pytest

from src.bot.events.member.on_user_update import On_user_update


@pytest.mark.asyncio
async def test_on_user_update_without_changes_does_nothing():
    bot = MagicMock()

    before = MagicMock()
    after = MagicMock()

    before.name = "Kevin"
    after.name = "Kevin"

    before.global_name = "Kevin"
    after.global_name = "Kevin"

    before.avatar = None
    after.avatar = None

    cog = On_user_update(bot)

    with patch(
        "src.bot.events.member.on_user_update.logger"
    ) as logger:

        await cog.on_user_update(before, after)

        logger.info.assert_not_called()
