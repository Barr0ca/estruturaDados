from random import randint
from datetime import datetime


def shell_sort(lista):
    gap = len(lista) // 2
    while gap > 0:
        for i in range(gap, len(lista)):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2
    return lista


datas = []

for i in range(5):  # Gera 5 datas diferentes
    dia = randint(1, 28)
    mes = randint(1, 12)
    ano = randint(1999, 2025)
    data = (f'{dia}/{mes}/{ano}')
    # As datas são adicionadas à lista no formato datetime
    datas.append(datetime.strptime(data, "%d/%m/%Y"))

shell_sort(datas)

for data in datas:
    print(data.strftime("%d/%m/%Y"))  # Print da lista com a formatação pedida
