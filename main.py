import asyncio
import json

import discord
from discord.ext import commands
from discord import guild


import DMstagram as dm

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

with open("sensitive_info.json", "r") as f:
    sensitiveinfo = json.load(f)

accountinfo = sensitiveinfo[0]
token = accountinfo['discordtoken']

webi = dm.dmstagram(accountinfo['instagramUsername'], accountinfo["instagramPassword"], accountinfo['mutedusers'])
webi.login()
insta_to_discord = sensitiveinfo[1]

discord_to_insta = {v:k for k, v in insta_to_discord.items()}




@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')


async def send_response(user, text):
    webi.respond(user, text)


@bot.command()
async def create_channel(ctx, channel_name): #todo fix duplicate channel creation
    guild = ctx.guild
    category = discord.utils.get(guild.categories, name="Instagram")
    channels = [i.name for i in bot.get_all_channels()]
    channels = channels[channels.index('Instagram') + 1:]

    print(channels)

    # replace "Instagram" with the name of your desired category

    if not (insta_to_discord[channel_name] in channels):
        print(f'Creating a new channel: {channel_name}')
        n = await guild.create_text_channel(channel_name, category=category)
        return n
    else:
        n = discord.utils.get(guild.channels, name=insta_to_discord[channel_name])
        print(n)
        return(n)
        print(f'A channel with the name "{channel_name}" already exists in the category "{category.name}".')




async def startup(message, n):
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name='Reading DMs'))
    instamsgs = webi.msgcheck()

    with open("saved.json", "r") as f:
        saved = json.load(f)
    # try:
    if instamsgs != saved and instamsgs != []:
        with open("saved.json", "w") as f:
            json.dump(instamsgs, f)

        print("instamsgs:")
        print(instamsgs)
        for i in instamsgs:
            c = await create_channel(message, i[0])
            await c.send(i[1])

    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name='Pink Floyd'))
    print(f"Checks: {n}\r", end='', flush=True)

async def refresh():
    webi.refresh_span_tags()


@bot.event
async def on_message(message):
    if message.content == '!test':
        await message.channel.send('Testing 1 2 3')

    if message.content == '!startup':
        n = 0
        await message.channel.send("Starting up!")

        while True:
            await startup(message, n)
            n += 1
            await asyncio.sleep(5)

    if message.content.startswith("respond"):
        await message.channel.send("Responding")
        str = message.content.split(',,')
        await send_response(str[1], str[2])

    if message.content == '!relogin':
        await message.channel.send(webi.relogin())
    if message.content == '!channel':
        await create_channel(message, 'test')
    if message.content == "!refresh":
        await refresh()


    if message.channel.category == discord.utils.get(message.guild.channels, name="Instagram") and not(message.author == bot.user):
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name='Sending DMs'))
        await send_response(discord_to_insta[message.channel.name], message.content)
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name='Patrick Bruel'))


bot.run(token)

