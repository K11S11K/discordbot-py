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

    if message.content == f'{PREFIX}안녕':
        await message.channel.send('안녕하세요 첨단 기술로 만들어진 웅봇입니다!')
        
    if message.content == f'{PREFIX}ksk':
        await message.channel.send('저를 로봇화 시켜준 분입니다!')
        
    if message.content == f'{PREFIX}루한':
        await message.channel.send('저의 주인입니다!')
       
    if message.content == f'{PREFIX}웅덩이':
        await message.channel.send('너무 커!!!!! 1972cm야!!!!!!!! 물론 둘레가!!!!!!!!')
   
    if message.content == f'{PREFIX}에이스':
        await message.channel.send('그는 에이스야!!')
        
    if message.content == f'{PREFIX}ppicu':
        await message.channel.send('그는 피츄야!!')
        
    if message.content == f'{PREFIX}요키':
        await message.channel.send('그는 요키야!!')
                                   
    if message.content == f'{PREFIX}웅이':
        await message.channel.send('내가 누군지 알고 싶어?!')
                                   
    if message.content == f'{PREFIX}응':
        await message.channel.send('가')
                                   
    if message.content == f'{PREFIX}오':
        await message.channel.send('줌')
                                   
    if message.content == f'{PREFIX}ㅋ':
        await message.channel.send('뭘 쪼개')
                                   
    if message.content == f'{PREFIX}야':
        await message.channel.send('왜?')
                                   
    if message.content == f'{PREFIX}어쩌라고':
        await message.channel.send('수듄ㅉㅉ')
        
    if message.content == f'{PREFIX}크스크':
        await message.channel.send('@ksk')

    if message.content == f'{PREFIX}와':
        await message.channel.send('샌즈')
        
    if message.content == f'{PREFIX}ㄹㅇ':
        await message.channel.send('ㅋㅋ')
        
    if message.content == f'{PREFIX}오레조레':
        await message.channel.send('요리조리')

    if message.content == f'{PREFIX}고백 받아본적 있어?':
        await message.channel.send('알려줘?')
        
    if message.content == f'{PREFIX}Ohio':
        await message.channel.send('woong in Ohio')

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
