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


global grokqueue
grokqueue=[]
matplotlib.use('Agg') # necessary for headless mode  
# see http://stackoverflow.com/a/3054314/3524528




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

global vc2

#Set Up Teh Loggah!
import logging
log_format = '[%(name)s] %(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(format=log_format,datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger=logging.getLogger('MUSIC')





class UtilityCommands(commands.Cog):

    

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        global vc
        global vc2
        





    @commands.command()
    async def play(self, ctx: commands.Context, *, fuck=''):
        ffmpath='L:\\School_tmp\\2021-22 School Year\\Clevster Flash Drive 1\\VideoProcessing\\ffmpeg.exe'
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        await ctx.send('Started playing: something')
        vc.play(discord.FFmpegPCMAudio(r'C:\Users\EzoGaming\Documents\Image-Line\Data\FL Studio\Projects\fanboiy and grand dad\flintboy and grum grum.mp3', executable=ffmpath), after=lambda e: print('done', e))
        
        
        
        
def setup(bot: commands.Bot):
    bot.add_cog(UtilityCommands(bot))
