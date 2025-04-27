from math import ceil
from random import randint


def shellSort(list):
    gap = ceil(len(list)/2)
    if gap % 2 != 0:
        gap += 1
    while gap > 0:
        for i in range(0, len(list)-gap):
            valorAtual = list[i]
            if list[i+gap] < valorAtual:
                aux = list[i]
                list[i] = list[i+gap]
                list[i+gap] = aux
        gap //= 2
    return list


for i in range(5):
    dia = randint(1, 30)
    mes = randint(1, 12)

lista = []
print("lista desordenada")
print(lista)
listaO = shellSort(lista)
print("lista ordenada")
print(listaO)
