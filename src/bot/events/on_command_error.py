from discord.ext import commands

from src.locales.i18n import translate
from src.core.logging import logger


class On_command_error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        logger.error(
            translate(
                ctx.guild,
                "command_error",
                command=ctx.command,
                error=error,
            ),
            exc_info=True,
        )
