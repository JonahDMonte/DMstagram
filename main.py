import discord
from discord.ext.commands import Bot
from discord.ext import commands
import webinteractions as wi
from discord.ext import tasks
from printsleep import printsleeptime
import threading
import typing
import functools

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
token = "Njk3MTY0OTQ2MDkzMzc1NTE4.GM5J5Q.lMiBeSiQ20IW0iY2VFpR2olM0rgWQxTc9uxIYw"
stopflag = False

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')


@bot.event
async def on_message(message):
    if message.content == 'test':
        await message.channel.send('Testing 1 2 3')
@bot.event
async def on_message(message):
    if message.content == 'stop':
        await message.channel.send("Stopping thread")
        stopflag = True


async def startup(message):
        instamsgs = wi.checkmsgs()
        print(instamsgs)
        embed = discord.Embed(title='Unread Messages', color=0xfc00bf)
        print("building embed")

        embed.set_author(name='DMstagram',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/2048px-Instagram_icon.png',
                         url='https://www.instagram.com/direct/inbox/')

        for i in instamsgs:
            embed.add_field(name=i[0], value=i[1], inline=False)

        await message.channel.send(embed=embed)
        printsleeptime(899, 901)

@bot.event
async def on_message(message):
    if message.content == 'startup':
        await message.channel.send("Starting up!")
        while not stopflag:
            await startup(message)

bot.run(token)

