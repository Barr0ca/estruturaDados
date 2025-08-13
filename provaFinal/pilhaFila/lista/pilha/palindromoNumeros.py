def palindromo(numeros: list):
    pilha = []
    pilha_aux = []

    for i in range(len(numeros)//2):
        pilha.append(numeros[i])

    for p in range(len(pilha)):
        pilha_aux.append(pilha.pop())

    for j in range((len(numeros)-1), len(numeros)//2, -1):
        if pilha_aux.pop() == numeros[j]:
            continue
        else:
            return False

    if pilha_aux == []:
        return True
    else:
        return False


print(palindromo([2, 5, 5, 2]))
