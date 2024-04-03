import random


def pk(ap,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,bp,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10): #a,b为种族，ap，bp为得分
    lista=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
    listb=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]
    a=random.choice(lista)
    b=random.choice(listb)
    if a==b:
        if a==0:
            ap=ap+1
            bp=bp+1
        if a==1:
            ap=ap-2
            bp=bp-2
    if a!=b:
        if a==1:
            ap+=2
        if b==1:
            bp+=2
            pass
        pass
    return ap,bp

