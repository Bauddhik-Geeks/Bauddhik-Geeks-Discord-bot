import discord
from discord.ext import commands


class socials(commands.Cog, name="socials"):

    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def socials(self, ctx):
        embed = discord.Embed()
        embed.description = "[Github](https://github.com/Bauddhik-Geeks)"
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(socials(client))
    print("Socials cog has been loaded")
