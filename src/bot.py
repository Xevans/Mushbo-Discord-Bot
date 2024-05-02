# bot.py
import os
import random
from dotenv import load_dotenv

import discord
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='99')
async def nine_nine(ctx):
    responses = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!'
    ]

    response = random.choice(responses)
    await ctx.send(response)

bot.run(TOKEN)