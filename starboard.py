
from silverutil import get_token
import discord
from discord.ext import *
from discord.ext import commands
import os
import datetime
import requests
available_guilds = [
    779136383033147403,
    706353387855151105
    ]
board_channels = [
    900850921481834526,
    903321629327773756
]
bot = commands.Bot(command_prefix=commands.when_mentioned_or('. ','.','proportion + '),help_command=None)
os.chdir('h:\\frart')

pin_emojis=['📌']  #emojis that pin the message and remove the reaction
star_emojis=['⭐'] #emojis that pin the message without removing the reaction

async def handle_pin(payload_channel_id,payload_message_id,payload_emoji,payload_member,preg):
    MessageChannel=bot.get_channel(payload_channel_id) #get channel of the original message this is useful for everything
    pinnable=True #default pinnable to true
    with open('pinned.txt', 'r') as the_file: #open up pinned files.txt
        pinned=the_file.readlines() #read into list
    for i in pinned: #iterate
        try:
            if int(i.strip('\n'))==payload_message_id: pinnable=False #already pinned, dont send it *again* in the pins channel.
            
        except:
            pass #i had some dummy entries that couldnt be interpreted as integers
    if not pinnable: print('could not be pinned, already pinned')
    if preg: 
        if str(payload_emoji)[0] in ['🤰','🆎','🥵']:
            #pinnable=True
            print("It's Preg")
    if MessageChannel==bot.get_channel(900850921481834526): pinnable=False
    if pinnable:
        print('can be pinned')
        message=await MessageChannel.fetch_message(payload_message_id) #get the message itself
        #if str(payload_emoji)[0] in pin_emojis: await message.remove_reaction(payload_emoji, payload_member)
        jumpfooter="\n\n**[Click to jump to message!]("+message.jump_url+")**"
        embed=discord.Embed(title="", description=message.content+jumpfooter,color=0xEEE2A0,timestamp=message.created_at)
        embed.set_author(name=message.author.display_name+(' 🤖'*message.author.bot), icon_url=message.author.avatar_url)
        imaged=False
        embed.set_footer(text="MessageID: "+str(payload_message_id))
        has_stuff=False
        imgurl=False
        if 'http' in message.content:
            cs_=message.content.split(' ')
            for i in cs_:
                if i.startswith('http'):
                    imgurl=i
                    break
        hasreply=False
        if message.reference: hasreply=True
        if hasreply: embed.description=message.content
        if message.attachments: imgurl=message.attachments[0].url
        if imgurl: has_stuff=True
        blah=False
        if has_stuff:
            image_exts=['png','jpg','webp','gif','jpeg']
            video_exts=['mp4','webm','mov']
            audio_exts=['wav','mp3','flac','ogg']
            has_image=False
            has_video=False
            has_audio=False
            for ext in image_exts:
                if ext in imgurl.lower(): has_image=True
            for ext in video_exts:
                if ext in imgurl.lower(): has_video=True
            for ext in audio_exts:
                if ext in imgurl.lower(): has_audio=True
            components=imgurl.split('.')
            original_filename=('.'.join(components[-2:])).split('/')[-1]
            if has_image:
                embed.set_image(url=imgurl)
                blah=True
            elif has_video:
                desc='['+original_filename+']('+imgurl+')'+"\n\n**[Click to watch!]("+message.jump_url+")**"
                if not hasreply: embed.description=desc
                with open('R:\\inputfile.mkv', 'wb') as f:
                    f.write(requests.get(imgurl).content)
                #os.system('ffmpeg -i R:\\inputfile.mkv -vf "select=eq(n\,0)" -q:v 3 R:\\FirstFrame.jpg -y')
                os.system('ffmpeg -i R:\\inputfile.mkv -lavfi "scale=256x256,fps=1,palettegen=max_colors=32:stats_mode=diff" R:\\palette.png -y')
                os.system('ffmpeg -i R:\\inputfile.mkv -i R:\\palette.png -lavfi "fps=25,scale=-1:240,mpdecimate,paletteuse=dither=none" -fs 8M R:\\FirstFrame.gif -y')
                with open('R:\\FirstFrame.gif', 'rb') as f:
                    imaged=True
                    f2 = discord.File(f, filename='image.gif')
                    embed.set_image(url="attachment://"+str('image.gif'))
                blah=True
            elif has_audio:
                desc='['+original_filename+']('+imgurl+')'+"\n\n**[Click to listen!]("+message.jump_url+")**"
                if not hasreply: embed.description=desc
            else:
                desc='['+original_filename+']('+imgurl+')'+jumpfooter
                if not hasreply: embed.description=desc
        
        if message.embeds: imgurl=message.embeds[0].image
        if message.embeds: #embeds like Starboard does
            if not has_stuff: 
                og_embed=message.embeds[0]
                try:
                    desc=og_embed.description+jumpfooter
                except:
                    desc=jumpfooter
                embed=discord.Embed(title=og_embed.title, description=desc,color=0xEEE2A0,timestamp=message.created_at)
                try:
                    if not hasreply: embed.description=og_embed.description+jumpfooter
                    if hasreply: embed.description=og_embed.description
                except:
                    if not hasreply: embed.description=jumpfooter
                    if hasreply: embed.description=''
                if og_embed.thumbnail:
                    if not has_stuff: embed.set_thumbnail(url=og_embed.thumbnail.url)
                if og_embed.image:
                    if not has_stuff: embed.set_image(url=og_embed.image.url)
                embed.set_author(name=message.author.display_name+(' 🤖'*message.author.bot), icon_url=message.author.avatar_url)
                embed.set_footer(text="MessageID: "+str(payload_message_id))
                for field in og_embed.fields:
                    embed.add_field(name=field.name,value=field.value,inline=field.inline) 
            
            
        #Reply handling, always goes after processing of all.
        if message.reference:
            replymessage=await bot.get_channel(message.reference.channel_id).fetch_message(message.reference.message_id)
            embed.add_field(name='Replying to '+replymessage.author.display_name,value=replymessage.content+"\n\n**[Replying to this message]("+replymessage.jump_url+")**"+jumpfooter,inline=False)
        if message.guild==bot.get_guild(779136383033147403): MessageChannel=bot.get_channel(900850921481834526) #BUTTPLUG: A Post-Hummus RPG
        if message.guild==bot.get_guild(706353387855151105): MessageChannel=bot.get_channel(903321629327773756) #EzoGaming
        if preg:
            if str(payload_emoji)[0]=='🤰': 
                MessageChannel=bot.get_channel(980788645579595796) #Hilarious Bot
            if str(payload_emoji)[0]=='🆎': 
                MessageChannel=bot.get_channel(980788685987532810) #Announceboard
            if str(payload_emoji)[0]=='🥵': 
                MessageChannel=bot.get_channel(936315324691795979) #hotboard
        omc=bot.get_channel(payload_channel_id)
        if imaged:
            await MessageChannel.send(omc.mention,file=f2,embed=embed)
        else:
            await MessageChannel.send(omc.mention,embed=embed)
        with open('pinned.txt', 'a') as the_file:
            the_file.write(str(payload_message_id)+'\n')
        if str(payload_emoji)[0] in pin_emojis: await message.remove_reaction(payload_emoji, payload_member)


@bot.event
async def on_raw_reaction_add(payload): #on_raw_reaction_add also sees really old messages get reacted, thus this command works on even the first message of the server from 2020
    if str(payload.emoji)[0] in pin_emojis or str(payload.emoji)[0] in star_emojis: #check if the emoji is in the reactions. [0] means that any skin color emoji can be used to react to a man emoji for example probably, i didnt test, it was really just a leftover from trying to get it to register the emoji as a character
        await handle_pin(payload.channel_id,payload.message_id,payload.emoji,payload.member,True)

@bot.event
async def on_ready():
    dynamic_limit=2000
    for guild in bot.guilds:
        if guild.id in available_guilds:
            #print(guild)
            for channel in guild.channels:
                if channel.id not in board_channels:
                    print(channel)
                    try:
                        async for message in channel.history(limit=dynamic_limit):
                            for reaction in message.reactions:
                                emo=str(reaction.emoji)[0]
                                #print(emo)
                                if emo in pin_emojis:
                                    print('found pin in '+str(channel))
                                    async for user in reaction.users():
                                        user_=user
                                        break
                                    #print(user_)
                                    await handle_pin(channel.id,message.id,reaction.emoji,user_,False)
                    except AttributeError:
                        pass
                    except discord.errors.Forbidden:
                        print('wtf')
                        print(channel)

                                
    
token=get_token()
bot.run(token)