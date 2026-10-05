from discord.ext import commands

from src.core.logging import logger
from src.database.repositories.guild import GuildRepository
from src.helpers.embeds import create_embed
from src.helpers.permissions import has_manage_guild
from src.locales.i18n import (
    SUPPORTED_LANGUAGES,
    translate,
)


class Language(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.guild_repository = GuildRepository(
            self.bot.database
        )

    @commands.command(name="language")
    @has_manage_guild()
    async def language(
        self,
        ctx,
        language: str | None = None,
    ):
        if ctx.guild is None:
            return

        guild_id = ctx.guild.id

        if language is None:
            current_language = self.bot.guild_languages.get(
                guild_id,
                "es",
            )

            language_name = SUPPORTED_LANGUAGES.get(
                current_language,
                current_language,
            )

            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.config.embeds.language.current_language",
                    language_name=language_name,
                    language=current_language,
                )
            )

        language = language.lower()

        if language not in SUPPORTED_LANGUAGES:
            available_languages = "\n".join(
                f"{code} — {name}"
                for code, name in SUPPORTED_LANGUAGES.items()
            )

            await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.config.embeds.language.invalid_language",
                )
            )

            return await ctx.send(
                embed=create_embed(
                    ctx.guild,
                    "bot.commands.config.embeds.language.available_languages",
                    languages=available_languages,
                )
            )

        old_language = self.bot.guild_languages.get(
            guild_id,
            "es",
        )

        guild = await self.guild_repository.update(
            guild_id=guild_id,
            language=language,
        )

        if guild is None:
            return

        self.bot.guild_languages[guild_id] = language

        await ctx.send(
            embed=create_embed(
                ctx.guild,
                "bot.commands.config.embeds.language.language_changed",
                language_name=SUPPORTED_LANGUAGES[language],
                language=language,
            )
        )

        logger.info(
            translate(
                None,
                "bot.commands.config.logs.language.changed",
                old_language=old_language,
                language=language,
                user=ctx.author.display_name,
                guild_id=guild_id,
            )
        )