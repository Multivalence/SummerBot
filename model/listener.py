import discord
import json
from discord.ext import commands

class Listener(commands.Cog):

    def __init__(self,client):
        self.client = client

        with open('setup.json','r') as jsonFile:
            self.channel_id = json.load(jsonFile)['channel_id']


    #Looks for new attachments in channel
    @commands.Cog.listener()
    async def on_message(self,message):

        images = message.attachments

        if message.channel.id != self.channel_id:
            return

        if message.author.bot:
            return

        if len(images) == 0:
            return

        with open('./model/utils/elements.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        for image in message.attachments:
            data.append(image.url)

        #Log
        print(data)

        with open('./model/utils/elements.json', 'w') as jsonFile:
            json.dump(data, jsonFile, indent=2)


    #Looks for attachments that have been deleted
    @commands.Cog.listener()
    async def on_message_delete(self,message):

        images = message.attachments

        if message.channel.id != self.channel_id:
            return

        if len(images) == 0:
            return

        with open('./model/utils/elements.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        for image in images:

            if image.url in data:
                data.remove(image.url)

        #Log
        print(data)

        with open('./model/utils/elements.json', 'w') as jsonFile:
            json.dump(data, jsonFile, indent=2)




#Setup
def setup(client):
    client.add_cog(Listener(client))



