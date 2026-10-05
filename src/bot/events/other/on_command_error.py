from discord.ext import commands

from src.core.logging import errors_logger
from src.helpers.embeds import create_embed
from src.helpers.permissions import VoiceChannelRequired
from src.locales.i18n import translate


class On_command_error(commands.Cog):
    """
    Gestiona cuando hay un error al usar un comando.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """
        Registra cuando hay un error al usar un comando.
        :param ctx: Contexto.
        :param error: Error.
        :return: None
        """
        if isinstance(error, VoiceChannelRequired):
            await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.events.embeds.other.voice_channel_required",
                )
            )
            return

        if isinstance(error, (commands.MissingPermissions, commands.CheckFailure)):
            await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.events.embeds.other.missing_permissions",
                )
            )
            return

        errors_logger.error(
            translate(
                None,
                "bot.events.logs.other.on_command_error.logged_error",
                command=ctx.invoked_with,
                error=error,
            ),
            exc_info=error,
        )

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "bot.events.embeds.other.command_error",
                command=ctx.invoked_with,
            )
        )