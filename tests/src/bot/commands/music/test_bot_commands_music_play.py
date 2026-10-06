from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.app.commands.music.play import Play


TEST_GUILD_ID = 123
TEST_DISPLAY_NAME = "Nombre"


def create_cog():
    return Play(MagicMock())


def create_ctx():
    ctx = MagicMock()

    ctx.guild = MagicMock()
    ctx.guild.id = TEST_GUILD_ID

    ctx.author = MagicMock()
    ctx.author.display_name = TEST_DISPLAY_NAME

    ctx.author.voice = None

    ctx.voice_client = None

    ctx.send = AsyncMock()

    return ctx


@pytest.mark.asyncio
async def test_play_requires_voice_channel():
    cog = create_cog()
    ctx = create_ctx()

    with patch(
            "src.app.commands.music.play.create_embed",
        return_value="embed",
    ) as create_embed:

        await cog.play.callback(
            cog,
            ctx,
            query="test",
        )

    create_embed.assert_called_once()
    ctx.send.assert_awaited_once_with(
        embed="embed",
    )


@pytest.mark.asyncio
async def test_play_sends_no_song_found():
    cog = create_cog()
    ctx = create_ctx()

    ctx.author.voice = MagicMock()
    ctx.author.voice.channel = MagicMock()
    player = MagicMock()
    ctx.author.voice.channel.connect = AsyncMock(return_value=player)

    with patch(
            "src.app.commands.music.play.wavelink.Playable.search",
        new=AsyncMock(return_value=[]),
    ), patch(
        "src.app.commands.music.play.create_embed",
        return_value="embed",
    ) as create_embed:

        await cog.play.callback(
            cog,
            ctx,
            query="test",
        )

    create_embed.assert_called_once()
    ctx.send.assert_awaited_once_with(
        embed="embed",
    )
