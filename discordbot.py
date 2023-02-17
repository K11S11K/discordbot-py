from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}안녕'):
        await message.channel.send('안녕하세요 첨단 기술로 만들어진 웅봇입니다!')
        
    if message.content.startswith(f'{PREFIX}ksk'):
        await message.channel.send('저를 로봇화 시켜준 분입니다!')
        
    if message.content.startswith(f'{PREFIX}루한'):
        await message.channel.send('저의 주인입니다!')


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
