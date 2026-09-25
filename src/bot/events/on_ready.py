import logging
import wavelink

from discord.ext import commands

from src.locales.i18n import translate
from src.core.logging import logger


class On_ready(commands.Cog):
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
