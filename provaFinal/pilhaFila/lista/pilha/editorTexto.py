def editor_texto():
    pilha_texto = []
    pilha_bck = []

    opcao = -1
    while opcao != 'x':
        print('\nESCREVER:  +')
        print('APAGAR:    -')
        print('REFAZER:   <')
        print('VER TEXTO: v')
        print('SAIR:      x')
        opcao = input('OPÇÃO:  ')

        if opcao == '+':
            texto = input('\nESCREVA: ')
            pilha_texto.append(texto)
            if len(pilha_bck) > 0:
                pilha_bck.pop()
                pilha_bck.append(texto)
            else:
                pilha_bck.append(texto)
        elif opcao == '-':
            if len(pilha_texto) == 0:
                print('\nNÃO HÁ NADA AQUI\n')
            else:
                print(f'\nAPAGANDO ESSE TRECHO: {pilha_texto.pop()}')
        elif opcao == '<':
            if len(pilha_bck) == 0:
                print('\nNÃO HÁ NADA PARA FAZER BACKUP')
            else:
                pilha_texto.append(pilha_bck.pop())
                print(f'\nVOLTANDO ÚLTIMO TRECHO APAGADO')
        elif opcao == 'v':
            print(f'\n{pilha_texto}')


editor_texto()
