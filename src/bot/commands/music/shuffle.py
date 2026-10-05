from discord.ext import commands

import wavelink

from src.helpers.embeds import create_embed


class Shuffle(commands.Cog):
    """
    Gestiona el comando para aleatorizar la cola de reproducción.
    """
    def __init__(self, bot, lavalink_password):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @commands.command(name="shuffle")
    async def shuffle(self, ctx):
        """
        Aleatoriza la cola de reproducción.

        :param ctx: Contexto del comando.
        :return: None
        """
        if ctx.voice_client is None:
            return await ctx.send(embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.shuffle.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                ))

        player: wavelink.Player = ctx.voice_client

        if player.queue.count < 2:
            return await ctx.send(embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.shuffle.not_enough_songs",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                ))

        player.queue.shuffle()

        await ctx.send(embed=create_embed(
                ctx.guild,
                "bot.commands.music.embeds.shuffle.shuffled",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            ))