from datetime import datetime, timezone


def normalize_datetime(value: datetime) -> datetime:
    """
    Formatea el formato de un datetime.
    :param value: Fecha datetime.
    :return: Devuelve datetime reformateado.
    """
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)

    return value.astimezone(timezone.utc)


def format_duration(milliseconds):
    """
    Convierte una duración expresada en milisegundos a minutos y segundos.

    :param milliseconds: Duración del recurso en milisegundos
    :return: Duración formateada como minutos y segundos
    """
    total_seconds = int(milliseconds / 1000)
    minutes, seconds = divmod(total_seconds, 60)

    return f"{minutes}:{seconds:02d}"
