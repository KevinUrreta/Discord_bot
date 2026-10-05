import yt_dlp


def get_original_info(url):
    """
    Obtiene la información multimedia desde una URL

    :param url: URL del recurso del que se quiere obtener informacion.
    :return: Diccionario con el título y visualizaciones.
    """
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
    """
    Convierte una duración expresada en milisegundos a minutos y segundos.

    :param milliseconds: Duración del recurso en milisegundos
    :return: Duración formateada como minutos y segundos
    """
    total_seconds = int(milliseconds / 1000)
    minutes, seconds = divmod(total_seconds, 60)

    return f"{minutes}:{seconds:02d}"


def get_thumbnail(track):
    """
    Obtiene el thumbnail de un track.

    :param track: Track que se quiere obtener.
    :return: URL o None del thumbnail.
    """
    if track.artwork:
        return track.artwork

    if track.identifier:
        return (
            f"https://img.youtube.com/vi/"
            f"{track.identifier}/hqdefault.jpg"
        )

    return None