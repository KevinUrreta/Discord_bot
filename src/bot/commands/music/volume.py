from discord.ext import commands

import wavelink

from src.core.logging import logger
from src.database.repositories.guild import GuildRepository
from src.locales.i18n import translate


class Volume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.guild_repository = GuildRepository(
            self.bot.database
        )

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

        logger.info(
            f"Guardando volumen en BD: "
            f"guild_id={ctx.guild.id}, volume={volume}"
        )

        guild = await self.guild_repository.update(
            guild_id=ctx.guild.id,
            volume=volume,
        )

        if guild is None:
            logger.error(
                f"No se pudo actualizar el volumen en BD: "
                f"guild_id={ctx.guild.id}"
            )
        else:
            logger.info(
                f"Volumen guardado correctamente en BD: "
                f"guild_id={guild.id}, volume={guild.volume}"
            )

        await ctx.send(
            translate(
                ctx.guild,
                "commands.music.volume.volume_changed",
                volume=volume,
            )
        )