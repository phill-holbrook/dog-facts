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
    url = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?index=" + str(random.randint(1,430))
    r = requests.get(url)
    fact = json.loads(r.text)[0]["fact"]

    await ctx.send(fact)

bot.run(token)