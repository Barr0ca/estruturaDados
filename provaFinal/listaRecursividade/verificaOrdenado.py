def verifica_ordenado(lista: list):
    if len(lista) <= 1:
        return True
    if lista[0] > lista[1]:
        return False
    return verifica_ordenado(lista[1:])


lista = [1, 2, 7, 99, 15]

print(verifica_ordenado(lista))
