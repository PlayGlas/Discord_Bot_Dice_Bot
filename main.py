import discord
from discord.ext import commands

nbtest = int(0)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ajouter1(ctx):
    nbtest =+1
    print(nbtest)
    await ctx.send('ajouter 1 à nbtest')

@bot.command()
async def print_nbtest(ctx):
    await ctx.send('la valeur de nbtest est ' + str(nbtest))
    print(nbtest)

@bot.command()
async def test(ctx):
    await ctx.send('test validé')
    await ctx.send("content")
    print("message envoyer")
@bot.command()
async def lien(ctx):
    await ctx.send('https://pypi.org/project/discord.py/')
    print("lien envoyer")

bot.run('ODc3ODU1MjA5Nzk4MzgxNTg5.Gsu-m8.uyZMkEbopbgdQqYxGLij2VzlKbLrVL0F64Fesk')