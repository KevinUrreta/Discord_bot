import logging
import os

os.makedirs("logs", exist_ok=True)

formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
)

file_handler = logging.FileHandler(
    "logs/bot.log",
    encoding="utf-8",
)

file_handler.setFormatter(formatter)

stream = logging.StreamHandler()
stream.setFormatter(formatter)


logger = logging.getLogger("music_bot")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(stream)


discord_logger = logging.getLogger("discord")
discord_logger.setLevel(logging.INFO)
discord_logger.addHandler(file_handler)
discord_logger.addHandler(stream)


wavelink_logger = logging.getLogger("wavelink")
wavelink_logger.setLevel(logging.INFO)
wavelink_logger.addHandler(file_handler)
wavelink_logger.addHandler(stream)