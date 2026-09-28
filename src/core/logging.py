import logging
import os


os.makedirs("logs", exist_ok=True)


formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
)


stream = logging.StreamHandler()
stream.setFormatter(formatter)


# ─────────────────────────────
# Bot
# ─────────────────────────────

bot_file_handler = logging.FileHandler(
    "logs/bot.log",
    encoding="utf-8",
)
bot_file_handler.setFormatter(formatter)


logger = logging.getLogger("music_bot")
logger.setLevel(logging.INFO)
logger.addHandler(bot_file_handler)
logger.addHandler(stream)


# ─────────────────────────────
# Wavelink
# ─────────────────────────────

wavelink_file_handler = logging.FileHandler(
    "logs/wavelink.log",
    encoding="utf-8",
)
wavelink_file_handler.setFormatter(formatter)


wavelink_logger = logging.getLogger("wavelink")
wavelink_logger.setLevel(logging.INFO)
wavelink_logger.addHandler(wavelink_file_handler)
wavelink_logger.addHandler(stream)


# ─────────────────────────────
# Discord
# ─────────────────────────────

discord_file_handler = logging.FileHandler(
    "logs/discord.log",
    encoding="utf-8",
)
discord_file_handler.setFormatter(formatter)


discord_logger = logging.getLogger("discord")
discord_logger.setLevel(logging.INFO)
discord_logger.addHandler(discord_file_handler)
discord_logger.addHandler(stream)


# ─────────────────────────────
# Database
# ─────────────────────────────

database_file_handler = logging.FileHandler(
    "logs/database.log",
    encoding="utf-8",
)
database_file_handler.setFormatter(formatter)


database_logger = logging.getLogger("database")
database_logger.setLevel(logging.INFO)
database_logger.addHandler(database_file_handler)
database_logger.addHandler(stream)


# ─────────────────────────────
# Errores
# ─────────────────────────────

errors_file_handler = logging.FileHandler(
    "logs/errors.log",
    encoding="utf-8",
)
errors_file_handler.setLevel(logging.ERROR)
errors_file_handler.setFormatter(formatter)


errors_logger = logging.getLogger("errors")
errors_logger.setLevel(logging.ERROR)
errors_logger.addHandler(errors_file_handler)
errors_logger.addHandler(stream)