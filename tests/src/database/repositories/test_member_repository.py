from datetime import datetime, timezone

from src.database.repositories.member import MemberRepository


async def test_create_member(database):
    repository = MemberRepository(database)

    joined_at = datetime.now(timezone.utc)

    member = await repository.create(
        member_id=123456789,
        guild_id=987654321,
        name="Kevin",
        display_name="Kevin",
        joined_at=joined_at,
    )

    assert member is not None
    assert member.id == 123456789
    assert member.guild_id == 987654321
    assert member.name == "Kevin"
    assert member.display_name == "Kevin"

    saved_member = await repository.get(
        member_id=123456789,
        guild_id=987654321,
    )

    assert saved_member is not None
    assert saved_member.id == 123456789
    assert saved_member.guild_id == 987654321
    assert saved_member.name == "Kevin"
    assert saved_member.display_name == "Kevin"


async def test_get_member(database):
    repository = MemberRepository(database)

    await repository.create(
        member_id=123456789,
        guild_id=987654321,
        name="Kevin",
        display_name="Kevin",
        joined_at=None,
    )

    member = await repository.get(
        member_id=123456789,
        guild_id=987654321,
    )

    assert member is not None
    assert member.id == 123456789
    assert member.guild_id == 987654321
    assert member.name == "Kevin"
    assert member.display_name == "Kevin"


async def test_get_nonexistent_member(database):
    repository = MemberRepository(database)

    member = await repository.get(
        member_id=999999999,
        guild_id=987654321,
    )

    assert member is None


async def test_update_member(database):
    repository = MemberRepository(database)

    await repository.create(
        member_id=123456789,
        guild_id=987654321,
        name="Kevin",
        display_name="Kevin",
        joined_at=None,
    )

    member = await repository.update(
        member_id=123456789,
        guild_id=987654321,
        name="KevinUpdated",
        display_name="Kevin Updated",
    )

    assert member is not None
    assert member.name == "KevinUpdated"
    assert member.display_name == "Kevin Updated"

    saved_member = await repository.get(
        member_id=123456789,
        guild_id=987654321,
    )

    assert saved_member is not None
    assert saved_member.name == "KevinUpdated"
    assert saved_member.display_name == "Kevin Updated"


async def test_update_nonexistent_member(database):
    repository = MemberRepository(database)

    member = await repository.update(
        member_id=999999999,
        guild_id=987654321,
        name="KevinUpdated",
    )

    assert member is None


async def test_delete_member(database):
    repository = MemberRepository(database)

    await repository.create(
        member_id=123456789,
        guild_id=987654321,
        name="Kevin",
        display_name="Kevin",
        joined_at=None,
    )

    deleted = await repository.delete(
        member_id=123456789,
        guild_id=987654321,
    )

    assert deleted is True

    member = await repository.get(
        member_id=123456789,
        guild_id=987654321,
    )

    assert member is None


async def test_delete_nonexistent_member(database):
    repository = MemberRepository(database)

    deleted = await repository.delete(
        member_id=999999999,
        guild_id=987654321,
    )

    assert deleted is False


async def test_create_existing_member(database):
    repository = MemberRepository(database)

    member = await repository.create(
        member_id=123456789,
        guild_id=987654321,
        name="Kevin",
        display_name="Kevin",
        joined_at=None,
    )

    existing_member = await repository.create(
        member_id=123456789,
        guild_id=987654321,
        name="Otro nombre",
        display_name="Otro nombre",
        joined_at=None,
    )

    assert existing_member is not None
    assert existing_member.id == member.id
    assert existing_member.guild_id == member.guild_id
    assert existing_member.name == "Kevin"
    assert existing_member.display_name == "Kevin"


async def test_delete_by_guild(database):
    repository = MemberRepository(database)

    await repository.create(
        member_id=111111111,
        guild_id=987654321,
        name="Kevin",
        display_name="Kevin",
        joined_at=None,
    )

    await repository.create(
        member_id=222222222,
        guild_id=987654321,
        name="Usuario2",
        display_name="Usuario 2",
        joined_at=None,
    )

    await repository.create(
        member_id=333333333,
        guild_id=123456789,
        name="Usuario3",
        display_name="Usuario 3",
        joined_at=None,
    )

    deleted_count = await repository.delete_by_guild(
        guild_id=987654321,
    )

    assert deleted_count == 2

    member_one = await repository.get(
        member_id=111111111,
        guild_id=987654321,
    )

    member_two = await repository.get(
        member_id=222222222,
        guild_id=987654321,
    )

    member_three = await repository.get(
        member_id=333333333,
        guild_id=123456789,
    )

    assert member_one is None
    assert member_two is None
    assert member_three is not None