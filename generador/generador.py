from random import randint
letr = "abcdefghijklmnopqrstuvwxyz"
def escribir(num,S1,S2):
    with open("tests/"+str(num)+".txt","w") as file:
        file.write(S1+"\n"+S2)
def conv(S1):
    op = randint(1,1)
    xd = [randint(0,3) for i in range(op)]
    for v1 in xd:
        if v1 == 0:
            l1 = len(S1)
            i1 = randint(0,l1-1)
            i2 = randint(0,l1-1)
            S1 = list(S1)
            aux = S1[i1]
            S1[i1] = S1[i2]
            S1[i2] = aux
            S1 = ''.join(S1)
        elif v1 == 1:
            l1 = len(S1)
            i1 = randint(0,l1-1)
            S1 = list(S1)
            S1[i1] = letr[randint(0,25)]
            S1 = ''.join(S1)
        elif v1 == 2:
            l1 = len(S1)
            i1 = randint(0,l1)
            S1 = S1[:i1]+letr[randint(0,25)]+S1[i1:]
        else:
            l1 = len(S1)
            i1 = randint(0,l1-1)
            S1 = S1[:i1]+S1[i1+1:]
    return S1
def generar(caso):
    if caso == 0:
        len1 = randint(1,5)
        S1 = "".join([letr[randint(0,25)] for i in range(len1)])
        S2 = conv(S1)
        return S1,S2
    elif caso == 1:
        len1 = randint(1,3)
        len2 = randint(1,max(len1-3,1))
        S1 = "".join([letr[randint(0,25)] for i in range(len1)])
        S2 = "".join([letr[randint(0,25)] for i in range(len2)])
        return S1,S2
    elif caso == 2:
        len1 = randint(1000,5000)
        S1 = "".join([letr[randint(0,25)] for i in range(len1)])
        S2 = conv(S1)
        return S1,S2
    elif caso == 3:
        len1 = randint(100,200)
        S1 = "".join([letr[randint(0,25)] for i in range(len1)])
        S2 = conv(S1)
        return S1,S2
    elif caso == 4:
        len1 = randint(1000,5000)
        len2 = randint(1000,5000)
        S1 = "".join([letr[randint(0,25)] for i in range(len1)])
        S2 = "".join([letr[randint(0,25)] for i in range(len2)])
        return S1,S2
    else:
        len1 = randint(100,200)
        len2 = randint(100,200)
        S1 = "".join([letr[randint(0,25)] for i in range(len1)])
        S2 = "".join([letr[randint(0,25)] for i in range(len2)])
        return S1,S2
def generar_caso(caso, num):
    S1,S2 = generar(caso)
    escribir(num,S1,S2)
casos = []
for i in range(5):
    casos.append(0)
for i in range(5):
    casos.append(1)
for i in range(3):
    casos.append(2)
for i in range(4):
    casos.append(3)
for i in range(len(casos)):
    generar_caso(casos[i],i)