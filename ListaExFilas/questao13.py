from collections import deque


def add(fila: deque, item):
    if len(fila) >= 5:
        print('Fila está cheia. Máx. 5')
    else:
        fila.append(item)
        print(f'{item} adicionado na lista.')


def rem(fila: deque):
    if len(fila) <= 0:
        print('Fila está vazia.')
    else:
        print(f'{fila.popleft()} removido da fila.')


fila_circular = deque([])

opcao = -1
while opcao != '0':
    print('')
    print('Adicionar na fila   [1]')
    print('Remover da fila     [2]')
    print('Exibir fila         [3]')
    print('Sair                [0]')
    opcao = input('Opção:               ')

    if opcao == '1':
        item = input('Informe oque quer adicionar na fila: ')
        add(fila_circular, item)
    elif opcao == '2':
        rem(fila_circular)
    elif opcao == '3':
        print(fila_circular)
    elif opcao == '0':
        break
    else:
        print('Opção inválida.')
