import discord
from discord.ext import commands

from src.core.logging import logger
from src.i18n.translator import translate


class On_message(commands.Cog):
    """
    Gestiona el evento al recibir un mensaje.
    """
    def __init__(self, bot):
        """
        Inicializa el evento.

        :param bot: Instancia principal del app de Discord.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """
        Procesa y registra los mensajes recibidos en los servers.

        :param message:
        :return:
        """
        if message.author == self.bot.user:
            return

        if message.guild is None:
            return

        channel_name = getattr(message.channel, "name", "DM")

        if message.embeds:
            embed_messages = []

            for embed in message.embeds:
                embed_info = []

                if embed.title:
                    embed_info.append(
                        f"Título: {embed.title}"
                    )

                if embed.description:
                    embed_info.append(
                        f"Descripción: {embed.description}"
                    )

                if embed.url:
                    embed_info.append(
                        f"URL: {embed.url}"
                    )

                if embed.type:
                    embed_info.append(
                        f"Tipo: {embed.type}"
                    )

                if embed.author.name:
                    author_info = embed.author.name

                    if embed.author.url:
                        author_info += f" ({embed.author.url})"

                    embed_info.append(
                        f"Autor: {author_info}"
                    )

                for field in embed.fields:
                    embed_info.append(
                        f"Campo: {field.name} = {field.value}"
                    )

                if embed.footer.text:
                    footer_info = embed.footer.text

                    if embed.footer.icon_url:
                        footer_info += (
                            f" ({embed.footer.icon_url})"
                        )

                    embed_info.append(
                        f"Pie: {footer_info}"
                    )

                if embed.thumbnail.url:
                    embed_info.append(
                        f"Thumbnail: {embed.thumbnail.url}"
                    )

                if embed.image.url:
                    embed_info.append(
                        f"Imagen: {embed.image.url}"
                    )

                if embed.timestamp:
                    embed_info.append(
                        f"Fecha: {embed.timestamp}"
                    )

                embed_messages.append(
                    " | ".join(embed_info)
                )

            message_content = " || ".join(
                embed_messages
            )

        else:
            message_content = message.content

        logger.info(
            translate(
                None,
                "app.events.logs.message.on_message.message_detected",
                server_name=message.guild.name,
                channel_name=channel_name,
                author_name=message.author.name,
                message=message_content,
            )
        )