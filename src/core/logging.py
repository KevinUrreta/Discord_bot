import logging
import os


os.makedirs("logs", exist_ok=True)


handler = logging.FileHandler(
    "logs/bot.log",
    encoding="utf-8",
)

handler.setFormatter(
    logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
    )
)


logger = logging.getLogger("music_bot")
logger.setLevel(logging.INFO)
logger.addHandler(handler)


discord_logger = logging.getLogger("discord")
discord_logger.setLevel(logging.INFO)
discord_logger.addHandler(handler)


wavelink_logger = logging.getLogger("wavelink")
wavelink_logger.setLevel(logging.INFO)
wavelink_logger.addHandler(handler)