import discord
import json
from discord.ext import commands

class Startup(commands.Cog):

    def __init__(self,client):
        self.client = client



    #On Startup
    @commands.Cog.listener()
    async def on_ready(self):
        print("SummerBot is Ready to go!")
        await self.client.change_presence(activity=discord.Game(name="+help | SummerBot"))


    #Help Command
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title="Help Menu",
            description="List of all commands",
            colour=discord.Colour.dark_purple()
        )

        with open('setup.json','r') as jsonFile:
            thumbnail = json.load(jsonFile)['help_image']

        embed.set_thumbnail(
            url=thumbnail)
        embed.add_field(name="`+random`", value="Returns random image or video.", inline=False)

        await ctx.channel.send(embed=embed)


#Setup
def setup(client):
    client.add_cog(Startup(client))



