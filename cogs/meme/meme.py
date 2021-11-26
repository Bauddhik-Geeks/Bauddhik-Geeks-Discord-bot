import discord
from discord.ext import commands, tasks
import requests


class meme(commands.Cog, name='meme'):

    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.automeme.start()

    @tasks.loop(seconds=7200)
    async def automeme(self):
        # Here your channel ID will be there, in which auto meme will be posted after every 2 hrs
        c = int(912618398712758286)
        channel1 = self.bot.get_channel(c)
        r = requests.get("https://memes.blademaker.tv/api?lang=en")
        res = r.json()
        title = res['title']
        ups = res['ups']
        downs = res['downs']
        sub = res['subreddit']
        m = discord.Embed(
            title=f"{title}\nSubreddit: {sub}")
        m.set_image(url=res["image"])
        m.set_footer(
            text=f"Automatic meme for your server \n 👍 {ups} 👎 {downs}")
        await channel1.send(embed=m)

    @commands.command()
    async def meme(self, ctx):
        r = requests.get("https://memes.blademaker.tv/api?lang=en")
        res = r.json()
        title = res['title']
        ups = res['ups']
        downs = res['downs']
        sub = res['subreddit']
        nsfw = res['nsfw']
        if nsfw is False:
            m = discord.Embed(title=f"{title}\nSubreddit: {sub}")
            m.set_image(url=res["image"])
            m.set_footer(text=f"Requested by {ctx.author} \n👍 {ups} 👎 {downs}",
                         icon_url=ctx.author.avatar_url)
            await ctx.send(embed=m)
        elif nsfw is True:
            return


def setup(client):
    client.add_cog(meme(client))
    print("Meme cog has loaded")
