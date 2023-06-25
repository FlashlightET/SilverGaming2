import num2words
import re
from num2words import num2words
def opencmu(let):
    with open('w:\\scripts\\syllables\\cmu-'+let+'.txt') as dic:
        cmyu=dic.readlines()
    cmu2=cmyu
    cmyu=[]
    for i in cmu2:
        if not i.startswith(';'):
            i2=i.strip('\r')
            i2=i.strip('\n')
            cmyu.append(i2.lower())
    return cmyu
def syllablecount(intext):
    cmu_a=opencmu('a')
    cmu_b=opencmu('b')
    cmu_c=opencmu('c')
    cmu_d=opencmu('d')
    cmu_e=opencmu('e')
    cmu_f=opencmu('f')
    cmu_g=opencmu('g')
    cmu_h=opencmu('h')
    cmu_i=opencmu('i')
    cmu_j=opencmu('j')
    cmu_k=opencmu('k')
    cmu_l=opencmu('l')
    cmu_m=opencmu('m')
    cmu_n=opencmu('n')
    cmu_o=opencmu('o')
    cmu_p=opencmu('p')
    cmu_q=opencmu('q')
    cmu_r=opencmu('r')
    cmu_s=opencmu('s')
    cmu_t=opencmu('t')
    cmu_u=opencmu('u')
    cmu_v=opencmu('v')
    cmu_w=opencmu('w')
    cmu_x=opencmu('x')
    cmu_y=opencmu('y')
    cmu_z=opencmu('z')
    text=intext.replace('’',"'")
    re.sub('\W+','',text).strip()
    text2=text.replace("x's","x s")
    text2=text.replace("'s","")
    #print(text2)
    text2=text2.replace("n't","nt")
    text2=text2.replace("n."," n dot ")
    text2=" ".join([i for i in re.split(r'([0-9]*[A-Z]*[a-z]*)',text2) if i])
    #print(text2)
    #print(text2)
    text2=text2.lower()
    text2=text2.replace("n."," n dot ")
    text2=text2.replace("-"," ")
    text2=text2.replace("–"," ")
    text2=text2.replace("_"," ")
    text2=text2.replace(",","")
    text2=text2.replace("!"," ")
    text2=text2.replace("?"," ")
    text2=text2.replace("("," ")
    text2=text2.replace(")"," ")
    text2=text2.replace("'","")
    text2=text2.replace('"'," ")
    text2=text2.replace(':'," ")
    text2=text2.replace("$"," dollars ")
    text2=text2.replace("#"," hash tag ")
    text2=text2.replace("@"," at ")
    text2=text2.replace("&"," and ")
    text2=text2.replace("*"," ")
    text2=text2.replace("\\","  ")
    text2=text2.replace("/"," slash ")
    text2=text2.replace("="," equals ")
    text2=text2.replace("0ti","0 ti")
    text2=text2.replace("550 ti","5 50 t i")
    text2=text2.replace("x 570","x 5 70")
    text2=text2.replace("gt 710","gt 7 10")
    text2=text2.replace("980 ti","9 80 t i")
    text2=text2.replace("980","9 80")
    text2=text2.replace("1010","10 10")
    text2=text2.replace("1030","10 30")
    text2=text2.replace("1050","10 50")
    text2=text2.replace("1060","10 60")
    text2=text2.replace("1070","10 70")
    text2=text2.replace("1080","10 80")
    text2=text2.replace("1060","10 60")
    text2=text2.replace("1650","16 50")
    text2=text2.replace("1650s","16 50 s")
    text2=text2.replace("1660","16 60")
    text2=text2.replace("1660s","16 60 s")
    text2=text2.replace("2001","2000 1") #These refer to both the years AND the GPUs once we get to 2060
    text2=text2.replace("2002","2000 2")
    text2=text2.replace("2003","2000 3")
    text2=text2.replace("2004","2000 4")
    text2=text2.replace("2005","2000 5")
    text2=text2.replace("2006","2000 6")
    text2=text2.replace("2007","2000 7")
    text2=text2.replace("2008","2000 8")
    text2=text2.replace("2009","2000 9")
    text2=text2.replace("2010","20 10")
    text2=text2.replace("2011","20 11")
    text2=text2.replace("2012","20 12")
    text2=text2.replace("2013","20 13")
    text2=text2.replace("2014","20 14")
    text2=text2.replace("2015","20 15")
    text2=text2.replace("2016","20 16")
    text2=text2.replace("2017","20 17")
    text2=text2.replace("2018","20 18")
    text2=text2.replace("2019","20 19")
    text2=text2.replace("2020","20 20")
    text2=text2.replace("2021","20 21")
    text2=text2.replace("2022","20 22")
    text2=text2.replace("2030","20 30")
    text2=text2.replace("2040","20 40")
    text2=text2.replace("2050","20 50")
    text2=text2.replace("2060","20 60")
    text2=text2.replace("2070","20 70")
    text2=text2.replace("2080","20 80")
    text2=text2.replace("2090","20 90")
    text2=text2.replace(" ' ","'")
    text2=text2.replace(" ' ","'")
    text2=text2.split(" ")
    text3=''
    for i in text2:
        try:
            #print(float(i))
            if str(float(i))==i:
                text3=text3+' '+(num2words(float(i))).replace('-',' ').replace(",","")
            else:
                if str(int(i))==i:
                   text3=text3+' '+(num2words(int(i))).replace('-',' ').replace(",","")
        except:
            text3=text3+' '+(i)

    text3=text3.replace('.',' ')
    text2=text3.split(' ')
    for Just_To_Be_Sure in range(3):
        text3=[]
        for i in text2:
            if i!=' ' and i != '':
                text3.append(i.strip('\n'))
        text2=text3
    #print(text2)
    syll=0
    if len(text2)>8: return(500)
    for i in text2:
        #print(i[0])
        try:
            char = i[0].lower()
            if char=='a': cmu=cmu_a
            if char=='b': cmu=cmu_b
            if char=='c': cmu=cmu_c
            if char=='d': cmu=cmu_d
            if char=='e': cmu=cmu_e
            if char=='f': cmu=cmu_f
            if char=='g': cmu=cmu_g
            if char=='h': cmu=cmu_h
            if char=='i': cmu=cmu_i
            if char=='j': cmu=cmu_j
            if char=='k': cmu=cmu_k
            if char=='l': cmu=cmu_l
            if char=='m': cmu=cmu_m
            if char=='n': cmu=cmu_n
            if char=='o': cmu=cmu_o
            if char=='p': cmu=cmu_p
            if char=='q': cmu=cmu_q
            if char=='r': cmu=cmu_r
            if char=='s': cmu=cmu_s
            if char=='t': cmu=cmu_t
            if char=='u': cmu=cmu_u
            if char=='v': cmu=cmu_v
            if char=='w': cmu=cmu_w
            if char=='x': cmu=cmu_x
            if char=='y': cmu=cmu_y
            if char=='z': cmu=cmu_z
            for i2 in cmu:
                thing=i2.split(" ")
                if thing[0]==i or (thing[0]+'s'==i and not i.endswith('es')):
                    #print(thing)
                    foun=0
                    for i3 in thing:
                        if i3.strip('0').strip('1').strip('2') in ['aa','ae','ah','ao','aw','ay','eh','er','ey','ih','iy','ow','oy','uh','uw'] or i3=='~':
                            #print(i3)
                            foun=1
                            syll+=1
                            if syll>7: break
                        if syll>7: break
                    break
        except UnboundLocalError: return 666
    #print(text)
    return(syll)


syllablecount("SiivaGunner's rippers be like")
