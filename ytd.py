from silverutil import get_token
import math
import discord
from discord.utils import get
import re
from discord.ext import commands, tasks
from discord import File
import datetime
import time
import random
import os
import json
import requests
import asyncio
import ffmpy
import subprocess
import urllib
import av
from json import loads
from PIL import Image, ImageOps
from silverutil import wtitle





def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)
    
def youtubeSearch(url):
    #print(url)
    txt = ""
    counter = 0
    #print(txt)
    while "ytInitialData" not in txt:
        #print(txt)
        txt = requests.get(f"https://www.youtube.com/results?search_query="+url).text
        if counter > 5:
            #fixPrint(f'Found no results for query '+url+'. Error:', e)
            return 'couldnt find a result'
        counter += 1
    try:
        #print('____')
        #print(txt)
        txt = txt[(start := txt.index("{", start := (txt.index(term := "ytInitialData") + len(term)))): txt.index("};", start) + 1]
        #print(txt)
        t = loads(txt)["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]
        #print(t)
    except Exception as e:
        #fixPrint(f'Error searching for query {url}. Error:', e)
        #print('____')
        #print(e)
        if e=="sectionListRenderer":
            #print('____')
            #print(txt)
            txt = txt[(start := txt.index("{", start := (txt.index(term := "ytInitialData") + len(term)))): txt.index("};", start) + 1]
            #print(txt)
            t = loads(txt)["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]
            #print(t)
        else:
            return 'weird error 2'
    for i in t:
        if next(iter(i)) == "videoRenderer":
            return f"https://youtube.com/watch?v={i['videoRenderer']['videoId']}"
    try:
        return 'weird error in youtube search function.\nvariables:\ni: '+str(i)+'\nt:'+str(t)+'\ntxt:'+str(txt)+'\ncounter:'+str(counter)+'\nlen of t:'+str(len(t))
    except:
        return 'weird error handling weird error'

wtitle("yt-dlp")
intents = discord.Intents(messages=True, guilds=True).all()
print(intents)
intents.message_content = True
print(intents)
bot = commands.Bot(help_command=None,command_prefix=['f'],intents=discord.Intents.all())
client=discord.Client(intents=intents)

def buildEmbed(desc,dr_,vb_,ab_,br_,sz_, id_):
    embed=discord.Embed(title="fdownload (Job ID: "+str(id_)+")",description=desc)
    embed.add_field(name="Target size", value=str(sz_*1024)+'K', inline=True)
    embed.add_field(name="Duration", value=str(dr_), inline=True)
    embed.add_field(name="Bitrate", value=str(vb_)+"k video\n"+str(ab_)+"k audio", inline=True)
    embed.add_field(name="Bitrate ratio", value=str(br_*100)+"% Video", inline=True)
    print(embed)
    return embed



def gettenor(url=''):
    # set the apikey and limit
    apikey = "8FMRE051ZV31"  # test value

    # our gif id
    gifid = url[url.rindex('-')+1:]
    print(gifid)

    # get the specific gif
    r = requests.get(
        "https://api.tenor.com/v1/gifs?ids=%s&key=%s&media_filter=minimal" % (gifid, apikey))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        gifs = json.loads(r.content)
        print(gifs)
    else:
        gifs = None
    return gifs

@bot.command()
async def download(ctx, *url_):
    fs_limit=ctx.guild.filesize_limit
    fs_limit=fs_limit/1000000
    fs_limit=fs_limit/1.07546256
    fs_limit=int(fs_limit*10)/10
    fs_limit=fs_limit-1
    print(fs_limit)
    job_id=int(str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)))
    args=" ".join(url_)
    print(args)
    args=args.split('--')
    print(args)
    scc=0
    if 'tenor' in args[0]:
        print('tenor detected')
        url=gettenor(url=args[0])['results'][0]['media'][0]['mp4']['url']
        print(url)
    else:
        if url_[0].startswith('http'):
            url=url_[0]
        else:
            scc=1
            print(args[0])
            url=youtubeSearch(args[0])
            if url=='couldnt find a result':
                await ctx.send(url)
                return
            if 'weird error' in url:
                await ctx.send(url)
                return
            if url=='weird error 2':
                await ctx.send(url)
                return
    verbose=True
    targetsize=fs_limit
    ratio=0.67
    mp3=False
    duration=0
    ss=False
    full=0
    if fs_limit>9: full=1
    encode=1
    res=1
    if 'tenor' not in args[0]:   
        for arg_ in args:
            arg=arg_.split(" ")
            print(arg)
            
            if arg[0] in ["verbose","v"]:
                verbose=True
                print("found verb")
            if arg[0] in ["size","target-size","s"]:
                targetsize=float(arg[1])
                print("found sz"+str(arg[1]))
            if arg[0] in ["ratio","r"]:
                ratio=float(arg[1])
                print("found rat"+str(arg[1]))
            if arg[0] in ["mp3","m"]:
                mp3=True
                full=1
                print("found mp3")
            if arg[0] in ["sponsorskip","nordvpn","ss"]:
                ss=True
                print("found ss")
            if arg[0] in ["full"]:
                full=1
            if arg[0] in ["maxres"]:
                res=0
            if arg[0] in ["original","skip-encode"]:
                encode=0
        if verbose:
            embed=discord.Embed(title="fdownload (Job ID: "+str(job_id)+")",description="downloading video...")
            sent_message = await ctx.reply(embed=embed)
        updateFile(0, "YouTube-DL: downloading video... "+str(datetime.now())+"\n")
        cmd='h:\\butthead\\yt-dlp '+url+' '+('--format-sort res:480'*res)+' -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4 --merge-output-format mp4 -o file'+str(job_id)+'.mp4 --force-overwrites --write-info-json -o infojson:file'+str(job_id)+'.json'
        cmd+=' --youtube-skip-dash-manifest --external-downloader c:\\aria2c.exe --external-downloader-args "-x 16 -s 16 -k 1M"'
        if ss: cmd+=' --sponsorblock-remove all'
        if mp3:
            #cmd='h:\\butthead\\yt-dlp '+url+'  -x --audio-format mp3 -o file'+str(job_id)+'.mp3 --force-overwrites'
            cmd='h:\\butthead\\yt-dlp '+url+'  -x --audio-format mp3 -o file'+str(job_id)+'.mp3 --force-overwrites --add-metadata --write-info-json -o infojson:file'+str(job_id)+'.json'
            cmd+=' --youtube-skip-dash-manifest --external-downloader c:\\aria2c.exe --external-downloader-args "-x 16 -s 16 -k 1M"'
        subprocess.check_call(cmd, shell=True)
        if verbose:
            embed=discord.Embed(title="fdownload (Job ID: "+str(job_id)+")",description="downloaded")
            await sent_message.edit(embed=embed)
        size=1
        if not mp3: size=os.path.getsize('file'+str(job_id)+'.mp4')/1000000 #size of image in MB
        fn='file'+str(job_id)+'.mp4'
        if not full: fn='file'+str(job_id)+'_cut.mp4'
        if not full: subprocess.check_call('ffmpeg -i file'+str(job_id)+'.mp4 -to 00:01:30 -c copy file'+str(job_id)+'_cut.mp4', shell=True)
        vrate=0
        arate=0
        if verbose:
            embed=buildEmbed(desc="downloaded",dr_=duration,vb_="N/A",ab_="N/A",br_=ratio,sz_=targetsize, id_=job_id)
            await sent_message.edit(embed=embed)
            embed=buildEmbed(desc="uploading...",dr_=duration,vb_=0,ab_=0,br_=0,sz_=0, id_=job_id)
        if size>targetsize and not mp3:
            fn='file'+str(job_id)+'_new.mp4'
            if not full: fn='file'+str(job_id)+'_cut_new.mp4'
            duration=get_length('file'+str(job_id)+'.mp4')
            if not full: duration=get_length('file'+str(job_id)+'_cut.mp4')
            print(duration)
            totalrate=(targetsize * 8192.0) / (1.048576*duration)
            vrate=totalrate*ratio
            if vrate<4:
                vrate=4
            arate=totalrate-vrate
            if arate<1:
                arate=1
            print(vrate)
            print(arate)
            if verbose: embed=buildEmbed(desc="encoding (pass 1)...",dr_=duration,vb_=round(vrate),ab_=round(arate),br_=ratio,sz_=targetsize, id_=job_id)
            if verbose: await sent_message.edit(embed=embed)
            updateFile(0, "YouTube-DL: encoding (pass 1)... "+str(datetime.now())+"\n")
            if full:
                os.system('ffmpeg -i file'+str(job_id)+'.mp4 -c:v h264_nvenc -b:v '+str(math.floor(vrate))+'k -vf scale=-2:360  -to 00:30:00 -pass 1 -an -f mp4 NUL -y')
            else:
                os.system('ffmpeg -i file'+str(job_id)+'_cut.mp4 -c:v h264_nvenc -b:v '+str(math.floor(vrate))+'k -vf scale=-2:360 -to 00:30:00 -pass 1 -an -f mp4 NUL -y')
            if verbose: embed=buildEmbed(desc="encoding (pass 2)...",dr_=duration,vb_=round(vrate),ab_=round(arate),br_=ratio,sz_=targetsize, id_=job_id)
            if verbose: await sent_message.edit(embed=embed)
            updateFile(0, "YouTube-DL: encoding (pass 2)... "+str(datetime.now())+"\n")
            if full:
                os.system('ffmpeg -i file'+str(job_id)+'.mp4 -c:v h264_nvenc -b:v '+str(math.floor(vrate))+'k -pass 2 -c:a aac -b:a '+str(math.floor(arate))+'k -fs '+str(targetsize)+'M -vf scale=-2:360  -to 00:30:00  file'+str(job_id)+'_new.mp4 -y')
            else:
                os.system('ffmpeg -i file'+str(job_id)+'_cut.mp4 -c:v h264_nvenc -b:v '+str(math.floor(vrate))+'k -pass 2 -c:a aac -b:a '+str(math.floor(arate))+'k -fs '+str(targetsize)+'M -vf scale=-2:360  -to 00:30:00file'+str(job_id)+'_cut_new.mp4 -y')
            if verbose: embed=buildEmbed(desc="uploading...",dr_=duration,vb_=round(vrate),ab_=round(arate),br_=ratio,sz_=targetsize, id_=job_id)	
        if verbose: await sent_message.edit(embed=embed)
        if mp3: fn='file'+str(job_id)+'.mp3'
        choices = ["h", "Here ya go", "Is this one as bad as the last one?", "هي لعبة الكترونية", "That moment when", "New punjabi movies 2014 full movie free download hd 1080p", "Yo mama moment","your autism, madam"]
        if mp3: os.system('ffmpeg -i file'+str(job_id)+'.mp3 -to 1800 -fs 7.8M file'+str(job_id)+'_mp3.mp3 -y')
        if mp3: fn='file'+str(job_id)+'_mp3.mp3'
        print(mp3)
        with open(fn, 'rb') as f:
            if mp3:
                #if not scc: await ctx.reply(file=File(f, 'audio'+str(job_id)+'.mp3')) #send the funny
                #if scc: await ctx.reply(file=File(f, args[0].replace(' ','_').replace('"','_')+'.mp3')) #send the funny
                with open('file'+str(job_id)+'.json.info.json', 'r',encoding='utf-8') as f2:
                    dataJson = json.load(f2)
                #@print(dataJson)
                nameFromJson=dataJson["title"]
                await ctx.reply(file=File(f, nameFromJson.replace(' ','_').replace('"','_')+'.mp3')) #send the funny
            else:
                with open('file'+str(job_id)+'.json.info.json', 'r',encoding='utf-8') as f2:
                    dataJson = json.load(f2)
                nameFromJson=dataJson["title"]
                await ctx.reply(file=File(f, nameFromJson.replace(' ','_').replace('"','_')+'.mp4'))
                #if scc: await ctx.reply(file=File(f, args[0].replace(' ','_').replace('"','_')+'.mp4'))
                #if not scc: await ctx.reply(file=File(f, 'video'+str(job_id)+'.mp4')) #send the funny
    else:
        gaga=requests.get(url)
        with open('tenor.mp4', 'wb') as f: 
            f.write(gaga.content) #saves file
        with open('tenor.mp4', 'rb') as f:
            await ctx.reply(file=File(f, 'tenor.mp4'))
    



        
        
        
from datetime import datetime
@client.event
async def start_status():
    print("ready")
    statuses2=[""]*8
    while 1:
        statuses2=[""]*8
        with open('status.txt','r+') as statusFile:
            statuses2=[""]*8
            statuses=statusFile.readlines()
            statuses2[0]="YouTube-DL: "+str(datetime.now())+"\n"
            statuses2[1]=statuses[1]
            statuses2[2]=statuses[2]
            statuses2[3]=statuses[3]
            statuses2[4]=statuses[4]
            statuses2[5]=statuses[5]
            statuses2[6]=statuses[6]
            statusFile.seek(0)
            statusFile.writelines(statuses2)
        print("written")
        await asyncio.sleep(1)
        
def updateFile(line, shit):
    statuses2=[""]*8
    with open('status.txt','r+') as statusFile:
        statuses2=[""]*8
        statuses=statusFile.readlines()
        statuses2[0]=shit
        statuses2[1]=statuses[1]
        statuses2[2]=statuses[2]
        statuses2[3]=statuses[3]
        statuses2[4]=statuses[4]
        statuses2[5]=statuses[5]
        statuses2[6]=statuses[6]
        statusFile.seek(0)
        statusFile.writelines(statuses2)
    print("written "+shit+" to line "+str(line))
        
token=get_token()
#bot.loop.create_task(start_status())
print('gorbon')
bot.run('MzAzMjMxNzI4MjEyOTAxODkx.WPO0jQ.Z7MZAilHQphOo-yp7LL9n8pQ6_8')