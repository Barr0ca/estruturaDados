from math import ceil
import time
from random import randint


def insertion(list, index):
    while index > 0:
        if list[index] < list[index - 1]:
            aux = list[index]
            list[index] = list[index - 1]
            list[index - 1] = aux
        index -= 1
    return list


def insertion_sort(list):
    i = 1
    while i < len(list):
        insertion(list, i)
        i += 1
    return list


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


def desempenho(list):
    tempoInicialInsertionSort = time.time()
    insertion_sort(list)
    tempoFinalInsertionSort = time.time()
    tempoTotalInsertionSort = tempoFinalInsertionSort-tempoInicialInsertionSort

    tempoInicialShellsort = time.time()
    shell_sort(list)
    tempoFinalShellSort = time.time()
    tempoTotalShellSort = tempoFinalShellSort-tempoInicialShellsort

    print(
        f'Tempo InsertionSort: {tempoTotalInsertionSort}\nTempo ShellSort: {tempoTotalShellSort}')


lista = []
for i in range(10000):
    lista.append(randint(0, 999999999))

desempenho(lista)
