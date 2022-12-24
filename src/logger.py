import logging


# Adds the logger.
bot_logger = logging.getLogger("nextcord")
handler = logging.FileHandler(filename="logs/nextcord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s :: %(levelname)-8s :: %(message)s"))
bot_logger.addHandler(handler)
