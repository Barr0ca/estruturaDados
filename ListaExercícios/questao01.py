# Questão elaborada com exemplo de insertion sort feito em sala apenas com alguams alterações

def insertion(list, index):
    while index > 0:
        # Inversão do sinal < para > assim a lista fica ordenada em forma decrescente
        if list[index] > list[index - 1]:
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


lista = [6.7, 8.5, 5.4, 9.0, 7.8]  # Lista pedida na questão
lista = insertionSort(lista)
print(lista)
