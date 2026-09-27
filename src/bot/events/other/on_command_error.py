import discord
from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class On_command_error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(
        self,
        ctx: commands.Context,
        error: commands.CommandError,
    ):
        if isinstance(
            error,
            commands.MissingPermissions,
        ):
            await ctx.send(
                translate(
                    ctx.guild,
                    "events.other.on_command_error.missing_permissions",
                )
            )

            return

        logger.error(
            f"Error en el comando "
            f"'{ctx.command}': {error}"
        )

        await ctx.send(
            translate(
                ctx.guild,
                "events.other.on_command_error.command_error",
                command=ctx.command,
                error=error,
            )
        )