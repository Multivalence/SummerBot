import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="+", status=discord.Status.idle, activity=discord.Game(name="Offline"))
client.remove_command('help')

for filename in os.listdir('./model'):
    if filename.endswith('.py'):
        client.load_extension(f'model.{filename[:-3]}')


client.run('TOKEN')
