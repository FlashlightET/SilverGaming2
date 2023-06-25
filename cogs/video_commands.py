from discord.ext import commands
from discord import File
import random
import requests
import subprocess
from .silverutil import wtitle

#Set Up Teh Loggah!
import logging
log_format = '[%(name)s] %(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(format=log_format,datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger=logging.getLogger('VIDEO')






class VideoCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def concat(self, ctx = commands.Context, *vids):
        #vid1=requests.get(vid1url)
        #vid2=requests.get(vid2url)
        #with open('r:\\vid1.mkv', 'wb') as f: 
        #    f.write(vid1.content)
        #with open('r:\\vid2.mkv', 'wb') as f: 
        #    f.write(vid2.content)
        #subprocess.check_call('ffmpeg -i r:\\vid1.mkv -i r:\\vid2.mkv -filter_complex "[0:v]scale=1024:576,setsar=1:1[v0]; [1:v]scale=1024:576,setsar=1:1[v1]; [v0][0:a][v1][1:a]concat=n=2:v=1:a=1[v][a]" -map [v] -map [a] -r 30 r:\\concat.mp4 -y', shell=True)
        i2=0
        cmd=""
        cmd+="ffmpeg "
        hasaudio=[]
        filez=[]
        for i in vids:
            fat=0
            with open('r:\\vid'+str(i2)+'.mkv', 'wb') as f: 
                if 'http' in i:
                    vid=requests.get(i)
                    f.write(vid.content)
                    cmd+='-i r:\\vid'+str(i2)+'.mkv '
                    vid='r:\\vid'+str(i2)+'.mkv'
                else:
                    fat=1
                    vid=i
            cum='ffprobe "'+vid+'"'
            ffprobe_output = subprocess.check_output(cum,stderr=subprocess.STDOUT).decode('utf-8')
            if "Audio:" not in ffprobe_output:
                hasaudio.append(0)
                logger.info("no sound")
                if fat==1: cmd+='-i "'+i+'.mkv" '
            if "Audio:" in ffprobe_output:
                hasaudio.append(1)
                logger.info("sound")
                if fat==1: cmd+='-i "'+i+'" '
            print(ffprobe_output)
            print(hasaudio)
            filez.append(vid)
            i2+=1
        cmd+=' -filter_complex "'
        #i2=# of videos
        for i in range(i2): #idk what this does but its in the ffmpeg command
            cmd+="["+str(i)+":v]scale=576x576,setsar=1:1[v"+str(i)+"]; "
        for i in range(i2): #idk what this does but its in the ffmpeg command
            cmd+="[v"+str(i)+"]["+str(i)+":a]"
        #n=number of videos which is i2
        cmd+='concat=n='+str(i2)+':v=1:a=1[v][a]" -map [v] -map [a] -r 30 -fs 6M -b:v 400k r:\\concat.mp4 -y'
        print(cmd)
        
        for i in range(i2):
            if hasaudio[i]==0:
                came='ffmpeg -y -i "'+filez[i]+'" -f lavfi -i anullsrc=cl=3 -shortest -c:v libx264 -c:a aac "'+filez[i]+'.mkv"'
                subprocess.check_call(came, shell=True)
                filez[i]=filez[i]+".mkv"
                logger.info('came='+came)

        #[v0][0:a][v1][1:a]concat=n=2:v=1:a=1[v][a]" -map [v] -map [a] -r 30 r:\\




        subprocess.check_call(cmd, shell=True)

        
        with open('r:\\concat.mp4', 'rb') as f:
            await ctx.send(file=File(f, 'concat.mp4')) #send the funny
        
    @commands.command()
    async def loggertest(self, ctx = commands.Context):
        logger=logging.getLogger('TEST_LOGGER')

        logger.info('hello mario')

    @commands.command()
    async def feverdream(self, ctx = commands.Context, aaaa="no", count=20):
        weewee=int(str(count))
        logger=logging.getLogger('FEVERDREAM')
        logger.info(weewee)
        global processing
        global fn
        ##processing=1
        try:
            if int(aaaa)!=0:
                funny=requests.get(ctx.message.attachments[0].url) #sets url to attached
                fileUrl=ctx.message.attachments[0].url#sets url to attached
                weewee=aaaa
            else:
                if(aaaa!="no"): #if its no it means theres no link
                    funny=requests.get(aaaa) #sets url to link
                    fileUrl=aaaa #sets url to link
                else:
                    funny=requests.get(ctx.message.attachments[0].url) #sets url to attached
                    fileUrl=ctx.message.attachments[0].url#sets url to attached
        except ValueError:
            if(aaaa!="no"): #if its no it means theres no link
                funny=requests.get(aaaa) #sets url to link
                fileUrl=aaaa #sets url to link
            else:
                funny=requests.get(ctx.message.attachments[0].url) #sets url to attached
                fileUrl=ctx.message.attachments[0].url#sets url to attached
        fn='r:\\repost\\in.'+(fileUrl[-6:].split(".", 1)[1]) #file name
        with open(fn, 'wb') as f: 
            f.write(funny.content) #saves file
        progmsg = await ctx.send("ok, reposting (this might take a while)")
        #ffm(countweewee)
        subprocess.check_call('ffmpeg -i '+fn+' r:\\repost\\out2.mkv -y', shell=True)
        the_nda=weewee#math.floor(int(str(weewee))/2)
        vcodecs=['h264','flv', 'mjpeg', 'libx264', 'libxvid', 'libtheora']
        acodecs=['aac','ac3','libopus','libvorbis','libmp3lame']
        pixfmt=['yuv420p','yuv422p','yuv444p','rgb24']
        resolutions=['320x240','376x240', '352x288','480x320','272x340','432x240','480x234', '427x240', '360x240', '312x390','480x272','640x320','640x360','480x360','852x480','854x480','864x480','720x480','640x480','960x544','1280x720','240x240','360x360','320x320','480x480','640x640','270x270','176x144','720x720']
        framerates=[23.976,24,25,29.97,30,30.01]
        presets=['medium', 'fast', 'ultrafast', 'veryfast']
        for i in range(0,int(str(the_nda))):
            wtitle("Mpreg ("+str(i)+"/"+str(int(str(the_nda)))+")")
            scale1=round((160*random.randrange(2,4))/8)*8
            scale=round((120*random.randrange(2,4))/8)*8
            try:
                subprocess.check_call('ffmpeg -i r:\\repost\\out2.mkv -c:v '+random.choice(vcodecs)+' -c:a '+random.choice(acodecs)+' -b:v '+str(random.randrange(1,100)*10)+'K -b:a '+str(random.randrange(6,25)*10)+'K -vf scale='+random.choice(resolutions)+' -pix_fmt '+random.choice(pixfmt)+' -r '+str(random.choice(framerates))+' -preset '+str(random.choice(presets))+' r:\\repost\\out1.mkv -y', shell=True)
            except:
                pass
            print("reposted "+str((i*2)+1)+" time(s)")
            if (i*2) % 5 == 0: await progmsg.edit(content="ok, reposting (this might take a while)\nprogress: "+str(int(((i*2)/20)*50))+'%')
            scale1=round((160*random.randrange(2,4))/8)*8
            scale=round((120*random.randrange(2,4))/8)*8
            try:
                subprocess.check_call('ffmpeg -i r:\\repost\\out1.mkv -c:v '+random.choice(vcodecs)+' -c:a '+random.choice(acodecs)+' -b:v '+str(random.randrange(1,100)*10)+'K -b:a '+str(random.randrange(6,25)*10)+'K -vf scale='+random.choice(resolutions)+' -pix_fmt '+random.choice(pixfmt)+' -r '+str(random.choice(framerates))+' -preset '+str(random.choice(presets))+' r:\\repost\\out2.mkv -y', shell=True)
            except:
                pass
            print("reposted "+str((i*2)+2)+" time(s)")
            if ((i*2)+1) % 5 == 0: await progmsg.edit(content="ok, reposting (this might take a while)\nprogress: "+str(int((((i*2)+1)/20)*50))+'%')
        subprocess.check_call('ffmpeg -i r:\\repost\\out2.mkv -c:v h264 -b:v 400K r:\\repost\\final.mp4 -y', shell=True)
        await progmsg.edit(content="ok, reposting (this might take a while)\nprogress: "+str(int((((i*2)+1)/20)*50))+'%')
        with open('r:\\repost\\final.mp4', 'rb') as f:
            await ctx.send(file=File(f, 'mpreg.mp4')) #send the funny

def setup(bot: commands.Bot):
    bot.add_cog(VideoCommands(bot))