import discord
from discord.ext import commands
import random

images = [
    "https://reurl.cc/ogj5Zl",
]

client = commands.Bot(command_prefix="/")

#meme
@client.command()
async def meme(ctx):
    embed = discord.Embed()
    embed.set_image(url=random.choice(images))
    await ctx.send(embed=embed)


