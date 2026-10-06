import asyncio

import discord
from discord.ext import commands

from src.core.config import settings
from src.core.loader import load_cogs
from src.core.prefix import get_prefix
from src.infrastructure.lavalink.connection import connect_lavalink
from src.infrastructure.database.connection import Database
from src.infrastructure.database.repositories.guild import GuildRepository


class App(commands.Bot):
    def __init__(self, database: Database) -> None:
        self.database = database
        self.guild_repository = GuildRepository(database)
        self.guild_languages = {}

        super().__init__(command_prefix=get_prefix, intents=discord.Intents.all())

    async def setup_hook(self) -> None:
        await connect_lavalink(self)
        await load_cogs(self)


async def main() -> None:
    database = Database()

    try:
        await database.create_tables()

        async with App(database) as bot: await bot.start(settings.discord_token)


    finally:
        await database.close()


if __name__ == "__main__": asyncio.run(main())