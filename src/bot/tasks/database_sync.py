from discord.ext import commands, tasks

from src.core.logging import database_logger
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
        database_logger.info(
            "Iniciando sincronización de %s servidores.",
            len(self.bot.guilds),
        )

        for guild in self.bot.guilds:
            guild_data = await self.guild_repository.create(
                guild_id=guild.id,
                name=guild.name,
            )

            self.bot.guild_languages[guild.id] = (
                guild_data.language
            )

            database_logger.info(
                "Servidor sincronizado: %s (%s).",
                guild.name,
                guild.id,
            )

        database_logger.info(
            "Sincronización completada: %s servidores.",
            len(self.bot.guilds),
        )

    @sync_database.before_loop
    async def before_sync_database(self):
        await self.bot.wait_until_ready()