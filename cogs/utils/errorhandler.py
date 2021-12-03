import discord
from discord.ext import commands


class errorhandler(commands.Cog, name="errorhandler"):

    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Choose a smaller number, as the current number is breaking the embed limit")
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Use all the required arguments")
        else:
            raise error


def setup(client):
    client.add_cog(errorhandler(client))
    print("Error handler cog has been loaded")
