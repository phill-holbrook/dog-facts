import json
from discord.ext import commands
import requests
import os
import random
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='/', case_insensitive=True)
token = os.environ.get('TOKEN')

@bot.command(name='DogFact')
async def getDogFact(ctx):

    factid = str(random.randint(1,430))
    url = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?index=" + factid
    r = requests.get(url)
    fact = "Dog Fact #" + factid + ": " + json.loads(r.text)[0]["fact"]

    await ctx.send(fact)

@bot.command(name='CatFact')
async def getCatFact(ctx):

    factid = str(random.randint(1,430)) #The fact id is just completely random lol
    url = "https://catfact.ninja/fact"
    r = requests.get(url)
    fact = "Cat Fact #" + factid + ": " + json.loads(r.text)["fact"]

    await ctx.send(fact)

bot.run(token)