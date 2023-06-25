import random
import json
import ctypes
from datetime import datetime

#Set Up Teh Loggah!
import logging
log_format = '[%(name)s] %(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(format=log_format,datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger=logging.getLogger('SILVERUTIL')






def RandomNumber():
    return str(random.randint(0,9))

def generateUUID():
    return RandomNumber()+RandomNumber()+RandomNumber()+RandomNumber()
    
def get_token():
    with open("h:\\NO PEEKING.txt", 'r') as text:
        return text.readline()
        

def get_lang(zah_,locale='en_ca'):
    key=zah_
    if key.startswith('ezoLang'): 
        key=zah_[:-1]
        key=key.replace('ezoLang(','')
    loc=locale
    if locale=='en_ca': loc='en_en'
    if locale=='en_uk': loc='en_en'
    with open("h:\\frart\\lang\\"+loc+".txt", 'r', encoding='UTF-8') as LangFile:
        data3=LangFile.readlines()
    with open("h:\\frart\\lang\\en_us.txt", 'r', encoding='UTF-8') as LangFile:
        data4=LangFile.readlines()
        data2=data3+data4
        for i in data2:
            i2=i.split('=')
            locator=i2[0]
            text="=".join(i2[1:])
            print(locator)
            print(key)
            if text[-2:-1]=='\r\n':
                text=text[:-2]
            try:
                if text[-1]=='\n':
                    text=text[:-1]
            except:
                pass
            if locator==key: return text


def get_data(key):
    with open("h:\\frart\\dataLang.json", 'r', encoding='UTF-8') as JsonFile:
        data=json.load(JsonFile)[key]
    print(data)
    print('PENIS????')
    try:
        if 'ezoLang' in data:
            print('zolamba')
            data=get_lang(data)
    except:
        pass
    return data


        
def wtitle(title):
    ctypes.windll.kernel32.SetConsoleTitleW("SilverGaming - "+title)

def debug_log(status):
    print(str(datetime.now())+' '+status)