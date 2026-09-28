import datetime

from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String

from src.database import Base


class Member(Base):
    __tablename__ = "guild_members"

    id = Column(BigInteger, primary_key=True)
    guild_id = Column(
        BigInteger,
        ForeignKey("guilds.id"),
        primary_key=True,
    )
    name = Column(String, nullable=False)
    display_name = Column(String, nullable=False)
    joined_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc),
        nullable=False,
    )