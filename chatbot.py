'''
Simla discord bot teszteléshez
'''

__author__ = 'Boda Zsolt'

import discord
from discord.ext import commands
from typing import List
from random import choice

TOKEN = 'token'

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Sikeres bejelentkezés {0.user}!'.format(client))


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')


@client.command(aliases=['praise_me', 'like'])
async def praise(ctx):
    praises: List[str] = [
        'You are the best',
        'The coolest dude',
        'The most handsome devil ever'
    ]

    await ctx.send(choice(praises))

client.run(TOKEN)