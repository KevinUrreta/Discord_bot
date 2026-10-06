import json
from pathlib import Path
from src.core.config import settings


LOCALES_PATH = Path(__file__).parent / "locales"

GUILD_LANGUAGES = {}

SUPPORTED_LANGUAGES = {
    "de": "Deutsch",
    "en": "English",
    "es": "Español",
    "fr": "Français",
    "ja": "日本語",
    "pt": "Português",
    "ru": "Русский",
    "zh": "中文",
}

LOCALE_FILES = {
    "de": "de_DE.json",
    "en": "en_US.json",
    "es": "es_ES.json",
    "fr": "fr_FR.json",
    "ja": "ja_JP.json",
    "pt": "pt_BR.json",
    "ru": "ru_RU.json",
    "zh": "zh_CN.json",
}


def set_guild_languages(guild_languages: dict) -> None:
    """
    Actualiza los idiomas configurados para los servidores.

    :param guild_languages: Diccionario con los idiomas de cada server.
    :return: None
    """
    global GUILD_LANGUAGES
    GUILD_LANGUAGES = guild_languages


def get_language(guild) -> str:
    """
    Obtiene el idioma configurado de un server.

    :param guild: Server del que se quiere obtener idioma.
    :return: Código del idioma.
    """
    if guild is None:
        return settings.log_language

    return GUILD_LANGUAGES.get(guild.id, "en")


def get_locale(guild) -> str:
    """
    Obtiene el ``.json`` correspondiente de un server.

    :param guild: Server del que se quiere obtener ``json``.
    :return: Nombre del ``json``.
    """
    language = get_language(guild)

    return LOCALE_FILES.get(language, "en_US.json")


def get_translations(guild) -> dict:
    """
    Carga las traducciones correspondientes a un servidor.

    :param guild: Server del que se quiere obtener traducción.
    :return: Diccionario de traducciones.
    """
    locale = get_locale(guild)

    with open(LOCALES_PATH / locale, "r", encoding="utf-8") as file:
        return json.load(file)


def get_nested_translation(translations: dict, key: str):
    """
    Obtiene una traducción utilizando una clave jerárquica.
    Las claves se separan mediante puntos para poder acceder a
    diferentes niveles dentro del diccionario de traducciones.
    Por ejemplo, la clave::
        app.commands.music.embeds.volume.invalid_volume

    :param translations: Diccionario de traducciones.
    :param key: Clave jerárquica de traducción.
    :return: Traducción encontrada o vacía.
    """
    for part in key.split("."):
        translations = translations.get(part, {})

    return translations


def translate(guild, key: str, **kwargs) -> str:
    """
    Obtiene y devuelve una traducción.

    :param guild: Server asociado a la traducción
    :param key: Clave jerárquica de traducción
    :param kwargs:
    :return: Texto traducido.
    """
    translations = get_translations(guild)

    message = get_nested_translation(translations, key)

    if not isinstance(message, str):
        return key

    kwargs.setdefault("guild", guild)

    return message.format(**kwargs)