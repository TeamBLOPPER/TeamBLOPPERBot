import discord
from discord.ext.commands import Bot
from discord.ext import commands
from pathlib import Path
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot is alive and connected!")

@client.command(pass_context = True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount + 1)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.send_message(channel, amount + " messages has been cleared!")

#OVERWATCH
@client.command(pass_context = True)
async def newowt(ctx, name, date, time):
    channel = ctx.message.channel
    if "518184827271512085" in [role.id for role in ctx.message.author.roles]:
        my_file = Path("Overwatch{0}".format(name))
        if my_file.is_file() == False:
            file = open("Overwatch{0}".format(name), "w+")
        await client.send_message(channel, "@everyone **New OVERWATCH Tournament!** \n\n**TOURNAMENT NAME**\n{0}\n\n**DATE   YYYY/MM/DD**\n{1}  \n\n**TIME (CET)**\n{2} \n\n**SIGN LIKE THIS** \n.signow (Your name) {0}".format(name, date, time))
    else:
        await client.send_message(channel, "You Don't Have The Premission To Execute This Command!")

@client.command(pass_context = True)
async def signow(ctx, name, turre):
    channel = ctx.message.channel
    my_file = Path("Overwatch{0}".format(turre))
    if my_file.is_file():
        with open("Overwatch{0}".format(turre), "a") as f:
            print(name, file=f)
        await client.send_message(channel, "You signed up!")
    else:
        await client.send_message(channel, "Please Create The Tournament First")

#QUAKE CHAMPIONS
@client.command(pass_context = True)
async def newqt(ctx, name, date, time):
    channel = ctx.message.channel
    if "518184827271512085" in [role.id for role in ctx.message.author.roles]:
        my_file = Path("Quake{0}".format(name))
        if my_file.is_file() == False:
            file = open("Quake{0}".format(name), "w+")
        await client.delete_message(ctx.message)
        await client.send_message(channel, "@everyone **New QUAKE CHAMPIONS Tournament!** \n\n**TOURNAMENT NAME**\n{0}\n\n**DATE   YYYY/MM/DD**\n{1}  \n\n**TIME (CET)**\n{2} \n\n**SIGN LIKE THIS** \n.signow (Your name) {0}".format(name, date, time))
    else:
        await client.send_message(channel, "You Don't Have The Premission To Execute This Command!")

@client.command(pass_context = True)
async def signq(ctx, name, turre):
    channel = ctx.message.channel
    my_file = Path("Quake{0}".format(turre))
    if my_file.is_file():
        with open("Quake{0}".format(turre), "a") as f:
            print(name, file=f)
        await client.send_message(channel, "@{0} signed up!".format(ctx.message.author.mention))
    else:
        await client.send_message(channel, "Please Create The Tournament First")
	
client.run("NTE4MjIyOTY4NjQwMjQxNzA0.DuNo6Q.KC_ATKB8VF9Qu5-AILAUvL94MuQ")
