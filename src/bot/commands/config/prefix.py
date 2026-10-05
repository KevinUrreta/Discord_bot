from discord.ext import commands

from src.helpers.embeds import create_embed
from src.helpers.permissions import has_manage_guild
from src.database.repositories.guild import GuildRepository


class Prefix(commands.Cog):
    """
    Gestiona el comando para consultar o cambiar el prefijo del server.
    """
    def __init__(self, bot, lavalink_password):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot
        self.guild_repository = GuildRepository(self.bot.database)

    @commands.command(name="prefix")
    @has_manage_guild()
    async def prefix(self, ctx, prefix: str | None = None):
        """
        Consulta o cambio el prefijo del server.

        :param ctx: Contexto del comando.
        :param prefix: Prefijo al que se desea cambiar.
        :return: None
        """
        if ctx.guild is None:
            return

        guild_id = ctx.guild.id

        if prefix is None:
            guild = await self.guild_repository.get(guild_id)

            if guild is None:
                return

            await ctx.send(embed=create_embed(
                    ctx.guild,
                    "bot.commands.config.embeds.prefix.current_prefix",
                    prefix=guild.prefix,
                ))
            return

        if len(prefix) != 1:
            return

        guild = await self.guild_repository.update(guild_id=guild_id, prefix=prefix)

        if guild is None:
            return

        await ctx.send(embed=create_embed(
                ctx.guild,
                "bot.commands.config.embeds.prefix.prefix_changed",
                prefix=prefix,
            ))