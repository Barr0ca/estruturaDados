def insertion(list, index):
    while index > 0:
        if list[index] > list[index - 1]:  # Troca o sinal para "maior que", assim a ordem inverte
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


notas = [6.7, 8.5, 5.4, 9.0, 7.8]

print(insertion_sort(notas))
