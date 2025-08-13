def shell_sort(lista):
    n = len(lista)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2
    return lista


def duplicatas(lista):
    contagem = {}
    for num in lista:
        contagem[num] = contagem.get(num, 0) + 1
    return [num for num, qtd in contagem.items() if qtd > 1]


lista = [3, 5, 2, 3, 8, 5, 1, 5]
lista_ordenada = shell_sort(lista.copy())
print("Lista ordenada:", lista_ordenada)
print("Duplicatas:", duplicatas(lista))
