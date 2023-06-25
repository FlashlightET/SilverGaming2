from silverutil import get_token
import discord
from discord.ext import *
from discord.ext import commands
#from discord import app_commands
import os
import requests


#Set Up Teh Loggah!
import logging
log_format = '[%(name)s] %(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(format=log_format,datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger=logging.getLogger('SILVERGAMING')



from PIL import Image

from discord import (
    SlashCommandOption as Option,
    ApplicationCommandInteraction as APPCI
)





import pytesseract
import asyncio
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Subtitle Edit\Tesseract302\tesseract.exe'
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or('. ','.','proportion + '),help_command=None,intents=intents, sync_commands=True, sync_commands_on_cog_reload=True)
os.chdir('h:\\frart')
#tree = app_commands.CommandTree(bot)
for file in os.listdir('h:/frart/cogs'):
    if file.endswith('_commands.py'):
        a='pee'
        bot.load_extension("cogs."+file[:-3])
        print(file+" loaded")
        #bot.load_extension("cogs.meme_commands")
#bot.load_extension("cogs.meme_commands")

@bot.command() #this code block is shamefully stolen from dannybot
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('loaded')

@bot.command() #this code block is shamefully stolen from dannybot
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send('unloaded')

@bot.command(aliases=['r']) #this code block is shamefully stolen from dannybot 
@commands.is_owner()
async def reload(ctx, extension):
    if extension=='uc': extension='utility_commands'
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send('reloaded')


@bot.event
async def on_ready():
    await bot.get_channel(964931350534696960).send('Bot Connected!')
    #await bot.get_channel(964958868004298833).send('please accept ezogothacked\'s request <@407564713740861440> this is legit')




@bot.event
async def on_message_delete(message):
    logchannel = Get_Log_Channel(message.guild)
    print('a')
    embed=discord.Embed(title="Message Deleted", description='A message by **'+str(message.author.name)+'#'+str(message.author.discriminator)+'** in **#'+str(message.channel.name)+'** was deleted.', color=0xff0000)
    embed.set_author(name=str(message.author.name)+'#'+str(message.author.discriminator), icon_url=message.author.avatar_url)
    embed.set_footer(text="SilverGaming Audit Log")
    #await logchannel.send(embed=embed)
    #await logchannel.send('A message by **'+str(message.author.name)+'#'+str(message.author.discriminator)+'** in **#'+str(message.channel.name)+'** was deleted.')

@bot.event
async def on_message_edit(message,after):
    logchannel = Get_Log_Channel(message.guild)
    embed=discord.Embed(title="Message Edited", description='A [message]('+message.jump_url+') by **'+str(message.author.name)+'#'+str(message.author.discriminator)+'** in **#'+str(message.channel.name)+'** was edited.', color=0x0000ff)
    embed.set_author(name=str(message.author.name)+'#'+str(message.author.discriminator), icon_url=message.author.avatar_url)
    embed.set_footer(text="SilverGaming Audit Log")
    #await logchannel.send(embed=embed)

@bot.event
async def on_bulk_message_delete(messages):
    logchannel = Get_Log_Channel(messages[0].guild)
    await logchannel.send(str(len(messages))+' messages in **#'+str(messages[0].channel.name)+'** were deleted.')

@bot.event
async def on_reaction_add(reaction,user):
    message=reaction.message
    logchannel = Get_Log_Channel(reaction.message.guild)
    print('ReactionAdd')
    embed=discord.Embed(title="Reaction added", description='A reaction was added by **'+user.name+'#'+str(user.discriminator)+'** to a [message]('+message.jump_url+') by **'+str(reaction.message.author.name)+'** in **#'+str(reaction.message.channel.name)+'**.', color=0x00ff00)
    embed.set_author(name=str(user.name), icon_url=user.avatar_url)
    embed.set_footer(text="SilverGaming Audit Log")
    #await logchannel.send(embed=embed)
    #await logchannel.send('A reaction was added by **'+user.name+'#'+str(user.discriminator)+'** to a message by **'+str(reaction.message.author.name)+'#'+str(reaction.message.author.discriminator)+'** in **#'+str(reaction.message.channel.name)+'**.')

@bot.event
async def on_reaction_remove(reaction,user):
    message=reaction.message
    logchannel = Get_Log_Channel(reaction.message.guild)
    print('ReactionAdd')
    embed=discord.Embed(title="Reaction removed", description='A reaction was removed by **'+user.name+'#'+str(user.discriminator)+'** from a [message]('+message.jump_url+') by **'+str(reaction.message.author.name)+'** in **#'+str(reaction.message.channel.name)+'**.', color=0xff0000)
    embed.set_author(name=str(user.name), icon_url=user.avatar_url)
    embed.set_footer(text="SilverGaming Audit Log")
    #await logchannel.send(embed=embed)
    #await logchannel.send('A reaction was added by **'+user.name+'#'+str(user.discriminator)+'** to a message by **'+str(reaction.message.author.name)+'#'+str(reaction.message.author.discriminator)+'** in **#'+str(reaction.message.channel.name)+'**.')

@bot.event
async def on_reaction_clear(message,reactions):
    logchannel = Get_Log_Channel(message.guild)
    embed=discord.Embed(title="Reactions cleared", description='A [message]('+message.jump_url+') by **'+str(message.author.name)+'#'+str(message.author.discriminator)+'** in **#'+str(message.channel.name)+'** had all of its reactions cleared.', color=0xff0000)
    embed.set_author(name=str(message.author.name)+'#'+str(message.author.discriminator), icon_url=message.author.avatar_url)
    embed.set_footer(text="SilverGaming Audit Log")
    #await logchannel.send(embed=embed)
    #await logchannel.send('A message by **'+str(message.author.name)+'#'+str(message.author.discriminator)+'** in **#'+str(message.channel.name)+'** had all of its reactions cleared.')

@bot.event
async def on_guild_channel_create(channel):
    logchannel = Get_Log_Channel(channel.guild)
    embed=discord.Embed(title="Channel Created", description='Channel **#'+str(channel.name)+'** created.', color=0x00ff00)
    embed.add_field(name="Name", value=channel.name, inline=False)
    embed.add_field(name="Topic", value=channel.topic, inline=False)
    embed.set_footer(text="SilverGaming Audit Log")
    await logchannel.send(embed=embed)
    #await logchannel.send('Channel **#'+str(channel.name)+'** created.')

@bot.event
async def on_guild_channel_delete(channel):
    logchannel = Get_Log_Channel(channel.guild)
    embed=discord.Embed(title="Channel Deleted", description='Channel **#'+str(channel.name)+'** deleted.', color=0xff0000)
    embed.set_footer(text="SilverGaming Audit Log")
    await logchannel.send(embed=embed)
    #await logchannel.send('Channel **#'+str(channel.name)+'** deleted.')

@bot.event
async def on_guild_channel_update(before, after):
    IsValid=False
    logchannel = Get_Log_Channel(before.guild)
    embed=discord.Embed(title="Channel Updated", description='Channel **#'+str(after.name)+'** updated.', color=0x0000ff)
    if before.name!=after.name:
        IsValid=True
        embed.add_field(name="Old Name", value=before.name, inline=False)
        embed.add_field(name="New Name", value=after.name, inline=False)
    try:
        if before.topic!=after.topic:
            IsValid=True
            embed.add_field(name="Old Topic", value=before.topic, inline=False)
            embed.add_field(name="New Topic", value=after.topic, inline=False)
    except AttributeError:
        pass
    embed.set_footer(text="SilverGaming Audit Log")
    if IsValid: await logchannel.send(embed=embed)
    #if before.name!=after.name:
    #    await logchannel.send('Channel **#'+str(before.name)+'** renamed to **#'+str(after.name)+'**.')
    #if before.topic!=after.topic:
    #    await logchannel.send('Channel **#'+str(after.name)+'** topic `'+str(before.topic)+'` changed to `'+str(after.topic)+'`.')

@bot.event
async def on_member_update(before, after):
    #print('MemberUpdate')
    usn=f'\@{before.name}' if str(before.discriminator)=='0' else f'{before.name}#{before.discriminator}'
    
    embed=discord.Embed(title="Member Updated", description='User **'+usn+'** updated their server profile.', color=0x0000ff)
    yeah=False
    if before.nick!=after.nick:
        logchannel = Get_Log_Channel(before.guild)
        yeah=True
        embed.add_field(name="Old Name", value=str(before.nick), inline=False)
        embed.add_field(name="New Name", value=str(after.nick), inline=False)
    #Add avatar change handler?
    embed.set_author(name=str(after.name), icon_url=after.avatar_url)
    embed.set_footer(text="SilverGaming Audit Log")
    if yeah: await logchannel.send(embed=embed)
    #await logchannel.send('User **'+before.name+'#'+str(before.discriminator)+'** changed their nickname from **'+str(before.nick)+'** to **'+str(after.nick)+'**.')

@bot.event
async def on_guild_update(before, after):
    #print('GuildUpdate')
    imaged=False
    logchannel = Get_Log_Channel(before)
    embed=discord.Embed(title="Server Updated", description='Server has been updated', color=0x0000ff)
    if before.name!=after.name:
        embed.add_field(name="Name", value='Changed from **'+str(before.name)+'** to **'+str(after.name)+'**.', inline=False)
    if before.afk_channel!=after.afk_channel:
        embed.add_field(name="AFK Channel", value='Changed from **'+str(before.afk_channel.name)+'** to **'+str(after.afk_channel.name)+'**.', inline=False)
    if before.banner_url!=after.banner_url:
        #embed.add_field(name="Banner", value='Changed', inline=False)
        with open('bann.png', 'wb') as f: 
            f.write(requests.get(after.banner_url).content) #saves file
        with open('bann.png', 'rb') as f:
            imaged=True
            f2 = discord.File(f, filename='image.png')
            embed.set_image(url="attachment://"+str('image.png'))
            embed.add_field(name="Banner", value='Changed.', inline=False)



    if before.icon_url!=after.icon_url:
        with open('icon.png', 'wb') as f: 
            f.write(requests.get(after.icon_url).content) #saves file
        with open('icon.png', 'rb') as f:
            imaged=True
            f2 = discord.File(f, filename='image.png')
            embed.set_image(url="attachment://"+str('image.png'))
            embed.add_field(name="Icon", value='Changed.', inline=False)








    embed.set_footer(text="SilverGaming Audit Log")
    if imaged: 
        await logchannel.send(file=f2,embed=embed)
    else:
        await logchannel.send(embed=embed)
    #await logchannel.send('User **'+before.name+'#'+str(before.discriminator)+'** changed their nickname from **'+str(before.nick)+'** to **'+str(after.nick)+'**.')



@bot.event
async def on_guild_role_update(before, after):
    #print('RoleUpdate')
    embed=discord.Embed(title="Role Updated", description='Role has been updated', color=0x0000ff)
    logchannel = Get_Log_Channel(before.guild)
    if before.name!=after.name:
        embed.add_field(name="Name", value='Changed from **'+str(before.name)+'** to **'+str(after.name)+'**.', inline=False)
        embed.set_footer(text="SilverGaming Audit Log")
        await logchannel.send(embed=embed)
    
@bot.event
async def on_guild_role_create(before):
    #print('RoleUpdate')
    embed=discord.Embed(title="Role Created", description='Role has been created', color=0x00ff00)
    logchannel = Get_Log_Channel(before.guild)
    embed.add_field(name="Name", value='**'+str(before.name)+'**', inline=False)
    embed.set_footer(text="SilverGaming Audit Log")
    await logchannel.send(embed=embed)

@bot.event
async def on_guild_role_delete(before):
    #print('RoleUpdate')
    embed=discord.Embed(title="Role Deleted", description='Role has been deleted', color=0xff0000)
    logchannel = Get_Log_Channel(before.guild)
    embed.add_field(name="Name", value='**'+str(before.name)+'**', inline=False)
    embed.set_footer(text="SilverGaming Audit Log")
    await logchannel.send(embed=embed)
import traceback
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    

    #eror=traceback.format_exc()
    embed=discord.Embed(title='Error', color=0xee2211, description='`'+str(error)+'`')
    embed.set_footer(text='lmao')
    await ctx.reply(embed=embed)
    raise error
    
    
@bot.event
async def on_message(before):
    # if before.attachments:
        # for i in before.attachments:
            # z=requests.get(i.url).content
            # with open('tmp.png','wb') as f:
                # f.write(z)
            # isCool=True
            # for b in ['mp3','wav','mp4']:
                # if i.url.endswith(b): isCool=False
            # if isCool: text=pytesseract.image_to_string(Image.open('tmp.png')) + i.url
            # if not isCool: text=i.url
            # print(text)
            # for yass in ['yass','yah','tiktok','smurf','slay','queen','camp','drag','fierce']:
                # if yass in text.lower():
                    # await before.add_reaction('💅')
            # for yass in ['eau','aux','eux','oux','uille','uill']:
                # if yass in text.lower():
                    # await before.add_reaction('🥖')
            # if ' le ' in text.lower() or text.lower().startswith('le '):
                # await before.add_reaction('🥖')
            # if 'poo' in text.lower(): 
                # await before.add_reaction('💩')
            # if 'laughter' in text.lower(): 
                # await before.add_reaction('😂')
            # if 'brap' in text.lower(): 
                # await before.add_reaction('💨')
            
            # for blart in ['in my','baja','ddlc','my house','yakuza','breaking bad','walter','meth','doki','literature','club','leffrey']:
                # if blart in text.lower():
                    # #emoji = get(bot.get_all_emojis(), name='leffreysoy2')
                    # await before.add_reaction('<:leffreysoy2:971914216904740864>')
            # for blart in ['gay','ay people','kay','k people']:
                # if blart in text.lower():
                    # #emoji = get(bot.get_all_emojis(), name='leffreysoy2')
                    # await before.add_reaction('<:gaypeople:1059615369003814994>')
            # for blart in ['dame','dane','da ne','baka','mitai','da me']:
                # if blart in text.lower():
                    # #emoji = get(bot.get_all_emojis(), name='leffreysoy2')
                    # await before.add_reaction('<:humantrafficking:900452097718378528>')
                    
                    
                    
            # for blart in ['bravo']:
                # if blart in text.lower():
                    # #emoji = get(bot.get_all_emojis(), name='leffreysoy2')
                    # await before.add_reaction('<:nekoboobs:934936250874478702>')
            # for blart in ['child','made in abyss','mia','riko','reg']:
                # if blart in text.lower():
                    # #emoji = get(bot.get_all_emojis(), name='leffreysoy2')
                    # await before.add_reaction('<:cheese_pizza:1049683785886732318>')
            # #await bot.process_commands(before)
                
            
            
    # for yass in ['yass','yah','tiktok','smurf','slay','queen','camp','drag','fierce']:
        # if yass in before.content.lower():
            # await before.add_reaction('💅')
    # for yass in ['eau','aux','eux','oux','uille','uill']:
        # if yass in before.content.lower():
            # await before.add_reaction('🥖')
    # if ' le ' in before.content.lower() or before.content.lower().startswith('le '):
        # await before.add_reaction('🥖')
    # if 'horse react' in before.content.lower(): 
        # await before.reference.resolved.add_reaction('🐴')
    # if 'pin this' in before.content.lower(): 
        # await before.reference.resolved.add_reaction('📌')
    # if 'poo' in before.content.lower(): 
        # await before.add_reaction('💩')
    # if 'laughter' in before.content.lower(): 
        # await before.add_reaction('😂')
    # if 'brap' in before.content.lower(): 
        # await before.add_reaction('💨')
    
    # for blart in ['in my','baja','ddlc','my house','yakuza','breaking bad','walter','meth','doki','literature','club','leffrey']:
        # if blart in before.content.lower():
            # #emoji = get(bot.get_all_emojis(), name='leffreysoy2')
            # await before.add_reaction('<:leffreysoy2:971914216904740864>')
    # for blart in ['gay','ay people','kay','k people']:
        # if blart in before.content.lower():
            # #emoji = get(bot.get_all_emojis(), name='leffreysoy2')
            # await before.add_reaction('<:gaypeople:1059615369003814994>')
    # for blart in ['dame','dane','da ne','baka','mitai','da me']:
        # if blart in before.content.lower():
            # #emoji = get(bot.get_all_emojis(), name='leffreysoy2')
            # await before.add_reaction('<:humantrafficking:900452097718378528>')
    # for blart in ['bravo']:
        # if blart in before.content.lower():
            # #emoji = get(bot.get_all_emojis(), name='leffreysoy2')
            # await before.add_reaction('<:nekoboobs:934936250874478702>')
            
            
            
            
    # for blart in ['child','made in abyss','mia','riko','reg']:
        # if blart in before.content.lower():
            # #emoji = get(bot.get_all_emojis(), name='leffreysoy2')
            # await before.add_reaction('<:cheese_pizza:1049683785886732318>')
    if before.content.startswith('.'): logger.info(before.author.name+' ran command '+'.'.join(before.content.split('.')[1:]))
    #if before.author.id==203882027366350859: await before.channel.send('https://tenor.com/view/bravo-gif-18088659')
    try:
        await bot.process_commands(before)
    except discord.ext.commands.CommandNotFound:
        pass
    



def Get_Log_Channel(guild):
    #print('b')
    #Uncomment these once i convince Danny to add audit log channel to server.
    if guild==bot.get_guild(779136383033147403): logchannel=bot.get_channel(964958868004298833)
    if guild==bot.get_guild(706353387855151105): logchannel=bot.get_channel(964931350534696960)
    #logchannel=bot.get_channel(964931350534696960) #EzoGaming Audit Log
    return logchannel

token=get_token()
bot.run(token)