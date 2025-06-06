from collections import deque

fila_clientes = deque([])
opcao = -1
while opcao != 0:
    print('')
    print('Situação da fila      [1]')
    print('Chegada de um cliente [2]')
    print('Atender um cliente    [3]')
    print('Sair                  [0]')
    opcao = int(input('Opção:                 '))
    
    if opcao == 1:
        print(f'\nSituação da fila: {len(fila_clientes)} pessoa(s) restante(s) na fila')
    elif opcao == 2:
        cliente = input('\nInforme o nome do cliente que chegou agora na fila: ')
        fila_clientes.append(cliente)
        print(f'Cliente {cliente} chegou na fila.')
    elif opcao == 3:
        if len(fila_clientes) == 0:
            print('\nNão há ninguem na fila.')
            continue
        print(f'\nAtendendo o cliente {fila_clientes.popleft()}.')
        print('Cliente atendido.')
    
        