from typing import cast

from sqlalchemy import select

from src.core.logging import database_logger
from src.database.connection import Database
from src.database.models.guild import Guild


class GuildRepository:

    def __init__(self, database: Database):
        self.database = database

    async def create(
        self,
        guild_id: int,
        name: str,
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
                        "Nombre del servidor actualizado: %s (%s).",
                        name,
                        guild_id,
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
                "Servidor creado: %s (%s).",
                name,
                guild_id,
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
        **values,
    ) -> Guild | None:
        async with self.database.session_factory() as session:
            guild = await self._get(
                session,
                guild_id,
            )

            if guild is None:
                database_logger.warning(
                    "No se puede actualizar el servidor %s: "
                    "no existe.",
                    guild_id,
                )
                return None

            for key, value in values.items():
                setattr(guild, key, value)

            await session.commit()
            await session.refresh(guild)

            database_logger.info(
                "Servidor actualizado: %s. Campos modificados: %s.",
                guild_id,
                ", ".join(values.keys()),
            )

            return guild

    async def delete(
        self,
        guild_id: int,
    ) -> bool:
        async with self.database.session_factory() as session:
            guild = await self._get(
                session,
                guild_id,
            )

            if guild is None:
                database_logger.warning(
                    "No se puede eliminar el servidor %s: "
                    "no existe.",
                    guild_id,
                )
                return False

            await session.delete(guild)
            await session.commit()

            database_logger.info(
                "Servidor eliminado: %s.",
                guild_id,
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