import discord
from discord.ext import commands

bot = commands.Bot(command_prefix ='!')

@bot.event
async def on_ready():
    print (">>> Bot is online <<<")

@bot.event
async def on_member_join(member):
    print (f'{member} join!')
    channel = bot.get_channel(617715046646022144)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print (f'{member} leave!')
    channel = bot.get_channel(617715147066310686)
    await channel.send(f'{member} join!')

bot.run("NjE3NTgzNzA4ODk1MDUxNzc2.XWtZCQ.zL5CmTV4FI3eVBoHOP_QTkIJxWc")