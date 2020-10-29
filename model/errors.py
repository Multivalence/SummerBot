import discord
from discord.ext import commands


class Errors(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Called when command raises an error
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        print(error)
        await ctx.channel.send("Something went wrong. Did you type the command correctly?")



#Setup
def setup(client):
    client.add_cog(Errors(client))


