from sqlalchemy import select

from src.database.connection import Database
from src.database.models.guild import Guild


class GuildRepository:

    def __init__(self, database: Database):
        self.database = database

    async def create(self, guild_id: int, name: str) -> Guild:
        async with self.database.session_factory() as session:
            guild = Guild(
                id=guild_id,
                name=name,
            )

            session.add(guild)
            await session.commit()
            await session.refresh(guild)

            return guild

    async def get(self, guild_id: int) -> Guild | None:
        async with self.database.session_factory() as session:
            result = await session.execute(
                select(Guild).where(Guild.id == guild_id)
            )

            return result.scalar_one_or_none()

    async def update(self, guild_id: int, **values) -> Guild | None:
        async with self.database.session_factory() as session:
            guild = await self._get(session, guild_id)

            if guild is None:
                return None

            for key, value in values.items():
                setattr(guild, key, value)

            await session.commit()
            await session.refresh(guild)

            return guild

    async def delete(self, guild_id: int) -> bool:
        async with self.database.session_factory() as session:
            guild = await self._get(session, guild_id)

            if guild is None:
                return False

            await session.delete(guild)
            await session.commit()

            return True

    async def _get(self, session, guild_id: int) -> Guild | None:
        result = await session.execute(
            select(Guild).where(Guild.id == guild_id)
        )

        return result.scalar_one_or_none()