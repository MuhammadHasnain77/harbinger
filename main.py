import discord
import os
import logging
import random
import sys
from helpers import timestamp, getVer, getLog
from urllib.parse import urlencode, urlparse, parse_qs
from lxml.html import fromstring
from requests import get
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
load_dotenv()

purple = 0x884EA0

TOKEN = os.getenv("TOKEN")
VERSION = getVer()
sTime = datetime.now()


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
channel = bot.get_channel(1165826071447486584)


@bot.event
async def on_ready():
    """Print username and ID on successful login."""
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    timestamp()

@bot.command()
async def clear(ctx, amount=2):
    amount = amount + 1
    if amount > 101:
        await ctx.send('Cannot delete more than 100 messages.')
    else:
        await ctx.channnel.purge(limit=amount)
        await ctx.send('Cleared messages.')


@bot.command()
async def changelog(ctx):
    """Send the changelog as a message and print it to console."""
    changelog = getLog()
    print("Getting changelog...")
    print(f"{changelog}")
    timestamp()
    await ctx.send(f"{changelog}")


@bot.command()
async def status(ctx):
    """Send message to confirm connection successful."""
    print(f"{bot.user} is online.")
    timestamp()
    await ctx.send(f"{bot.user} is online.")


@bot.command()
async def add(ctx, left: int, right: int):
    """Add two integers and return total as message.

    Args:
        left (int): first addend
        right (int): second addend
    """
    total = left + right
    print(f"Adding {left} and {right}.")
    print(f"Total = {total}")
    timestamp()
    await ctx.send(total)


@bot.command()
async def say(ctx, message: str):
    """Repeat the message received as an argument.

    Args:
        message (str): Text of the message to be said by the bot
    """
    print("BOT SAYS:")
    print(f"{message}")
    await ctx.send(message)


@bot.command()
async def roll(ctx, dice: str):
    """Roll XdY dice and return result(s) as message.

    Args:
        dice (str): amount of n-sided dice to roll (NdN)
    """
    print("Rolling dice...")
    try:
        rolls, limit = map(int, dice.split("d"))
    except Exception:
        logging.warn(f"Bad format: {dice}")
        await ctx.send("Format must be NdN!")
        return
    result = ", ".join(str(random.randint(1, limit)) for r in range(rolls))
    print(result)
    timestamp()
    await ctx.send(result)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Return datetime a particular user joined the channel.

    Args:
        member (discord.Member): The name of the member to be looked up.
    """
    print(f"Join on {member.name}")
    timestamp()
    await ctx.send(f"{member.name} joined {discord.utils.format_dt(member.joined_at)}")


@bot.command()
async def info(ctx):
    """Returns detailed information about current bot version."""
    cTime = datetime.now()
    delta = cTime - sTime
    embedVar = discord.Embed(title="mcswitch", color=purple)
    embedVar.add_field(name="version", value=f"v{VERSION}", inline=True)
    embedVar.add_field(name="uptime", value=f"{delta}", inline=True)
    embedVar.add_field(name="author", value="notoriouslogank", inline=True)
    embedVar.add_field(
        name="source code", value="https://github.com/notoriouslogank/mcswitch"
    )
    print(f"info dumped")
    timestamp()
    await ctx.send(embed=embedVar)


@bot.command()
async def ping(ctx):
    """Returns current network latency."""
    print(f"pinged")
    timestamp()
    await ctx.send("Current ping: {0}".format(round(bot.latency, 2)))


@bot.command()
async def uptime(ctx):
    """Returns the uptime of the current bot instance."""
    cTime = datetime.now()
    delta = cTime - sTime
    print(f"uptime: {delta}")
    timestamp()
    await ctx.send(f"Uptime: {delta}")


@bot.command()
async def shutdown(ctx):
    """Safely shutdown the bot instance."""
    embedShutdown = discord.Embed(
        title="Shutdown", color=0xFF0000, timestamp=datetime.now()
    )
    embedShutdown.add_field(name="user", value=f"{ctx.message.author}", inline=True)
    logging.warn(f"Shutting down!")
    print("Shutdown command received!")
    timestamp()
    await ctx.send(embed=embedShutdown)
    sys.exit()


# @bot.command()
# async def mcstart(ctx):
#    await os.system("sh mc.sh")
#    print("Starting the server, maybe.")
#    await ctx.send("Starting MC Server.")


@bot.command()
async def rps(ctx, choice: str):
    """Play a game of rock, paper, scissors with the bot.

    Args:
        choice (str): rock, paper, or scissors
    """
    print(f"played rps")
    timestamp()
    choices = ["rock", "paper", "scissors"]
    botChoice = choices[random.randint(0, 2)]
    embedRPS = discord.Embed(color=purple, title="rock, paper, scissors")
    embedRPS.add_field(name="You", value=f"{choice}", inline=True)
    embedRPS.add_field(name="Bot", value=f"{botChoice}", inline=True)
    if choice == botChoice:
        embedRPS.add_field(name="result", value="You tied!", inline=False)
        await ctx.send(embed=embedRPS)
    elif botChoice == "rock" and choice == "paper":
        embedRPS.add_field(name="result", value="You win!", inline=False)
        await ctx.send(embed=embedRPS)
    elif botChoice == "paper" and choice == "scissors":
        embedRPS.add_field(name="result", value="You win!", inline=False)
        await ctx.send(embed=embedRPS)
    elif botChoice == "scissors" and choice == "rock":
        embedRPS.add_field(name="result", value="You win!", inline=False)
        await ctx.send(embed=embedRPS)
    else:
        embedRPS.add_field(name="result", value="You lose!", inline=False)
        await ctx.send(embed=embedRPS)


@bot.command()
async def lmgtfy(ctx, query: str):
    """Passive-aggressively Google something. Returns embed with URL.

    Args:
        query (str): string to be Googled
    """
    google = "https://google.com/search?q="
    search = google + query
    embed = discord.Embed(color=purple, title="LMGTFY")
    embed.description = f"[Here]({search}), let me Google that for you!"
    print(f"LMGTFY: {search}")
    timestamp()
    await ctx.send(embed=embed)
    

#@bot.event
#async def on_message(message):
#    if message.author.id == bot.user.id:
#        return
#    msg_content = message.content.lower()
#    
#    curseWord = ['palestine']
#    
#    if any(word in msg_content for word in curseWord):
#        await message.delete()

bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
