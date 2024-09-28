import discord, requests, random, os, time, logging, fade, asyncio, urllib.request
from discord.ext import commands
from colorama import init, Fore
from selflib3 import *
from colorama import init
from bs4 import BeautifulSoup

client = commands.Bot(command_prefix='1', self_bot=True)
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

# -- functions

@client.command()
async def find(ctx, *, search: str):
	soup = BeautifulSoup(requests.get(f'https://www.bing.com/images/search?q={" ".join(sp)}&form=HDRSC2&first=1').text,'lxml')
	sp = search.split()
	count = 1
	try:
		int(sp[0])
		count = int(sp[0])
		sp.pop(0)
	except:
		pass
	if count == 1:
		await ctx.send(f'{count} - фото | поиск по запросу | {" ".join(sp)}')
		grab = soup.findAll('img', 'mimg')[random.randint(1,10)].get('src')
		await ctx.send(f'[.]({grab})')
	else:
		await ctx.send(f'{count} - фото | поиск по запросу | {" ".join(sp)}')
		for i in range(int(count)):
			grab = soup.findAll('img', 'mimg')[i].get('src')
			list_ = []
			list_.append(f'[.]({grab})')
		await ctx.send(" ".join(list_))

@client.command()
async def gif(ctx, search):
	await ctx.send(BeautifulSoup(requests.get(f'https://tenor.com/ru/search/{search}-memes').text,'lxml').findAll('img')[random.randint(1,40)].get('src'))

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
	soup = BeautifulSoup(requests.get('https://www.accuweather.com/ru/world-weather', headers=hdr).text,'lxml')
	city = soup.findAll('span', 'text title no-wrap')
	temp = soup.findAll('span', 'text temp')
	for i_ in range(0, len(city)):
		x = str(f'{city[i_].text} ')
		x += str(f'{temp[i_].text}')
	await ctx.send(f'```{x}```')

@client.command()
async def music(ctx, *, name):
	channel = ctx.channel
	await ctx.message.delete()
	soup = BeautifulSoup(requests.get(f'https://rus.hitmotop.com/search?q={name}', headers=hdr).text,'lxml')
	artist = soup.findAll('div', 'track__desc')
	music_name = soup.findAll('div', 'track__title')

	for i_ in range(0,len(artist)):
		if i_ < 11:
			result = str(f'```{i_} {artist[i_].text} - {" ".join(music_name[i_].text.split())}` \n```')
		else:
			break
	mes_ = await ctx.send(result)

	def check(m):
		return m.channel == channel
	try:
		message = await client.wait_for('message', timeout=30, check=check)
	except asyncio.TimeoutError:
		await ctx.send('Превышено время ожидания')

	await mes_.delete(), message.delete()
	url = soup.findAll('a', 'track__download-btn')[int(message.content)].get('href')
	file_name = url.split('/')[6]
	urllib.request.urlretrieve(url, file_name)
	await ctx.send(content = f'```{artist[int(message.content)].text} - {" ".join(soup.findAll('div', 'track__title')[int(message.content)].text.split())}```', file=discord.File(file_name))


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
