from discord.ext import commands

import wavelink


class Join(commands.Cog):
    def __init__(self, bot, lavalink_password):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @commands.command(name="join")
    async def join(self, ctx):
        if not ctx.voice_client:
            if not ctx.author.voice:
                return

            return await ctx.author.voice.channel.connect(cls=wavelink.Player)

        if ctx.voice_client.channel != ctx.author.voice.channel:
            await ctx.voice_client.move_to(ctx.author.voice.channel)