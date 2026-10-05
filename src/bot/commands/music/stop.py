from discord.ext import commands

import wavelink

from src.helpers.embeds import create_embed


class Stop(commands.Cog):
    def __init__(self, bot, lavalink_password):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @commands.command(name="stop")
    async def stop(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.stop.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player: wavelink.Player = ctx.voice_client

        player.queue.clear()
        await player.stop()

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "bot.commands.music.embeds.stop.stopped",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            )
        )