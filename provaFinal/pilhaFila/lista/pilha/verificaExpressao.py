def verifica_expressao(expressao: str):
    pilha = []
    palavra = []

    for i in range(len(expressao)):
        palavra.append(expressao[i])

    for item in palavra:
        if item in ('(', '[', '{'):
            pilha.append(item)
        else:
            if pilha == []:
                return False
            else:
                if pilha.pop() + item in ('()', '[]', '{}'):
                    continue
                else:
                    return False

    if pilha == []:
        return True
    else:
        return False


print(verifica_expressao('([])(){([])}[]'))
