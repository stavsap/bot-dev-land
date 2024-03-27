import os
import discord
from discord.ext import commands

# set a sub set intents of what is allowed for the bot from its application config.
intents = discord.Intents.default()
intents.dm_messages = True
bot = commands.Bot(intents=intents, command_prefix="/")

# Event triggered when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# https://stackoverflow.com/questions/65207823/discord-py-bot-command-not-running

# simple on message echo
@bot.event
async def on_message(message):
    # Check if the message is from a user and not the bot itself
    if message.author == bot.user:
        return
    print(message.content)
    if message.content.startswith("!hello"):
        await message.channel.send("Hi, use !showpic to get a picture")
    # Check if the message starts with a specific command or trigger
    if message.content.startswith("!showpic"):
        # Open the image file
        with open("example.png", "rb") as f:
            picture = discord.File(f)

        # Send the message with the picture attached
        await message.channel.send("Here's a picture!", file=picture)


# Command to get a pong response for slash command 'ping', the guild id is the id of the server that bot in, remove it to update all.
@bot.slash_command(name="ping", guild=discord.Object(id=1111))
async def ping(ctx):
    await ctx.respond("pong")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create a new bot instance
    bot.run(os.getenv('DISCORD_BOT_API_TOKEN'))
