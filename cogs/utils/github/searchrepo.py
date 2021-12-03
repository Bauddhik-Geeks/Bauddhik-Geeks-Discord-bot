import discord
from discord import embeds
from discord.ext import commands
import requests
import json
import discordSuperUtils


class searchrepo(commands.Cog, name="searchrepo"):

    def __init__(self, client):
        self.bot = client

    @commands.command(aliases=["gs_r"])
    # This command allows the user to search through for a repo in GitHub
    async def githubsearch_repo(self, ctx, page, *, repo):
        url = f"https://api.github.com/search/repositories?q={repo}&per_page={page}"
        repo_search = requests.get(url)
        repos = repo_search.json()

        if repo_search.status_code == 404:
            error_em = discord.Embed(
                title='', description="Sorry I couldn't find any repos \nPlease try again and check if there are any repos or not")
            await ctx.send(embed=error_em)

        elif repo_search.status_code == 200:
            if page.isdigit():
                repo_name = []
                repo_url = []
                repo_star = []
                repo_fork = []
                for repo in repos["items"]:
                    repo_name.append(repo["full_name"])
                    repo_url.append(repo["html_url"])
                    repo_star.append(repo["stargazers_count"])
                    repo_fork.append(repo["forks_count"])

                repo_info = [
                    f"**Repo Name**: [{repo_name[x]}]({repo_url[x]}) \n**Stars**: {repo_star[x]} \n**Forks**: {repo_fork[x]}" for x in range(len(repo_name))
                ]

                await discordSuperUtils.ButtonsPageManager(ctx,
                                                           discordSuperUtils.generate_embeds(
                                                               repo_info,
                                                               title="GitHub Repo Search Results",
                                                               fields=5,
                                                               color=discord.Color.from_rgb(
                                                                   0, 207, 200),
                                                               description="These are the results, I have found",
                                                           ),
                                                           timeout=120,  # After 2 mins the user can't use the buttons
                                                           ).run()
                repo_name.clear()
                repo_star.clear()
                repo_fork.clear()
            else:
                page_err_em = discord.Embed(
                    title='', description='Make sure that your `page` argument is a digit')
                await ctx.send(embed=page_err_em)


def setup(client):
    client.add_cog(searchrepo(client))
    print("GitHub search repo cog has been loaded")
