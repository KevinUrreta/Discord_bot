import importlib
import inspect
from collections import defaultdict
from pathlib import Path

from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


async def load_cogs(bot, lavalink_password):
    """
    Recorre, busca y carga automáticamente los comandos, eventos y tareas del bot.

    :param bot: Instancia del Bot.
    :param lavalink_password: Contraseña para conectar lavalink.
    :return: None
    """
    base_path = Path(__file__).parent.parent

    categories = defaultdict(
        lambda: {"total": 0, "loaded": 0, "failed": []}
    )

    for cog_type in ("commands", "events", "tasks"):
        cog_path = base_path / "bot" / cog_type

        for file in cog_path.rglob("*.py"):
            if file.name == "__init__.py":
                continue

            category = file.parent.name
            key = (cog_type, category)

            categories[key]["total"] += 1

            module_path = ".".join(
                file.relative_to(base_path.parent).with_suffix("").parts
            )

            try:
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

                    parameters = inspect.signature(attribute).parameters

                    if "lavalink_password" in parameters:
                        cog = attribute(bot, lavalink_password)
                    else:
                        cog = attribute(bot)

                    await bot.add_cog(cog)

                    categories[key]["loaded"] += 1

            except Exception as error:
                categories[key]["failed"].append((file.name, error))

    for (cog_type, category), data in categories.items():
        label = translate(None, f"core.logs.loader.{cog_type}")

        if data["failed"]:
            for filename, error in data["failed"]:
                logger.error(
                    translate(
                        None,
                        "core.logs.loader.load_error",
                        label=label,
                        category=category,
                        filename=filename,
                        error_type=type(error).__name__,
                        error=error,
                    )
                )

            continue

        logger.info(
            translate(
                None,
                "core.logs.loader.loaded",
                label=label,
                category=category,
                loaded=data["loaded"],
            )
        )