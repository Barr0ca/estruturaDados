# Questão elaborada com exemplo de insertion sort feito em sala apenas com algumass alterações

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


def calcMediana(list):  # Função que calcula a mediana de uma lista
    lista = insertionSort(list)
    if len(lista) % 2 == 0:
        # Se o tamanho da lista for par é feita a divisão por 2, o resultado é somado com o
        # item de posição anterior e depois é feita novamente a divisão por 2 (média entre eles)
        # resultando na mediana
        index = (len(lista) / 2)
        mediana = ((lista[index] + lista[index-1]) / 2)
    else:
        # Caso o tamanho da lista seja ímpar é feita a divisão inteira do tamanho da lista
        # por 2, nesse caso o resultado sempre será o elemento na posição da mediana
        # 5//2=2 [1,2,(3),4,5] elemento 3 na posição 2
        index = (len(lista) // 2)
        mediana = lista[index]
    return mediana


notas = [6, 7, 5, 5, 8]
print(f'Notas: {insertionSort(notas)}\nMediana: {calcMediana(notas)}')
