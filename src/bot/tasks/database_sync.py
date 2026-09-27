from discord.ext import commands, tasks

from src.core.logging import logger
from src.locales.i18n import set_guild_languages
from src.database.repositories.guild import GuildRepository


class DatabaseSync(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.guild_repository = GuildRepository(
            self.bot.database
        )
        set_guild_languages(
            self.bot.guild_languages
        )
        self.sync_database.start()

    def cog_unload(self):
        self.sync_database.cancel()

    @tasks.loop(minutes=10)
    async def sync_database(self):
        for guild in self.bot.guilds:
            guild_data = await self.guild_repository.create(
                guild_id=guild.id,
                name=guild.name,
            )

            self.bot.guild_languages[guild.id] = (
                guild_data.language
            )

            logger.info(
                f"Servidor sincronizado: "
                f"{guild.name} ({guild.id})"
            )

        logger.info(
            f"Sincronización completada: "
            f"{len(self.bot.guilds)} servidores"
        )

    @sync_database.before_loop
    async def before_sync_database(self):
        await self.bot.wait_until_ready()