from keep_alive import keep_alive
import discord
from discord.ext import commands, tasks
import os
import random
from replit import db
import response as res
#import asyncio
#from clock import checkTime

bot = commands.Bot(command_prefix=".")
#detects
sad_words = ["sad", "depressed", "unhappy", "miserable", "金莎"]
taunt_words=["angry", "大便"]
dog = ["浪浪", "狗狗", "笨狗", "doge"]
sheep = ["傻羊"]
_1116 = ["睡覺", "烤羊", "1116", "咩肉爐"]
#actives
listen=["banana phone","Susumu Hirasawa - Guts"]
#response
animal_sound = ["汪", "喵", "呱", "哞", "嘶", "嘎"]

starter_encouragements = ["咩咩背著羊娃娃", "Nooooo", "Wow!"]


from datetime import datetime
import pytz

remaindays = 46
@tasks.loop(seconds=60)
async def checkTime():
    channel = bot.get_channel(879288777804251177)
    datetime_TW = datetime.now(pytz.timezone('Asia/Taipei'))
    current_time = datetime_TW.strftime("%H:%M")
    print("Current Time =", current_time)

    if (current_time == '00:00'):  # check if matches with the desired time
        global remaindays
        chname=""
        if (remaindays > 0):
            remaindays -= 1
            chname = "🦙再" + str(remaindays) + "天單身23年"
        else:
            chname = "🦙已經單身23年"
        await channel.edit(name=chname)

@checkTime.before_loop
async def before_checkTime():
    print('waiting...')
    await bot.wait_until_ready()


#boot bot
@bot.event
async def on_ready():
    
    print('Logged in as')
    print(bot.user.name)
    print('------')
    act = random.choice(["game", "streaming", "listenting", "watching"])
    if act == "game":
        await bot.change_presence(activity=discord.Game("Mining Simulator"))
    if act == "streaming":
        await bot.change_presence(
            activity=discord.Streaming(name="Reaction", url=''))
    if act == "watching":
        await bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name="MeMe"))
    if act == "listenting":
        await bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening, name=random.choice(listen)))



#detect msg
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print("{} : {}".format(message.author, message.content))  #msg log
    await bot.process_commands(message)

    msg = message.content
    if any(word in msg for word in animal_sound):
        await message.channel.send(random.choice(animal_sound))

    if msg.startswith('7414'):
        await message.channel.send("<:cheem:862575383374725131>")

    if msg.startswith("咩"):
        out=random.choices(["咩", "咩肉爐"],weights=(80, 20))
        await message.channel.send(out[0])

    if msg.startswith("<:cheem:862575383374725131>"):
        await message.add_reaction("cheem:862575383374725131")

    if msg.startswith("<:doge:668358894128463879>"):
        await message.add_reaction("doge:668358894128463879")

    if any(word in msg for word in sheep):
        await message.add_reaction("lul:671687629678313501")

    if any(word in msg for word in _1116):
        await message.add_reaction("1116:668820651540480031")

    if msg.startswith("!inspire"):
        quote = res.get_quote()
        await message.channel.send(quote)

    options = starter_encouragements
    if "encouragements" in db.keys():
        options = options + list(db['encouragements'])

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    if msg.startswith("!newc"):  #add new encourage msg
        encouraging_message = msg.split("!newc ", 1)[1]
        res.update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")

    if msg.startswith("!delc"):  #del exist encourage msg
        if "encouragements" in db.keys():
            index = int(msg.split("!delc ", 1)[1])
            res.delete_encouragment(index)
        await message.channel.send("Encourage message deleted.")

    if "doges" in db.keys():
        dogeo = list(db["doges"])

    if any(word in msg for word in dog):
        await message.channel.send(random.choice(dogeo))

    if msg.startswith("!newd"):  #add new doge msg
        doge_message = msg.split("!newd ", 1)[1]
        res.update_doges(doge_message)
        await message.channel.send("New doge message added.")

    if msg.startswith("!deld"):  #del exist doge msg
        if "doges" in db.keys():
            dmsg = msg.split("!deld ", 1)[1]
            res.delete_doge(dmsg)
        await message.channel.send("doge message deleted.")

    if msg.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)


# react roles
@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 869105815301271572:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

        if payload.emoji.name == "cheem":
            role = discord.utils.get(guild.roles, name="doge")
        elif payload.emoji.name == "leaf":
            role = discord.utils.get(guild.roles, name="萬國")

        if role is not None:
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("role added")
            else:
                print("role not found")
        else:
            print("member not found")


@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 869105815301271572:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

        if payload.emoji.name == "cheem":
            role = discord.utils.get(guild.roles, name="doge")

        if role is not None:
            member = guild.get_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print("role removed")
            else:
                print("role not found")
        else:
            print("member not found")

  
checkTime.start()

keep_alive()
bot.run(os.getenv('TOKEN'))
