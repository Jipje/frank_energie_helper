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

client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    server = client.guilds[0]
    print(
        f'{client.user} is connected to the following guild: '
        f'{server.name}(id: {server.id})'
    )


@client.command()
async def get_prices(ctx):
    await ctx.send("I don't know anything about energy prices yet.")


@client.command()
async def current_price(ctx):
    await ctx.send("I don't know what the current energy price is.")


if __name__ == '__main__':
    client.run(TOKEN)
