import discord

from src.i18n.translator import get_nested_translation, get_translations


def create_embed(
    guild,
    key: str,
    *,
    color: discord.Color = discord.Color.purple(),
    timestamp: bool = True,
    thumbnail: str | None = None,
    footer_icon: str | None = None,
    **kwargs,
) -> discord.Embed:
    """
    Crea un `Embed` y lo devuelve con los valores proporcionados.

    :param guild: Server asociado al Embed.
    :param key: Clave jerárquica para la traducción.
    :param color: Color del Embed
    :param timestamp: Fecha en la que se envía el mensaje
    :param thumbnail: URL de imagen como miniatura.
    :param footer_icon: URL de imagen como pie de página.
    :param kwargs:
    :raises ValueError: Si no hay traducción
    :return: Embed configurado con valores.
    """
    translations = get_translations(guild)

    data = get_nested_translation(translations, key)

    if not isinstance(data, dict):
        raise ValueError(f"Embed translation '{key}' does not exist.")

    embed = discord.Embed(color=color)

    if timestamp:
        embed.timestamp = discord.utils.utcnow()

    title = data.get("title")
    if title:
        embed.title = title.format(**kwargs)

    description = data.get("description")
    if description:
        embed.description = description.format(**kwargs)

    for field in data.get("fields", []):
        embed.add_field(
            name=field["name"].format(**kwargs),
            value=field["value"].format(**kwargs),
            inline=field.get("inline", False),
        )

    footer = data.get("footer")

    if isinstance(footer, dict):
        text = footer.get("text")

        if text:
            embed.set_footer(text=text.format(**kwargs), icon_url=footer_icon)

    if thumbnail:
        embed.set_thumbnail(url=thumbnail)

    return embed