def calc_pos_fixo(notacao: str):
    pilha = []
    notacao_lista = notacao.split()

    for iten in notacao_lista:
        if iten in '0123456789':
            pilha.append(int(iten))
        else:
            operando_02 = pilha.pop()
            operando_01 = pilha.pop()
            resultado = calc(iten, operando_01, operando_02)
            pilha.append(resultado)
    return pilha.pop()


def calc(operador, op1, op2):
    if operador == "*":
        return op1 * op2
    elif operador == "/":
        return op1 / op2
    elif operador == "+":
        return op1 + op2
    else:
        return op1 - op2


notacao = ("5 1 2 + 4 * + 3 -")

print(calc_pos_fixo(notacao))
