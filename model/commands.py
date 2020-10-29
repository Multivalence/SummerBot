import discord
import random
import json
from discord.ext import commands

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.limited = []
        self.count = 0

    @commands.command()
    async def random(self,ctx):

        with open('./model/utils/elements.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        if len(data) == 0:
            await ctx.channel.send("No Images or Videos found!")
            return


        image = random.choice(data)

        while image in self.limited:
            self.count += 1

            if self.count == 30:
                self.limited = []
                self.count = 0

            image = random.choice(data)


        self.limited.append(image)
        await ctx.channel.send(image)





#Setup
def setup(client):
    client.add_cog(Commands(client))


