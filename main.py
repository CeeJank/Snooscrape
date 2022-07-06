import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# .env file for token
TOKEN = os.getenv('DISCORD_TOKEN') # Token must have '' containing  itself, otherwise "improper token passed"

# Intents // prefix
intents = discord.Intents.default()     # 1.5 update, "subcribe to bucket of events"
intents.typing = False          # wihout spammy events like presences or typing
intents.presences = False       # I actually have no idea what these 2 lines actually mean
client = commands.Bot(command_prefix= '!', intents=intents) # client refers to the bot itself


@client.event   # decorator that registers an event to listen to
async def on_ready():
    print (f'{client.user} is connected to discord! ')


client.run(TOKEN)