#AI_Commands
import discord
from discord.ext import commands
from .silverutil import get_data
from .silverutil import generateUUID
from .silverutil import debug_log
import traceback
import random
import os
import time
from discord import File
import requests
import urllib
from PIL import Image
from discord.ext import commands
import subprocess
import math

#Set Up Teh Loggah!
import logging
log_format = '[%(name)s] %(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(format=log_format,datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger=logging.getLogger('AI')



speed=get_data("upload")/8000

def upscale_script(uuuid='null', modl='null'):
    global model
    subprocess.check_call('conda activate uvr & python "upscaler\\upscale.py" "'+modl+'" --alpha_mode 2 --input input_'+uuuid, shell=True) #upscaled
bot = commands.Bot(help_command=None,command_prefix=['. ','.'])
client=discord.Client()


class NeuralCommands(commands.Cog):
    ctx=commands.Context

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def modellist(self, ctx=ctx, scale=0):
        scalestring=str(scale)+'x'
        NOE=25
        if scale==0: scalestring='all scales'
        models=get_data("models")
        for i2 in range(0,math.ceil(len(models)/25)):
            lis1=''
            lis2=''
            embed=discord.Embed(title='Model list', description='Scale: '+scalestring)
            namber=0
            for modl in range(0+(i2*NOE),NOE+(i2*NOE)):
                try:
                    model=models[modl]
                    if model[1]==str(scale)+'x' or scale==0: 
                        lis1+='`'
                        lis2+='`'
                        if scale==0: lis1+=model[1]+': '
                        lis1+=model[0]+'`\n'
                        lis2+=model[2]+'`\n'
                        namber+=1
                except IndexError: #This is typically because it just went out of the list.
                    pass 
            if namber>0:
                embed.add_field(name="alias", value=lis1, inline=True)
                embed.add_field(name="model", value=lis2, inline=True)
                await ctx.send(embed=embed)

    @bot.command(brief='.upscale [image or attachment]: runs an interpolated anime upscale model', description='.w2x [image or attachment]: waifu2xes an image')
    async def upscale(self,ctx=ctx, inmodel=None, attach=None):
        uuid=generateUUID()
        global globalmodel
        global model
        if(attach is not None):
            fileRequest=requests.get(attach) #sets url to link
        else:
            fileRequest=requests.get(ctx.message.attachments[0].url) #sets url to attached
        os.makedirs('input_'+uuid, exist_ok=True)
        os.makedirs('input_'+uuid, exist_ok=True)
        os.makedirs('input_'+uuid, exist_ok=True)
        os.makedirs('input_'+uuid, exist_ok=True)
        os.makedirs('input_'+uuid, exist_ok=True)
        os.makedirs('input_'+uuid, exist_ok=True)
        os.makedirs('input_'+uuid, exist_ok=True)
        os.makedirs('input_'+uuid, exist_ok=True)
        os.makedirs('input_'+uuid, exist_ok=True)
        os.makedirs('input_'+uuid, exist_ok=True)
        os.makedirs('input_'+uuid, exist_ok=True)
        os.makedirs('input_'+uuid, exist_ok=True)
        os.system('mkdir input_'+uuid)
        fn='input_'+uuid+'\\waifuin_'+uuid+'.png' #file name
        with open(fn, 'wb') as f: 
            f.write(fileRequest.content) #saves file
        synonyms=get_data("models")
        for modele in synonyms:
            debug_log('(AI) DEBUG: '+ str(modele))
            modelnick=modele[0]
            modeldir=modele[1]
            modelname=modele[2]
            if modelnick==inmodel:
                model="H:\\Users\\Flashlight Bulbton\\esrgan\\esr2\\models\\"+modeldir+"\\"+modelname
                debug_log('(AI) DEBUG: ' + str(model))
                globalmodel=modelname
        await ctx.send("upscaling with "+str(globalmodel)+"...") #feedback
        result = await bot.loop.run_in_executor(None, upscale_script, uuid, model)
        debug_log('(AI) DEBUG: '+ str(result))
        size=os.path.getsize("output\\waifuin_"+uuid+".png")/1000000 #size of image in MB
        if size>7.8:
            subprocess.check_call('magick convert output\\waifuin_'+uuid+'.png output\\waifuin_'+uuid+'.jpg', shell=True)
            size=os.path.getsize("output\\waifuin_"+uuid+".jpg")/1000000 #size of image in MB
            time=size/speed #usual upload speed in Mbit/8
            await ctx.send("uploading... (this may take a while for larger files, approx. "+str(round(time*10)/10)+" seconds.)") #feedback
            with open('output\\waifuin_'+uuid+'.jpg', 'rb') as f:
                await ctx.reply(file=File(f, 'mangout.jpg')) #send the funny
        else:
            time=size/speed #usual upload speed in Mbit/8
            await ctx.send("uploading... (this may take a while for larger files, approx. "+str(round(time*10)/10)+" seconds.)") #feedback
            with open('output\\waifuin_'+uuid+'.png', 'rb') as f:
                await ctx.reply(file=File(f, 'mang.png')) #send the funny

    @commands.command()
    async def downscale(self, ctx=ctx, factor=None, method_=None, InputUrl_=None):
        InputUrl=InputUrl_
        method=method_
        if method is not None:
            if 'http' in method:
                InputUrl=method_
                method=None
        if(InputUrl is not None): #if its gay it means theres no link
            FileUrl=requests.get(InputUrl) #sets url to link
        else:
            FileUrl=requests.get(ctx.message.attachments[0].url) #sets url to attached
        fn='imurder.png' #file name
        with open(fn, 'wb') as f: 
            f.write(FileUrl.content) #saves file
        await ctx.send("downscaling...") #feedback
        im = Image.open(fn)
        width, height = im.size
        if method is None:
            im1 = im.resize((int(width/float(factor)),int(height/float(factor))))
        else:
            print(method.lower().replace('_','-'))
            if 'near' in method.lower().replace('_','-'): samp=Image.NEAREST
            if 'line' in method.lower().replace('_','-'): samp=Image.BILINEAR
            if 'cubi' in method.lower().replace('_','-'): samp=Image.BICUBIC
            if 'lanc' in method.lower().replace('_','-'): samp=Image.LANCZOS
            if 'alia' in method.lower().replace('_','-'): samp=Image.ANTIALIAS
            if 'box'  in method.lower().replace('_','-'): samp=Image.BOX
            im1 = im.resize((int(width/float(factor)),int(height/float(factor))),resample=samp)
        im1.save('downscaled.png')
        with open('downscaled.png', 'rb') as f:
                await ctx.reply(file=File(f, 'downscaled.png')) #send the funny





def setup(bot: commands.Bot):
    bot.add_cog(NeuralCommands(bot))