from unittest.mock import MagicMock

from src.i18n import translator


TEST_NAME = "Nombre"


def test_supported_languages_contains_expected_languages():
    expected = {
        "es",
        "en",
        "fr",
        "de",
        "it",
        "pt",
        "nl",
        "pl",
        "ja",
    }

    assert expected.issubset(
        translator.SUPPORTED_LANGUAGES.keys()
    )


def test_locale_files_match_supported_languages():
    assert set(
        translator.SUPPORTED_LANGUAGES
    ) == set(
        translator.LOCALE_FILES
    )


def test_set_guild_languages():
    languages = {
        123: "en",
    }

    translator.set_guild_languages(
        languages,
    )

    assert translator.GUILD_LANGUAGES is languages


def test_get_language_with_none_guild():
    assert translator.get_language(None) == translator.LOG_LANGUAGE


def test_get_language_for_unknown_guild():
    guild = MagicMock()
    guild.id = 999

    translator.set_guild_languages({})

    assert translator.get_language(guild) == "es"


def test_get_language_for_known_guild():
    guild = MagicMock()
    guild.id = 123

    translator.set_guild_languages(
        {123: "en"},
    )

    assert translator.get_language(guild) == "en"


def test_get_locale():
    guild = MagicMock()
    guild.id = 123

    translator.set_guild_languages(
        {123: "en"},
    )

    assert translator.get_locale(guild) == "en_US.json"


def test_get_nested_translation():
    translations = {
        "music": {
            "play": {
                "title": "Play",
            },
        },
    }

    result = translator.get_nested_translation(
        translations,
        "app.commands.music.embeds.play.title",
    )

    assert result == "Play"


def test_get_nested_translation_missing_key():
    translations = {
        "music": {},
    }

    result = translator.get_nested_translation(
        translations,
        "app.commands.music.embeds.play.title",
    )

    assert result == {}


def test_translate_existing_key():
    result = translator.translate(
        None,
        "app.commands.music.embeds.play.voice_not_connected",
        user=TEST_NAME,
    )

    assert isinstance(
        result,
        str,
    )
    assert result


def test_translate_missing_key():
    result = translator.translate(
        None,
        "this.key.does.not.exist",
    )

    assert result == "this.key.does.not.exist"
