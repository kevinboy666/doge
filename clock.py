from datetime import datetime
import threading
import pytz
import asyncio

remaindays = 46

async def checkTime(channel):
    print(channel.is_nsfw())
    await channel.edit(name="asdlkl")
    # This function runs periodically every 1 second
    threading.Timer(5, checkTime,args=[channel]).start()
    datetime_TW = datetime.now(pytz.timezone('Asia/Taipei'))
    current_time = datetime_TW.strftime("%H:%M")
    print("Current Time =", current_time)

    if (current_time == '13:29'):  # check if matches with the desired time
        global remaindays
        chname=""
        if (remaindays > 0):
            remaindays -= 1
            chname = "咩再" + str(remaindays) + "天單身23年"
        else:
            chname = "恭喜咩單身23年"
        await channel.edit(name=chname)
