import discord
import os
from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.default())

print('ddddd 1')

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    emoji ="👍"
    await message.add_reaction(emoji)

print('ddddd 2')

TOKEN = os.getenv("DISCORD_TOKEN")

print('ddddd 3')

print(TOKEN)

# Web サーバの立ち上げ
keep_alive()

print('ddddd 4')

client.run(TOKEN)

print('ddddd 5')
