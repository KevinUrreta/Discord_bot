import asyncio
import os
from typing import cast

import discord
from discord.ext import commands
from dotenv import load_dotenv

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

        super().__init__(command_prefix="!", intents=discord.Intents.all())

    async def get_prefix(self, message: discord.Message) -> str:
        if message.guild is None:
            return "!"

        guild = await self.guild_repository.get(message.guild.id)

        if guild is None:
            return "!"

        return cast(str, guild.prefix)

    async def setup_hook(self):
        await load_cogs(self, lavalink_password=LAVALINK_PASSWORD)


async def main() -> None:
    database = Database()

    try:
        await database.create_tables()

        async with App(database) as bot:
            await bot.start(TOKEN)

    finally:
        await database.close()


if __name__ == "__main__": asyncio.run(main())