from keep_alive import keep_alive
from discord.ext import commands
import discord
import os
import random
from replit import db
import asyncio
from cmd import cmd

client = commands.Bot(command_prefix=".")

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "金莎", "大便"]
dog = ["浪浪", "狗狗", "笨狗", "doge"]
sheep = ["傻羊"]
eee = ["睡覺", "烤羊", "1116"]
starter_encouragements = ["咩咩背著羊娃娃", "Nooooo", "Wow!"]
animal_sound = ["汪", "喵", "咩", "呱", "哞", "嘶", "嘎"]


if "responding" not in db.keys():
    db["responding"] = False


#boot bot
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="Susumu Hirasawa - Guts"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


#detect msg
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print("{} : {}" .format(message.author, message.content))  #msg log
    await client.process_commands(message)

    #record chat (todo)
    if message.content.startswith('record chat'):
        with open('output.txt', 'a') as the_file:
            async for log in client.logs_from(messagechannellimit=1000):
                stringTime = log.timestamp.strftime("%Y-%m-%d %H:%M")
                try:
                    author = log.author
                except:
                    author = 'invalid'
                message = str(log.content.encode("utf-8"))[2:-1]

                template = '[{stringTime}] <{author}> {message}\n'
                try:
                    the_file.write(
                        template.format(stringTime=stringTime,
                                        author=author,
                                        message=message))
                except:
                    author = log.author.discriminator
                    the_file.write(
                        template.format(stringTime=stringTime,
                                        author=author,
                                        message=message))
                print(
                    template.format(stringTime=stringTime,
                                    author=author,
                                    message=message)[:-1])
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    msg = message.content
    if msg.startswith(("汪")):
        await message.channel.send(random.choice(animal_sound))

    if msg.startswith('7414'):
        await message.channel.send("<:cheem:862575383374725131>")

    if msg.startswith("咩"):
        await message.channel.send("咩")

    if msg.startswith("<:cheem:862575383374725131>"):
        await message.add_reaction("cheem:862575383374725131")

    if msg.startswith("<:doge:668358894128463879>"):
        await message.add_reaction("doge:668358894128463879")

    if any(word in msg for word in sheep):
        await message.add_reaction("lul:671687629678313501")

    if any(word in msg for word in eee):  #1116
        await message.add_reaction("1116:668820651540480031")

    if msg.startswith("!inspire"):
        quote = get_quote()
        await message.channel.send(quote)

    options = starter_encouragements
    if "encouragements" in db.keys():
        options = options + list(db['encouragements'])

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    if msg.startswith("!newc"):  #add new encourage msg
        encouraging_message = msg.split("!newc ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")

    if msg.startswith("!delc"):  #del exist encourage msg
        if "encouragements" in db.keys():
            index = int(msg.split("!delc ", 1)[1])
            delete_encouragment(index)
        await message.channel.send("Encourage message deleted.")

    if "doges" in db.keys():
        dogeo = list(db["doges"])

    if any(word in msg for word in dog):
        await message.channel.send(random.choice(dogeo))

    if msg.startswith("!newd"):  #add new doge msg
        doge_message = msg.split("!newd ", 1)[1]
        update_doges(doge_message)
        await message.channel.send("New doge message added.")

    if msg.startswith("!deld"):  #del exist doge msg
        if "doges" in db.keys():
            dmsg = msg.split("!deld ", 1)[1]
            delete_doge(dmsg)
        await message.channel.send("doge message deleted.")

    if msg.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("$responding"):
        value = msg.split("$responding ", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")


# react roles
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 869105815301271572:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

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


@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 869105815301271572:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

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


keep_alive()
client.run(os.getenv('TOKEN'))
