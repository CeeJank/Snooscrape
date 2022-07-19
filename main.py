import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import asyncpraw

import asyncio
# reddit instance
reddit = asyncpraw.Reddit(client_id='client_id',
client_secret='client_secret',
#username='',
#password='',
user_agent='Snooscrape', check_for_async = False)


# .env file for token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # Token must have '' containing  itself, otherwise "improper token passed"

# Intents // prefix
intents = discord.Intents.default()     # 1.5 update, "subcribe to bucket of events"
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix= '!', intents=intents) # client refers to the bot itself

@bot.event
async def on_ready():
    print(f'logged in as {bot.user} (ID: {bot.user.id})')
    print ('---')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == '!hello':
        await message.channel.send (f'hi there {message.author}')

'''
class MyClient(discord.Client):
    async def on_ready(self):
        print (f'{self.user} has logged in (ID:{self.user.id})')
        print ('------')
    
    async def on_message(self, message):
        if message.content.startswith('!hello'):
            await message.reply ("hi there.", mention_author=True)

intents.message_content = True
client = MyClient(intents=intents)
''' 

# initiating the bot
bot.run(TOKEN)