from discord.ext import commands

from src.helpers.embeds import create_embed


class Leave(commands.Cog):
    """
    Gestiona el comando para abandonar el canal de audio.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.command(name="leave", aliases=["disconnect"])
    async def leave(self, ctx):
        """
        Abandona el canal de audio.

        :param ctx: Contexto del comando.
        :return: None
        """
        if ctx.voice_client is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "app.commands.music.embeds.leave.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        await ctx.voice_client.disconnect()

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "app.commands.music.embeds.leave.disconnected",
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            )
        )