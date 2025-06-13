from collections import deque # Biblioteca para trabalhar com filas

fila_clientes = deque([])

# Abaixo um meno para guiar no processo de entrada e atendimendo de clientes
opcao = -1
while opcao != 0:
    print('')
    print('Situação da fila      [1]')
    print('Chegada de um cliente [2]')
    print('Atender um cliente    [3]')
    print('Sair                  [0]')

    # Verificando entrada do usuário.
    try:
        opcao = int(input('Opção:                 '))
    except ValueError:
        print('\nOpção inválida.')

    if opcao == 1:
        print(f'\nSituação da fila: {len(fila_clientes)} pessoa(s) restante(s) na fila')
        for c in fila_clientes:
            print(f'Resta: {c}')
    elif opcao == 2:
        cliente = input('\nInforme o nome do cliente que chegou agora na fila: ')
        fila_clientes.append(cliente)
        print(f'Cliente {cliente} chegou na fila.')
    elif opcao == 3:
        if len(fila_clientes) == 0: # Caso não tenha ninguem na fila
            print('\nNão há ninguem na fila.')
            continue # Retorna pro loop para o usuário poder continuar as operações

        print(f'\nAtendendo o cliente {fila_clientes.popleft()}.') # Caso tenha alguem na fila, popleft para tira o primeiro elemento da fila.
        print('Cliente atendido.')
    