import json
import os
from pathlib import Path


LOCALES_PATH = Path(__file__).parent.parent / "locales"

GUILD_LANGUAGES = {}

SUPPORTED_LANGUAGES = {
    "es": "Español",
    "en": "English",
    "fr": "Français",
    "de": "Deutsch",
    "it": "Italiano",
    "pt": "Português",
    "nl": "Nederlands",
    "pl": "Polski",
    "ja": "日本語",
}

LOG_LANGUAGE = os.getenv(
    "LOG_LANGUAGE",
    "es",
)

LOCALE_FILES = {
    "es": "es_ES.json",
    "en": "en_US.json",
    "fr": "fr_FR.json",
    "de": "de_DE.json",
    "it": "it_IT.json",
    "pt": "pt_PT.json",
    "nl": "nl_NL.json",
    "pl": "pl_PL.json",
    "ja": "ja_JP.json",
}


def set_guild_languages(
    guild_languages: dict,
) -> None:
    global GUILD_LANGUAGES

    GUILD_LANGUAGES = guild_languages


def get_language(guild) -> str:
    if guild is None:
        return LOG_LANGUAGE

    return GUILD_LANGUAGES.get(
        guild.id,
        "es",
    )


def get_locale(guild) -> str:
    language = get_language(guild)

    return LOCALE_FILES.get(
        language,
        "es_ES.json",
    )


def get_translations(guild) -> dict:
    locale = get_locale(guild)

    with open(
        LOCALES_PATH / locale,
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


def get_nested_translation(
    translations: dict,
    key: str,
):
    for part in key.split("."):
        translations = translations.get(
            part,
            {},
        )

    return translations


def translate(
    guild,
    key: str,
    **kwargs,
) -> str:
    translations = get_translations(guild)

    message = get_nested_translation(
        translations,
        key,
    )

    if not isinstance(message, str):
        return key

    kwargs.setdefault(
        "guild",
        guild,
    )

    return message.format(**kwargs)