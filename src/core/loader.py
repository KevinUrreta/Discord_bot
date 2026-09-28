import importlib
import inspect
from pathlib import Path

from discord.ext import commands

from src.core.logging import logger


async def load_cogs(bot, lavalink_password):
    base_path = Path(__file__).parent.parent

    logger.info(
        "Iniciando carga de Cogs desde: %s",
        base_path,
    )

    for file in base_path.rglob("*.py"):
        if file.name == "__init__.py":
            continue

        if file.name == "loader.py":
            continue

        logger.debug(
            "Archivo encontrado: %s",
            file,
        )

        module_path = ".".join(
            file.relative_to(base_path.parent)
            .with_suffix("")
            .parts
        )

        logger.debug(
            "Módulo encontrado: %s",
            module_path,
        )

        module = importlib.import_module(module_path)

        for attribute in vars(module).values():
            if not isinstance(attribute, type):
                continue

            if not issubclass(attribute, commands.Cog):
                continue

            if attribute is commands.Cog:
                continue
            if attribute.__module__ != module.__name__:
                continue

            parameters = inspect.signature(
                attribute
            ).parameters

            if "lavalink_password" in parameters:
                cog = attribute(
                    bot,
                    lavalink_password,
                )
            else:
                cog = attribute(bot)

            await bot.add_cog(cog)

            logger.info(
                "Cog cargado: %s",
                attribute.__name__,
            )

    logger.info("Carga de Cogs completada.")