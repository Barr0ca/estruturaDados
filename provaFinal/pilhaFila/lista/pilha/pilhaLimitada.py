def pilha_limitada():
    pilha = []

    opcao = -1
    while opcao != 'x':
        print(f'\nCAPACIDADE: 10\nATUAL: {len(pilha)}')
        print('INSERIR: +')
        print('REMOVER: -')
        print('SAIR:    x')
        opcao = input('OPÇÃO:  ')

        if opcao == '+':
            if len(pilha) == 10:
                print('\nPILHA CHEIA.\n')
            else:
                add = input('\nADICIONAR: ')
                pilha.append(add)
        elif opcao == '-':
            if len(pilha) <= 0:
                print('\nPILHA VAZIA.\n')
            else:
                pilha.pop()


pilha_limitada()
