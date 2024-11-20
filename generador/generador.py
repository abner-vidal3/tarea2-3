from random import randint, shuffle
letr = "abcdefghijklmnopqrstuvwxyz"
def escribir(num,S1,S2):
    with open("tests/"+str(num)+".txt","w") as file:
        file.write(str(len(S1))+" "+S1+"\n"+str(len(S2))+" "+S2)
def aleatorio(sz):
    S = ""
    for i in range(sz):
        S += letr[randint(0,25)]
    return S
def generar(caso,sz):
    if caso == 0:
        estr = randint(0,1)
        if estr == 0:
            return "",aleatorio(sz)
        return aleatorio(sz),""
    elif caso == 1:
        S1 = aleatorio(sz)
        S2 = list(S1)
        shuffle(S2)
        return S1,"".join(S2)
    elif caso == 2:
        S1 = aleatorio(sz)
        S2 = ""
        for i in range(sz):
            c1 = randint(0,2)
            if c1 == 0:
                S2 += letr[randint(0,25)]
            elif c1 == 1:
                S2 += S1[i]
        return S1,S2
    else:
        S1 = aleatorio(randint(sz,sz+5))
        S2 = aleatorio(randint(sz,sz+5))
        return S1,S2
def generar_caso(caso, num, sz):
    S1,S2 = generar(caso,sz)
    escribir(num,S1,S2)
    return (len(S1)+1)*(len(S2)+1)
l = []
cnt = 0
for i in range(4):
    for k in range(4):
        for j in range(1,6):
            res = generar_caso(i,cnt,10**k*j)
            l.append([cnt,i,res])
            cnt += 1
print(l)
