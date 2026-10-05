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