from discord.ext import commands

from src.database.repositories.guild import GuildRepository
from src.helpers.permissions import has_manage_messages
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
    @has_manage_messages()
    async def language(
        self,
        ctx,
        language: str | None = None,
    ):
        if ctx.guild is None:
            return

        guild_id = ctx.guild.id

        if language is None:
            current_language = (
                self.bot.guild_languages.get(
                    guild_id,
                    "es",
                )
            )

            language_name = SUPPORTED_LANGUAGES.get(
                current_language,
                current_language,
            )

            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.config.language.current_language",
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
                translate(
                    ctx.guild,
                    "commands.config.language.invalid_language",
                )
            )

            return await ctx.send(
                translate(
                    ctx.guild,
                    "commands.config.language.available_languages",
                    languages=available_languages,
                )
            )

        guild = await self.guild_repository.update(
            guild_id=guild_id,
            language=language,
        )

        if guild is None:
            return

        self.bot.guild_languages[guild_id] = language

        await ctx.send(
            translate(
                ctx.guild,
                "commands.config.language.language_changed",
                language_name=SUPPORTED_LANGUAGES[language],
                language=language,
            )
        )
