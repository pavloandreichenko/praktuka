import random

def randomm(array):
    for i in range(0,10):
        array.append(random.randint(0,100))
    return array

def sort(array):
    poslid = random.randint(0, 1)
    if poslid == 1:
        array.sort(reverse = True)

    else:
        array.sort()
    return print("Посортований масив",array)

def index(array,indexe):
    t = array.index(indexe)
    return print("Iндекс вашого елемента: ",t)

def arpos(array):

    if array[0] >= array[1]:
        if array[1] >= array[3]:
            if array[3] >= array[5]:
                if array[5] >= array[7]:
                    if array[7] >= array[9]:
                        return print("Послідовнiсть масива з більшого до меншого")
    else:
        return print("Послідовнiсть масива меншого до більшого")

def first(array):
    array.sort()
    return print("Перші 5 мінімальних",array[0],array[1],array[2],array[3],array[4])

def second(array):
    array.sort(reverse = True)
    return print("Перші 5 максимальних",array[0],array[1],array[2],array[3],array[4])

def sered(array):
    a=(array[0]+array[1]+array[2]+array[3]+array[4]+array[5]+array[6]+array[7]+array[8]+array[9])/(len(array))
    return print("Середнє арефметичне: ",a)

def deletpow(array):
    return print("Видалення повторів",list(set(array)))

Z=0
for i in range(0,a):
    if arr[i]>=arr[i+1]:
        Z=Z+1
if z==9:
    print(від більшого до меншого)
else:
    print(від меншого до більшого)