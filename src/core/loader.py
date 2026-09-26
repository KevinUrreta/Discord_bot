import importlib
from pathlib import Path

from discord.ext import commands


async def load_cogs(bot, lavalink_password):
    base_path = Path(__file__).parent.parent

    # print(f"BASE PATH: {base_path}")

    for file in base_path.rglob("*.py"):
        if file.name == "__init__.py":
            continue

        if file.name == "loader.py":
            continue

        # print(f"ARCHIVO ENCONTRADO: {file}")

        module_path = ".".join(
            file.relative_to(base_path.parent)
            .with_suffix("")
            .parts
        )

        # print(f"MODULO: {module_path}")

        module = importlib.import_module(module_path)

        for attribute in vars(module).values():
            if not isinstance(attribute, type):
                continue

            # print(
            #     f"CLASE: {attribute.__name__} "
            #     f"| COG: {issubclass(attribute, commands.Cog)}"
            # )

            if not issubclass(attribute, commands.Cog):
                continue

            if attribute is commands.Cog:
                continue

            try:
                cog = attribute(
                    bot,
                    lavalink_password,
                )
            except TypeError:
                cog = attribute(bot)

            await bot.add_cog(cog)
            # print(f"COG CARGADO: {attribute.__name__}")