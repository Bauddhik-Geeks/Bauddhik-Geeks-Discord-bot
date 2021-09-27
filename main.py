import discord
import asyncio
import subprocess
subprocess.call(['pip', 'install','discord_components'])
from discord_components import *    #pip install discord-components
from discord.ext.commands import bot
from discord.utils import get
from discord.ext import commands, tasks
import os
import requests
import json
import random
import pyjokes
#################################################################################
intents = discord.Intents.default()
intents.members = True
intents = intents.all()
##################################################################################
client=commands.Bot(command_prefix="%", intents=intents)
client.remove_command('help')
status=['cooking code','eating logic','%help']
########################### AUTOMATION CODE ############################################
@client.event
async def on_ready():
  change_status.start()
  meme1.start()
  DiscordComponents(client)
  print("we have logged in as {0.user}".format(client))

@tasks.loop(seconds=2)
async def change_status():
  await client.change_presence(activity=discord.Game(random.choice(status)))

@tasks.loop(seconds=7200)
async def meme1():
  c=int(875801279111233626) #here your channel id will be there, in which auto meme will be posted after every 2 hrs
  channel1 = client.get_channel(c)
  r=requests.get("https://memes.blademaker.tv/api?lang=en")
  res=r.json()
  title=res['title']
  ups=res['ups']
  downs=res['downs']
  sub=res['subreddit']
  m=discord.Embed(title=f"{title}\nsubreddit: {sub}")
  m.set_image(url=res["image"])
  m.set_footer(text="Automatic meme for your server")
  await channel1.send(embed=m)
########################### COMMAND CODE ######################################

@client.command()
async def hello(ctx):
  await ctx.send('hey! I am Bauddhik Geeks bot, type %help to see what can I do :) !!')
########################### HELP COMMAND ######################################

@client.command()
async def help(ctx):
  Hangouts=['**%meme\n**:> get a random meme\n','**%rps\n**:> play Rock Paper Scissors\n','**%jokes** \n:> Bored ???\n','**%inspire**\n:> need some inspiration ??\n','**%motivate**\n:> Want some motivational posts?\n', ]
  Socials=['All social links for bauddhik geeks will be provided here']
  Resources=['All links will be provided for each field in IT plus how to contribute in open source \n %python']
  Info=['**%hello\n**:> Say hello to me\n','**%ping\n**:> check latency\n']

  hel=discord.Embed(title='LIST OF COMMANDS', description ="Click anyone to explore",color=0x3498db)
  hel.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  Hangouts=discord.Embed(title='Hangouts', description =''.join(Hangouts),color=0x3498db)
  Hangouts.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  Socials=discord.Embed(title='Socials', description =''.join(Socials),color=0x3498db)
  Socials.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  Resources=discord.Embed(title='crypto', description =''.join(Resources),color=0x3498db)
  Resources.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  info=discord.Embed(title='Info', description =''.join(Info),color=0x3498db)
  info.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  m = await ctx.reply(
        embed=hel,
        components=[[Button(style=1, label="Hangouts"),Button(style=3, label="Socials"),Button(style=ButtonStyle.red,label="Resources"),Button(style=ButtonStyle.grey,label="Info")]
        ],
    )
  def check(res):
    return ctx.author == res.user and res.channel == ctx.channel
  res = await client.wait_for("button_click", check=check)
  if res.component.label=="Hangouts":
    await m.edit(embed=Hangouts,components=[],)
  if res.component.label=="Socials":
    await m.edit(embed=Socials, components=[],)
  if res.component.label=="Resources":
    await m.edit(embed=Resources, components=[],)
  if res.component.label=="Info":
    await m.edit(embed=info, components=[],)
############################# MEME ####################################

@client.command()
async def meme(ctx):
  r=requests.get("https://memes.blademaker.tv/api?lang=en")
  res=r.json()
  title=res['title']
  ups=res['ups']
  downs=res['downs']
  sub=res['subreddit']
  m=discord.Embed(title=f"{title}\nsubreddit: {sub}")
  m.set_image(url=res["image"])
  m.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=m)
############################### ANTI GHOSTPING ###############################

@client.event
async def on_message_delete(message):
    if len(message.mentions) == 0:
        return
    else:
        ghostping = discord.Embed(title=f'GHOSTPING CAUGHT', color=0xe74c3c, timestamp=message.created_at)
        ghostping.add_field(name='**Name:**', value=f'{message.author} ({message.author.id})')
        ghostping.add_field(name='**Message:**', value=f'{message.content}')
        ghostping.set_thumbnail(
            url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXtzZMvleC8FG1ExS4PyhFUm9kS4BGVlsTYw&usqp=CAU')
        try:
            await message.channel.send(embed=ghostping)
        except discord.Forbidden:
            try:
                await message.author.send(embed=ghostping)
            except discord.Forbidden:
                return
######################### MOTIVATIONAL POST #################################

@client.command()
async def motivate(ctx):
  data=requests.get("https://efflux.herokuapp.com/post")
  json_data=json.loads(data.text)
  quote =json_data['p']
  await ctx.reply(quote)
################ SOCIALS #############################

@client.command()
async def socials(ctx):
    embed = discord.Embed()
    embed.description = "Github [link](https://github.com/Bauddhik-Geeks)"
    await ctx.send(embed=embed)

@client.command()
async def python(ctx):
    embed = discord.Embed(title="Resources", color=0x00ff00)
    embed.description = "Here are a few python learning tools to assist you master or improve your python skills."
    embed.add_field(name=":man_climbing: Youtube",value="[Python tutorial for beginners (full playlist by Telusko)](https://www.youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) `English` \n[Python tutorial for beginners (full playlist by code with harry)](https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME) `Hindi` ")
    await ctx.send(embed=embed)

field= os.environ['token']
client.run(field)