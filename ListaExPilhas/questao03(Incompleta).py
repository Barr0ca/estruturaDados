listaDes = ['[', '[', '(', ')', ')', ')', '{', ']']
listaBal = [']','[',]

def verifica_parenteses(pilha: list):
    valida_pilha = []

    for c in range(len(pilha)):
        index = pilha.pop()
        if index == '(':
            valida_pilha.append(1)
        elif index == '[':
            valida_pilha.append(2)
        elif index == '{':
            valida_pilha.append(3)
        elif index == ')':
            valida_pilha.append(-1)
        elif index == ']':
            valida_pilha.append(-2)
        elif index == '}':
            valida_pilha.append(-3)
            
    if sum(valida_pilha) == 0:
        print('Balanciado.')
    else:
        print('Não balanciado.')

verifica_parenteses(listaBal)