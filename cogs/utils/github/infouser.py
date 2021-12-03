import discord
from discord import embeds
from discord.ext import commands
import requests
import json
import discordSuperUtils


class infouser(commands.Cog, name="infouser"):

    def __init__(self, client):
        self.bot = client

    @commands.command(aliases=["gi_u"])
    # This command allows the user to get the info about an user in GitHub
    async def githubinfo_user(self, ctx, *, user):
        url = f"https://api.github.com/users/{user}"
        user_search = requests.get(url)
        users = user_search.json()

        if user_search.status_code == 404:
            error_em = discord.Embed(
                title='', description="Sorry I couldn't find any users \nMake sure that you don't have any typos", color=discord.Color.from_rgb(0, 207, 200))
            await ctx.send(embed=error_em)

        elif user_search.status_code == 200:
            embed = discord.Embed(
                title='', description=f'[**Profile link**]({users["html_url"]}) \n**Type**: {users["type"]} \n**Email** : {users["email"]} \n**Company** : {users["company"]} \n**Hireable** : {users["hireable"]} \n**Location** : {users["location"]} \n**Bio**: {users["bio"]} \n**Public repos**: {users["public_repos"]} \n**Public gists**: {users["public_gists"]} \n**Followers**: {users["followers"]} \n**Following**: {users["following"]}', color=discord.Color.from_rgb(0, 207, 200))
            embed.set_author(name=users["login"], icon_url=users["avatar_url"])
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(infouser(client))
    print("GitHub info user cog has been loaded")
