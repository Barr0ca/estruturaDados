def palindromo_pilha(palavra):
    pilha = list(palavra)  # Cada letra vira um elemento da pilha
    inverso = ""
    while pilha:
        inverso += pilha.pop()  # Retira da pilha e constrói o inverso
    return palavra == inverso


print(palindromo_pilha("radar"))    # True
print(palindromo_pilha("teclado"))  # False
