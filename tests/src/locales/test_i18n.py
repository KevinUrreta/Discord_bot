from unittest.mock import MagicMock

from src.locales import i18n


def test_get_locale_without_guild():
    assert i18n.get_locale(None) == "es_ES.json"


def test_get_locale_supported_languages():
    languages = {
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

    for language, locale in languages.items():
        guild = MagicMock()
        guild.id = 123

        i18n.set_guild_languages(
            {123: language}
        )

        assert i18n.get_locale(guild) == locale


def test_get_locale_unknown_language_falls_back_to_spanish():
    guild = MagicMock()
    guild.id = 123

    i18n.set_guild_languages(
        {123: "unknown"}
    )

    assert i18n.get_locale(guild) == "es_ES.json"


def test_get_nested_translation():
    translations = {
        "commands": {
            "music": {
                "play": "Play",
            }
        }
    }

    assert (
        i18n.get_nested_translation(
            translations,
            "commands.music.play",
        )
        == "Play"
    )


def test_get_nested_translation_missing_key():
    translations = {
        "commands": {}
    }

    assert (
        i18n.get_nested_translation(
            translations,
            "commands.music.play",
        )
        == {}
    )


def test_translate_formats_message(monkeypatch):
    monkeypatch.setattr(
        i18n,
        "get_translations",
        lambda guild: {
            "hello": "Hola {name}",
        },
    )

    assert (
        i18n.translate(
            None,
            "hello",
            name="Kevin",
        )
        == "Hola Kevin"
    )


def test_translate_missing_message_returns_key(monkeypatch):
    monkeypatch.setattr(
        i18n,
        "get_translations",
        lambda guild: {},
    )

    assert (
        i18n.translate(
            None,
            "missing.key",
        )
        == "missing.key"
    )
