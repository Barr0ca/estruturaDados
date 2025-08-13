from collections import deque


def add(fila: deque, item):
    fila.append(item)
    print(f'Sistema recebeu a requisição {item}.')


def rem(fila: deque):
    if len(fila) <= 0:
        print('Sem requisições a serem processadas no momento.')
    else:
        print(f'A requisição {fila.popleft()} foi processada.')


requisicoes = deque([])

opcao = -1
while opcao != 0:
    print('')
    print('Enviar requisição    [1]')
    print('Processar requisição [2]')
    print('Ordem de requisições [3]')
    print('Sair                 [0]')
    try:
        opcao = int(input('Opção:                '))
    except (ValueError):
        print('\nOpção inválida.\n')

    if opcao == 1:
        item = input('Nome da requisição: ')
        add(requisicoes, item)
    elif opcao == 2:
        rem(requisicoes)
    elif opcao == 3:
        print(requisicoes)
    elif opcao == 0:
        break
