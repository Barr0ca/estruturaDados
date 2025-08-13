def shell_sort(lista):
    gap = len(lista) // 2
    while gap > 0:
        for i in range(gap, len(lista)):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap][1] > temp[1]:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2
    return lista


produtos = [('chapeu', 20), ('bone', 19), ('camisa', 80),
            ('vestido', 20), ('tenis', 30)]

print(shell_sort(produtos))
