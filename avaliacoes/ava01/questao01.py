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

# Função recursiva que retorna se uma palavra é palíndromo ou não
def palindromo(nome: str):
    if len(nome) <= 1:
        return True
    if nome[0] != nome[-1]:
        return False
    return palindromo(nome[1:-1])

lista = ["ana", "casa", "arara", "luz", "radar"]
palindromos = []

print(insertion_sort(lista)) # Lista ordenada

# Laço para identificar se cada elemento da lista é um palíndromo
# Caso seja um palídromo ele adiciona na lista 
for i in range(len(lista)):
    if palindromo(lista[i]):
        palindromos.append(lista[i])

print(palindromos) # Lista de palíndromos