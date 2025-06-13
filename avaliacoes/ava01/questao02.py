def insertion(lista: list[int], indice: int) -> list[int]:
    i = indice  # início
    while (i > 0):  # condição de parada
        if lista[i-1] > lista[i]:
            aux = lista[i-1]
            lista[i-1] = lista[i]
            lista[i] = aux
        else:
            break
        i -= 1  # passo
    return lista


def insertion_sort(lista: list[int]) -> list[int]:
    i = 1  # início
    while (i < len(lista)):  # condição de parada
        lista = insertion(lista, i)
        i += 1  # passo

    return lista

def sumVetor(lista: list):
    if len(lista) == 1:
        return lista[0]
    ultimo = lista.pop()
    return ultimo + sumVetor(lista)

lista = [6.7, 8.5, 5.4, 4.6, 9.0, 7.8]

# Lista ordenada 
print(f'Lista ordenada: {insertion_sort(lista)}')

# Condição para saber se a lista é par ou ímpar
# Caso seja par ela soma os dois elementos do meio e divide por 2 para calcular a mediana
# Caso não, o elemento do meio é a mediana
if len(lista)%2 == 0:
    metade = len(lista)//2
    mediana = lista[metade-1] + lista[metade]
    mediana = mediana // 2
    print(f'Mediana: {mediana}')
else:
    metade = len(lista)//2
    print(f'Mediana: {lista[metade]}')

# Usando função recursiva para somar as notas
print(f'Soma total: {sumVetor(lista)}')