import discord
from discord.ext import commands
import json
import random
import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time
import re
from google_images_download import google_images_download

with open("setting.json","r", encoding='utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix ='!')

@bot.event
async def on_ready():
    print (">>> Bot is online <<<")

@bot.event
async def on_member_join(member):
    print (f'{member} join!')
    channel = bot.get_channel(int(jdata['welcome_ch']))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print (f'{member} leave!')
    channel = bot.get_channel(int(jdata['Leave_ch']))
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

@bot.command()
async def 鏡華(ctx):
   
    rootdir = "C:\\Users\\Dragon\\Documents\\GitHub\\discord-bot\\downloads\\鏡華"
    if os.path.exists(rootdir) == False:
        os.system('googleimagesdownload -k \"鏡華\" -l \"30\" -f \"jpg\" -e')
    
    file_names =[]
    for parent, dirnames, filenames in os.walk(rootdir):
        file_names = filenames
    
    p = random.randint(0,len(file_names)-1)
    pic = discord.File('C:\\Users\\Dragon\\Documents\\GitHub\\discord-bot\\downloads\\鏡華\\'+file_names[p])
    await ctx.send(file=pic)

@bot.command()
async def 小望(ctx):
   
    rootdir = "C:\\Users\\Dragon\\Documents\\GitHub\\discord-bot\\downloads\\小望"
    if os.path.exists(rootdir) == False:
        os.system('googleimagesdownload -k \"小望\" -l \"50\" -f \"jpg\" -e')
    
    file_names =[]
    for parent, dirnames, filenames in os.walk(rootdir):
        file_names = filenames
    
    p = random.randint(0,len(file_names)-1)
    pic = discord.File('C:\\Users\\Dragon\\Documents\\GitHub\\discord-bot\\downloads\\小望\\'+file_names[p])
    await ctx.send(file=pic)


bot.run(jdata['TOKEN'])