# Задача 1
import math
text1="у мові програмування пiтон рядок це вбудований тип який призначений "
mas =[0,0,0,0,0,0,0,0,0,0]
s2="x"
s4=text1[0]
z=0
i=0
try:
    while True:
        z=z+1
        s2 = text1[z]
        if s2 != " ":
            s4 = s4+s2

        else:
            z=z+1
            s2 = text1[z]
            mas[i]=s4
            i=i+1
            s4=s2
except IndexError:
    mas[i]=s4
    print(mas)

# Задача 2
text2="in my programming python has this type of built-in type 2 3 421 23"
z=len(text2)

id=0
prigol=0
gol=0
probl=0
for link in range(0,z):
    word=text2[link]
    if word == "a" or word == "e" or word == "i" or word =="o" or word == "u" or word == "y":
        gol=gol+1
    if word == " ":
        probl=probl+1
    if word == "q" or word == "w" or word == "r" or word =="t" or word == "p" or word == "s" or word == "d" or word == "f" or word == "g" or word == "h":
        prigol=prigol+1
    if word == "l" or word == "z" or word == "x" or word =="c" or word == "v" or word == "b" or word == "n" or word == "m" or word == "j" or word == "k":
        prigol=prigol+1
print("Голоснi",gol,"Приголоснi",prigol,"Пропуски",probl)
if gol<prigol:
    print("Приголосних бiльше")
if gol>prigol:
    print("Голосних бiльше")
if gol==prigol:
    print("Голосних i Приголосних порівну")
# Задача 3
a1=0
e1=0
i1=0
o1=0
u1=0
y1=0
text3=""
for link2 in range(0,z):
    word2=text2[link2]
    if word2 == "a" and a1==0:
        text3 = text3+word2
        a1=a1+1
    if word2 == "e" and e1==0:
        text3 = text3+word2
        e1=e1+1
    if word2 == "i" and i1==0:
        text3 = text3+word2
        i1=i1+1
    if word2 == "o" and o1==0:
        text3 = text3+word2
        o1=o1+1
    if word2 == "u" and u1==0:
        text3 = text3+word2
        u1=u1+1
    if word2 == "y" and y1==0:
        text3 = text3+word2
        y1=y1+1
sor=sorted(text3)
print(sor)