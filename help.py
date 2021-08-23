import discord
from discord.ext import commands

bot = commands.Bot("#")

@bot.command()
async def dhelp(ctx):
  embed=discord.Embed(title= "dhelp", description= "use #dhelp command to show this page")
  embed.add_field(name= "fun", value="`doge`,`1116`")
  await ctx.send(embed=embed)