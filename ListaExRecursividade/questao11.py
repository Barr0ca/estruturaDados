# Elementos de uma lista ao contrário

def listaInversa(lista: list):
    lista02 = []
    if len(lista)-1 == 0:
        return lista
    lista02.append(lista.pop())
    return lista02 + listaInversa(lista)


vetor = [1]
print(listaInversa(vetor))
