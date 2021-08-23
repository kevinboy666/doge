from datetime import datetime
import threading
from discord.ext import commands
import discord
import pytz
import asyncio

remaindays=48
bot = commands.Bot(".")
channel = bot.get_channel(879291076706451506)


async def changeChannelName():
  global remaindays
  if(remaindays>0):
    remaindays-=1
    chname="咩再"+str(remaindays)+"天單身23年"
    await bot.edit(name = chname)
  else:
    chname="恭喜咩單身23年"
    await bot.edit(name = chname)

loop = asyncio.get_event_loop()
task=loop.create_task(changeChannelName())

def checkTime():
    # This function runs periodically every 1 second
    threading.Timer(60, checkTime).start()
    datetime_TW = datetime.now(pytz.timezone('Asia/Taipei'))
    current_time = datetime_TW.strftime("%H:%M")
    print("Current Time =", current_time)

    if(current_time == '22:46'):  # check if matches with the desired time
      asyncio.run(asyncio.wait(task))

