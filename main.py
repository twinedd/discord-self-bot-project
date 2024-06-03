import discord, requests, random, os, time, logging, fade, asyncio, urllib.request
import speech_recognition as sr
from discord.ext import commands
from colorama import init, Fore
from selflib3 import *
from colorama import init
from bs4 import BeautifulSoup

client = commands.Bot(command_prefix='1', self_bot=True)
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

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
async def voicefind(ctx, method):
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
	list_ = []
	sp = search.split()
	count = 1
	try:
		int(sp[0])
		count = int(sp[0])
		sp.pop(0)
	except:
		pass
	if count == 1:
		s = requests.get(f'https://www.bing.com/images/search?q={" ".join(sp)}&form=HDRSC2&first=1')
		q = BeautifulSoup(s.text,'lxml')
		await ctx.send(content=f'{count} - фото | поиск по запросу | {" ".join(sp)}')
		grab = q.findAll('img', 'mimg')[random.randint(1,10)].get('src')
		await ctx.send(content=f'[.]({grab})')
	else:
		s = requests.get(f'https://www.bing.com/images/search?q={" ".join(sp)}&form=HDRSC2&first=1')
		q = BeautifulSoup(s.text,'lxml')
		await ctx.send(content=f'{count} - фото | поиск по запросу | {" ".join(sp)}')
		for i in range(int(count)):
			grab = q.findAll('img', 'mimg')[i].get('src')
			list_.append(f'[.]({grab})')
		await ctx.send(content=" ".join(list_))

@client.command()
async def gid(ctx, *, search):
	s = requests.get(f'https://tenor.com/ru/search/{search}-memes')
	q = BeautifulSoup(s.text,'lxml')
	time.sleep(0.5)
	grab = q.findAll('img')[random.randint(1,40)].get('src')
	await ctx.send(content=f'[.]({grab})')

@client.command()
async def voice(ctx):
	await ctx.message.delete()
	text = speech()
	await ctx.send(text)

@client.command()
async def ghostping(ctx, user_id):
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

@client.command()
async def weather(ctx):
	await ctx.message.delete()
	x = ''
	q = BeautifulSoup(requests.get('https://www.accuweather.com/ru/world-weather', headers=hdr).text,'lxml')
	city = q.findAll('span', 'text title no-wrap')
	temp = q.findAll('span', 'text temp')
	for i_ in range(0, len(city)):
		x += str(f'{city[i_].text} ')
		x += str(f'{temp[i_].text}')
	await ctx.send(f'```{x}```')

@client.command()
async def music(ctx, *, name):
	channel = ctx.channel
	cool = ''
	await ctx.message.delete()
	s = requests.get(f'https://rus.hitmotop.com/search?q={name}', headers=hdr)
	q = BeautifulSoup(s.text,'lxml')
	artist = q.findAll('div', 'track__desc')
	music_name = q.findAll('div', 'track__title')
	for i_ in range(0,len(artist)):
		if i_ < 11:
			music_name_ = music_name[i_].text.split()
			cool += str(f'```{i_} {artist[i_].text} - {" ".join(music_name_)}` \n```')
		else:
			break
	mes_ = await ctx.send(cool)
	def check(m):
		return m.channel == channel
	try:
		message = await client.wait_for('message', timeout=30, check=check)
	except asyncio.TimeoutError:
		await ctx.send('Превышено время ожидания')
	await mes_.delete()
	await message.delete()
	url = q.findAll('a', 'track__download-btn')[int(message.content)].get('href')
	file_name = url.split('/')[6]
	urllib.request.urlretrieve(url, file_name)
	music_name__ = q.findAll('div', 'track__title')[int(message.content)]
	gusic_name = music_name__.text.split()
	await ctx.send(content = f'```{artist[int(message.content)].text} - {" ".join(gusic_name)}```', file=discord.File(file_name))


@client.command()
async def phonk(ctx):
	await ctx.message.delete()
	list_ = ['https://rus.hitmotop.com/genre/209','https://rur.hitmotop.com/genre/209/start/48','https://rus.hitmotop.com/genre/209/start/96','https://rus.hitmotop.com/genre/209/start/144','https://rus.hitmotop.com/genre/209/start/192','https://rus.hitmotop.com/genre/209/start/240','https://rus.hitmotop.com/genre/209/start/288','https://rus.hitmotop.com/genre/209/start/336','https://rus.hitmotop.com/genre/209/start/384','https://rus.hitmotop.com/genre/209/start/432']
	lenght = len(list_) - 1
	number_ = random.randint(0,lenght)

	page = BeautifulSoup(requests.get(f'{list_[number_]}', headers=hdr).text,'lxml')
	pesna = random.randint(0,45)
	url = page.findAll('a', 'track__download-btn')[pesna].get('href')

	artist = page.findAll('div', 'track__desc')[pesna]
	music_name = page.findAll('div', 'track__title')[pesna]
	music_name = music_name.text.split()
	urllib.request.urlretrieve(url, url.split('/')[6])

	await ctx.send(content = f'```страница - {number_} | {artist.text} - {" ".join(music_name)} {pesna}```', file=discord.File(url.split('/')[6]))

@client.command()
async def animation(ctx, channelid: int, messageid: int, word):
	chanel = client.get_channel(channelid)
	msg =  await chanel.fetch_message(messageid)
	await ctx.message.delete()
	while True:
		for i in word:
			await asyncio.sleep(.3)
			await msg.add_reaction(abc.get(i))
		for k in reversed(word):
			await asyncio.sleep(.3)
			await msg.remove_reaction(abc.get(k), client.user)

@client.command()
async def breakchat(ctx, channelid: int):
	list_ = []
	chanel = client.get_channel(channelid)
	async for i in chanel.history(limit=7):
		list_.append(i)
	for i in list_:
		await i.add_reaction('🔑')
		await asyncio.sleep(.4)
		await i.remove_reaction('🔑', client.user)
client.run(tok)
