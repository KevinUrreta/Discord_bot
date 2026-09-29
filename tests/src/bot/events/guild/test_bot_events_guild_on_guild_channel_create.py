import ast
import importlib
from pathlib import Path


SOURCE = Path(r"D:\Carpeta\Nueva carpeta\src\bot\events\guild\on_guild_channel_create.py")


def test_source_has_valid_python_syntax():
    source = SOURCE.read_text(
        encoding="utf-8",
    )

    ast.parse(source)


def test_module_can_be_imported():
    module = importlib.import_module(
        "src.bot.events.guild.on_guild_channel_create"
    )

    assert module is not None
