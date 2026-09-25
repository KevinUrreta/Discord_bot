# import asyncio
# import os
# from dotenv import load_dotenv
# import sys
# import logging
# from typing import Any

# import discord
# import yt_dlp as youtube_dl   # pyright: ignore[reportMissingModuleSource]
# from discord.ext import commands

# # -----------------------------------------------------------------------------
# # CONFIGURACIÓN DEL LOGGER
# # -----------------------------------------------------------------------------
# # Asegurar que la carpeta de logs exista dentro del contenedor Docker
# os.makedirs("logs", exist_ok=True)

# logger = logging.getLogger('music_bot')
# logger.setLevel(logging.INFO)

# # Formato de los mensajes: [Fecha/Hora] [Nivel] [Componente]: Mensaje
# formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(name)s: %(message)s')

# # Manejador 1: Escribir en un archivo físico (Se guardará en tu volumen de Docker)
# file_handler = logging.FileHandler('logs/bot.log', encoding='utf-8')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# # Manejador 2: Mostrar en la terminal de Docker (stdout)
# stream_handler = logging.StreamHandler(sys.stdout)
# stream_handler.setFormatter(formatter)
# logger.addHandler(stream_handler)

# # Integrar también los logs internos de discord.py para capturar errores de conexión
# discord_logger = logging.getLogger('discord')
# discord_logger.setLevel(logging.INFO)
# discord_logger.addHandler(file_handler)
# discord_logger.addHandler(stream_handler)

# logger.info("Iniciando el bot de música...")

# # -----------------------------------------------------------------------------
# # CARGA DE ENTORNO DE VOZ (OPUS)
# # -----------------------------------------------------------------------------
# if not discord.opus.is_loaded():
#     try:
#         if sys.platform == 'win32':
#             import ctypes.util
#             opus_path = ctypes.util.find_library('libopus')
#             if opus_path:
#                 discord.opus.load_opus(opus_path)
#                 logger.info(f"Opus cargado correctamente en Windows desde: {opus_path}")
#         else:
#             discord.opus.load_opus('libopus.so.0')
#             logger.info("Opus cargado correctamente en entorno Linux/Docker.")
#     except Exception as e:
#         logger.error(f"Error crítico al cargar la librería de audio Opus: {e}")

# # -----------------------------------------------------------------------------
# # CONFIGURACIÓN DE AUDIO (YT-DLP)
# # -----------------------------------------------------------------------------
# ytdl_format_options = {
#     'format': 'bestaudio/best',
#     'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
#     'restrictfilenames': True,
#     'noplaylist': True,
#     'nocheckcertificate': True,
#     'ignoreerrors': False,
#     'logtostderr': False,
#     'quiet': True,
#     'no_warnings': True,
#     'default_search': 'auto',
#     'source_address': '0.0.0.0',  
# }

# ytdl = youtube_dl.YoutubeDL(ytdl_format_options) # type: ignore


# class YTDLSource(discord.PCMVolumeTransformer):
#     def __init__(self, source: Any, *, data: Any, volume: float = 0.5):
#         super().__init__(source, volume)
#         self.data = data
#         self.title = data.get('title')
#         self.url = data.get('url')

#     @classmethod
#     async def from_url(cls, url: str, *, loop: Any = None, stream: bool = False):
#         loop = loop or asyncio.get_event_loop()
#         logger.info(f"Extrayendo información de la URL (Stream={stream}): {url}")
        
#         data: Any = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

#         if 'entries' in data and data['entries']:
#             data = data['entries'][0]

#         filename = data.get('url') if stream else ytdl.prepare_filename(data)
#         if filename is None:
#             filename = ""

#         # Opciones avanzadas para evitar que YouTube corte el streaming a la mitad
#         ffmpeg_options = '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'

#         logger.info(f"Origen de audio preparado. Archivo/Stream: {filename}")
#         return cls(
#             discord.FFmpegPCMAudio(
#                 str(filename), 
#                 options='-vn', 
#                 before_options=ffmpeg_options
#             ), 
#             data=data
#         )


# class Music(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot

#     @commands.Cog.listener()
#     async def on_command(self, ctx):
#         # Este listener registrará CUALQUIER comando que el bot detecte
#         logger.info(f"Comando ejecutado: '{ctx.command.name}' por el usuario {ctx.author} en el canal #{ctx.channel}")

#     @commands.Cog.listener()
#     async def on_command_error(self, ctx, error):
#         # Este listener capturará fallos internos de los comandos
#         logger.error(f"Error en comando '{ctx.command}': {error}", exc_info=True)

#     @commands.command()
#     async def join(self, ctx, *, channel: discord.VoiceChannel):
#         """Joins a voice channel"""
#         logger.info(f"Intentando unirse al canal de voz: {channel.name}")
#         if ctx.voice_client is not None:
#             return await ctx.voice_client.move_to(channel)
#         await channel.connect()
#         logger.info(f"Conectado con éxito a: {channel.name}")

#     @commands.command(name="play", aliases=["p"])
#     async def play(self, ctx, *, url):
#         """Streams from a url"""
#         async with ctx.typing():
#             loop = asyncio.get_running_loop()
#             player = await YTDLSource.from_url(url, loop=loop, stream=True)
#             ctx.voice_client.play(player, after=lambda e: logger.error(f'Error de reproducción: {e}') if e else None)
#         await ctx.send(f'Now playing: {player.title}')

#     @commands.command()
#     async def volume(self, ctx, volume: int):
#         """Changes the player's volume"""
#         if ctx.voice_client is None:
#             return await ctx.send('Not connected to a voice channel.')
#         ctx.voice_client.source.volume = volume / 100
#         await ctx.send(f'Changed volume to {volume}%')

#     @commands.command()
#     async def stop(self, ctx):
#         """Stops and disconnects the bot from voice"""
#         logger.info("Desconectando el bot del canal de voz por comando stop.")
#         await ctx.voice_client.disconnect()

#     @play.before_invoke
#     async def ensure_voice(self, ctx):
#         logger.info("Ejecutando comprobación previa 'ensure_voice'...")
#         if ctx.voice_client is None:
#             if ctx.author.voice:
#                 logger.info(f"El autor está en un canal. Conectando al bot a: {ctx.author.voice.channel.name}")
#                 await ctx.author.voice.channel.connect()
#             else:
#                 await ctx.send('You are not connected to a voice channel.')
#                 logger.warning(f"Comando rechazado: {ctx.author} no está en un canal de voz.")
#                 raise commands.CommandError('Author not connected to a voice channel.')
#         elif ctx.voice_client.is_playing():
#             logger.info("El reproductor estaba activo. Deteniendo pista anterior.")
#             ctx.voice_client.stop()


# # -----------------------------------------------------------------------------
# # INICIALIZACIÓN DEL BOT
# # -----------------------------------------------------------------------------
# intents = discord.Intents.default()
# intents.message_content = True  
# intents.guilds = True           
# intents.voice_states = True     

# bot = commands.Bot(
#     command_prefix='!',         
#     description='Relatively simple music bot example',
#     intents=intents,
# )


# @bot.event
# async def on_ready():
#     assert bot.user is not None
#     logger.info(f'¡Bot conectado con éxito! Identificado como: {bot.user} (ID: {bot.user.id})')


# @bot.event
# async def on_message(message):
#     # Imprime en los logs cada vez que el bot ve pasar un mensaje de texto
#     if message.author == bot.user:
#         return
#     logger.info(f"Mensaje detectado en el chat -> [{message.author.name}]: {message.content}")
#     await bot.process_commands(message)


# async def main():
#     async with bot:
#         await bot.add_cog(Music(bot))
#         # Intentará leer el Token de tu archivo .env de Docker. Si no existe, usa un string de respaldo.
#         load_dotenv(dotenv_path='config/.env')
#         TOKEN :str | None = str(os.getenv("DISCORD_TOKEN"))
#         await bot.start(TOKEN)


# if __name__ == "__main__":
#     asyncio.run(main())
