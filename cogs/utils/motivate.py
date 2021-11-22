import discord
from discord.ext import commands
import requests
import json


class motivate(commands.Cog, name="motivate"):

    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def motivate(self, ctx):
        data = requests.get("https://efflux.herokuapp.com/post")
        json_data = json.loads(data.text)
        quote = json_data['p']
        await ctx.reply(quote)


def setup(client):
    client.add_cog(motivate(client))
    print("Motivate cog has been loaded")
