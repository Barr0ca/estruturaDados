def insertion(list, index):
    while index > 0:
        if list[index][1] < list[index - 1][1]:
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


lista = [('Ian', 20), ('Iago', 31), ('Adonias', 60),
         ('Filho', 31), ('Íris', 55)]
lista = insertionSort(lista)
print(lista)
