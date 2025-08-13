def infixa_para_posfixa(expressao):
    pilha = []
    posfixa = []
    tokens = expressao.split()

    for token in tokens:
        if token.isdigit():
            posfixa.append(token)
        elif token == '(':
            pilha.append(token)
        elif token == ')':
            while pilha and pilha[-1] != '(':
                posfixa.append(pilha.pop())
            if pilha and pilha[-1] == '(':
                pilha.pop()
        else:
            # operador
            while (pilha and pilha[-1] != '(' and
                   ((pilha[-1] in ['*', '/'] and token in ['+', '-']) or
                    (pilha[-1] in ['+', '-'] and token in ['+', '-']) or
                    (pilha[-1] in ['*', '/'] and token in ['*', '/']))):
                posfixa.append(pilha.pop())
            pilha.append(token)
    while pilha:
        posfixa.append(pilha.pop())
    return ' '.join(posfixa)


notacao = "( ( 5 + ( ( 1 + 2 ) * 4 ) ) - 3 )"

print(infixa_para_posfixa(notacao))
