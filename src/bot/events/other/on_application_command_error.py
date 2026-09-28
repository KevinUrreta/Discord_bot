from discord.ext import commands

from src.core.logging import logger
from src.locales.i18n import translate


class ApplicationCommandError(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_app_command_error(self, interaction, error):
        logger.info(
            translate(
                interaction.guild,
                "events.other.on_application_command_error.command_error",
                command=interaction.command, error=error,
            )
        )
