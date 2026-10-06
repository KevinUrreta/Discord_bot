import asyncio

import wavelink
from discord.ext import commands

from src.helpers.embeds import create_embed
from src.helpers.music_utils import get_original_info
from src.helpers.permissions import has_voice_channel


class Queue(commands.Cog):
    """
    Gestiona el comando para consultar la información de la cola de reproducción.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @has_voice_channel()
    @commands.command(name="queue", aliases=["q"])
    async def queue(self, ctx):
        """
        Consulta la información de la cola de reproducción.

        :param ctx: Contexto del comando.
        :return: None
        """
        if ctx.voice_client is None:
            return await ctx.send(embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.queue.not_connected",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))

        player: wavelink.Player = ctx.voice_client

        if player.queue.is_empty:
            return await ctx.send(embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.queue.empty",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))

        tracks = list(player.queue)
        infos = await asyncio.gather(*(
            asyncio.to_thread(get_original_info, track.uri)
            for track in tracks
        ))

        titles = [info["title"] for info in infos]
        message = "\n".join(
            f"{index}. {title}"
            for index, title in enumerate(titles, start=1)
        )

        await ctx.send(embed=create_embed(
            ctx.guild,
            "app.commands.music.embeds.queue.list",
            queue=message,
            user=ctx.author.display_name,
            footer_icon=ctx.author.display_avatar.url,
        ))
