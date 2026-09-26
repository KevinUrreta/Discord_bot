import logging

import discord
import wavelink
from discord.ext import commands

from src.locales.i18n import translate


logger = logging.getLogger("music_bot")


class Events(commands.Cog):
    def __init__(self, bot, lavalink_password):
        self.bot = bot
        self.lavalink_password = lavalink_password

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(
            translate(
                None,
                "bot_connected",
                bot=self.bot.user,
            )
        )

        if not wavelink.Pool.nodes:
            logger.info(
                translate(
                    None,
                    "connecting_lavalink",
                )
            )

            await wavelink.Pool.connect(
                nodes=[
                    wavelink.Node(
                        identifier="main",
                        uri="http://lavalink:2333",
                        password=self.lavalink_password,
                    )
                ],
                client=self.bot,
            )

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return

        logger.info(
            translate(
                message.guild,
                "message_detected",
                author=message.author.name,
                message=message.content,
            )
        )

        await self.bot.process_commands(message)

    @commands.Cog.listener()
    async def on_command(self, ctx):
        logger.info(
            translate(
                ctx.guild,
                "command_executed",
                command=ctx.command.name,
                author=ctx.author,
                channel=ctx.channel,
            )
        )

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
