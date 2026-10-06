import inspect

from unittest.mock import MagicMock

from discord.ext import commands


MODULE_NAME = "src.app.commands.music.remove"


def _find_cog_class(module):
    classes = []

    for _, candidate in inspect.getmembers(
        module,
        inspect.isclass,
    ):
        if candidate is commands.Cog:
            continue

        try:
            is_cog = issubclass(
                candidate,
                commands.Cog,
            )
        except TypeError:
            continue

        if is_cog:
            classes.append(candidate)

    return classes


def test_module_imports():
    import importlib

    module = importlib.import_module(
        MODULE_NAME,
    )

    assert module is not None


def test_module_contains_expected_cog():
    import importlib

    module = importlib.import_module(
        MODULE_NAME,
    )

    cogs = _find_cog_class(module)

    assert cogs, (
        f"No se encontró ningún Cog en {MODULE_NAME}"
    )


def test_cog_can_be_instantiated():
    import importlib

    module = importlib.import_module(
        MODULE_NAME,
    )

    cogs = _find_cog_class(module)

    assert cogs

    cog_class = cogs[0]

    cog = cog_class(
        MagicMock(),
    )

    assert cog is not None


def test_cog_registers_commands():
    import importlib

    module = importlib.import_module(
        MODULE_NAME,
    )

    cogs = _find_cog_class(module)

    assert cogs

    cog = cogs[0](
        MagicMock(),
    )

    commands_found = cog.get_commands()

    assert commands_found
