pilha = [] 
pilha_inversa = [] # Vou armazenar os elementos aqui para descomactalos com pop na ordem certa.
historia = '' # String concatenada estará aqui após sair da pilha.
opcao = '' # Armazena entrada do usuário
while opcao != '0':
    print('')
    print('A cada palavra que deseja escrever pressione "enter" os')
    print('Espaços entre as letras serão colocados automaticamente.')
    print('\nCaso queira apagar a última palavra escrita digite [1]')
    print('\nCaso queira ver sua como está a história digite [2]')
    print('Para sair digite [0]\n')
    opcao = (input(''))

    pilha.append(opcao) # Adiciona qualquer entrada na pilha

    # Aqui, caso não tenha nada escrito, ele retirar a entrada (1) e retorna pro usuário.
    if opcao == '1':
        if len(pilha) <= 1:
            pilha.pop()
            print('Mas não tem nada escrito.')
            continue
    # Caso tenha algo escrito ele retira a entrada (1) e a última palavra escrita.
        pilha.pop()
        pilha.pop()

    # Aqui utilizo da pilha inversa para descompactar e concatenar na string 'história' para ter a saída correta para o usuário.
    elif opcao == '2':
        pilha.pop() # Retirando a entrada (2).

        # Adicionando na pilha inversa
        for a in range(len(pilha)):
            pilha_inversa.append(pilha.pop())

        # Retirando da pilha inversa e concatenando na string 'historia'.
        for c in range(len(pilha_inversa)):
            historia += pilha_inversa.pop() + ' ' #Concatena com um espaço após a palavra.
        print(historia)

# Mesmo esquema que ocorre na opção (2).
for a in range(len(pilha)):
    pilha_inversa.append(pilha.pop())

for c in range(len(pilha_inversa)):
    historia += pilha_inversa.pop() + ' '

print(historia)
