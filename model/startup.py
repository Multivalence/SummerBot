import discord
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

        embed.set_thumbnail(
            url="https://www.nomadfoods.com/wp-content/uploads/2018/08/placeholder-1-e1533569576673.png")
        embed.add_field(name="`+random`", value="Returns random image or video.", inline=False)

        await ctx.channel.send(embed=embed)


#Setup
def setup(client):
    client.add_cog(Startup(client))



