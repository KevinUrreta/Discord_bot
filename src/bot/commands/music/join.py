import discord
from discord.ext import commands

import wavelink

from src.locales.i18n import translate
from src.core.logging import logger


class Join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            return

        channel = ctx.author.voice.channel

        logger.info(
            translate(
                ctx.guild,
                "commands.music.join.joining_voice",
                channel=channel.name,
            )
        )

        if ctx.voice_client is not None:
            await ctx.voice_client.move_to(channel)
            return

        await channel.connect(cls=wavelink.Player)

        logger.info(
            translate(
                ctx.guild,
                "commands.music.join.joined_voice",
                channel=channel.name,
            )
        )