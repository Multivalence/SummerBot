import discord
import json
import os
from discord.ext import commands

client = commands.Bot(command_prefix="+", status=discord.Status.idle, activity=discord.Game(name="Offline"))
client.remove_command('help')

for filename in os.listdir('./model'):
    if filename.endswith('.py'):
        client.load_extension(f'model.{filename[:-3]}')



with open('setup.json') as jsonFile:
    setup = json.load(jsonFile)
    token = setup['token']

client.run(token)
