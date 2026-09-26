from discord.ext import commands

from src.locales.i18n import translate
from src.core.logging import logger


class On_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self, ctx):
        logger.info(
            translate(
                ctx.guild,
                "events.other.on_command.command_executed",
                command=ctx.command.name,
                author=ctx.author,
                channel=ctx.channel,
            )
        )