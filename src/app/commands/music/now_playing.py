import asyncio

import wavelink
from discord.ext import commands

from src.helpers.embeds import create_embed
from src.helpers.formatting import format_duration
from src.helpers.music_utils import (
    get_original_info,
    get_thumbnail
)


class Nowplaying(commands.Cog):
    """
    Gestiona el comando de información de la reproducción presente.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.command(name="nowplaying")
    async def nowplaying(self, ctx):
        """
        Muestra la información de la reproducción actual.

        :param ctx: Contexto del comando.
        :return: None
        """
        if ctx.voice_client is None:
            return await ctx.send(embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.now_playing_not_connected",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))

        player: wavelink.Player = ctx.voice_client
        track = player.current

        if track is None:
            return await ctx.send(embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.now_playing_empty",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))

        info = await asyncio.to_thread(get_original_info, track.uri)

        return await ctx.send(embed=create_embed(
            ctx.guild,
            "app.commands.music.embeds.now_playing",
            title=info["title"],
            duration=format_duration(track.length),
            views=info["views"],
            queue=player.queue.count,
            user=ctx.author.display_name,
            thumbnail=get_thumbnail(track),
            footer_icon=ctx.author.display_avatar.url,
        ))
