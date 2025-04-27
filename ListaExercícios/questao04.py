# Questão elaborada com exemplo de insertion sort feito em sala apenas com algumas alterações

from math import ceil
from random import randint
from datetime import datetime


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


lista = [] 

# Esquema para adicionar 5 datas aleatórias
for i in range(5):
    dia = randint(1, 28)
    mes = randint(1, 12)
    ano = randint(1999, 2025)
    data = (f'{dia}/{mes}/{ano}')
    lista.append(datetime.strptime(data, "%d/%m/%Y")) # As datas são adicionadas à lista no formato datetime 

print("lista desordenada")
for data in lista:
    print(data.strftime("%d/%m/%Y")) # Print da lista com a formatação pedida

listaO = shellSort(lista)

print("lista ordenada")
for data in listaO:
    print(data.strftime("%d/%m/%Y"))
