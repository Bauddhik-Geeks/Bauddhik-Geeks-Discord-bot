import discord
from discord.ext import commands


class resources(commands.Cog, name="resources"):

    def __init__(self, client):
        self.bot = client

    @commands.command(aliases=['py'])
    async def python(self, ctx):
        embed = discord.Embed(title="Python resources",
                              color=discord.Color.from_rgb(255, 212, 59))
        embed.description = "Here are a few python learning tools to assist you master or improve your python skills. <:python:911606397274300416>"
        embed.add_field(name="YouTube",
                        value="[Python tutorial for beginners (Full playlist by Telusko)](https://www.youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) `English` \n[Python tutorial for beginners (Full playlist by Code With Harry)](https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME) `Hindi` \n[Python tutorial for beginners (Full tutorial by Programming By Mosh)](https://www.youtube.com/watch?v=_uQrJ0TkZlc&ab_channel=ProgrammingwithMosh) `English` \n[Python tutorial for intermediates (Full playlist by Code With Harry)](https://www.youtube.com/playlist?list=PLu0W_9lII9aiJWQ7VhY712fuimEpQZYp4) `Hindi`")
        await ctx.send(embed=embed)

    @commands.command(aliases=['js'])
    async def javascript(self, ctx):
        embed = discord.Embed(title="Javascript resources",
                              color=discord.Color.from_rgb(240, 219, 79))
        embed.description = "Here are javascript learning tools to assist you master or improve your javascript skills. <:javascript:911592678964228156>"
        embed.add_field(name="YouTube",
                        value="[Javascript tutorial for beginners (Full tutorial by FreeCodeCamp)](https://www.youtube.com/watch?v=PkZNo7MFNFg&ab_channel=freeCodeCamp.org) `English` \n[Javascript tutorial for beginners (Full playlist by Code With Harry)](https://www.youtube.com/playlist?list=PLu0W_9lII9ajyk081To1Cbt2eI5913SsL) `Hindi` \n[Javascript tutorial for beginners (Full playlist by Telusko)](https://www.youtube.com/playlist?list=PLsyeobzWxl7rrvgG7MLNIMSTzVCDZZcT4) `English` \n[Javascript tutorial for beginners (Full playlist by Programming By Mosh)](https://www.youtube.com/playlist?list=PLTjRvDozrdlxEIuOBZkMAK5uiqp8rHUax) `English`")
        await ctx.send(embed=embed)

    @commands.command(aliases=['reactjs'])
    async def react(self, ctx):
        embed = discord.Embed(title="ReactJS resources",
                              color=discord.Color.from_rgb(97, 219, 251))
        embed.description = "Here are reactjs learning tools to assist you master or improve your reactjs skills. <:reactjs:911598930553352232>"
        embed.add_field(name="YouTube",
                        value="[ReactJS tutorial for beginners (Full playlisy by Code With Harry)](https://www.youtube.com/playlist?list=PLu0W_9lII9agx66oZnT6IyhcMIbUMNMdt) `Hindi` \n[ReactJS tutorial for beginners (Full tutorial by FreeCodeCamp)](https://www.youtube.com/watch?v=4UZrsTqkcW4&ab_channel=freeCodeCamp.org) `English`\n[ReactJS tutorial for beginners (Full tutorial by Programming By Mosh)](https://www.youtube.com/watch?v=Ke90Tje7VS0&ab_channel=ProgrammingwithMosh) `English`"
                        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["c++"])
    async def cpp(self, ctx):
        embed = discord.Embed(title="C++ resources",
                              color=discord.Color.from_rgb(102, 154, 210))
        embed.description = "Here are reactjs learning tools to assist you master or improve your reactjs skills. <:cpp:911602273078112256>"
        embed.add_field(name="YouTube",
                        value="[C++ tutorial for beginners (Full tutorial by FreeCodeCamp)](https://www.youtube.com/watch?v=vLnPwxZdW4Y&ab_channel=freeCodeCamp.org) `English` \n[C++ tutorial for beginners (Full playlist by Code With Harry)](https://www.youtube.com/playlist?list=PLu0W_9lII9agpFUAlPFe_VNSlXW5uE0YL) `Hindi`\n[C++ tutorial for beginners (Full playlist by Apna Collegs)](https://www.youtube.com/playlist?list=PLfqMhTWNBTe0b2nM6JHVCnAkhQRGiZMSJ) `Hindi`"
                        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(resources(client))
    print("Resources cog has loaded")
