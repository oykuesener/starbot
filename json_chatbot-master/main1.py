import discord
from discord.ext import commands
from main import get_response

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ask(ctx, *question ):
    str = ''
    for item in question:
        str = str + ' ' + item
    
    response = get_response(str)
    await ctx.send(response)

@bot.command()
async def latte(ctx):

    with open('images/ice-latte-1024x683.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def americano(ctx):

    with open('images/americano.webp', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def whitechocolatemocha(ctx):

    with open('images/2102020-White-Chocolate-Mocha-164058.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def turkkahvesi(ctx):

    with open('images/turk_kahvesinin_faydalari_nelerdir_turk_kahvesi_zayiflatir_mi_1659337199_0182.jpg.webp', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def meksikan(ctx):

    with open('images/los-altos-gourmet-mexicano-4.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def japon(ctx):

    with open('images/IMG_2603.jpg.webp', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def italyan(ctx):

    with open('images/TERAS5762.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    

bot.run("MTIyNTUyNTk2NzYzMjQ2NjAzNA.GCXdcV.p-PfemhWHIIpPRe3h75bprMlCqfopQcslXWRzE")