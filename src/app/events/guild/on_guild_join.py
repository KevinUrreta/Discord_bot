import discord
from discord.ext import commands

from src.core.logging import logger
from src.infrastructure.database.repositories.guild import GuildRepository
from src.infrastructure.database.repositories.member import MemberRepository
from src.i18n.translator import translate


class On_guild_join(commands.Cog):
    """
    Gestiona la entrada a un server.
    """
    def __init__(self, bot):
        """
        Inicializa la entrada a un server.

        :param bot:
        """
        self.bot = bot
        self.guild_repository = GuildRepository(self.bot.database)
        self.member_repository = MemberRepository(self.bot.database)

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        """
        Crea o actualiza la base de datos con los valores del nuevo server.

        :param guild: Server
        :return: None
        """
        await self.guild_repository.create(guild_id=guild.id, name=guild.name)

        for member in guild.members:
            await self.member_repository.create(
                member_id=member.id,
                guild_id=guild.id,
                name=member.name,
                display_name=member.display_name,
                joined_at=member.joined_at,
            )

        logger.info(
            translate(
                None,
                "app.events.logs.guild.on_guild_join.guild_added",
                guild_name=guild.name,
                guild_id=guild.id,
            )
        )