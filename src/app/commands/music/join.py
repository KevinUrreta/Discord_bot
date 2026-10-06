import wavelink
from discord.ext import commands


class Join(commands.Cog):
    """
    Gestiona el comando para unir el app al canal de voz.
    """

    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.command(name="join")
    async def join(self, ctx):
        """
        Llama al app al canal de voz.

        :param ctx: Contexto del comando.
        :return: None
        """
        if not ctx.voice_client:
            if not ctx.author.voice:
                return

            return await ctx.author.voice.channel.connect(cls=wavelink.Player)

        if ctx.voice_client.channel != ctx.author.voice.channel:
            await ctx.voice_client.move_to(ctx.author.voice.channel)
