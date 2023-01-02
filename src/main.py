import decouple
from logger import bot_logger
import nextcord
from nextcord.ext import commands
import sys
import time


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


@bot.slash_command()
async def poll(
	interaction: nextcord.Interaction, 
	question: str, 
	choices: str, 
	length: int, 
	color: int = nextcord.SlashOption(
		choices={
			"red": nextcord.Color.red().value, "orange": nextcord.Color.orange().value, "yellow": nextcord.Color.yellow().value, 
			"green": nextcord.Color.green().value, "blue": nextcord.Color.blue().value, "purple": nextcord.Color.purple().value, 
			"gray": nextcord.Color.light_gray().value
		}
	)
):
	"""
		This is the main description.

		Parameters
		=========================
		interaction: Interaction
			The interaction object.
		question: str
			The poll question.
		choices: str
			A command-separated string of poll choices.
		length: int
			The number of days the poll will be open for.
		color: int
			The color of the left side-bar.
	"""
	# The title of the embed.
	embed_title = f"\U0001F4DD {question}"

	# The description of the embed.
	choices_list = [choice.strip() for choice in choices.split(",") if choice != ""]
	if len(choices_list) < 2:
		await interaction.send("You must specify at least two poll choices!", ephemeral=True)
		return
	if len(choices_list) >= 10:
		await interaction.send("Sorry, polls can only have up to nine (9) choices.", ephemeral=True)
		return
	
	embed_description = ""
	for i in range(len(choices_list)):
		embed_description += chr(i + 49) + f"\U000020E3 {choices_list[i]}\n"
	embed_description += f"\nThis poll will close <t:{int(time.time()) + (length * 24 * 60 * 60)}:R>"

	# Sends the poll to the channel.
	embed_poll = nextcord.Embed(title=embed_title, description=embed_description, color=color)
	partial_message = await interaction.send(embed=embed_poll)

	# Reacts to the message with each choice number.
	message = await partial_message.fetch()
	for i in range(len(choices_list)):
		await message.add_reaction(chr(i + 49) + "\U000020E3")


bot.run(token)
