import random
from disnake.ext import commands

import os
from dotenv import load_dotenv

load_dotenv("secret.env")

bot = commands.Bot(command_prefix="&", test_guilds=[943739589326155788, 883045046029516880])

@bot.event
async def on_ready():
    print("The bot is ready!")

# load commands

bot.load_extension("cogs.help")
bot.load_extension("cogs.ping")
bot.load_extension("cogs.info")
bot.load_extension("cogs.roll")
bot.load_extension("cogs.slots")
bot.load_extension("cogs.poll")

# events

@bot.event
async def on_message(message):
    if (message.author.id == bot.user.id):
        return
    if (("need" in message.content and "essay" in message.content) or ("have" in message.content and "essay" in message.content)):
        messageResponse = int(random.random()*3) + 1
        if(messageResponse == 1):
            await message.reply("Top quality essay writing DM me")
        if(messageResponse == 2):
            await message.reply("DM for cheap essay writing")
        if(messageResponse == 3):
            await message.reply("If you need essay DM me fast")
    
    if (message.content.endswith("I'm dad!")):
        await message.reply("Hi dad, that's enough...")

YOUR_BOT_TOKEN = os.environ["YOUR_BOT_TOKEN"]
bot.run(YOUR_BOT_TOKEN)