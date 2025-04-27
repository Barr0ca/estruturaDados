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


def insertionSort(list):
    i = 1
    while i < len(list):
        insertion(list, i)
        i += 1
    return list


def shellSort(list):
    gap = ceil(len(list)/2)
    while gap > 0:
        for i in range(0, len(list)-gap):
            valorAtual = list[i]
            if list[i+gap] < valorAtual:
                aux = list[i]
                list[i] = list[i+gap]
                list[i+gap] = aux
        gap -= 1
    return list


def desempenho(list):
    tempoInicialInsertionSort = time.time()
    insertionSort(list)
    tempoFinalInsertionSort = time.time()
    tempoTotalInsertionSort = tempoFinalInsertionSort-tempoInicialInsertionSort

    tempoInicialShellsort = time.time()
    shellSort(list)
    tempoFinalShellSort = time.time()
    tempoTotalShellSort = tempoFinalShellSort-tempoInicialShellsort

    print(
        f'Tempo InsertionSort: {tempoTotalInsertionSort}\nTempo ShellSort: {tempoTotalShellSort}')


lista = []
for i in range(10000):
    lista.append(randint(0, 999999999))

desempenho(lista)
