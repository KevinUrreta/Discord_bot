from unittest.mock import MagicMock, patch

import discord

from src.helpers.embeds import create_embed


def test_create_embed_returns_embed():
    guild = MagicMock()

    with patch(
        "src.helpers.embeds.translate",
        return_value="Mensaje",
        create=True,
    ):

        result = create_embed(
            guild,
            "test.key",
        )

    assert isinstance(
        result,
        discord.Embed,
    )
