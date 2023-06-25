from discord.ext import commands
from discord import File
import subprocess
import requests
from .silverutil import debug_log

#Set Up Teh Loggah!
import logging
log_format = '[%(name)s] %(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(format=log_format,datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger=logging.getLogger('MANIPULATION')



def upscalscripte():
    subprocess.check_call('conda activate matte & python "W:\\ai\\RobustVideoMatting\\bg.py"', shell=True) #upscaled

class ManipulationCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def greenscreen(self, ctx: commands.Context, aaaa=None):
        debug_log('(Greenscreen) DEBUG: Command issued')
        global globalmodel
        global model
        if(aaaa!=None): #if its none it means theres no link
            debug_log('(Greenscreen) DEBUG: Linked')
            funny=requests.get(aaaa) #sets url to link
            fileUrl=aaaa #sets url to link
            debug_log('(Greenscreen) DEBUG: '+fileUrl)
        else:
            debug_log('(Greenscreen) DEBUG: Attached')
            funny=requests.get(ctx.message.attachments[0].url) #sets url to attached
            fileUrl=ctx.message.attachments[0].url#sets url to attached
            debug_log('(Greenscreen) DEBUG: '+fileUrl)
        #os.makedirs('input_'+uuid, exist_ok=True)
        fn='bg_input.mp4' #file name
        debug_log('(Greenscreen) DEBUG: Saving file...')
        with open(fn, 'wb') as f: 
            f.write(funny.content) #saves file
        debug_log('(Greenscreen) DEBUG: Running...')
        result = await self.bot.loop.run_in_executor(None, upscalscripte)
        debug_log('(Greenscreen) DEBUG: Finished, uploading...')
        await ctx.send("uploading... (this may take a while for larger files)") #feedback
        with open('bg_output.mp4', 'rb') as f:
            await ctx.reply(file=File(f, 'removed.mp4')) #send the funny








def setup(bot: commands.Bot):
    bot.add_cog(ManipulationCommands(bot))