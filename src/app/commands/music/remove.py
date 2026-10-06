from discord.ext import commands

import wavelink

from src.helpers.embeds import create_embed


class Remove(commands.Cog):
    """
    Gestiona el comando para limpiar la reproducción especificada.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.command(name="remove")
    async def remove(self, ctx, position: int):
        """
        Elimina una reproducción especificada de la cola.

        :param ctx: Contexto del comando.
        :param position: Posición de la cola de reproducción.
        :return: None
        """
        if ctx.voice_client is None:
            return await ctx.send(embed=create_embed(
                    ctx.guild,
                    "app.commands.music.embeds.remove.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                ))

        player: wavelink.Player = ctx.voice_client

        if player.queue.is_empty:
            return await ctx.send(embed=create_embed(
                    ctx.guild,
                    "app.commands.music.embeds.remove.queue_empty",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                ))

        tracks = list(player.queue)

        if position < 1 or position > len(tracks):
            return await ctx.send(embed=create_embed(
                    ctx.guild,
                    "app.commands.music.embeds.remove.invalid_position",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                ))

        track = tracks[position - 1]
        player.queue.remove(track)

        await ctx.send(embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.remove.removed",
                title=track.title,
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))