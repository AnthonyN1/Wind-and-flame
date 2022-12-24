import nextcord
from nextcord.ext import commands
from logger import bot_logger


bot = commands.Bot()


@bot.event
async def on_ready():
	print(f"We have logged in as {bot.user}")

@bot.slash_command(description="My first slash command")
async def hello(interaction: nextcord.Interaction):
	await interaction.send("Hello!")


bot.run(<token>)