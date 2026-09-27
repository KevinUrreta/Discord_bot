from sqlalchemy import select

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
                return None

            for key, value in values.items():
                setattr(member, key, value)

            await session.commit()
            await session.refresh(member)

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
                return False

            await session.delete(member)
            await session.commit()

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
