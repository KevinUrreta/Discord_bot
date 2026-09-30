from discord.ext import commands

from src.helpers.permissions import has_manage_guild
from src.database.repositories.guild import GuildRepository
from src.locales.i18n import translate


class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.guild_repository = GuildRepository(
            self.bot.database
        )

    @commands.command(name="prefix")
    @has_manage_guild()
    async def prefix(
        self,
        ctx,
        prefix: str | None = None,
    ):
        if ctx.guild is None:
            return

        guild_id = ctx.guild.id

        if prefix is None:
            guild = await self.guild_repository.get(
                guild_id
            )

            if guild is None:
                return

            await ctx.send(
                translate(
                    ctx.guild,
                    "commands.config.prefix.current_prefix",
                    prefix=guild.prefix,
                )
            )

            return

        guild = await self.guild_repository.update(
            guild_id=guild_id,
            prefix=prefix,
        )

        if guild is None:
            return

        await ctx.send(
            translate(
                ctx.guild,
                "commands.config.prefix.prefix_changed",
                prefix=prefix,
            )
        )