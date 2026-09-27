import datetime

from sqlalchemy import BigInteger, Column, DateTime, Integer, String

from src.database import Base


class Guild(Base):
    __tablename__ = "guilds"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    prefix = Column(String, default="!", nullable=False)
    language = Column(String, default="es", nullable=False)
    volume = Column(Integer, default=100, nullable=False)
    created_at = Column(
        DateTime,
        default=datetime.datetime.now(datetime.timezone.utc),
        nullable=False,
    )