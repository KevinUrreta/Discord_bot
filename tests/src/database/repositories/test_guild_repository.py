from src.database.repositories.guild import GuildRepository


async def test_create_guild(database):
    repository = GuildRepository(database)

    guild = await repository.create(
        guild_id=123456789,
        name="Servidor de prueba",
    )

    assert guild is not None
    assert guild.id == 123456789
    assert guild.name == "Servidor de prueba"

    saved_guild = await repository.get(123456789)

    assert saved_guild is not None
    assert saved_guild.id == 123456789
    assert saved_guild.name == "Servidor de prueba"


async def test_get_guild(database):
    repository = GuildRepository(database)

    await repository.create(
        guild_id=123456789,
        name="Servidor de prueba",
    )

    guild = await repository.get(123456789)

    assert guild is not None
    assert guild.id == 123456789
    assert guild.name == "Servidor de prueba"


async def test_get_nonexistent_guild(database):
    repository = GuildRepository(database)

    guild = await repository.get(999999999)

    assert guild is None


async def test_update_guild(database):
    repository = GuildRepository(database)

    await repository.create(
        guild_id=123456789,
        name="Servidor de prueba",
    )

    guild = await repository.update(
        guild_id=123456789,
        name="Servidor actualizado",
        prefix=">",
        language="en",
        volume=75,
    )

    assert guild is not None
    assert guild.name == "Servidor actualizado"
    assert guild.prefix == ">"
    assert guild.language == "en"
    assert guild.volume == 75

    saved_guild = await repository.get(123456789)

    assert saved_guild is not None
    assert saved_guild.name == "Servidor actualizado"
    assert saved_guild.prefix == ">"
    assert saved_guild.language == "en"
    assert saved_guild.volume == 75


async def test_update_nonexistent_guild(database):
    repository = GuildRepository(database)

    guild = await repository.update(
        guild_id=999999999,
        name="Servidor actualizado",
    )

    assert guild is None


async def test_delete_guild(database):
    repository = GuildRepository(database)

    await repository.create(
        guild_id=123456789,
        name="Servidor de prueba",
    )

    deleted = await repository.delete(123456789)

    assert deleted is True

    guild = await repository.get(123456789)

    assert guild is None


async def test_delete_nonexistent_guild(database):
    repository = GuildRepository(database)

    deleted = await repository.delete(999999999)

    assert deleted is False


async def test_create_existing_guild(database):
    repository = GuildRepository(database)

    guild = await repository.create(
        guild_id=123456789,
        name="Servidor de prueba",
    )

    updated_guild = await repository.create(
        guild_id=123456789,
        name="Servidor actualizado",
    )

    assert guild.id == updated_guild.id
    assert updated_guild.name == "Servidor actualizado"

    saved_guild = await repository.get(123456789)

    assert saved_guild is not None
    assert saved_guild.name == "Servidor actualizado"