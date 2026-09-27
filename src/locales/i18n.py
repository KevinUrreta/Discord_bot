import json
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

def set_guild_languages(
    guild_languages: dict,
) -> None:
    global GUILD_LANGUAGES

    GUILD_LANGUAGES = guild_languages


def get_locale(guild) -> str:
    if guild is None:
        return "es_ES"

    language = GUILD_LANGUAGES.get(
        guild.id,
        "es",
    )

    if language == "es":
        return "es_ES"

    if language == "en":
        return "en_US"

    if language == "fr":
        return "fr_FR"

    if language == "de":
        return "de_DE"

    if language == "it":
        return "it_IT"

    if language == "pt":
        return "pt_PT"

    if language == "nl":
        return "nl_NL"

    if language == "pl":
        return "pl_PL"

    if language == "ja":
        return "ja_JP"

    return "es_ES"


def get_translations(guild) -> dict:
    locale = get_locale(guild)

    with open(
        LOCALES_PATH / f"{locale}.json",
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

    return message.format(**kwargs)