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


notas = [6.5, 8.5, 5.0, 4.0, 10.0]

print(insertion_sort(notas))

if len(notas) % 2 == 0:  # Caso a lista seja de tamanho par a mediana se da pela média aritmética entre os dois valores do meio
    mediana = (notas[len(notas)//2] + notas[(len(notas)//2) - 1])/2
else:
    mediana = notas[len(notas)//2]

print(f'Mediana: {mediana}')
