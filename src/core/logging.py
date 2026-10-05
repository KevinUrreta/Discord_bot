import logging
import os

os.makedirs("logs", exist_ok=True)

formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
)

stream = logging.StreamHandler()
stream.setFormatter(formatter)

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

bot_file_handler = logging.FileHandler(
    "logs/bot.log",
    encoding="utf-8",
)
bot_file_handler.setLevel(logging.INFO)
bot_file_handler.setFormatter(formatter)

logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)
logger.addHandler(bot_file_handler)
logger.addHandler(errors_file_handler)
logger.addHandler(stream)

wavelink_file_handler = logging.FileHandler(
    "logs/wavelink.log",
    encoding="utf-8",
)
wavelink_file_handler.setLevel(logging.INFO)
wavelink_file_handler.setFormatter(formatter)

wavelink_logger = logging.getLogger("wavelink")
wavelink_logger.setLevel(logging.INFO)
wavelink_logger.addHandler(wavelink_file_handler)
wavelink_logger.addHandler(errors_file_handler)
wavelink_logger.addHandler(stream)

database_file_handler = logging.FileHandler(
    "logs/database.log",
    encoding="utf-8",
)
database_file_handler.setLevel(logging.INFO)
database_file_handler.setFormatter(formatter)

database_logger = logging.getLogger("database")
database_logger.setLevel(logging.INFO)
database_logger.addHandler(database_file_handler)
database_logger.addHandler(errors_file_handler)
database_logger.addHandler(stream)
