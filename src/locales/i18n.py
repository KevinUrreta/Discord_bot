import json
import os
from pathlib import Path


LOCALES_PATH = Path(__file__).parent.parent / "locales"

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

LOG_LANGUAGE = os.getenv(
    "LOG_LANGUAGE",
    "es",
)

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
    global GUILD_LANGUAGES
    GUILD_LANGUAGES = guild_languages


def get_language(guild) -> str:
    if guild is None:
        return LOG_LANGUAGE

    return GUILD_LANGUAGES.get(guild.id, "en")


def get_locale(guild) -> str:
    language = get_language(guild)

    return LOCALE_FILES.get(language, "en_US.json")


def get_translations(guild) -> dict:
    locale = get_locale(guild)

    with open(LOCALES_PATH / locale, "r", encoding="utf-8") as file:
        return json.load(file)


def get_nested_translation(translations: dict, key: str):
    for part in key.split("."):
        translations = translations.get(part, {})

    return translations


def translate(guild, key: str, **kwargs) -> str:
    translations = get_translations(guild)

    message = get_nested_translation(translations, key)

    if not isinstance(message, str):
        return key

    kwargs.setdefault("guild", guild)

    return message.format(**kwargs)