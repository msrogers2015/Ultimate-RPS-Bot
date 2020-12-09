# invite link: https://discord.com/api/oauth2/authorize?client_id=785983710361026561&permissions=75776&scope=bot
import discord, os, random
from discord.ext import commands
from dotenv import load_dotenv
import data.matrix as m
import data.moves as o

# Dotenv is used to load discord token without hosting it inside the code
load_dotenv()
TOKEN = os.getenv('TOKEN')


# Setting up bot command and disabling default help command
client = commands.Bot(command_prefix='rps')
client.remove_command('help')


# When bot comes online, set status and print connection verification in terminal
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(
       activity=discord.Activity(type=discord.ActivityType.watching,
       name=str(len(client.guilds)) + " servers | rpshelp")
    )


# Update bot presence when connecting to a new guild
@client.event
async def on_guild_join():
    await client.change_presence(
       activity=discord.Activity(type=discord.ActivityType.watching,
       name=str(len(client.guilds)) + " servers | rpshelp")
    )


# Update bot presence when disconnecting form a guild
@client.event
async def on_guild_remove():
    await client.change_presence(
       activity=discord.Activity(type=discord.ActivityType.watching,
       name=str(len(client.guilds)) + " servers | rpshelp")
    )


# Creates a invite link for others to add bot to their server
@client.command()
async def invite_link(ctx):
    await ctx.send('<https://discord.com/api/oauth2/authorize?client_id=785983710361026561&permissions=75776&scope=bot>')


# Display source code
@client.command()
async def source(ctx):
    await ctx.send('<https://github.com/msrogers2015/Ultimate-RPS-Bot>')


# Check bot latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)} ms')


# Returns links to support and follow developer
@client.command()
async def support(ctx):
    embed = discord.Embed(title='Support the Dev!')
    embed.add_field(name="Patreon", value='https://www.patreon.com/QuailWare')
    embed.add_field(name="Github", value='https://github.com/msrogers2015')
    embed.add_field(name='Website', value='https://msrogers2015.github.io/')
    await ctx.send(embed=embed)



# Standard game of Rock Paper Scissors
@client.command(aliases=['3'])
async def _3(ctx, *, pmove):
    image_link = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Rock-paper-scissors.svg/1200px-Rock-paper-scissors.svg.png"
    if pmove.title() in o.rps3:
        bmove = random.choice(o.rps3)
        pv = o.rps3.index(pmove.title())
        bv = o.rps3.index(bmove)
        outcome = m.rps3[pv][bv]
        #Losing Embed
        if outcome[1] == -1:
            you_lose = f'{bmove} {outcome[0]} {pmove.title()}: {ctx.author.name} lost!'
            embed = discord.Embed(title="1,2,3, Shoot!")
            embed=discord.Embed()
            embed.set_thumbnail(url=image_link)
            embed.add_field(name="Player's Move", value=pmove.title(), inline=False)
            embed.add_field(name="Bot's Move", value=bmove, inline=False)
            embed.add_field(name="Outcome", value=you_lose)
            await ctx.send(embed=embed)
        #Tied Embed
        if outcome[1] == 0:
            tied = f'{pmove.title()} {outcome[0]} {bmove}!'
            embed = discord.Embed(title="1,2,3, Shoot!")
            embed=discord.Embed()
            embed.set_thumbnail(url=image_link)
            embed.add_field(name="Player's Move", value=pmove.title(), inline=False)
            embed.add_field(name="Bot's Move", value=bmove, inline=False)
            embed.add_field(name="Outcome", value=tied)
            await ctx.send(embed=embed)
        #Winning Embed
        if outcome[1] == 1:
            you_win = f'{pmove.title()} {outcome[0]} {bmove}: {ctx.author.name} won!'
            embed = discord.Embed(title="1,2,3, Shoot!")
            embed=discord.Embed()
            embed.set_thumbnail(url=image_link)
            embed.add_field(name="Player's Move", value=pmove.title(), inline=False)
            embed.add_field(name="Bot's Move", value=bmove, inline=False)
            embed.add_field(name="Outcome", value=you_win)
            await ctx.send(embed=embed)
    #If player arg isn't in list of moves
    if pmove.title() not in o.rps3:
        await ctx.send('Please select a valid option')


# Standard game of Rock Paper Scissors
@client.command(aliases=['5'])
async def _5(ctx, *, pmove):
    image_link = "https://upload.wikimedia.org/wikipedia/commons/d/d8/Rock_Paper_Scissors_Lizard_Spock.JPG"
    if pmove.title() in o.rps5:
        bmove = random.choice(o.rps5)
        pv = o.rps5.index(pmove.title())
        bv = o.rps5.index(bmove)
        outcome = m.rps5[pv][bv]
        #Losing Embed
        if outcome[1] == -1:
            you_lose = f'{bmove} {outcome[0]} {pmove.title()}: {ctx.author.name} lost!'
            embed = discord.Embed(title="1,2,3, Shoot!")
            embed=discord.Embed()
            embed.set_thumbnail(url=image_link)
            embed.add_field(name="Player's Move", value=pmove.title(), inline=False)
            embed.add_field(name="Bot's Move", value=bmove, inline=False)
            embed.add_field(name="Outcome", value=you_lose)
            await ctx.send(embed=embed)
        #Tied Embed
        if outcome[1] == 0:
            tied = f'{pmove.title()} {outcome[0]} {bmove}!'
            embed = discord.Embed(title="1,2,3, Shoot!")
            embed=discord.Embed()
            embed.set_thumbnail(url=image_link)
            embed.add_field(name="Player's Move", value=pmove.title(), inline=False)
            embed.add_field(name="Bot's Move", value=bmove, inline=False)
            embed.add_field(name="Outcome", value=tied)
            await ctx.send(embed=embed)
        #Winning Embed
        if outcome[1] == 1:
            you_win = f'{pmove.title()} {outcome[0]} {bmove}: {ctx.author.name} won!'
            embed = discord.Embed(title="1,2,3, Shoot!")
            embed=discord.Embed()
            embed.set_thumbnail(url=image_link)
            embed.add_field(name="Player's Move", value=pmove.title(), inline=False)
            embed.add_field(name="Bot's Move", value=bmove, inline=False)
            embed.add_field(name="Outcome", value=you_win)
            await ctx.send(embed=embed)
    #If player arg isn't in list of moves
    if pmove.title() not in o.rps5:
        await ctx.send('Please select a valid option')



# Rock Paper Scissors with 7 options
@client.command(aliases=['7'])
async def _7(ctx, *, pmove):
    image_link = "https://www.umop.com/images/hands.jpg"
    if pmove.title() in o.rps7:
        bmove = random.choice(o.rps7)
        pv = o.rps7.index(pmove.title())
        bv = o.rps7.index(bmove)
        outcome = m.rps7[pv][bv]
        #Losing Embed
        if outcome[1] == -1:
            you_lose = f'{bmove} {outcome[0]} {pmove.title()}: {ctx.author.name} lost!'
            embed = discord.Embed(title="1,2,3, Shoot!")
            embed=discord.Embed()
            embed.set_thumbnail(url=image_link)
            embed.add_field(name="Player's Move", value=pmove.title(), inline=False)
            embed.add_field(name="Bot's Move", value=bmove, inline=False)
            embed.add_field(name="Outcome", value=you_lose)
            await ctx.send(embed=embed)
        #Tied Embed
        if outcome[1] == 0:
            tied = f'{pmove.title()} {outcome[0]} {bmove}!'
            embed = discord.Embed(title="1,2,3, Shoot!")
            embed=discord.Embed()
            embed.set_thumbnail(url=image_link)
            embed.add_field(name="Player's Move", value=pmove.title(), inline=False)
            embed.add_field(name="Bot's Move", value=bmove, inline=False)
            embed.add_field(name="Outcome", value=tied)
            await ctx.send(embed=embed)
        #Winning Embed
        if outcome[1] == 1:
            you_win = f'{pmove.title()} {outcome[0]} {bmove}: {ctx.author.name} won!'
            embed = discord.Embed(title="1,2,3, Shoot!")
            embed=discord.Embed()
            embed.set_thumbnail(url=image_link)
            embed.add_field(name="Player's Move", value=pmove.title(), inline=False)
            embed.add_field(name="Bot's Move", value=bmove, inline=False)
            embed.add_field(name="Outcome", value=you_win)
            await ctx.send(embed=embed)
    #If player arg isn't in list of moves
    if pmove.title() not in o.rps7:
        await ctx.send('Please select a valid option')


# Rock Paper Scissors with 9 options
@client.command(aliases=['9'])
async def _9(ctx, *, pmove):
    image_link = "https://www.umop.com/images/rps9.jpg"
    if pmove.title() in o.rps9:
        bmove = random.choice(o.rps9)
        pv = o.rps9.index(pmove.title())
        bv = o.rps9.index(bmove)
        outcome = m.rps9[pv][bv]
        #Losing Embed
        if outcome[1] == -1:
            you_lose = f'{bmove} {outcome[0]} {pmove.title()}: {ctx.author.name} lost!'
            embed = discord.Embed(title="1,2,3, Shoot!")
            embed=discord.Embed()
            embed.set_thumbnail(url=image_link)
            embed.add_field(name="Player's Move", value=pmove.title(), inline=False)
            embed.add_field(name="Bot's Move", value=bmove, inline=False)
            embed.add_field(name="Outcome", value=you_lose)
            await ctx.send(embed=embed)
        #Tied Embed
        if outcome[1] == 0:
            tied = f'{pmove.title()} {outcome[0]} {bmove}!'
            embed = discord.Embed(title="1,2,3, Shoot!")
            embed=discord.Embed()
            embed.set_thumbnail(url=image_link)
            embed.add_field(name="Player's Move", value=pmove.title(), inline=False)
            embed.add_field(name="Bot's Move", value=bmove, inline=False)
            embed.add_field(name="Outcome", value=tied)
            await ctx.send(embed=embed)
        #Winning Embed
        if outcome[1] == 1:
            you_win = f'{pmove.title()} {outcome[0]} {bmove}: {ctx.author.name} won!'
            embed = discord.Embed(title="1,2,3, Shoot!")
            embed=discord.Embed()
            embed.set_thumbnail(url=image_link)
            embed.add_field(name="Player's Move", value=pmove.title(), inline=False)
            embed.add_field(name="Bot's Move", value=bmove, inline=False)
            embed.add_field(name="Outcome", value=you_win)
            await ctx.send(embed=embed)
    #If player arg isn't in list of moves
    if pmove.title() not in o.rps9:
        await ctx.send('Please select a valid option')


# Custom help command
@client.command()
async def help(ctx):
    embed = discord.Embed(title='Help')
    embed.add_field(name="rps3", value='Standard game of Rock Paper Scissors')
    embed.add_field(name="rps5", value='Rock Paper Scissors Lizard Spock')
    embed.add_field(name="rps7", value='<https://www.umop.com/rps7.htm>')
    embed.add_field(name="rps9", value='<https://www.umop.com/rps9.htm>')
    embed.add_field(name='rpsping', value="Wanna see how fast I can run in my new shoes?")
    embed.add_field(name='rpssupport', value='Links to support the developer.')
    embed.add_field(name='rpssource', value='Check out my source code!')
    await ctx.send(embed=embed)


client.run(TOKEN)
