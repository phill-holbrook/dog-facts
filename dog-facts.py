import json
from nextcord.ext import commands
import requests
import os
import random
from dotenv import load_dotenv
import nextcord
import logging
import subprocess

logger = logging.getLogger('nextcord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='/discord-bot/dog-facts/dogfacts.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = nextcord.Intents.default()
intents.message_content = True

load_dotenv()

bot = commands.Bot(case_insensitive=True, intents=intents)
token = os.environ.get('TOKEN')

@bot.slash_command(name='help', description='Get help with DogFacts!')
async def getHelp(ctx):

    resp = 'Current supported commands:\n- `/dogfact`: Gets a random fact about dogs.\n- `/catfact`: Gets a random fact about cats.\n- `/help`: Shows this message.\n- `/about`: Shows information about me.'

    await ctx.send(resp)

@bot.slash_command(name='uptime')
async def uptime(ctx):
    
    process = subprocess.Popen(['systemctl', 'status', 'dogfacts'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    output_str = output.decode('utf-8')

    grep_process = subprocess.Popen(['grep', 'Active'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    grep_output, grep_error = grep_process.communicate(input=output_str.encode('utf-8'))
    resp = grep_output.decode('utf-8')  

    await ctx.send(resp)

@bot.slash_command(name='about', description='Get information about DogFacts!')
async def get_about(ctx):
    resp = 'Hi! I\'m **DogFacts**. My creator made me as part of a side project to learn about Python, GitHub Actions, and AWS CodePipeline. To see what commands I currently support, use `/help`.\n\nSee my source code here: https://github.com/phill-holbrook/dog-facts'
    await ctx.send(resp)

@bot.slash_command(name='dogfact', description='Get a DogFact!')
async def getDogFact(ctx):

    factid = str(random.randint(1,1000)) #The fact id is just completely random lol
    url = "https://dog-api.kinduff.com/api/facts"
    r = requests.get(url)
    fact = "**Dog Fact #" + factid + ":** " + json.loads(r.text)["facts"][0]

    await ctx.send(fact)

@bot.slash_command(name='catfact', description='Get a CatFact!')
async def getCatFact(ctx):

    factid = str(random.randint(1,1000)) #The fact id is just completely random lol
    url = "https://catfact.ninja/fact"
    r = requests.get(url)
    fact = "**Cat Fact #" + factid + ":** " + json.loads(r.text)["fact"]

    await ctx.send(fact)

bot.run(token)