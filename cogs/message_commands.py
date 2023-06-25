import random
import re
import traceback
from time import thread_time
import markovify
import nltk
from discord.ext import commands
import json
import discord
from discord.ext import *
from .silverutil import debug_log
#from .syllables import syllablecount
import sqlite3
from datetime import datetime
# list of cjk codepoint ranges
# tuples indicate the bottom and top of the range, inclusive


#Set Up Teh Loggah!
import logging
log_format = '[%(name)s] %(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(format=log_format,datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger=logging.getLogger('MESSAGE')







cjk_ranges = [
        ( 0x4E00,  0x62FF),
        ( 0x6300,  0x77FF),
        ( 0x7800,  0x8CFF),
        ( 0x8D00,  0x9FCC),
        ( 0x3400,  0x4DB5),
        (0x20000, 0x215FF),
        (0x21600, 0x230FF),
        (0x23100, 0x245FF),
        (0x24600, 0x260FF),
        (0x26100, 0x275FF),
        (0x27600, 0x290FF),
        (0x29100, 0x2A6DF),
        (0x2A700, 0x2B734),
        (0x2B740, 0x2B81D),
        (0x2B820, 0x2CEAF),
        (0x2CEB0, 0x2EBEF),
        (0x2F800, 0x2FA1F)
    ]

safe_channels_=[
                '954219578211307560',
                '864374950343999509',
                '806180275037798453',
                '968962138179772426',
                '886788323648094219',
                '900431883559661649',
                '882118990397337640',
                '820170835569541120',
                '879426296290082906',
                '947963019319709777',
                '943264110735421480',
                '891417896272662589',
                '952476036036173834',
                '855681266296684564',
                '875952277796556910',
                '975664785741971486',
                '968776044968574976',
                '966031190433882133',
                '875031587262193694',
                '911140602442285118',
                '892586391328935937',
                '954253320694951946',
                '889226496298868807',
                '829216521959768065',
                '915423760604094535',
                '886777147413385226',
                '893301682157522955',
                '877605701365661766',
                '870860884904394772',
                '862711377519837245',
                '858565022355161088',
                '846578571132141568',
                '830639008912637952',
                '860035877542690826',
                '837529512387936298',
                '851595182989901924',
                '827339164512813077',
                '818978617446236161',
                '809156586249256981',
                '795386437641961472',
                '785977488907829251',
                '779136383603834902',
                '849523303177519124',
                '779136433294147695',
                '785588391546060823',
                '805608843656298517',
                '792505997296926741',
                '779146758063390740',
                '810014654955782154',
                '782805706922393640',
                '891558470761984001',
                '595974673561419776',
                '876265174623985695',
                '953612037500592181',
                '734371031057432606',
                '693232670842421298',
                '867610342896697414',
                '533867795910492180',
                '677769318775259156',
                '638924276266958880',
                '583006408086257715',
                '719017701640634458',
                '767698702466154516',
                '779129225286385726',
                '533527842315698176',
                '682383641816334363',
                '716182537063628801',
                '691816820230979604',
                '684308892527624216',
                '702976401497915472',
                '707783008622739497',
                '737182065929224212',
                '749011575431495720',
                '906775061967556620',
                '740439307013324832',
                '533802959021015040'
            ]

def is_cjk(char):
    char = ord(char)
    for bottom, top in cjk_ranges:
        if char >= bottom and char <= top:
            return True
    return False

"""d ebug_log('(Message) DEBUG: Generating Markov Model...')
with open("C:\\Users\\EzoGaming\\yomama\\allmsg.txt", encoding='utf-8') as f:
    text = f.read().replace('fdestroy','destroy')
MarkovModel = markovify.NewlineText(text, state_size=2)

debug_log('(Message) DEBUG: Generating Pizzi Markov Model...')
with open("C:\\Users\\EzoGaming\\yomama\\pizzi.txt", encoding='utf-8') as f:
    text = f.read()
PizziModel = markovify.NewlineText(text, state_size=2)

debug_log('(Message) DEBUG: Generating Danny Markov Model...')
with open("C:\\Users\\EzoGaming\\yomama\\danny.txt", encoding='utf-8') as f:
    text = f.read()
DannyModel = markovify.NewlineText(text, state_size=2)

debug_log('(Message) DEBUG: Generating Cris Markov Model...')
with open("C:\\Users\\EzoGaming\\yomama\\cris.txt", encoding='utf-8') as f:
    text = f.read()
CrisModel = markovify.NewlineText(text, state_size=2)

debug_log('(Message) DEBUG: Generating Queen Deltarune Markov Model...')
with open("h:\\frart\\QueenFiltered.txt", encoding='utf-8') as f:
    text = f.read()
QueenModel = markovify.NewlineText(text, state_size=2)

debug_log('(Message) DEBUG: Generating Pedo Markov Model...')
with open("C:\\Users\\EzoGaming\\yomama\\maki.txt", encoding='utf-8') as f:
    text = f.read()
MakiModel = markovify.NewlineText(text, state_size=2)

debug_log('(Message) DEBUG: Generating Leffrey Markov Model...')
with open("C:\\Users\\EzoGaming\\yomama\\leffrey.txt", encoding='utf-8') as f:
    text = f.read()
LeffreyModel = markovify.NewlineText(text, state_size=2)

debug_log('(Message) DEBUG: Generating Bravo Markov Model...')
with open("C:\\Users\\EzoGaming\\yomama\\bravo.txt", encoding='utf-8') as f:
    text = f.read()
BravoModel = markovify.NewlineText(text, state_size=2)

debug_log('(Message) DEBUG: Generating EzoGaming Markov Model...')
with open("C:\\Users\\EzoGaming\\yomama\\ezo2.txt", encoding='utf-8') as f:
    text = f.read()
EzoModel = markovify.NewlineText(text, state_size=2) """

def randomize_messages():
    global gala
    return gala[random.randrange(0,len(gala))].replace('@','')

def check_for_all_bot_prefixes():
    global finale
    global gala
    for i in range(500):
        if finale.startswith('.'): finale=randomize_messages()
        if finale.startswith('!'): finale=randomize_messages()
        if finale.startswith('d.'): finale=randomize_messages()
        if finale.startswith('--'): finale=randomize_messages()
        if finale.startswith('/'): finale=randomize_messages()
        if finale.startswith('fd'): finale=randomize_messages()

class MessageCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def haiku(self, ctx=commands.Context):
        await ctx.send('Haiku is currently disabled due to loss of the processed syllable dictionary as it was stored on the W:\\ drive.')
        # global finale
        # global gala
        # with open('C:\\Users\\EzoGaming\\yomama\\allmsg.txt', encoding='utf-8') as f:
        #     gala1=f.readlines()
        # gala=[]
        # for i in gala1:
        #     if len(i)<80 and len(i)>5:
        #         if len(i.split(" "))<=7 and 'processing' not in i.lower():
        #             i2=i
        #             for Just_To_Be_Sure in range(10):
        #                 i2=i2.replace("ohh","oh")
        #                 i2=i2.replace("oooh","ooh")
        #                 i2=i2.replace("aaa","aa")
        #             gala.append(i2.replace("'d",''))
        # drigma=''
        # thesy=0
        # finale=''
        # while thesy!=5 and 'http' not in drigma:
        #     thesy=0
        #     finale=""
        #     finale=randomize_messages()
        #     check_for_all_bot_prefixes()
        #     finale2=finale
        #     syl=syllablecount(finale2)
        #     thesy=syl
        #     if 'http' in finale2: thesy=99
        # drigma+=finale+'\n'
        # thesy=0
        # while thesy!=7 and 'http' not in drigma:
        #     thesy=0
        #     finale=""
        #     finale=randomize_messages()
        #     check_for_all_bot_prefixes()
        #     finale2=finale
        #     syl=syllablecount(finale2)
        #     thesy=syl
        #     if 'http' in finale2: thesy=99
        # drigma+=finale+'\n'
        # thesy=0
        # while thesy!=5 and 'http' not in drigma:
        #     thesy=0
        #     finale=""
        #     finale=randomize_messages()
        #     check_for_all_bot_prefixes()
        #     finale2=finale
        #     syl=syllablecount(finale2)
        #     thesy=syl
        #     if 'http' in finale2: thesy=99
        # drigma+=finale+'\n'
        # drigma=drigma.replace('\n\n','\n').replace('SPOILER_','DoNotReplaceThisWithSPOILER_ItsProbablyGore')
        # await ctx.send(drigma)#send the funny

    @commands.command()
    async def markov(self, ctx=commands.Context, size=2):
        if size>4: size=4
        text_model=MarkovModel
        if size!=2:
            with open("C:\\Users\\EzoGaming\\yomama\\allmsg.txt", encoding='utf-8') as f:
                text = f.read()
            text_model = markovify.NewlineText(text, state_size=size)
            class POSifiedText(markovify.Text):
                def word_split(self, sentence):
                    words = re.split(self.word_split_pattern, sentence)
                    words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
                    return words
                def word_join(self, words):
                    sentence = " ".join(word.split("::")[0] for word in words)
                    return sentence
        shit=0
        shits=[]
        while shit<5:
            temp = text_model.make_sentence()
            if str(temp) not in shits:
                if temp is not None:
                    shits.append(str(temp))
                    shit+=1
        finale=temp.replace('@','')
        await ctx.send(finale)

    @commands.command()
    async def usermarkov(self, ctx=commands.Context, user='Gigachad', size=2):
        debug_log('(Messages) DEBUG: '+user+' markov command issued with chain length of '+str(size))
        if size>4: size=4
        text_model=None
        if user.lower()=='danny': textpath="C:\\Users\\EzoGaming\\yomama\\danny.txt"
        if user.lower()=='pizzi': textpath="C:\\Users\\EzoGaming\\yomama\\pizzi.txt"
        if user.lower()=='cris': textpath="C:\\Users\\EzoGaming\\yomama\\cris.txt"
        if user.lower()=='queen': textpath="C:\\Users\\EzoGaming\\yomama\\queen.txt"
        if user.lower()=='maki': textpath="C:\\Users\\EzoGaming\\yomama\\maki.txt"
        if user.lower()=='leffrey': textpath="C:\\Users\\EzoGaming\\yomama\\leffrey.txt"
        if user.lower()=='bravo': textpath="C:\\Users\\EzoGaming\\yomama\\bravo.txt"
        if user.lower()=='ezo': textpath="C:\\Users\\EzoGaming\\yomama\\ezo2.txt"
        if user.lower()=='danny': text_model=DannyModel
        if user.lower()=='pizzi': text_model=PizziModel
        if user.lower()=='cris': text_model=CrisModel
        if user.lower()=='queen': text_model=QueenModel
        if user.lower()=='maki': text_model=MakiModel
        if user.lower()=='leffrey': text_model=LeffreyModel
        if user.lower()=='bravo': text_model=BravoModel
        if user.lower()=='ezo': text_model=EzoModel
        if text_model is None:
            debug_log('(Messages) ERROR: Not a user')
            await ctx.send('Please put a valid user')
        if size!=2:
            debug_log('(Messages) DEBUG: Building temporary model with new chain length...')
            with open(textpath, encoding='utf-8') as f:
                text = f.read()
            text_model = markovify.NewlineText(text, state_size=size)
            class POSifiedText(markovify.Text):
                def word_split(self, sentence):
                    words = re.split(self.word_split_pattern, sentence)
                    words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
                    return words
                def word_join(self, words):
                    sentence = " ".join(word.split("::")[0] for word in words)
                    return sentence
        shit=0
        shits=[]
        while shit<5:
            temp = text_model.make_sentence()
            if str(temp) not in shits:
                if temp is not None:
                    shits.append(str(temp))
                    shit+=1
        finale=temp.replace('@','')
        await ctx.send(finale)
    @commands.command()
    async def usermarkovprime(self, ctx=commands.Context, user='Gigachad', *inntext):
        debug_log('(Messages) DEBUG: '+user+' markov prime command issued')
        intext=" ".join(inntext)
        intext=intext.split(" ")
        ogintext=" ".join(intext[:-2])+" "
        intext=intext[-2:]
        intext=" ".join(intext)
        text_model=None
        if user.lower()=='danny': textpath="C:\\Users\\EzoGaming\\yomama\\danny.txt"
        if user.lower()=='pizzi': textpath="C:\\Users\\EzoGaming\\yomama\\pizzi.txt"
        if user.lower()=='cris': textpath="C:\\Users\\EzoGaming\\yomama\\cris.txt"
        if user.lower()=='queen': textpath="C:\\Users\\EzoGaming\\yomama\\queen.txt"
        if user.lower()=='maki': textpath="C:\\Users\\EzoGaming\\yomama\\maki.txt"
        if user.lower()=='leffrey': textpath="C:\\Users\\EzoGaming\\yomama\\leffrey.txt"
        if user.lower()=='bravo': textpath="C:\\Users\\EzoGaming\\yomama\\bravo.txt"
        if user.lower()=='ezo': textpath="C:\\Users\\EzoGaming\\yomama\\ezo2.txt"
        if user.lower()=='danny': text_model=DannyModel
        if user.lower()=='pizzi': text_model=PizziModel
        if user.lower()=='cris': text_model=CrisModel
        if user.lower()=='queen': text_model=QueenModel
        if user.lower()=='maki': text_model=MakiModel
        if user.lower()=='leffrey': text_model=LeffreyModel
        if user.lower()=='bravo': text_model=BravoModel
        if user.lower()=='ezo': text_model=EzoModel
        if text_model is None:
            debug_log('(Messages) ERROR: Not a user')
            await ctx.send('Please put a valid user')
        temp = text_model.make_sentence_with_start(intext, test_output=False)
        finale=temp.replace('@','')
        finale=ogintext+finale
        await ctx.send(finale)
    @commands.command()
    async def markovprime(self, ctx=commands.Context, *inntext):
        debug_log('(Messages) DEBUG: markov prime command issued')
        intext=" ".join(inntext)
        intext=intext.split(" ")
        ogintext=" ".join(intext[:-2])+" "
        intext=intext[-2:]
        intext=" ".join(intext)
        text_model=MarkovModel
        temp = text_model.make_sentence_with_start(intext, test_output=False)
        finale=temp.replace('@','')
        finale=ogintext+finale
        await ctx.send(finale)
    @commands.command()
    async def msg(self, ctx=commands.Context, amt=1):
        if ctx.guild==self.bot.get_guild(779136383033147403):
            with open('C:\\Users\\EzoGaming\\yomama\\allmsg.txt', encoding='utf-8') as f:
                gala=f.readlines()
            drigma=''
            for i in range(amt):
                finale="" 
                finale=gala[random.randrange(0,len(gala))].replace('@','')
                for i in range(500):
                    if finale.startswith('.'): finale=gala[random.randrange(0,len(gala))].replace('@','')
                    if finale.startswith('!'): finale=gala[random.randrange(0,len(gala))].replace('@','')
                    if finale.startswith('d.'): finale=gala[random.randrange(0,len(gala))].replace('@','')
                    if finale.startswith('--'): finale=gala[random.randrange(0,len(gala))].replace('@','')
                    if finale.startswith('/'): finale=gala[random.randrange(0,len(gala))].replace('@','')
                    if finale.startswith('fd'): finale=gala[random.randrange(0,len(gala))].replace('@','')
                    if 'googleuser' in finale: finale=gala[random.randrange(0,len(gala))].replace('@','')
                drigma+=finale+'\n'
            if 'status' in drigma: 
                drigma=drigma.replace('twitter.com','sxtwitter.com')
                drigma=drigma.replace('xsxtwitter.com','xtwitter.com')
                drigma=drigma.replace('fxtwitter.com','sxtwitter.com')
            drigma=drigma.replace('\n\n','\n').replace('SPOILER_','DoNotReplaceThisWithSPOILER_ItsProbablyGore')
            await ctx.send(drigma) #send the funny
        else:
            await ctx.send('This is not the Mickey Mouse Club! This command is confidential!')





    @commands.command()
    async def burping(self, ctx=commands.Context, user=''):
        if user=='leffrey': await ctx.send('https://media.discordapp.net/attachments/886788323648094219/990466077626609664/4740605377_1656215907176.gif')
        if user=='gilbert': await ctx.send('https://media.discordapp.net/attachments/886788323648094219/1004518046553096262/0527758303_1659566148896.gif')
        if user=='kneecap': await ctx.send('https://media.discordapp.net/attachments/886788323648094219/1004518483532447804/7797983935_1659566251717.gif')

        
    @commands.command()
    async def farting(self, ctx=commands.Context, user=''):
        if user=='leffrey': await ctx.send('https://media.discordapp.net/attachments/886788323648094219/1004518186563162133/1496101011_1659566182230.gif')
        if user=='bomb': await ctx.send('https://media.discordapp.net/attachments/886788323648094219/1004518911196270642/4084152685_1659566352561.gif')


    @commands.command()
    async def msg_asian(self, ctx=commands.Context, amt=1):
        if ctx.guild==self.bot.get_guild(779136383033147403):
            with open('C:\\Users\\EzoGaming\\yomama\\allmsg.txt', encoding='utf-8') as f:
                gala=f.readlines()
            drigma=''
            for i in range(amt):
                finale="" 
                finale=gala[random.randrange(0,len(gala))].replace('@','')
                for i in range(500):
                    yay=False
                    for i2 in finale: 
                        if is_cjk(i2):
                            yay=True
                    if not yay and i<498: finale=gala[random.randrange(0,len(gala))].replace('@','')
                    #if 'googleuser' in finale: finale=gala[random.randrange(0,len(gala))].replace('@','')
                    
                    
                drigma+=finale+'\n'
            if 'status' in drigma: 
                drigma=drigma.replace('twitter.com','sxtwitter.com')
                drigma=drigma.replace('xsxtwitter.com','xtwitter.com')
                drigma=drigma.replace('fxtwitter.com','sxtwitter.com')
            drigma=drigma.replace('\n\n','\n').replace('SPOILER_','DoNotReplaceThisWithSPOILER_ItsProbablyGore')
            await ctx.send(drigma) #send the funny
        else:
            await ctx.send('This is not the Mickey Mouse Club! This command is confidential!')



    @commands.command()
    async def longmsg(self, ctx=commands.Context, amt=1):
        if ctx.guild==self.bot.get_guild(779136383033147403):
            with open('C:\\Users\\EzoGaming\\yomama\\allmsg.txt', encoding='utf-8') as f:
                gala=f.readlines()
            drigma=''
            for i in range(amt):
                finale="" 
                finale=gala[random.randrange(0,len(gala))].replace('@','')
                for i in range(500):
                    yay=False
                    if len(finale.split(' '))>4:
                        yay=True
                    if not yay and i<498: finale=gala[random.randrange(0,len(gala))].replace('@','')
                    #if 'googleuser' in finale: finale=gala[random.randrange(0,len(gala))].replace('@','')
                    
                    
                drigma+=finale+'\n'
            if 'status' in drigma: 
                drigma=drigma.replace('twitter.com','sxtwitter.com')
                drigma=drigma.replace('xsxtwitter.com','xtwitter.com')
                drigma=drigma.replace('fxtwitter.com','sxtwitter.com')
            drigma=drigma.replace('\n\n','\n').replace('SPOILER_','DoNotReplaceThisWithSPOILER_ItsProbablyGore')
            await ctx.send(drigma) #send the funny
        else:
            await ctx.send('This is not the Mickey Mouse Club! This command is confidential!')

    @commands.command()
    async def link(self, ctx=commands.Context, amt=1):    
        if ctx.guild==self.bot.get_guild(779136383033147403):
            with open('C:\\Users\\EzoGaming\\yomama\\allmsg.txt', encoding='utf-8') as f:
                gala=f.readlines()
            drigma=''
            finale=''
            for i in range(amt):
                finale1=""
                for i in range(500):
                    finale1=gala[random.randrange(0,len(gala))].replace('@','')
                    if 'googleuser' not in finale1 and finale1.startswith('http'): finale=finale1
                drigma+=finale+'\n'
            drigma=drigma.replace('\n\n','\n').replace('SPOILER_','DoNotReplaceThisWithSPOILER_ItsProbablyGore')
            if 'status' in drigma: 
                drigma=drigma.replace('twitter.com','sxtwitter.com')
                drigma=drigma.replace('xsxtwitter.com','xtwitter.com')
                drigma=drigma.replace('fxtwitter.com','sxtwitter.com')
            await ctx.send(drigma) #send the funny
        else:
            await ctx.send('This is not the Mickey Mouse Club! This command is confidential!')

    @commands.command()
    async def msgsearch_old(self, ctx=commands.Context, *amt):    
        if ctx.guild==self.bot.get_guild(779136383033147403):
            with open('C:\\Users\\EzoGaming\\yomama\\allmsg.txt', encoding='utf-8') as f:
                gala=f.readlines()
            drigma=''
            finale=''
            for i in range(1):
                finale1=""
                for i in range(50000):
                    finale1=gala[random.randrange(0,len(gala))].replace('@','')
                    if 'googleuser' not in finale1 and ' '.join(amt).lower() in finale1.lower(): finale=finale1
                drigma+=finale+'\n'
            drigma=drigma.replace('\n\n','\n').replace('SPOILER_','DoNotReplaceThisWithSPOILER_ItsProbablyGore')
            if 'status' in drigma: 
                drigma=drigma.replace('twitter.com','sxtwitter.com')
                drigma=drigma.replace('xsxtwitter.com','xtwitter.com')
                drigma=drigma.replace('fxtwitter.com','sxtwitter.com')
            await ctx.send(drigma) #send the funny
        else:
            await ctx.send('This is not the Mickey Mouse Club! This command is confidential!')

    @commands.command()
    async def ft(self, ctx=commands.Context, *amt):  
        args={
            'query' : '',
            'before' : None,
            'after' : None,
            'on' : None,
            'in' : None,
            'by' : None,
            'has' : None,
            'before' : None
            }
        args_=args
        for i in amt:  
            if ':' in i:
                arg=i.split(':')
                for i2 in args: #i2 in args goes through the list of args so i dont have repeated code for 'before' 'after' 'on'
                    if arg[0]==i2: args_[i2]=arg[1]
            else:
                args_['query']+=i+' '
        args=args_
        try:
            if args['query'][-1]==' ': args['query']=args['query'][:-1]
        except:
            pass
        await ctx.send(args)

    @commands.command()
    async def msgsearch(self, ctx=commands.Context, *amt):    
        try:
            args={
                'query' : '',
                'before' : None,
                'after' : None,
                'on' : None,
                'in' : None,
                'by' : None,
                'has' : None,
                'before' : None
                }
            args_=args
            for i in amt:  
                if ':' in i:
                    arg=i.split(':')
                    for i2 in args: #i2 in args goes through the list of args so i dont have repeated code for 'before' 'after' 'on'
                        if arg[0]==i2: args_[i2]=arg[1]
                        if arg[0]=='from': args_['by']=arg[1]
                else:
                    args_['query']+=i+' '
            args=args_
            try:
                if args['query'][-1]==' ': args['query']=args['query'][:-1]
            except:
                pass
            if ctx.guild==self.bot.get_guild(779136383033147403):
                #todo: not have this be hardcoded, etc
                global safe_channels_
                safe_channels=safe_channels_
                g=self.bot.get_guild(779136383033147403)
                for channel in g.channels:
                    safe_channels.append(str(channel.id))
                safechannels=safe_channels
            else:
                safe_channels=[]
                g=ctx.message.guild
                for channel in g.channels:
                    safe_channels.append(str(channel.id))
                safechannels=safe_channels
            
            complicated=False
            complicated_2=False
            if args['in'] is not None:
                print(str(args['in']))
                safechannels=[args['in'].strip('<').strip('>').strip('#')]
                try:
                    if str(int(safechannels[0]))!=safechannels[0]: complicated=True
                except:
                    complicated=True
                    safechannels=safe_channels
                print(("it's "*complicated)+("it's not "*(not complicated))+'complicated')


                
            thingy=''
            if args['by'] is not None:
                zz=args['by'].strip('<').strip('>').strip('@')
                print(str(args['by']))
                try:
                    if str(int(zz))!=zz: complicated_2=True
                except:
                    complicated_2=True
                if not complicated_2: thingy+=' AND sender_id='+zz

            processed_stamp=0
            processed_stamp_start=0
            processed_stamp_end=0
            if args['before'] is not None:
                print(str(args['by']))
                thingy+=' AND timestamp<'+processed_stamp
            if args['after'] is not None:
                print(str(args['by']))
                thingy+=' AND timestamp>'+processed_stamp
            if args['before'] is not None:
                print(str(args['by']))
                thingy+=' AND timestamp>'+processed_stamp_start+' AND timestamp<'+processed_stamp_end
            #print('safe: '+str(safechannels))
            def ordinalize(num):
                suf=''
                if str(num)[-1]=='0': suf='th'
                if str(num)[-1]=='1': suf='st'
                if str(num)[-1]=='2': suf='nd'
                if str(num)[-1]=='3': suf='rd'
                if str(num)[-1]=='4': suf='th'
                if str(num)[-1]=='5': suf='th'
                if str(num)[-1]=='6': suf='th'
                if str(num)[-1]=='7': suf='th'
                if str(num)[-1]=='8': suf='th'
                if str(num)[-1]=='9': suf='th'
                return str(num)+suf

            con = sqlite3.connect('i:\\dht\\archiveREEAL.dht')

            cur = con.cursor()

            results=[]
            query=args['query']
            #await ctx.send('SELECT * FROM messages WHERE channel_id IN ('+(','.join(safechannels))+')')
            if complicated:
                safechannels=[]
                exc='SELECT * FROM channels'
                #await ctx.send(exc)
                for channel in cur.execute(exc):
                    print(channel[2])
                    if channel[2]==args['in'].replace('_',' ') and str(channel[0]) in safe_channels: safechannels.append(str(channel[0]))
                    
                print(safechannels)



            for message in cur.execute('SELECT * FROM messages WHERE channel_id IN ('+(','.join(safechannels))+')'+thingy):
                if query.replace('^','').lower() in message[3].lower(): results.append(message)


            results2=[]
            for i in results:
                if not 'mado' in str(i).lower():
                    if args['has']=='link':
                        if 'http' in i[3]: results2.append(i)
                    else:
                        results2.append(i)
                results=results2

            if '^' in query:
                results2=[]
                for i in results:
                    y=re.sub('r[^\W\d]','',i[3].lower()).split(' ')
                    if query.replace('^','').lower() in y:
                        print(y)
                        results2.append(i)
                results=results2
                res=random.choice(results)
            else:
                try:
                    res=random.choice(results)
                except:
                    res=results[0]
            msg_id=res[0]
            usr_id=res[1]
            chn_id=res[2]
            timest=res[4]
            is_bot=False
            is_gdm=False

            for channel in cur.execute('SELECT * FROM channels WHERE id='+str(chn_id)):
                srv_id=channel[1]
                chn_nm=channel[2]
                break

            if chn_id==srv_id: is_gdm=True

            if not is_gdm:
                for server in cur.execute('SELECT * FROM servers WHERE id='+str(srv_id)):
                    srv_nm=server[1]
                    break

            for user in cur.execute('SELECT * FROM users WHERE id='+str(usr_id)):
                if user[3] is None: is_bot=True
                usr_nm=str(user[1])+(('#'+str(user[3]))*(not is_bot))
                break

            time=datetime.utcfromtimestamp(int(timest)/1000).strftime('%A, %B replace, %Y at %I:%M:%S %p')
            goo=int(datetime.utcfromtimestamp(int(timest)/1000).strftime('%d'))
            time=time.replace('replace',ordinalize(goo))

            embeds=None
            for i in cur.execute('SELECT * FROM embeds WHERE message_id='+str(msg_id)):
                embeds=i
                print(i)
            
            attachments=[]
            for i in cur.execute('SELECT * FROM attachments WHERE message_id='+str(msg_id)):
                attachments.append(i[2:])
            if not is_gdm:
                ball='#'+chn_nm+' in server '+srv_nm
            else:
                ball='in GC '+chn_nm
            embed=discord.Embed(title=ball, description=res[3],color=0xEEE2A0,timestamp=datetime.utcfromtimestamp(int(timest)/1000))
            try: 
                gay_ass=await self.bot.fetch_user(usr_id)
            except:
                gay_ass=await self.bot.fetch_user(1065191458069557298)
            
            #print(await self.bot.fetch_user(usr_id))
            #print(await self.bot.fetch_user(158418656861093888))
            try:
                z=gay_ass.avatar_url
            except:
                z='https://cdn.discordapp.com/attachments/896060285763325962/1006518279478722642/85dcfc5d1408c7dfca0278377da1ee60.png'
            embed.set_author(name=usr_nm+(' 🤖'*is_bot), icon_url=z)
            embed.set_footer(text="MessageID: "+str(msg_id))
            zookler=''
            try:
                print(json.loads(embeds[1]))
            except:
                pass
            try:
                zookler=json.loads(embeds[1])['image']['url']
            except:
                try:
                    zookler=json.loads(embeds[1])['thumbnail']['url']
                except:
                    pass

            if len(attachments)>0:
                print(attachments)
                embed.set_image(url=attachments[0][2])
                print(zookler)
                if embeds: embed.set_image(url=zookler)
                await ctx.send(embed=embed)
                #await ctx.send(str(embeds))
            else:
                print(zookler)
                if embeds: embed.set_image(url=zookler)
                await ctx.send(embed=embed)
                #await ctx.send(str(embeds))
        
        except Exception as e:
        # except Exception as e:
            eror=traceback.format_exc()
            embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
            embed.set_footer(text='lmao')
            await ctx.reply(embed=embed)
    
    @commands.command()
    async def gogoo(self,ctx=commands.Context,*amt):
        for i in ctx.message.guild.channels:
            print(i.id)
    @commands.command(aliases=['wsi'])
    async def whosaidit(self,ctx=commands.Context,amt=None):
        if ctx.guild==self.bot.get_guild(779136383033147403):
            #todo: not have this be hardcoded, etc
            global safe_channels_
            safe_channels=safe_channels_
            g=self.bot.get_guild(779136383033147403)
            for channel in g.channels:
                safe_channels.append(str(channel.id))
            safechannels=safe_channels
            with open('users.json', 'r') as f:
                data = json.load(f)
        else:
            safe_channels=[]
            g=ctx.message.guild
            for channel in g.channels:
                safe_channels.append(str(channel.id))
            safechannels=safe_channels
            with open('users_ezo2.json', 'r') as f:
                data = json.load(f)

        con = sqlite3.connect('i:\\dht\\archiveREEAL.dht')

        cur = con.cursor()

        results=[]
        

        #with open('users.json', 'r') as f:
            #data = json.load(f)

        # Output: {'name': 'Bob', 'languages': ['English', 'French']}
        #print(data)
        safe_users=[]
        for i in data['users']:
            for i2 in range(int(i[2]*1)):
                safe_users.append(i[0])
        #print(safe_users)
        selected_user=random.choice(safe_users)
        #await ctx.send(selected_user)
        for message in cur.execute('SELECT * FROM messages WHERE channel_id IN ('+(','.join(safechannels))+') AND text NOT LIKE \'.%\' AND text NOT LIKE \'--%\' AND text NOT LIKE \'<@%\' AND text NOT LIKE \'n.%\' AND text NOT LIKE \'fd%\' AND text NOT LIKE \'d.%\' AND text NOT LIKE \'!%\' AND text NOT LIKE \'^%\' AND text NOT LIKE \'$%\' AND sender_id='+selected_user):
            results.append(message)
        testmsg=''
        result=(0, 0, 0, '', 0)
        tries=0
        while result[3] is '' or 'http' in result[3] or 'mado' in result[3].lower() and tries<100000:
            tries+=1
            if amt is None:
                print(result)
                result=random.choice(results)
            else:
                if amt=='lunatic' and tries<100000:
                    result=(0, 0, 0, 'jhdgjhdghkdsghykdghkdghkdghkghkdghkdghkdghkdgkgh', 0)
                    while len(result[3])>4 and tries<100000:
                        print(result)
                        result=random.choice(results)
                        tries+=1
                elif amt=='hard' and tries<100000:
                    result=(0, 0, 0, 'jhdgjhdghkdsghykdghkdghkdghkghkdghkdghkdghkdgkgh', 0)
                    while len(result[3])>12 and tries<100000:
                        print(result)
                        result=random.choice(results)
                        tries+=1
                elif amt=='easy' and tries<100000:
                    result=(0, 0, 0, '', 0)
                    while len(result[3])<25 and tries<100000:
                        print(result)
                        result=random.choice(results)
                        tries+=1
                elif amt=='peaceful' and tries<100000:
                    result=(0, 0, 0, '', 0)
                    while len(result[3])<90 and tries<100000:
                        print(result)
                        result=random.choice(results)
                        tries+=1
                else:
                    ctx.send('fuck you')
                    break
                        
        testmsg+=str(result)
        for i in data['users']:
            if i[0]==selected_user: correct_user=i[1]
        testmsg+='\ncorrect answer(s): '+str(correct_user)

        def ordinalize(num):
            suf=''
            if str(num)[-1]=='0': suf='th'
            if str(num)[-1]=='1': suf='st'
            if str(num)[-1]=='2': suf='nd'
            if str(num)[-1]=='3': suf='rd'
            if str(num)[-1]=='4': suf='th'
            if str(num)[-1]=='5': suf='th'
            if str(num)[-1]=='6': suf='th'
            if str(num)[-1]=='7': suf='th'
            if str(num)[-1]=='8': suf='th'
            if str(num)[-1]=='9': suf='th'
            return str(num)+suf

        msg_id=result[0]
        usr_id=result[1]
        chn_id=result[2]
        timest=result[4]

        time=datetime.utcfromtimestamp(int(timest)/1000).strftime('%A, %B replace, %Y at %I:%M:%S %p')
        goo=int(datetime.utcfromtimestamp(int(timest)/1000).strftime('%d'))
        time=time.replace('replace',ordinalize(goo))

        for channel in cur.execute('SELECT * FROM channels WHERE id='+str(chn_id)):
            srv_id=channel[1]
            chn_nm=channel[2]
            break

        ball='#'+chn_nm



        embed=discord.Embed(title=ball, description=result[3],color=0xEEE2A0,timestamp=datetime.utcfromtimestamp(int(timest)/1000))
        embed.set_author(name='???', icon_url='https://archive.org/download/discordprofilepictures/discordblue.png')


        botmessage=await ctx.reply(ctx.message.author.display_name+': this is your question',embed=embed, mention_author=False)
        def check(message):
            #print(message.channel)
            #print(botmessage.channel)
            return message.channel == botmessage.channel and message.author == ctx.message.author
        msg = await self.bot.wait_for("message",check=check)

        if msg.content.lower() in correct_user:
            await msg.reply('correct!', mention_author=False)
        else:
            await msg.reply('incorrect - correct user: '+str(correct_user), mention_author=False)

        for user in cur.execute('SELECT * FROM users WHERE id='+str(usr_id)):
            usr_nm=str(user[1])+(('#'+str(user[3])))
            break
        gay_ass=await self.bot.fetch_user(usr_id)
        try:
            z=gay_ass.avatar_url
        except:
            z='https://cdn.discordapp.com/attachments/896060285763325962/1006518279478722642/85dcfc5d1408c7dfca0278377da1ee60.png'
        embed.set_author(name=usr_nm, icon_url=z)
        embed.set_footer(text="MessageID: "+str(msg_id))
        await botmessage.edit(embed=embed)


    @commands.command()
    async def filesearch(self, ctx=commands.Context, *amt):    
        try:
            args={
                'query' : '',
                'before' : None,
                'after' : None,
                'on' : None,
                'in' : None,
                'by' : None,
                'has' : None,
                'before' : None
                }
            args_=args
            for i in amt:  
                if ':' in i:
                    arg=i.split(':')
                    for i2 in args: #i2 in args goes through the list of args so i dont have repeated code for 'before' 'after' 'on'
                        if arg[0]==i2: args_[i2]=arg[1]
                        if arg[0]=='from': args_['by']=arg[1]
                else:
                    args_['query']+=i+' '
            args=args_
            try:
                if args['query'][-1]==' ': args['query']=args['query'][:-1]
            except:
                pass
            if ctx.guild==self.bot.get_guild(779136383033147403):
                #todo: not have this be hardcoded, etc
                global safe_channels_
                safe_channels=safe_channels_
                g=self.bot.get_guild(779136383033147403)
                for channel in g.channels:
                    safe_channels.append(str(channel.id))
                safechannels=safe_channels
            else:
                safe_channels=[]
                g=ctx.message.guild
                for channel in g.channels:
                    safe_channels.append(str(channel.id))
                safechannels=safe_channels
            
            complicated=False
            complicated_2=False
            if args['in'] is not None:
                print(str(args['in']))
                safechannels=[args['in'].strip('<').strip('>').strip('#')]
                try:
                    if str(int(safechannels[0]))!=safechannels[0]: complicated=True
                except:
                    complicated=True
                    safechannels=safe_channels
                print(("it's "*complicated)+("it's not "*(not complicated))+'complicated')


                
            thingy=''
            if args['by'] is not None:
                zz=args['by'].strip('<').strip('>').strip('@')
                print(str(args['by']))
                try:
                    if str(int(zz))!=zz: complicated_2=True
                except:
                    complicated_2=True
                if not complicated_2: thingy+=' AND sender_id='+zz

            processed_stamp=0
            processed_stamp_start=0
            processed_stamp_end=0
            if args['before'] is not None:
                print(str(args['by']))
                thingy+=' AND timestamp<'+processed_stamp
            if args['after'] is not None:
                print(str(args['by']))
                thingy+=' AND timestamp>'+processed_stamp
            if args['before'] is not None:
                print(str(args['by']))
                thingy+=' AND timestamp>'+processed_stamp_start+' AND timestamp<'+processed_stamp_end
            #print('safe: '+str(safechannels))
            def ordinalize(num):
                suf=''
                if str(num)[-1]=='0': suf='th'
                if str(num)[-1]=='1': suf='st'
                if str(num)[-1]=='2': suf='nd'
                if str(num)[-1]=='3': suf='rd'
                if str(num)[-1]=='4': suf='th'
                if str(num)[-1]=='5': suf='th'
                if str(num)[-1]=='6': suf='th'
                if str(num)[-1]=='7': suf='th'
                if str(num)[-1]=='8': suf='th'
                if str(num)[-1]=='9': suf='th'
                return str(num)+suf

            con = sqlite3.connect('i:\\dht\\archiveREEAL.dht')

            cur = con.cursor()

            results=[]
            query=args['query']
            #await ctx.send('SELECT * FROM messages WHERE channel_id IN ('+(','.join(safechannels))+')')
            if complicated:
                safechannels=[]
                exc='SELECT * FROM channels'
                #await ctx.send(exc)
                for channel in cur.execute(exc):
                    print(channel[2])
                    if channel[2]==args['in'].replace('_',' ') and str(channel[0]) in safe_channels: safechannels.append(str(channel[0]))
                    
                print(safechannels)



            for message in cur.execute('SELECT * FROM messages WHERE channel_id IN ('+(','.join(safechannels))+')'+thingy):
                if query.replace('^','').lower() in message[3].lower(): results.append(message)


            results2=[]
            for i in results:
                if not 'mado' in str(i).lower():
                    if args['has']=='link':
                        if 'http' in i[3]: results2.append(i)
                    else:
                        results2.append(i)
                results=results2

            if '^' in query:
                results2=[]
                for i in results:
                    y=re.sub('r[^\W\d]','',i[3].lower()).split(' ')
                    if query.replace('^','').lower() in y:
                        print(y)
                        results2.append(i)
                results=results2
                res=random.choice(results)
            else:
                try:
                    res=random.choice(results)
                except:
                    res=results[0]
            msg_id=res[0]
            usr_id=res[1]
            chn_id=res[2]
            timest=res[4]
            is_bot=False
            is_gdm=False

            for channel in cur.execute('SELECT * FROM channels WHERE id='+str(chn_id)):
                srv_id=channel[1]
                chn_nm=channel[2]
                break

            if chn_id==srv_id: is_gdm=True

            if not is_gdm:
                for server in cur.execute('SELECT * FROM servers WHERE id='+str(srv_id)):
                    srv_nm=server[1]
                    break

            for user in cur.execute('SELECT * FROM users WHERE id='+str(usr_id)):
                if user[3] is None: is_bot=True
                usr_nm=str(user[1])+(('#'+str(user[3]))*(not is_bot))
                break

            time=datetime.utcfromtimestamp(int(timest)/1000).strftime('%A, %B replace, %Y at %I:%M:%S %p')
            goo=int(datetime.utcfromtimestamp(int(timest)/1000).strftime('%d'))
            time=time.replace('replace',ordinalize(goo))

            embeds=None
            for i in cur.execute('SELECT * FROM embeds WHERE message_id='+str(msg_id)):
                embeds=i
                print(i)
            
            attachments=[]
            for i in cur.execute('SELECT * FROM attachments WHERE message_id='+str(msg_id)):
                attachments.append(i[2:])
            if not is_gdm:
                ball='#'+chn_nm+' in server '+srv_nm
            else:
                ball='in GC '+chn_nm
            embed=discord.Embed(title=ball, description=res[3],color=0xEEE2A0,timestamp=datetime.utcfromtimestamp(int(timest)/1000))
            gay_ass=await self.bot.fetch_user(usr_id)
            print(await self.bot.fetch_user(usr_id))
            print(await self.bot.fetch_user(158418656861093888))
            try:
                z=gay_ass.avatar_url
            except:
                z='https://cdn.discordapp.com/attachments/896060285763325962/1006518279478722642/85dcfc5d1408c7dfca0278377da1ee60.png'
            embed.set_author(name=usr_nm+(' 🤖'*is_bot), icon_url=z)
            embed.set_footer(text="MessageID: "+str(msg_id))
            zookler=''
            try:
                print(json.loads(embeds[1]))
            except:
                pass
            try:
                zookler=json.loads(embeds[1])['image']['url']
            except:
                try:
                    zookler=json.loads(embeds[1])['thumbnail']['url']
                except:
                    pass

            if len(attachments)>0:
                print(attachments)
                embed.set_image(url=attachments[0][2])
                print(zookler)
                if embeds: embed.set_image(url=zookler)
                await ctx.send(embed=embed)
                #await ctx.send(str(embeds))
            else:
                print(zookler)
                if embeds: embed.set_image(url=zookler)
                await ctx.send(embed=embed)
                #await ctx.send(str(embeds))
        
        except Exception as e:
        # except Exception as e:
            eror=traceback.format_exc()
            embed=discord.Embed(title='Error', color=0xee2211, description='`'+eror+'`')
            embed.set_footer(text='lmao')
            await ctx.reply(embed=embed)



    @commands.command()
    async def sitelink(self, ctx=commands.Context, site=None, amt=1):    
        if site is not None:
            if ctx.guild==self.bot.get_guild(779136383033147403):
                with open('C:\\Users\\EzoGaming\\yomama\\allmsg.txt', encoding='utf-8') as f:
                    gala=f.readlines()
                drigma=''
                finale=''
                for i in range(amt):
                    finale1=""
                    for i in range(160000):
                        finale1=gala[random.randrange(0,len(gala))].replace('@','')
                        if 'googleuser' not in finale1 and finale1.startswith('http') and site in finale1: 
                            finale=finale1
                            break
                    drigma+=finale+'\n'
                if 'status' in drigma: 
                    drigma=drigma.replace('twitter.com','sxtwitter.com')
                    drigma=drigma.replace('xsxtwitter.com','xtwitter.com')
                    drigma=drigma.replace('fxtwitter.com','sxtwitter.com')
                drigma=drigma.replace('\n\n','\n').replace('SPOILER_','DoNotReplaceThisWithSPOILER_ItsProbablyGore')
                                        
                await ctx.send(drigma) #send the funny
            else:
                await ctx.send('This is not the Mickey Mouse Club! This command is confidential!')
        else:
            await ctx.send('Please provide a website.')




def setup(bot: commands.Bot):
    bot.add_cog(MessageCommands(bot))
