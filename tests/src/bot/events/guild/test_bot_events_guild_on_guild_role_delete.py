import ast
import importlib
from pathlib import Path


SOURCE = Path(r"/app\events\guild\on_guild_role_delete.py")


def test_source_has_valid_python_syntax():
    source = SOURCE.read_text(
        encoding="utf-8",
    )

    ast.parse(source)


def test_module_can_be_imported():
    module = importlib.import_module(
        "src.app.events.guild.on_guild_role_delete"
    )

    assert module is not None
