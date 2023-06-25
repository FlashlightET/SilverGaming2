import random
import json
import ctypes
from datetime import datetime
def RandomNumber():
    return str(random.randint(0,9))

def generateUUID():
    return RandomNumber()+RandomNumber()+RandomNumber()+RandomNumber()
    
def get_token():
    with open("h:\\NO PEEKING.txt", 'r') as text:
        return text.readline()
        

def get_lang(zah_):
    key=zah_
    if key.startswith('ezoLang'): 
        key=zah_[:-1]
        key=key.replace('ezoLang(','')
    with open("h:\\frart\\en_us.json", 'r', encoding='UTF-8') as LangFile:
        data2=LangFile.readlines()
        for i in data2:
            i2=i.split('=')
            locator=i2[0]
            text="=".join(i2[1:])
            print(locator)
            print(key)
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