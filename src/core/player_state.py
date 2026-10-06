from dataclasses import dataclass
from weakref import WeakKeyDictionary

import discord
import wavelink


@dataclass
class MusicState:
    text_channel: discord.TextChannel | None = None
    requester: str | None = None
    footer_icon: str | None = None
    show_now_playing: bool = False


_states: WeakKeyDictionary[wavelink.Player, MusicState] = (
    WeakKeyDictionary()
)


def get_music_state(player: wavelink.Player) -> MusicState:
    """
    Obtiene el estado de música asociado a un reproductor.

    :param player: Reproductor de Wavelink cuyo estado se desea obtener.
    :return: Estado de música asociado al reproductor.
    """
    state = _states.get(player)

    if state is None:
        state = MusicState()
        _states[player] = state

    return state
