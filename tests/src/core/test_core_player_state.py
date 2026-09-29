from unittest.mock import MagicMock

from src.core.player_state import (
    MusicState,
    get_music_state,
)


def test_music_state_default_values():
    state = MusicState()

    assert state.text_channel is None
    assert state.requester is None
    assert state.footer_icon is None
    assert state.show_now_playing is False


def test_get_music_state_creates_state():
    player = MagicMock()

    state = get_music_state(player)

    assert isinstance(
        state,
        MusicState,
    )


def test_get_music_state_returns_same_state():
    player = MagicMock()

    first = get_music_state(player)
    second = get_music_state(player)

    assert first is second
