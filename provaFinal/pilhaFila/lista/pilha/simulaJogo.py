def simula():
    pilha = ['COMEÇO']

    opcao = -1
    while opcao != 'x':
        print(f'\nAÇÕES')
        print('ANDAR PARA FRENTE: +')
        print('ANDAR PARA TRÁS:   -')
        print('ATACAR:            a')
        print('DEFENDER:          d')
        print('VOLTAR NO TEMPO:   p')
        print('SAIR:              x')
        opcao = input('OPÇÃO:  ')

        if opcao == '+':
            pilha.append('AVANÇAR.')
            print(f'SEQUÊNCIA DE AÇÕES: {pilha}')
        elif opcao == '-':
            pilha.append('RECUAR.')
            print(f'SEQUÊNCIA DE AÇÕES: {pilha}')
        elif opcao == 'a':
            pilha.append('ATACAR!')
            print(f'SEQUÊNCIA DE AÇÕES: {pilha}')
        elif opcao == 'd':
            pilha.append('DEFENDER!')
            print(f'SEQUÊNCIA DE AÇÕES: {pilha}')
        elif opcao == 'p':
            if pilha[-1] == 'AVANÇAR.':
                pilha.pop()
                print('VOLTOU NO TEMPO E NÃO AVANÇOU.')
                print(f'SEQUÊNCIA DE AÇÕES: {pilha}')
            elif pilha[-1] == 'RECUAR.':
                pilha.pop()
                print('VOLTOU NO TEMPO E NÃO RECUOU.')
                print(f'SEQUÊNCIA DE AÇÕES: {pilha}')
            elif pilha[-1] == 'ATACAR!':
                pilha.pop()
                print('VOLTOU NO TEMPO E NÃO ATACOU.')
                print(f'SEQUÊNCIA DE AÇÕES: {pilha}')
            elif pilha[-1] == 'DEFENDER!':
                pilha.pop()
                print('VOLTOU NO TEMPO E NÃO DEFENDEU.')
                print(f'SEQUÊNCIA DE AÇÕES: {pilha}')
            elif pilha[-1] == 'COMEÇO':
                pilha.pop()
                print('VOLTOU MUITO NO TEMPO E MORREU.')
                break


simula()
