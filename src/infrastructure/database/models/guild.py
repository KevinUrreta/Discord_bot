import datetime

from sqlalchemy import BigInteger, Column, DateTime, Integer, String

from src.infrastructure.database import Base


class Guild(Base):
    """
    Representa un servidor de Discord almacenado en la base de datos.

    Guarda la información de configuración asociada al servidor.
    """
    __tablename__ = "guilds"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    prefix = Column(String, default="!", nullable=False)
    language = Column(String, default="es", nullable=False)
    volume = Column(Integer, default=100, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc),
        nullable=False,
    )
