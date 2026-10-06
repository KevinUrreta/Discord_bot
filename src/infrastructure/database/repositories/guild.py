from typing import cast

from sqlalchemy import select

from src.core.logging import database_logger
from src.i18n.translator import translate
from src.infrastructure.database.connection import Database
from src.infrastructure.database.models.guild import Guild


class GuildRepository:
    """
    Gestiona las operaciones relacionadas con los servers almacenados en la base de datos.
    Permite CRUD, create, read, update, delete servers.
    """

    def __init__(self, database: Database):
        """
        Inicializa el repositorio de servers.
        :param database: Instancia encargada de gestionar la conexión y las sesiones de la base de datos.
        """
        self.database = database

    async def create(self, guild_id: int, name: str, source: str | None = None) -> Guild:
        """
        Crea un servidor o actualiza su nombre si ya existe.

        :param guild_id: ID del server.
        :param name: Nombre del servidor.
        :param source: Origen de la operación.
        :return: Instancia del servidor creado o existente.
        """
        async with self.database.session_factory() as session:
            guild = await self._get(session, guild_id)

            if guild is not None:
                current_name = cast(str, guild.name)

                if current_name != name:
                    setattr(guild, "name", name)

                    await session.commit()
                    await session.refresh(guild)

                    database_logger.info(
                        translate(
                            None,
                            "database.logs.update.guild",
                            id=guild_id,
                            name=current_name,
                            changes=f"name: {current_name} -> {name}",
                            source=f" | {source}" if source else "",
                        )
                    )

                return guild

            guild = Guild(id=guild_id, name=name)

            session.add(guild)
            await session.commit()
            await session.refresh(guild)

            database_logger.info(
                translate(
                    None,
                    "database.logs.insert.guild",
                    id=guild_id,
                    name=name,
                    source=f" | {source}" if source else "",
                )
            )

            return guild

    async def get(self, guild_id: int) -> Guild | None:
        """
        Busca un server por su ID.
        :param guild_id: ID del servidor.
        :return: Server encontrado o None.
        """
        async with self.database.session_factory() as session:
            return await self._get(session, guild_id)

    async def update(self, guild_id: int, source: str | None = None, **values) -> Guild | None:
        """
        Actualiza los campos indicados de un server existente.

        :param guild_id: ID del server.
        :param source: Origen de la operacion.
        :param values: Campos que se desean actualizar.
        :return: El server actualizado, el server sin cambios o None.
        """
        async with self.database.session_factory() as session:
            guild = await self._get(session, guild_id)

            if guild is None:
                return None

            guild_name = cast(str, guild.name)
            changes = []

            for key, value in values.items():
                current_value = getattr(guild, key)

                if current_value != value:
                    changes.append(f"{key}: {current_value} -> {value}")
                    setattr(guild, key, value)

            if not changes:
                return guild

            await session.commit()
            await session.refresh(guild)

            database_logger.info(
                translate(
                    None,
                    "database.logs.update.guild",
                    id=guild_id,
                    name=guild_name,
                    changes=", ".join(changes),
                    source=f" | {source}" if source else "",
                )
            )

            return guild

    async def delete(self, guild_id: int, source: str | None = None) -> bool:
        """
        Elimina un servidor de la base de datos.

        :param guild_id: ID del server.
        :param source: Origen de la operacion.
        :return: True o False.
        """
        async with self.database.session_factory() as session:
            guild = await self._get(session, guild_id)

            if guild is None:
                return False

            guild_name = cast(str, guild.name)

            await session.delete(guild)
            await session.commit()

            database_logger.info(
                translate(
                    None,
                    "database.logs.delete.guild",
                    id=guild_id,
                    name=guild_name,
                    source=f" | {source}" if source else "",
                )
            )

            return True

    async def _get(self, session, guild_id: int) -> Guild | None:
        """
        Busca un servidor utilizando una sesión existente.

        :param session: Sesión activa de SQLAlchemy.
        :param guild_id: ID del server.
        :return: Server encontrado o None.
        """
        result = await session.execute(
            select(Guild).where(Guild.id == guild_id)
        )

        return result.scalar_one_or_none()
