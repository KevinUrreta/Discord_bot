import wavelink
from discord.ext import commands

from src.helpers.embeds import create_embed


class Loop(commands.Cog):
    """
    Gestiona el comando de comenzar o cerrar bucle en la reproducción.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.command(name="loop")
    async def loop(self, ctx):
        """
        Activa o desactiva el bucle en la reproducción actual.
        :param ctx: Contexto del comando.
        :return: None
        """
        if ctx.voice_client is None:
            return await ctx.send(embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.loop.not_connected",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))

        player: wavelink.Player = ctx.voice_client

        if not player.current:
            return await ctx.send(embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.loop.no_song_playing",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))

        player.queue.mode = (
            wavelink.QueueMode.loop
            if player.queue.mode != wavelink.QueueMode.loop
            else wavelink.QueueMode.normal
        )

        if player.queue.mode == wavelink.QueueMode.loop:
            await ctx.send(embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.loop.enabled",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))
        else:
            await ctx.send(embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.loop.disabled",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))
