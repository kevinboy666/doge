import discord
from discord.ext import commands

bot = commands.Bot("#")

@bot.command()
async def cmd(ctx):
  await ctx.channel.send("cmd")