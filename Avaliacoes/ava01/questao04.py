from math import ceil

def shell_sort(list):
    gap = ceil(len(list)/2)
    while gap > 0:
        for i in range(0, len(list)-gap):
            if list[i+gap] < list[i]:
                aux = list[i]
                list[i] = list[i+gap]
                list[i+gap] = aux
        gap -= 1
    return list

# Função que retorna uma lista de duplicatas
def duplicatas(lista: list):
    duplicatas = {'duplicatas': []} # Utilizando dicionário para armazenar as duplicatas
    for c in lista:
        if lista.count(c) >= 2:
            duplicatas['duplicatas'].append(c)

    return duplicatas

lista = [3, 5, 2, 3, 8, 5, 1, 5]

print(shell_sort(lista)) # Shell sort para ordenar a lista

print(duplicatas(lista)) # Função para retornar a lista de duplicatas