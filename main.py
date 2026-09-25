import asyncio
import logging
import os
import sys

import discord
from discord.ext import commands
from dotenv import load_dotenv

from src.core.loader import load_cogs
from src.database.connection import Database
from src.database.repositories.guild import GuildRepository


# -----------------------
# Configuración
# -----------------------

load_dotenv()
TOKEN = str(os.getenv("DISCORD_TOKEN"))
LAVALINK_PASSWORD = str(os.getenv("LAVALINK_PASSWORD"))


# -----------------------
# Logs
# -----------------------

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("music_bot")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
)

file_handler = logging.FileHandler(
    "logs/bot.log",
    encoding="utf-8",
)

file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


discord_logger = logging.getLogger("discord")
discord_logger.setLevel(logging.INFO)
discord_logger.addHandler(file_handler)
discord_logger.addHandler(stream_handler)


wavelink_logger = logging.getLogger("wavelink")
wavelink_logger.setLevel(logging.DEBUG)
wavelink_logger.addHandler(file_handler)
wavelink_logger.addHandler(stream_handler)


# -----------------------
# Bot
# -----------------------

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.voice_states = True


bot = commands.Bot(
    command_prefix="!",
    description="Relatively simple music bot example",
    intents=intents,
)


# -----------------------
# Aplicación
# -----------------------

async def main():
    database = Database()
    guild_repository = GuildRepository(database)

    try:
        await database.connect()
        logger.info(
            "Conexión con PostgreSQL establecida correctamente."
        )

        await database.create_tables()
        logger.info(
            "Tablas de PostgreSQL comprobadas correctamente."
        )

        async with bot:
            await load_cogs(
                bot,
                lavalink_password=LAVALINK_PASSWORD,
            )

            logger.info(
                f"Cogs cargados: {[cog.__class__.__name__ for cog in bot.cogs]}"
            )

            await bot.start(TOKEN)

    finally:
        await database.close()


if __name__ == "__main__":
    asyncio.run(main())