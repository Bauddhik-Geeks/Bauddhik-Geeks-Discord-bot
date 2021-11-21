import discord
from discord.ext import commands
import discordSuperUtils


class help(commands.Cog, name='help'):

    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def help(self, ctx):
        # The front page of the help command embed
        em_help = discord.Embed(title="Help", description="")
        em_help.add_field(name="**Meme commands**", value="`%meme`")
        em_help.add_field(name="**Resources commands**",
                          value="`%python` \n`%javascript`\n `%react` \n`%cpp`")

        # The second page of the help command embed
        em_help_meme = discord.Embed(title="Meme command", description="")
        em_help_meme.add_field(name="**Syntax**", value="`%meme`")
        em_help_meme.add_field(name="**Description**",
                               value="Sends a random meme using [**this**](https://memes.blademaker.tv/api?lang=en) API")
        em_help_meme.add_field(name="**Aliases**",
                               value="`None`")

        # The third page of the help command embed
        em_help_resources = discord.Embed(
            title="Resources command", description="")
        em_help_resources.add_field(
            name="**Syntax**", value="`%python` \n`%javascript`\n `%react` \n`%cpp`")
        em_help_resources.add_field(name="**Description**",
                                    value="These commands have the list of few resources which will be useful to improve/master your skills in that languages")
        em_help_resources.add_field(name="**Aliases**",
                                    value="`py` \n`js` \n`reactjs` \n`cpp`")

        em_list = [em_help, em_help_meme, em_help_resources]

        messages = em_list

        # The user won't be able to use the buttons after 60 seconds
        await discordSuperUtils.ButtonsPageManager(ctx, messages, timeout=60).run()


def setup(client):
    client.add_cog(help(client))
    print("Help cog has loaded")
