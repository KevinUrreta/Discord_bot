from datetime import timezone
from typing import cast

from sqlalchemy import select

from src.core.logging import database_logger
from src.infrastructure.database.connection import Database
from src.infrastructure.database.models.member import Member
from src.i18n.translator import translate


class MemberRepository:
    """
    Gestiona operaciones con la tabla de Miembros de la base de datos.
    Permite CRUD, create, read, update, delete miembros.
    """

    def __init__(self, database: Database):
        """
        Inicializa el repositorio de miembros.

        :param database: Instancia encargada de gestionar la conexión y sesiones.
        """
        self.database = database

    async def create(
            self,
            member_id: int,
            guild_id: int,
            name: str,
            display_name: str,
            joined_at=None,
            source: str | None = None,
    ) -> Member:
        """
        Crea un miembro o actualiza sus datos si ya existe.

        :param member_id: ID del usuario.
        :param guild_id: ID del server al que se le asocia.
        :param name: Nombre del usuario
        :param display_name: Mote del usuario.
        :param joined_at: Fecha de unión al server del usuario.
        :param source:
        :return: Miembro con los datos aportados.
        """
        async with self.database.session_factory() as session:
            member = await self._get(
                session,
                member_id,
                guild_id,
            )

            if member is not None:
                current_name = cast(str, member.name)
                current_display_name = cast(
                    str,
                    member.display_name,
                )
                current_joined_at = member.joined_at

                if current_joined_at is not None and current_joined_at.tzinfo is None:
                    current_joined_at = current_joined_at.replace(tzinfo=timezone.utc)

                if joined_at is not None and joined_at.tzinfo is None:
                    joined_at = joined_at.replace(tzinfo=timezone.utc)

                changes = []

                if current_name != name:
                    changes.append(f"name: {current_name} -> {name}")
                    setattr(member, "name", name)

                if current_display_name != display_name:
                    changes.append(
                        f"display_name: "
                        f"{current_display_name} -> "
                        f"{display_name}"
                    )
                    setattr(
                        member,
                        "display_name",
                        display_name,
                    )

                if current_joined_at != joined_at:
                    changes.append(
                        f"joined_at: "
                        f"{current_joined_at} -> "
                        f"{joined_at}"
                    )
                    setattr(
                        member,
                        "joined_at",
                        joined_at,
                    )

                if not changes:
                    return member

                await session.commit()
                await session.refresh(member)

                database_logger.info(
                    translate(
                        None,
                        "database.logs.update.member",
                        id=member_id,
                        name=current_name,
                        changes=", ".join(changes),
                        guild_id=guild_id,
                        source=f" | {source}" if source else "",
                    )
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
                translate(
                    None,
                    "database.logs.insert.member",
                    id=member_id,
                    name=name,
                    guild_id=guild_id,
                    source=f" | {source}" if source else "",
                )
            )

            return member
    async def get(self, member_id: int, guild_id: int) -> Member | None:
        """
        Busca un miembro por su identificador y el servidor al que pertenece.

        :param member_id: ID del usuario
        :param guild_id: ID del server al que pertenece
        :return: Miembro encontrado o None
        """
        async with self.database.session_factory() as session:
            return await self._get(
                session,
                member_id,
                guild_id,
            )

    async def update(self, member_id: int, guild_id: int, source: str | None = None, **values) -> Member | None:
        """
        Actualiza los campos de un miembro existente.

        :param member_id: ID del usuario
        :param guild_id: ID del servidor al que pertenece
        :param source: Origen de la operación, utilizado en los registros.
        :param values: Campos del miembro que se desean actualizar.
        :return: El miembro actualizado, el miembro sin cambios o None si no existe.
        """
        async with self.database.session_factory() as session:
            member = await self._get(session, member_id, guild_id)

            if member is None:
                return None

            member_name = cast(str, member.name)
            changes = []

            for key, value in values.items():
                current_value = getattr(member, key)

                if current_value != value:
                    changes.append(f"{key}: {current_value} -> {value}")
                    setattr(member, key, value)

            if not changes:
                return member

            await session.commit()
            await session.refresh(member)

            database_logger.info(
                translate(
                    None,
                    "database.logs.update.member",
                    id=member_id,
                    name=member_name,
                    changes=", ".join(changes),
                    guild_id=guild_id,
                    source=f" | {source}" if source else "",
                )
            )

            return member

    async def delete(self, member_id: int, guild_id: int, source: str | None = None) -> bool:
        """
        Elimina el miembro de la tabla.

        :param member_id: ID del miembro.
        :param guild_id: ID del servidor.
        :param source: Origen de la operación.
        :return: True o False en la eliminación.
        """
        async with self.database.session_factory() as session:
            member = await self._get(session, member_id, guild_id)

            if member is None:
                return False

            member_name = cast(str, member.name)

            await session.delete(member)
            await session.commit()

            database_logger.info(
                translate(
                    None,
                    "database.logs.delete.member",
                    id=member_id,
                    name=member_name,
                    guild_id=guild_id,
                    source=f" | {source}" if source else "",
                )
            )

            return True

    async def delete_by_guild(self, guild_id: int, source: str | None = None) -> int:
        """
        Elimina los miembros de un server.

        :param guild_id: ID del server.
        :param source: Origen de la operación.
        :return: N.º de usuarios eliminados o 0.
        """
        async with self.database.session_factory() as session:
            result = await session.execute(
                select(Member).where(Member.guild_id == guild_id)
            )

            members = result.scalars().all()

            for member in members:
                await session.delete(member)

            if not members:
                return 0

            await session.commit()

            for member in members:
                member_name = cast(str, member.name)

                database_logger.info(
                    translate(
                        None,
                        "database.logs.delete.member",
                        id=member.id,
                        name=member_name,
                        guild_id=guild_id,
                        source=f" | {source}" if source else "",
                    )
                )

            return len(members)

    async def _get(self, session, member_id: int, guild_id: int, ) -> Member | None:
        """
        Busca a un miembro de un server.

        :param session: Sesión activa de SQLAlchemy
        :param member_id: ID del usuario.
        :param guild_id: ID del servidor.
        :return: Miembro encontrado o None.
        """
        result = await session.execute(
            select(Member).where(
                Member.id == member_id,
                Member.guild_id == guild_id,
            )
        )

        return result.scalar_one_or_none()