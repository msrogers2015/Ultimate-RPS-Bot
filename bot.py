# invite link: https://discord.com/api/oauth2/authorize?client_id=785983710361026561&permissions=75776&scope=bot
import discord, os, random
from discord.ext import commands
from dotenv import load_dotenv
import data.matrix as m
import data.moves as o

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix='rps')
client.remove_command('help')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(
       activity=discord.Activity(type=discord.ActivityType.watching,
       name=str(len(client.guilds)) + " servers | rpshelp")
    )

@client.command()
async def invite_link(ctx):
    await ctx.send('<https://discord.com/api/oauth2/authorize?client_id=785983710361026561&permissions=75776&scope=bot>')


@client.command()
async def source(ctx):
    await ctx.send('<https://discord.com/api/oauth2/authorize?client_id=785983710361026561&permissions=75776&scope=bot>')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)} ms')

@client.command()
async def support(ctx):
    embed = discord.Embed(title='Support the Dev!')
    embed.add_field(name="Patreon", value='https://www.patreon.com/QuailWare')
    embed.add_field(name="Github", value='https://github.com/msrogers2015')
    embed.add_field(name='Website', value='https://msrogers2015.github.io/')
    await ctx.send(embed=embed)



@client.command(help="Normal game of rock paper scissors")
async def g3(ctx, *, pmove):
    if pmove.title() in o.rps3:
        bmove = random.choice(o.rps3)
        pv = o.rps3.index(pmove.title())
        bv = o.rps3.index(bmove)
        outcome = m.rps3[pv][bv]
        
        if outcome[1] == -1:
            await ctx.send(f'{bmove} {outcome[0]} {pmove.title()}: {ctx.author.mention} lost!')
        if outcome[1] == 0:
            await ctx.send(f'{pmove.title()} {outcome[0]} {bmove}!')
        if outcome[1] == 1:
            await ctx.send(f'{pmove.title()} {outcome[0]} {bmove}: {ctx.author.mention} won!')
    if pmove.title() not in o.rps3:
        await ctx.send('Please select a valid option')

@client.command(help="Rock Paper Scissors Lizard Spock")
async def g5(ctx, *, pmove):
    if pmove.title() in o.rps5:
        bmove = random.choice(o.rps5)
        pv = o.rps5.index(pmove.title())
        bv = o.rps5.index(bmove)
        outcome = m.rps5[pv][bv]
        
        if outcome[1] == -1:
            await ctx.send(f'{bmove} {outcome[0]} {pmove.title()}: {ctx.author.mention} lost!')
        if outcome[1] == 0:
            await ctx.send(f'{pmove.title()} {outcome[0]} {bmove}!')
        if outcome[1] == 1:
            await ctx.send(f'{pmove.title()} {outcome[0]} {bmove}: {ctx.author.mention} won!')
    if pmove.title() not in o.rps5:
        await ctx.send('Please select a valid option')


@client.command(help='https://www.umop.com/rps7.htm')
async def g7(ctx, *, pmove):
    if pmove.title() in o.rps7:
        bmove = random.choice(o.rps7)
        pv = o.rps7.index(pmove.title())
        bv = o.rps7.index(bmove)
        outcome = m.rps7[pv][bv]
        
        if outcome[1] == -1:
            await ctx.send(f'{bmove} {outcome[0]} {pmove.title()}: {ctx.author.mention} lost!')
        if outcome[1] == 0:
            await ctx.send(f'{pmove.title()} {outcome[0]} {bmove}!')
        if outcome[1] == 1:
            await ctx.send(f'{pmove.title()} {outcome[0]} {bmove}: {ctx.author.mention} won!')
    if pmove.title() not in o.rps7:
        await ctx.send('Please select a valid option')


@client.command(help='https://www.umop.com/rps9.htm')
async def g9(ctx, *, pmove):
    if pmove.title() in o.rps9:
        bmove = random.choice(o.rps9)
        pv = o.rps9.index(pmove.title())
        bv = o.rps9.index(bmove)
        outcome = m.rps9[pv][bv]
        
        if outcome[1] == -1:
            await ctx.send(f'{bmove} {outcome[0]} {pmove.title()}: {ctx.author.mention} lost!')
        if outcome[1] == 0:
            await ctx.send(f'{pmove.title()} {outcome[0]} {bmove}!')
        if outcome[1] == 1:
            await ctx.send(f'{pmove.title()} {outcome[0]} {bmove}: {ctx.author.mention} won!')
    if pmove.title() not in o.rps9:
        await ctx.send('Please select a valid option')


@client.command()
async def help(ctx):
    embed = discord.Embed(title='Help')
    embed.add_field(name="rpsg3", value='Standard game of Rock Paper Scissors')
    embed.add_field(name="rpsg5", value='Rock Paper Scissors Lizard Spock')
    embed.add_field(name="rpsg7", value='<https://www.umop.com/rps7.htm>')
    embed.add_field(name="rpsg9", value='<https://www.umop.com/rps9.htm>')
    embed.add_field(name='rpsping', value="Wanna see how fast I can run in my new shoes?")
    embed.add_field(name='rpssupport', value='Links to support the developer.')
    embed.add_field(name='rpssource', value='Check out my source code!')
    await ctx.send(embed=embed)

client.run(TOKEN)