import os
import discord
from discord import Intents
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client(intents=Intents())


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


def send_message_to_discord():
    pass


if __name__ == '__main__':
    send_message_to_discord()
    client.run(TOKEN)
