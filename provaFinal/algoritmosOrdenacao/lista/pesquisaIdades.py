from random import randint


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


def dados_pesquisa(lista):
    insertion_sort(lista)  # Ordena a lista com isertion sort
    if len(lista) % 2 == 0:  # Calculando mediana
        mediana = (lista[len(lista)//2] + lista[(len(lista)//2) - 1])/2
    else:
        mediana = lista[len(lista)//2]
    print(
        f'A menor idade: {lista[0]}\nA maior idade: {lista[499]}\nA mediana: {mediana}')


idades = []

for i in range(500):
    idade = randint(15, 78)
    idades.append(idade)

dados_pesquisa(idades)
