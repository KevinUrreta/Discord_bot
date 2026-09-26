import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from src.core.loader import load_cogs
from src.database.connection import Database
from src.database.repositories.guild import GuildRepository

 #
 # @KevinUrreta
 #
 #

load_dotenv()
TOKEN = str(os.getenv("DISCORD_TOKEN"))
LAVALINK_PASSWORD = str(os.getenv("LAVALINK_PASSWORD"))


class App(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

    async def setup_hook(self):
        await load_cogs(self, lavalink_password=LAVALINK_PASSWORD)


async def main():
    database = Database(); guild_repository = GuildRepository(database)

    try:
        await database.connect(); await database.create_tables()
        async with App() as bot: await bot.start(TOKEN)

    finally: await database.close()


if __name__ == "__main__":
    try: asyncio.run(main())
    except KeyboardInterrupt: os.close(0)