from datetime import datetime
import pytz
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix=".")
remaindays = 45

@tasks.loop(seconds=60)
async def checkTime():
    channel = bot.get_channel(879291076706451506)
    print(channel.is_nsfw())
    datetime_TW = datetime.now(pytz.timezone('Asia/Taipei'))
    current_time = datetime_TW.strftime("%H:%M")
    print("Current Time =", current_time)

    if (current_time == '19:07'):  # check if matches with the desired time
        global remaindays
        chname=""
        if (remaindays > 0):
            remaindays -= 1
            chname = "🦙再" + str(remaindays) + "天單身23年"
        else:
            chname = "恭喜🦙又老了一歲"
        await channel.edit(name=chname)

@checkTime.before_loop
async def before_checkTime():
    print('waiting...')
    await bot.wait_until_ready()