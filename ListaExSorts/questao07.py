# Questão elaborada com exemplo de insertion sort feito em sala apenas com algumas alterações

from math import ceil


def shellSort(list):
    gap = ceil(len(list)/2)
    if gap % 2 != 0:
        gap += 1
    while gap > 0:
        for i in range(0, len(list)-gap):
            if list[i+gap][1] < list[i][1]: # Basicamente mesma lógica da questão 2 implementada
                aux = list[i]
                list[i] = list[i+gap]
                list[i+gap] = aux
        gap //= 2
    return list


lista = [('Botas', 20), ('Tênis', 31), ('Camisas', 60), ('Chepéus', 199),
         ('Braceletes', 55), ('Meias', 88), ('Luvas', 26), ('Relógios', 7)]
lista = shellSort(lista)
print(lista)
