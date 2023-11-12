import json
from discord.ext import commands
import requests
import os
import random
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='!', case_insensitive=True)
token = os.environ.get('TOKEN')

@bot.remove_command('help')
@bot.command(name='help')
async def getHelp(ctx):

    resp = 'Current supported commands:\n - `!dogfact`: Gets a random fact about dogs.\n - `!catfact`: Gets a random fact about cats.\n - `!help`: Shows this message.\n - `!about`: Shows information about me.'

    await ctx.send(resp)

# @bot.command(name='about')
# async def getAbout(ctx):

#     resp = 'Hi! I\'m **DogFacts**. My creator made me as part of a side project to learn about Python, GitHub Actions, and AWS CodePipeline. To see what commands I currently support, use `!help`. \n\n See my source code here: https://github.com/phill-holbrook/dog-facts'

#     await ctx.send(resp)

@bot.slash_command(name='about', description='Get information about the bot.')
async def get_about(ctx):
    resp = 'Hi! I\'m **DogFacts**. My creator made me as part of a side project to learn about Python, GitHub Actions, and AWS CodePipeline. To see what commands I currently support, use `/help`.\n\nSee my source code here: https://github.com/phill-holbrook/dog-facts'
    await ctx.send(resp)

@bot.command(name='DogFact')
async def getDogFact(ctx):

    factid = str(random.randint(1,1000)) #The fact id is just completely random lol
    url = "https://dog-api.kinduff.com/api/facts"
    r = requests.get(url)
    fact = "**Dog Fact #" + factid + ":** " + json.loads(r.text)["facts"][0]

    await ctx.send(fact)

@bot.command(name='CatFact')
async def getCatFact(ctx):

    factid = str(random.randint(1,1000)) #The fact id is just completely random lol
    url = "https://catfact.ninja/fact"
    r = requests.get(url)
    fact = "**Cat Fact #" + factid + ":** " + json.loads(r.text)["fact"]

    await ctx.send(fact)

bot.run(token)