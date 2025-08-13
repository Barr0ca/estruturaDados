def shell_sort(lista):
    gap = len(lista) // 2
    while gap > 0:
        for i in range(gap, len(lista)):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2
    return lista


listaD = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("lista desordenada")
print(listaD)
listaO = shell_sort(listaD)
print("lista ordenada")
print(listaO)
