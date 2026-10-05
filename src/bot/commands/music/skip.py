from discord.ext import commands

import wavelink

from src.helpers.embeds import create_embed
from src.helpers.permissions import has_voice_channel


class Skip(commands.Cog):
    def __init__(self, bot, lavalink_password):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @has_voice_channel()
    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.skip.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player: wavelink.Player = ctx.voice_client

        if player.current is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.skip.no_song_playing",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        await player.skip(force=True)

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "bot.commands.music.embeds.skip.skipped",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            )
        )