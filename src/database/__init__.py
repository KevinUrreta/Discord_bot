from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from src.database.models.guild import Guild
from src.database.models.member import Member

__all__ = [
    "Guild",
    "Member",
]