import os
import discord
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')
intents = Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)


@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    server = client.guilds[0]
    print(
        f'{client.user} is connected to the following guild: '
        f'{server.name}(id: {server.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await message.channel.send('Hello!')


if __name__ == '__main__':
    client.run(TOKEN)
