import discord, music, os
from discord.ext import commands
from keep_alive import keep_alive

cogs = [music]

client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

token = os.environ['TOKEN']

# start web server
keep_alive()
# start bot
client.run(token)