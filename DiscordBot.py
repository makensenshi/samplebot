from typing import Text
import discord
from discord.ext import commands
import asyncio
import glob
import discord
import asyncio
client = discord.Client()
import discord, os



client = discord.Client()

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    activity = discord.Game(name="DO U LIKE VAPO BEAT?", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("起動完了")
    
@bot.command()
async def vapo(ctx):
     await ctx.send("VAPO VAPO VAPO")
     await ctx.send("https://www.youtube.com/c/McMaha")
     await ctx.send("Do u like vapo beat?")
     await ctx.send(":smile:")

@bot.command()
async def elna(ctx):
     await ctx.send("VAPO VAPO VAPO")
     await ctx.send("https://soundcloud.com/3runa")
     await ctx.send(":smile:")

 
@bot.command()
async def vapolist(ctx):
     await ctx.send("https://youtu.be/8KXGyczvAVI")
     await ctx.send("https://youtu.be/ubvsV93Eg68")
     await ctx.send("https://youtu.be/ysn45p70Sv8")
     await ctx.send("https://youtu.be/2rjLpN4qUZg")
     await ctx.send("https://youtu.be/1SNpid7oPxc")
     await ctx.send("https://youtu.be/DHuwoQetbWI")
     
@bot.command()
async def WS(ctx):
     await ctx.send("https://youtu.be/hhbhHFwrRCQ")
     
bot.run("TOKEN") #PASTE YOUR TOKEN
