def soma_vetor(lista: list):
    if len(lista) == 0:
        return 0
    return lista.pop() + soma_vetor(lista)


lista = [1, 2, 7, 5, 15]

print(soma_vetor(lista))
