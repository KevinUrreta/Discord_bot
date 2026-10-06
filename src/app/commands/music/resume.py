from discord.ext import commands
import wavelink

from src.helpers.embeds import create_embed
from src.helpers.permissions import has_voice_channel



class Resume(commands.Cog):
    """
    Gestiona el comando para continuar con la reproducción.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @has_voice_channel()
    @commands.command(name="resume")
    async def resume(self, ctx):
        """
        Continúa la reproducción pausada anteriormente.

        :param ctx: Contexto del comando.
        :return: None
        """
        if ctx.voice_client is None:
            return await ctx.send(embed=create_embed(
                    ctx.guild,
                    "app.commands.music.embeds.resume.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                ))

        player: wavelink.Player = ctx.voice_client

        if not player.paused:
            return await ctx.send(embed=create_embed(
                    ctx.guild,
                    "app.commands.music.embeds.resume.no_song_playing",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                ))

        await player.pause(False)

        await ctx.send(embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.resume.resumed",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))