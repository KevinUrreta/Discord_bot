from unittest.mock import AsyncMock, MagicMock, patch

import pytest
import wavelink

from src.bot.events.other.on_ready import On_ready


@pytest.mark.asyncio
async def test_on_ready_connects_lavalink_when_no_nodes():
    bot = MagicMock()
    password = "secret"

    cog = On_ready(bot, password)

    with patch.object(
        wavelink.Pool,
        "nodes",
        {},
        create=True,
    ), patch.object(
        wavelink.Pool,
        "connect",
        new_callable=AsyncMock,
    ) as connect, patch(
        "src.bot.events.other.on_ready.wavelink.Node"
    ) as node:

        await cog.on_ready()

        node.assert_called_once_with(
            identifier="main",
            uri="http://lavalink:2333",
            password=password,
        )

        connect.assert_awaited_once()


@pytest.mark.asyncio
async def test_on_ready_does_not_connect_when_node_exists():
    bot = MagicMock()
    password = "secret"

    cog = On_ready(bot, password)

    with patch.object(
        wavelink.Pool,
        "nodes",
        {"main": MagicMock()},
        create=True,
    ), patch.object(
        wavelink.Pool,
        "connect",
        new_callable=AsyncMock,
    ) as connect:

        await cog.on_ready()

        connect.assert_not_awaited()
