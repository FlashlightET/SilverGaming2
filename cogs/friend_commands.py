import discord
from discord.ext import commands
from .silverutil import get_data, get_lang
from .silverutil import debug_log
import traceback
import random
import os
import time
import discord
import requests
import urllib
from PIL import Image
from discord.ext import commands
import json
import datetime as dt

#Set Up Teh Loggah!
import logging
log_format = '[%(name)s] %(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(format=log_format,datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger=logging.getLogger('FRIEND')

global friend_stack
friend_stack=0
oangry=""
angry=""
processing=0
idd=0
vc=0
contextfn="context.png"
contexturl=""
recents=[6942069420]*32
global tagshttp
global tagshttp1
global tagshttp2
global tagshttp3

tagshttp='["character:serval (kemono friends)", "sendable"]'
tagshttp1='["character:serval (kemono friends)", "sendable"]'
tagshttp2='["character:serval (kemono friends)", "sendable"]'
tagshttp3='["character:serval (kemono friends)", "sendable"]'
tagshttp4='["character:serval (kemono friends)", "sendable"]'



def SiteHandle(i,name,short):
    global sites
    global sites2
    global filelinks
    if name.lower() in i and short not in sites:
        filelinks=filelinks+', ['+name+']('+i+')'
        debug_log('(Friend) DEBUG: '+name+' link: '+i)
        sites.append(short)
        sites2.append(i)


def friend_fatness(friend_stack):
    size=os.stat('r:\\friend\\image'+str(friend_stack)+'.png').st_size/(1024*1024) #fucking windows and its mebibytes
    debug_log('(Friend) DEBUG: size='+str(size)+'MB')
    return size

def check_tags(metadata, service):
    debug_log('(Friend) DEBUG: Checking "'+service+'"...')
    try:
        print('EZOGAMING LOOK THERE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
        print('EZOGAMING LOOK THERE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
        print('EZOGAMING LOOK THERE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
        print('EZOGAMING LOOK THERE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
        print('EZOGAMING LOOK THERE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
        print('EZOGAMING LOOK THERE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
        print('EZOGAMING LOOK THERE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
        print('EZOGAMING LOOK THERE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
        print('EZOGAMING LOOK THERE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
        print('EZOGAMING LOOK THERE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
        print('EZOGAMING LOOK THERE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
        print('EZOGAMING LOOK THERE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
        print('EZOGAMING LOOK THERE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
        print(metadata['metadata'][0]["service_keys_to_statuses_to_tags"])
        print('EZOGAMING LOOK THERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!')
        print('EZOGAMING LOOK THERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!')
        print('EZOGAMING LOOK THERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!')
        print('EZOGAMING LOOK THERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!')
        print('EZOGAMING LOOK THERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!')
        print('EZOGAMING LOOK THERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!')
        print('EZOGAMING LOOK THERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!')
        print('EZOGAMING LOOK THERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!')
        print('EZOGAMING LOOK THERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!')
        print('EZOGAMING LOOK THERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!')
        print('EZOGAMING LOOK THERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!')
        print('EZOGAMING LOOK THERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!')
        print(metadata['metadata'][0]["service_names_to_statuses_to_tags"]['my tags']['0'])
        return metadata['metadata'][0]["service_names_to_statuses_to_tags"][service]['0']
        #print(tags2)
    except:
        debug_log('(Friend) DEBUG: Found no tags in "'+service+'"')
        return []

def check_tags2(metadata, service):
    debug_log('(Friend) DEBUG: Checking "'+service+'"...')
    try:
        print(metadata['metadata'][0]["service_keys_to_statuses_to_tags"]['my tags']['0'])
        return metadata['metadata'][0]["service_keys_to_statuses_to_tags"][service]['0']
        #print(tags2)
    except:
        debug_log('(Friend) DEBUG: Found no tags in "'+service+'"')
        return []

def combine_tags(tags1, tags2):
    tags=[]
    for i in tags1:
        tags.append(i)
    for i in tags2:
        if i not in tags: tags.append(i)
    return tags



class FriendCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_message(self, message):
        #print(message)
        if message.content=='sauce':
            if message.reference: 
                replying=await self.bot.get_channel(message.reference.channel_id).fetch_message(message.reference.message_id)
                if replying.attachments:
                    glooga=[]
                    for i in replying.attachments:
                        glooga.append(i.url)
                else:
                    glooga=[replying.content]
                print(glooga)
                for gloogi in glooga:
                    zooga=gloogi.split('/')[-1].split('.')[0]
                    print(zooga)
                    hydrusip="http://127.0.0.1:"+get_data("hydrus_port")
                    headers={'Hydrus-Client-API-Access-Key': get_data("hydrus_key")}
                    tagshttp='["system:hash='+zooga+'"]'
                    tagshttp2='["system:hash='+zooga+' md5"]'
                    req_prefix=hydrusip+"/get_files/search_files?system_inbox=true&tags="
                    request_1=requests.get(req_prefix+tagshttp, headers=headers)
                    request_2=requests.get(req_prefix+tagshttp2, headers=headers)
                    print(request_1)
                    recieved_1=request_1.json()
                    recieved_2=request_2.json()
                    print(recieved_1['file_ids'])
                    results=recieved_1['file_ids']+recieved_2['file_ids']+recieved_1['file_ids']
                    print(results)
                    results=list(set(results))
                    
                    try:
                        debug_log('(Friend) DEBUG: choosing image...')
                        result=random.choice(results)
                        tries=0
                        recents.pop(0)
                        recents.append(result)
                        debug_log('(Friend) DEBUG: requesting image...')
                        image=requests.get(hydrusip+'/get_files/file?file_id='+str(result), headers=headers)
                        meta=requests.get(hydrusip+'/get_files/file_metadata?file_ids=%5B'+str(result)+'%5D', headers=headers)
                        metadata=meta.json()
                        chares=[]
                        tags1=[]
                        tags2=[]
                        debug_log('(Friend) DEBUG: Checking Tags...')
                        tags1=check_tags2(metadata, '6c6f63616c2074616773')
                        tags2=check_tags2(metadata, '5623f549415038b40cc7ac843f0b99a66ec0c18df4acc58ee40020a258fc9954')
                        tags=combine_tags(tags1, tags2)
                        debug_log('(Friend) DEBUG: '+str(tags))
                        image_hash=metadata['metadata'][0]["hash"]
                        artist="No Artist Tag" #default artist tag if none present
                        chare=None
                        emote=None #default artist tag if none present
                        artists=[] #initialize the list of artists incase there are multiple names
                        emotes=[]
                        for i in tags:
                            if i.startswith("creator:"): #this namespace is artists
                                artists.append(i[8:]) #add artist to list
                            if i.startswith("character:"): #this namespace is artists
                                chares.append(i[10:].replace(" (kemono friends)","")) #add artist to list
                        if len(artists)>0: #if there are any artists
                            artist="/".join(artists) #add discriminator for different usernames
                        for i in tags:
                            if i.startswith("emote:"): #this namespace is emotes
                                emotes.append(i[6:]) #add emote name to list
                        if len(emotes)>0: #if it even is an emote source
                            emote=emotes[0] #put emote source
                        if len(chares)>0: #if it even is an emote source
                            chare=", ".join(chares) #put emote source
                        links=metadata['metadata'][0]['known_urls']
                        global filelinks
                        global sites
                        global sites2
                        filelinks=''
                        sites=[]
                        sites2=[]
                        debug_log('(Friend) DEBUG: looking at links...')
                        gif=False
                        for i in links:
                            #filelinks=filelinks+', <'+i+'>'
                            if 'gif' in i: gif=True
                            if 'jpg' not in i and 'png' not in i and 'jpeg' not in i:
                                SiteHandle(i,'Pixiv','px')
                                SiteHandle(i,'Safebooru','sb')
                                SiteHandle(i,'Danbooru','db')
                                SiteHandle(i,'Gelbooru','gb')
                                SiteHandle(i,'Twitter','tw')
                                SiteHandle(i,'e621','e6')
                        filelinks=filelinks[2:]
                        
                        if len(artists)==0:
                            if 'tw' in sites:
                                twiturl=sites2[sites.index('tw')].split('/')
                                index2=0
                                for index in twiturl:
                                    if index=='twitter.com' and twiturl[index2+1]!='i': break
                                    index2+=1
                                debug_log('(Friend) DEBUG: '+str(twiturl))
                                debug_log('(Friend) DEBUG: '+str(index))
                                debug_log('(Friend) DEBUG: '+str(index2))
                                debug_log('(Friend) DEBUG: '+str(twiturl[index2+1]))
                                artist=str(twiturl[index2+1])
                        debug_log('(Friend) DEBUG: caching file...')
                        if gif:
                            with open("r:\\friend\\image"+str(friend_stack)+".gif", 'wb') as f: 
                                f.write(image.content) #saves file
                        else:
                            with open("r:\\friend\\image"+str(friend_stack)+".png", 'wb') as f: 
                                f.write(image.content) #saves file
                        debug_log('(Friend) DEBUG: checking size...')
                        size=friend_fatness(friend_stack)
                        #if True: artist+='.png'
                        if gif:
                            with open('r:\\friend\\image'+str(friend_stack)+'.gif', 'rb') as f:
                                f2 = discord.File(f, filename='image.gif')
                            desc='Known URLs: '+str(filelinks)+'\nHash: '+str(image_hash)
                            if emote: desc+='\nEmote: '+emote
                            if chare: desc+='\nCharacters: '+chare
                            embed=discord.Embed(title='Artist: '+artist, color=0x225588, description=desc)
                            #embed.set_image(url="attachment://"+str('image.gif'))
                            embed.set_footer(text="found "+str(len(results))+" results for "+search_term+" in "+str(req_time)+" seconds.")
                            debug_log('(Friend) DEBUG: uploading...')
                            await ctx.reply(file=f2, embed=embed)
                        else:
                            if size>2.0:
                                debug_log('(Friend) DEBUG: resizing >2MB image...')
                                image = Image.open("r:\\friend\\image"+str(friend_stack)+".png").convert('RGB')
                                size=image.size
                                ratio=image.size[0]/image.size[1]
                                newy=1000
                                newx=newy*ratio
                                image=image.resize((int(newx),int(newy)),resample=Image.BICUBIC)
                                image.save("r:\\friend\\image"+str(friend_stack)+".png")
                                size=friend_fatness(friend_stack)
                            else:
                                size=friend_fatness(friend_stack)
                            with open('r:\\friend\\image'+str(friend_stack)+'.png', 'rb') as f:
                                f2 = discord.File(f, filename='image.png')
                                desc='Known URLs: '+str(filelinks)+'\nHash: '+str(image_hash)
                                if emote: desc+='\nEmote: '+emote
                                if chare: desc+='\nCharacters: '+chare
                                embed=discord.Embed(title='Artist: '+artist, color=0x225588, description=desc)
                                #embed.set_image(url="attachment://"+str('image.png'))
                                embed.set_footer(text="found "+str(len(results))+" results for "+'balegdah'+" in "+str(69)+" seconds.")
                                debug_log('(Friend) DEBUG: uploading...')
                                await message.reply(embed=embed)
                    except IndexError:
                        await message.reply("No results. if this friend is absolutely necessary please tell ezogaming to download images of "+'balegdah'+" kthx")
                        debug_log('(Friend) ERROR: No Bitches')
                    except Exception as e:
                        eror=traceback.format_exc()
                        embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
                        embed.set_footer(text='lmao')
                        await message.reply(embed=embed)
                        debug_log('(Friend) ERROR: \n'+eror)


    @commands.command()
    async def friend(self, ctx: commands.Context, *friend):
        if 'tag:gartic' in friend and ctx.guild!=self.bot.get_guild(779136383033147403):
            await ctx.send('nice try')
        elif 'tag:sex' in friend:
            await ctx.send('https://cdn.discordapp.com/attachments/829216521959768065/849066547955499018/makesweet-5ot4tr.gif')
        else:
            try:
                if ctx.message.channel.id==self.bot.get_channel(443281312967688194).id:
                    await ctx.send("nosend zone detected")
                global friend_stack
                friend_stack+=1
                if friend_stack>15:
                    friend_stack=0
                global recents
                hydrusip="http://127.0.0.1:"+get_data("hydrus_port")
                headers={'Hydrus-Client-API-Access-Key': get_data("hydrus_key")}
                search_term=" ".join(friend[:])
                tagged=0
                query=0
                if search_term!="":
                    query=1
                if search_term[:4]=="tag:":
                    tagged=1
                kys=0
                if "tag:*" in search_term:
                    await ctx.send('balls itch')
                    query=0
                    tagged=0
                    kys=1
                debug_log('(Friend) DEBUG: brb looking for more '+search_term)
                synonyms=get_data("friend_tag_synonyms")
                for names in synonyms:
                    syn_count=-1
                    for name in names:
                        syn_count+=1
                    for i in range(syn_count):
                        search_term=search_term.replace(names[i+1],names[0])
                
                #i know jack about the scope im just brute forcing things at this point
                global tagshttp
                global tagshttp1
                global tagshttp2
                global tagshttp3
                
                nosend_tag=', "-nosend"' #exclude stuff that shouldnt be sent
                
                if ctx.message.channel.id==self.bot.get_channel(get_data("nosend_channel")).id:
                    nosend_tag='' #clear the nosend tag excluder if in the funny channel
                debug_log('(Friend) DEBUG: preparing query...')
                if query and kys==0:
                    if not tagged:
                        #Comic tag is too inclusive to be reliable for searches
                        tagshttp=urllib.parse.quote('["character:'+search_term+' (kemono friends)", "-comic"'+nosend_tag+']')
                        tagshttp2=urllib.parse.quote('["'+search_term.replace(" ", "_")+'_(kemono_friends)", "-comic"'+nosend_tag+']')
                        tagshttp3=urllib.parse.quote('["'+search_term+' (kemono friends)", "-comic"'+nosend_tag+']')
                    else:
                        tagshttp=urllib.parse.quote('["'+search_term[4:]+'", "-comic"'+nosend_tag+']')
                        tagshttp2=urllib.parse.quote('["'+search_term[4:].replace(" ", "_")+'", "-comic"'+nosend_tag+']')
                        tagshttp3=urllib.parse.quote('["DummyTagNeverUser9i8u98U", "-comic"'+nosend_tag+']')
                else:
                    tagshttp=urllib.parse.quote('["series:kemono friends", "-comic"'+nosend_tag+']') #find any KF image if no query or tag:x
                
                req_prefix=hydrusip+"/get_files/search_files?system_inbox=true&tags="
                debug_log('(Friend) DEBUG: searching...')
                start = time.time()
                request_1=requests.get(req_prefix+tagshttp, headers=headers)
                request_2=requests.get(req_prefix+tagshttp2, headers=headers)
                request_3=requests.get(req_prefix+tagshttp3, headers=headers)
                req_time=time.time() - start
                recieved_1=request_1.json()
                recieved_2=request_2.json()
                recieved_3=request_3.json()
                
                results=recieved_1['file_ids']+recieved_2['file_ids']+recieved_3['file_ids']
                results=list(set(results))
                
                try:
                    debug_log('(Friend) DEBUG: choosing image...')
                    result=random.choice(results)
                    tries=0
                    if result in recents:
                        while result in recents:
                            debug_log('(Friend) DEBUG: image already sent')
                            result=random.choice(results)
                            tries+=1
                            if tries>(len(results)*2):
                                debug_log('(Friend) DEBUG: too many tries')
                                break
                    recents.pop(0)
                    recents.append(result)
                    debug_log('(Friend) DEBUG: requesting image...')
                    image=requests.get(hydrusip+'/get_files/file?file_id='+str(result), headers=headers)
                    meta=requests.get(hydrusip+'/get_files/file_metadata?file_ids=%5B'+str(result)+'%5D', headers=headers)
                    metadata=meta.json()
                    chares=[]
                    tags1=[]
                    tags2=[]
                    sex=[]
                    sex2=[]
                    sex3=[]
                    debug_log('(Friend) DEBUG: Checking Tags...')
                    tags1=check_tags(metadata, 'my tags')
                    tags2=check_tags(metadata, 'new service')
                    tags=combine_tags(tags1, tags2)
                    try:
                        sex=metadata['metadata'][0]["service_keys_to_statuses_to_tags"]['5623f549415038b40cc7ac843f0b99a66ec0c18df4acc58ee40020a258fc9954']['1']
                    except KeyError:
                        pass#await ctx.send('big key balls')
                    try:
                        sex2=metadata['metadata'][0]["service_keys_to_statuses_to_tags"]['6c6f63616c2074616773']['0']
                    except KeyError:
                        pass#await ctx.send('small key balls')
                    sex3=combine_tags(sex,sex2)
                    tags=combine_tags(tags,sex3)
                    debug_log('(Friend) DEBUG: '+str(tags))
                    image_hash=metadata['metadata'][0]["hash"]
                    #try:
                    time1=None
                    try:
                        time1=metadata['metadata'][0]["time_modified"]
                        yayaya=dt.datetime.utcfromtimestamp(time1).strftime("%Y-%m-%d %H:%M")
                    except KeyError:
                        print('no date')
                    #time2=metadata["time_modified_details"]
                    #await ctx.send(str(time1))
                    #await ctx.send(str(time2))
                    #except KeyError:
                        #print(str(metadata))
                        #with open('i:\\die.json','w',encoding='utf-8') as f:
                            #json.dump(metadata,f)
                    with open('i:\\die.json','w',encoding='utf-8') as f:
                            json.dump(metadata,f)
                    artist="No Artist Tag" #default artist tag if none present
                    chare=None
                    title=None
                    emote=None #default artist tag if none present
                    request=[]
                    year=[]
                    artists=[] #initialize the list of artists incase there are multiple names
                    emotes=[]
                    request_=None
                    year_=None
                    for i in tags:
                        if i.startswith("creator:"): #this namespace is artists
                            artists.append(i[8:]) #add artist to list
                        if i.startswith("character:"): #this namespace is artists
                            chares.append(i[10:].replace(" (kemono friends)","")) #add artist to list
                        if i.startswith("year:"): #this namespace is artists
                            year.append(i[5:]) #add artist to list
                        if i.startswith("request:"): #this namespace is artists
                            request.append(i[8:]) #add artist to list 
                    if len(artists)>0: #if there are any artists
                        artist="/".join(artists) #add discriminator for different usernames
                    if len(year)>0: #if there are any artists
                        year_="/".join(year) #add discriminator for different usernames
                    if len(request)>0: #if there are any artists
                        request_="/".join(request) #add discriminator for different usernames
                    for i in tags:
                        if i.startswith("emote:"): #this namespace is emotes
                            emotes.append(i[6:]) #add emote name to list
                    for i in tags:
                        print(i)
                        if i.startswith("title:"): #this namespace is emotes
                            print('im ballin')
                            title=i[6:] #add emote name to list
                    if len(emotes)>0: #if it even is an emote source
                        emote=emotes[0] #put emote source
                    if len(chares)>0: #if it even is an emote source
                        chare=", ".join(chares) #put emote source
                    links=metadata['metadata'][0]['known_urls']
                    global filelinks
                    global sites
                    global sites2
                    filelinks=''
                    sites=[]
                    sites2=[]
                    debug_log('(Friend) DEBUG: looking at links...')
                    gif=False
                    vid=False
                    for i in links:
                        #filelinks=filelinks+', <'+i+'>'
                        print(i)
                        #await ctx.reply(i)
                        if 'gif' in i: 
                            gif=True
                            #await ctx.reply('wooo')
                        
                        for ext in ['mp4','mov','webm','mkv']:
                            if ext in i:
                                vid=True
                        if 'gif' in i: 
                            gif=True
                            #await ctx.reply('wooo')
                        if 'jpg' not in i and 'png' not in i and 'jpeg' not in i:
                            SiteHandle(i,'Pixiv','px')
                            SiteHandle(i,'Safebooru','sb')
                            SiteHandle(i,'Danbooru','db')
                            SiteHandle(i,'Gelbooru','gb')
                            SiteHandle(i,'Twitter','tw')
                            SiteHandle(i,'e621','e6')

                    filelinks=filelinks[2:]
                    
                    if len(artists)==0:
                        if 'tw' in sites:
                            twiturl=sites2[sites.index('tw')].split('/')
                            index2=0
                            for index in twiturl:
                                if index=='twitter.com' and twiturl[index2+1]!='i': break
                                index2+=1
                            debug_log('(Friend) DEBUG: '+str(twiturl))
                            debug_log('(Friend) DEBUG: '+str(index))
                            debug_log('(Friend) DEBUG: '+str(index2))
                            debug_log('(Friend) DEBUG: '+str(twiturl[index2+1]))
                            artist=str(twiturl[index2+1])
                    debug_log('(Friend) DEBUG: caching file...')
                    




                    if gif:
                        with open("r:\\friend\\image"+str(friend_stack)+".gif", 'wb') as f: 
                            f.write(image.content) #saves file
                    elif vid:
                        with open('R:\\inputfile.mkv', 'wb') as f:
                            f.write(image.content)
                        os.system('ffmpeg -i R:\\inputfile.mkv -lavfi "scale=256x256,fps=1,palettegen=max_colors=32:stats_mode=diff" R:\\palette.png -y')
                        os.system('ffmpeg -i R:\\inputfile.mkv -i R:\\palette.png -lavfi "fps=25,scale=-1:240,mpdecimate,paletteuse=dither=none" -fs 8M '+"r:\\friend\\image"+str(friend_stack)+".gif"+' -y')
                        gif=True
                    else:
                        with open("r:\\friend\\image"+str(friend_stack)+".png", 'wb') as f: 
                            f.write(image.content) #saves file
                    debug_log('(Friend) DEBUG: checking size...')
                    size=friend_fatness(friend_stack)
                    #if True: artist+='.png'
                    if gif:
                        #await ctx.reply('its a gif yup')
                        with open('r:\\friend\\image'+str(friend_stack)+'.gif', 'rb') as f:
                            f2 = discord.File(f, filename='image.gif')
                        desc='Known URLs: '+str(filelinks)+'\nHash: '+str(image_hash)
                        if emote: desc+='\nEmote: '+emote
                        if chare: desc+='\nCharacters: '+chare
                        if title: desc+='\nTitle: '+title
                        if request_: desc+='\nRequested by: '+request_
                        if time1: desc+='\nFile modified: '+str(yayaya)
                        if year_: desc+='\nYear: '+year_
                        embed=discord.Embed(title=('Artist: '+artist)[:252], color=0x225588, description=desc)
                        embed.set_image(url="attachment://"+str('image.gif'))
                        embed.set_footer(text="found "+str(len(results))+" results for "+search_term+" in "+str(req_time)+" seconds.")
                        debug_log('(Friend) DEBUG: uploading...')
                        await ctx.reply(file=f2, embed=embed)
                    else:
                        if size>2.0:
                            debug_log('(Friend) DEBUG: resizing >2MB image...')
                            image = Image.open("r:\\friend\\image"+str(friend_stack)+".png").convert('RGB')
                            size=image.size
                            ratio=image.size[0]/image.size[1]
                            newy=1000
                            newx=newy*ratio
                            image=image.resize((int(newx),int(newy)),resample=Image.BICUBIC)
                            image.save("r:\\friend\\image"+str(friend_stack)+".png")
                            size=friend_fatness(friend_stack)
                        else:
                            size=friend_fatness(friend_stack)
                        with open('r:\\friend\\image'+str(friend_stack)+'.png', 'rb') as f:
                            f2 = discord.File(f, filename='image.png')
                            desc='Known URLs: '+str(filelinks)+'\nHash: '+str(image_hash)
                            if emote: desc+='\nEmote: '+emote
                            if chare: desc+='\nCharacters: '+chare
                            if title: desc+='\nTitle: '+title
                            if request_: desc+='\nRequested by: '+request_
                            if time1: desc+='\nFile modified: '+str(yayaya)
                            if year_: desc+='\nYear: '+year_
                            embed=discord.Embed(title='Artist: '+artist, color=0x225588, description=desc)
                            embed.set_image(url="attachment://"+str('image.png'))
                            embed.set_footer(text="found "+str(len(results))+" results for "+search_term+" in "+str(req_time)+" seconds.")
                            debug_log('(Friend) DEBUG: uploading...')
                            await ctx.reply(file=f2, embed=embed)
                except IndexError:
                    await ctx.reply(get_lang('friend.nobitches').replace('%0',search_term))
                    debug_log('(Friend) ERROR: No Bitches')
                except Exception as e:
                    eror=traceback.format_exc()
                    embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
                    embed.set_footer(text='lmao')
                    await ctx.reply(embed=embed)
                    debug_log('(Friend) ERROR: \n'+eror)
            except Exception as e:
                eror=traceback.format_exc()
                embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
                embed.set_footer(text='lmao')
                await ctx.reply(embed=embed)
                debug_log('(Friend) ERROR: \n'+eror)

    @commands.command()
    async def panties(self, ctx: commands.Context, *friend):
        if 'tag:gartic' in friend and ctx.guild!=self.bot.get_guild(779136383033147403):
            await ctx.send('nice try')
        elif 'tag:sex' in friend:
            await ctx.send('https://cdn.discordapp.com/attachments/829216521959768065/849066547955499018/makesweet-5ot4tr.gif')
        else:
            try:
                if ctx.message.channel.id==self.bot.get_channel(443281312967688194).id:
                    await ctx.send("nosend zone detected")
                global friend_stack
                friend_stack+=1
                if friend_stack>15:
                    friend_stack=0
                global recents
                hydrusip="http://127.0.0.1:"+get_data("hydrus_port")
                headers={'Hydrus-Client-API-Access-Key': get_data("hydrus_key")}
                search_term=" ".join(friend[:])
                tagged=0
                query=0
                if search_term!="":
                    query=1
                if search_term[:4]=="tag:":
                    tagged=1
                debug_log('(Friend) DEBUG: brb looking for more '+search_term)
                synonyms=get_data("friend_tag_synonyms")
                for names in synonyms:
                    syn_count=-1
                    for name in names:
                        syn_count+=1
                    for i in range(syn_count):
                        search_term=search_term.replace(names[i+1],names[0])
                
                #i know jack about the scope im just brute forcing things at this point
                global tagshttp
                global tagshttp1
                global tagshttp2
                global tagshttp3
                
                nosend_tag=', "-nosend"' #exclude stuff that shouldnt be sent
                
                if ctx.message.channel.id==self.bot.get_channel(get_data("nosend_channel")).id:
                    nosend_tag='' #clear the nosend tag excluder if in the funny channel
                debug_log('(Friend) DEBUG: preparing query...')
                if query:
                    if not tagged:
                        #Comic tag is too inclusive to be reliable for searches
                        tagshttp=urllib.parse.quote('["character:'+search_term+' (kemono friends)", "panties", "-comic"'+nosend_tag+']')
                        tagshttp2=urllib.parse.quote('["'+search_term.replace(" ", "_")+'_(kemono_friends)", "panties", "-comic"'+nosend_tag+']')
                        tagshttp3=urllib.parse.quote('["'+search_term+' (kemono friends)", "panties", "-comic"'+nosend_tag+']')
                    else:
                        tagshttp=urllib.parse.quote('["'+search_term[4:]+'", "panties", "-comic"'+nosend_tag+']')
                        tagshttp2=urllib.parse.quote('["'+search_term[4:].replace(" ", "_")+'", "panties", "-comic"'+nosend_tag+']')
                        tagshttp3=urllib.parse.quote('["DummyTagNeverUser9i8u98U", "panties", "-comic"'+nosend_tag+']')
                else:
                    tagshttp=urllib.parse.quote('["series:kemono friends", "panties", "-comic"'+nosend_tag+']') #find any KF image if no query or tag:x
                    
                req_prefix=hydrusip+"/get_files/search_files?system_inbox=true&tags="
                debug_log('(Friend) DEBUG: searching...')
                start = time.time()
                request_1=requests.get(req_prefix+tagshttp, headers=headers)
                request_2=requests.get(req_prefix+tagshttp2, headers=headers)
                request_3=requests.get(req_prefix+tagshttp3, headers=headers)
                req_time=time.time() - start
                recieved_1=request_1.json()
                recieved_2=request_2.json()
                recieved_3=request_3.json()
                
                results=recieved_1['file_ids']+recieved_2['file_ids']+recieved_3['file_ids']
                results=list(set(results))
                
                try:
                    debug_log('(Friend) DEBUG: choosing image...')
                    result=random.choice(results)
                    tries=0
                    if result in recents:
                        while result in recents:
                            debug_log('(Friend) DEBUG: image already sent')
                            result=random.choice(results)
                            tries+=1
                            if tries>(len(results)*2):
                                debug_log('(Friend) DEBUG: too many tries')
                                break
                    recents.pop(0)
                    recents.append(result)
                    debug_log('(Friend) DEBUG: requesting image...')
                    image=requests.get(hydrusip+'/get_files/file?file_id='+str(result), headers=headers)
                    meta=requests.get(hydrusip+'/get_files/file_metadata?file_ids=%5B'+str(result)+'%5D', headers=headers)
                    metadata=meta.json()
                    chares=[]
                    tags1=[]
                    tags2=[]
                    debug_log('(Friend) DEBUG: Checking Tags...')
                    tags1=check_tags(metadata, 'my tags')
                    tags2=check_tags(metadata, 'new service')
                    tags=combine_tags(tags1, tags2)
                    debug_log('(Friend) DEBUG: '+str(tags))
                    image_hash=metadata['metadata'][0]["hash"]
                    artist="No Artist Tag" #default artist tag if none present
                    chare=None
                    title=None
                    emote=None #default artist tag if none present
                    artists=[] #initialize the list of artists incase there are multiple names
                    emotes=[]
                    for i in tags:
                        if i.startswith("creator:"): #this namespace is artists
                            artists.append(i[8:]) #add artist to list
                        if i.startswith("character:"): #this namespace is artists
                            chares.append(i[10:].replace(" (kemono friends)","")) #add artist to list
                    if len(artists)>0: #if there are any artists
                        artist="/".join(artists) #add discriminator for different usernames
                    for i in tags:
                        if i.startswith("emote:"): #this namespace is emotes
                            emotes.append(i[6:]) #add emote name to list
                    for i in tags:
                        print(i)
                        if i.startswith("title:"): #this namespace is emotes
                            print('im ballin')
                            title=i[6:] #add emote name to list
                    if len(emotes)>0: #if it even is an emote source
                        emote=emotes[0] #put emote source
                    if len(chares)>0: #if it even is an emote source
                        chare=", ".join(chares) #put emote source
                    links=metadata['metadata'][0]['known_urls']
                    global filelinks
                    global sites
                    global sites2
                    filelinks=''
                    sites=[]
                    sites2=[]
                    debug_log('(Friend) DEBUG: looking at links...')
                    gif=False
                    for i in links:
                        #filelinks=filelinks+', <'+i+'>'
                        print(i)
                        #await ctx.reply(i)
                        if 'gif' in i: 
                            gif=True
                            #await ctx.reply('wooo')
                        if 'jpg' not in i and 'png' not in i and 'jpeg' not in i:
                            SiteHandle(i,'Pixiv','px')
                            SiteHandle(i,'Safebooru','sb')
                            SiteHandle(i,'Danbooru','db')
                            SiteHandle(i,'Gelbooru','gb')
                            SiteHandle(i,'Twitter','tw')
                            SiteHandle(i,'e621','e6')
                    filelinks=filelinks[2:]
                    
                    if len(artists)==0:
                        if 'tw' in sites:
                            twiturl=sites2[sites.index('tw')].split('/')
                            index2=0
                            for index in twiturl:
                                if index=='twitter.com' and twiturl[index2+1]!='i': break
                                index2+=1
                            debug_log('(Friend) DEBUG: '+str(twiturl))
                            debug_log('(Friend) DEBUG: '+str(index))
                            debug_log('(Friend) DEBUG: '+str(index2))
                            debug_log('(Friend) DEBUG: '+str(twiturl[index2+1]))
                            artist=str(twiturl[index2+1])
                    debug_log('(Friend) DEBUG: caching file...')
                    if gif:
                        with open("r:\\friend\\image"+str(friend_stack)+".gif", 'wb') as f: 
                            f.write(image.content) #saves file
                    else:
                        with open("r:\\friend\\image"+str(friend_stack)+".png", 'wb') as f: 
                            f.write(image.content) #saves file
                    debug_log('(Friend) DEBUG: checking size...')
                    size=friend_fatness(friend_stack)
                    #if True: artist+='.png'
                    if gif:
                        #await ctx.reply('its a gif yup')
                        with open('r:\\friend\\image'+str(friend_stack)+'.gif', 'rb') as f:
                            f2 = discord.File(f, filename='image.gif')
                        desc='Known URLs: '+str(filelinks)+'\nHash: '+str(image_hash)
                        if emote: desc+='\nEmote: '+emote
                        if chare: desc+='\nCharacters: '+chare
                        if title: desc+='\nTitle: '+title
                        embed=discord.Embed(title='Artist: '+artist, color=0x225588, description=desc)
                        embed.set_image(url="attachment://"+str('image.gif'))
                        embed.set_footer(text="found "+str(len(results))+" results for "+search_term+" in "+str(req_time)+" seconds.")
                        debug_log('(Friend) DEBUG: uploading...')
                        await ctx.reply(file=f2, embed=embed)
                    else:
                        if size>2.0:
                            debug_log('(Friend) DEBUG: resizing >2MB image...')
                            image = Image.open("r:\\friend\\image"+str(friend_stack)+".png").convert('RGB')
                            size=image.size
                            ratio=image.size[0]/image.size[1]
                            newy=1000
                            newx=newy*ratio
                            image=image.resize((int(newx),int(newy)),resample=Image.BICUBIC)
                            image.save("r:\\friend\\image"+str(friend_stack)+".png")
                            size=friend_fatness(friend_stack)
                        else:
                            size=friend_fatness(friend_stack)
                        with open('r:\\friend\\image'+str(friend_stack)+'.png', 'rb') as f:
                            f2 = discord.File(f, filename='image.png')
                            desc='Known URLs: '+str(filelinks)+'\nHash: '+str(image_hash)
                            if emote: desc+='\nEmote: '+emote
                            if chare: desc+='\nCharacters: '+chare
                            if title: desc+='\nTitle: '+title
                            embed=discord.Embed(title='Artist: '+artist, color=0x225588, description=desc)
                            embed.set_image(url="attachment://"+str('image.png'))
                            embed.set_footer(text="found "+str(len(results))+" results for "+search_term+" in "+str(req_time)+" seconds.")
                            debug_log('(Friend) DEBUG: uploading...')
                            await ctx.reply(file=f2, embed=embed)
                except IndexError:
                    await ctx.reply(get_lang('friend.nobitches').replace('%0',search_term))
                    debug_log('(Friend) ERROR: No Bitches')
                except Exception as e:
                    eror=traceback.format_exc()
                    embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
                    embed.set_footer(text='lmao')
                    await ctx.reply(embed=embed)
                    debug_log('(Friend) ERROR: \n'+eror)
            except Exception as e:
                eror=traceback.format_exc()
                embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
                embed.set_footer(text='lmao')
                await ctx.reply(embed=embed)
                debug_log('(Friend) ERROR: \n'+eror)

    @commands.command()
    async def boobfriend(self, ctx: commands.Context, *friend):
        try:
            if ctx.message.channel.id==self.bot.get_channel(443281312967688194).id:
                await ctx.send("nosend zone detected")
            global friend_stack
            friend_stack+=1
            if friend_stack>15:
                friend_stack=0
            global recents
            hydrusip="http://127.0.0.1:"+get_data("hydrus_port")
            headers={'Hydrus-Client-API-Access-Key': get_data("hydrus_key")}
            search_term=" ".join(friend[:])
            tagged=0
            query=0
            if search_term!="":
                query=1
            if search_term[:4]=="tag:":
                tagged=1
            debug_log('(Friend) DEBUG: brb looking for more '+search_term)
            synonyms=get_data("friend_tag_synonyms")
            for names in synonyms:
                syn_count=-1
                for name in names:
                    syn_count+=1
                for i in range(syn_count):
                    search_term=search_term.replace(names[i+1],names[0])
            
            #i know jack about the scope im just brute forcing things at this point
            global tagshttp
            global tagshttp1
            global tagshttp2
            global tagshttp3
            
            nosend_tag=', "-nosend"' #exclude stuff that shouldnt be sent
            
            if ctx.message.channel.id==self.bot.get_channel(get_data("nosend_channel")).id:
                nosend_tag='' #clear the nosend tag excluder if in the funny channel
            debug_log('(Friend) DEBUG: preparing query...')
            if query:
                if not tagged:
                    #Comic tag is too inclusive to be reliable for searches
                    tagshttp=urllib.parse.quote('["character:'+search_term+' (kemono friends)", "-comic"'+nosend_tag+', "booba"]')
                    tagshttp2=urllib.parse.quote('["'+search_term.replace(" ", "_")+'_(kemono_friends)", "-comic"'+nosend_tag+', "booba"]')
                    tagshttp3=urllib.parse.quote('["'+search_term+' (kemono friends)", "-comic"'+nosend_tag+', "booba"]')
                else:
                    tagshttp=urllib.parse.quote('["'+search_term[4:]+'", "-comic"'+nosend_tag+', "booba"]')
                    tagshttp2=urllib.parse.quote('["'+search_term[4:].replace(" ", "_")+'", "-comic"'+nosend_tag+', "booba"]')
                    tagshttp3=urllib.parse.quote('["DummyTagNeverUser9i8u98U", "-comic"'+nosend_tag+', "booba"]')
            else:
                tagshttp=urllib.parse.quote('["series:kemono friends", "-comic"'+nosend_tag+', "booba"]') #find any KF image if no query or tag:x
                
            req_prefix=hydrusip+"/get_files/search_files?system_inbox=true&tags="
            debug_log('(Friend) DEBUG: searching...')
            start = time.time()
            request_1=requests.get(req_prefix+tagshttp, headers=headers)
            request_2=requests.get(req_prefix+tagshttp2, headers=headers)
            request_3=requests.get(req_prefix+tagshttp3, headers=headers)
            req_time=time.time() - start
            recieved_1=request_1.json()
            recieved_2=request_2.json()
            recieved_3=request_3.json()
            
            results=recieved_1['file_ids']+recieved_2['file_ids']+recieved_3['file_ids']
            results=list(set(results))
            
            try:
                debug_log('(Friend) DEBUG: choosing image...')
                result=random.choice(results)
                tries=0
                if result in recents:
                    while result in recents:
                        debug_log('(Friend) DEBUG: image already sent')
                        result=random.choice(results)
                        tries+=1
                        if tries>(len(results)*2):
                            debug_log('(Friend) DEBUG: too many tries')
                            break
                recents.pop(0)
                recents.append(result)
                debug_log('(Friend) DEBUG: requesting image...')
                image=requests.get(hydrusip+'/get_files/file?file_id='+str(result), headers=headers)
                meta=requests.get(hydrusip+'/get_files/file_metadata?file_ids=%5B'+str(result)+'%5D', headers=headers)
                metadata=meta.json()
                chares=[]
                tags1=[]
                tags2=[]
                debug_log('(Friend) DEBUG: Checking Tags...')
                tags1=check_tags(metadata, 'my tags')
                tags2=check_tags(metadata, 'new service')
                tags=combine_tags(tags1, tags2)
                debug_log('(Friend) DEBUG: '+str(tags))
                image_hash=metadata['metadata'][0]["hash"]
                artist="No Artist Tag" #default artist tag if none present
                chare=None
                emote=None #default artist tag if none present
                artists=[] #initialize the list of artists incase there are multiple names
                emotes=[]
                for i in tags:
                    if i.startswith("creator:"): #this namespace is artists
                        artists.append(i[8:]) #add artist to list
                    if i.startswith("character:"): #this namespace is artists
                        chares.append(i[10:].replace(" (kemono friends)","")) #add artist to list
                if len(artists)>0: #if there are any artists
                    artist="/".join(artists) #add discriminator for different usernames
                for i in tags:
                    if i.startswith("emote:"): #this namespace is emotes
                        emotes.append(i[6:]) #add emote name to list
                if len(emotes)>0: #if it even is an emote source
                    emote=emotes[0] #put emote source
                if len(chares)>0: #if it even is an emote source
                    chare=", ".join(chares) #put emote source
                links=metadata['metadata'][0]['known_urls']
                global filelinks
                global sites
                global sites2
                filelinks=''
                sites=[]
                sites2=[]
                debug_log('(Friend) DEBUG: looking at links...')
                for i in links:
                    #filelinks=filelinks+', <'+i+'>'
                    if 'jpg' not in i and 'png' not in i and 'jpeg' not in i:
                        SiteHandle(i,'Pixiv','px')
                        SiteHandle(i,'Safebooru','sb')
                        SiteHandle(i,'Danbooru','db')
                        SiteHandle(i,'Gelbooru','gb')
                        SiteHandle(i,'Twitter','tw')
                        SiteHandle(i,'e621','e6')
                filelinks=filelinks[2:]
                if len(artists)==0:
                    if 'tw' in sites:
                        twiturl=sites2[sites.index('tw')].split('/')
                        index2=0
                        for index in twiturl:
                            if index=='twitter.com' and twiturl[index2+1]!='i': break
                            index2+=1
                        debug_log('(Friend) DEBUG: '+str(twiturl))
                        debug_log('(Friend) DEBUG: '+str(index))
                        debug_log('(Friend) DEBUG: '+str(index2))
                        debug_log('(Friend) DEBUG: '+str(twiturl[index2+1]))
                        artist=str(twiturl[index2+1])
                debug_log('(Friend) DEBUG: caching file...')
                with open("r:\\friend\\image"+str(friend_stack)+".png", 'wb') as f: 
                    f.write(image.content) #saves file
                debug_log('(Friend) DEBUG: checking size...')
                size=friend_fatness(friend_stack)
                #if True: artist+='.png'
                if size>2.0:
                    debug_log('(Friend) DEBUG: resizing >2MB image...')
                    image = Image.open("r:\\friend\\image"+str(friend_stack)+".png").convert('RGB')
                    size=image.size
                    ratio=image.size[0]/image.size[1]
                    newy=1000
                    newx=newy*ratio
                    image=image.resize((int(newx),int(newy)),resample=Image.BICUBIC)
                    image.save("r:\\friend\\image"+str(friend_stack)+".png")
                    size=friend_fatness(friend_stack)
                else:
                    size=friend_fatness(friend_stack)
                with open('r:\\friend\\image'+str(friend_stack)+'.png', 'rb') as f:
                    f2 = discord.File(f, filename='image.png')
                    desc='Known URLs: '+str(filelinks)+'\nHash: '+str(image_hash)
                    if emote: desc+='\nEmote: '+emote
                    if chare: desc+='\nCharacters: '+chare
                    embed=discord.Embed(title='Artist: '+artist, color=0x225588, description=desc)
                    embed.set_image(url="attachment://"+str('image.png'))
                    embed.set_footer(text="found "+str(len(results))+" results for "+search_term+" in "+str(req_time)+" seconds.")
                    debug_log('(Friend) DEBUG: uploading...')
                    await ctx.reply(file=f2, embed=embed)
            except IndexError:
                await ctx.reply("No results. if this friend is absolutely necessary please tell ezogaming to download images of "+search_term+" kthx")
                debug_log('(Friend) ERROR: No Bitches')
            except Exception as e:
                eror=traceback.format_exc()
                embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
                embed.set_footer(text='lmao')
                await ctx.reply(embed=embed)
                debug_log('(Friend) ERROR: \n'+eror)
        except Exception as e:
            eror=traceback.format_exc()
            embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
            embed.set_footer(text='lmao')
            await ctx.reply(embed=embed)
            debug_log('(Friend) ERROR: \n'+eror)

    @commands.command()
    async def r63(self, ctx: commands.Context, *friend):
        try:
            if ctx.message.channel.id==self.bot.get_channel(443281312967688194).id:
                await ctx.send("nosend zone detected")
            global friend_stack
            friend_stack+=1
            if friend_stack>15:
                friend_stack=0
            global recents
            hydrusip="http://127.0.0.1:"+get_data("hydrus_port")
            headers={'Hydrus-Client-API-Access-Key': get_data("hydrus_key")}
            search_term=" ".join(friend[:])
            tagged=0
            query=0
            if search_term!="":
                query=1
            if search_term[:4]=="tag:":
                tagged=1
            debug_log('(Friend) DEBUG: brb looking for more '+search_term)
            synonyms=get_data("friend_tag_synonyms")
            for names in synonyms:
                syn_count=-1
                for name in names:
                    syn_count+=1
                for i in range(syn_count):
                    search_term=search_term.replace(names[i+1],names[0])
            
            #i know jack about the scope im just brute forcing things at this point
            global tagshttp
            global tagshttp1
            global tagshttp2
            global tagshttp3
            
            nosend_tag=', "-nosend"' #exclude stuff that shouldnt be sent
            
            if ctx.message.channel.id==self.bot.get_channel(get_data("nosend_channel")).id:
                nosend_tag='' #clear the nosend tag excluder if in the funny channel
            debug_log('(Friend) DEBUG: preparing query...')
            quer=4
            if query:
                quer=4
                if not tagged:
                    tagshttp=urllib.parse.quote('["character:'+search_term+' (kemono friends)", "-comic"'+nosend_tag+', "genderswap (ftm)"]')
                else:
                    tagshttp=urllib.parse.quote('["'+search_term[4:]+'", "-comic"'+nosend_tag+', "genderswap (ftm)"]')
            else:
                quer=2
                tagshttp=urllib.parse.quote('["series:kemono friends", "-comic"'+nosend_tag+', "genderswap (ftm)"]') #find any KF image if no query or tag:x
                
            req_prefix=hydrusip+"/get_files/search_files?system_inbox=true&tags="
            debug_log('(Friend) DEBUG: searching...')
            start = time.time()
            request_1=requests.get(req_prefix+tagshttp, headers=headers)
            req_time=time.time() - start
            recieved_1=request_1.json()
            
            results=recieved_1['file_ids']
            results=list(set(results))
            
            try:
                debug_log('(Friend) DEBUG: choosing image...')
                result=random.choice(results)
                tries=0
                if result in recents:
                    while result in recents:
                        debug_log('(Friend) DEBUG: image already sent')
                        result=random.choice(results)
                        tries+=1
                        if tries>(len(results)*2):
                            debug_log('(Friend) DEBUG: too many tries')
                            break
                recents.pop(0)
                recents.append(result)
                debug_log('(Friend) DEBUG: requesting image...')
                image=requests.get(hydrusip+'/get_files/file?file_id='+str(result), headers=headers)
                meta=requests.get(hydrusip+'/get_files/file_metadata?file_ids=%5B'+str(result)+'%5D', headers=headers)
                metadata=meta.json()
                chares=[]
                tags1=[]
                tags2=[]
                debug_log('(Friend) DEBUG: Checking Tags...')
                tags1=check_tags(metadata, 'my tags')
                tags2=check_tags(metadata, 'new service')
                tags=combine_tags(tags1, tags2)
                debug_log('(Friend) DEBUG: '+str(tags))
                image_hash=metadata['metadata'][0]["hash"]
                artist="No Artist Tag" #default artist tag if none present
                chare=None
                emote=None #default artist tag if none present
                artists=[] #initialize the list of artists incase there are multiple names
                emotes=[]
                for i in tags:
                    if i.startswith("creator:"): #this namespace is artists
                        artists.append(i[8:]) #add artist to list
                    if i.startswith("character:"): #this namespace is artists
                        chares.append(i[10:].replace(" (kemono friends)","")) #add artist to list
                if len(artists)>0: #if there are any artists
                    artist="/".join(artists) #add discriminator for different usernames
                for i in tags:
                    if i.startswith("emote:"): #this namespace is emotes
                        emotes.append(i[6:]) #add emote name to list
                if len(emotes)>0: #if it even is an emote source
                    emote=emotes[0] #put emote source
                if len(chares)>0: #if it even is an emote source
                    chare=", ".join(chares) #put emote source
                links=metadata['metadata'][0]['known_urls']
                global filelinks
                global sites
                global sites2
                filelinks=''
                sites=[]
                sites2=[]
                debug_log('(Friend) DEBUG: looking at links...')
                for i in links:
                    #filelinks=filelinks+', <'+i+'>'
                    if 'jpg' not in i and 'png' not in i and 'jpeg' not in i:
                        SiteHandle(i,'Pixiv','px')
                        SiteHandle(i,'Safebooru','sb')
                        SiteHandle(i,'Danbooru','db')
                        SiteHandle(i,'Gelbooru','gb')
                        SiteHandle(i,'Twitter','tw')
                        SiteHandle(i,'e621','e6')
                filelinks=filelinks[2:]
                if len(artists)==0:
                    if 'tw' in sites:
                        twiturl=sites2[sites.index('tw')].split('/')
                        index2=0
                        for index in twiturl:
                            if index=='twitter.com' and twiturl[index2+1]!='i': break
                            index2+=1
                        debug_log('(Friend) DEBUG: '+str(twiturl))
                        debug_log('(Friend) DEBUG: '+str(index))
                        debug_log('(Friend) DEBUG: '+str(index2))
                        debug_log('(Friend) DEBUG: '+str(twiturl[index2+1]))
                        artist=str(twiturl[index2+1])
                debug_log('(Friend) DEBUG: caching file...')
                with open("r:\\friend\\image"+str(friend_stack)+".png", 'wb') as f: 
                    f.write(image.content) #saves file
                debug_log('(Friend) DEBUG: checking size...')
                size=friend_fatness(friend_stack)
                #if True: artist+='.png'
                if size>2.0:
                    debug_log('(Friend) DEBUG: resizing >2MB image...')
                    image = Image.open("r:\\friend\\image"+str(friend_stack)+".png").convert('RGB')
                    size=image.size
                    ratio=image.size[0]/image.size[1]
                    newy=1000
                    newx=newy*ratio
                    image=image.resize((int(newx),int(newy)),resample=Image.BICUBIC)
                    image.save("r:\\friend\\image"+str(friend_stack)+".png")
                    size=friend_fatness(friend_stack)
                else:
                    size=friend_fatness(friend_stack)
                with open('r:\\friend\\image'+str(friend_stack)+'.png', 'rb') as f:
                    f2 = discord.File(f, filename='image.png')
                    desc='Known URLs: '+str(filelinks)+'\nHash: '+str(image_hash)
                    if emote: desc+='\nEmote: '+emote
                    if chare: desc+='\nCharacters: '+chare
                    embed=discord.Embed(title='Artist: '+artist, color=0x225588, description=desc)
                    embed.set_image(url="attachment://"+str('image.png'))
                    embed.set_footer(text="found "+str(len(results))+" results for "+search_term+" in "+str(req_time)+" seconds.")
                    debug_log('(Friend) DEBUG: uploading...')
                    await ctx.reply(file=f2, embed=embed)
            except IndexError:
                await ctx.reply(get_lang('friend.nobitches').replace('%0',search_term))
                debug_log('(Friend) ERROR: No Bitches')
            except Exception as e:
                eror=traceback.format_exc()
                embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
                embed.set_footer(text='lmao')
                await ctx.reply(embed=embed)
                debug_log('(Friend) ERROR: \n'+eror)
        except Exception as e:
            eror=traceback.format_exc()
            embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
            embed.set_footer(text='lmao')
            await ctx.reply(embed=embed)
            debug_log('(Friend) ERROR: \n'+eror)



def setup(bot: commands.Bot):
    bot.add_cog(FriendCommands(bot))