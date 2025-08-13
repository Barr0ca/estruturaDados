def vetor_reverso(lista: list):
    if len(lista) == 0:
        return lista
    return [lista.pop()] + vetor_reverso(lista)


lista = [1, 2, 7, 5, 15]

print(vetor_reverso(lista))
