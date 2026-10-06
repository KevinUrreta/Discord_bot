from discord.ext import commands, tasks

from src.infrastructure.database.repositories.guild import GuildRepository
from src.infrastructure.database.repositories.member import MemberRepository
from src.core.logging import logger
from src.i18n.translator import translate, set_guild_languages


class DatabaseSync(commands.Cog):
    """
    Sincroniza periódicamente los servidores y miembros de Discord
    con la base de datos.
    """
    def __init__(self, bot):
        """
        Inicializa el task de sincronización de la base de datos.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot
        self.guild_repository = GuildRepository(self.bot.database)
        self.member_repository = MemberRepository(self.bot.database)

        # Inicia la tarea de sincronización, forzamos esta sincronización
        # para comprobar cambios entre encendidos y apagados.
        self.sync_database.start()

    def cog_unload(self):
        """
        Detiene la tarea de sincronización.
        :return:
        """
        self.sync_database.cancel()

    @tasks.loop(minutes=10)
    async def sync_database(self):
        """
        Sincroniza los servidores y miembros del app con la base de datos.
        :return:
        """
        logger.info(
            translate(
                None,
                "app.tasks.logs.database_sync.started",
            )
        )

        for guild in self.bot.guilds:
            guild_data = await self.guild_repository.create(
                guild_id=guild.id,
                name=guild.name,
                source="sync_database",
            )

            self.bot.guild_languages[guild.id] = (guild_data.language)

            for member in guild.members:
                await self.member_repository.create(
                    member_id=member.id,
                    guild_id=guild.id,
                    name=member.name,
                    display_name=member.display_name,
                    joined_at=member.joined_at,
                    source="sync_database",
                )

        set_guild_languages(self.bot.guild_languages)

    @sync_database.before_loop
    async def before_sync_database(self):
        """
        Espera que el app este iniciado para iniciar la sincronización.
        :return: None
        """
        await self.bot.wait_until_ready()