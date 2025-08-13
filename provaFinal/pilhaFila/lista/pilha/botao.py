def botao():
    pilha_visitadas = [1]
    pilha_navegacao = [1]
    conta_paginas = 1

    opcao = -1
    while opcao != 'x':
        print('-------SITE GENÉRICO--------')
        print(
            f'----------PÁGINA {pilha_navegacao[len(pilha_navegacao)-1]}----------')
        print('VOLTAR:    -')
        print('AVANÇAR:   +')
        print('VISITADOS: *')
        print('SAIR:      x')
        opcao = input('BOTÃO:   ')

        if opcao == '-':
            if len(pilha_navegacao) <= 1:
                print('\nPÁGINA INICIAL\n')
            else:
                pilha_navegacao.pop()
        elif opcao == '+':
            conta_paginas += 1
            pilha_navegacao.append(conta_paginas)
            pilha_visitadas.append(conta_paginas)
        elif opcao == '*':
            print(f'\nPÁGINAS VISITAS {pilha_visitadas}\n')


botao()
