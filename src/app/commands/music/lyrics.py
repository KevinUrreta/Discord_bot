from discord.ext import commands

from src.helpers.embeds import create_embed


class Lyrics(commands.Cog):
    """
    Gestiona el comando de letras de la reproducción actual.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.command(name="lyrics")
    async def lyrics(self, ctx, *, query=None):
        """
        Muestra la letra de la reproducción a actual o solicitada.
        :param ctx: Contexto del comando.
        :param query: Canción que se quiere la letra.
        :return: None
        """
        await ctx.send(embed=create_embed(
            ctx.guild,
            "app.commands.music.embeds.lyrics.not_available",
            user=ctx.author.display_name,
            footer_icon=ctx.author.display_avatar.url,
        ))
