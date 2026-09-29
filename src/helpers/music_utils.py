import yt_dlp


def get_original_info(url):
    ydl = yt_dlp.YoutubeDL(
        {
            "quiet": True,
            "no_warnings": True,
        }
    )

    info = ydl.extract_info(url, download=False)

    return {
        "title": info.get("title", "Título desconocido"),
        "views": info.get("view_count", 0),
    }


def format_duration(milliseconds):
    total_seconds = int(milliseconds / 1000)
    minutes, seconds = divmod(total_seconds, 60)

    return f"{minutes}:{seconds:02d}"


def get_thumbnail(track):
    if track.artwork:
        return track.artwork

    if track.identifier:
        return (
            f"https://img.youtube.com/vi/"
            f"{track.identifier}/hqdefault.jpg"
        )

    return None