import decouple
from logger import bot_logger
import nextcord
from nextcord.ext import commands
import sys


# Initialize the bot.
bot = commands.Bot()

# Gets the bot's token from the environment.
try:
	token = decouple.config("TOKEN")
except decouple.UndefinedValueError as e:
	bot_logger.error(e)
	sys.exit("An error has occurred. Consult the log file for more details.")


@bot.event
async def on_ready():
	bot_logger.info("The bot has successfully logged in.")


bot.run(token)
