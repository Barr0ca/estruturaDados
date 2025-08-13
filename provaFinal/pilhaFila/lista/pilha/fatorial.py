def fatorial(numero: int):
    pilha = []
    fatorial = 1

    for i in range(1, numero+1):
        pilha.append(i)

    for num in pilha:
        fatorial *= num

    return fatorial


print(fatorial(10))
