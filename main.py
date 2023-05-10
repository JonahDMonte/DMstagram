import asyncio
import json

import discord
from discord.ext import commands


import DMstagram as dm

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
token = "Njk3MTY0OTQ2MDkzMzc1NTE4.GQEivi.zTGPvHv590JUSno24yFXtD6jlxKZdpoNY_p6B4"

webi = dm.dmstagram("6476738000", "Globie123", ["OG Gangsters", "Ahnenerbe Cafe"],)
webi.login()
@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

async def startup(message, n):
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name='Instagram DMs'))

    instamsgs = webi.msgcheck()
    with open("saved.json", "r") as f:
        saved = json.load(f)
    # try:
    if instamsgs != saved and instamsgs != []:
        with open("saved.json", "w") as f:
            json.dump(instamsgs, f)

        embed = discord.Embed(title='Unread Messages', color=0xfc00bf)


        embed.set_author(name='DMstagram',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/2048px-Instagram_icon.png',
                         url='https://www.instagram.com/direct/inbox/')

        for i in instamsgs:
            embed.add_field(name=i[0], value=i[1], inline=False)

        await message.channel.send(embed=embed)

    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name='Pink Floyd'))

    print(f"Checks: {n}\r", end='', flush=True)
    # except:
    #     message.channel.send("Check failed.")
    #
    #     print("Check Failed. Attempting relogin.")
    #     await bot.change_presence(
    #         activity = discord.Activity(type=discord.ActivityType.listening, name='Troubleshooting'))
    #     webi.relogin()


async def send_response(x, y, msg):
    await msg.channel.send(webi.respond(x, y))

@bot.event
async def on_message(message):
    if message.content == 'test':
        await message.channel.send('Testing 1 2 3')

    if message.content == 'startup':

        n = 0
        await message.channel.send("Starting up!")

        while True:
            await startup(message, n)
            n += 1
            await asyncio.sleep(60)

    if message.content.startswith("respond"):
        await message.channel.send("Responding")
        str = message.content.split(',,')
        await send_response(str[1], str[2], message)


    if message.content == 'relogin':
        await message.channel.send(webi.relogin())

bot.run(token)

