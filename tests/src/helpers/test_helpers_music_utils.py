from unittest.mock import MagicMock, patch

from src.helpers.music_utils import (
    format_duration,
    get_original_info,
    get_thumbnail,
)


def test_format_duration_zero():
    assert format_duration(0) == "0:00"


def test_format_duration_seconds():
    assert format_duration(5000) == "0:05"


def test_format_duration_minutes():
    assert format_duration(60000) == "1:00"


def test_format_duration_minutes_and_seconds():
    assert format_duration(125000) == "2:05"


def test_get_thumbnail_uses_artwork():
    track = MagicMock()
    track.artwork = "https://example.com/art.jpg"
    track.identifier = "abc"

    assert (
        get_thumbnail(track)
        == "https://example.com/art.jpg"
    )


def test_get_thumbnail_uses_youtube_identifier():
    track = MagicMock()
    track.artwork = None
    track.identifier = "abc123"

    assert (
        get_thumbnail(track)
        == "https://img.youtube.com/vi/"
        "abc123/hqdefault.jpg"
    )


def test_get_thumbnail_returns_none_without_data():
    track = MagicMock()
    track.artwork = None
    track.identifier = None

    assert get_thumbnail(track) is None


def test_get_original_info():
    info = {
        "title": "Canción",
        "view_count": 123,
    }

    fake_ydl = MagicMock()

    fake_ydl.extract_info.return_value = info

    with patch(
        "src.helpers.music_utils.yt_dlp.YoutubeDL",
        return_value=fake_ydl,
    ):

        result = get_original_info(
            "https://youtube.com/watch?v=test",
        )

    assert result == {
        "title": "Canción",
        "views": 123,
    }
