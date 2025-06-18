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

def vetor_ordenado(lista: list):
    if len(lista) <= 1:
        return True
    if lista[-2] >= lista[-1]:
        return False
    return vetor_ordenado(lista[0:-1])

lista = [10, 15, 12, 20, 25]

print(vetor_ordenado(lista)) # Utilizando função recursiva que retorna True para ordenada e False para desordenada

print(shell_sort(lista)) # Utilizando shell sort para ordenar a lista