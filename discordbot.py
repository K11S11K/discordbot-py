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
       
    if message.content.startswith(f'{PREFIX}웅덩이'):
        await message.channel.send('웅덩이

목차
1. 개요
2. 내용
3. 역사
4. 여담

통칭: 웅덩이
성별: 남성
세포 수: 2조 개 (추정)
소속: 대한민국 정부 WDI
상태: 활동 중

1. 개요
"웅"군의 볼기 부분에 위치해있는 작은 혹 따위의 형체.
그의 엉덩이는 이제 더이상 작지 않다.

"웅" - 자세한 내용은 웅/문서 참고

2. 내용
통칭 "웅덩이" 현대 인류가 해결하지 못한 물리적 법칙을 거스르는 신체의 일부분(형체)이다.
그것은 "웅"군의 엉덩이 부위에 위치해있으며 둘레는 평균 1972cm(제곱)이고, 그는 짱구의 엉덩이와 함께 엉덩이 걷기를 할 수 있는 개체이다.
현재 상태는 온도 73도로 매우 뜨겁고 둘레는 1963cm(제곱)으로 줄어들었기 때문에 정부에서 연구팀을 파견해 평균치로 복구하기에 노력중이다.

3. 역사
2000년대 초반 대한민국에서 웅이 태어났다.
그의 볼기 부분이 3살 무렵 급작스럽게 커지면서 인간의 모든 구성 세포를 포함한 값보다 더 많아졌다.
물리적 법칙과 자연의 법칙을 거스른 유전적 변이가 심하게 일어나자 정부에서도 연구팀 "WDI"를 파견해 연구중에 있다.
그의 볼기 부분의 연구명은 "웅덩이" 라고 불리고 그의 웅덩이는 실시간 라이브로 유튜브에서 관찰할 수 있다.

"WDI" - 자세한 내용은 WDI/문서 참고

4. 여담
한 돌팔이 연구팀에서 1954cm(제곱)이라고 주장하고 있지만, 이는 사실이 아니다. 정부가 파견한 WDI 연구팀에 따르면 그의 엉덩이는 현재 1963cm(제곱)으로
정확하게 확인하였고, 영양분 공급을 주기적으로 이루고 있어, 크기가 작아질 일은 거의 없다고 한다. ')
   
    if message.content.startswith(f'{PREFIX}에이스'):
        await message.channel.send('그는 에이스야!!')
        
    if message.content.startswith(f'{PREFIX}ppicu'):
        await message.channel.send('그는 피츄야!!')
        
    if message.content.startswith(f'{PREFIX}요키'):
        await message.channel.send('그는 요키야!!')
                                   
    if message.content.startswith(f'{PREFIX}웅이'):
        await message.channel.send('내가 누군지 알고 싶어?!')
                                   
    if message.content.startswith(f'{PREFIX}응'):
        await message.channel.send('가')
                                   
    if message.content.startswith(f'{PREFIX}오'):
        await message.channel.send('줌')
                                   
    if message.content.startswith(f'{PREFIX}ㅋ'):
        await message.channel.send('뭘 쪼개')
                                   
    if message.content.startswith(f'{PREFIX}야'):
        await message.channel.send('왜?')
                                   
    if message.content.startswith(f'{PREFIX}어쩌라고'):
        await message.channel.send('수듄ㅉㅉ')



try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
