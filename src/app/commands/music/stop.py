from discord.ext import commands

import wavelink

from src.helpers.embeds import create_embed


class Stop(commands.Cog):
    """
    Gestiona el comando para detener la reproducción.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.command(name="stop")
    async def stop(self, ctx):
        """
        Detiene la reproducción.

        :param ctx: Contexto del comando.
        :return: None
        """
        if ctx.voice_client is None:
            return await ctx.send(embed=create_embed(
                    ctx.guild,
                    "app.commands.music.embeds.stop.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                ))

        player: wavelink.Player = ctx.voice_client

        player.queue.clear()
        await player.stop()

        await ctx.send(embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.stop.stopped",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))