listaDes = ['[', '[', '(', ')', ')', ')', '{', ']']
listaBal = ['[]',]

# def verifica_parenteses(pilha: list):
#     valida_pilha = []

#     for c in range(len(pilha)):
#         index = pilha.pop()
#         if index == '(':
#             valida_pilha.append(1)
#         elif index == '[':
#             valida_pilha.append(2)
#         elif index == '{':
#             valida_pilha.append(3)
#         elif index == ')':
#             valida_pilha.append(-1)
#         elif index == ']':
#             valida_pilha.append(-2)
#         elif index == '}':
#             valida_pilha.append(-3)
            
#     if sum(valida_pilha) == 0:
#         print('Balanciado.')
#     else:
#         print('Não balanciado.')

# verifica_parenteses(listaBal)

def expressao_bem_formada(expressao):
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}

    for simbolo in expressao:
        if simbolo in '([{':
            pilha.append(simbolo)
        elif simbolo in ')]}':
            if not pilha or pilha[-1] != pares[simbolo]:
                return False
            pilha.pop()
        else:
            # Caracter inválido (não é (), [], {})
            return False

    return len(pilha) == 0


print(expressao_bem_formada(listaBal))