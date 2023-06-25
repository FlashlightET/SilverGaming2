from discord.ext import commands
from discord import File
import random
import requests
import subprocess
from .silverutil import wtitle

class StableCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def stable(self, ctx = commands.Context, *vids):
        subprocess.check_call('conda activate uvr & python "upscaler\\upscale.py" "'+modl+'" --alpha_mode 2 --input input_'+uuuid, shell=True) #upscaled

def setup(bot: commands.Bot):
    bot.add_cog(StableCommands(bot))