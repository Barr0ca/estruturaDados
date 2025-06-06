def op_pos_fixa(pilha: list):
    pilha_resultado = []
    pilha_inversa = []

    for i in range(len(pilha)):
        pilha_inversa.append(pilha.pop())

    for c in range(len(pilha_inversa)):
        index = pilha_inversa.pop()
        if type(index) == int:
            pilha_resultado.append(index)
        else:
            if index == '+':
                n1 = pilha_resultado.pop()
                n2 = pilha_resultado.pop()
                pilha_resultado.append(n2+n1)
            elif index == '-':
                n1 = pilha_resultado.pop()
                n2 = pilha_resultado.pop()   
                pilha_resultado.append(n2-n1)        
            elif index == '*':
                n1 = pilha_resultado.pop()
                n2 = pilha_resultado.pop()
                pilha_resultado.append(n2*n1)
            elif index == '/':
                n1 = pilha_resultado.pop()
                n2 = pilha_resultado.pop()
                pilha_resultado.append(n2/n1)
    return pilha_resultado

pilha = [5, 1, 2, '+', 4, '*', '+', 3, '-']

print(op_pos_fixa(pilha))