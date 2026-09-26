from discord.ext import commands

import wavelink

from src.locales.i18n import translate


class Volume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="volume")
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.volume.not_connected",
                )
            )

        if volume < 0 or volume > 100:
            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.music.volume.invalid_volume",
                )
            )

        player: wavelink.Player = ctx.voice_client

        await player.set_volume(volume)

        await ctx.send(
            translate(
                ctx.guild,
                "commands.music.volume.volume_changed",
                volume=volume,
            )
        )