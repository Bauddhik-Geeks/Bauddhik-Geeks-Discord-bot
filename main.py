from discord_components import *  # pip install discord-components
import random
import json
import requests
import os
import sys
import traceback
from discord.ext import commands, tasks
from discord.utils import get
from discord.ext.commands import bot
import discord  # pip install discord


intents = discord.Intents.default()
intents.members = True
intents = intents.all()


client = commands.Bot(command_prefix="%",
                      intents=intents,
                      case_insensitive=True)
client.remove_command('help')
# List of all the activities through which the bot will switch
status = ['Cooking code', 'Eating logic', '%help']


@client.event  # This will take place when the bot comes online
async def on_ready():
    change_status.start()  # The activity of the will change due to this
    # The automeme command is been shifted into the cogs folder
    DiscordComponents(client)
    print("We have logged in as {0.user}".format(client))


@tasks.loop(seconds=300)
async def change_status():
    await client.change_presence(activity=discord.Game(random.choice(status)))


@client.command()
async def hello(ctx):
    await ctx.send('Hey :wave:! I am Bauddhik Geeks bot, Type `%help` to see what can I do :) !!')

extensions = [
    'cogs.utils.errorhandler',
    'cogs.meme.meme',
    'cogs.utils.ghostping',
    'cogs.utils.help',
    'cogs.utils.motivate',
    'cogs.utils.socials',
    'cogs.utils.github.inforepo',
    'cogs.utils.github.infouser',
    'cogs.utils.github.searchrepo',
    'cogs.utils.github.searchuser',
    'cogs.resources.resources'
]
if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Error loading {extension}', file=sys.stderr)
            traceback.print_exc()


field = os.environ['token']
client.run(field)
