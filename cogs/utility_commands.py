import urllib
global stammerqueue
stammerqueue=[]
import unicodedata
import geopy
from geopy import distance
from math import sin, cos, sqrt, atan2, radians
import discord
from grpc import FutureCancelledError
import speedtest
from lyricsgenius import Genius
from discord.ext import commands
from .silverutil import get_data, generateUUID, get_lang
import datetime
from typing import Optional
import html2text
from discord import ActionRow, Button, ButtonStyle
global glooba
glooba=False
#from mediawiki import MediaWiki
#from mediawiki import DisambiguationError
from datetime import datetime, timezone, timedelta
from dateutil import relativedelta
import random
import requests
import asyncio
import math
import traceback
import pypandoc
from wordcloud import WordCloud
import os
import multidict 
import re
import discord
import requests
import GPUtil
from datetime import datetime
import platform
import time
import json
import psutil
import dateutil
import os
import re
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import pytz
from pylab import *
from rtlsdr import *

from rtlsdr import RtlSdr  
import numpy as np  
import scipy.signal as signal
import os
global sampler
sampler = 'Euler a'
import matplotlib
import matplotlib.pyplot as plt
import random
from gtts import gTTS
global grokReason
grokReason=""
global grokqueue
grokqueue=[]
global groktimer
groktimer=0
matplotlib.use('Agg') # necessary for headless mode  
# see http://stackoverflow.com/a/3054314/3524528

#Set Up Teh Loggah!
import logging
log_format = '[%(name)s] %(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(format=log_format,datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger=logging.getLogger('UTILITY')


from PIL import Image, ImageFont, ImageDraw, ImageColor
import wmi
from discord.ext import commands, tasks
from discord import File
from discord.utils import get

from os import path
import traceback
import multidict
import random

import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin

def newreplace(in_,rep1,rep2): #thing that replaces things
    if rep1 in in_: return in_.replace(rep1,rep2)
    return in_

def ran(a,b):
    return random.randint(a,b)/100


global ungrok
ungrok=False
global ungrok_override
ungrok_override=False

from discord import (
    SlashCommandOption as Option,
    ApplicationCommandInteraction as APPCI
) #idfk what this is for actually i do

async def message_history_img_handler(ctx): #hell
    channel = ctx.message.channel
    async for msg in channel.history(limit = 500):
        if len(msg.attachments) > 0:
            ext=msg.attachments[0].url.split('.')[-1]
            if ext in ['png','jpg','jpeg','gif','bmp']:
                return msg.attachments[0].url
        if 'http' in msg.content:
            aa=str(msg.content)
            ext=aa.split('.')[-1]
            if ext in ['png','jpg','jpeg','gif','bmp']:
                a=re.findall("(?=http).*?(?= |\n|$)",msg.content)[0]
                a=a.split('?')[0]
                return a

async def resolve_args_2(ctx,args, attachments): #HELL
    print(attachments)
    fart=1
    try:
        print(args[0])
    except:
        fart=0
    if fart:
        if 'http' in args[0]:
            url=args[0]
            kys=args[1:]
            text=' '.join(kys)
            return [url.split('?')[0],'dummy']
        elif attachments:
            url=attachments[0].url
            text=' '.join(args)
            return [url.split('?')[0],'dummy']
        else:
            url=await message_history_img_handler(ctx)
            text=' '.join(args)
            return [url,'dummy']
    elif attachments:
        url=attachments[0].url
        text=' '.join(args)
        return [url.split('?')[0],'dummy']
    else:
        url=await message_history_img_handler(ctx)
        text=' '.join(args)
        return [url,'dummy']
        
async def resolve_args(ctx,args, attachments):
    
    if 'http' in args[0]:
        url=args[0]
        kys=args[1:]
        text=' '.join(kys)
        return [url.split('?')[0],text]
    elif attachments:
        url=attachments[0].url
        text=' '.join(args)
        return [url.split('?')[0],text]
    else:
        url=await message_history_img_handler(ctx)
        text=' '.join(args)
        return [url,text]






def getFrequencyDictForText(sentence):  #for wordcloud
    fullTermsDict = multidict.MultiDict()
    tmpDict = {}

    # making dict for counting frequencies
    for text in sentence.split(" "):
        if re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|that|be", text):
            continue
        val = tmpDict.get(text, 0)
        tmpDict[text.lower()] = val + 1
    for key in tmpDict:
        fullTermsDict.add(key, tmpDict[key])
    return fullTermsDict

def finda(tofind,theuhh,ayytch): #clean up wikismegma
    findchrung=0
    for findi in theuhh:
        if findchrung:
            findye=findi
            findye=findye.replace('<td> ','')
            findye=findye.replace('<td>','')
            findye=findye.replace(' </td>','')
            findye=findye.replace('</td>','').replace('<i>','*').replace('</i>','*').replace('<b>','**').replace('</b>','**').replace('&amp;','&') #ugh i hate &amp;
            findnam=html2text.html2text((findye)).replace('\r',' ').replace('\n',' ').replace('  ',' ').rstrip()
            return findye
        if tofind.lower() in findi.lower():
            findchrung=1
            print(findi)

def do_shit(url, payload):
    return requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
    
    
def do_vid_shit(url, payload):
    print('doing vid shit')
    return requests.post(url=f'{url}/t2v/run', json=payload)

def do_other_shit(checkpoint):
    return requests.post(url='http://127.0.0.1:7860/sdapi/v1/options', json={"filter_nsfw": 'false', "sd_model_checkpoint": checkpoint}) #change the model for stable diffable wiffusion yiff yiff yiff
    
import subprocess
    
def baka_shit(): #dame dame dame yo dame mamo yo
    os.chdir('h:\\baka\\first-order-model')
    kys=subprocess.check_call('cd /d h:\\baka\\first-order-model && conda activate baka && python h:\\baka\\first-order-model\\demo.py  --config h:\\baka\\first-order-model\\config\\vox-adv-256.yaml --driving_video h:\\baka\\first-order-model\\baka.mkv --source_image h:\\baka\\first-order-model\\bakain.png --checkpoint h:\\baka\\first-order-model\\vox-adv-cpk.pth.tar --adapt_scale', shell=True)
    os.system('ffmpeg -i h:\\baka\\first-order-model\\result.mp4 -i h:\\baka\\first-order-model\\dane.wav -c:v copy -map 0:v:0 -map 1:a:0 h:\\baka\\first-order-model\\final.mp4 -y')
    os.chdir('h:\\frart')
    return 'yay!'
    
def blahja(uuid): #?????????????????????????????????????????
    #i still have no clue what the fuck this is supposed to do
    return 'the n word'

def thor(tofind,theuhh,ayytch):
    try:
        return html2text.html2text(finda(tofind,theuhh,ayytch)).replace('\r',' ').replace('\n',' ').replace('  ',' ').rstrip()
    except:
        pass

words=['pornography', 'cock and ball', 'porn', 'erotic', 'sexual']

class UtilityCommands(commands.Cog):

    

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        global wikipedia
        global wikiped
        global mario
        global wikt
        #wikipedia = MediaWiki('https://japari-library.com/w/api.php')
        #wikiped = MediaWiki('https://en.wikipedia.org/w/api.php')
        #3mario = MediaWiki('https://mariowiki.com/api.php')
        #wikt = MediaWiki('https://en.wiktionary.org/w/api.php')
        self.medbay.start()
        
        
    def cog_unload(self):
        self.medbay.cancel()
    @commands.command(name="fix")
    async def fix(self, ctx: commands.Context): #This command... Is no longer useful as notsobot images no longer save without extensions on discord "mobile"
        for i in ctx.message.attachments:
            f=requests.get(i).content
            g=generateUUID()+'.png'
            with open(g,'wb') as f2:
                f2.write(f)
            with open(g, 'rb') as f2: 
                await ctx.send(file=discord.File(f2, filename='image.png'))

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command() #GILBERT EATS POOP
    async def gilbert(self, ctx: commands.Context):
        with open('gilbert\\'+random.choice(os.listdir('gilbert')), 'rb') as f:
            await ctx.send(file=discord.File(f))
            
    @commands.command() #SEND A FUNNY DRAKE IMAGE
    async def drake(self, ctx: commands.Context):
        with open('x:\\images\\drake\\'+random.choice(os.listdir('x:\\images\\drake')), 'rb') as f:
            await ctx.send(file=discord.File(f))
            
    @commands.command() #INSECAM
    async def cam(self, ctx: commands.Context, *, fuck=''):
        z=get_data("cams")
        woombly=random.choice(z)
        
        if woombly['type'] in ['wtov','jpeg']:
            q=requests.get(woombly['url'])
            with open('cam.jpg', 'wb') as f:
                f.write(q.content)
        if woombly['type'] in ['mjpeg']:
            os.system('ffmpeg -i '+woombly['url']+' -f image2 -vframes 1 cam.jpg -y')
        desc=woombly['subj']
        desc+='\n[Feed Link]('+woombly['url']+')'
        embed=discord.Embed(title=woombly['type'].upper()+' Camera', color=0x225588, description=desc)
        embed.set_image(url="attachment://"+str('cam.jpg'))
        with open('cam.jpg', 'rb') as f:  # discord file objects must be opened in binary and read mode
            f2 = discord.File(f, filename='cam.jpg')
            await ctx.send(file=f2,embed=embed)
        
    @commands.command() #split an image into discords new "embeds"
    async def split(self, ctx: commands.Context, *args):
        uuid=str(generateUUID())
        try:
            cmd_info=await resolve_args(ctx,args, ctx.message.attachments)
        except:
            cmd_info=await resolve_args_2(ctx,args, ctx.message.attachments)
        with open('splitin'+uuid+'.png','wb') as f:
            f.write(requests.get(cmd_info[0]).content)
        splitin=Image.open('splitin'+uuid+'.png')
        splitin=splitin.resize((342*2,216*2))
        split1=splitin.crop((0, 0, 341, 215))
        split2=splitin.crop((342, 0, 342*2-1, 215))
        split3=splitin.crop((0, 216, 341, 216*2-1))
        split4=splitin.crop((342, 216, 342*2-1, 216*2-1))
        split1.save('split1'+uuid+'.png')
        split2.save('split2'+uuid+'.png')
        split3.save('split3'+uuid+'.png')
        split4.save('split4'+uuid+'.png')
        
        files_to_read: list[str] = ['split1'+uuid+'.png','split2'+uuid+'.png','split3'+uuid+'.png','split4'+uuid+'.png']
        files_to_send: list[discord.File] = []
        for filename in files_to_read:
            with open(filename, 'rb') as f:  # discord file objects must be opened in binary and read mode
                files_to_send.append(discord.File(f))
        await ctx.send(files=files_to_send)

    @tasks.loop(seconds=1.0)
    async def medbay(self): #main loop
        global ungrok_override #vram autodisable override for grok
        
        #get vram for grok
        GPUs = GPUtil.getGPUs()[0]
        free=round(GPUs.memoryFree/100)/10
        used=12-free
        total=12
        if free>6:
            ungrok_override=False
            
        
        #check if grok is stale enough to unload
        global groktimer
        if time.time()>groktimer: 
            if groktimer!=0:
                print('unloading sd models')
                jerma=requests.post(url='http://127.0.0.1:7860/sdapi/v1/unload-checkpoint')
                if jerma.status_code==200: 
                    print('success')
                else:
                    print(str(jerma))
                groktimer=0
                
        #In My House Playing DDLC
        global stammerqueue
        if len(stammerqueue)>0: #process the in my house playing ddlc queue
            try:
                if stammerqueue[0][2]=='imh': 
                    flnm='leffreyrapsing.mp3'
                else:
                    flnm=stammerqueue[0][3]
                os.system('ffmpeg -i housein_'+stammerqueue[0][1]+'.mp4 -vf scale=-2:360 -crf 33 -to 5:00 housein'+stammerqueue[0][1]+'.mp4 -y')
                os.system('python stammer.py housein'+stammerqueue[0][1]+'.mp4 '+flnm+' houseout'+stammerqueue[0][1]+'.mp4')
                os.system('ffmpeg -i houseout'+stammerqueue[0][1]+'.mp4 -vf scale=-2:360 -crf 33 -fs 7.8M houseout2'+stammerqueue[0][1]+'.mp4 -y')
                
                with open('houseout2'+stammerqueue[0][1]+'.mp4', 'rb') as f:
                    f2 = discord.File(f, filename='image.mp4')
                    await stammerqueue[0][0].send('sending...')
                    await stammerqueue[0][0].send(file=f2)
            except:
                pass
            stammerqueue.pop(0)
        #[msg,prompt,negs,seed,model,steps,sampler,resolution,cfg, bypass]
        canGrokk=True
        global grokqueue
        try:
            joebiden=(grokqueue[0][0])
        except IndexError:
            canGrokk=False #make it shut the fuck up if there are no groks in queue ?
        global ungrok
        
        global grokReason
        
        if ungrok==True: canGrokk=False
        if ungrok_override==True: canGrokk=False
        if canGrokk: #Porn Generator (Not for kids or christians)
            maintenanceMode=False
            #print('BEFORE: '+str(grokqueue))
            org=grokqueue[0]
            #fuck=grokqueue[0][0]
            mess=grokqueue[0][0]
            #await mess.channel.send('QUEUELOOP: '+str(grokqueue))
            
            #prompt=fuck.replace('—','--').split('--neg')[0]
            prompt=grokqueue[0][1]
            _negs=grokqueue[0][2]
            _seed=grokqueue[0][3]
            _model=grokqueue[0][4]
            _steps=grokqueue[0][5]
            _sampler=grokqueue[0][6]
            _resolution=grokqueue[0][7]
            _cfg=grokqueue[0][8]
            _bypass=grokqueue[0][9]
            
            #print('AFTER: '+str(grokqueue))
            url = "http://127.0.0.1:7860"
            #prompt=prompt.lower()
            prompt=prompt.replace('—','--')
            oprompt=prompt
            width=512
            height=512
            width=int(_resolution.split('x')[0])
            height=int(_resolution.split('x')[1])
            blahstodo=[]
            for yort in range(0,3):
                blahstodo.append(str(yort))
                for yort2 in range(0,10):
                    blahstodo.append(str(yort)+'.'+str(yort2))
                    for yort3 in range(0,10):
                        blahstodo.append(str(yort)+'.'+str(yort2)+str(yort3))
            #await mess.send(str(blahstodo)[:1990])
            
            
            
            
            
            
            
            
            
            snap=64
            if '16:9' in prompt:
                prompt=prompt.replace('16:9','')
                height=512
                width=int(floor((512*(16/9))/2)*2)
            if '9:16' in prompt:
                prompt=prompt.replace('9:16','')
                width=512
                height=int(floor((512*(16/9))/2)*2)
                
            if '21:9' in prompt:
                prompt=prompt.replace('21:9','')
                height=512
                width=int(floor((512*(21/9))/2)*2)
            if '9:21' in prompt:
                prompt=prompt.replace('9:21','')
                width=512
                height=int(floor((512*(21/9))/2)*2)
                
                
            if '4:3' in prompt:
                prompt=prompt.replace('4:3','')
                height=512
                width=768
            if '3:4' in prompt:
                prompt=prompt.replace('3:4','')
                height=768
                width=512
            chardef=False
            bypass=_bypass
            
            for yort in blahstodo:
                prompt=prompt.replace(':'+str(yort),'!!REPLACETHIS!!'+str(yort))
            if 'bypass' in prompt: 
                prompt=prompt.replace('bypass','')
                bypass=True
            if not bypass:
                
                prompt=prompt.replace('ezogaming','eeegaming')
                prompt=prompt.replace('ezomodel','eeemodel')
                prompt=prompt.replace("hex maniac","<lora:hexManiacPokemonLora_1:0.7> hex maniac")
                prompt=prompt.replace("mori calliope","<lora:calliopeMoriHololive_v10:0.7> mori calliope")
                prompt=prompt.replace("(kemono friends)","")
                if ' kemono friends ' in prompt:
                    prompt=prompt.replace(" kemono friends ","<lora:kemonoFriendsOfficial_kemonoFriendsOfficial:0.9> kemono friends, ")+', art by mine yoshizaki'
                if ' kemonofriends ' in prompt:
                    prompt=prompt.replace(" kemonofriends ","<lora:kemonoFriendsOfficial_kemonoFriendsOfficial:0.9> ")+', art by mine yoshizaki'
                prompt=prompt.replace('among us','<lora:amongus:1> among us')
                prompt=prompt.replace('big chungus','<lora:bigchungus:0.4> big chungus')
                prompt=prompt.replace("ezo red fox","ezo")
                prompt=newreplace(prompt,"ezo","<lora:ezo:0.75> ezo, ezo GRGGRGRGR \(kemono friends\), 1girl, solo, ")
                if 'appleq' in prompt: prompt='<lora:appleq:1> '+prompt
                prompt=newreplace(prompt,"caracal","<lora:floppa:0.75> floppa, 1girl, ((solo)), caracal \(kemono friends\), ")
                prompt=prompt.replace("prushka","<lora:prushka:0.75> prushka")
                prompt=prompt.replace("boykisser","<lora:boykisser:0.75> boykisser")
                prompt=prompt.replace("island fox","shimahai")
                prompt=newreplace(prompt,"shimahai","<lora:shimahai:0.75> shimahai, island fox \(kemono friends\), 1girl, ((solo)), ")
                prompt=prompt.replace("astolfo","<lora:astolfo1:0.8> astolfo, 1boy,")
                prompt=prompt.replace("jerma","<lora:jerma:0.8> Jerma985")
                prompt=prompt.replace("fursuit","<lora:fursuit_good:0.9> fursuit")
                prompt=newreplace(prompt,"araisan","<lora:araisan:0.75> araisan, common raccoon \(kemono friends\), 1girl, solo, ")
                prompt=prompt.replace("anya forger","anya")
                prompt=newreplace(prompt,"anya","<lora:anya:0.8> anya forger,")
                prompt=newreplace(prompt,"red fox","<lora:akagitsu:0.75> akagitsu, red fox \(kemono friends\), 1girl, solo, ")
                prompt=prompt.replace('mirai','<lora:mirai:0.7> mirai \(kemono friends\), 1girl, solo, green hair')
                prompt=prompt.replace('cartoon2','<lora:cartoonFanartStyle_v10:0.35> cartoon fanart style, ')
                prompt=prompt.replace('bimbo','<lora:bimbo:0.7> BimboT, ')
                prompt=prompt.replace("australian devil","rotty")
                prompt=newreplace(prompt,"rotty","<lora:aussie:0.75> ausdev, australian devil \(kemono friends\), 1girl, solo, medical eyepatch, ")
                prompt=newreplace(prompt,"coyote","<lora:coyo:0.7> coyo, 1girl, ((solo)), coyote \(kemono friends\), ")
                prompt=newreplace(prompt,"dhole","<lora:dolr:0.75> dolr, dhole \(kemono friends\), 1girl, solo, ")
                prompt=prompt.replace('vore','<lora:stomachInteriorVore_v2Loha:0.7> stomach interior, vore')
                prompt=prompt.replace('mrbeast','<lora:jimmyDonaldsonMrBeast_10b:0.8> jimmy_mr_beast')
                prompt=newreplace(prompt,"korone","<lora:korone:0.75> korone, inugami korone, solo, 1girl, ")
                prompt=newreplace(prompt,"neuro-sama","<lora:neuroSamaMomoseHiyori_v10:0.75> neuro-sama")
                prompt=newreplace(prompt,"fennec","<lora:feen:0.75> feen, fennec \(kemono friends\), 1girl, solo")
                prompt=prompt.replace("fubuki","<lora:fubuki2:0.75> fubuki")
                prompt=newreplace(prompt,"ryouna","<lora:ryouna:0.75> ryouna, ryouna (senran kagura), (solo), 1girl, ahoge, ")
                prompt=prompt.replace('hyperbreasts','<lora:hyper_breasts_1.8k-lr1e-4-av3-LoRA_epoc12-v5:0.4> hyperbreasts')
                prompt=prompt.replace('eee','ezo')
                if "fumo" in prompt: prompt="<lora:fumo:0.85> "+prompt
                if "cdi" in prompt: prompt="<lora:cdi:0.9> "+prompt
                if "cd-i" in prompt: prompt="<lora:cdi:0.9> "+prompt
                if "90s" in prompt: prompt="<lora:90s:0.6> "+prompt
                if "anime screen" in prompt: prompt="<lora:anime:0.4> "+prompt
                if "leffrey" in prompt: prompt="<lora:leffrey:0.9> "+prompt
                if "danny" in prompt and 'gee' not in prompt: prompt="<lora:danny:0.9> "+prompt
                if "kf1" in prompt: prompt="<lora:kf1style_v3_abyss-000016:0.8> "+prompt
                if "bottomheavy" in prompt: prompt: prompt="<lora:hyperBottomHeavy_v1:0.4> "+prompt
                if "persona" in prompt: prompt: prompt="<lora:persona:0.5> "+prompt
                if "soejima shigenori" in prompt: prompt: prompt="<lora:persona:0.5> "+prompt
                if "ftm" in prompt: prompt: prompt="<lora:ftm:0.4> "+prompt
                if "ezogaming" in prompt: prompt: prompt="<lora:ezomodel:0.8> "+prompt
                if "vhs" in prompt: prompt: prompt="<lora:vhs:1.2> "+prompt
                if "polaroid" in prompt or 'pqr' in prompt: prompt="<lora:photo:1.2> vintage polaroid analog portrait photography of"+(prompt.replace('polaroid','').replace('pqr',''))
                if "sayoriv4" in prompt: prompt=prompt.replace('sayoriv4',"<lora:sayoriv4:2.7>)")
                if "analog" in prompt and 'polaroid' not in prompt: prompt="<lora:analog:1.2> (analog style film still of) "+(prompt.replace('analog',''))
                if "shrift" in prompt: prompt="<lora:nekomata:1> ((SHRIFT, nekomata-aran)), simple shading, flat shading, pixel art, lowres, "+(prompt.replace('shrift',''))
                if 'leash' in prompt:
                    if "sub" in prompt:
                        prompt="((<lora:leash_sub:1> leashed_pov, ))"+prompt
                    if "dom" in prompt:
                        prompt="((<lora:leash_dom:1> leashing_pov, ))"+prompt
                prompt=newreplace(prompt,"bondrewd","<lora:bondrewd:0.8> bdsks, mask, white whistle, ")
                prompt=prompt.replace("silver fox","silver")
                prompt=newreplace(prompt,"silver","<lora:gingitsu:0.7> gingitsu, silver fox \(kemono friends\), 1girl, solo, ")
                prompt=prompt.replace('izuna','<lora:izuna-v1-NAI-VAE-768px:0.6456> izuna \(blue archive\), 1girl, solo') 
                prompt=newreplace(prompt,"japanese wolf","<lora:jpwolf:0.8> japanese wolf (kemono friends), 1girl, solo, ")
                prompt=prompt.replace('grey wolf','<lora:g_wolkf:0.8> g_wolkf, grey wolf \(kemono friends\), 1girl, solo, heterochromia')
                if 'wolkf' in prompt:
                    prompt=prompt+' AND blue eyes, yellow eyes' 
                    #It couldve been a one liner but for some reason python wants it to be like this now despite it literally fucking working before. :))))))_
                prompt=prompt.replace("greater roadrunner","roadrunner")
                #prompt=prompt.replace("penis","<lora:penisLora_v1:"+str(ran(60,90))+"> penis")
                prompt=newreplace(prompt,"roadrunner","<lora:kusomeepchan:0.75> kusomeepchan, greater roadrunner \(kemono friends\), 1girl, ((solo)), ")
                prompt=prompt.replace("greater lophorina","lophorina")
                prompt=newreplace(prompt,"lophorina","<lora:lophorina:0.75> lophorina, superb bird-of-paradise (kemono friends), ")
                prompt=newreplace(prompt,"natsuki2","<lora:natuki:0.65> natuki, 1girl, ((solo)), pink hair, hair ornament, pink eyes, short hair, ribbon, hairclip, hair ribbon, pigtails, white tshirt, pink frilly skirt, rolled up sleeves, tucked in shirt, wide necked shirt, collarbone, [bra straps], ")
                prompt=newreplace(prompt,"natsuki","<lora:natuki:0.75> natuki, 1girl, ((solo)), pink hair, hair ornament, pink eyes, short hair, hairclip, hair ribbon, pigtails ")
                prompt=prompt.replace('natuki, ','natuki, natsuki \(doki doki literature club\), ')
                prompt=prompt.replace("sans","<lora:sans:0.5> sans,")
                prompt=prompt.replace("senko","<lora:senko:0.75> senko")
                prompt=prompt.replace("burger","<lora:burger:0.7> burger")
                prompt=prompt.replace("by cwc","<lora:cwc:1.1> by cwc")
                prompt=newreplace(prompt,"serval","<lora:serval:0.75> serval \(kemono friends\), 1girl, solo, ")
                
                prompt=newreplace(prompt,"toki","<lora:toki:0.65> toki, crested ibis \(kemono friends\), 1girl, solo, ")
                prompt=prompt.replace("arma","<lora:arma:0.8> arma, giant armadillo \(kemono friends\), 1girl, solo, ")
                prompt=prompt.replace("scarlet ibis","<lora:scarlet_ibis-red_toki:0.8> red_toki, scarlet ibis \(kemono friends\), 1girl, solo, ")
                prompt=newreplace(prompt,"tsuchinoko","<lora:tsunsnek:0.75> tsunsnek, tsuchinoko \(kemono friends\), 1girl, solo, ")
                prompt=prompt.replace('brid', '<lora:bird_wings:0.75> anthro furry bird, winged arms,')
                prompt=newreplace(prompt,"mikudayo","<lora:mikudayo_1:0.75> 1girl, (chibi:1.2), hatsune_miku, looking_at_viewer, open_mouth, smile, solo, standing,")
                prompt=prompt.replace('amiya', '<lora:arknightsAMIYA_v10:0.8> amiya')
                prompt=prompt.replace('nessa','<lora:character_pokemon_nessa:0.8> nessa')
                prompt=prompt.replace('hooters','<lora:hooters:0.8> hooters')
                prompt=prompt.replace('ricardo milos','<lora:ricardoMilos_v10:0.8> ricardo milos')
                prompt=prompt.replace('gawr gura','<lora:virtualYoutuberGawr_ggV1:0.8> gawr gura')
                prompt=prompt.replace('karaoke','<lora:karaokeroom_test08:0.8> karaoke room')
                prompt=prompt.replace('inkling','<lora:inklingGirlsLora_v1:0.8> inkling')
                prompt=prompt.replace('koishi','<lora:komeijikoishiV01_komeijikoishiV01:0.8> koishi')
                prompt=prompt.replace('diane foxington','<lora:dianeFoxington_v4:0.8> diane foxington')
                prompt=newreplace(prompt,"common bottlenose dolphin","<lora:cbd:0.75> cbd, solo, 1girl, gray hair, ")
                prompt=prompt.replace('kagamine_rin','kagamine rin')
                prompt=prompt.replace('kagamine rin','<lora:KagamineRin_kagamineRin:0.8> kagamine_rin')
                prompt=prompt.replace('moviepeach','<lora:princessPeachMario_v10:0.7> princess peach')
                prompt=prompt.replace('cum bath','<lora:cumBath_v10:0.7> cum bath') #lol
                if 'middle finger' in prompt: prompt='<lora:middlefinger:0.75> '+prompt
                if 'quicksand' in prompt or 'mud' in prompt: prompt='<lora:partially_submerged:0.75> partially_submerged, '+prompt
                prompt=prompt.replace('character','myfuckingballshurtow')
                if 'chara' in prompt: prompt='<lora:chara:0.75> brown hair, '+prompt
                prompt=prompt.replace('myfuckingballshurtow','character')
                if 'felix' in prompt: prompt='<lora:felix:0.75> 1boy, male, '+prompt
                if 'mgq' in prompt or 'monster girl quest' in prompt or 'mon-musu' in prompt: prompt='<lora:mgq:0.75> '+prompt
                
                
                prompt=newreplace(prompt,"sylph","<lora:sylph:0.75> sylphmgq, 1girl, ahoge, bare shoulders, breasts, sylph (mon-musu quest!), dress, elbow gloves, gloves, green dress, green hair, long hair, medium breasts, multicolored hair, mon-musu quest!, solo, yellow eyes, elf shoes, ")
                
                prompt=newreplace(prompt,"karyl","<lora:karyl:"+str(ran(30,70))+"> cat ears, black hair, green eyes, ")
                
                prompt=newreplace(prompt,"pooltoy","<lora:pooltoy:"+str(ran(110,130))+"> pool_toy, ")
                prompt=prompt.replace("danganronpa","<lora:Danganronpa_Style:0.7> danganronpa style")
                prompt=newreplace(prompt,"cat nonsense girl","<lora:karyl:"+str(ran(60,90))+"> cat ears, black hair, green eyes, ")
                prompt=prompt.replace("yuki","<lora:yukicrush:"+str(ran(70,100))+"> yukicrush,")
                prompt=prompt.replace("rougethebat","<lora:rouge:0.5> rougethebat")
                prompt=prompt.replace("tinkaton","<lora:tinkaton:"+str(ran(70,100))+"> tinkaton,")
                
                #prompt=prompt.replace("mia","<lora:mia:"+str(ran(70,100))+"> mia,")
                
                prompt=prompt.replace("pregnant","<lora:pregnant:"+str(ran(10,40))+"> pregnant,")
                
                prompt=prompt.replace("gardevoir","<lora:gardewhore:"+str(ran(60,100))+"> gardevoir,")
                
                if 'neco' in prompt: prompt="<lora:neco:"+str(ran(100,110))+"> (necoarc, necopose),"+prompt

                if "zun" in prompt: prompt="<lora:zun:"+str(ran(80,110))+"> ((zun, zun (style))), "+(prompt.replace('zun',''))
                prompt=prompt.replace('tttttttttttttttttttttttttttttttt','izuna')
                if len(prompt)<1:
                    prompt=''
                    for qyoo in range(random.randint(1,10)):
                        prompt+='<lora:'+random.choice(['90s', 'akagitsu', 'analog', 'anime', 'anya', 'araisan', 'astolfo1', 'astolfo2', 'aussie', 'betterscales', 'bondrewd', 'braixen', 'cbd', 'cdi', 'chara', 'coyo', 'danny', 'dark', 'dolr', 'ezo', 'ezomodel', 'feen', 'felix', 'floppa', 'ftm', 'fubuki1', 'fubuki2', 'fumo', 'gardewhore', 'gingitsu', 'hyperBottomHeavy_v1', 'ilulu', 'izuna-v1-NAI-VAE-768px', 'jpwolf', 'karyl', 'kf1style', 'korone', 'kusomeepchan', 'leash_dom', 'leash_sub', 'leffrey', 'lophorina', 'marina', 'mgq', 'microwaist', 'middlefinger', 'natuki', 'nekomata', 'partially_submerged', 'persona', 'photo', 'pooltoy', 'pregnant', 'ryouna', 'sans', 'sayori', 'sayoriv4', 'scales', 'senkonanoja', 'serval', 'shimahai', 'shizue', 'spider', 'surtr', 'sylph', 'tinkaton', 'toki', 'tsunsnek', 'vhs', 'yukicrush', 'zun'])+':'+str(ran(10,120))+'> '
            
            negs=''
            if not bypass and 'shrift' not in prompt.lower(): negs="lowres, bad anatomy, bad hands, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name, simple background, flat background,  high saturation, black and white, small feet, simple shading, flat shading, blue skin"
            if not bypass and 'shrift' not in prompt.lower(): negs="lowres, bad anatomy, bad hands, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name"
            if not bypass: negs="ng_deepnegative_v1_75t, (worst quality, low quality:1.4), (child, loli, little kid:1.4)"
            #if 'ezogaming' in prompt:
                #negs="bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, signature, watermark, username, blurry, artist name, high saturation, black and white, small feet"
            prompt=prompt.replace("GRGGRGRGR","red fox")
            prompt=prompt.replace("neso","<lora:servalneso:0.8> sogganeso")
            
            
            if mess.id==886788323648094219:
                await mess.send('go to grok bitch')
                return
            
            if "1girl" in oprompt and "1boy" not in oprompt and not bypass:
                prompt=newreplace(prompt,'boy','girl')
                prompt=newreplace(prompt,'1girl','female, 1girl')
                negs+=', 1boy, male, boy'
            if "1boy" in oprompt and not bypass and "1girl" not in oprompt:
                prompt=newreplace(prompt,'girl','boy')
                prompt=newreplace(prompt,'1boy','male, 1boy')
                p_=[]
                for i in prompt.split(','):
                    #print(i)
                    if True:#'breasts' not in i:
                        p_.append(i)
                #print(p_)
                prompt=','.join(p_)
                negs+=', ((1girl, female, breasts, girl))'
                
            
            test=prompt
            if not bypass:
                test=prompt.replace('lora:','lora_')


                split_=re.split('([<>()\[\]:])|(, )',test)
                split=[]
                for i in split_:
                    if i != None:
                        split.append(i)

                proc=[]
                
                for i in split:
                    ginja=False
                    for i2 in i:
                        if i2 in '0123456789':
                            ginja=True
                    
                    
                    if i not in proc and i+':' not in proc or i in ['<','>','(',')','[',']',', '] or ginja:
                        if i.startswith('lora'):
                            proc.append(i+':')
                        else:
                            proc.append(i)
                    
                zooga=''.join(proc)
                
                for q in range(40):
                    zooga=zooga.replace('::',':')
                    zooga=zooga.replace('<0.','')
                    zooga=zooga.replace('<1.','')
                    for zr in range(100):
                        zooga=zooga.replace(' '+str(zr)+'>',' ')
                        zooga=zooga.replace(' '+str(zr)+'>',' ')
                    zooga=zooga.replace('  ',' ')
                    zooga=zooga.replace(' , ',', ')
                    zooga=zooga.replace(',,',',')
                    
                    
                prompt=zooga.replace('lora_','lora:')
                
            loras=[]
            try:
                for i in prompt.split(','):
                    #print(i)
                    if 'lora' in i:
                        loras.append(i.split(':')[1]+' at '+str(int(float(i.split(':')[2].replace('>',''))*100))+'% weight')
            except:
                loras=['error']
                
                
                
                
            try:
                negs+=', '+_negs
            except:
                pass
            #print(prompt)
            #print(negs)
            prompt=newreplace(prompt,",,",",")
            prompt=newreplace(prompt,"  "," ")
            prompt=newreplace(prompt," ,",",")
            checkpoint='i_models\\Anything-V3.0-pruned-fp32.ckpt'
            __model=_model
            if 'cwc' in prompt: checkpoint='fluffusion_r1_e6_640x.ckpt'
            if 'tofm' in prompt: checkpoint='x_models\\ThisOnesFinalMixv1.ckpt'
            if 'ezmix' in prompt: checkpoint='i_models\\abyss-rs-anything-rs-40-60.safetensors'
            if 'aom' in prompt: 
                try:
                    blah=mess.nsfw
                except:
                    blah=True
                if blah==True:
                    checkpoint='i_models\\abyssorangemix3AOM3_aom3a3.safetensors'
                    __model='aom3'
                else:
                    checkpoint='i_models\\AbyssOrangeMix2_sfw_pruned_fp16_with_VAE.ckpt'
                    __model='aom2-sfw'
                prompt=prompt.replace('aom','')
                _steps=40
            prompt=prompt.replace('ezmix','')
            #if 'sayotrigger' in prompt: 
                #checkpoint='sayoriDiffusion_v1.ckpt'
                #prompt=prompt.replace('sayotrigger','')
            if 'fluffusion' in prompt: 
                checkpoint='aaaaaaaaaaaaaaaaaaaaaaaa-fluffusion-merge-test.safetensors'
                
                
                prompt=prompt.replace('fluffusion','')
                
            if 'sayotrigger' in prompt: 
                checkpoint='i_models\\SayoriAnythingv5.ckpt'
                prompt=prompt.replace(' sayotrigger','')
                prompt=prompt.replace('sayotrigger ','')
                prompt=prompt.replace('sayotrigger','')
                
                
            if __model=='furry':
                checkpoint='i_models\\lawlassYiffMix_lawlasmix.safetensors'
            if __model=='model':
                checkpoint='model.safetensors'  
            if __model=='stable':
                checkpoint='model.safetensors'  
            if __model=='appleq':
                checkpoint='i_models\\Anything-V3.0-pruned-fp32+appleq.ckpt'   
            if __model=='sayori':
                checkpoint='i_models\\SayoriAnythingv5.ckpt'  
            if __model=='yeah':
                checkpoint='i_models\\Merges\yeah.ckpt'  
            #if fuck=='anything': mod='Anything-V3.0-pruned-fp32.ckpt'
            #if fuck=='furry': mod='lawlassYiffMix_lawlasmix.safetensors'
            #if fuck=='hot': mod='hot.safetensors'
            #if fuck=='model': mod='model.ckpt'
                
            #sampler='Euler a'
            cfg=6.5#random.randint(12,18)/2
            cfg=_cfg
            #if "sayori" in prompt: cfg=random.randint(12,14)/2
            if prompt=='carrots':
                prompt='joe biden sexy'
            
            ballsac=prompt.split(' ')
            proompt=''
            prampt=[]
            #await mess.send(str(ballsac))
            for q in ballsac:
                #print(q.startswith('seed='))
                if q.startswith('seed='):
                    _seed=int(q.replace('seed=',''))
                    
                else:
                    prampt.append(q)
            proompt=' '.join(prampt)
            prompt=proompt
            if _seed==-1:
                _seed=random.randint(0,99999999)
            
            #if 'shrift' in prompt.lower():
            #    width=256
            #    height=256
            ms=await mess.send('switching models... (queue length: '+str(len(grokqueue))+')')
            global sampler
            __sampler=_sampler
            if 'dpm' in prompt: 
                __sampler='DPM++ SDE Karras'
                prompt=prompt.replace('dpm','')
            if 'unipc' in prompt: 
                __sampler='UniPC'
                prompt=prompt.replace('unipc','')
            if 'reverse_prompts' in prompt:
                prompt=prompt.replace('reverse_prompts','')
                negs=negs.replace('(child, loli, little kid:1.4)','')
                n=negs
                negs='(child, loli, little kid:1.4), '+prompt
                prompt=n
                
            prompt=prompt.replace('!!REPLACETHIS!!',':')
            payload = {
                "prompt": prompt,
                "negative_prompt": negs,
                "steps": _steps,
                "sd_model_checkpoint": checkpoint,
                "sampler_index": __sampler,
                "cfg_scale": _cfg,
                "width": width,
                "height": height,
                "seed": _seed
                
            }
            width2=width
            height2=height
            if 'tofm' in prompt:
                prompt=prompt.replace('tofm','')
                payload = {
                    "prompt": prompt,
                    "negative_prompt": negs,
                    "steps": _steps,
                    "sd_model_checkpoint": checkpoint,
                    "sampler_index": __sampler,
                    "cfg_scale": _cfg,
                    "width": width,
                    "height": height,
                    "seed": _seed,
                    "hr_scale": 2,
                    "hr_upscale": "Latent",
                    "guess_mode": True,
                    "enable_hr": True,
                    "denoising_strength": 0.6
                    
                }
                width2=width2*2
                height2=height2*2
            if 'hires' in prompt:
                prompt=prompt.replace('hires','')
                payload = {
                    "prompt": prompt,
                    "negative_prompt": negs,
                    "steps": _steps,
                    "sd_model_checkpoint": checkpoint,
                    "sampler_index": __sampler,
                    "cfg_scale": _cfg,
                    "width": width,
                    "height": height,
                    "seed": _seed,
                    "hr_scale": 2,
                    "hr_upscale": "Latent",
                    "guess_mode": True,
                    "enable_hr": True,
                    "denoising_strength": 0.61
                    
                }
                width2=width2*2
                height2=height2*2
            #payload2={"filter_nsfw" : True}
            booberinoes=await self.bot.loop.run_in_executor(None, do_other_shit, checkpoint)
            
            
            try:
                if ctx.guild.id==706353387855151105:
                    #if 'ezogaming' not in prompt: negs+='((porn, nipples, pussy, vagina, penis, sex, penetration))'
                    payload = {
                        "prompt": prompt,
                        "negative_prompt": negs,
                        "steps": _steps,
                        "sd_model_checkpoint": checkpoint,
                        "sampler_index": __sampler,
                        "cfg_scale": _cfg,
                        "filter_nsfw": True,
                        "width": width,
                        "height": height,
                        "seed": _seed
                    }
                    booberinoes=await self.bot.loop.run_in_executor(None, do_other_shit, checkpoint)
            except:
                pass
            #print(booberinoes)
            #print(payload)
            apnd=''
            if maintenanceMode: apnd='\nMAINTENANCE MODE: your grok may end up being cancelled from a reload'
            await ms.edit(content='processing "'+prompt+'"... (queue length: '+str(len(grokqueue))+')'+apnd)
            response = await self.bot.loop.run_in_executor(None, do_shit, url, payload)
            #print(response.json())

            r = response.json()
            uuid=generateUUID()
            
            try:
                for i in r['images']:
                    image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

                    png_payload = {
                        "image": "data:image/png;base64," + i
                    }
                    response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

                    pnginfo = PngImagePlugin.PngInfo()
                    pnginfo.add_text("parameters", response2.json().get("info"))
                    
                    image=image.resize((width2,height2),resample=Image.NEAREST)
                    image.save('h:\\ai\\output'+str(uuid)+'.png', pnginfo=pnginfo)
                await ms.edit(content='uploading "'+test+'"...')
                with open('h:\\ai\\output'+str(uuid)+'.png', 'rb') as f: 
                    f2 = discord.File(f, filename='image.png')
                    #await mess.send('your grok, sir.\nPrompt: `'+r['parameters']['prompt']+'`\nNegative Prompt: `'+r['parameters']['negative_prompt']+'`\nSampler: '+r['parameters']['sampler_index']+'\nModel: '+__model+'\nCFG: '+str(_cfg)+'\nLoRAs Used:\n'+'\n'.join(loras)+'\nSeed: '+str(_seed),file=f2)
                    
                    await mess.send('your grok, sir.\n`'+str(response2.json().get("info"))+'`',file=f2)
                    
                    
                    #await mess.send('your grok, sir.\n'+str(org),file=f2)
                await ms.delete()
            except: 
                await mess.send('error')
            grokqueue.pop(0)
            
        
    @commands.command() #IN MY HOUSE PLAYING DDLC
    async def inmyhouse(self, ctx: commands.Context, link=None):
        uuid=str(generateUUID())
        if link is None: imgurl=ctx.message.attachments[0].url
        if link is not None:imgurl=link
        
        with open('housein_'+uuid+'.mp4', 'wb') as f:
            f.write(requests.get(imgurl).content)
        await ctx.send('processing...')
        global stammerqueue
        stammerqueue.append([ctx,uuid,'imh',None,None])
        
        
        
    
        
        
        
    @commands.command()
    async def stammer(self, ctx: commands.Context, *args): #Manual INMYHOUSE.PLAYINGDDL_C
        uuid=str(generateUUID())
        #if link is None: imgurl=ctx.message.attachments[0].url
        #if link is not None:imgurl=link
        for attach in ctx.message.attachments:
            for beep in ['mp3','wav','flac','ogg']:
                if attach.url.endswith(beep): audurl=attach.url
            for beep in ['mp4','avi','webm','mov','mkv']:
                if attach.url.endswith(beep): vidurl=attach.url
        
        for url in args:
            for beep in ['mp3','wav','flac','ogg']:
                if url.endswith(beep): audurl=url
            for beep in ['mp4','avi','webm','mov','mkv']:
                if url.endswith(beep): vidurl=url
        
        
        with open('housein_'+uuid+'.mp4', 'wb') as f:
            f.write(requests.get(vidurl).content)
        
        ext=audurl.split('.')[-1]
        with open('stammer_'+uuid+'.'+ext, 'wb') as f:
            f.write(requests.get(audurl).content)
        await ctx.send('processing...')
        global stammerqueue
        stammerqueue.append([ctx,uuid,'stammer','stammer_'+uuid+'.'+ext,None])
        
    @commands.command(name="help")
    async def help(self, ctx: commands.Context, section='main'): #the most epic help command of all time!!!!!!!!
        if section=='main':
            embed=discord.Embed(title='Help', description='Do .help [section] to get help')
            embed.add_field(name="Utility", value="Useful stuff", inline=True)
            embed.add_field(name="Fun", value="HAHAHAHAHAAH", inline=True)
            embed.add_field(name="Manipulation", value="Image/Video manipulation", inline=True)
            embed.add_field(name="Voice", value="Probably broken voice commands", inline=True)
            embed.add_field(name="AI", value="Harvesting my GPU for slave labor", inline=True)
            await ctx.send(embed=embed)
        else:
            if section=='utility': helps=get_data("help_utility")
            if section=='fun': helps=get_data("help_fun")
            if section=='manipulation': helps=get_data("help_manipulation")
            if section=='voice': helps=get_data("help_voice")
            if section=='ai': helps=get_data("help_ai")
            inde=0
            inde2=0
            for i2 in range(0,10):
                if inde<len(helps):
                    embed=discord.Embed(title='Help', description=section+" commands")
                    comlis1='`'
                    for i3 in range(0+inde2,len(helps)):
                        i=helps[i3]
                        print(len(comlis1))
                        if len(comlis1)>800: inde2=inde
                        if len(comlis1)>800: break
                        a=i[0]
                        b=i[1]
                        if a.startswith('ezoLang'): a=get_lang(a)
                        if b.startswith('ezoLang'): b=get_lang(b)
                        comlis1+=a+': '+b+'\n'
                        inde+=1
                    print(len(comlis1))
                    comlis1+='`'
                    comlis1=comlis1.replace('\n`','`')
                    print(len(comlis1))
                    embed.add_field(name="Command", value=comlis1, inline=True)
                    await ctx.send(embed=embed)

    @commands.command()
    async def gifify(self, ctx=commands.Context, *args): #turn a VIDOE into ANIMETED GIF GILF
        try:
            cmd_info=await resolve_args(ctx,args, ctx.message.attachments)
        except:
            cmd_info=await resolve_args_2(ctx,args, ctx.message.attachments)
        imgurl=cmd_info[0]
        with open('R:\\inputfile.mkv', 'wb') as f:
            f.write(requests.get(imgurl).content)
        #os.system('ffmpeg -i R:\\inputfile.mkv -vf "select=eq(n\,0)" -q:v 3 R:\\FirstFrame.jpg -y')
        os.system('ffmpeg -i R:\\inputfile.mkv -lavfi "scale=256x256,fps=1,palettegen=max_colors=128:stats_mode=diff" R:\\palette.png -y')
        os.system('ffmpeg -i R:\\inputfile.mkv -i R:\\palette.png -lavfi "fps=25,scale=-1:240,mpdecimate,paletteuse=dither=none" -fs 8M R:\\FirstFrame.gif -y')
        with open('R:\\FirstFrame.gif', 'rb') as f:
            f2 = discord.File(f, filename='image.gif')
            await ctx.send(file=f2)
    @commands.command() #i dont think this command works anymore ok it does
    async def lyrics(self, ctx: commands.Context, *sch):
        search=" ".join(sch)
        genius = Genius('7I-Tp4i9xplnuwrEuFQG6bxVjSoN3DOI6zELttPoPL9fERrvdjtBx_rojcjr7eq7')
        genius.response_format = 'markdown'
        songh = genius.search_song(search)
        penis=songh.lyrics
        final=[penis[i:i+2000] for i in range(0, len(penis), 2000)]
        for i in final:
            await ctx.send(i)
            
            
            
    @commands.command()
    async def greverse(self, ctx=commands.Context, *args): #reverse a gif because NOTSOBOT REMOVED IT
        try:
            cmd_info=await resolve_args(ctx,args, ctx.message.attachments)
        except:
            cmd_info=await resolve_args_2(ctx,args, ctx.message.attachments)
        imgurl=cmd_info[0]
        with open('R:\\inputfile.gif', 'wb') as f:
            f.write(requests.get(imgurl).content)
        #os.system('ffmpeg -i R:\\inputfile.mkv -vf "select=eq(n\,0)" -q:v 3 R:\\FirstFrame.jpg -y')
        os.system('ffmpeg -i R:\\inputfile.gif -vf reverse R:\\reversed.gif -y')
        with open('R:\\reversed.gif', 'rb') as f:
            f2 = discord.File(f, filename='image.gif')
            await ctx.send(file=f2)
   
    
    @commands.command(aliases=['jw']) #broken as of python update
    async def jwiki(self, ctx: commands.Context, *url_):
        # try:
            # print("4")
            # sch=" ".join(url_).title()
            # albums=get_data("albums")
            # albtitle=[]
            # for i in albums:
                # albtitle.append(i['name_e'].lower())
            # for i in albums:
                # albtitle.append(i['name_j'].lower())
            # for i in albums:
                # for i2 in i['aliases']:
                    # albtitle.append(i2.lower())
            # print(sch.lower())
            # if sch.lower()=="album" or sch.lower()=="album ":
                # albtitle.append(sch.lower())
                # print('coolio')
            # if sch.lower() not in albtitle:
                # if sch=="" or sch==" ": sch="friend"
                # if sch is not "All" and sch.lower() is not "friend":
                    # p = wikipedia.search(sch)
                    # if 'Anime' in p[0] and 'anime' not in sch.lower():
                        # print('found greasy anime fan')
                        # print(p[0])
                        # p.pop(0)
                        # print(p[0])
                    # print("5")
                    # shat=0
                    # try:
                        # print(sch)
                        # p2 = wikipedia.page(title=sch, auto_suggest=False)
                        # print("Yee-Haw!")
                    # except:
                        # shat=1
                        # print("Gets Shot")
                        # try:
                            # p2 = wikipedia.page(p[0])
                        # except IndexError:
                            # p = wikipedia.prefixsearch(sch)
                            # p2 = wikipedia.page(p[0])
                    # print('shat? '+str(shat)+'.')
                    # if not shat: 
                        # p2=wikipedia.page(title=sch, auto_suggest=False)
                    # thisshitsucks=0
                    # if 'anime' in p[0].lower():
                        # print('shoebill')
                        # if 'anime' not in sch.lower():
                            # print(p)
                            # print(p[1])
                            # print('sex')
                            # thisshitsucks=1
                            # print(p2)
                            # print(wikipedia.page(p[1]))
                    # if thisshitsucks: p2 = wikipedia.page(p[1])
                # if sch=='' or sch==' ' or sch.lower()=="friend" or sch.lower()=="all" or sch.lower() in ['fox','foxes','cat','cats','felid','felines','feline','wolf','wolves','bird','birds','song','songs','album','albums']:
                    # if sch=='' or sch==' ' or sch.lower()=="friend":
                        # goodmembers=wikipedia.categorymembers('Friends', results=None, subcategories=False)
                        # badmembers=wikipedia.categorymembers('Anime Friends', results=None, subcategories=False)
                        # members=[]
                        # for i in goodmembers:
                            # print(i)
                            # if i not in badmembers:
                                # members.append(i)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="song" or sch.lower()=="songs":
                        # members=wikipedia.categorymembers('Songs', results=None, subcategories=False)
                        # print(members)
                        # if type(members) is tuple:
                            # members=members[0]
                        # print(members)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="fox" or sch.lower()=="foxes":
                        # goodmembers=wikipedia.categorymembers('Fox Friends', results=None, subcategories=False)
                        # badmembers=wikipedia.categorymembers('Anime Friends', results=None, subcategories=False)
                        # members=[]
                        # for i in goodmembers:
                            # print(i)
                            # if i not in badmembers:
                                # members.append(i)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="bird" or sch.lower()=="birds":
                        # goodmembers=wikipedia.categorymembers('Bird Friends', results=None, subcategories=False)
                        # badmembers=wikipedia.categorymembers('Anime Friends', results=None, subcategories=False)
                        # members=[]
                        # for i in goodmembers:
                            # print(i)
                            # if i not in badmembers:
                                # members.append(i)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="canid" or sch.lower()=="canine":
                        # goodmembers=wikipedia.categorymembers('Canid Friends', results=None, subcategories=False)
                        # badmembers=wikipedia.categorymembers('Anime Friends', results=None, subcategories=False)
                        # members=[]
                        # for i in goodmembers:
                            # print(i)
                            # if i not in badmembers:
                                # members.append(i)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="wolf" or sch.lower()=="wolves":
                        # goodmembers=wikipedia.categorymembers('Wolf Friends', results=None, subcategories=False)
                        # badmembers=wikipedia.categorymembers('Anime Friends', results=None, subcategories=False)
                        # members=[]
                        # for i in goodmembers:
                            # print(i)
                            # if i not in badmembers:
                                # members.append(i)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="felid" or sch.lower()=="feline" or sch.lower()=="felines" or sch.lower()=="cats" or sch.lower()=="cat":
                        # goodmembers=wikipedia.categorymembers('Felid Friends', results=None, subcategories=False)
                        # badmembers=wikipedia.categorymembers('Anime Friends', results=None, subcategories=False)
                        # members=[]
                        # for i in goodmembers:
                            # print(i)
                            # if i not in badmembers:
                                # members.append(i)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="album" or sch.lower()=="albums":
                        # members=wikipedia.categorymembers('Albums', results=None, subcategories=False)
                        # print(members)
                        # if type(members) is tuple:
                            # members=members[0]
                        # print(members)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="all":
                        # p2=wikipedia.page(wikipedia.random())
                # print("6")
                # htm=p2.html
                # sd=htm.split('\n')
                # print("7")
                # imgss=p2.images
                # print("8")
                # imglink='http://example.com'
                # for i in sd:
                    # if 'img' in i:
                        # print(i)
                        # kindaimg=i
                        # break
                # print("9")
                # for i in imgss:
                    # q=i[-16:]
                    # if q in kindaimg:
                        # print(q)
                        # imglink=i
                        # break
                # for i in sd:
                    # if i.startswith('<p>') and 'img' not in i:
                        # print(i)
                        # wikitext=i
                        # break
                # h = html2text.HTML2Text()
                # h.ignore_links = True
                # h.ignore_images = True
                # wikicode=h.handle(wikitext).replace('\r',' ').replace('\n',' ').replace('  ',' ')
                # print("10")
                # with open('frien.png', 'wb') as f: 
                    # f.write(requests.get(imglink).content)
                # with open('frien.png', 'rb') as f: 
                    # f2 = discord.File(f, filename='image.png')
                    # embed=discord.Embed(title=p2.title, color=0x225588, description=wikicode, url=p2.url)
                    # embed.set_image(url="attachment://"+str('image.png'))
                    # embed.set_footer(text='wikipedia results')
                    # print(p2.categories)
                    # if 'Friends' in p2.categories:
                        # nam='Empty'
                        # appear='Empty'
                        # scientific='Empty'
                        # dist='Empty'
                        # conservation='Empty'
                        # wikipedia_article='Empty'
                        # nam=thor('Japanese Name',sd,h)
                        # synonyms=get_data("friend_japanese_names")
                        # hasit=0
                        # for i in synonyms:
                            # if i[0]==nam:
                                # haskanji=1
                                # hasit=1
                                # kanji=i[1]
                                # trans=i[2]
                                # if kanji=="NoKanji": haskanji=0
                        
                        # if hasit and haskanji: nam+="/"+kanji
                        # nam+="\n*"+thor('Romanised Name',sd,h)+'*'
                        # if hasit: nam+='/*'+trans+'*'
                        # #nam+="\n*"+thor('Romanised Name',sd,h)+'*'
                        # appear=thor('Also known as',sd,h)
                        # scientific=thor('Scientific Name',sd,h)
                        # dist=thor('Distribution',sd,h)
                        # wikipedia_article=thor('Read More',sd,h)
                        # if 'Status iucn3.1 LC' in htm:
                            # conservation='Least Concern'
                        # if 'Status iucn3.1 NT' in htm:
                            # conservation='Near Threatened'
                        # if 'Status iucn3.1 VU' in htm:
                            # conservation='Vulnerable'
                        # if 'Status iucn3.1 EN' in htm:
                            # conservation='Endangered'
                        # if 'Status iucn3.1 CR' in htm:
                            # conservation='Critically Endangered'
                        # if 'Status iucn3.1 EW' in htm:
                            # conservation='Extinct In Wild'
                        # if 'Status iucn3.1 EX' in htm:
                            # conservation='Extinct'
                        # if 'Uma_label' in htm:
                            # conservation='Unidentified Mysterious Animal'
                        # print(nam)
                        # print(appear)
                        # print(scientific)
                        # print(dist)
                        # print(conservation)
                        # embed.add_field(name='Japanese Name',value=nam, inline=True)
                        # embed.add_field(name='Other Names',value=appear, inline=True)
                        # embed.add_field(name='Scientific Name',value=scientific, inline=True)
                        # embed.add_field(name='Distribution',value=dist, inline=True)
                        # embed.add_field(name='IUCN',value=conservation, inline=True)
                        # embed.add_field(name='Wikipedia',value=wikipedia_article, inline=True)
                    
                    # if 'Albums' in p2.categories:
                        # embed=discord.Embed(title=p2.title, color=0x225588, description='Test')
                        # album=get_data("albums")[0]
                        # embed.add_field(name='Japanese Name',value=nam, inline=True)
                        # embed.add_field(name='Other Names',value=appear, inline=True)
                        # embed.add_field(name='Scientific Name',value=scientific, inline=True)
                        # embed.add_field(name='Distribution',value=dist, inline=True)
                        # embed.add_field(name='IUCN',value=conservation, inline=True)
                        # embed.add_field(name='Wikipedia',value=wikipedia_article, inline=True)
                    
                    # await ctx.reply(file=f2, embed=embed)
                # # print(imglink)
                # # embed=discord.Embed(title=p2.title, color=0x225588, description=wikicode, url=p2.url)
                # # embed.set_image(url=imglink)
                # # embed.set_footer(text='wikipedia results')
                # # await ctx.reply(embed=embed)
                    
                    
                # print("11")
            # else:
                # print("its album")
                # i2=0
                # found=0
                # if sch.lower()=="album":
                    # albidx=random.randint(0,len(albums))
                # else:
                    # for i in albtitle:
                        # if not found: print((sch)+'|'+(i)+'|'+(albums[i2]["name_j"])+'|'+str(albums[i2]["aliases"]))
                        # if not found:
                            # if i.lower()==sch.lower() or albums[i2]["name_j"]==sch.lower() or sch.lower() in [shit.lower() for shit in albums[i2]["aliases"]] and  found==0:
                                # print("hole sht")
                                # albidx=i2
                                # found=1
                        # i2+=1
                # print(albidx)
                # print(albums[albidx])
                # alb=albums[albidx]
                # with open('frien.png', 'wb') as f: 
                    # print(albums[albidx]["cover"])
                    # f.write(requests.get(alb["cover"]).content)
                # await asyncio.sleep(1)
                # with open('frien.png', 'rb') as f: 
                    # f2 = discord.File(f, filename='image.png')
                    # embed=discord.Embed(title=alb["name_j"], color=0x225588, description=pypandoc.convert_text(alb['desc'], 'markdown', format='mediawiki').replace(' "wikilink"','').replace('](','](http://japari-library.com/wiki/').replace('http://japari-library.com/wiki/https://japari-library.com/wiki/','https://japari-library.com/wiki/').replace('"','\\"').replace("\\'","'").replace('\r\n',' ').replace('  ',' ').replace('KemoNewline','\n'))
                    # embed.add_field(name='Track Listing',value='\n'.join(alb["tracks"]), inline=False)
                    # embed.add_field(name='Release Date',value=alb["date"], inline=True)
                    # embed.add_field(name='Length',value=alb["length"], inline=True)
                    # embed.add_field(name='Price',value=alb["price"], inline=True)
                    # embed.add_field(name='Catalog #',value=alb["catlog"], inline=True)
                    # embed.set_thumbnail(url="attachment://"+str('image.png'))
                    # embed.set_footer(text='Information from [Japari Library](https://japari-library.com/wiki/List_of_albums)')
                    # await ctx.reply(file=f2, embed=embed)
        # except DisambiguationError as e:
            # eror=traceback.format_exc()
            # embed=discord.Embed(title='Disambiguation', color=0x225588, description=e)
            # embed.set_footer(text='wikipedia results')
            # await ctx.reply(embed=embed)
        # except IndexError as e:
            # eror=traceback.format_exc()
            # embed=discord.Embed(title='Search', color=0x225588, description='No results found.'+eror)
            # embed.set_footer(text='wikipedia results')
            # await ctx.reply(embed=embed)
        # except Exception as e:
            # eror=traceback.format_exc()
            # embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
            # embed.set_footer(text='lmao')
            # await ctx.reply(embed=embed)
        await ctx.send('disabled because python sucks and broke my modules')

    @commands.command() #broken as of python update
    async def jwimg(self, ctx: commands.Context, *url_):
        # try:
            # print("4")
            # sch=" ".join(url_).title()
            # albums=get_data("albums")
            # albtitle=[]
            # for i in albums:
                # albtitle.append(i['name_e'].lower())
            # for i in albums:
                # albtitle.append(i['name_j'].lower())
            # for i in albums:
                # for i2 in i['aliases']:
                    # albtitle.append(i2.lower())
            # print(sch.lower())
            # if sch.lower()=="album" or sch.lower()=="album ":
                # albtitle.append(sch.lower())
                # print('coolio')
            # if sch.lower() not in albtitle:
                # if sch=="" or sch==" ": sch="friend"
                # if sch is not "All" and sch.lower() is not "friend":
                    # p = wikipedia.search(sch)
                    # if 'Anime' in p[0] and 'anime' not in sch.lower():
                        # print('found greasy anime fan')
                        # print(p[0])
                        # p.pop(0)
                        # print(p[0])
                    # print("5")
                    # shat=0
                    # try:
                        # print(sch)
                        # p2 = wikipedia.page(title=sch, auto_suggest=False)
                        # print("Yee-Haw!")
                    # except:
                        # shat=1
                        # print("Gets Shot")
                        # try:
                            # p2 = wikipedia.page(p[0])
                        # except IndexError:
                            # p = wikipedia.prefixsearch(sch)
                            # p2 = wikipedia.page(p[0])
                    # print('shat? '+str(shat)+'.')
                    # if not shat: 
                        # p2=wikipedia.page(title=sch, auto_suggest=False)
                    # thisshitsucks=0
                    # if 'anime' in p[0].lower():
                        # print('shoebill')
                        # if 'anime' not in sch.lower():
                            # print(p)
                            # print(p[1])
                            # print('sex')
                            # thisshitsucks=1
                            # print(p2)
                            # print(wikipedia.page(p[1]))
                    # if thisshitsucks: p2 = wikipedia.page(p[1])
                # if sch=='' or sch==' ' or sch.lower()=="friend" or sch.lower()=="all" or sch.lower() in ['fox','foxes','cat','cats','felid','felines','feline','wolf','wolves','bird','birds','song','songs','album','albums']:
                    # if sch=='' or sch==' ' or sch.lower()=="friend":
                        # goodmembers=wikipedia.categorymembers('Friends', results=None, subcategories=False)
                        # badmembers=wikipedia.categorymembers('Anime Friends', results=None, subcategories=False)
                        # members=[]
                        # for i in goodmembers:
                            # print(i)
                            # if i not in badmembers:
                                # members.append(i)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="song" or sch.lower()=="songs":
                        # members=wikipedia.categorymembers('Songs', results=None, subcategories=False)
                        # print(members)
                        # if type(members) is tuple:
                            # members=members[0]
                        # print(members)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="fox" or sch.lower()=="foxes":
                        # goodmembers=wikipedia.categorymembers('Fox Friends', results=None, subcategories=False)
                        # badmembers=wikipedia.categorymembers('Anime Friends', results=None, subcategories=False)
                        # members=[]
                        # for i in goodmembers:
                            # print(i)
                            # if i not in badmembers:
                                # members.append(i)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="bird" or sch.lower()=="birds":
                        # goodmembers=wikipedia.categorymembers('Bird Friends', results=None, subcategories=False)
                        # badmembers=wikipedia.categorymembers('Anime Friends', results=None, subcategories=False)
                        # members=[]
                        # for i in goodmembers:
                            # print(i)
                            # if i not in badmembers:
                                # members.append(i)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="canid" or sch.lower()=="canine":
                        # goodmembers=wikipedia.categorymembers('Canid Friends', results=None, subcategories=False)
                        # badmembers=wikipedia.categorymembers('Anime Friends', results=None, subcategories=False)
                        # members=[]
                        # for i in goodmembers:
                            # print(i)
                            # if i not in badmembers:
                                # members.append(i)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="wolf" or sch.lower()=="wolves":
                        # goodmembers=wikipedia.categorymembers('Wolf Friends', results=None, subcategories=False)
                        # badmembers=wikipedia.categorymembers('Anime Friends', results=None, subcategories=False)
                        # members=[]
                        # for i in goodmembers:
                            # print(i)
                            # if i not in badmembers:
                                # members.append(i)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="felid" or sch.lower()=="feline" or sch.lower()=="felines" or sch.lower()=="cats" or sch.lower()=="cat":
                        # goodmembers=wikipedia.categorymembers('Felid Friends', results=None, subcategories=False)
                        # badmembers=wikipedia.categorymembers('Anime Friends', results=None, subcategories=False)
                        # members=[]
                        # for i in goodmembers:
                            # print(i)
                            # if i not in badmembers:
                                # members.append(i)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="album" or sch.lower()=="albums":
                        # members=wikipedia.categorymembers('Albums', results=None, subcategories=False)
                        # print(members)
                        # if type(members) is tuple:
                            # members=members[0]
                        # print(members)
                        # p2=wikipedia.page(random.choice(members))
                    # if sch.lower()=="all":
                        # p2=wikipedia.page(wikipedia.random())
                # print("6")
                # htm=p2.html
                # sd=htm.split('\n')
                # print("7")
                # imgss=p2.images
                # print("8")
                # imglink='http://example.com'
                # for i in sd:
                    # if 'img' in i:
                        # print(i)
                        # kindaimg=i
                        # break
                # print("9")
                # for i in imgss:
                    # q=i[-16:]
                    # if q in kindaimg:
                        # print(q)
                        # imglink=i
                        # break
                # for i in sd:
                    # if i.startswith('<p>') and 'img' not in i:
                        # print(i)
                        # wikitext=i
                        # break
                # h = html2text.HTML2Text()
                # h.ignore_links = True
                # h.ignore_images = True
                # wikicode=h.handle(wikitext).replace('\r',' ').replace('\n',' ').replace('  ',' ')
                # print("10")
                # with open('frien.png', 'wb') as f: 
                    # f.write(requests.get(imglink).content)
                # with open('frien.png', 'rb') as f: 
                    # f2 = discord.File(f, filename='image.png')
                    # embed=discord.Embed(title=p2.title, color=0x225588, url=p2.url)
                    # embed.set_image(url="attachment://"+str('image.png'))
                    # #embed.set_footer(text='wikipedia results')
                    # print(p2.categories)
                    # if 'Friends' in p2.categories:
                        # nam='Empty'
                        # appear='Empty'
                        # scientific='Empty'
                        # dist='Empty'
                        # conservation='Empty'
                        # wikipedia_article='Empty'
                        # nam=thor('Japanese Name',sd,h)
                        # synonyms=get_data("friend_japanese_names")
                        # hasit=0
                        # for i in synonyms:
                            # if i[0]==nam:
                                # haskanji=1
                                # hasit=1
                                # kanji=i[1]
                                # trans=i[2]
                                # if kanji=="NoKanji": haskanji=0
                        
                        # if hasit and haskanji: nam+="/"+kanji
                        # nam+="\n*"+thor('Romanised Name',sd,h)+'*'
                        # if hasit: nam+='/*'+trans+'*'
                        # #nam+="\n*"+thor('Romanised Name',sd,h)+'*'
                        # appear=thor('Also known as',sd,h)
                        # scientific=thor('Scientific Name',sd,h)
                        # dist=thor('Distribution',sd,h)
                        # wikipedia_article=thor('Read More',sd,h)
                        # if 'Status iucn3.1 LC' in htm:
                            # conservation='Least Concern'
                        # if 'Status iucn3.1 NT' in htm:
                            # conservation='Near Threatened'
                        # if 'Status iucn3.1 VU' in htm:
                            # conservation='Vulnerable'
                        # if 'Status iucn3.1 EN' in htm:
                            # conservation='Endangered'
                        # if 'Status iucn3.1 CR' in htm:
                            # conservation='Critically Endangered'
                        # if 'Status iucn3.1 EW' in htm:
                            # conservation='Extinct In Wild'
                        # if 'Status iucn3.1 EX' in htm:
                            # conservation='Extinct'
                        # if 'Uma_label' in htm:
                            # conservation='Unidentified Mysterious Animal'
                        # print(nam)
                        # print(appear)
                        # print(scientific)
                        # print(dist)
                        # print(conservation)
                        # #embed.add_field(name='Japanese Name',value=nam, inline=True)
                        # #embed.add_field(name='Other Names',value=appear, inline=True)
                        # #embed.add_field(name='Scientific Name',value=scientific, inline=True)
                        # #embed.add_field(name='Distribution',value=dist, inline=True)
                        # #embed.add_field(name='IUCN',value=conservation, inline=True)
                        # #embed.add_field(name='Wikipedia',value=wikipedia_article, inline=True)
                    
                    # if 'Albums' in p2.categories:
                        # embed=discord.Embed(title=p2.title, color=0x225588, description='Test')
                        # album=get_data("albums")[0]
                        # #embed.add_field(name='Japanese Name',value=nam, inline=True)
                        # #embed.add_field(name='Other Names',value=appear, inline=True)
                        # #embed.add_field(name='Scientific Name',value=scientific, inline=True)
                        # #embed.add_field(name='Distribution',value=dist, inline=True)
                        # #embed.add_field(name='IUCN',value=conservation, inline=True)
                        # #embed.add_field(name='Wikipedia',value=wikipedia_article, inline=True)
                    
                    # await ctx.reply(file=f2, embed=embed)
                # # print(imglink)
                # # embed=discord.Embed(title=p2.title, color=0x225588, description=wikicode, url=p2.url)
                # # embed.set_image(url=imglink)
                # # embed.set_footer(text='wikipedia results')
                # # await ctx.reply(embed=embed)
                    
                    
                # print("11")
            # else:
                # print("its album")
                # i2=0
                # found=0
                # if sch.lower()=="album":
                    # albidx=random.randint(0,len(albums))
                # else:
                    # for i in albtitle:
                        # if not found: print((sch)+'|'+(i)+'|'+(albums[i2]["name_j"])+'|'+str(albums[i2]["aliases"]))
                        # if not found:
                            # if i.lower()==sch.lower() or albums[i2]["name_j"]==sch.lower() or sch.lower() in [shit.lower() for shit in albums[i2]["aliases"]] and  found==0:
                                # print("hole sht")
                                # albidx=i2
                                # found=1
                        # i2+=1
                # print(albidx)
                # print(albums[albidx])
                # alb=albums[albidx]
                # with open('frien.png', 'wb') as f: 
                    # print(albums[albidx]["cover"])
                    # f.write(requests.get(alb["cover"]).content)
                # await asyncio.sleep(1)
                # with open('frien.png', 'rb') as f: 
                    # f2 = discord.File(f, filename='image.png')
                    # embed=discord.Embed(title=alb["name_j"], color=0x225588, description=pypandoc.convert_text(alb['desc'], 'markdown', format='mediawiki').replace(' "wikilink"','').replace('](','](http://japari-library.com/wiki/').replace('http://japari-library.com/wiki/https://japari-library.com/wiki/','https://japari-library.com/wiki/').replace('"','\\"').replace("\\'","'").replace('\r\n',' ').replace('  ',' ').replace('KemoNewline','\n'))
                    # #embed.add_field(name='Track Listing',value='\n'.join(alb["tracks"]), inline=False)
                    # #embed.add_field(name='Release Date',value=alb["date"], inline=True)
                    # #embed.add_field(name='Length',value=alb["length"], inline=True)
                    # #embed.add_field(name='Price',value=alb["price"], inline=True)
                    # #embed.add_field(name='Catalog #',value=alb["catlog"], inline=True)
                    # embed.set_thumbnail(url="attachment://"+str('image.png'))
                    # embed.set_footer(text='Information from [Japari Library](https://japari-library.com/wiki/List_of_albums)')
                    # await ctx.reply(file=f2, embed=embed)
        # except DisambiguationError as e:
            # eror=traceback.format_exc()
            # embed=discord.Embed(title='Disambiguation', color=0x225588, description=e)
            # embed.set_footer(text='wikipedia results')
            # await ctx.reply(embed=embed)
        # except IndexError as e:
            # eror=traceback.format_exc()
            # embed=discord.Embed(title='Search', color=0x225588, description='No results found.'+eror)
            # embed.set_footer(text='wikipedia results')
            # await ctx.reply(embed=embed)
        # except Exception as e:
            # eror=traceback.format_exc()
            # embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
            # embed.set_footer(text='lmao')
            # await ctx.reply(embed=embed)
        await ctx.send('disabled because python sucks and broke my modules')

    @commands.command() #broken as of python update
    async def wiki(self, ctx = commands.Context, *url_):
        # try:
            # print("4")
            # sch=" ".join(url_)
            # p = wikiped.search(sch)
            # print("5")
            # print(p)
            # p2 = wikiped.page(p[0])
            # thisshitsucks=0
            # if 'anime' in p[0].lower():
                # print('shoebill')
                # if 'anime' not in sch.lower():
                    # print(p)
                    # print(p[1])
                    # print('sex')
                    # thisshitsucks=1
                    # print(p2)
                    # print(wikiped.page(p[1]))
            # if thisshitsucks: p2 = wikiped.page(p[1])
            # print("6")
            # sd=p2.html.split('\n')
            # print("7")
            # imgss=p2.images
            # print("8")
            # imglink='http://example.com'
            # for i in sd:
                # if 'img' in i:
                    # print(i)
                    # kindaimg=i
                    # break
            # print("9")
            # for i in imgss:
                # q=i[-16:]
                # if q in kindaimg:
                    # print(q)
                    # imglink=i
                    # break
            # for i in sd:
                # if i.startswith('<p>') and 'img' not in i:
                    # print(i)
                    # wikitext=i
                    # break
            # h = html2text.HTML2Text()
            # h.ignore_links = True
            # h.ignore_images = True
            # wikicode=h.handle(wikitext).replace('\r',' ').replace('\n',' ').replace('  ',' ')
            # #wikicode=p2.summary
            # print("10")
            # print(p2.images)
            
            # fart=[]
            # sfw=1
            # fnfn='http://png'
            # fnext='png'
            # for i in words:
                # if i in p2.content:
                    # print("found word "+i)
                    # sfw=0
            # shoot=""
            # try:
                # shart=p2.logos
                # for i in shart:
                    # if i[-3:]=='png' or i[-3:]=='jpg' or i[-3:]=='peg' or i[-3:]=='gif':
                        # fnfn=i
                        # fnext=i[-3:]
                        # shoot=i
                        # if fnext=='peg': fnext='jpeg'
                        # break
                # print(fnfn)
                # print(fnext)
            # except Exception as e:
                # print(e)
                # shart=p2.images
                # for i in shart:
                    # if i[-3:]=='png' or i[-3:]=='jpg' or i[-3:]=='peg' or i[-3:]=='gif':
                        # fnfn=i
                        # fnext=i[-3:]
                        # shoot=i
                        # if fnext=='peg': fnext='jpeg'
                        # break
                # print(fnfn)
                # print(fnext)
            # try:
                # with open('frien.'+fnext, 'wb') as f: 
                    # #f.write(requests.get(imglink).content)
                    # yeah=requests.get(fnfn).content
                    # await asyncio.sleep(1)
                    # f.write(yeah)
                    
            # except:
                # sfw=0
            # # with open('frien.'+fnext, 'rb') as f: 
                # # if sfw: f2 = discord.File(f, filename='image.'+fnext)
                # # embed=discord.Embed(title=p2.title, color=0x225588, description=wikicode, url=p2.url)
                # # #if sfw: embed.set_image(url="attachment://"+str('image.'+fnext))
                # # if sfw: embed.set_image(url=i)
                # # embed.set_footer(text='wikipedia results')
                # # if sfw: await ctx.reply(file=f2, embed=embed)
                # # if not sfw: await ctx.reply( embed=embed)
                
            # embed=discord.Embed(title=p2.title, color=0x225588, description=wikicode, url=p2.url)
            # if sfw and i is not 'erotic': embed.set_image(url=i)
            # embed.set_footer(text='wikipedia results')
            # if sfw: await ctx.reply(embed=embed)
            # if not sfw: await ctx.reply(embed=embed)
            # print("11")
        # except DisambiguationError as e:
            # eror=traceback.format_exc()
            # embed=discord.Embed(title='Disambiguation', color=0x225588, description=e)
            # embed.set_footer(text='wikipedia results')
            # await ctx.reply(embed=embed)
        # except Exception as e:
            # eror=traceback.format_exc()
            # embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
            # embed.set_footer(text='lmao')
            # await ctx.reply(embed=embed)
        await ctx.send('disabled because python sucks and broke my modules')

    @commands.command(aliases=['mario']) #broken as of python update
    async def mariowiki(self, ctx = commands.Context, *url_):
        # try:
            # print("4")
            # sch=" ".join(url_)
            # p = mario.search(sch)
            # print("5")
            # print(p)
            # p2 = mario.page(p[0])
            # thisshitsucks=0
            # imglink='http://example.com'
            # if 'anime' in p[0].lower():
                # print('shoebill')
                # if 'anime' not in sch.lower():
                    # print(p)
                    # print(p[1])
                    # print('sex')
                    # thisshitsucks=1
                    # print(p2)
                    # print(mario.page(p[1]))
            # if thisshitsucks: p2 = mario.page(p[1])
            # print("6")
            # sd=p2.html.split('\n')
            # print("7")
            # imgss=p2.images
            # print("8")
            # for i in sd:
                # if 'img' in i:
                    # print(i)
                    # kindaimg=i
                    # break
            # print("9")
            # for i in imgss:
                # q=i[-16:]
                # if q in kindaimg:
                    # print(q)
                    # imglink=i
                    # break
            # for i in sd:
                # if i.startswith('<p>') and 'img' not in i:
                    # print(i)
                    # wikitext=i
                    # break
            # h = html2text.HTML2Text()
            # h.ignore_links = True
            # h.ignore_images = True
            # wikicode=h.handle(wikitext).replace('\r',' ').replace('\n',' ').replace('  ',' ')
            # print("10")
            # with open('frien.png', 'wb') as f: 
                # f.write(requests.get(imglink).content)
            # print('decs and imgmdfgkasdgkdaflka leg dksjfhsdjuifidfsgbgfd')
            # print(len(wikicode))
            # print(len(imglink))
            # embed=discord.Embed(title=p2.title, color=0x225588, description=wikicode, url=imglink)#p2.url)
            # embed.set_image(url=imglink)#"attachment://"+str('image.png'))
            # embed.set_footer(text='wikipedia results')
            # await ctx.reply(embed=embed)
            # print("11")
        # except DisambiguationError as e:
            # eror=traceback.format_exc()
            # embed=discord.Embed(title='Disambiguation', color=0x225588, description=e)
            # embed.set_footer(text='wikipedia results')
            # await ctx.reply(embed=embed)
        # except Exception as e:
            # eror=traceback.format_exc()
            # embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
            # embed.set_footer(text='lmao')
            # await ctx.reply(embed=embed)
        await ctx.send('disabled because python sucks and broke my modules')

    @commands.command() #broken as of python update
    async def define(self, ctx = commands.Context, *url_):
        # wikia = wikt
        # print("4")
        # sch=" ".join(url_)
        # p = wikia.search(sch)
        # print("5")
        # print(p)
        # p2 = wikia.page(p[0])
        # thisshitsucks=0
        # if 'anime' in p[0].lower():
            # print('shoebill')
            # if 'anime' not in sch.lower():
                # print(p)
                # print(p[1])
                # print('sex')
                # thisshitsucks=1
                # print(p2)
                # print(wikia.page(p[1]))
        # if thisshitsucks: p2 = wikia.page(p[1])
        # print("6")
        # sd=p2.html.split('\n')
        # print("7")
        # imgss=p2.images
        # print("8")
        # imglink='http://example.com'
        # for i in sd:
            # if 'img' in i:
                # print(i)
                # kindaimg=i
                # break
        # print("9")
        # for i in imgss:
            # q=i[-16:]
            # if q in kindaimg:
                # print(q)
                # imglink=i
                # break
        # for i in sd:
            # if i.startswith('<p>') and 'img' not in i:
                # print(i)
                # wikitext=i
                # break
        # h = html2text.HTML2Text()
        # h.ignore_links = True
        # h.ignore_images = True
        # wikicode=h.handle(wikitext).replace('\r',' ').replace('\n',' ').replace('  ',' ')
        # #wikicode=p2.section('English')
        # print("10")
        # with open('frien.png', 'wb') as f: 
            # f.write(requests.get(imglink).content)
        # with open('frien.png', 'rb') as f: 
            # f2 = discord.File(f, filename='image.png')
            # embed=discord.Embed(title=p2.title, color=0x225588, description=wikicode, url=p2.url)
            # embed.set_image(url="attachment://"+str('image.png'))
            # embed.set_footer(text='wikipedia results')
            # await ctx.reply(file=f2, embed=embed)
        # print("11")
        await ctx.send('disabled because python sucks and broke my modules')

    @commands.command(aliases=["wc",'WC']) #wordcloud bc NOT SOBOT
    async def cloud(self, ctx=commands.Context,limit=50):
        try:
            allmsg=[]
            channel = ctx.message.channel
            async for msg in channel.history(limit = limit):
                if msg.content:
                    if not msg.content.startswith('.') and not msg.content.startswith('d.'):
                        if 'http' not in msg.content: #replace this wirh a url deleter
                            aa=str(msg.content)+" "
                            ab=""
                            for i in aa:
                                if i not in ['0','1','2','3','4','5','6','7','8','9','!','.',',','?','_','-','#','@','<','>',':',';']: ab+=i
                            allmsg+=ab
            with open('msg.txt','w',encoding='UTF-8') as f:
                f.writelines((allmsg))
        # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
        #  d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

            # Read the whole text.
            text = open(('msg.txt'),encoding='UTF-8').read()

            # Generate a word cloud image
            e='PENIS'
            wordcloud=None
            while wordcloud is None:
                try:
                    fnt=random.choice(os.listdir('C:\\Windows\\Fonts\\'))
                    print(fnt)
            
                    wordcloud = WordCloud(font_path='C:\\Windows\\Fonts\\'+fnt, width=800, height=400, max_font_size=80,max_words=10000,min_font_size=4).generate_from_frequencies(getFrequencyDictForText(text))
                    
                except Exception as e:
                    print(e)
            
            # Display the generated image:
            # the matplotlib way:
            

            # lower max_font_size
            #wordcloud = WordCloud(max_font_size=80,max_words=10000,min_font_size=1,relative_scaling=1).generate(text)
            
            # The pil way (if you don't have matplotlib)
            image = wordcloud.to_image()
            image.save('wc.png')
            await ctx.send(file=File('wc.png'))
        except Exception as e:
        # except Exception as e:
            eror=traceback.format_exc()
            embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
            embed.set_footer(text='lmao')
            await ctx.reply(embed=embed)



    @commands.command()
    async def vc1(self, ctx=commands.Context, *friend):
        channel=self.bot.get_channel(1068002130977370153)
        await channel.edit(name=" ".join(friend[:]))

    @commands.command()
    async def vc2(self, ctx=commands.Context, *friend):
        channel=self.bot.get_channel(1070548432135127110)
        await channel.edit(name=" ".join(friend[:]))
        
    @commands.command()
    async def vc3(self, ctx=commands.Context, *friend):
        channel=self.bot.get_channel(1068002110551105557)
        await channel.edit(name=" ".join(friend[:]))

    @commands.command()
    async def status(self, ctx=commands.Context):
        hydrusip="http://127.0.0.1:45869"
        hykey="f409b6bfe0098430722f8f8813a43af066f862589947236cbee9bfdaae932c74"
        headers={'Hydrus-Client-API-Access-Key': hykey}
        hydrus=requests.get(hydrusip, headers=headers)
        stattus="Bot Status:\nBot: Idk you tell me\n"
        stattus+="Hydrus: "+str(hydrus)+"\n"
        with open("status.txt") as fartstatus:
            stattus+="\nLast Ping:\n"+("".join(fartstatus.readlines()))
        await ctx.send(stattus)

    @commands.command()
    async def filelink(self, ctx=commands.Context):
        print('test')
        await ctx.send(ctx.message.attachments[0].url)
        
    @commands.command() #dannybot wrote this not me
    async def dothemario(self, ctx=commands.Context):
        await ctx.send("Alright, let's do the Mario!")
    
        # Create an array of Mario moves
        marioMoves = ['Jump!', 'Jump and spin!', 'Jump and kick!', 'Jump and punch!', 'Jump and slide!', 'Jump and do the Mario!']
        
        # Iterate over the array and send each move
        for move in marioMoves:
            await ctx.send(move)
            
        # Let the user know the Mario is complete
        await ctx.send('Woohoo! The Mario is complete!')

    @commands.command() #get the link to a file given the id of a message -- this is used to copy links to audio files on mobile
    async def msglink(self, ctx=commands.Context, msgID=None):
        print('test')
        msg=await ctx.fetch_message(msgID)
        await ctx.send(msg.attachments[0].url)

    @commands.command() #Change the bots nickname
    async def nick(self, ctx=commands.Context, *nic):
        await self.bot.user.edit(nick=" ".join(nic))

    
    @commands.command() #see my drives die of  overprofisioning idk
    async def info(self, ctx=commands.Context):
        c = wmi.WMI ()
        def add_drive(stn, drv, stgname,type):
            try:
                global embed
                disk1=psutil.disk_usage(drv+":/")
                total=(disk1.total >> 20)/1000
                available=(disk1.free >> 20)/1000
                perc=(disk1.percent)
                embed.add_field(name=stgname, value=type+'\n'+str(round(available,2))+" GB free out of "+str(round(total,2))+"GB ("+str(perc)+"% used)", inline=True)
            except OSError:
                pass
        global embed
        GPUs = GPUtil.getGPUs()
        load = GPUs[0].load
        upt=datetime.datetime.fromtimestamp(time.time()-psutil.boot_time()+(5*60*60))
        ut="PC Uptime: "
        if (upt.year-1970)>0:ut=ut+str(upt.year-1970)+" years, "
        if (upt.month-1)>0:ut=ut+str(upt.month-1)+" months, "
        if (upt.day-1)>0:ut=ut+str(upt.day-1)+" days, "
        if (upt.hour)>0:ut=ut+str(upt.hour)+" hours, "
        if (upt.minute)>0:ut=ut+str(upt.minute)+" minutes, "
        if (upt.second)>0:ut=ut+str(upt.second)+" seconds. "
        embed=discord.Embed(title=platform.platform(), description=ut)
        embed.add_field(name="CPU", value="AMD Ryzen 5 2600"+"\n"+str(psutil.cpu_percent())+"%", inline=True)
        embed.add_field(name="GPU", value="EVGA GeForce RTX 3060 12GB\n"+str(load*100)+"%", inline=True)
        values = psutil.virtual_memory()
        total=(values.total >> 20)/1024
        available=(values.available >> 20)/1024
        use=round(total-available,2)
        tot=round(total,2)
        embed.add_field(name="RAM", value="4x8GB Corsair Vengeance DDR4 @ 2300MHz"+"\n"+str(use)+"/32GB", inline=True)
        total2=0
        available2=0
        drive_i=1
        DriveInfos=get_data('drive_infos')
        for drive in c.Win32_LogicalDisk ():
            for info_i in DriveInfos:
                if info_i[0]==drive.VolumeSerialNumber: #Serial
                    drvhw=info_i[1] #Hardware
                    drvpp=info_i[2] #Purpose
            if drvhw!='IGNORE': #Some Hardware and Purpose keys are set to "IGNORE" to avoid showing unneccessary 8MB system volumes
                try:
                    add_drive(drive_i, drive.Name[0],drive.VolumeName+' ('+drive.Name+')',''+drvhw+'\n*'+drvpp+'*')
                except:
                    pass
            drive_i+=1
        #add_drive(1, "C","WD SN750 NVMe 500GB")
        #add_drive(2, "D","5400RPM HDD 160GB")
        #add_drive(3, "F","Old Lenovo HDD")
        #add_drive(4, "G","USB 16GB")
        #add_drive(5, "H","Samsung 860 EVO SSD 1TB")
        #add_drive(6, "R","RamDisk 250MB")
        #add_drive(7, "J","Old PC HDD 2TB")
        #add_drive(8, "K","Old External 1TB")
        #add_drive(9, "L","Old External Partition 100GB")
        #add_drive(10, "M","Old External Partition 20GB")
        #add_drive(11, "W","Seagate Barracuda 2TB")
        #add_drive(59, "Fortnite","Invalid drive test")
        embed.set_footer(text="Stable PC")
        await ctx.send(embed=embed)

    @commands.command() #i used this to create "poo ping" in the night of nights ytpmv
    async def delayed_ping_effect(self, ctx=commands.Context):
        await asyncio.sleep(10)
        await ctx.send('<@'+str(ctx.author.id)+'>')

    @commands.command()
    async def userinfo(self, ctx=commands.Context, user_='me'): #verbose user info command
        guild=ctx.guild
        try:
            user=ctx.message.mentions[0]
        except:
            pass
        if user_=='me':
            user=ctx.message.author
        if str(int(user_))==user_:
            user=await guild.fetch_member(user_)
        desc=''
        lst=[]
        lst.append('**joined_at**: '+str(user.joined_at))
        lst.append('**activities**: '+str(user.activities))
        lst.append('**guild**: '+str(user.guild))
        lst.append('**nick**: '+str(user.nick))
        lst.append('**pending**: '+str(user.pending))
        lst.append('**premium_since**: '+str(user.premium_since))
        lst.append('**raw_status**: '+str(user.raw_status))
        lst.append('**status**: '+str(user.status))
        lst.append('**mobile_status**: '+str(user.mobile_status))
        lst.append('**desktop_status**: '+str(user.desktop_status))
        lst.append('**web_status**: '+str(user.web_status))
        lst.append('**is_on_mobile()**: '+str(user.is_on_mobile()))
        lst.append('**colour**: '+str(user.colour))
        lst.append('**roles**: '+str(user.roles))
        lst.append('**mention**: '+str(user))
        lst.append('**display_name**: '+str(user.display_name))
        lst.append('**activity**: '+str(user.activity))
        lst.append('**top_role**: '+str(user.top_role))
        lst.append('**guild_permissions**: '+str(user.guild_permissions))
        lst.append('**voice**: '+str(user.voice))
        lst.append('**bot**: '+str(user.bot))
        lst.append('**system**: '+str(user.system))
        lst.append('**id**: '+str(user.id))
        lst.append('**discriminator**: '+str(user.discriminator))
        lst.append('**mutual_guilds**: '+str(user.mutual_guilds))
        lst.append('**dm_channel**: '+str(user.dm_channel))
        lst.append('**default_avatar_url**: '+str(user.default_avatar_url))
        lst.append('**is_avatar_animated()**: '+str(user.is_avatar_animated()))
        lst.append('**public_flags**: '+str(user.public_flags))
        
        desc='\n'.join(lst)
        
        embed=discord.Embed(title=user.display_name, description=desc,color=user.colour)
        
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def browse(self, ctx=commands.Context, *dirt_): #oh
        dirt=" ".join(dirt_)
        directory='L:\\'+dirt
        dr=os.listdir(directory)
        goo=('\n    '.join(dr))[:1900]
        await ctx.send('Directory of '+directory+': \n    '+goo)

    @commands.command()
    async def speed(self,ctx=commands.Context): #frontier sux
        servers = []
        threads = None
        await ctx.send("Be warned: It's Garbage:tm:")
        s = speedtest.Speedtest()
        print("downtest")
        dn=s.download(threads=threads)
        print("uptest")
        up=s.upload(threads=threads)
        print("done")
        results_dict = s.results.dict()
        print(results_dict)
        embed=discord.Embed(title="Speedtest results", description="ISP: "+results_dict["client"]["isp"]+"("+results_dict["client"]["isprating"]+"/5)\nSERVER: "+results_dict["server"]["name"]+" ("+results_dict["server"]["sponsor"]+")")
        embed.add_field(name="Ping", value=str(round(results_dict["ping"]))+"ms", inline=True)
        embed.add_field(name="Download", value=str(round(results_dict["download"]/1000000,2))+"mbps", inline=True)
        embed.add_field(name="Upload", value=str(round(results_dict["upload"]/1000000,2))+"mbps", inline=True)
        embed.set_footer(text="haha look thats slow haha ah ha ha ha hha ha ha ha hah ah ha ha h ah h aha hh ah ah aha ha h ha at least the ping and download are usable")
        await ctx.send(embed=embed)

    @commands.command()
    async def lb_old(self,ctx=commands.Context, id=0): #was med deprived
        with open('lb_good.json','r',encoding='utf-8') as f:
            file=json.load(f)
        i2=0
        #for i in file:
        if id==0:
            u=ctx.author.id
        else:
            u=id
        usa=await self.bot.fetch_member(u)
        try:
            i=file[str(u)]
        except:
            await ctx.send(usa.name+' has never used the bot!')
        #print(i['friend'])
        #await ctx.send('`'+str(i['friend'])[:1800]+'`')
        MPTA='NoTag'
        MPTB=0
        FCI=0
        try:
            FCI=file[str(u)]['friend'][0]
            for i2 in file[str(u)]['friend'][1]:
                print(i2)
                print(file[str(u)]['friend'][1][i2])
                if i['friend'][1][i2]>MPTB:
                    MPTA=i2
                    MPTB=file[str(u)]['friend'][1][i2]
        except:
            pass
        MPUA='NoTag'
        MPUB=0
        UCI=0
        try:
            UCI=i['upscale'][0]
            for i2 in i['upscale'][1]:
                print(i2)
                print(i['upscale'][1][i2])
                if i['upscale'][1][i2]>MPUB:
                    MPUA=i2
                    MPUB=i['upscale'][1][i2]
        except:
            pass

        FavComName='nocommand'
        FavComCont=0
        commandsissued=0
        for i2 in i:
            if i2 is not '':
                if i[i2][0]>FavComCont:
                    FavComName=i2
                    FavComCont=i[i2][0]
                commandsissued+=i[i2][0]
        WoahMama=int((UCI*9.6235453367)*10)/10
        embed=discord.Embed(title="Stats for "+usa.name, description='Friend Commands Issued: '+str(FCI)+'\n'+'Most Used Tag: '+MPTA+' ('+str(MPTB)+')'+'\n'+'Upscale Commands Issued: '+str(UCI)+' (~'+str(math.floor(WoahMama/60))+'m'+str(math.floor(WoahMama % 60))+'s of gpu time) \n'+'Most Used Model: '+MPUA+' ('+str(MPUB)+')'+'\n'+'Commands Issued: '+str(commandsissued)+'\n'+'Most Used Command: '+FavComName+' ('+str(FavComCont)+')')
        #await ctx.send()
        #await ctx.send()
        await ctx.send(embed=embed)

    @commands.command()
    async def lb(self,ctx=commands.Context, id='', cmd_=''): #no longer med deprived
        with open('lb_good.json','r',encoding='utf-8') as f:
            file=json.load(f)
        #                                                                                       {
        #tree structure: User_List[Member]                                                          "5684262457257": {
        #                                 [Command]                                                  |  "friend": [
        #                                          [0]: (Usage count of command)                     |      69,
        #                                          [1]: {"Argument": Argument usage count}           |      {"tag:serval": 39, "tag:caracal": 30}]
        #                                                                                            }
        #                                                                                       }
        
        #        try:
        #    FCI=file[str(u)]['friend'][0]
        #    for i2 in file[str(u)]['friend'][1]:
        #        print(i2)         #i forgot how i did this sorry lol
        #        print(file[str(u)]['friend'][1][i2])
        #        if file[str(u)]['friend'][1][i2]>MPTB:

        #        if User_List[Member][Command][Arguments][i2]>MPTB #over means its comparing numbers? 
        #                                                           OH [Arguments][i2] returns the friend tag, 
        #                                                           and since its a dict its like 
        #                                                           [Arguments]['serval'] which would return 1 if {"serval": 1}!!!!!!!!!!!!!!!!!!

        #            MPTA=i2
        #            MPTB=file[str(u)]['friend'][1][i2]

        #calculate total bot uses for a user for a command
        def calcUserBotUsageCommand(id,comm):
            comm_count=file[str(id)][comm][0] #element 0 of a command's tree is always the use count.
            return comm_count

        #calculate total bot uses for a user
        def calcUserBotUsage(id):
            for member in file:
                if member==str(id):
                    comms=file[member]
                    comm_count=0
                    for comm in comms:
                        if comm is not "":# a buggy element that somehow appeared? it counts commands and noncommands, i have no fucking clue how it couldve come to be OH OK I FUCKING MADE IT SPLIT [. FRIEND] INTO [.] FROM WHEN I WAS SPLITTING ARGUMENTS INTO [.CMD ARGUMENT] IT THOUGHT IT WAS [CMD (.)] [ARGUMENT (FRIEND FARTBAG)], because you cant send " .friend" in chat? and nobodys ever typed ". .friend?" and i have it set to exclude "..*" commands too (which it DID do) ???????????
                            comm_count+=comms[comm][0] #element 0 of a command's tree is always the use count.
            return comm_count

        #calculate total bot uses for a command
        def calcCommandBotUsage(comm):
            comm_count=0
            for member in file:
                try:
                    comm_count+=file[member][comm][0]
                except KeyError:
                    print('user did not have command')
                except TypeError:
                    print('???')
            return comm_count

        #calculate user who used most of command
        def calcCommandUserPref(comm):
            comm_count=0
            comm_user='Joe Schmoe'
            for member in file:
                try:
                    if file[member][comm][0]>comm_count:
                        comm_count=file[member][comm][0]
                        comm_user=member
                except KeyError:
                    print('user did not have command')
                except TypeError:
                    print('???')
            return {'user': comm_user, 'count': comm_count}

        #calculate arg used most for command
        def calcCommandArgPref(comm):
            comm_count=0
            comm_arg='balls'
            for member in file:
                try:
                    for arg in file[member][comm][1]:
                        #print(arg)
                        if file[member][comm][1][arg]>comm_count:
                            comm_count=file[member][comm][1][arg] #value of arg of file/member/comm/1
                            comm_arg=arg
                except KeyError:
                    print('user did not have command')
                except TypeError:
                    print('???')
            return {'arg': comm_arg, 'count': comm_count}

        #calculate most used command statistics for a user
        def calcUserCommandPref(id):
            comm_count=0
            comm_name='null'
            arg_count=0
            arg_name='null'
            for member in file:
                if member==str(id):
                    for comm in file[member]:
                        if file[member][comm][0]>comm_count:
                            comm_count=file[member][comm][0]
                            comm_name=comm
                    for arg in file[member][comm_name][1]:
                        if file[member][comm_name][1][arg]>arg_count:
                            if arg!='':
                                arg_count=file[member][comm_name][1][arg]
                                arg_name=arg
            return {
                'command': {
                     'name': comm_name, 
                    'count': comm_count
                    },
                'argument': {
                     'name': arg_name, 
                    'count': arg_count
                    }
                }

        #calculate most used arg statistics for a user's command
        def calcUserArgPref(id,comm_name):
            member=str(id)
            comm_count=file[member][comm_name][0]
            arg_count=0
            arg_name='null'
            for member in file:
                if member==str(id):
                    for arg in file[member][comm_name][1]:
                        if file[member][comm_name][1][arg]>arg_count:
                            if arg!='':
                                arg_count=file[member][comm_name][1][arg]
                                arg_name=arg
            return {
                'command': {
                     'name': comm_name, 
                    'count': comm_count
                    },
                'argument': {
                     'name': arg_name, 
                    'count': arg_count
                    }
                }



        AllMode=0
        MemberMode=1
        CommandMode=2 
        MemberCommandMode=3
        # ^^ just for readability
        mode=None
        try:
            int(id) #int(id) will error out if int has non-numbers in it...
            if cmd_=='':
                mode=MemberMode
            else:
                mode=MemberCommandMode
            print(mode)
        except ValueError: #...thus being a more clever method to detect whether a string is a number than "str(int(number))==str(number)"
            print('valueerrror lets go')
            if id=='': 
                mode=AllMode
                print(mode)
            else: 
                if cmd_=='':
                    mode=CommandMode
                else:
                    mode=MemberCommandMode
                print(mode)
        desc='Tests'
        if mode==MemberMode:

            desc+='\ncalcUserBotUsage(id): '+str(calcUserBotUsage(id))
            desc+='\ncalcUserCommandPref(id): '+str(calcUserCommandPref(id))
        if mode==CommandMode:
            desc+='\ncalcCommandBotUsage(id): '+str(calcCommandBotUsage(id))
            desc+='\ncalcCommandUserPref(id): '+str(calcCommandUserPref(id))
            desc+='\ncalcCommandArgPref(id): '+str(calcCommandArgPref(id))
        if mode==MemberCommandMode:
            desc+='\ncalcUserBotUsageCommand(id,"friend"): '+str(calcUserBotUsageCommand(id,cmd_))
            desc+='\ncalcUserArgPref(id,"friend"): '+str(calcUserArgPref(id,cmd_))
        embed=discord.Embed(title="Embed", description=desc)
        await ctx.send(embed=embed)
    #1106197404769849374
    @commands.command(aliases=['pa'])
    async def pruneafterrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr(self,ctx=commands.Context, msg_id=None): #multiple years and notsobot still hasnt added it so i did it myself in one morning
        deleted = await ctx.channel.purge(after=await ctx.fetch_message(msg_id),limit=50)
        successmsg=await ctx.send(f'Deleted {len(deleted)} message(s)')
        await asyncio.sleep(3)
        successmsg.delete()
        
        # def prune_checker(m):
            
            
                # return True
        # if msg_id==None:
            # await ctx.send('put a message id dipass')
        # else:
            # msg_id=int(msg_id)
            # #code here
            # await ctx.send('hi')
            # msgs_to_prune=[]
            # channel = ctx.message.channel
            # async for msg in channel.history(limit = 50):
                # if msg.id>=msg_id:
                    # msgs_to_prune.append(msg)
            # proceed_message=await ctx.send('found '+str(len(msgs_to_prune))+' messages.')
            # await asyncio.sleep(1)
            # #for msg in msgs_to_prune:
                # #await msg.delete()
                # #await ctx.send(str(msg.channel))
            # await 
            # await proceed_message.delete()
            # await ctx.message.delete()
            

    @commands.command()
    async def nick(self,ctx=commands.Context, *, fuck=''):
        await ctx.guild.me.edit(nick=fuck)

    #@commands.command()
    #async def upscale_stats(self,ctx=commands.Context, id=''): 
        #with open('lb_good.json','r',encoding='utf-8') as f:
            #file=json.load(f)
        #print('die')
        #fdjkiongadg ill finish this later
        
        #i will not finish this its been over one year

    @commands.command()
    async def modellist_dev(self,ctx=commands.Context): 
        #Fuck this by the way
    
        #Blart
        components = [ActionRow(Button(label='Option Nr.1',
                                   custom_id='option1',
                                   emoji="🆒",
                                   style=ButtonStyle.green
                                   ),
                            Button(label='Option Nr.2',
                                   custom_id='option2',
                                   emoji="🆗",
                                   style=ButtonStyle.blurple)),
                  ActionRow(Button(label='A Other Row',
                                   custom_id='sec_row_1st option',
                                   style=ButtonStyle.red,
                                   emoji='😀'),
                            Button(url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                                   label="This is an Link",
                                   style=ButtonStyle.url,
                                   emoji='🎬'))
                  ]
        an_embed = discord.Embed(title='Here are some Button\'s', description='Choose an option', color=discord.Color.random())
        msg = await ctx.send(embed=an_embed, components=components)

        def _check(i: discord.Interaction, b):
            return i.message == msg and i.member == ctx.author

        interaction, button = await client.wait_for('button_click', check=_check)
        button_id = button.custom_id

        # This sends the Discord-API that the interaction has been received and is being "processed"
        await interaction.defer()
        # if this is not used and you also do not edit the message within 3 seconds as described below,
        # Discord will indicate that the interaction has failed.

        # If you use interaction.edit instead of interaction.message.edit, you do not have to defer the interaction,
        # if your response does not last longer than 3 seconds.
        await interaction.edit(embed=an_embed.add_field(name='Choose', value=f'Your Choose was `{button_id}`'),
                            components=[components[0].disable_all_buttons(), components[1].disable_all_buttons()])

        # The Discord API doesn't send an event when you press a link button so we can't "receive" that.
    @commands.command()
    async def color(self, ctx=commands.Context, url=None): #Bravy wanted a command that gets the hex code of an image
        if(url is not None): #if its gay it means theres no link
            FileUrl=requests.get(url) #sets url to link
        else:
            FileUrl=requests.get(ctx.message.attachments[0].url) #sets url to attached
        fn='R:\\temp.png' #file name
        with open(fn, 'wb') as f: 
            f.write(FileUrl.content) #saves file
        #with Image.open("R:\\temp.png") as im:
        gay=Image.open("R:\\temp.png")
        w,h=gay.size
        img = gay.load()
        r_values=[]
        g_values=[]
        b_values=[]
        for y in range(h):
            for x in range(w):
                p=gay.getpixel((x,y))
                r_values.append(p[0])
                g_values.append(p[1])
                b_values.append(p[2])
        r=0
        g=0
        b=0
        for i in range(len(r_values)):
            r+=r_values[i]
            g+=g_values[i]
            b+=b_values[i]
        r=round(r/len(r_values))
        g=round(g/len(r_values))
        b=round(b/len(r_values))
        hex_code=f'{r:x}'.zfill(2)+f'{g:x}'.zfill(2)+f'{b:x}'.zfill(2)
        img=Image.new('RGB', (256, 256), (r,g,b))
        img.save('r:\\tmp.png')
        with open('r:\\tmp.png', 'rb') as f: 
            embed=discord.Embed(title='#'+hex_code, description="rgb("+str(r)+','+str(g)+','+str(b)+")", color=discord.Color.from_rgb(r,g,b))
            embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            f2 = discord.File(f, filename='image.png')
            embed.set_thumbnail(url="attachment://"+str('image.png'))
            embed.set_footer(text="Color detected by SilverGaming")
            await ctx.reply(hex_code,file=f2, embed=embed)
            
            
    @commands.command()
    async def grokmodels(self,ctx=commands.Context, *, fuck=''):
        mods=['anything','furry','model (this is sd 1.4)','sayori','appleq'] #this is out of date
        await ctx.send(',\n'.join(mods))
            
            
    @commands.command()
    async def groksampler(self,ctx=commands.Context, *, fuck=''): #this is derprecarded
        global sampler
        sampler=fuck
        await ctx.send('ok')
        
    #@commands.cooldown(4, 8, commands.BucketType.user)
    @commands.command()
    async def grok(self,ctx=commands.Context, *, fuck=''):
        #etymology of grok: grok (from "ngrok") - remote stable diffusion interface
        global grokReason
        passcode=str(generateUUID())*random.randint(3,13)
        global ungrok
        global ungrok_override
        def check(m):
            return m.content != 'agdfgadfgadfhadfhadfhfahf'
        def check2(m):
            return m.author.id==158418656861093888
        if fuck=='disable':
            if ctx.author.id==158418656861093888:
                await ctx.send('alright, enter the reason')
                jeep=await self.bot.wait_for('message', check=check2)
                grokReason=jeep.content
                ungrok=True
                await ctx.send('grokking disabled successfully')
                return
            else:
                if ctx.author.nick.lower()=='ezogaming':
                    await ctx.send('alright, enter the passcode')
                    await self.bot.wait_for('message', check=check)
                    await ctx.send('WRONG!!')
                return
        if fuck=='enable':
            if ctx.author.id==158418656861093888:
                await ctx.send('alright, enter the passcode')
                await self.bot.wait_for('message', check=check2)
                ungrok=False
                await ctx.send('grokking reabled successfully')
                return
            else:
                if ctx.author.nick.lower()=='ezogaming':
                    await ctx.send('alright, enter the passcode')
                    await self.bot.wait_for('message', check=check)
                    await ctx.send('WRONG!!')
                return
        if fuck=='unload':
            await ctx.send('unloading sd models')
            jerma=requests.post(url='http://127.0.0.1:7860/sdapi/v1/unload-checkpoint')
            if jerma.status_code==200: 
                await ctx.send('success')
            else:
                await ctx.send(str(jerma))
            return
        global grokqueue
        
        jerma=requests.get(url='http://127.0.0.1:7860/sdapi/v1/memory')
        #await ctx.send(str(jerma.json()))
        resp=jerma.json()
        GiB=1024**3
        cuda_ram_json=resp['cuda']
        
        GPUs = GPUtil.getGPUs()[0]
        #await ctx.send(str(GPUs))
        #await ctx.send(str(GPUs.memoryFree))
        free=round(GPUs.memoryFree/100)/10
        used=12-free
        total=12
        
        
        #free=round((cuda_ram_json['system']['free']/GiB)*10)/10
        #used=round((cuda_ram_json['system']['used']/GiB)*10)/10
        #total=round((cuda_ram_json['system']['total']/GiB)*10)/10
        
        
        #return
        
        
        if fuck=='vram':
            #await ctx.send('checking grok vram')
            await ctx.send(f'VRAM Used: {used}/{total} GB ({free} GB free)')
            return
            
        #if ungrok==True:
            #await ctx.send('grok is DISABLED (flashlight may be generating furries or training a lora)')
            #return
            
        if len(grokqueue)==0 and free<5.5:
            await ctx.send('[EXPERIMENTAL] Queue is fresh but VRAM is low, pausing grok')
            ungrok_override=True
            grokReason='Auto-disabled due to low VRAM'
            
        if ungrok==True or ungrok_override==True:
            await ctx.send(f'grok queued! grok will be grokked once grok is enabled (reason: {grokReason})\nVRAM Used: {used}/{total} GB ({free} GB free)')
            if free>6:
                if ungrok_override==True and ungrok==False:
                    await ctx.send('hey..... there is enough vram free and grok was NOT manually disabled....... time to reable grok')
                    ungrok_override=False
            
        #else:
        
        try:
            fgadgadg=fuck.split(' --neg')[1]
        except:
            fgadgadg=''
        global groktimer
        groktimer=time.time()+(60*5)
        grokqueue.append([ctx.channel,fuck.split(' --neg')[0],fgadgadg,-1,'anything',20,'Euler a','512x512',random.randrange(12,18)/2,'bypass' in fuck])
           #await ctx.send('COMMAND: '+str(grokqueue))\
        
            
        
    
    @commands.Cog.slash_command( #Someone wanted it as a slash command so i slashed out my eyes and made this
        description='generate ai images',
        options=[
            Option(
                name='prompt',
                description='Positive prompt for the image',
                option_type=str,
                required=False
            ),
            Option(
                name='negs',
                description='Negative prompt for the image',
                option_type=str,
                required=False
            ),
            Option(
                name='seed',
                description='Seed to generate the image with',
                option_type=int,
                required=False
            ),
            Option(
                name='model',
                description='Model to generate the image with',
                option_type=str,
                required=False
            ),
            Option(
                name='steps',
                description='Steps for the sampler',
                option_type=int,
                required=False
            ),
            Option(
                name='sampler',
                description='Sampler',
                option_type=str,
                required=False
            ),
            Option(
                name='resolution',
                description='Image resolution',
                option_type=str,
                required=False
            ),
            Option(
                name='cfg',
                description='CFG scale - higher is more wild and lower is more flat and desaturated',
                option_type=str,
                required=False
            ),
            Option(
                name='bypass',
                description='Bypass LoRAs and replacements',
                option_type=str,
                required=False
            )
        ]
    )
    async def grok2(self, ctx: APPCI, prompt: Optional[str] = "", negs: Optional[str] = "", seed: Optional[int] = -1, model: Optional[str] = "anything", steps: Optional[int] = 20, sampler: Optional[str] = "Euler a", resolution: Optional[str] = "512x512", cfg: Optional[str] = '6.5', bypass: Optional[str] = 'False'):
        await ctx.respond('processing '+prompt+'...')#,hidden=True)
        _cfg=float(cfg)
        _bypass=False
        if bypass.lower()=='true':
            _bypass=True
        global grokqueue
        grokqueue.append([ctx.channel,prompt,negs,seed,model,steps,sampler,resolution,_cfg,_bypass])
    
    
    @commands.command()
    async def iro(self, ctx=commands.Context): #pull up a random irodori character image
        dir='I:\\kftest2\\img\\1_kf1style kf1style\\'
        lis=[]
        for i in os.listdir(dir):
            if 'png' in i: lis.append(i)
        with open(dir+random.choice(lis), 'rb') as f:
            f2 = discord.File(f, filename='image.png')
            await ctx.send(file=f2)
            
            
            
    @commands.command()
    async def neko(self, ctx=commands.Context): #Nyan Neko Sugar Girls Screenshot
        dir='H:\\neko\\'
        lis=[]
        for i in os.listdir(dir):
            lis.append(i)
        with open(dir+random.choice(lis), 'rb') as f:
            f2 = discord.File(f, filename='image.png')
            await ctx.send(file=f2)
            
            
            
            
    @commands.command()
    async def danny(self, ctx=commands.Context): #Danny
        dir='I:\\dan2\\img\\16_danny danny\\'
        lis=[]
        for i in os.listdir(dir):
            if 'jp' in i: lis.append(i)
        with open(dir+random.choice(lis), 'rb') as f:
            f2 = discord.File(f, filename='image.png')
            await ctx.send(file=f2)
            
            
            
    @commands.command()
    async def projared(self, ctx=commands.Context): #Send a tiled collage of Projared with a wav2lip mouth
        files_to_read: list[str] = ['projar1.jpg','projar2.jpg','projar3.jpg','projar4.jpg']
        files_to_send: list[discord.File] = []
        for filename in files_to_read:
            with open(filename, 'rb') as f:  # discord file objects must be opened in binary and read mode
                files_to_send.append(discord.File(f))# discord file objects must be opened in binary and read mode
        await ctx.send(files=files_to_send)# discord file objects must be opened in binary and read mode
        # discord file objects must be opened in binary and read mode
        # discord file objects must be opened in binary and read model# discord file objects must be opened in binary and read mode
        # discord file objects must be opened in binary and read mode
        # discord file objects must be opened in binary and read mode# discord file objects must be opened in binary and read mode# discord file objects must be opened in binary and read mode# discord file objects must be opened in binary and read mode# discord file objects must be opened in binary and read mode# discord file objects must be opened in binary and read mode# discord file objects must be opened in binary and read mode# discord file objects must be opened in binary and read mode
        
    @commands.command()
    async def loss(self, ctx=commands.Context): #I II II L
        files_to_read: list[str] = ['loss1.jpg','loss2.jpg','loss3.jpg','loss4.jpg']
        files_to_send: list[discord.File] = []
        for filename in files_to_read:
            with open(filename, 'rb') as f:  # discord file objects must be opened in binary and read mode
                files_to_send.append(discord.File(f))
        await ctx.send(files=files_to_send)
            
    @commands.command()
    async def thumbnail(self, ctx=commands.Context, *, fuck=''): #pull youtube thumbnail
        if '.be' in fuck:
            q=fuck.split('.be/')[1]
        else:
            q=fuck.split('watch?v=')[1]
        q=q.split('&')[0]
        #await ctx.send(q)
        url='https://i3.ytimg.com/vi/'+q+'/maxresdefault.jpg'
        r=requests.get(url).content
        with open('thumbnail.jpg','wb') as f:
            f.write(r)
        #await ctx.send('`'+url+'`')
        with open('thumbnail.jpg','rb') as f:
            await ctx.send(file=discord.File(f, filename='image.png'))
            
    @commands.command()
    async def sam(self, ctx=commands.Context, *, fuck=''): #moonbase alpha tts
        os.system('sam '+fuck+' -wav output.wav')
        with open('output.wav','rb') as f:
            await ctx.send(file=discord.File(f, filename='sam.wav'))
            
            
    @commands.command()
    async def baka(self, ctx=commands.Context, *args): #dame dame!!! dame yo dame mamo yo!!!!!! (REWORKED 2023)
        try:
            cmd_info=await resolve_args(ctx,args, ctx.message.attachments)
        except:
            cmd_info=await resolve_args_2(ctx,args, ctx.message.attachments)
        url=cmd_info[0]
        q=requests.get(url)
        with open('h:\\baka\\first-order-model\\bakain.png','wb') as f:
            f.write(q.content)
        response = await self.bot.loop.run_in_executor(None, baka_shit)
        with open('h:\\baka\\first-order-model\\final.mp4','rb') as f:
            await ctx.send(file=discord.File(f, filename='baka.mp4'))
            
            
    
            
            
            
    @commands.command()
    async def inthebible(self, ctx=commands.Context, *, fuck=''): #see if a message is in hebrew or not
        hebrew=['֑ ', '֒ ', '֓ ', '֔ ', '֕ ', '֖ ', '֗ ', '֘ ', '֙ ', '֚ ', '֛ ', '֜ ', '֝ ', '֞ ', '֟ ', '֠ ', '֡ ', '֢ ', '֣ ', '֤ ', '֥ ', '֦ ', '֧ ', '֨ ', '֩ ', '֪ ', '֫ ', '֬ ', '֭ ', '֮ ', '֯ ', 'ְ ', 'ֱ ', 'ֲ ', 'ֳ ', 'ִ ', 'ֵ ', 'ֶ ', 'ַ ', 'ָ ', 'ֹ ', 'ֺ ', 'ֻ ', 'ּ ', 'ֽ ', '־', 'ֿ ', '׀', 'ׁ ', 'ׂ ', '׃', 'ׄ ', 'ׅ ', '׆', 'ׇ ', 'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'ך', 'כ', 'ל', 'ם', 'מ', 'ן', 'נ', 'ס', 'ע', 'ף', 'פ', 'ץ', 'צ', 'ק', 'ר', 'ש', 'ת', 'ׯ', 'װ', 'ױ', 'ײ', '׳', '״']
        fuck2=fuck.replace(' ','').replace('.','').replace('?','').replace('!','').replace('1','').replace('2','').replace('3','').replace('4','')
        fuck2=fuck2.replace('5','').replace('6','').replace('7','').replace('8','').replace('9','').replace('0','').replace(',','').replace('@','')
        inbible=False
        for i in hebrew:
            if i in fuck2:
                inbible=True
        if inbible:
            await ctx.send('yeah, that word is probably in the bible.')
        else:
            await ctx.send('none of those words are in the bible.')
            
            
            
            
            
    @commands.command()
    async def tune(self, ctx=commands.Context, frq=None): #tune to an fm station in the area using RTL-SDR dongle
        global glooba
        if not glooba:
            glooba=True
            freqs=[88.1, 88.7, 89.3, 89.9, 90.5, 91.5, 91.9, 92.9, 93.7, 94.5, 95.3, 95.7, 96.1, 96.5, 96.9, 97.3, 98.1, 98.3, 98.7, 99.7, 100.1, 100.5, 100.9, 101.5, 102.5, 103.5, 103.9, 104.3, 104.7, 105.5, 105.9, 106.3, 106.7, 107.5]
            
                
            sdr = RtlSdr()

            fq=random.choice(freqs)
            if frq is not None:fq=float(frq)
            await ctx.send('tuning frequency '+str(fq)+' FM')
            
            with open('h:\\frart\\stations.txt','r',encoding='utf-8') as f:
                z=f.readlines()
            callsign=''
            brand=''
            latitude=''
            longitude=''
            location=''
            school=''
            format=''
            coords='40.4940 N 80.0190 W'
            for i in z:
                r=i.strip('\r\n').split('|')
                try:
                    if r[2]==str(fq)+' FM':
                        callsign=str(r[0])
                        brand=str(r[1])
                        latitude=str(r[3].split('N')[0])
                        longitude=str(r[3].split('N')[1])
                        power=str(r[4])
                        location=str(r[5])
                        school=str(r[6])
                        format=str(r[7])
                        coords=str(r[3])
                except:
                    pass
            mylat=40.164052
            mylon=-80.603257

            #40 9 49.0 N 80 36 6.0 W
            #40.4940 N 80.0190 W

            
            
            c=coords.split(' ')
            if len(c)==4:
                print('zung!')
                destlat=float(c[0])
                destlon=-float(c[2])
            else:
                lat=c[0:3]
                lon=c[4:7]
                destlat=float(lat[0])+(float(lat[1])/60)+(float(lat[2])/3600)
                destlon=-(float(lon[0])+(float(lon[1])/60)+(float(lon[2])/3600))

            source=(mylat,mylon)
            dest=(destlat,destlon)
            dist=geopy.distance.distance(source, dest)
            try:
                inf='\n'.join([str(fq)+' '+callsign,'"'+brand+'"','Latitude: '+latitude,'Longitude: '+longitude,'Location: '+location,'Power: '+power, 'Format: '+format,'Distance: '+str(round(dist.km*10)/10)+'km ('+str(round(dist.miles*10)/10)+'mi)'])
            except:
                inf=''
            # configure device
            Fs=1.024e6
            sdr.sample_rate = Fs  # Hz
            sdr.center_freq = fq*1e6#98.7e6     # Hz
            sdr.freq_correction = 60   # PPM
            sdr.gain = 'auto'


            
            samples = sdr.read_samples(Fs*10)
            sdr.close()

            x1 = np.array(samples).astype("complex64")
            x2=x1
            ##
            ##plt.specgram(x1, NFFT=2048, Fs=Fs)  
            ##plt.title("x1")  
            ##plt.ylim(-Fs/2, Fs/2)  
            ##plt.savefig("x1_spec.pdf", bbox_inches='tight', pad_inches=0.5)  
            ##plt.close()


            # An FM broadcast signal has  a bandwidth of 200 kHz
            f_bw = 200000  
            dec_rate = int(Fs / f_bw)  
            x4 = signal.decimate(x2, dec_rate)  
            # Calculate the new sampling rate
            Fs_y = Fs/dec_rate

            ### Polar discriminator
            y5 = x4[1:] * np.conj(x4[:-1])  
            x5 = np.angle(y5)

            # The de-emphasis filter
            # Given a signal 'x5' (in a numpy array) with sampling rate Fs_y
            d = Fs_y * 75e-6   # Calculate the # of samples to hit the -3dB point  
            x = np.exp(-1/d)   # Calculate the decay between each sample  
            b = [1-x]          # Create the filter coefficients  
            a = [1,-x]  
            x6 = signal.lfilter(b,a,x5)  
            
            #booba=x5[19000-500:19000+500]
            #sig=np.max(booba)
            #noi=np.min(booba)
            #print(sig)
            #print(noi)
            
            # Find a decimation rate to achieve audio sampling rate between 44-48 kHz
            audio_freq = 44100#/1.166#44100.0  
            dec_audio = int(Fs_y/audio_freq)  
            Fs_audio = Fs_y / dec_audio

            x7 = signal.decimate(x6, dec_audio)  

            # Scale audio to adjust volume
            x7 *= 10000 / np.max(np.abs(x7))  
            # Save to file as 16-bit signed single-channel audio samples
            x7.astype("int16").tofile("wbfm-mono.raw")  

            # Note: x5 is now an array of real, not complex, values
            # As a result, the PSDs will now be plotted single-sided by default (since
            # a real signal has a symmetric spectrum)
            # Plot the PSD of x5
            sex=plt.psd(x5, NFFT=2048, Fs=Fs_y, color="blue")  
            plt.title(str(fq)+' FM')  
            plt.axvspan(0,             15000,         color="red", alpha=0.2)  
            plt.axvspan(19000-500,     19000+500,     color="green", alpha=0.4)  
            plt.axvspan(19000*2-15000, 19000*2+15000, color="orange", alpha=0.2)  
            plt.axvspan(19000*3-1500,  19000*3+1500,  color="blue", alpha=0.2)  
            plt.ticklabel_format(style='plain', axis='y' )  
            plt.savefig("yeah.png", bbox_inches='tight', pad_inches=0.5)  
            def convert_to_decibel(arr):
                ref = 1
                return 20 * np.log10(abs(arr) / ref)
            s1=sex[0][190-5:190+5]
            sn=[]
            for i in s1:
                print(convert_to_decibel(i))
                sn.append(convert_to_decibel(i))
            sig=max(sn)/2
            noi=min(sn)/2
            snr=sig-noi
            
            
            
            
            plt.close()  
            
            
            
            inf+='\nSNR: '+str(round(snr*10)/10)
            
            
            
            
            
            os.system('ffmpeg -f s16le -ar 44100 -i wbfm-mono.raw yeah.mp3 -y')
            
            with open('yeah.png','rb') as f:
                await ctx.send(file=discord.File(f, filename='yeah.png'))
            with open('yeah.mp3','rb') as f:
                await ctx.send(inf, file=discord.File(f, filename='yeah.mp3'))
            glooba=False
        else:
            await ctx.send('pleaase wait for the other  guy to finish tuning ')
    
    @commands.command() #IS IT TUESDAY???
    async def tuesday(self, ctx=commands.Context):
        dt=datetime.datetime.today().weekday()
        print(dt)
        if ctx.author.id==419715716770562078: 
            dt=(datetime.datetime.today() - timedelta(hours = 1)).weekday() 
            print('ball-sack!')
        print(dt)
        #if youre momentum (cst) and run it at 12:30am on a wednesday real people time (est) it says tuesday still
        #if youre greek it also adjusts
        
        #this command has a lookup table for people who are greek and who are not
        if ctx.author.id==206392667351941121: dt=(datetime.datetime.today() - timedelta(hours = 1)).weekday()
        if ctx.author.id==211419370860183552: dt=(datetime.datetime.today() - timedelta(hours = 3)).weekday()
        if ctx.author.id==407564713740861440: dt=(datetime.datetime.today() + timedelta(hours = 8)).weekday()
        #vv ITS TUESDAY vv
        if dt==1: await ctx.send('https://cdn.discordapp.com/attachments/1069995179358031922/1072698277620895854/EqbbrjcXUAAH4cM.png')
        #^^ ITS TUESDAY ^^
        if dt==0:
            with open('MONDAY.jpg','rb') as f:
                await ctx.send(file=discord.File(f, filename='image.jpg')) #Shambles Cirno
        if dt==2:
            await ctx.send('https://tenor.com/view/made-in-abyss-anime-gif-26144590') #Made In Abyss Wednesday
        if dt==3:
            with open('thursday.png','rb') as f:
                await ctx.send(file=discord.File(f, filename='image.png')) #Shambles Cirno
        if dt==4:
            with open('FRIDAY.jpg','rb') as f:
                await ctx.send(file=discord.File(f, filename='image.jpg')) #Shambles Cirno
        if dt==5:
            with open('SATURDAY.jpg','rb') as f:
                await ctx.send(file=discord.File(f, filename='image.jpg')) #Shambles Cirno
        if dt==6:
            with open('SUNDAY.jpg','rb') as f:
                await ctx.send(file=discord.File(f, filename='image.jpg')) #Shambles Cirno
                
                
    
                
                
    @commands.command()
    async def poop(self, ctx): #ai-generated command
        poop_role = discord.utils.get(ctx.guild.roles, name="poop")
        if poop_role is None:
            poop_role = await ctx.guild.create_role(name="poop")
        await ctx.author.add_roles(poop_role)
        await ctx.send("You are now a poop")
        
    @commands.command() #ai-generated command
    async def gay(self, ctx, member: discord.Member):  # turns a straight person gay (or not)

        if member == ctx.author:  # checks if the user is trying to turn themselves gay (or not)
            await ctx.send("You can't turn yourself gay!")  # sends message saying you can't turn yourself gay (or not)

        else:  # if the user isn't trying to turn themselves gay (or not), then...
            random_number=generateUUID()
            await ctx.send("{} is now {}% gay!".format(member, random_number))  # sends message saying that they are now x% straight or x% gay depending on the number generated by random_number() function below
    
    @commands.command() #ai-generated command
    async def piss(self, ctx):
        """
        Create piss role
        """
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name="piss")
        if role is None:
            role = await guild.create_role(name="piss")
        await ctx.author.add_roles(role)
        await ctx.send("You are now a piss")
        
    @commands.command() #use WhatFontIs API to detect a font
    async def font(self, ctx, *args):
        try:
            cmd_info=await resolve_args(ctx,args, ctx.message.attachments)
        except:
            cmd_info=await resolve_args_2(ctx,args, ctx.message.attachments)
        url=cmd_info[0]
        
        body={
            "FONT": {
                "API_KEY": "9bde9650548146eee18856a53ebb323ce9ec5f575b0947b5457c98d9d08375d5",
                "P": "1",
                "F": "1",
                "INFO": {
                    "urlimage": url
                }
            }
        }
        
        with open('font.json','w') as f:
            f.write(json.dumps(body))
            
        storageChannel=self.bot.get_channel(1101971423930622024)
        with open('font.json','rb') as f:
            jsonmessage=await storageChannel.send(file=discord.File(f, filename='font.json'))
        jsonurl=jsonmessage.attachments[0].url
        print(jsonurl)
        encoded_jsonurl=urllib.parse.quote(jsonurl)
        requesturl='https://www.whatfontis.com/api/?file=' + encoded_jsonurl + '&limit=1'
        print(requesturl)
        
        fontName='null_fontname'
        fontPreviewURL='https://media.discordapp.net/attachments/727669455211200562/1101975312364994570/image.png'
        fontLinkURL='https://media.discordapp.net/attachments/727669455211200562/1101975312364994570/image.png'
        
        results=requests.get(requesturl).json()
        print(results)
        foant=results[0]
        fontName=foant['title']
        fontPreviewURL=foant['image']
        fontLinkURL=foant['url']
        
        q=requests.get(fontPreviewURL)
        with open('font.png','wb') as f:
            f.write(q.content)
        
        
        embed=discord.Embed(title='recognized font: '+fontName, color=0x225588, description='[whatfontis]('+fontLinkURL+')\n\nremember to keep the image black on a white background with clean sharp edges')
        embed.set_image(url="attachment://"+str('font.png'))
        favicon='https://media.discordapp.net/attachments/1101971423930622024/1101978109445681282/image.png'
        
        embed.set_footer(text='powered by WhatFontIs',icon_url=favicon)
        with open('font.png', 'rb') as f:  # discord file objects must be opened in binary and read mode
            f2 = discord.File(f, filename='font.png')
            await ctx.send(file=f2,embed=embed)
        
        #q=requests.get(url)
        #with open('h:\\baka\\first-order-model\\bakain.png','wb') as f:
            #f.write(q.content)
            
    @commands.command(aliases=['ek','emojicombo','gboard'])
    async def emojikitchen(self, ctx, emo1_=None, emo2_=None): #get the hilarious google gboard emojis!!
        emo1=emo1_
        emo2=emo2_
        if len(emo1_)>1:
            emo1=emo1[0]
            emo2=emo1_[1]
        job=str(generateUUID())+str(generateUUID())+str(generateUUID())
        result = None
        
        if emo1 is None:
            while result is None:
                try:
                    with open('emojiOutput.json',encoding='utf-8') as f:
                        emojis=json.load(f)
                    gay=random.randrange(len(emojis))
                    i2=0
                    the_it=''
                    for i in emojis:
                        #print(i)
                        i2+=1
                        if i2==gay and '-' not in i:
                            the_it=i
                            break
                        if i2==gay and '-' in i:
                            gay=random.randrange(0,len(emojis))
                            #break
                    print(the_it)
                    combos=emojis[the_it]
                    combo=random.choice(combos)

                    cp1=combo['leftEmoji']
                    cp2=combo['rightEmoji']
                    date=combo['date']
                    
                    emoji1=chr(int(cp1,16))
                    emoji2=chr(int(cp2,16))
                    name1=unicodedata.name(emoji1)
                    name2=unicodedata.name(emoji2)
                    
                    url='https://www.gstatic.com/android/keyboard/emojikitchen/'+date+'/u'+cp1+'/u'+cp1+'_u'+cp2+'.png'
                    with open('emoji'+job+'.png','wb') as f:
                        q=requests.get(url).content
                        f.write(q)
                    with open('emoji'+job+'.png','rb') as f:
                        await ctx.send(emoji1+' ('+name1+') + '+emoji2+' ('+name2+')', file=discord.File(f, filename='emoji'+job+'.png'))
                    result='my penis'
                except:
                    result=None
        else:
            try:
                if emo2 is None:
                    with open('emojiOutput.json',encoding='utf-8') as f:
                        emojis=json.load(f)

                    for i in emojis:
                        if i==str(hex(ord(emo1)))[2:]:
                            combos=emojis[i]
                            combo=random.choice(combos)
                            break
                    cp1=combo['leftEmoji']
                    cp2=combo['rightEmoji']
                    date=combo['date']
                    
                else:
                    with open('emojiOutput.json',encoding='utf-8') as f:
                        emojis=json.load(f)
                    found=False
                    for i in emojis:
                        if i==str(hex(ord(emo1)))[2:]:
                            combos=emojis[i]
                            #combo=random.choice(combos)
                            #break
                            for i2 in combos:
                                if i2['leftEmoji']==str(hex(ord(emo1)))[2:] and i2['rightEmoji']==str(hex(ord(emo2)))[2:]:
                                    combo=i2
                                    found=True
                                if i2['leftEmoji']==str(hex(ord(emo2)))[2:] and i2['rightEmoji']==str(hex(ord(emo1)))[2:]:
                                    combo=i2
                                    found=True
                    if not found:
                        for i in emojis:
                            if i==str(hex(ord(emo2)))[2:]:
                                combos=emojis[i]
                                #combo=random.choice(combos)
                                #break
                                for i2 in combos:
                                    if i2['leftEmoji']==str(hex(ord(emo1)))[2:] and i2['rightEmoji']==str(hex(ord(emo2)))[2:]:
                                        combo=i2
                                        found=True
                                    if i2['leftEmoji']==str(hex(ord(emo2)))[2:] and i2['rightEmoji']==str(hex(ord(emo1)))[2:]:
                                        combo=i2
                                        found=True
                        if not found:
                            await ctx.send('Emoji combo does not exist... :(')
                        return
                    cp1=combo['leftEmoji']
                    cp2=combo['rightEmoji']
                    date=combo['date']
                    
                    
                try:
                    emoji1=chr(int(cp1,16))
                    name1=unicodedata.name(emoji1)
                except:
                    emoji1='ERROR'
                    name1='ERROR'
                try:
                    emoji2=chr(int(cp2,16))
                    name2=unicodedata.name(emoji2)
                except:
                    emoji2='ERROR'
                    name2='ERROR'    
                url='https://www.gstatic.com/android/keyboard/emojikitchen/'+date+'/u'+cp1+'/u'+cp1+'_u'+cp2+'.png'
                with open('emoji'+job+'.png','wb') as f:
                    q=requests.get(url).content
                    f.write(q)
                with open('emoji'+job+'.png','rb') as f:
                    await ctx.send(emoji1+' ('+name1+') + '+emoji2+' ('+name2+')', file=discord.File(f, filename='emoji'+job+'.png'))
                result='my penis'
            except ValueError as e:
                await ctx.send('Error - perhaps the emoji uses more than one codepoint which at this point i find tricky to figure out, at least at 10pm with a headache. full error:\n'+str(e))
#https://i3.ytimg.com/vi/erLk59H86ww/maxresdefault.jpg

def setup(bot: commands.Bot):
    bot.add_cog(UtilityCommands(bot))
