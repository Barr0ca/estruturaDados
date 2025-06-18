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


# listaD = [3, 1, 5, 10, 15, 90, 2]
# print("lista desordenada")
# print(listaD)
# listaO = insertionSort(listaD)
# print("lista ordenada")
# print(listaO)
