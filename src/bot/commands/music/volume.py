from discord.ext import commands

import wavelink

from src.database.repositories.guild import GuildRepository
from src.helpers.embeds import create_embed


class Volume(commands.Cog):
    def __init__(self, bot, lavalink_password):
        """
        Inicializa el evento.

        :param bot: Instancia principal del bot de Discord.
        """
        self.bot = bot
        self.guild_repository = GuildRepository(self.bot.database)

    @commands.command(name="volume")
    async def volume(self, ctx, volume: int | None = None):
        if volume is None:
            guild = await self.guild_repository.get(ctx.guild.id)

            if guild is None:
                return

            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.volume.current",
                    volume=guild.volume,
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        if ctx.voice_client is None:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.volume.not_connected",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        if volume < 1 or volume > 100:
            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.music.embeds.volume.invalid_volume",
                    user=ctx.author.display_name,
                    footer_icon=ctx.author.display_avatar.url,
                )
            )

        player: wavelink.Player = ctx.voice_client

        await player.set_volume(volume)

        await self.guild_repository.update(guild_id=ctx.guild.id, volume=volume)

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "bot.commands.music.embeds.volume.changed",
                volume=volume,
                user=ctx.author.display_name,
                footer_icon=ctx.author.display_avatar.url,
            )
        )
