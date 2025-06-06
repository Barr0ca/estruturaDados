pilha = []
i = 1
while len(pilha) > -1:
    print('Avançar: [ + ]')
    print('Voltar:  [ - ]')
    print('Sair:    [ x ]')
    opcao = input('Opção: ')

    if opcao == '+':
        pilha.append(f'site {i}')
        i += 1
        print(f'Voce está no {pilha[len(pilha)-1]}')
    elif opcao == '-':
        if len(pilha) <= 0:
            print('Não tem como voltar mais.')
            continue
        pilha.pop()
        i -= 1
        if len(pilha) <= 0:
            print('Não tem como voltar mais.')
            continue
        print(f'Voce está no {pilha[len(pilha)-1]}')
    elif opcao == 'x':
        break
    else:
        print('Opção inválida.')