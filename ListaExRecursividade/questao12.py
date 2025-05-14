# Verificando ordenação de um vetor

def vetor_ordenado(lista: list):
    if len(lista) <= 1:
        return f'Lista ordenada'
    if lista[-2] >= lista[-1]:
        return f'Lista desordenada'
    return vetor_ordenado(lista[0:-1])

lista = [2,3,4,8,9]
print(vetor_ordenado(lista))

