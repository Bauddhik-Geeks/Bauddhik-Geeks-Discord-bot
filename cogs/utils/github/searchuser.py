import discord
from discord import embeds
from discord.ext import commands
import requests
import json
import discordSuperUtils


class searchuser(commands.Cog, name="searchuser"):

    def __init__(self, client):
        self.bot = client

    @commands.command(aliases=["gs_u"])
    # This command allows the user to search for a user in GitHub
    async def githubsearch_user(self, ctx, page, *, username):
        url = f"https://api.github.com/search/users?q={username}&per_page={page}"
        user_search = requests.get(url)
        users = user_search.json()

        if user_search.status_code == 404:
            error_em = discord.Embed(
                title='', description="Sorry I couldn't find any users \nPlease try again and check if there are any repos or not")
            await ctx.send(embed=error_em)

        elif user_search.status_code == 200:
            if page.isdigit():
                user_name = []
                user_url = []

                for user in users["items"]:
                    user_name.append(user["login"])
                    user_url.append(user["html_url"])

                user_info = [
                    f"** Name**: [{user_name[x]}]({user_url[x]})" for x in range(len(user_name))
                ]

                await discordSuperUtils.ButtonsPageManager(ctx,
                                                           discordSuperUtils.generate_embeds(
                                                               user_info,
                                                               title="GitHub User Search Results",
                                                               fields=5,
                                                               color=discord.Color.from_rgb(
                                                                   0, 207, 200),
                                                               description="These are the results, I have found",
                                                           ),
                                                           timeout=120,  # After 2 mins the user can't use the buttons
                                                           ).run()
                user_name.clear()
                user_url.clear()
            else:
                page_err_em = discord.Embed(
                    title='', description='Make sure that your `page` argument is a digit')
                await ctx.send(embed=page_err_em)


def setup(client):
    client.add_cog(searchuser(client))
    print("GitHub search user cog has been loaded")
