# Questão elaborada com exemplo de insertion sort feito em sala apenas com algumas alterações

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


def duplicatas(list): # Função para indentificar duplicatas
    i = 1 # Variável para contrlar o range da lista
    duplicatas = [] # Lista para armazenar duplicatas
    lista = insertionSort(list) # Ordenando a lista com a função insertionSort
    while i < len(lista):
        if list[i] == list[i-1] and list[i] not in duplicatas: # Se o elemento seguido dele mesmo for igual a ele esse elemento é adicionado a duplicatas
            duplicatas.append(list[i])
        i += 1
    return duplicatas


listaD = [3, 1, 5, 10, 15, 90, 15, 1, 3, 3, 2, 2, 2, 2]

print("lista desordenada")
print(listaD)

listaO = insertionSort(listaD)

print("lista ordenada")
print(listaO)

print("lista de duplicatas")
print(duplicatas(listaD))