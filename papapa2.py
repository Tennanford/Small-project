import random
def yichuan(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10):
    def ramnum(start, end) :
        num1 = random.randint(start, end)
        num2 = num1
        while num2 == num1 :
            num2 = random.randint(start, end)
        return num1, num2
    a,b=ramnum(0,11)
    if a>b:
        a,b=b,a
        pass
    lista=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
    listb=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]
    listb[a:b],lista[a:b]=lista[a:b],listb[a:b]
    #突变
    x=random.randint(0,10)
    y=random.randint(0,10)
    if x==1:
        choice = random.choice(lista)
        mm=lista[choice]
        if mm==0:
            lista[choice]=1
        else:
            lista[choice]=0
    if y==1:
        choice = random.choice(listb)
        mm=listb[choice]
        if mm==0:
            listb[choice]=1
        else:
            listb[choice]=0

    x4, x5, x6, x7, x8, x9, x10, x11, x12, x13=lista
    y4, y5, y6, y7, y8, y9, y10, y11, y12, y13=listb

    return x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13



