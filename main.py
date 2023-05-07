import json

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import webinteractions as wi
from discord.ext import tasks
from printsleep import printsleeptime
import threading
import typing
import functools
import asyncio

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
token = "Njk3MTY0OTQ2MDkzMzc1NTE4.GQEivi.zTGPvHv590JUSno24yFXtD6jlxKZdpoNY_p6B4"


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

async def startup(message):
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name='Instagram DMs'))
    instamsgs = wi.checkmsgs()
    with open("saved.json", "r") as f:
        saved = json.load(f)
    try:
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
        print("check successful")
    except Exception as e:
        print("Check Failed. See Error:" )
        print(e)
    await asyncio.sleep(60)

@bot.event
async def on_message(message):

    stopflag = False
    if message.content == 'test':
        await message.channel.send('Testing 1 2 3')

    if message.content == 'startup':
        await message.channel.send("Starting up!")
        while not stopflag:
            await startup(message)

    if message.content == 'stop':
        await message.channel.send("Stopping thread")
        stopflag = True

bot.run(token)

