# Importando as funções de forma modular
from shellSort import shell_sort

# Randint para sortear números para lista
from random import randint


def merge_sort(lista: list):
    # Quando o tamanho da lista for 1 retorna
    if len(lista) == 1:
        return lista

    # Divide a lista pela metade
    metade = len(lista)//2

    # Concatena as sublista e realiza shell sort para ordenar
    return shell_sort(merge_sort(lista[:metade])+merge_sort(lista[metade:]))


# Elaborando uma lista de 10000 números de forma aleatória
lista = []
for i in range(10000):
    lista.append(randint(1, 100000))
