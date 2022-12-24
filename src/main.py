import decouple
from logger import bot_logger
import nextcord
from nextcord.ext import commands
import sys


bot = commands.Bot()

try:
	token = decouple.config("TOKEN")
except decouple.UndefinedValueError as e:
	bot_logger.error(e)
	sys.exit("An error has occurred. Consult the log file for more details.")


@bot.event
async def on_ready():
	print(f"We have logged in as {bot.user}")

@bot.slash_command(description="My first slash command")
async def hello(interaction: nextcord.Interaction):
	await interaction.send("Hello!")


bot.run(token)