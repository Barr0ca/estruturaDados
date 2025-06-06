def pilha_limitada(pilha: list):
    tam_pilha = len(pilha)
    while tam_pilha < 11:
        tam_pilha = len(pilha)
        print(f'Sua pilha tem {tam_pilha} elementos. Max: 10')
        print('Adicionar elemento [+]')
        print('Retirar elemento   [-]')
        print('Sair               [x]')
        opcao = input('Opção:              ')

        if opcao == '+':
            if tam_pilha >= 10:
                print('A pilha já está cheia.')
                continue

            pilha.append(input('Informe oque deseja adicionar a pilha: '))
        elif opcao == '-':
            if tam_pilha < 1:
                print('A pilha já está vazia.')
                continue
            
            print(f'Removendo o elemendo {pilha.pop()} da lista.')
        elif opcao == 'x':
            break
        else:
            print('Opção inválida.')

pilha = [1,2,3,4,5]

pilha_limitada(pilha)
        
