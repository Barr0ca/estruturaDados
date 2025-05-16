# Elaboração do Merge Sort utilizando Shell Sort para ordenação
from shellSort import shell_sort
from random import randint
from desempenho import desempenho

def merge_sort(lista: list):
    if len(lista) == 1:
        return lista
    
    metade = len(lista)//2

    return shell_sort(shell_sort(merge_sort(lista[:metade])) + shell_sort(merge_sort(lista[metade:])))

lista = []
for i in range(10000):
    lista.append(randint(1, 100000))

desempenho(shell_sort, lista)
desempenho(merge_sort, lista)