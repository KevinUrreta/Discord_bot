import wavelink
import yt_dlp

from src.infrastructure.database.repositories.guild import GuildRepository


def get_original_info(url):
    """
    Obtiene la información multimedia desde una URL

    :param url: URL del recurso del que se quiere obtener información.
    :return: Diccionario con el título y visualizaciones.
    """
    ydl = yt_dlp.YoutubeDL(
        {"quiet": True, "no_warnings": True, }
    )

    info = ydl.extract_info(url, download=False)

    return {
        "title": info.get("title", "Título desconocido"),
        "views": info.get("view_count", 0),
    }


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


async def restore_volume(player: wavelink.Player, guild_repository: GuildRepository) -> None:
    """
    Restaura el volumen almacenado para el servidor del reproductor.

    :param player: Reproductor de Wavelink cuyo volumen se desea restaurar.
    :param guild_repository: Server para consultar la configuración de volumen del server.
    :return:
    """
    guild = player.guild

    if guild is None:
        return

    guild_data = await guild_repository.get(guild.id)

    if guild_data is None:
        return

    volume = guild_data.volume

    await player.set_volume(volume)
