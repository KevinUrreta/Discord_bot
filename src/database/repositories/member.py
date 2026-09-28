from sqlalchemy import select

from src.core.logging import database_logger
from src.database.connection import Database
from src.database.models.member import Member


class MemberRepository:

    def __init__(self, database: Database):
        self.database = database

    async def create(
        self,
        member_id: int,
        guild_id: int,
        name: str,
        display_name: str,
        joined_at=None,
    ) -> Member:
        async with self.database.session_factory() as session:
            member = await self._get(
                session,
                member_id,
                guild_id,
            )

            if member is not None:
                database_logger.info(
                    "Miembro ya existente: %s en el servidor %s.",
                    member_id,
                    guild_id,
                )
                return member

            member = Member(
                id=member_id,
                guild_id=guild_id,
                name=name,
                display_name=display_name,
                joined_at=joined_at,
            )

            session.add(member)
            await session.commit()
            await session.refresh(member)

            database_logger.info(
                "Miembro creado: %s en el servidor %s.",
                member_id,
                guild_id,
            )

            return member

    async def get(
        self,
        member_id: int,
        guild_id: int,
    ) -> Member | None:
        async with self.database.session_factory() as session:
            return await self._get(
                session,
                member_id,
                guild_id,
            )

    async def update(
        self,
        member_id: int,
        guild_id: int,
        **values,
    ) -> Member | None:
        async with self.database.session_factory() as session:
            member = await self._get(
                session,
                member_id,
                guild_id,
            )

            if member is None:
                database_logger.warning(
                    "No se puede actualizar el miembro %s: "
                    "no existe en el servidor %s.",
                    member_id,
                    guild_id,
                )
                return None

            for key, value in values.items():
                setattr(member, key, value)

            await session.commit()
            await session.refresh(member)

            database_logger.info(
                "Miembro actualizado: %s en el servidor %s. "
                "Campos modificados: %s.",
                member_id,
                guild_id,
                ", ".join(values.keys()),
            )

            return member

    async def delete(
        self,
        member_id: int,
        guild_id: int,
    ) -> bool:
        async with self.database.session_factory() as session:
            member = await self._get(
                session,
                member_id,
                guild_id,
            )

            if member is None:
                database_logger.warning(
                    "No se puede eliminar el miembro %s: "
                    "no existe en el servidor %s.",
                    member_id,
                    guild_id,
                )
                return False

            await session.delete(member)
            await session.commit()

            database_logger.info(
                "Miembro eliminado: %s del servidor %s.",
                member_id,
                guild_id,
            )

            return True

    async def delete_by_guild(
        self,
        guild_id: int,
    ) -> int:
        async with self.database.session_factory() as session:
            result = await session.execute(
                select(Member).where(
                    Member.guild_id == guild_id
                )
            )

            members = result.scalars().all()

            for member in members:
                await session.delete(member)

            await session.commit()

            database_logger.info(
                "Miembros eliminados del servidor %s: %s.",
                guild_id,
                len(members),
            )

            return len(members)

    async def _get(
        self,
        session,
        member_id: int,
        guild_id: int,
    ) -> Member | None:
        result = await session.execute(
            select(Member).where(
                Member.id == member_id,
                Member.guild_id == guild_id,
            )
        )

        return result.scalar_one_or_none()