from collections import deque


def add(fila: deque, item):
    fila.append(item)
    print('Mensagem recebida.')


def rem(fila: deque):
    if len(fila) <= 0:
        print('Você está sem mensagens armazenadas.')
    else:
        print(f"{' '.join(fila.popleft())}")


mensagens = deque([])

opcao = -1
while opcao != 0:
    print('Escrever mensagem               [1]')
    print('Enviar mensagem armazenada      [2]')
    print('Sair                            [0]')
    try:
        opcao = int(input('Opção:                           '))
    except (ValueError):
        print('\nOpção inválida.\n')

    if opcao == 1:
        item = input('Mensagem: ')
        add(mensagens, item)
    elif opcao == 2:
        rem(mensagens)
    elif opcao == 0:
        break
