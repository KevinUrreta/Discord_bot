import wavelink
from discord.ext import commands

from src.helpers.embeds import create_embed
from src.infrastructure.database.repositories.guild import GuildRepository


class Volume(commands.Cog):
    """
    Gestiona el comando para consultar o cambiar el volumen del server.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot
        self.guild_repository = GuildRepository(self.bot.database)

    @commands.command(name="volume")
    async def volume(self, ctx, volume: int | None = None):
        """
        Consulta o cambia el volumen del server.

        :param ctx: Contexto del comando.
        :param volume: Volumen a cambiar
        :return: None
        """
        if volume is None:
            guild = await self.guild_repository.get(ctx.guild.id)

            if guild is None:
                return

            return await ctx.send(embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.volume.current",
                volume=guild.volume,
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))

        if ctx.voice_client is None:
            return await ctx.send(embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.volume.not_connected",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))

        if volume < 1 or volume > 100:
            return await ctx.send(embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.volume.invalid_volume",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))

        player: wavelink.Player = ctx.voice_client

        await player.set_volume(volume)
        await self.guild_repository.update(guild_id=ctx.guild.id, volume=volume)

        await ctx.send(embed=create_embed(
            ctx.guild,
            "app.commands.music.embeds.volume.changed",
            volume=volume,
            user=ctx.author.display_name,
            footer_icon=ctx.author.display_avatar.url,
        ))
