from datetime import datetime, date
import pytz
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix=".")
ch_id=879288777804251177
sheepbd=date(2021, 10, 11)

@tasks.loop(seconds=60)
async def checkTime():
    channel = bot.get_channel(ch_id)
    print(channel.is_nsfw())
    datetime_TW = datetime.now(pytz.timezone('Asia/Taipei'))
    today_TW=datetime_TW.date()
    Current_Time=datetime_TW.strftime("%H:%M")
    print("Current Time =", Current_Time)
    remaindays=sheepbd-today_TW

    if (Current_Time == '00:00'):  # check if matches with the desired time
        chname=""
        if (remaindays.days >= 0):
            chname = "🦙再" + str(remaindays.days) + "天單身23年"
        else:
            chname = "恭喜🦙又老了一歲"
        await channel.edit(name=chname)
        print("chname=%d",chname)

@checkTime.before_loop
async def before_checkTime():
    print('waiting...')
    await bot.wait_until_ready()