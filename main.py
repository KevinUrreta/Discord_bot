import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from src.core.prefix import get_prefix
from src.core.loader import load_cogs
from src.database.connection import Database
from src.database.repositories.guild import GuildRepository


load_dotenv()

TOKEN = str(os.getenv("DISCORD_TOKEN"))
LAVALINK_PASSWORD = str(os.getenv("LAVALINK_PASSWORD"))

if TOKEN is None:
    raise RuntimeError("DISCORD_TOKEN no está configurado.")

if LAVALINK_PASSWORD is None:
    raise RuntimeError("LAVALINK_PASSWORD no está configurado.")


class App(commands.Bot):
    def __init__(self, database: Database) -> None:
        self.database = database
        self.guild_repository = GuildRepository(database)
        self.guild_languages = {}

        super().__init__(command_prefix=get_prefix, intents=discord.Intents.all())

    async def setup_hook(self) -> None:
        await load_cogs(self, lavalink_password=LAVALINK_PASSWORD)


async def main() -> None:
    database = Database()

    try:
        await database.create_tables()
        async with App(database) as bot: await bot.start(TOKEN)

    finally:
        await database.close()


if __name__ == "__main__": asyncio.run(main())