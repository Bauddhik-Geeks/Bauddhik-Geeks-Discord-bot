import discord
from discord.ext import commands


class ghost_ping(commands.Cog, name='ghost_ping'):

    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if len(message.mentions) == 0:
            return
        else:
            ghostping = discord.Embed(
                title="Ghostping caught!",
                color=0xe74c3c,
                timestamp=message.created_at)
            ghostping.add_field(
                name='**Ghost pinged by:**', value=f'<@{message.author.id}>')
            ghostping.add_field(name='**Ghost ping message:**',
                                value=f'{message.content}')
            ghostping.set_thumbnail(
                url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXtzZMvleC8FG1ExS4PyhFUm9kS4BGVlsTYw&usqp=CAU')
            try:
                await message.channel.send(embed=ghostping)
            except discord.Forbidden:
                try:
                    await message.author.send(embed=ghostping)
                except discord.Forbidden:
                    return


def setup(client):
    client.add_cog(ghost_ping(client))
    print("Ghost ping cog has loaded")
