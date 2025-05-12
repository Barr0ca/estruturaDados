# Soma os elementos de uma lista de inteiros

def sumVetor(lista: list):
    if len(lista) == 1:
        return lista[0]
    ultimo = lista.pop()
    return ultimo + sumVetor(lista)


vetor = [1, 2, 3, 4, 5, 6, 9]
print(sumVetor(vetor))
