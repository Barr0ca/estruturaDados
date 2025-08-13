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


lista = [3, 1, 5, 10, 15, 90, 2, 10, 5, 5, 5]

shell_sort(lista)

vistos = []  # Lista com os números visitados

for i in range(len(lista)):
    if lista[i] not in vistos:  # Se o número ainda não tiver sido visitado
        contador = 0  # Contador zera
        # A lista de números é percorrida denovo (para cada novo elemento no "for" anterior)
        for j in range(len(lista)):
            # Se o número percorrido no momento deste "for" for igual ao número que está sendo percorrido no "for" anterior
            if lista[i] == lista[j]:
                contador += 1  # Sempre um número terá no contador 1, números repetidos teram 2 ou mais
        if contador > 1:  # Repetidos são imprimidos
            print(lista[i])
        # Sempre que um número é visto ele é adicionado
        vistos.append(lista[i])
