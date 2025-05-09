# Função que retorna a potênciaçãode um número qualquer

def potencia(a,b):
    if b == 0:
        return 1
    return a * potencia(a, b-1)

print(potencia(5, 2))