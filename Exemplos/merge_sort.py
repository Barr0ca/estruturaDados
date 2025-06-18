# Elaboração do Merge Sort utilizando Shell Sort para ordenação
from shellSort import shell_sort
from random import randint
from desempenho import desempenho


def merge_sort(lista: list):
    if len(lista) == 1:
        return lista

    metade = len(lista)//2

    return shell_sort(merge_sort(lista[:metade])+merge_sort(lista[metade:]))


lista = []
for i in range(10000):
    lista.append(randint(1, 100000))
desempenho(merge_sort, lista)

# lista = [3, 1, 5, 15, 10, 90, 3, 1, 5, 15, 10, 90]
# desempenho(merge_sort, lista)
