from unittest.mock import MagicMock

from src.locales import i18n


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
        i18n.SUPPORTED_LANGUAGES.keys()
    )


def test_locale_files_match_supported_languages():
    assert set(
        i18n.SUPPORTED_LANGUAGES
    ) == set(
        i18n.LOCALE_FILES
    )


def test_set_guild_languages():
    languages = {
        123: "en",
    }

    i18n.set_guild_languages(
        languages,
    )

    assert i18n.GUILD_LANGUAGES is languages


def test_get_language_with_none_guild():
    assert i18n.get_language(None) == i18n.LOG_LANGUAGE


def test_get_language_for_unknown_guild():
    guild = MagicMock()
    guild.id = 999

    i18n.set_guild_languages({})

    assert i18n.get_language(guild) == "es"


def test_get_language_for_known_guild():
    guild = MagicMock()
    guild.id = 123

    i18n.set_guild_languages(
        {123: "en"},
    )

    assert i18n.get_language(guild) == "en"


def test_get_locale():
    guild = MagicMock()
    guild.id = 123

    i18n.set_guild_languages(
        {123: "en"},
    )

    assert i18n.get_locale(guild) == "en_US.json"


def test_get_nested_translation():
    translations = {
        "music": {
            "play": {
                "title": "Play",
            },
        },
    }

    result = i18n.get_nested_translation(
        translations,
        "bot.commands.music.embeds.play.title",
    )

    assert result == "Play"


def test_get_nested_translation_missing_key():
    translations = {
        "music": {},
    }

    result = i18n.get_nested_translation(
        translations,
        "bot.commands.music.embeds.play.title",
    )

    assert result == {}


def test_translate_existing_key():
    result = i18n.translate(
        None,
        "bot.commands.music.embeds.play.voice_not_connected",
        user=TEST_NAME,
    )

    assert isinstance(
        result,
        str,
    )
    assert result


def test_translate_missing_key():
    result = i18n.translate(
        None,
        "this.key.does.not.exist",
    )

    assert result == "this.key.does.not.exist"
