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
        em_help.add_field(name="__**Hangout commands**__",
                          value="`%meme` - Get a random meme\n`%rps` - Play rock paper scissors\n`%joke` - Bored ???\n`%inspire` - Need some inspiration ??\n `%motivate` - Want some motivational posts?")
        em_help.add_field(name="__**Socials**__",
                          value="All social links for Bauddhik Geeks will be provided here")
        em_help.add_field(name="__**Resources**__",
                          value="All links will be provided for each field in IT plus how to contribute in open source\n`%python`\n`%javascript`\n`%reactjs`\n`%cpp`")
        em_help.add_field(name="__**Info**__",
                          value="`%hello` - Say hello to me\n`%ping` - Check latency")
        em_help.add_field(name="__**GitHub Search**__",
                          value="`%gs_r <number_of_results_you_want> <repo_name>` - Sends the list of repos which are similar to the user's input\n `%gs_u <number_of_results_you_want> <user_name>` - Sends the list of users which are similar to the user's input \n`%gi_r <repo_name>` - Sends info about a repo \n`%gi_u <user_name>` - Sends info about an user")

        # The second page of the help command embed
        em_help_hangout = discord.Embed(
            title="Hangout commands", description="")
        em_help_hangout.add_field(
            name="**Syntax**", value="`%meme`\n`%rps`\n`%joke`\n`%inspire`\n`%motivate`")
        em_help_hangout.add_field(name="**Description**",
                                  value="`%meme` - Sends a random meme using [**this**](https://memes.blademaker.tv/api?lang=en) API\n`%rps` - Play rock paper scissors with the bot\n`%joke` - Sends a one line jokes for programmers using `pyjokes` module\n`%inspire` - Sends inspirational posts\n`%motivate` - Sends motivational posts using [**this**](https://efflux.herokuapp.com/post) API")
        em_help_hangout.add_field(name="**Aliases**",
                                  value="`None`")

        # The third page of the help command embed
        em_help_socials = discord.Embed(
            title="Socials", description="<:github:912184960734081074> [**GitHub**](https://github.com/Bauddhik-Geeks)\n \n<:BG:912185310698422273> [**Website**](https://bauddhikgeeks.tech/)")

        # The fourth page of the help command embed
        em_help_resources = discord.Embed(
            title="Resources", description="All links will be provided for each field in IT plus how to contribute in open source")
        em_help_resources.add_field(
            name="**Syntax**", value="`%python`\n`%javascript`\n`%reactjs`\n`%cpp`")
        em_help_resources.add_field(
            name="**Aliases**", value="`%py`\n`%js`\n`%react`\n`%c++`")

        # The fifth page of the help command embed
        em_help_info = discord.Embed(title="Info", description="")
        em_help_info.add_field(name="**Syntax**", value="`%hello`\n`%ping`")
        em_help_info.add_field(name="**Aliases**", value="`None`")

        # The sixth page of the help command embed
        em_github = discord.Embed(
            title="GitHub Search", description="These commands allows the user to search through repos and users and get their info via simple discord commands")
        em_github.add_field(name="**Commands*",
                            value="`%gs_r`- Sends the list of repos which are similar to the user's input\n`%gs_u`- Sends the list of users which are similar to the user's input\n`%gi_r`- Sends info about a repo\n`%gi_u`- Sends info about an user")

        em_list = [em_help, em_help_hangout,
                   em_help_socials, em_help_resources, em_github]
        messages = em_list

        # The user won't be able to use the buttons after 60 seconds
        await discordSuperUtils.ButtonsPageManager(ctx, messages, timeout=180).run()


def setup(client):
    client.add_cog(help(client))
    print("Help cog has loaded")
