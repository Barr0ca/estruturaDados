# Questão elaborada com exemplo de insertion sort feito em sala apenas com algumas alterações

def insertion(list, index):
    while index > 0:
        if list[index][1] < list[index - 1][1]: 
            # Alteração na frente dos indexes para sinalizar o elemento da tupla 
            # (0, 1) elemento 1 da tupla (nome, idade) nesse caso é idade
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
