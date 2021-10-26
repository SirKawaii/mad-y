# mad-y discord bot

import os
import request
import discord
import json

from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.client()

prefix = "!mdy"

# messages
WELCOME_MESSAGE = "Hola! aun"

# program

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix):
        command = message.content.replace(prefix, '', 1).strip()
        print(f'command text [{command}]')

        if command == '':
            await message.channel.send(WELCOME_MESSAGE)

        if command == ('hola'):
            await message.channel.send('que rayos!')

client.run(TOKEN)
