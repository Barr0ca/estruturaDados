def sum_vetor(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + sum_vetor(lista[1:])


def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista


notas = [6.7, 8.5, 5.4, 4.6, 9.0, 7.8]

notas_ordenadas = insertion_sort(notas.copy())
print("Notas ordenadas:", notas_ordenadas)

# Mediana
n = len(notas_ordenadas)
if n % 2 == 0:
    mediana = (notas_ordenadas[n//2 - 1] + notas_ordenadas[n//2]) / 2
else:
    mediana = notas_ordenadas[n//2]
print("Mediana:", mediana)

# Soma total
print("Soma total:", sum_vetor(notas))
