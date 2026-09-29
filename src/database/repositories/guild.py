from typing import cast

from sqlalchemy import select

from src.core.logging import database_logger
from src.database.connection import Database
from src.database.models.guild import Guild
from src.locales.i18n import translate


class GuildRepository:

    def __init__(self, database: Database):
        self.database = database

    async def create(
        self,
        guild_id: int,
        name: str,
        source: str | None = None,
    ) -> Guild:
        async with self.database.session_factory() as session:
            guild = await self._get(
                session,
                guild_id,
            )

            if guild is not None:
                current_name = cast(str, guild.name)

                if current_name != name:
                    setattr(guild, "name", name)

                    await session.commit()
                    await session.refresh(guild)

                    database_logger.info(
                        translate(
                            None,
                            "database.update.guild",
                            id=guild_id,
                            name=current_name,
                            changes=f"name: {current_name} → {name}",
                            source=f" | {source}" if source else "",
                        )
                    )

                return guild

            guild = Guild(
                id=guild_id,
                name=name,
            )

            session.add(guild)
            await session.commit()
            await session.refresh(guild)

            database_logger.info(
                translate(
                    None,
                    "database.insert.guild",
                    id=guild_id,
                    name=name,
                    source=f" | {source}" if source else "",
                )
            )

            return guild

    async def get(
        self,
        guild_id: int,
    ) -> Guild | None:
        async with self.database.session_factory() as session:
            return await self._get(
                session,
                guild_id,
            )

    async def update(
        self,
        guild_id: int,
        source: str | None = None,
        **values,
    ) -> Guild | None:
        async with self.database.session_factory() as session:
            guild = await self._get(
                session,
                guild_id,
            )

            if guild is None:
                return None

            guild_name = cast(str, guild.name)
            changes = []

            for key, value in values.items():
                current_value = getattr(guild, key)

                if current_value != value:
                    changes.append(
                        f"{key}: {current_value} → {value}"
                    )
                    setattr(guild, key, value)

            if not changes:
                return guild

            await session.commit()
            await session.refresh(guild)

            database_logger.info(
                translate(
                    None,
                    "database.update.guild",
                    id=guild_id,
                    name=guild_name,
                    changes=", ".join(changes),
                    source=f" | {source}" if source else "",
                )
            )

            return guild

    async def delete(
        self,
        guild_id: int,
        source: str | None = None,
    ) -> bool:
        async with self.database.session_factory() as session:
            guild = await self._get(
                session,
                guild_id,
            )

            if guild is None:
                return False

            guild_name = cast(str, guild.name)

            await session.delete(guild)
            await session.commit()

            database_logger.info(
                translate(
                    None,
                    "database.delete.guild",
                    id=guild_id,
                    name=guild_name,
                    source=f" | {source}" if source else "",
                )
            )

            return True

    async def _get(
        self,
        session,
        guild_id: int,
    ) -> Guild | None:
        result = await session.execute(
            select(Guild).where(
                Guild.id == guild_id
            )
        )

        return result.scalar_one_or_none()