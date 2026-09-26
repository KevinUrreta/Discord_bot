import json
from pathlib import Path


LOCALES_PATH = Path(__file__).parent.parent / "locales"


def get_locale(guild) -> str:
    if guild is None:
        return "en_US"

    locale = str(guild.preferred_locale)

    if locale.startswith("es"):
        return "es_ES"

    if locale.startswith("en"):
        return "en_US"

    if locale.startswith("fr"):
        return "fr_FR"

    if locale.startswith("de"):
        return "de_DE"

    if locale.startswith("it"):
        return "it_IT"

    if locale.startswith("pt"):
        return "pt_PT"

    if locale.startswith("nl"):
        return "nl_NL"

    if locale.startswith("pl"):
        return "pl_PL"

    if locale.startswith("ja"):
        return "ja_JP"

    return "en_US"


def get_translations(guild) -> dict:
    locale = get_locale(guild)

    with open(
        LOCALES_PATH / f"{locale}.json",
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


def get_nested_translation(translations: dict, key: str):
    for part in key.split("."):
        translations = translations.get(part, {})

    return translations


def translate(guild, key: str, **kwargs) -> str:
    translations = get_translations(guild)

    message = get_nested_translation(
        translations,
        key,
    )

    if not isinstance(message, str):
        return key

    return message.format(**kwargs)