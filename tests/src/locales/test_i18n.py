from unittest.mock import MagicMock

from src.locales import i18n


def test_get_locale_without_guild():
    assert i18n.get_locale(None) == "es_ES"


def test_get_locale_supported_languages():
    languages = {
        "es": "es_ES",
        "en": "en_US",
        "fr": "fr_FR",
        "de": "de_DE",
        "it": "it_IT",
        "pt": "pt_PT",
        "nl": "nl_NL",
        "pl": "pl_PL",
        "ja": "ja_JP",
    }

    i18n.set_guild_languages({})

    for language, locale in languages.items():
        guild = MagicMock()
        guild.id = 123

        i18n.set_guild_languages({123: language})

        assert i18n.get_locale(guild) == locale


def test_get_locale_unknown_language_falls_back_to_spanish():
    guild = MagicMock()
    guild.id = 123

    i18n.set_guild_languages({123: "unknown"})

    assert i18n.get_locale(guild) == "es_ES"


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
