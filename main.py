import discord 
from discord.ext import tasks, commands
import asyncio
import random
import youtube_dl
from discord import User
from random import choice
from discord.ext.commands import Bot, guild_only
import os
import urllib
import webbrowser
import requests
from PIL import Image
from io import BytesIO
import datetime
import json
import DiscordUtils
from keep_alive import keep_alive
import requests
import praw
from datetime import datetime


reddit = praw.Reddit(client_id = "2MzSl7O_ZQjsow",
					client_secret = "WveKAN3PDgy1V8LjrN7nOAox6SRkNg",
					username = "Saranshpypy",
					password = "saransh2009",
					user_agent = "Ranzers-Talks")

s = ['s']

true = True

prefix = '> | bot mention'

name = ".."

def get_prefix(client,message):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      with open("prefixes.json", "r") as f:
          prefixes = json.load(f)

      pre = prefixes[str(ctx.guild.id)]

      await ctx.send(f"```\noops! this command was not found please use {pre}help\n```")
      return
    elif isinstance(error, commands.MissingPermissions):
      await ctx.send("""```yaml\nMissing Perms Error\nNote this problem can be caused due to two reason \n1st => you lack permissions\n2nd => Try keeping my role in top of the role on whom you are trying to trigger the command\n```""")
      return
    else:
      pass




@client.event
async def on_guild_join(guild):


    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = ">"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)




@client.command()
@commands.has_permissions(administrator = True)
async def changeprefix(ctx, prefix):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)    

    await ctx.send(f"The prefix was changed to {prefix}")



@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open('users.json', 'w') as f:
        json.dump(users, f)




client.remove_command('help')

class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)

class MyCog(commands.Cog):
    def __init__(self, bot):
        self._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self._original_help_command

invitel=discord.Embed(title="INVITE ME", description="|[Invite](https://bit.ly/3y9Ahuo)| |[support server](https://discord.gg/ygS6KWFUQq)|", color=0x00ffee)
invitel.set_author(name="Ranzer's Talks", url="https://discord.com/api/oauth2/authorize?client_id=829363895549558845&permissions=268445808&scope=bot", icon_url="https://media.istockphoto.com/vectors/vector-handwritten-logo-letter-r-vector-id1008257372?k=6&m=1008257372&s=612x612&w=0&h=CG0gusH4nCB6zjkdeqD_wmEkNn-bQPEv86N4xoK4WBw=")
invitel.set_thumbnail(url="https://media.istockphoto.com/vectors/vector-handwritten-logo-letter-r-vector-id1008257372?k=6&m=1008257372&s=612x612&w=0&h=CG0gusH4nCB6zjkdeqD_wmEkNn-bQPEv86N4xoK4WBw=")
invitel.set_footer(text="by ranzer's team")




@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f">help | >invite in {len(client.guilds)} servers --[{round(client.latency * 1000)} ms!]--"))

@client.command(name='hi', help='invite me to your server')
async def hi(ctx):
    async with ctx.typing():
        message = await ctx.send('O hello dear '+ format(ctx.author.display_name))

hhh=discord.Embed(title="Ranzer's Help", description='[commands](https://bit.ly/3hiyBbZ)', color=0x00ffa6)
hhh.set_thumbnail(url="https://cdn.discordapp.com/app-icons/830292896015056896/d20017b4607c7674b97d98c94c198311.png?size=64")
hhh.add_field(name="Vote me", value="[vote](https://discordbotlist.com/bots/ranzers-talks/upvote)", inline=False)
hhh.add_field(name="Invite me ", value="[invite](https://bit.ly/3y9Ahuo)", inline=False)
hhh.add_field(name="support server", value='[join](https://discord.gg/ygS6KWFUQq)', inline=False)
hhh.set_footer(text = "page 1/3")

hhh1=discord.Embed(title="Updates", description="**`Added Music Added Economy Added More commands Added leveling system`**", color=0x00ff80)
hhh1.set_footer(text = "page 2/3")

@client.command(name='help', aliases=["HELP", "Help"])
async def help(ctx):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  pre = prefixes[str(ctx.guild.id)] 

  hhh2=discord.Embed(title="Information", color=0x00ff80)
  hhh2.add_field(name="Prefix", value=f"**`Prefix = {pre}`**", inline=False)
  hhh2.add_field(name="Help command", value="**`Default Help command = >help `**", inline=False)
  hhh2.add_field(name="Age", value="**`Sat, Apr 10, 2021 12:07 AM`**", inline=False)
  hhh2.add_field(name="Tags", value="**`Economy | Music | Moderation | etc`**", inline=True)
  hhh2.add_field(name="Default Ping", value="**`44 ms`**", inline=False)
  hhh2.add_field(name="Perms Use Moderation", value="**`administrator`**", inline=False)
  hhh2.set_footer(text = "page 3/3")

  paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
  paginator.add_reaction('⏪', "first")
  paginator.add_reaction('◀', "back")
  paginator.add_reaction('▶', "next")
  paginator.add_reaction('⏩', "last")
  embeds = [hhh, hhh1, hhh2]
  await paginator.run(embeds)



@client.command(name='support_server')
async def support_server(ctx):
    await ctx.message.delete()
    message = await ctx.send(embed=invitel)



async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'```yaml\n{user.display_name} has leveled up to level {lvl_end}\n```')
        users[f'{user.id}']['level'] = lvl_end

@client.command()
async def level(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'```yaml\nYou are at level {lvl}!\n```')
    else:
        id = member.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'{member}\n```yaml\n is at level {lvl}!\n```')



music = DiscordUtils.Music()

@client.command()
async def join(ctx):
    await ctx.author.voice.channel.connect() #Joins author's voice channel

@client.command()
@commands.has_permissions(administrator = True)
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def play(ctx, *, url):
    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(url, search=True)
        song = await player.play()
        await ctx.send(f"```yaml\nPlaying {song.name}\n```")
    else:
        song = await player.queue(url, search=True)
        await ctx.send(f"```yaml\nQueued {song.name}\n```")

@play.error
async def play(ctx, error):
  if isinstance(error, commands.CommandInvokeError):
    await ctx.send("```yaml\nIt seems that I am not connected to a voice channel use >join to make me join```")
    return
  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("```yaml\nIt seems some arguments are missing use >play [url or song name]\n```")
  else:
    pass



@client.command()
async def pause(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.pause()
    await ctx.send(f"```yaml\nPaused {song.name}\n```")

@client.command()
async def resume(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()
    await ctx.send(f"```yaml\nResumed {song.name}\n```")

@client.command()
async def stop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await player.stop()
    await ctx.send("```yaml\nStopped\n```")

@client.command()
async def loop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        await ctx.send(f"```yaml\nEnabled loop for {song.name}\n```")
    else:
        await ctx.send(f"```yaml\nDisabled loop for {song.name}\n```")

@client.command()
async def queue(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await ctx.send(f"```yaml\n{', '.join([song.name for song in player.current_queue()])}\n```")

@client.command()
async def np(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    await ctx.send(f"```yaml\nNow playing {song.name}\n```")

@client.command()
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
        await ctx.send(f"```yaml\nSkipped from {data[0].name} to {data[1].name}\n```")
    else:
        await ctx.send(f"```yaml\nSkipped {data[0].name}\n```")

@client.command()
async def volume(ctx, vol):
    player = music.get_player(guild_id=ctx.guild.id)
    song, volume = await player.change_volume(float(vol) / 100) # volume should be a float between 0 to 1
    await ctx.send(f"```yaml\nChanged volume for {song.name} to {volume*100}%\n```")

@client.command()
async def remove(ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    await ctx.send(f"```yaml\nRemoved {song.name} from queue\n```")
  
@client.command(name='banner')
async def banner(ctx):
    await ctx.message.delete()
    await ctx.send("https://cdn.discordapp.com/attachments/836196010744086598/839459943467712532/standard.gif")

@client.command()
async def pro(ctx):
	await ctx.send("😎 I AM ISN'T IT ")
@client.command()
async def no(ctx):
	await ctx.send("😎 I AM ISN'T IT ")


@client.command(name='sl_dm', pass_context=True)
async def sl_dm(ctx,member:discord.Member,*, message=None):
    await ctx.message.delete()
    message = message
    msg = await member.send(message)


@client.command(name='rh')
async def rh(ctx):
    async with ctx.typing():
            await ctx.send(f'Hello '+ format(ctx.author.display_name))
@client.command(name='ytsearch')
async def ytsearch(ctx, message):
    async with ctx.typing():
        await ctx.message.delete()
        message = await ctx.send('Opening')

        webbrowser.open(f'https://www.youtube.com/results?search_query={message}')
@client.command(pass_context=True)
async def hey(ctx):
    async with ctx.typing():
        await ctx.send('ayo Hello There')
@client.command(name='information')
async def information(ctx):
    await ctx.message.delete()
    embed = discord.Embed( timestamp=ctx.message.created_at)
    embed.set_author(name=f"Information for the {ctx.guild.name}")
    embed.add_field(name="Guild id:", value= f"{ctx.guild.id}")
    embed.add_field(name="The guilds owner is:", value = f" {ctx.guild.owner}")
    message = await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    message = await ctx.send('Deleted sucsessfully')


@client.command(name='who_are_you')
async def who_are_you(ctx):
    async with ctx.typing():
        message = await ctx.send("I am Ranzer's The small talks Bot")


@client.command()
@commands.has_permissions(administrator = True)
async def nuke(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.send("You did not mention a channel!")

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Nuked!")
        em = discord.Embed(title = f"This channel was nuked by **`{ctx.author.display_name}`**", color = 0xff0000)
        em.set_image(url = "https://i.pinimg.com/originals/6c/48/5e/6c485efad8b910e5289fc7968ea1d22f.gif")
        await nuke_channel.delete()
        mes = await new_channel.send(f"{ctx.author.mention}")
        await new_channel.send(embed = em)
        await mes.delete()
        await ctx.author.send("Nuked the Channel sucessfully!")
    else:
        await ctx.send(f"No channel named {channel} was found!")

@nuke.error
async def nuke(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("It seems u lack permissions")
    return

          
@client.command(name='cool')
async def cool(ctx):
    async with ctx.typing():
        message = await ctx.send('Yes cool')


@client.command(name='invsend')
async def invsend(ctx, member:discord.Member, link):
    await ctx.message.delete()
    embed =  discord.Embed(title=f'Hello {member}', description=f"Hey There I am " + format(ctx.author.display_name) + 'Please Join The server' , color=0x00ffd0)
    embed.add_field(name='Click Here To Invite', value=f'| [Click me!]({link}) |', inline=False)
    message = await member.send(embed=embed)


@client.command(name='hello')
async def hello(ctx):
    async with ctx.typing():
        message = await ctx.send('O soo sweet Hi '+ format(ctx.author.display_name))


@client.command(name='how_old_Are_you')
async def how_old_Are_you(ctx):
    async with ctx.typing():
        await ctx.send("I don't really know about that")
@client.command(name='you_are_annoying')
async def you_are_annoying(ctx):
    async with ctx.typing():
        await ctx.send('I did not mean that to you dude sorry')
@client.command(name="answer_my_question")
async def answer_my_question(ctx):
    async with ctx.typing():
        await ctx.send('I think you are going stupid I not got any quetion')
@client.command(name='rm_warn', pass_context=True)
@commands.has_permissions(administrator=True)
async def rm_warn(ctx,*, member):
    async with ctx.typing():
        await ctx.message.delete()
        message = await ctx.send(f'DEAR {member} YOU ARE WARNED ' + format(ctx.message.author.mention))

@client.command(name='call')
@commands.cooldown(1, 3600, commands.BucketType.user)
async def call(ctx,*, member, pass_context=True):
    await ctx.message.delete()
    async with ctx.typing():
        message = await ctx.send(format(ctx.message.author.mention) + f'CALLED {member} PLEASE BE HERE ')


@client.command(name='invite', aliases = ["INVITE", "Invite"])
async def invite(ctx):
    await ctx.message.delete()
    async with ctx.typing():
        await ctx.send(embed=invitel)
        inv = await ctx.send("https://cdn.discordapp.com/attachments/836196010744086598/839459943467712532/standard.gif")
        await inv.add_reaction('✅')





@client.command(name='noice')
async def noice(ctx):
    async with ctx.typing():
        await ctx.send('NICE!')
@client.command(name='nice')
async def nice(ctx):
    async with ctx.typing():
        await ctx.send('NOICE!')
@client.command(name='NICE')
async def NICE(ctx):
    async with ctx.typing():
        await ctx.send('NOICE!')
@client.command(name='NOICE')
async def NOICE(ctx):
    async with ctx.typing():
        await ctx.send('NICE!')
@client.command(name='Nice')
async def Nice(ctx):
    async with ctx.typing():
        await ctx.send('Noice!')
@client.command(name='Noice')
async def Noice(ctx):
    async with ctx.typing():
        await ctx.send('Nice!')
@client.command(name='pog')
async def pog(ctx):
    async with ctx.typing():
        await ctx.send('pogggg!')
@client.command(name='i_like_you')
async def i_like_you(ctx):
    async with ctx.typing():
        await ctx.send('Ok so its cool mmm do invite so i can do that in your server also')
@client.command(name='code')
async def code(ctx):
    async with ctx.typing():
        await ctx.send('Super secret!')
@client.command(name='trespassing')
async def trespassing(ctx):
    async with ctx.typing():
        await ctx.send('Dont do it u will be punished')
@client.command(name='you_are_hacking')
async def you_are_hacking(ctx):
    async with ctx.typing():
        await ctx.send('I am a hacker <:stay_gold_ranzer:837146114171600896> Thanks TO tell me about that')
        await ctx.send('I am not a hacker ok dude👿')
@client.command(name='nope')
async def nope(ctx):
    async with ctx.typing():
        await ctx.send('Yep!')
@client.command(name='yep')
async def yep(ctx):
    async with ctx.typing():
        await ctx.send('Nope!')
@client.command(name='op')
async def op(ctx):
    async with ctx.typing():
        await ctx.send('OPPPPPPPPPPPPPPPPPPPPPPPPPPPP!')
@client.command(name='createrole',
                brief='Creates a role',
                aliases=['cr','makerole'],
                pass_ctx=True)
async def createrole(ctx, rname: str, clr: discord.Colour):
    await ctx.message.delete()
    if ctx.author.guild_permissions.manage_roles:
        await ctx.guild.create_role(name=rname, colour=clr)
        message = await ctx.send('Role created with name: ' + rname)
        print('Createrole command executed\n-  -  -')
    else:
        message = await ctx.send('You lack permission.')
    print('Createrole command executed\n-  -  -')
@client.command(name='shit')
async def shit(ctx):
    async with ctx.typing():
        await ctx.send('SHITTTTTTTTTT!')
@client.command(name='lol')
async def lol(ctx):
    async with ctx.typing():
        await ctx.send('LOLLLLLLLLLLLLL!')
@client.command(name='screw')
async def screw(ctx):
    async with ctx.typing():
        await ctx.send('!')
@client.command(name='print')
async def print(ctx):
    async with ctx.typing():
        await ctx.send('WHAT! BTW I DONT KNOW HOW TO PRINT')
@client.command(name='danger')
async def danger(ctx):
    async with ctx.typing():
        await ctx.send('ZONE!')
@client.command(name='area51')
async def area51(ctx):
    async with ctx.typing():
        await ctx.send('AREA 51 SHUT UP! ')
@client.command(name='poggers')
async def poggers(ctx):
    async with ctx.typing():
        await ctx.send('POG!')
@client.command(name='stupidbot')
async def stupidbot(ctx):
    async with ctx.typing():
        await ctx.send('MMMM OK I AM STUPID POG!')
@client.command(name='java')
async def java(ctx):
    async with ctx.typing():
        await ctx.send('A PROGRAMING LANGUAGE')
@client.command(name='python')
async def python(ctx):
    async with ctx.typing():
        await ctx.send('A LANGUAGE BY WHICH I AM CODED I LOVE IT')
@client.command(name='goggle')
async def google(ctx):
    await ctx.message.delete()
    async with ctx.typing():
        await ctx.send('MMMMMMM!')
        webbrowser.open('https://www.google.com/')
@client.command(name='yourrtcode')
async def yourrtcode(ctx):
    async with ctx.typing():
        await ctx.send('I AM NOT TELLING ABOUT THAT')
@client.command(name='how_are_you')
async def how_are_you(ctx):
    async with ctx.typing():
        await ctx.send('I MAY BE FINE RIGHT NOW!')
@client.command(name='are_you_typing')
async def are_you_typing(ctx):
    async with ctx.typing():
        await ctx.send('NOPE!')
@client.command(name='how_is_this_possible')
async def how_is_this_possible(ctx):
    async with ctx.typing():
        await ctx.send('EVERYTHING IS POSSIBLE!')
@client.command(name='you_are_shit')
async def you_are_shit(ctx):
    async with ctx.typing():
        await ctx.send('M OK')
@client.command(name='noobbot')
async def noobbot(ctx):
    async with ctx.typing():
        await ctx.send('<:stay_gold_ranzer:837146114171600896> HEHE!')
@client.command(name='noob')
async def noob(ctx):
    async with ctx.typing():
        await ctx.send('YOU ARE!')
@client.command(name='freindsbot')
async def freindsbot(ctx):
    async with ctx.typing():
        await ctx.send('YES!')
@client.command(name='stopbot')
async def stopbot(ctx):
    async with ctx.typing():
        await ctx.send('NOPE!')
@client.command(name='member')
async def member(ctx):
    async with ctx.typing():
        embed=discord.Embed(title=f'Member Count of The server', description='SERVER MEMBER COUNT = ' + format(ctx.guild.member_count), color=0x00ffee)
        message = await ctx.send(embed=embed)
@client.command(name='daring')
async def daring(ctx):
    async with ctx.typing():
        await ctx.send(f'DARING!!!')
@client.command(name='openinv')
async def openinv(message):
    await ctx.message.delete()
    async with message.typing():
        message = await ctx.send('Opening')
        await message.add_reaction('<:stay_gold_ranzer:837146114171600896>')
        webbrowser.open('https://discord.com/api/oauth2/authorize?client_id=830292896015056896&permissions=8&redirect_uri=https%3A%2F%2Fmedia.tenor.com%2Fimages%2Fd44eb6cb4f9aec64298e14f72de07d96%2Ftenor.gif&response_type=code&scope=bot%20messages.read%20applications.commands%20identify')
@client.command(name='eval')
@commands.is_owner()
async def _eval(ctx, *, code):
    """A bad example of an eval command"""
    await ctx.send(eval(code))
@client.command(pass_context=True)
async def dm(ctx,member:discord.Member,*, message=None):
    try:
        await ctx.message.delete()
        message = message
        mlk = await member.send(message + ' By ' + format(ctx.author.display_name))
        await mlk.add_reaction('<:stay_gold_ranzer:837146114171600896>')
    except:
        await ctx.message.delete()
        await ctx.send('I got some error')
        await ctx.send('The persion whom you are sending message must be authenticated with the bot')
@client.command(name='o')
async def o(ctx):
    async with ctx.typing():
        await ctx.send('Ooooo!')
@client.command(name='gay')
async def gay(ctx):
    async with ctx.typing():
        await ctx.send('YOU ARE BITCH!')
@client.command(name='nonono')
async def nonono(ctx):
    async with ctx.typing():
        await ctx.send('Yes yes yes yes!')
@client.command(name='gosh')
async def gosh(ctx):
    async with ctx.typing():
        await ctx.send('Oh my gosh!')

@client.command(name='rmail')
async def rmail(ctx):
    await ctx.message.delete()
    async with ctx.typing():
        embed=discord.Embed(title="Gmail Buisness ", description="[sdiscordof@gmail.com](sdiscordof@gmail.com)", color=0x00ffe1)
        embed.add_field(name="No spams", value="404", inline=False)
        embed.set_footer(text="Buisness Mail No spam")
        msff = await ctx.send(embed=embed)
@client.command(name='stupid_shit')
async def stupid_shit(ctx):
    async with ctx.typing():
        await ctx.send('You are!')
@client.command(name='redbull')
async def redbull(ctx):
    async with ctx.typing():
        await ctx.send("Redbull gives u wing's")
@client.command(name='gotcha')
async def gotcha(ctx):
    async with ctx.typing():
        await ctx.send("Got it!")
@client.command(name='program')
async def program(ctx):
    async with ctx.typing():
        await ctx.send("C++, python, java, javascript, rust, html, php, c#")
@client.command(name='tellall_dear')
@commands.cooldown(1, 3600, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def tellall_dear(ctx,*,message):
    async with ctx.typing():
        await ctx.message.delete()
        g = await ctx.send('||@everyone@here|| ' + format(message))
@client.command(name='h')
async def h(ctx):
    async with ctx.typing():
        await ctx.send('H')
        await message.add_reaction(':ok:')
@client.command(name='test', help='This command tests a sentence')
async def test(ctx, *args):            
    mf = await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
    await ctx.message.delete()
@client.command(name='add', help='Adds 2 number ex:s.add 2 2')
async def add(ctx, a: int, b: int):
    await ctx.message.delete()
    await ctx.send(a + b)
@client.command(name='mul', help='multiplies 2 number')
async def mul(ctx, a: int, b: int):
    await ctx.message.delete()
    await ctx.send(a * b)
@client.command(name='div', help='divides 2 number')
async def div(ctx, a: int, b: int):
    await ctx.message.delete()
    await ctx.send(a / b)
@client.command(name='whiso', help='Tells who is the bot owner')
async def whiso(ctx):
    await ctx.send('My owner is SARANSH#5918')
@client.command(name='sub', help='subtracts 2 number')
async def sub(ctx, a: int, b: int):
    await ctx.message.delete()
    await ctx.send(a - b)
@client.command(name='joined', help='Tells about joining of a member')
async def joined(ctx, *, member: discord.Member):
    await ctx.message.delete()
    message = await ctx.send('{0} joined on {0.joined_at}'.format(member))
    await message.add_reaction('<:stay_gold_ranzer:837146114171600896>')

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)
@client.command(name='slap', help='Hellps slapping someone')
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.message.delete()
    message = await ctx.send('{} just got slapped for {}'.format(slapped, reason))

class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]]
@client.command(name='roles', help='Tells about roles of a member')
async def roles(ctx, *, member: MemberRoles):
    await ctx.message.delete()
    message = await ctx.send('I see the following roles: ' + ', '.join(member))


@client.command(name='ping', help='Tells client latency')
async def ping(ctx):
    await ctx.message.delete()
    message = await ctx.send(f'pong! Latency : {round(client.latency * 1000)}')


@client.command(name='info', help='Tells the info of a member')
async def info(ctx, *, member: discord.Member):
    await ctx.message.delete()
    fmt = '{0} joined on {0.joined_at} and has {1} roles.'
    gg  = await ctx.send(fmt.format(member, len(member.roles)))

@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("I can't find the member in this server please check......")
class JoinDistance:
    def __init__(self, joined, created):
        self.joined = joined
        self.created = created

    @property
    def delta(self):
        return self.joined - self.created

class JoinDistanceConverter(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return JoinDistance(member.joined_at, member.created_at)
@client.command(name="delta", help='hmmm just for fun')
async def delta(ctx, *, member: JoinDistanceConverter):
    is_new = member.delta.days < 10
    if is_new:
        await ctx.send("Hey you're pretty new!")
    else:
        await ctx.send("Hm you're not so new.")

class Sinner(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument) # gets a member object
        permission = argument.guild_permissions.manage_messages # can change into any permission
        if not permission: # checks if user has the permission
            return argument # returns user object
        else:
            raise commands.BadArgument("You cannot punish other staff members")
@client.command()
async def membercount(ctx):
    await ctx.message.delete()
    message = await ctx.send(format(ctx.guild.member_count) + " Members")

@client.command(name='love_it')
async def love_it(ctx):
    async with ctx.typing():
        await ctx.send('Thanks dear')
@client.command(name='what')
async def what(ctx):
    async with ctx.typing():
        await ctx.send('What!')
@client.command(name='noob_shit')
async def noob_shit(ctx):
    async with ctx.typing():
        await ctx.send('Pog!')
@client.command(name='yoping')
@commands.cooldown(1, 60, commands.BucketType.user)
async def yoping(ctx):
    async with ctx.typing():
        message = await ctx.send('Pong! ' + format(ctx.message.author.mention))
        await message.add_reaction('<:stay_gold_ranzer:837146114171600896>')

@client.command(name='tellall')
@commands.cooldown(1, 3600, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def tellall(ctx, message):
    async with ctx.typing():
        await ctx.send('@everyone @here announcement📢')
        await ctx.send(format(message))
        msage = await ctx.send("announced by " + format(ctx.author.display_name))
        await msage.add_reaction('<:stay_gold_ranzer:837146114171600896>')

@client.command(pass_context=True)
async def dmme(ctx):
    await ctx.message.delete()
    message = await ctx.author.send('Hi')

@client.command(name='auth')
async def auth(ctx):
    async with ctx.typing():
        await ctx.message.delete()
        await ctx.send(embed=invite1)
        await ctx.message.delete()




@client.command(name='gsearch')
async def gsearch(ctx, message):
	async with ctx.typing():
		await ctx.message.delete()
		webbrowser.open(f'https://www.google.com/search?q={message}')

@client.command(name='userinfo')
async def userinfo(ctx, member: discord.Member):
    async with ctx.typing():

        roles = [role for role in member.roles]

        infouser=discord.Embed(color=member.color, timestamp=ctx.message.created_at)
        infouser.set_thumbnail(url=member.avatar_url)
        infouser.set_footer(text=f'Asked By {ctx.author}', icon_url=ctx.author.avatar_url)

        infouser.add_field(name="ID", value=member.id)
        infouser.add_field(name="Guild name : ", value=member.display_name)
        infouser.add_field(name="Created at ", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC "))
        infouser.add_field(name="Joined at", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC "))

        infouser.add_field(name=f"Roles ({len(roles)})", value="".join([role.mention for role in roles]))
        infouser.add_field(name=f"Top roles of {member}", value=member.top_role.mention)
        infouser.set_footer(text=f'Asked By {ctx.author}', icon_url=ctx.author.avatar_url)
        
        await ctx.message.delete()
        mfa = await ctx.send(embed=infouser)

@client.command(name='serverinfo')
async def serverinfo(ctx):
    await ctx.message.delete()

    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
    staff_roles = ["Owner", "Head Dev", "Dev", "Head Admin", "Admins", "Moderators", "Community Helpers", "Members"]
        
    embed2 = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
    embed2.add_field(name='Name', value=f"{ctx.guild.name}", inline=False)
    embed2.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=False)
    embed2.add_field(name='Highest role', value=ctx.guild.roles[-2], inline=False)

    for r in staff_roles:
        role = discord.utils.get(ctx.guild.roles, name=r)
        if role:
            members = '\n'.join([member.name for member in role.members]) or "None"
            embed2.add_field(name=role.name, value=members)

    embed2.add_field(name='Number of roles', value=str(role_count), inline=False)
    embed2.add_field(name='Number Of Members', value=ctx.guild.member_count, inline=False)
    embed2.add_field(name='Bots:', value=(', '.join(list_of_bots)))
    embed2.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
    embed2.set_thumbnail(url=ctx.guild.icon_url)
    embed2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)

    mes = await ctx.send(embed=embed2)

@client.command(name='mail')
async def mail(ctx, user:discord.Member,*,message):
    async with ctx.typing():
        await ctx.message.delete()
        embed=discord.Embed(title=f"**YOU RECIVED A MAIL 📧 {user}**", description="<------------CONTENT------------>", color=0x00ffe1)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.add_field(name=message, value='.mail.', inline=False)
        embed.set_footer(text='Rmail services')
        me = await user.send(embed=embed)
        await me.add_reaction('📧')
@client.command()
async def meme(ctx):
    await ctx.message.delete()
    r = requests.get('https://memes.blademaker.tv/api/dankmemes')
    res = r.json()
    title = res['title']
    ups = res['ups']
    downs = res['downs']
    sub = res['subreddit']
    m = discord.Embed(title=f'{title}\n', description = res['author'], color=0x00ffe1)
    m.set_image(url = res['image'])
    m.set_footer(text=f'👍: {ups} 🤣: ' + format(random.randint(500, 500000)) + ' 💝: ' + format(random.randint(10000, 500000)))
    mes = await ctx.send(embed=m)
@client.command(name='wanted')
async def wanted(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user == None:
        user = ctx.author

    wanted = Image.open('wanted.jpg')
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((409,381))
    wanted.paste(pfp, (105,269))
    wanted.save("profile.jpg")
    mes = await ctx.send(file = discord.File("profile.jpg"))



def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]

@client.command()
@commands.has_permissions(administrator=True)
async def gstart(ctx):
    await ctx.send("Lets create a giveaway! answers The questions I ask in 1 minute")

    questions = ["Which channel should the giveaway hosted in?",
                 "What should be the durations (s|m|h|d)",
                 "What is the prize?"]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timeout=59.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You didn\'t answer in time, please be quicker next time')
            return 
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f'You didn\'t mention the channel properly. Do it like {ctx.channel.mention}')
        return

    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f'Use proper unit (s|m|h|d)')
        return
    if time == 2:
        await ctx.send(f'You have not used a integer please use a integer next time')
        return

    prize = answers[2]
 
    await ctx.send(f'The giveaway will be in {channel.mention} and will last {answers[1]}')

    await ctx.message.delete()
    embed=discord.Embed(title=f'Giveaway by ' + format(ctx.author.display_name), description=f'Prize : {prize}', color = 0x00ffd0)
    embed.add_field(name = 'Hosted by : ', value = ctx.author.display_name)
    embed.set_footer(text = f'Ends {answers[1]} from now!')
    message = await channel.send(embed=embed)
    await message.add_reaction('🎉')
    await asyncio.sleep(time)
    new_msg = await channel.fetch_message(message.id)
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    winner = random.choice(users)
    mes = await channel.send(f'Hey {winner.mention} You won the giveaway Hosted by ' + format(ctx.author.mention) + f' You won {prize}')


@client.command(name='gannounce')
@commands.cooldown(1, 3600, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def gannounce(ctx):
    await ctx.message.delete()
    mes = await ctx.send(f'@everyone @here A giveaway is hosted join the giveaway')
    await ctx.author.send('You are now on a 1hour cooldown By using the giveaway announcement command')
    await mes.add_reaction('<:stay_gold_ranzer:837146114171600896>')

@client.command(name = 'roll')
async def roll(ctx):
    await ctx.message.delete()
    roll = random.choice(['Head', 'Tales'])
    mes = await ctx.send(f'rolled = {roll}')
    await mes.add_reaction('<:stay_gold_ranzer:837146114171600896>')
@client.command(name='flip')
async def flip(ctx):
    await ctx.message.delete()
    flip = random.randrange(1, 99)
    mes = await ctx.send(f'flipped = {flip}')
    await mes.add_reaction('<:stay_gold_ranzer:837146114171600896>')
@client.command(name='roll_cs')
async def flics(ctx, num1: int, num2: int):
    await ctx.message.delete()
    f = random.randrange(num1, num2)
    mes = await ctx.send(f)
    await mes.add_reaction('<:stay_gold_ranzer:837146114171600896>')
@client.command(pass_context=True)
@commands.has_permissions(change_nickname=True)
async def nick(ctx, nick):
    await ctx.message.delete()
    await ctx.author.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

em = discord.Embed(title = 'The id was entered incorrectly', description = 'Try >devid to know how to get message id', color=0x00ffd0)

@client.command()
@commands.has_permissions(administrator=True)
async def reroll(ctx, channel : discord.TextChannel, id_ : int):
    await ctx.message.delete()
    try:
        jg = await channel.fetch_message(id_)
    except:
        await ctx.send(embed = em)
        return

    users = await jg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f'Congratulations The new winner is {winner.mention}.')

@client.command()
async def devid(ctx):
    await ctx.message.delete()
    em = discord.Embed(title='How to get a message id', description='To get a message id Click on user settings and then go to advanced section and Then turn on developer mode after that return to the giveaway message click on 3 dots on the giveaway message and after that copy the message id and u are ready to go', color = ctx.author.color )
    await ctx.send(embed = em)
@client.command()
@commands.has_permissions(ban_members=True)
async def kick(ctx, member: discord.Member,*, reason = None):
    await ctx.message.delete()
    await member.kick(reason = reason)
    await ctx.send('Kicked')
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member,*, reason = None):
    await ctx.message.delete()
    await member.ban(reason = reason)
    await ctx.send(f"Banned {member.name}#{member.discriminator}")
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    await ctx.message.delete()
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")


    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.name}#{user.discriminator}")


@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name=f"TO UNMUTE {member}", value = f"Type = >unmute {member.name}#{member.discriminator}")
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)





@client.command(aliases = ["Kill", "KILL"])
async def kill(ctx, member: discord.Member):
    messages = [f"🥺{member.mention} died", f"{member.mention} GF LEFT HIM AND HE DIED 😶😶", f"{member.mention} DIED F", f"Oh dang you are dead {member.mention}", f"{member.mention} dies of simping", f"{member.mention} dies of cringe", f"{member.mention} dies after Fapping 50 times in a row with no break", f"{member.mention} steps on a lego", f"BOOM HEAD SHOT {member.mention}", f"{member.mention} dies after knowing His girlfreind loves Joker", f"You Died {member.mention}", f"YOU DED {member.mention}", f"mission failed {member.mention}", f"you are now ded {member.mention}", f"you fall in lava and lose all your stuff {member.mention}", f"{member.mention} you get killed by {ctx.author.mention}", f"{ctx.author.mention} kills {member.mention} with an axe", f"{ctx.author.mention} rolls a car over {member.mention}", f"{member.mention} dies", f"{member.mention} dies of their own stupidity 🤣", f"{ctx.author.mention} slaps {member.mention} in the face and he died lol 😁", f"{member.mention} dies in his sleep"]
    messages_1 = [f"YOU ARE BEING STUPID TRY KILLING A MEMBER {member.mention} NOT YOURSELF", f"YOU NOOB {member.mention} MENTION A MEMBER DONOT KILL YOUR SELF OK", f"HUH YOU ARE DED MENTION SOMEONE ElSE {member.mention}", f"LOLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL TAG SOMEONE ELSE {member.mention}", f"I LOVE YOU I DONT WANT TO KILL YOU 🥺 PLEASE MENTION A MEMBER {ctx.author.mention}", f"{member.mention} YOU ARE ALREADY DEAD TRY SOMEONE ELSE PLEASE", f"YOU ARE UGLY TRY SOMEONE ELSE {member.mention}"]
    if ctx.author == member:
        await ctx.send(random.choice(messages_1))
        return(False)
    elif member.id == ctx.guild.owner_id:
        embed = discord.Embed(title = "OWNER", description = "I AM THE BOSS MUHAHAHA! YOU CANT KILL ME!", color = ctx.author.color)
        await ctx.send(embed = embed)
        return(False)
    else:
        await ctx.send(random.choice(messages))
        return(True)


@kill.error
async def kill(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("You must mention a member to kill")
        return(False)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You must mention a member to kill")
        return(False)
    else:
        await ctx.send("HUH SOME ERROR TRY ONE MORE TIME")
        return(True)





@client.command()
async def hug(ctx, member: discord.Member):
	hug_mes = [f"{ctx.author.mention} HUGGED {member.mention}", f"{ctx.author.mention} LOVES {member.mention} AND HUGS HER", f"WE ALL LOVE {member.mention} AND WE HUGGED HIM", f"{member.mention} I HUGGED HIM/HER WE LOVE HIM ISN'T", f"{ctx.author.mention} LOVES  {member.mention} AND HE HUGGED HIM", f"WE LOVEEEEEEEE {member.mention}", f"{ctx.author.mention} HUGGGGGGGGGGGGGGGGGGGGGGGED {member.mention}", f"WE LOVEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE {member.mention}", f"WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE LOVE {member.mention}"]
	if member == ctx.author:
		await ctx.send("YOU HUGGED YOURSELF TRY SOMEONE ELSE")
		return(False)
	else:
		await ctx.send(random.choice(hug_mes))
		return(True)


@hug.error
async def hug(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("YOU MUST MENTION A MEMBER")
        return(False)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("YOU MUST MENTION A MEMBER TO HUG")
        return(False)
    else:
    	await ctx.send("ERROR!!")


player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command(aliases = ["ttt"])
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn. type >place <position> to place")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn. type >place <position> to place")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one. type >place <position> to place")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command. example >tictactoe <player1> <player2>")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@814002302561026108>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark. example >place <position> ")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")







class DurationConverter(commands.Converter):
	async def convert(self, ctx, argument):
		amount = argument[:-1]
		unit = argument[-1]

		if amount.isdigit() and unit in ["s", "m", "h", "d"]:
			return (int(amount), unit)

		raise commands.BadArgument(message = "Not a valid duration")

@client.command()
@commands.has_permissions(administrator = True)
async def tempban(ctx, member:commands.MemberConverter, duration: DurationConverter):

	multiplier = {"s": 1, "m": 60, "h": 3600, "d": 86400}
	amount, unit = duration

	await ctx.guild.ban(member)
	await ctx.send(f"{member} was Banned by {ctx.author.mention} for {amount}{unit}")
	await asyncio.sleep(amount * multiplier[unit])
	await ctx.guild.unban(member)
	await ctx.send(f"{member} IS UNBANNED")

@tempban.error
async def tempban(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
	    await ctx.send("Please use arguments correctly >tempban <member> [duration in s, m, h, d]")
	    return
	elif isinstance(error, commands.BadArgument):
		await ctx.send("Please use arguments correctly >tempban <member> [duration in s, m, h, d]")
		return
	elif isinstance(error, commands.MissingPermissions):
		await ctx.send("You Lack permissions To use this commands you must have Ban members permissions")




@client.command()
@commands.has_permissions(administrator = True)
async def tempmute(ctx, member:commands.MemberConverter, duration: DurationConverter):

	multiplier = {"s": 1, "m": 60, "h": 3600, "d": 86400}
	amount, unit = duration

	guild = ctx.guild
	mutedRole = discord.utils.get(guild.roles, name="Muted")

	if not mutedRole:
	    mutedRole = await guild.create_role(name="Muted")

	    for channel in guild.channels:
	        await channel.set_permissions(mutedRole, speak=False, send_messages=False)
	embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
	await ctx.send(embed=embed)
	await member.add_roles(mutedRole)
	await member.send(f" you have been muted from: {guild.name}")
	await asyncio.sleep(amount * multiplier[unit])
	mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
	await member.remove_roles(mutedRole)
	await member.send(f" you have unmutedd from: - {ctx.guild.name}")
	embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
	await ctx.send(embed=embed)



@tempmute.error
async def tempmute(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
	    await ctx.send("Please use arguments correctly >tempmute <member> [duration in s, m, h, d]")
	    return
	elif isinstance(error, commands.BadArgument):
		await ctx.send("Please use arguments correctly >tempmute <member> [duration in s, m, h, d]")
		return
	elif isinstance(error, commands.MissingPermissions):
		await ctx.send("You Lack permissions To use this commands you must have Mute members permissions")



@client.command()
async def cat(ctx):
    await ctx.message.delete()
    r = requests.get('https://memes.blademaker.tv/api/Cats')
    res = r.json()
    title = res['title']
    ups = res['ups']
    downs = res['downs']
    sub = res['subreddit']
    m = discord.Embed(title=f'Cats\n', description = res['author'], color=0x00ffe1)
    m.set_image(url = res['image'])
    m.set_footer(text=f'👍: {ups}' + ' 💝: ' + format(random.randint(10000, 500000)))
    mes = await ctx.send(embed=m)

@client.command(aliases = ["pfp", "pfp_pic"])
async def profile_pic(ctx, member: discord.User):
	if member == None:
		member == ctx.author

	embed = discord.Embed(title = f"Profile Picture of {member.display_name}", color = member.color)
	embed.set_image(url = member.avatar_url)
	embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Asked by {ctx.author.display_name}#{ctx.author.discriminator}")
	await ctx.send(embed=embed)

@profile_pic.error
async def profile_pic(ctx, error):
	await ctx.send("Please use the arguments correctly >pfp <member>")



mainshop = [{"name":"watch", "price":100, "description": "Not tells u time?"},
            {"name":"laptop", "price":1000, "description": "A LAPTOPPPPP"},
            {"name":"pc", "price": 10000, "description":"Not a gaming one for online classes"},
            {"name":"toy", "price": 50, "description":"A thing for kids"},
            {"name":"gun", "price": 60, "description":"A gun for kids"},
            {"name":"glasses", "price":50, "description":"SWAG"},
            {"name":"cream", "price": 25, "description":"COLD"},
            {"name":"shirt", "price": 10, "description":"A shirt"},
            {"name":"pants", "price":10, "description":"A pant"},
            {"name":"candy", "price":10, "description":"A CANDY"},
            {"name":"pizza", "price":10, "description":"A PIZZA"},
            {"name":"sushi", "price":10, "description":"A SUSHI"}]


@client.command(name = "acc")
async def acc(ctx):

    user = ctx.author

    await open_account(user)

    users  = await get_bank_data()

    walletgg = users[str(user.id)]["wallet"]
    bankgg = users[str(user.id)]["bank"]

    em = discord.Embed(title = f'{user.display_name}\'s balance', color = 0xff0000)
    em.set_thumbnail(url = ctx.author.avatar_url)
    em.add_field(name = f"{user}'s account", value = "Name = " + format(ctx.author.name))
    em.add_field(name = "Wallet", value = walletgg, inline = False)
    em.add_field(name = "Bank", value = bankgg, inline = False)
    await ctx.send(embed = em)









@client.command()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.send(f"You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]




























@client.command(aliases = ["lb"])
async def leaderboard(ctx,x = 1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        em.add_field(name = f"{index}." , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)



@client.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "Bag", color = ctx.author.color)
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)    

    await ctx.send(embed = em)  

@client.command()
async def open_acc(ctx):

    user = ctx.author

    users  = await get_bank_data()

    if str(user.id) in users:
        await ctx.send("You already have an account")
    else:
        await ctx.send("Account created")

    await open_account(ctx.author)

    user = ctx.author

    users  = await get_bank_data()

@client.command(aliases = ["bal"])
async def balance(ctx):

    user = ctx.author

    await open_account(user)

    users  = await get_bank_data()

    walletgg = users[str(user.id)]["wallet"]
    bankgg = users[str(user.id)]["bank"]

    em = discord.Embed(title = f'{user.display_name}\'s balance', color = 0xff0000)
    em.add_field(name = "Wallet", value = walletgg, inline = False)
    em.add_field(name = "Bank", value = bankgg, inline = False)
    await ctx.send(embed = em)

@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users  = await get_bank_data()

    earnings = random.randrange(1001)

    if earnings >= 500:
        await ctx.send(f"You got lucky someone gave you {earnings} coins!")
    elif earnings < 500:
        await ctx.send(f"Someone gave you {earnings} coins!")
    elif earnings >= 900:
        await ctx.send(f"wtf someone gave you {earnings} coins you got lucky!")
    elif earnings == 1000:
        await ctx.send(f"wtf inpossible you got {earnings} coins!!")


    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump(users,f)

@beg.error
async def beg(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"I am not that fast",description=f"Try again in {error.retry_after:.2f}s.", color=0xff0000)
        await ctx.send(embed=em)
@client.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def work(ctx):
    await open_account(ctx.author)
    
    user = ctx.author

    users  = await get_bank_data()

    earnings = random.randrange(1000, 5000)
    if earnings == 1000:
        await ctx.send(f"You may have worked better {ctx.author.mention}")
    else:
        await ctx.send(f"{ctx.author.mention} you got ${earnings} by working")


    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump(users,f)
@work.error
async def work(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"I am not that fast",description=f"Try again in {error.retry_after:.2f}s.", color=0xff0000)
        await ctx.send(embed=em)
@client.command()
async def shop(ctx):
    em = discord.Embed(title = "Shop", color = ctx.author.color )

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        description = item["description"]
        em.add_field(name = name, value = f"💵{price} | {description}")
    await ctx.send(embed = em)

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    await open_account(ctx.author)
    
    user = ctx.author

    users  = await get_bank_data()

    earnings = random.randrange(100, 10000)
    if earnings == 100:
        await ctx.send(f"You may have got better {ctx.author.mention} you got ${earnings}")
    else:
        await ctx.send(f"{ctx.author.mention} you got ${earnings} as daily reward")


    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump(users,f)
@daily.error
async def daily(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"You already claimed it",description=f"YOU ARE ON A DEFAULT COOLDOWN OF 1 DAY", color=0xff0000)
        await ctx.send(embed=em)
@client.command()
@commands.cooldown(1, 604800, commands.BucketType.user)
async def weekly(ctx):
    await open_account(ctx.author)
    
    user = ctx.author

    users  = await get_bank_data()

    earnings = random.randrange(10000, 100000)
    if earnings == 100:
        await ctx.send(f"You may have got better {ctx.author.mention} you got ${earnings}")
    else:
        await ctx.send(f"{ctx.author.mention} you got ${earnings} as weekly reward")


    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump(users,f)
@weekly.error
async def weekly(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"You already claimed it",description=f"YOU ARE ON A DEFAULT COOLDOWN OF 1 WEEK", color=0xff0000)
        await ctx.send(embed=em)
@client.command(aliases=["with"])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)

    if amount == None:
        em = discord.Embed(title = "Argument error", description = "please use >withdraw (amount)", color=0xff0000)
        await ctx.send(embed = em)
        return

    if amount == "max" or amount == "all":
        users = await get_bank_data()
        user = ctx.author
        amount = int(users[str(user.id)]["bank"])
        bank = int(users[str(user.id)]["bank"])
        wallet = int(users[str(user.id)]["wallet"])
        bank -= amount
        wallet += amount
        users[str(user.id)]["bank"] = bank
        users[str(user.id)]["wallet"] = wallet
        with open("mainbank.json","w") as f:
            json.dump(users, f)
        await ctx.send(f"You withdrawed your coins safely!")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount>bal[1]:
        await ctx.send("You dont have that much of money!")
        return
    if amount<0:
        await ctx.send("Amount must be a positive number!")
        return
    
    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,"bank")
    await ctx.send(f"You withdrawed {amount} coins!")
@client.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return


    await ctx.send(f"You just bought {amount} {item}")

@client.command(aliases=["dep"])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)

    if amount == None:
        em = discord.Embed(title = "Argument error", description = "please use >deposit (amount)", color=0xff0000)
        await ctx.send(embed = em)
        return

    await open_account(ctx.author)

    if amount == "max" or amount == "all":
        users = await get_bank_data()
        user = ctx.author
        amount = int(users[str(user.id)]["wallet"])
        bank = int(users[str(user.id)]["bank"])
        wallet = int(users[str(user.id)]["wallet"])
        bank += amount
        wallet -= amount
        users[str(user.id)]["bank"] = bank
        users[str(user.id)]["wallet"] = wallet
        with open("mainbank.json","w") as f:
            json.dump(users, f)
        await ctx.send(f"You deposited your coins safely!")
        return
    else:
	    bal = await update_bank(ctx.author)

	    amount = int(amount)

	    if amount>bal[0]:
	        await ctx.send("You dont have that much of money!")
	        return
	    if amount<0:
	        await ctx.send("Amount must be a positive number!")
	        return
	    
	    await update_bank(ctx.author,-1*amount)
	    await update_bank(ctx.author,amount,"bank")
	    await ctx.send(f"You deposited {amount} coins!")

@client.command(aliases=["send"])
@commands.cooldown(1, 60, commands.BucketType.user)
async def give(ctx,member: discord.Member, amount = None):
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        em = discord.Embed(title = "Argument error", description = "please use >give (member) (amount)", color=0xff0000)
        await ctx.send(embed = em)
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount>bal[1]:
        await ctx.send("You dont have that much of money!")
        return
    if amount<0:
        await ctx.send("Amount must be a positive number!")
        return
    
    await update_bank(ctx.author,-1*amount, "bank")
    await update_bank(member,amount,"bank")
    await ctx.send(f"You gave {amount} coins to {member.mention}!")
@give.error
async def give(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"I am not that fast",description=f"Try again in {error.retry_after:.2f}s.", color=0xff0000)
        await ctx.send(embed=em)


@client.command(aliases=["rb"])
@commands.cooldown(1, 3600, commands.BucketType.user)
async def rob(ctx,member: discord.Member):
    await open_account(ctx.author)
    await open_account(member)

    bal = await update_bank(member)


    if bal[0]<100:
        await ctx.send("He dont have even 100 coins lol")
        return

    earnings = random.randrange(0, 100)

    
    await update_bank(ctx.author,earnings)
    await update_bank(member,-1*earnings)
    await ctx.send(f"You robbed {earnings} coins!")
@rob.error
async def rob(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"I am not that fast",description=f"Try again in {error.retry_after:.2f}s.", color=0xff0000)
        await ctx.send(embed=em)
@client.command()
async def bet(ctx,amount = None):
    await open_account(ctx.author)

    if amount == None:
        em = discord.Embed(title = "Argument error", description = "please use >bet (amount)", color=0xff0000)
        await ctx.send(embed = em)
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount>bal[0]:
        await ctx.send("You dont have that much of money!")
        return
    if amount<0:
        await ctx.send("Amount must be a positive number!")
        return
    
    final = []
    for i in range(3):
        a = random.choice(["<:staygold:837194554057818152>", "<:RANZERS_SERVER2:836546762134650910>", "<:staydark:837195326250811392>", "👀", "<:peperee:837197677325451285>", "<:nani:837196665253003265>", "<:reddittroll:837197956511563776>", "<:bigbrain:837199486416846890>", "<:villagerwhat:837198159775006730>", "<:Youtuber:827071539999539230>"])

        final.append(a)
    
    await ctx.send(str(final))

    if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
        await update_bank(ctx.author,2*amount)
        await ctx.send("You won")
    else:
        await update_bank(ctx.author,-1*amount)
        await ctx.send("You lost")

async def open_account(user):


    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 1000
        users[str(user.id)]["bank"] = 1000
        await user.send("```\nHey welcome to my bank community you recived 1000 in your bank and wallet as your starter make sure to use dep all to keep your coins safe in your bank and use daily and weekly for ur daily and weekly rewards thankyou for using Ranzers\n```")

    with open("mainbank.json","w") as f:
        json.dump(users, f)
    return True


async def get_bank_data():
    with open("mainbank.json","r") as f:
        users = json.load(f)
    return users

async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json","w") as f:
        json.dump(users,f)
    
    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
    return bal



@client.command(aliases = ["pic"])
async def image(ctx):

	subreddit = reddit.subreddit("pics")

	all_subs = []

	top = subreddit.top(limit = 100)

	for submission in top:
		all_subs.append(submission)

	random_sub = random.choice(all_subs)

	name = random_sub.title
	url = random_sub.url

	em = discord.Embed(description = f"**[{name}]({url})**",  color = ctx.author.color)
	em.set_image(url = url)

	await ctx.send(embed = em)

@client.command()
async def dog(ctx):
	subreddit = reddit.subreddit("dogpictures")

	all_subs = []

	top = subreddit.top(limit = 100)

	for submission in top:
		all_subs.append(submission)

	random_sub = random.choice(all_subs)

	name = random_sub.title
	url = random_sub.url

	em = discord.Embed(description = f"**[{name}]({url})**",  color = ctx.author.color)
	em.set_image(url = url)

	await ctx.send(embed = em)

@client.command()
async def news(ctx):

	await ctx.send("Getting a news for you give me some secs")

	subreddit = reddit.subreddit("news")

	all_subs = []

	top = subreddit.top(limit = 100)

	for submission in top:
		all_subs.append(submission)

	random_sub = random.choice(all_subs)

	name = random_sub.title
	url = random_sub.url

	em = discord.Embed(description = f"**[{name}]({url})**",  color = ctx.author.color)

	await ctx.send(embed = em)

@client.command(aliases =  ["rpic"])
async def randompic(ctx):

	subreddit = reddit.subreddit("RandomPics")

	all_subs = []

	top = subreddit.top(limit = 100)

	for submission in top:
		all_subs.append(submission)

	random_sub = random.choice(all_subs)

	name = random_sub.title
	url = random_sub.url

	em = discord.Embed(description = f"**[{name}]({url})**",  color = ctx.author.color)
	em.set_image(url = url)

	await ctx.send(embed = em)


client.load_extension("cogs.afk")

@client.command()
async def testembed(ctx):
    embed = discord.Embed(colour=ctx.author.color, timestamp=ctx.message.created_at)
    embed.set_author(name='Test')
    embed.set_footer(text=f'Called by {ctx.author}', icon_url=ctx.author.avatar_url)
    embed.add_field(name='Test', value='Test Done')

    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def prefix(ctx):
  with open("prefixes.json", "r") as f:
      prefixes = json.load(f)

  pre = prefixes[str(ctx.guild.id)] 

  await ctx.send(f"```\n hello my current prefix in the server is ({pre}) please use ({pre}help) to get a list of commands\n```")





@client.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)

        with open('users.json', 'w') as f:
            json.dump(users, f)

    await client.process_commands(message)




keep_alive()
client.run(os.getenv("TOKEN"))