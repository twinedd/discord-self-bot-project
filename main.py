import discord, requests, random, os, time, logging, fade, datetime, asyncio
import speech_recognition as sr
from discord.ext import commands
from colorama import init, Fore
from selflib3 import *
from colorama import init
from bs4 import BeautifulSoup

client = commands.Bot(command_prefix='1', self_bot=True)

print(fade.purpleblue(tex))
print(fade.purpleblue(tex1))
for name in logging.Logger.manager.loggerDict.keys():
	logging.getLogger(name).setLevel(logging.CRITICAL)

# -- functions

def speech():
	mic = sr.Microphone()
	recog = sr.Recognizer()
	with mic as audio_file:
		print('Идет записывание...')
		recog.adjust_for_ambient_noise(audio_file)
		audio = recog.listen(audio_file)
		return recog.recognize_google(audio, language = 'ru-RU')

@client.command()
async def vcfind(ctx, method):
	await ctx.message.delete()
	list_ = []
	text = speech()
	resp = requests.get(f'https://www.google.com/search?q={text}&sca_esv=579651652&sxsrf=AM9HkKkXW4PvE1uEWdewQzXk7hKQRhQPJw%3A1699211670876&source=hp&ei=lulHZdvrMpP9wPAP6ZqReA&iflsig=AO6bgOgAAAAAZUf3ppmoOayI1YosEOvbIln-f_xf1uGn&ved=0ahUKEwjbjqfgyK2CAxWTPhAIHWlNBA8Q4dUDCAk&uact=5&oq=%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82&gs_lp=Egdnd3Mtd2l6IgzQv9GA0LjQstC10YIyDRAAGIAEGLEDGEYY-QEyCxAuGIAEGLEDGIMBMgsQABiABBixAxiDATILEC4YgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgUQABiABDIFEAAYgAQyBBAAGAMyBRAuGIAEMgsQLhiABBjHARivAUiNHVDjB1i_GXAEeACQAQCYAZABoAGlB6oBAzUuNLgBA8gBAPgBAagCCsICBxAjGOoCGCfCAgcQIxiKBRgnwgIIEAAYgAQYsQPCAgkQABiABBgKGAHCAg4QABiABBixAxgKGAEYKsICBxAAGIAEGArCAgsQABiKBRixAxiDAcICCxAuGIoFGLEDGIMBwgIIEC4YgAQYsQM&sclient=gws-wiz')
	soup = BeautifulSoup(resp.text, "lxml")
	bred = soup.find_all(method)
	for i in bred:
		list_.append(i.text)
	await ctx.send(f'`({method})` по запросу | `{text}` - ```{", ".join(list_)}```')

@client.command()
async def find(ctx, *, search: str):
    sp = search.split()
    count = 1
    try:
        int(sp[0])
        count = int(sp[0])
    except:
        pass
    if count == 1:
    	s = requests.get(f'https://www.bing.com/images/search?q={search}&form=HDRSC2&first=1')
    	q = BeautifulSoup(s.text,'lxml')
    	await ctx.send(content=f'{count} - фото | поиск по запросу | {search}')
    	for i in range(int(count)):
        	grab = q.findAll('img', 'mimg')[random.randint(1,10)].get('src')
        	await ctx.send(content=f'[.]({grab})')
    else:
    	s = requests.get(f'https://www.bing.com/images/search?q={search}&form=HDRSC2&first=1')
    	q = BeautifulSoup(s.text,'lxml')
    	await ctx.send(content=f'{count} - фото | поиск по запросу | {search}')
    	for i in range(int(count)):
        	grab = q.findAll('img', 'mimg')[i].get('src')
        	await ctx.send(content=f'[.]({grab})')

@client.command()
async def giffind(ctx, *, search):
	s = requests.get(f'https://tenor.com/ru/search/{search}-memes')
	q = BeautifulSoup(s.text,'lxml')
	for i in range(1,10):
		time.sleep(0.5)
		grab = q.findAll('img')[i].get('src')
		await ctx.send(content=f'[.]({grab})')

@client.command()
async def vc(ctx):
	await ctx.message.delete()
	text = speech()
	await ctx.send(text)

@client.command()
async def gping(ctx, user_id):
	await ctx.message.delete()
	await ctx.send('||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||<@' + str(user_id) + ">", delete_after = 0.01)

@client.command()
async def getf(ctx):
	print(Fore.MAGENTA + 'Your friends in this server')
	for i in ctx.guild.members:
		print(f'{Fore.BLUE}[+] {i}')
	print('\n------------\n')
	await ctx.message.delete()

@client.command()
async def emoji(ctx, messageid: int, word: str):
	msg =  await ctx.fetch_message(messageid)
	await ctx.message.delete()
	for i in word:
		await asyncio.sleep(.2)
		await msg.add_reaction(abc.get(i))

@client.command()
async def cemoji(ctx, messageid: int, channelid, word: str):
	chanel = client.get_channel(int(channelid))
	msg =  await chanel.fetch_message(messageid)
	await ctx.message.delete()
	for i in word:
		await asyncio.sleep(.2)
		await msg.add_reaction(abc.get(i))

@client.command()
async def femoji(ctx, word: str):
	list_ = ['']
	async for i in ctx.channel.history(limit=2):
		list_.append(i.id)
	message_ = await ctx.channel.fetch_message(int(list_[2]))
	await ctx.message.delete()
	for k in word:
		await asyncio.sleep(.2)
		await message_.add_reaction(abc.get(k))

@client.command()
async def avatar(ctx, userID: int):
	user = await client.fetch_user(userID)
	await ctx.send(str(user.avatar))
	await ctx.message.delete()

client.run(popa)

