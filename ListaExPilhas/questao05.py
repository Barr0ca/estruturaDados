def fatorial_pilha(numero: int):
    pilha_numeros = []
    fatorial = 1
    for numeros in range(2, (numero+1)):
        pilha_numeros.append(numeros)
    for index in range(len(pilha_numeros)):
        fatorial *= pilha_numeros.pop()
    return fatorial


print(fatorial_pilha(5))
