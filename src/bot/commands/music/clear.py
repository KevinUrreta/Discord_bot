from discord.ext import commands

import wavelink

from src.helpers.embeds import create_embed


class Clear(commands.Cog):
    """
    Gestiona el comando para limpiar la cola de reproducción.
    """
    def __init__(self, bot, lavalink_password):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @commands.command(name="clear")
    async def clear(self, ctx):
        """
        Elimina todas las canciones pendientes de la cola de reproducción.

        :param ctx: Contexto del comando.
        :return: None
        """
        if ctx.voice_client is None:
            return await ctx.send(embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.clear.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                ))

        player: wavelink.Player = ctx.voice_client

        if player.queue.is_empty:
            return await ctx.send(embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.clear.queue_empty",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                ))

        player.queue.clear()

        await ctx.send(embed=create_embed(
                ctx.guild,
                "bot.commands.music.embeds.clear.cleared",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))