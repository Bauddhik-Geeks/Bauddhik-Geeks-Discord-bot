import discord
from discord import embeds
from discord.ext import commands
import requests
import json
import discordSuperUtils


class inforepo(commands.Cog, name="inforepo"):

    def __init__(self, client):
        self.bot = client

    @commands.command(aliases=["gi_r"])
    # This command allows the user to get the info about a repo in GitHub
    async def githubinfo_repo(self, ctx, *, repo):
        url = f"https://api.github.com/repos/{repo}"
        repo_search = requests.get(url)
        repos = repo_search.json()

        if repo_search.status_code == 404:
            error_em = discord.Embed(
                title='', description="Sorry I couldn't find any repos \nMake sure that you are passing the argument in this format `owner_username/repo_name`")
            await ctx.send(embed=error_em)

        elif repo_search.status_code == 200:
            topics = []
            for topic in repos["topics"]:
                topics.append(topic)
            topics_joined = '\n'.join([str(elem) for elem in topics])
            embed = discord.Embed(
                title='', description=f'[**Repo link**]({repos["html_url"]}) \n**Description**: {repos["description"]} \n**Stars**: {repos["stargazers_count"]} \n**Forks**: {repos["forks_count"]} \n**Open issues**: {repos["open_issues"]} \n**Topics**: `{topics_joined}`', color=discord.Color.from_rgb(0, 207, 200))
            embed.set_author(name=repos["full_name"],
                             icon_url=repos["owner"]["avatar_url"])
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(inforepo(client))
    print("GitHub info repo cog has been loaded")
