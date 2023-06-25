from PIL import ImageFont, ImageDraw
import discord
import requests

import os
import re
from PIL import Image, ImageFont, ImageDraw

from discord.ext import commands
from discord import File
from discord.utils import get

from os import path
import traceback
import multidict
import subprocess
import random
import json

#Set Up Teh Loggah!
import logging
log_format = '[%(name)s] %(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(format=log_format,datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger=logging.getLogger('MEME')

from .silverutil import generateUUID, get_data
global recent_choices
recent_choices=['recentchoice']

def logogen(uuid):
        subprocess.check_call(r'"C:\Program Files\Blender Foundation\Blender 3.4\blender.exe" -b "h:\blah blah had to move these\logo2.blend" -o "h:\frart\logo'+uuid+'.mp4" -a',shell=True)
        #return
        
def cpgen(uuid):
        subprocess.check_call(r'"C:\Program Files\Blender Foundation\Blender 3.4\blender.exe" -b "i:\evangelion meme\cp logo scale.blend" -o "h:\frart\logo'+uuid+'.png" -f 0 -- '+uuid,shell=True)
        #return
        
def cpgengc(uuid,fov):
        subprocess.check_call(r'"C:\Program Files\Blender Foundation\Blender 3.4\blender.exe" -b "i:\evangelion meme\cp logo scale_fovtest.blend" -o "h:\frart\logo'+uuid+'.png" -f 0 -- '+uuid+' '+str(fov),shell=True)
        #return
        
def cpgenezo(uuid):
        subprocess.check_call(r'"C:\Program Files\Blender Foundation\Blender 3.4\blender.exe" -b "i:\evangelion meme\cp logo scale.blend" -o "h:\frart\logo'+uuid+'.png" -f 0 -- '+uuid,shell=True)
        #return
        
bot = commands.Bot(help_command=None,command_prefix=['. ','.'])
client=discord.Client()









async def message_history_img_handler(ctx):
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

async def resolve_args_2(ctx,args, attachments):
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
    

def save_input(fn,data):
    with open(fn, 'wb') as f:
        f.write(data)

def download_file(url):
    funny=requests.get(url)
    return funny.content

def extract_extension(url):
    if '.' in url:
        return url.split('.')[-1]
    else:
        return 'file'

def findWords(letter,pos,multiword):
    with open('i:\\cp\\wordset-dictionary\\data\\'+letter+'.json', encoding='utf-8') as f:
        c=json.load(f)

    dummy=None
    words=[]
    for i in c:
        skip=False
        try:
            dummy=(c[i]['meanings'])
        except:
            skip=True
        if not skip:
            for meaning in c[i]['meanings']:
                if meaning['speech_part']==pos:
                    #print(meaning)
                    if multiword or (len(i.split(' '))==1 and len(i.split('-'))==1):
                        if len(i)<6:
                            words.append(i)
                        elif len(i)<8:
                            if random.randint(0,100)<80: words.append(i)
                        elif len(i)<12:
                            if random.randint(0,100)<50: words.append(i)
                        elif len(i)<20:
                            if random.randint(0,100)<20: words.append(i)
                        else:
                            if random.randint(0,100)<10: words.append(i)
    return words

def findWordsEnding(letter,pos,ending,multiword):
    with open('i:\\cp\\wordset-dictionary\\data\\'+letter+'.json', encoding='utf-8') as f:
        c=json.load(f)

    dummy=None
    words=[]
    for i in c:
        skip=False
        try:
            dummy=(c[i]['meanings'])
        except:
            skip=True
        if not skip:
            for meaning in c[i]['meanings']:
                if meaning['speech_part']==pos:
                    #print(meaning)
                    if (multiword or (len(i.split(' '))==1 and len(i.split('-'))==1)) and i.endswith(ending):
                        print(i)
                        words.append(i)
    return words




class MemeCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command()
    async def kys(self, ctx=commands.Context):
        await ctx.send(str(os.getcwd()))
        os.chdir('h:\\frart')
        await ctx.send(str(os.getcwd()))
    @commands.command()
    async def says(self, ctx=commands.Context, ima=None):
        jon=False
        url=''
        if ima=='jon1' or ima=='jon' or ima=='water': #If Water Is Water To You'd Brain
            jon=True
            await ctx.send(file=File('water.png'))
            await ctx.message.delete()
        elif ima=='jon2' or ima=='oven' or ima=='ofin': #Why Do They Call It Oven
            jon=True
            await ctx.send(file=File('jon.jpg'))
            await ctx.message.delete()
        else:
            lis=get_data('says')
            for i in lis:
                for i2 in i[0]:
                    print(i2)
                    if i2==ima:
                        
                        url=i[1]
                        break
                    if ima==None:
                        url=random.choice(lis)[1]
                        break
            if url=='': jon=True
            
        if not jon:
            if url.startswith('D:'):
                await ctx.send(file=File(url.replace('/','\\')))
            else:
                await ctx.send(url)
            await ctx.message.delete()

        if url=='':
            charz=[]
            for i in lis:
                if i[0][0] is not '':
                    charz.append(i[0])
            chars_='\n'.join([str(die) for die in charz])
            #await ctx.send('list of .says characters\n'+str(chars_))



    @commands.command()
    @commands.is_owner()
    async def say(self, ctx=commands.Context, *frien):
        aru=" ".join(frien[:])
        await ctx.message.delete()
        await ctx.send(aru)
        
    @commands.command()
    async def sayhelp(self, ctx=commands.Context, ide=1, *frien):
        aru=" ".join(frien[:])
        #await ctx.message.delete()
        gar=await self.bot.fetch_user(int(ide))
        await gar.send(aru)

    @commands.command()
    async def sayhelp2(self, ctx=commands.Context, ide=1, *frien):
        aru=" ".join(frien[:])
        #await ctx.message.delete()
        gar=await self.bot.fetch_channel(int(ide))
        await gar.send(aru)
        
    
        
    @commands.command(aliases=['intro'])
    async def logo(self, ctx=commands.Context, *shit):
        text=' '.join(shit)
        with open('logo.txt','w',encoding='utf-8') as f:
            f.write(text.replace('\\n','\n'))
        #logo1 render time:10m
        #logo2 render time:10m
        #os.system(r'"C:\Program Files\Blender Foundation\Blender 3.4\blender.exe" -b -a "h:\blah blah had to move these\Intro Template 60FPS(2).blend"')
        #kys=subprocess.check_call(r'"C:\Program Files\Blender Foundation\Blender 3.4\blender.exe" -b "h:\blah blah had to move these\Intro Template 60FPS(2).blend" -a')
        await ctx.send('cooking up your logo... this may take a bit...')
        gay=generateUUID()
        result = await bot.loop.run_in_executor(None, logogen, gay)
        await ctx.reply(file=File('logo'+gay+'.mp4'))
        
        
    @commands.command()
    async def cp(self, ctx=commands.Context, *_texxt): #Generate Child Porn
                                                           #...Logoswaps
        texxt=_texxt
        _textscale=None
        _text=' '.join(texxt).replace(' | ','|').split('--fov')[0]
        passFov=False
        if len(texxt)>2:
            if texxt[-2]=='--fov':
                passFov=True
                fov_=int(texxt[-1])
                texxt=_texxt[:-2]
        text1=''
        text2=''
        #await ctx.send(len(texxt))
        if '|' in _text:
            text1=_text.split('|')[0]
            text2=_text.split('|')[1]
        else:
            if len(texxt)==2:
                text1=texxt[0]
                text2=texxt[1]
            else:
                mid=round(len(texxt)/2)
                text1=' '.join(texxt[:mid])
                text2=' '.join(texxt[mid:])
        if _textscale!=None: textscale=_textscale
        if _textscale==None:
            textscale=1.0
        if text2=='':
            text2=text1
            text1=' '
        if text2=='': text2=' '
        if text1=='': text1=' '
        the_id=generateUUID()
        with open('textTopLine'+the_id+'.txt','w',encoding='utf-8') as f:
            f.write(text1.upper())
        with open('textBottomLine'+the_id+'.txt','w',encoding='utf-8') as f:
            f.write(text2.upper())
        font = ImageFont.truetype(r"X:\impactjpn.otf", 72)
        width=font.getlength(text1.upper())
        width2=font.getlength(text2.upper())
        
        scale1=317/width
        scale2=317/width2
        if _textscale==None:
            textscale=1.0
            if scale1<1.25: textscale=1.5
            if scale2<1.25: textscale=1.5
        if passFov==True:
            fov=fov_
        else:
            fov=27
        fovCoefficient=((((90/(fov+7.85))-0.5)/1.4)+0.5125)/2
        textscale=textscale*fovCoefficient
        with open('scaleTopLine'+the_id+'.txt','w',encoding='utf-8') as f:
            f.write(str(scale1*textscale))
        with open('scaleBottomLine'+the_id+'.txt','w',encoding='utf-8') as f:
            f.write(str(scale2*textscale))
        
        #$with open('fovCoefficient'+the_id+'.txt','w',encoding='utf-8') as f:
        #    f.write(str(fovCoefficient))
            
        #logo1 render time:10m
        #logo2 render time:10m
        #os.system(r'"C:\Program Files\Blender Foundation\Blender 3.4\blender.exe" -b -a "h:\blah blah had to move these\Intro Template 60FPS(2).blend"')
        #kys=subprocess.check_call(r'"C:\Program Files\Blender Foundation\Blender 3.4\blender.exe" -b "h:\blah blah had to move these\Intro Template 60FPS(2).blend" -a')
        warn=''
        if passFov:
            if fov<13 or fov>32: warn='\nwarning: setting the FOV lower than 13 will cause dark edges and setting the FOV higher than 32 will clip the top of the text'
        await ctx.send('cooking up your <:cheese_pizza:1049683785886732318>...'+warn)
        result = await bot.loop.run_in_executor(None, cpgengc, the_id,fov)
        await ctx.reply(file=File('logo'+the_id+'.png0000.png'))

    # @commands.command() #This command was created the day my account got hacked, to transmit things between my alt and SilverGaming.
    # async def dm(self, ctx=commands.Context):
    #     ##creating invite link
    #     gar2=await self.bot.fetch_channel(706353388278775892)
    #     #invitelink = await gar2.create_invite(max_uses=1,unique=True)
    #     ##dming it to the person
    #     #gar=await self.bot.fetch_user(422249760876003328)
    #     #await gar.send(invitelink)
    #     hell=[]
    #     async for msg in gar2.history(limit = 50):
    #         #hell+=''.join(msg.content)
    #         print(msg.content)
    #     #with open ('hell.txt',encoding='UTF-8') as f:
    #         #f.writelines('\n'.join(hell))






    @commands.command(aliases=['rdj','rob','Robert'])
    async def robert(self, ctx=commands.Context,*args): #i'm stuff
        try:
            cmd_info=await resolve_args(ctx,args, ctx.message.attachments)
            url=cmd_info[0]
            txt=cmd_info[1]
            data=download_file(url)
            fn='robert_in.'+extract_extension(url)
            print(fn)
            save_input(fn,data)
            data=None
            img=Image.open(fn)
            roberti=Image.open('robert.png')
            img = img.resize((roberti.width,int((float(img.height)*float(roberti.width/float(img.width))))))
            canvas=Image.new(size=(img.width,img.height+roberti.height),mode='RGB')
            canvas.paste(img)
            offs=(0,img.height)
            canvas.paste(roberti, offs)
            img=None
            text_pos=(26,108)
            roberti=None
            font=ImageFont.truetype(font='arial.ttf',size=1)
            i=1
            while font.getlength(txt)<220 and i<2000:
                font=ImageFont.truetype(font='arial.ttf',size=i)
                i+=1
            d=ImageDraw.Draw(canvas)
            tp=(offs[0]+text_pos[0],offs[1]+text_pos[1])
            d.multiline_text(tp,txt,font=font,fill=(0,0,0))
            canvas.save('robertout.png')
            await ctx.send (file=File('robertout.png'))
        except Exception as e:
        # except Exception as e:
            eror=traceback.format_exc()
            embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
            embed.set_footer(text='lmao')
            await ctx.reply(embed=embed)


    @commands.command() #of in the cold food
    async def ofin(self, ctx=commands.Context,*args):
        try:
            cmd_info=await resolve_args_2(ctx,args, ctx.message.attachments)
            print(cmd_info)
            url=cmd_info[0]
            data=download_file(url)
            fn='robert_in.'+extract_extension(url)
            print(fn)
            save_input(fn,data)
            data=None
            img=Image.open(fn)
            roberti=Image.open('jon.jpg')
            img = img.resize((roberti.width,int((float(img.height)*float(roberti.width/float(img.width))))))
            canvas=Image.new(size=(img.width,img.height+roberti.height),mode='RGB')
            canvas.paste(img)
            offs=(0,img.height)
            canvas.paste(roberti, offs)
            img=None
            roberti=None
            canvas.save('jonout.png')
            await ctx.send (file=File('jonout.png'))
        except Exception as e:
        # except Exception as e:
            eror=traceback.format_exc()
            embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
            embed.set_footer(text='lmao')
            await ctx.reply(embed=embed)

    @commands.command() #why do they call it water when you water the cold water idfk
    async def water(self, ctx=commands.Context,*args):
        try:
            cmd_info=await resolve_args_2(ctx,args, ctx.message.attachments)
            print(cmd_info)
            url=cmd_info[0]
            data=download_file(url)
            fn='robert_in.'+extract_extension(url)
            print(fn)
            save_input(fn,data)
            data=None
            img=Image.open(fn)
            roberti=Image.open('water.png')
            img = img.resize((roberti.width,int((float(img.height)*float(roberti.width/float(img.width))))))
            canvas=Image.new(size=(img.width,img.height+roberti.height),mode='RGB')
            canvas.paste(img)
            offs=(0,img.height)
            canvas.paste(roberti, offs)
            img=None
            roberti=None
            canvas.save('jonout.png')
            await ctx.send (file=File('jonout.png'))
        except Exception as e:
        # except Exception as e:
            eror=traceback.format_exc()
            embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
            embed.set_footer(text='lmao')
            await ctx.reply(embed=embed)


            

    @commands.command(aliases=['dgjs']) #IT'S NOT A SOUNDFONT - This Command broke When W Crashed
    async def soundfont(self, ctx=commands.Context,*args):
        try:
            uuid=generateUUID()
            cmd_info=await resolve_args_2(ctx, args, ctx.message.attachments)
            url=cmd_info[0]
            txt=cmd_info[1]
            data=download_file(url)
            fn='midi.mid'
            print(fn)
            save_input(fn,data)
            with open('w:\\soundfonts.txt') as f:
                sfs=f.readlines()
            sf=random.choice(sfs).strip('\r').strip('\n')
            cmd='C:\\Users\\EzoGaming\\Downloads\\fluidsynth-2.2.4-win10-x64\\bin\\fluidsynth.exe -ni '+sf+' midi.mid -F "slapped'+str(uuid)+'.wav" -r 44100 -R 0'
            cmd=cmd.strip('\n')
            print(cmd)
            os.system(cmd)
            os.system('ffmpeg -i slapped'+str(uuid)+'.wav -q:a 6 slapped'+str(uuid)+'.mp3 -y')
            og_name=url.replace('\\','/').split('/')[-1]
            sf_name=sf.replace('\\','/').split('/')[-1][:-1]
            await ctx.reply ('Selected soundfont: '+sf,file=File(fp='slapped'+str(uuid)+'.mp3',filename=og_name+'-'+sf_name+'.mp3'))
        except Exception as e:
        # except Exception as e:
            eror=traceback.format_exc()
            embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
            embed.set_footer(text='lmao')
            await ctx.reply(embed=embed)


    @commands.command(aliases=['dgjgs'])
    async def midi(self, ctx=commands.Context):
        try:
            with open('w:\\soundfonts.txt') as f:
                sfs=f.readlines()
            sf=random.choice(sfs).strip('\r').strip('\n')
            with open('w:\\mids.txt') as f:
                mid=f.readlines()
            md=random.choice(mid).strip('\r').strip('\n')
            cmd='C:\\Users\\EzoGaming\\Downloads\\fluidsynth-2.2.4-win10-x64\\bin\\fluidsynth.exe -ni '+sf+' '+md+' -F "slapped.wav" -r 44100 -R 0'
            cmd=cmd.strip('\n')
            print(cmd)
            os.system(cmd)
            os.system('ffmpeg -i slapped.wav slapped.mp3 -y')
            await ctx.send ('Selected soundfont: '+sf+"\n"+'Selected MIDI: '+md,file=File('slapped.mp3'))
        except Exception as e:
        # except Exception as e:
            eror=traceback.format_exc()
            embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
            embed.set_footer(text='lmao')
            await ctx.reply(embed=embed)

    @commands.command()
    async def selfdox(self, ctx=commands.Context):
        await ctx.send(ctx.message.author.display_name + "'s ip is `8.8.8.8`")

    @commands.command()
    async def cancel(self, ctx=commands.Context, aaaa='Dumbass Who Cant Issue Commands Properly'):
        if(aaaa.lower()=="me"):
            await ctx.send("#"+ctx.message.author.display_name.replace(" ","") + "IsOverParty")
        else:
            await ctx.send("#"+aaaa.replace(" ","")+"IsOverParty")

    @commands.command()
    async def rolegen(self,ctx=commands.Context, count = 1):
        all=''
        for noog in range(count):
            thing='curdling rapidly'
            rl_=open('rolelist.txt','r',encoding='utf-8').readlines()
            rl=[i.strip('\r\n') for i in rl_]
            while thing in rl or thing+' ' in rl:
                global recent_choices
                _1=open('wordlist_1.txt','r',encoding='utf-8').readlines()
                _2=open('wordlist_2.txt','r',encoding='utf-8').readlines()
                a1='RecentChoice'
                a2='RecentChoice'
                while a1.lower().strip() in recent_choices or a1 is None or a1 is 'RecentChoice':
                    #print('a1')
                    a1=random.choice(_1).strip('\r\n')
                while a2.lower().strip() in recent_choices or a2 is None or a2 is 'RecentChoice':
                    #print('a2')
                    a2=random.choice(_2).strip('\r\n')
                print(a1)
                print(a2)
                w2='<'
                while '<' in w2:
                    w2=random.choice(_2).strip('\r\n')
                print(w2)
                if not w2.endswith('s'):
                    print(w2)
                    w2+='s'
                    print(w2)
                a1=a1.replace('<word2>',w2)
                #print(a1)
                #print(a2)
                if a1=='j-':
                    yoo=random.randint(0,1)
                    if yoo:
                        await ctx.send('j'+random.choice(_1)[1:])
                        break
                    else:
                        await ctx.send('j'+random.choice(_2)[1:])
                        break
                else:
                    for i2 in range(600):
                        if a2==a2.upper():
                            a1=a1.upper()
                        if a1==a1.upper():
                            a2=a2.upper()
                        if a2.split(' ')[0][:3]==a2.split(' ')[0][:3].capitalize():
                            a1=' '.join([i.capitalize() for i in a1.split(' ')])
                        if a1.split(' ')[0][:3]==a1.split(' ')[0][:3].capitalize():
                            a2=' '.join([i.capitalize() for i in a2.split(' ')])
                        if a2.startswith('-'):
                            a2=a2.lower()
                        if a1.endswith('-'):
                            a2=a2.lower()
                    if a2.lower().endswith('<adv>'):
                        a2=a2.replace('<adv>','').replace('<ADV>','')
                        a1_=a1
                        a1=a2
                        a2=a1_
                    if a1.startswith('-'):
                        a1_=a1
                        a1=a2
                        a2=a1_
                    thing=a1+' '+a2
                    if '-ed' in a1:
                        thing=a2+' '+a1
                    for i in range(500): #sanitation
                        thing=thing.replace('e -ed','ed')
                        thing=thing.replace('e  -ed','ed')
                        thing=thing.replace('e- -ed','ed')
                        thing=thing.replace('e -ist','ist')
                        thing=thing.replace('e  -ist','ist')
                        thing=thing.replace('e- -ist','ist')
                        thing=thing.replace('t -ing','ing')
                        thing=thing.replace('t  -ing','ing')
                        thing=thing.replace('t- -ing','ing')
                        thing=thing.replace('ttt','tt')
                        thing=thing.replace('- -','')
                        thing=thing.replace(' -','')
                        thing=thing.replace('- ','')
                        thing=thing.replace('-','')
                        thing=thing.replace('  ',' ')
                        thing=thing.replace('  ',' ')
                        thing=thing.replace('  ',' ')
                        thing=thing.replace('  ',' ')
                        thing=thing.replace(' A ',' a ')
                        thing=thing.replace(' An ',' an ')
                        thing=thing.replace(' a a',' an a')
                        thing=thing.replace(' a e',' an e')
                        thing=thing.replace(' a i',' an i')
                        thing=thing.replace(' a o',' an o')
                        thing=thing.replace(' a A',' an A')
                        thing=thing.replace(' a E',' an E')
                        thing=thing.replace(' a I',' an I')
                        thing=thing.replace(' a O',' an O')
                        thing=thing.replace(' Of ',' of ')
                        thing=thing.replace(' The ',' the ')
                        thing=thing.replace('of of','of')
                        thing=thing.replace('the the','the')
                        if thing.endswith('ed'):
                            thing=thing.replace(' ed','ed')
                        if thing.endswith('er'):
                            thing=thing.replace(' er','er')
                        if thing.endswith('ington'):
                            thing=thing.replace(' ington','ington')
                        thing=thing.replace('yington','ington')
                        thing=thing.replace('eington','ington')
                        thing=thing.replace('aington','ington')
                        thing=thing.replace('oington','ington')
                        thing=thing.replace('uington','ington')
                        if random.randint(0,10)<9:
                            thing=thing.replace('eer','er')
                        thing=thing.replace('erist','rist')
                        thing=thing.replace('erer','er')
                        thing=thing+'<eol>'
                        thing=thing.replace('aer<eol>','er')
                        thing=thing.replace('ieington<eol>','ington')
                        thing=thing.replace('eington<eol>','ington')
                        thing=thing.replace('aington<eol>','ington')
                        thing=thing.replace('<eol>','')
                        thing=thing.replace('ggg','gg')
                        thing=thing.replace('ttt','tt')
                        thing=thing.replace('aified','afied')
                        thing=thing.replace('eified','efied')
                        thing=thing.replace('iified','ified')
                        thing=thing.replace('oified','ofied')
                        thing=thing.replace('uified','ufied')
                        thing=thing.replace('yified','ified')
                        #print(thing)
                        thing=thing.replace('inging','ing')
                        thing=thing.replace('istist','ist')
                        #print(a1[-2:])
                        if a1[-2:]!="oo":
                            thing=thing.replace('oologist','ologist')
                        thing=thing.replace('ooo','oo')
                    if not '-' in a1:
                        #print(a1)
                        recent_choices.append(a1.lower())
                    if not '-' in a2:
                        recent_choices.append(a2.lower())
                    if len(recent_choices)>16:
                        dummy=recent_choices.pop(0)
                        dummy=recent_choices.pop(0)
                    print(recent_choices)
                    all+='\n'+thing
                    
        await ctx.send(all)
    @commands.command()
    async def backronym(self,ctx=commands.Context, acr_ = None):
        acr=acr_
        all_words=[]
        if acr_ is None:
            if random.randint(0,100)<50:
                acr=''
                while len(acr) not in [3,4]:
                    for i in 'abcdefghijklmnopqrstuvwxyz':
                        with open('i:\\cp\\wordset-dictionary\\data\\'+i+'.json', encoding='utf-8') as f:
                            c=json.load(f)
                        for i2 in c:
                            #print('lesbian')
                            #print(i2)
                            if len(i2) in [3,4]:
                                all_words.append(i2)
                                #print('gay')
                                #print(i2)
                    acr=random.choice(all_words)
                    #await ctx.send('test 3-4 Letter Words: '+acr)
            else:
                acr=''
                while len(acr)!=2:
                    acr=random.choice('abcdefghijklmnopqrstuvwxyz')+random.choice('abcdefghijklmnopqrstuvwxyz')
                    #await ctx.send('test 2 Letters: '+acr)
        output=''
        if len(acr)==2:
            words=findWords(acr[0],'adjective',False)
            adj=random.choice(words)
            words=findWords(acr[1],'noun',False)
            noun=random.choice(words)
            output=(adj+' '+noun)
        if len(acr)==3:
            if random.randint(0,1):
                words=findWords(acr[0],'adjective',False)
                adj=random.choice(words)
            else:
                words=findWords(acr[0],'adverb',False)
                adj=random.choice(words)
            if adj.startswith('non'):
                if random.randint(0,100)<20:
                    words=findWords(acr[1],'adjective',False)
                    adj='near-'+random.choice(words)
                else:
                    words=findWords(acr[1],'adjective',False)
                    adj='non-'+random.choice(words)
            elif adj in ['big','small','fat'] and random.randint(0,100)<35:
                words=findWords(acr[1],'noun',False)
                adj+=' '+random.choice(words)
            else:
                words=findWords(acr[1],'adjective',False)
                adj+=' '+random.choice(words)
            if acr[2] in ['0','1','2','3','4','5','6','7','8','9']:
                if acr[2]=='0': noun='zero'
                if acr[2]=='1': noun='one'
                if acr[2]=='2': noun='two'
                if acr[2]=='3': noun='three'
                if acr[2]=='4': noun='four'
                if acr[2]=='5': noun='five'
                if acr[2]=='6': noun='six'
                if acr[2]=='7': noun='seven'
                if acr[2]=='8': noun='eight'
                if acr[2]=='9': noun='nine'
            else:
                words=findWords(acr[2],'noun',False)
                noun=random.choice(words)
            output=(adj+' '+noun)
        if len(acr)==4:
            if random.randint(0,1)==0:
                words=findWords(acr[0],'adverb',False)
                adj=random.choice(words)
            else:
                words=findWords(acr[0],'adjective',False)
                adj=random.choice(words)
            if adj.startswith('non'):
                if random.randint(0,100)<20:
                    words=findWords(acr[1],'adjective',False)
                    adj='near-'+random.choice(words)
                else:
                    words=findWords(acr[1],'adjective',False)
                    adj='non-'+random.choice(words)
            else:
                words=findWords(acr[1],'adjective',False)
                adj+=' '+random.choice(words)
            words=findWords(acr[2],'adjective',False)
            adj+=' '+random.choice(words)
            words=findWords(acr[3],'noun',False)
            noun=random.choice(words)
            output=adj+' '+noun
        if len(acr)==5:
            if random.randint(0,1)==0:
                words=findWords(acr[0],'adverb',False)
                adj=random.choice(words)
            else:
                words=findWords(acr[0],'adjective',False)
                adj=random.choice(words)
            if adj.startswith('non'):
                if random.randint(0,100)<20:
                    words=findWords(acr[1],'adjective',False)
                    adj='near-'+random.choice(words)
                else:
                    words=findWords(acr[1],'adjective',False)
                    adj='non-'+random.choice(words)
            else:
                words=findWords(acr[1],'adjective',False)
                adj+=' '+random.choice(words)
            words=findWords(acr[2],'adjective',False)
            adj+=' '+random.choice(words)
            words=findWords(acr[3],'noun',False)
            noun=random.choice(words)
            words=findWords(acr[4],'noun',False)
            noun+=' '+random.choice(words)
            output=adj+' '+noun
        await ctx.send(output)

    @commands.command()
    async def rhyme(self,ctx=commands.Context, *phrase):
        res=''
        p=' '.join(phrase)
        p_=p.replace('_',' ')
        #p=p.split(' ')[-1]
        p_=' '.join(p_.split('-'))#[-1]
        p_=' '.join(p_.split('.'))#[-1]
        p_=p_.split(' ')
        #await ctx.send(str(p_))
        sylls=[]
        #await ctx.send(p_)
        if len(p_)>1:
            #await ctx.send('ballsing')
            for i in p_:
                q=requests.get('https://api.datamuse.com/words?sp='+i+'&md=s')
                q2=json.loads(q.content)
                #await ctx.send(q2[0]['numSyllables'])
                try:
                    sylls.append(q2[0]['numSyllables'])
                except:
                    sylls.append(1)
        index=0
        for p in p_:
            
            for i in '"\'!@#$%^&*()+-={}|[]\:;<>?,./`~0123456789':
                p=p.replace(i,'')
            print(p)
            q=requests.get('https://api.datamuse.com/words?rel_rhy='+p)
            q2=json.loads(q.content)
            w=[]
            for i in q2:
                print(i)
                if not i["word"].endswith(p): 
                    if not i["word"].replace(' ','').endswith(p): 
                        if len(p_)>1:
                            if i["numSyllables"]==sylls[index]: w.append(i["word"])
                        else:
                            w.append(i["word"])
            try:
                res+=' '+(random.choice(w))
            except:
                q=requests.get('https://api.datamuse.com/words?rel_nry='+p)
                q2=json.loads(q.content)
                w=[]
                for i in q2:
                    print(i)
                    if not i["word"].endswith(p): 
                        if not i["word"].replace(' ','').endswith(p): w.append(i["word"])
                try:
                    res+=' '+(random.choice(w))
                except:
                    p2=p
                    q=requests.get('https://api.datamuse.com/words?sl='+p2)
                    q2=json.loads(q.content)
                    pe=q2[0]["word"]
                    for i in q2:
                        print(p2[-3:])
                        print(i['word'])
                        if True:#i['word'].endswith(p2[-3:]): 
                            p=i['word']
                            #await ctx.send(p)
                            break
                    w=[]
                    q=requests.get('https://api.datamuse.com/words?rel_rhy='+pe)
                    q2=json.loads(q.content)
                    for i in q2:
                        print(i)
                        if not i["word"].endswith(p): 
                            if not i["word"].replace(' ','').endswith(p): w.append(i["word"])
                    try:
                        res+=' '+(random.choice(w))
                    except:
                        q=requests.get('https://api.datamuse.com/words?rel_nry='+p)
                        q2=json.loads(q.content)
                        w=[]
                        for i in q2:
                            print(i)
                            if not i["word"].endswith(p): 
                                if not i["word"].replace(' ','').endswith(p): w.append(i["word"])
                        try:
                            res+=' '+(random.choice(w))
                        except:
                            res+=''
            index+=1
        await ctx.send(res)


def setup(bot: commands.Bot):
    bot.add_cog(MemeCommands(bot))
























































































